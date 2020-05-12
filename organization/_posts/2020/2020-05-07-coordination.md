---
title: "HSF Weekly Meeting #186, 7 May, 2020"
layout: meetings
---

# {{page.title}}

Present/Contributors: Graeme Stewart, Paolo Calafiura, Serhan Mete, Attila Krasznahorkay, Caterina Doglioni, Jose Benito Gonzalez, Kyle Knoepfel, Efe Yazgan, Eduardo Rodrigues, Paul Laycock, Witek Pokorski, Horst Severini, Michel Jouvin, Andrea Valassi, Stefan Roiser, Agnieszka Dziurda, Ben Morgan, Bernhard Gruber, Chris Jones, Gloria Corti, Liz Sexton-Kennedy, Paolo Calafiura, Pere Mato, Philippe Canal, Sam Meehan, Stefan Roiser, Teng Jian Khoo, Savannah Thais, Andrea Rizzi

## News, general matters

### Letter of support for EuSSI project

Our CERN colleagues (Jose Gonzalez, Tim Smith) asked for a letter of support for their EuSSI proposal, a H2020 call. The project abstract is [here](https://drive.google.com/open?id=18Tua2QiQ9JKi7Vw9Bgdn3lP9qm7ffb5U) and they aim at building a Europe-wide initiative for Research Software with the goal of software becoming a first-class citizen in research. The initiative will provide guidelines for good software sustainability practices and reproducible science and integrate with many of the similar existing local initiatives (NLeSC, SSI, etc.).

This looks very well aligned with the HSF and we have prepared a [draft letter of support](https://docs.google.com/document/d/1Pqc918XiqmrcGuPCZKjgi8QPxqUEZNgVKaaBXZRnq6c/edit?usp=sharing).

Q. What about software standards? What constitutes "well written software"? A. Yes, there is a work package on sustainability and quality. There will be a body that tries to improve this area and also training is a significant work package.

*The meeting approved the letter of support for EuSSI.*

### Repository for Graph-NN Tracking Algorithms and Results

Paolo and Savannah (Exa-TrkX) proposed creating a "project-neutral" repository and website to collect R&D ideas and results on graph algorithms for tracking.

A possibility would be to have a GraphTracking (name TBC) repository under the HSF umbrella. The repository would collect code/results/datasets in areas such as Graph NNs (including trigger apps, and distributed training/inference), metric/similarity learning, clustering/partitioning, and global optimization methods like annealing. Traditional graph algorithms (e.g. min-cut and maxflow) would also be in scope.

Caterina - this is a good idea. How would the HSF repo relate to other repositories? Would need a gatekeeper process (Reco WG coordinators?). Can live side by side with other repos. Can have an open list in the Reco WG page of established connections to different projects. (Technical point, there is a good example of how to host multiple WG pages from the Training WG, which Killian authored.)

Is this then *maintained* by the HSF? Specific instructions (e.g. Conda instructions) and limited support. What about code that gets abandoned later? At least the price of entry should be working CI (Travis, GitHub Actions). Everyone that contributes would be expected to maintain their piece.

Meeting agreed that we should proceed with this by *baby steps*, starting with the Exa-TrkX material from Savannah.

### Snowmass Process

Some of us met with the [Snowmass Computing Frontier](https://snowmass21.org/computational/) (CF) convenors (Oli, Ben, Steve) on Monday. We discussed how the HSF contributed to the EPPSU and what we could do in Snowmass. Seven working groups are being formed who will look at particular topics.

Existing HSF documents (e.g. LHCC input) are welcome already as a submission, no need to pay too much heed to formal dates or LoIs, we are asked to submit as soon as possible.
- Happy to contribute the Common Tools and Community Software paper, after any tweaks from LHCC feedback
    - And the generators document as well
- HSF would also like to say more about other experiments and facilities (e.g. Intensity Frontier)
    - FNAL would like to collaborate on that as well, happy to work in HSF context

Call for CF working group members will be open and an international flavour is encouraged (there will be smaller writing teams, but the WGs can be quite large).
- Presentation about the CF and WGs in HSF meeting is foreseen
    - As well as any other WLCG/HSF meetings
- Advertise on HSF Forum list too

## Google Summer of Code 2020

36 student projects got slots. Now in Community Bonding period, until end of the month. A meeting with the students will be announced closer to the beginning of the coding period. The TODO for this period was sent to the mentors, to be followed by another regarding the Coding Period at the end of the month.

## Google Season of Docs 2020

3 project proposals (AllPix2, Rucio, ROOT). Waiting for the announcement of Google of the accepted Orgs (May 11). The program targets starting effectively the technical writer projects on Sep 14, but the interaction mentors-potential writers starts as soon as projects get contacted, second half of May.

## LHCC Review of HL-LHC Software and Computing

The HSF Common Tools and Community Software document was submitted on time for the review. It is also published on [Zenodo](https://zenodo.org/record/3779250). Some light updating can happen if people spot mistakes or new references are to be added (we know of a few). Please make a PR against the HSF Documents repository: <https://github.com/HSF/documents>.

*Many thanks to all who made that happen!*

### Other Documents

In addition to the HSF document our [generators group](https://arxiv.org/abs/2004.13687) and the [ROOT team](https://arxiv.org/abs/2004.07675) provided additional input.

The WLCG and DOMA documents are public (will go on the WLCG website soon).

As far as we understand ATLAS and CMS foresee making their documents public after the review.

### Review Process

About 5 people per paper can attend the review. We will send Graeme and Liz from HSF Coordination, plus one person per WG: Andrea for Generators; Gloria for Simulation; Caterina for Reconstruction; Paul for Analysis.

Review is Tuesday 19 May, with a feedback session on Wednesday 20 May.

## Discussion on Multi-Threading

We organised a [meeting yesterday](https://indico.cern.ch/event/915659/) prompted by Intel [deprecating](https://github.com/oneapi-src/oneTBB/issues/243) their low-level `tbb::task` API. Goals were to assess the state of thread management in each framework and project, as well as to ensure we remain coherent going forwards (it's important that each piece of the full HEP application uses threads coherently).

Very useful summary of status and plans. Main conclusions:

1. First choice migration strategy is to use `task_group` / `task_arena` - all in the TBB universe. Work so far is promising.
1. Option to have an arena per toolkit is worth exploring. Can then set individual limits per arena that would give a nice way to control threading in the more complex cases (e.g. Framework + Geant4 + ROOT).
1. HPX is a more long term project, but useful R&D as it is close to how we expect the C++ standard to evolve. Not for Run 3.

Follow-up in the HSF Frameworks Group.

## Working Group Updates

### Data Analysis

- Need to decide on dates for next meetings, particularly the analysis languages workshop.

### Detector Simulation

- We are targeting a working group meeting on 27th May or 3rd June. Currently discussing which topic we want to focus on. In addition to the list of topics we had penciled in we are considering those that were to be addressed in the original Lund workshop.


### Reconstruction and Software Triggers

- Meetings for the foreseeable future: connect to LHCC document topics
    - June: GPU in trigger
    - July or August: Tracking algorithms exploiting timing information 
[Note: take one of the two months as “vacation”] 
    - September: reconstruction algorithms in experiments connected to LHC
    - October: ML inference in trigger 
    - November: particle flow commissioning up to Run-3 

- Common trigger&reco page updates:
    - As discussed, would like to add links and descriptions for projects that have been added to the LHCC document [[link to text](https://docs.google.com/document/d/10D5Lf7NWfd5FvS9OJzcNPw_t1xbEn5gXRZoDCTk8QEs/edit#heading=h.penorw1ehh1k)]
    - How to distinguish what is endorsed and hosted by HSF, if any? See discussion above

### PyHEP
- We want to finalise the preparations for the workshop but things have been moving more slowly than usual, understandably.
- Our community got 3 talks and one poster at SciPy 2020, and this strong presence is excellent news.
    - Standard registration for the whole conference is now just $75 ($25 for students)! Do consider attending.

### Software Tools and Packaging

* Ben Morgan gave a nice presentation on Spack at the pre-GDB meeting on May 5th ([slides](https://indico.cern.ch/event/813800/contributions/3830178/attachments/2031805/3400697/SpackGDBMeeting_1.pdf)).
    * Perhaps it'll be beneficial to have a meeting to discuss the latest developments on the packaging/Spack side. In particular, it would be nice to review the recent developments, survey the missing packages that we want to see in the Spack repository etc. This was also brought up [previously](https://hepsoftwarefoundation.org/organization/2020/03/26/coordination.html) and the suggestion was to collect LCG release contents as a start.
    * News from [Key4hep project](https://indico.cern.ch/event/912631/): Valentin now has the whole Key4hep stack building in Spack (not bootstrapping from LCG release).
* On the tools side we're going to be adding an optional GPU monitoring support to `prmon` (see issue [#105](https://github.com/HSF/prmon/issues/105)). The main idea is to initially support NVidia and use `nvidia-smi` for collection. Then extend it to support other hardware as well.


### Software Training

- Will organise virtual training soon. Recorded talks, with small group work a few days after.

### Event generators
* Updating the generator paper. Will submit to the journal next week (still waiting for some comments).
    * Also plan to contribute the paper to the Snowmass process.
* Started discussion with Andy Buckley on collaboration between the HSF and UK "Efficient Computing in HEP" generators projects. Will schedule a discussion at an upcoming WG meeting. 

### Frameworks
* In our next meeting we plan to cover ATLAS's multi-threaded scheduling strategy. We are still working with the authors to find a possible time.
* Plan to continue (technical) discussions about the removal of the [tbb::task](https://software.intel.com/en-us/node/506299) API in dedicated meetings of the WG.
* Now mainly working on the material for next week's Virtual Workshop.

---

## Workshops

### New Architectures, Portability, and Sustainability

[HSF WLCG Virtual Workshop on New Architectures, Portability, and Sustainability](https://indico.cern.ch/event/908146/) is next week.
* Timetable finalised with speakers known.

**We ask that people [register](https://indico.cern.ch/event/908146/registrations/)** so that we can gauge the level of interest and best organisation options.

### PyHEP 2020 Workshop

[Virtual Workshop](https://indico.cern.ch/e/pyhep2020).

## AOB

### Next Meeting

- Next regular meeting slot is 21 May, *however this is the Ascension holiday in many European countries (and at CERN)* so no meeting.
    - *We decided to have a meeting on 28 May, but dedicated to feedback from the LHCC review*.
    - Then next regular meeting will be 4 June
