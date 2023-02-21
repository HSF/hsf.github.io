---
title: Acts GPU R&D - Optimization of GPU tracking pipeline
layout: gsoc_proposal
project: Acts
year: 2022
difficulty: high
duration: 350
mentor_avail: June-August
organization:
  - LBNL
---

## Description

A Common Tracking Software ([Acts][Acts]) is a general track reconstruction software toolkit for High Energy Physics experiments. In the upcoming High luminosity LHC experiments, the large number of particle interactions will significantly increase the track reconstruction time on CPUs. Therefore, the Acts collaboration has launched several GPU R&D lines ([vecmem][vecmem], [detray][detray], and [traccc][traccc]) 
to accelerate the track reconstruction: [vecmem][vecmem] is a memory management toolkit which provides 
users with convenient GPU interface. [detray][detray] is a geometry builder which translates the CPU geometry into GPU one. 
[traccc][traccc] incorporates the other R&D lines to demonstrate GPU tracking pipeline which includes hit clusterization, 
seed finding, and track fitting. 

The goal of project will be the optimization of traccc GPU pipeline with CUDA API. The track reconstruction algorithms can be improved by multi-threading with CUDA-MPS and partitioning the GPU device with Multi-Instance GPU (MIG). The caching of event data model (EDM), which contains information on event, is also critical to the throughput. Their memory access or allocation in the GPU device can be optimized by using a proper caching allocator provided by vecmem. 

## Expected Results

* Investigate how the throughput scales up with the number of threads used in CUDA-MPS.
* Applying MIG to the GPU pipeline with the high-end NVIDIA GPUs (A30 and A100).
* Understand how the vecmem caching works in GPU and find the best caching allocator for EDM.
* Create benchmark codes for each tracking algorithm (hit clusterization, seed finding, and track fitting) to demonstrate the improvements from the above works

## Evaluation Task

Interested students can contact mentor for evaluation task.
It is also possible to submit past projects on GPU (e.g. github link)

## Requirements

 * Strong C++ skills
 * Linux, Git, and Shell
 * Experience with any of GPU APIs (CUDA, SYCL, etc.) will be advantageous

## Mentors

 * **[Beomki Yeo](mailto:beomki.yeo@berkeley.edu)** (LBNL)
 * [Charles Leggett](mailto:cgleggett@lbl.gov) (LBNL)

## Links

 * [Acts repository][Acts]
 * [GPU tracking demonstrator][traccc]
 * [GPU geometry builder][detray]
 * [GPU memory management tool][vecmem]

[Acts]: https://acts.readthedocs.io/en/latest/#
[traccc]: https://github.com/acts-project/traccc
[detray]: https://github.com/acts-project/detray
[vecmem]: https://github.com/acts-project/vecmem
