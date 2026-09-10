---
project: DUNE
title: "Fine grained storage for the DUNE experiment"
author: Ahmed Idani
photo: blog_authors/AhmedIdani.jpeg
date: 24.08.2026
year: 2026
layout: blog_post
logo: DUNE-logo.png
intro: |
  DUNE is building a new data processing framework, Phlex, whose I/O layer FORM lets each pipeline stage write its own data product into its own container without waiting for anyone else. That makes writing cheap, but it moves the cost onto the reader: someone who needs several products of the same event can follow only one of them in its natural order and has to read the rest out of order. I spent the summer building a benchmark on ROOT's RNTuple to find out what that actually costs. Short version: you pay in decompression, not in disk, and the size of the bill is set by how many events share a page. At one event per page the read order is free. At four thousand, the same bytes cost 48 times as much.
---

|              |                                                                                                                          |
| ------------ | ------------------------------------------------------------------------------------------------------------------------ |
| Name         | [Ahmed Idani](https://github.com/Ahmed-Idani)                                                                            |
| Organization | [CERN-HSF](https://hepsoftwarefoundation.org/activities/gsoc.html), [Argonne National Laboratory](https://www.anl.gov/)  |
| Mentors      | [Wanwei Wu](https://www.anl.gov/profile/wanwei-wu), [Peter Van Gemmeren](https://www.anl.gov/profile/peter-van-gemmeren) |
| Project      | [Fine grained storage for the DUNE experiment](https://hepsoftwarefoundation.org/gsoc/2026/proposal_DUNE_FORM.html)      |
{: .table}

## Important Links

- **Project proposal:** [Fine grained storage for the DUNE experiment](https://hepsoftwarefoundation.org/gsoc/2026/proposal_DUNE_FORM.html)
- **Project repository:** [wwuoneway/fine-grained-storage](https://github.com/wwuoneway/fine-grained-storage/tree/gsoc-2026-final)
- **Final work report** (the long version, with every figure, table and configuration file): [GSoC 2026 Final Work Report](https://gist.github.com/Ahmed-Idani/2a9d3bdc4b03b0e3d0cf4da4e82c258f)

## The problem

[DUNE](https://www.dunescience.org/) is a neutrino experiment. Its scale creates a computing problem: PB-scale datasets, GB-scale event objects, and a lot of different workflows that all want different slices of the same detector data. At that scale the traditional way of processing physics data, one whole event at a time, starts to get in the way.

So the experiment is building [Phlex](https://github.com/Framework-R-D/phlex), a framework that works with fine grained data instead. Its I/O layer, [FORM](https://indico.fnal.gov/event/72820/contributions/341330/attachments/199633/278226/FORM_DUNE_DPF2026.pdf), lets each stage of the pipeline write its own data product into its own container, eagerly, without synchronising with the other writers.

Writing that way is easy. Reading is where it gets interesting.

Say two stages are writing `Hit` and `Track` into two containers at the same time, and nobody is keeping them in step. Then the row an event occupies in one container has nothing to do with the row it occupies in the other. Event 5 can be row 5 in `Hit` and row 900 in `Track`. Now a reader comes along and wants both products of the same event. It can follow one container in its cheap, natural order, front to back. The other one it has to jump around in.

That is the whole question of this project, and it is narrow enough to measure:

> On [RNTuple](https://root.cern/doc/master/group__NTuple.html), the columnar format DUNE is moving to, how much does it cost to read a data product out of its storage order? Where does that cost go, and what decides how big it is?

One detail of RNTuple's design ends up deciding the entire answer, so it is worth putting on the table now. RNTuple does not store rows. It stores each field as its own column, cuts each column into **pages**, and compresses every page as a single unit. That makes a page the smallest thing you can read: ask for one row and you decompress the whole page it happens to sit in. Keep an eye on how many events fit into one page, because everything below comes back to that number.

## What I built

The temptation at the start was to reproduce FORM. I am glad my mentors talked me out of it. What I built instead is a standalone benchmark suite whose only dependency is ROOT: it links neither Phlex nor FORM, and it does not reimplement them. It just rebuilds the smallest system that still has the same problem, which is each data product living in its own container, in its own order on disk, reachable at read time only through an index.

FORM's vocabulary maps onto it directly:

| FORM concept | This benchmark                                                 |
| ------------ | -------------------------------------------------------------- |
| Container    | one RNTuple per data product, all sharing one `.root` file     |
| Technology   | RNTuple, the format under study                                |
| Index        | a TTree on disk, mapping `event_id` to each product's Token    |
| Token        | `{container, entry}`, naming the row a product's data lives at |
| Data product | `position` and `momentum`, one of each per particle            |
{: .table .table-bordered}

It runs in three phases, all driven from one configuration file.

**1. Generate.** An event here is one simulated collision holding some number of particles, and a particle is described by two things, where it is and how it is moving:

```cpp
struct Position { float x, y, z; };     // where the particle is
struct Momentum { float px, py, pz; };  // how it is moving
```

Those two structs are the benchmark's data products. Every event carries a vector of each, both the same length, so particle `i` of an event is the pair `(positions[i], momenta[i])`. The particle count may vary from event to event, though for every dataset in this post I hold it fixed, so that bytes per event is a knob I set rather than a distribution I have to argue about. Everything is drawn from a single seeded `mt19937_64` and written to plain binary files, so any dataset can be regenerated exactly. Positions are uniform over a detector-shaped box, momentum components are Gaussian, and any triplet below a minimum magnitude is redrawn.

> These distributions are not a physics simulation and are not meant to reproduce DUNE data. What this study needs from the data is its _shape_: bytes per event, and how many events share a page. That is set by the particle count and the struct layout, not by the values themselves.

**2. Write.** Each product goes into its own RNTuple, and one row is one whole event. But RNTuple does not keep a row together on disk: every field becomes its own column. So a container declares two fields, the `event_id` and the particle vector, and RNTuple ends up storing five columns for it: `event_id`, an offsets column recording where each event's particles begin, and one `float` column each for `px`, `py` and `pz`. Those last three carry essentially all of the bytes, which is why the rest of this post calls them the **payload columns**. Alongside the containers goes the index TTree that says which row holds which event.

**3. Read.** Read it all back with the stopwatch running, splitting the wall time into storage I/O and decompression using ROOT's own per-container counters, and recording bytes fetched, bytes decompressed, pages fetched and pages unzipped.

### Turning disorder into a knob

Reading a file sequentially, then randomly, and comparing gives you two points and no explanation. So I made disorder adjustable instead: start from the sequential order, walk it once, and swap each position with another no further than `distance` away. It only ever swaps, so the result is still a permutation: every event is read exactly once, and only the order changes. Two endpoints become a curve.

I also simulate the container mismatch on the read side rather than the write side. Files are written in plain event order and the reader jumps around instead. It is the same experiment seen from the other end, the same pages in the same sequence for the same cost, but far cheaper to run: the visit order is a seeded list I can change between cases, while concurrent writers would leave a different layout behind on every run.

### Getting the machine out of the way

My first numbers measured the Linux scheduler more than they measured RNTuple. This is a hybrid CPU, so an unpinned case would land on a performance core in one repetition and an efficiency core in the next, an effect bigger than most of the knobs I was trying to study.

So everything below runs pinned to isolated cores, one CPU per physical core so the reader and ROOT's I/O thread never end up sharing execution units, with the frequency governor locked to `performance` and ASLR off. The page cache is also dropped before every repetition, with `posix_fadvise(POSIX_FADV_DONTNEED)`, which needs no root and touches only my own files.

That last one has a trap in it that cost me a while. `DONTNEED` only drops **clean** pages, and a file I had just written in the write phase was still full of dirty ones, so it stayed comfortably cached and my "cold" runs were not cold at all. The fix is a `sync` first, to push those pages out so the kernel is allowed to drop them.

## What I found

I ran two studies, 110 measured cases between them. Every dataset holds the same 104,857,600 particles, about 1,200 MiB of raw momentum, just cut into different numbers of events. So the payload never changes. The only thing that changes is how many events end up sharing a page. Write settings are [ROOT's defaults](https://root.cern.ch/doc/master/classROOT_1_1RNTupleWriteOptions.html) throughout: zstd level 5, 1 MiB maximum page.

### Study one: the disk keeps up, the decompressor does not

Four datasets, from one event per page up to about four thousand. Ten access patterns each: sequential, then scatter at distance 1, 2, 4, all the way to 256. Cold cache, and the cluster cache deliberately **off**. That last one is ROOT's read-ahead: RNTuple groups pages into clusters, and with the cluster cache on it fetches and unpacks a whole cluster on a background thread before you ask for it. Switching it off means no read-ahead, so every page is fetched only when the reader actually asks for it, and the time it takes stays on the critical path where I can measure it. ROOT's implicit multithreading is off as well, in both studies, so every number below is single-threaded decompression.

<p align="center" style="margin: 2.5rem 0;">
<img src="https://raw.githubusercontent.com/Ahmed-Idani/gsoc-2026-report-assets/refs/heads/main/bottleneck-line-style/image.png" alt="Read wall-time decomposition against scatter distance" width="760" style="max-width:100%">
<br>
<em style="display:inline-block; max-width:760px; margin-top:0.9rem; font-size:0.9em; line-height:1.5; color:#666;"><strong>Figure 1.</strong> Where the read wall time goes, against scatter distance, all four panels on one scale. Decompression reproduces the shape of the total. I/O and everything else stay flat against the axis.</em>
</p>

All four datasets hold the same particles, so whatever separates those curves has nothing to do with how much data there is. Here is the widest case, scatter distance 256, measured against the same dataset read sequentially:

<div class="table-responsive" markdown="1">

| Dataset                          | Events per page | Storage time | Decompression time | Wall time |
| -------------------------------- | --------------: | -----------: | -----------------: | --------: |
| 262,144 particles x 400 events   |               1 |        1.05x |              0.99x | **1.00x** |
| 65,536 particles x 1,600 events  |               4 |        1.45x |              3.56x | **1.82x** |
| 1,024 particles x 102,400 events |             256 |        15.8x |               151x | **41.8x** |
| 64 particles x 1,638,400 events  |           4,096 |        15.4x |               186x | **48.0x** |
{: .table .table-bordered}

</div>

Look at the first row. At one event per page, reading in a scattered order costs **nothing**: 1.00x, indistinguishable from reading the file front to back. Pack more events into a page and the cost fans out, until the finest dataset, the one cut into the most and therefore the smallest events, is paying 48x to visit exactly the same bytes in a different order. The bill is set by the size of an event against the size of a page, not by the size of the payload.

Now look at the last two columns. Storage time does climb, about fifteen times over on the two finest datasets, so I/O is not free. But decompression climbs an order of magnitude harder, and it is what the total follows. On the finest dataset at distance 256, 177 seconds of a 193 second read is decompression, against 13 seconds of actual I/O.

So the read is not I/O bound. And "CPU bound" is too vague: it is **decompression bound**, specifically. What makes that convincing is that I measured it under the conditions most likely to make storage look expensive, with no read-ahead and a cache dropped before every repetition. If the disk were the limit, that is where it would have shown, and it did not.

**Why does it happen?** A column holds the page it is currently sitting on, and nothing else. Walk off that page and the decompressed buffer is gone; come back later and you fetch it and decompress all of it again. The two costs then part ways, because the second _read_ is usually served by the OS file cache, which still has those bytes lying around from the first visit. Decompression has no equivalent cache. Once the buffer is dropped, the CPU pays for it again in full, every single time. That is why I/O flattens out while decompression keeps climbing.

### Study two: the multiplier is the number of events sharing a page

That explanation makes a prediction I could go and check. If a page gets decompressed once per visit, then a page can never be decompressed more times than it has events on it. Which means **the number of events sharing a page is a ceiling on how much you can waste**.

Study two goes looking for that ceiling: seven datasets, from 1 event per page up to 4,045, same ten access patterns, this time counting bytes and pages instead of timing them.

Events per page is a property of a column rather than of a file, so I measured it instead of assuming it. [A small ROOT macro](https://github.com/wwuoneway/fine-grained-storage/blob/gsoc-2026-final/scripts/inspect_columns.C) prints ROOT's own page counts per column. On the 409,600-event dataset, the three payload columns (`px`, `py`, `pz`) carry 1,017 MiB of compressed bytes between them, against 6 KiB in the `event_id` and offsets columns, and each cuts its 104,857,600 floats into 404 pages. That is 409,600 / 404, or about 1,014 events per page.

<p align="center" style="margin: 2.5rem 0;">
<img src="https://raw.githubusercontent.com/Ahmed-Idani/gsoc-2026-report-assets/refs/heads/main/study-2/read_cost/scatter_distance/read_cost_vs_scatter_distance__pg1mib__no-shuffle__decomp_amplification.png" alt="Decompressed over read bytes, against scatter distance" width="700" style="max-width:100%">
<br>
<em style="display:inline-block; max-width:700px; margin-top:0.9rem; font-size:0.9em; line-height:1.5; color:#666;"><strong>Figure 2.</strong> Bytes out of the decompressor for every byte the read actually asked for. Every dataset starts on the same line, then bends off it and flattens at a ceiling set by its own events per page.</em>
</p>

The prediction holds up. Every dataset starts on the same line, with the amplification growing in proportion to the scatter distance. Then each curve peels off that line and flattens, and the fewer events share a page, the sooner it peels off. The level each one settles at is close to that dataset's events per page, exactly as the page mechanism says it should be. And the 1 event per page curve never climbs at all. It sits flat at 1.0 from end to end: nothing is shared, so the read order simply stops mattering.

Study two runs with the cluster cache **on**, unlike study one, which is safe here because it counts bytes and pages rather than timing them, and those counts do not care about read-ahead. Study one's four datasets are among study two's seven, so the two studies share 40 cases, and on those the counts come out identical either way. That cross-check is what lets the two studies be read together.

## What this means for DUNE

For any given data product, the question is **its bytes per event against the page size**.

- If a product is big enough that one event fills a page or more, it is in the safe regime. An event can still straddle a boundary and share a page with its neighbour, but only with one neighbour, so reading it out of order costs almost nothing. `Wire`, the raw digitised waveforms off the detector's readout channels, looks like this: it is one of the biggest things DUNE writes per event.
- Smaller and higher-level products are in the other regime, where one page holds many events and collecting them out of order means decompressing the same page over and over for one event's worth of use. `Track`, a reconstructed particle trajectory and so a summary of the raw data rather than the raw data itself, is the candidate here.


## Acknowledgments

My thanks to my mentors, [Wanwei Wu](https://www.anl.gov/profile/wanwei-wu) and [Peter Van Gemmeren](https://www.anl.gov/profile/peter-van-gemmeren), who gave me a great deal of their time and kept steering the work back towards the questions worth answering. [Andrew Olivier](https://www.anl.gov/profile/andrew-olivier) pointed me at the parts of ROOT and RNTuple that turned out to matter here, and reviewed the work along the way.

Thanks also to CERN-HSF for hosting the project, and to Google Summer of Code for making it possible.

I hope DUNE goes on to do what it set out to do, and that this small piece of work is of some use along the way.
