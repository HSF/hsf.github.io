---
title: Enable the Mesh Memory Allocator in ROOT
layout: gsoc_proposal
project: CMSSW
year: 2020
organization: princeton
---

## Description

*Mesh* is a drop in replacement for *malloc* that compacts the heap without rewriting application pointers. More information can be found [here](https://github.com/plasma-umass/Mesh#readme)

According to the authors of [this paper](https://github.com/plasma-umass/Mesh/raw/master/mesh-pldi19-powers.pdf) using the Mesh allocator reduced the memory consumption of Firefox by 16% and Redis by 39%.


## Task ideas and expected results

The main task is to understand how the Mesh allocator performs in ROOT. We should start with enabling the allocator for ROOT on UNIX using the LD_PRELOAD mechanism. Then we should produce a set of performance measurements and compare them to the baseline ROOT. This can be done in the context of the [Rootbench](https://github.com/root-project/rootbench) infrastructure. We should understand the bottlenecks if any and fix them, reporting to either ROOT or Mesh projects.

The deliverable of the project should be a detailed report and presentation on performance comparison of the Mesh allocator and the standard allocation facilities in ROOT. ROOT’s build system should be extended to handle custom allocators with a switch such as -Dmem_alloc=[default,mesh]. ROOT and *Rootbench* should be extended for the needs of the project.

## Necessary skills

Intermediate C++; understanding how memory allocation works; minimal experience with performance analysis.

## Mentors

  * [Vassil Vassilev](mailto:vvasilev@cern.ch)
  * [Oksana Shadura](mailto:Oksana.Shadura@cern.ch)
