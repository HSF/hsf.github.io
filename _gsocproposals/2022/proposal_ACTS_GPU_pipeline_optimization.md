---
title: Acts GPU R&D - Optimization of GPU tracking pipeline
layout: gsoc_proposal
project: Acts
year: 2022
difficulty: high
duration: 175
mentor_avail: June-August
organization:
  - LBNL
---

## Description

A Common Tracking Software ([Acts][Acts]) is a general tracking software toolkit for High Energy Physics experiments. 
The Acts collaboration has launched several R&D lines ([vecmem][vecmem], [detray][detray], and [traccc][traccc]) 
for GPU acceleration by parallelizing the track reconstruction. vecmem is a memory management toolkit which provides 
users with convenient GPU interface. detray is a geometry builder which translates the CPU geometry into GPU one. 
traccc incorporates the other R&D lines to demonstrate GPU tracking pipeline which includes hit clusterization, 
seed finding, and Kalman filtering. 

The goal of project will be the acceleration of [traccc][traccc] GPU pipeline with CUDA API. The performance can be optimized 
by (1) selecting a proper caching allocator and (2) realizing multi-threaded environment with CUDA-MPS or Multi-Instance GPU (MIG).

## Task Ideas

* Benchmarking downstream caching allocators provided by [vecmem][vecmem] for [traccc][traccc] algorithms
* Benchmarking the unified memory and device memory for CUDA memory allocation
* Application of CUDA-MPS and MIG to the pipeline

## Expected Results

We are expected to observe the actual acceleration of GPU pipeline, especially for CUDA API. 
The student is expected to create proper benchmark codes to demonstrate the performance.

## Evaluation Task

Interested students can contact mentor for evaluation task.
It is also possible to submit past projects on GPU (e.g. github link)

## Requirements

 * Strong C++ skills
 * Experience with GPU APIs (CUDA, SYCL, etc.)
 * Linux, Git, and Shell scripting

## Mentors

 * **[Beomki Yeo](mailto:beomki.yeo@berkeley.edu)** (LBNL)

## Links

 * [Acts repository][Acts]
 * [GPU tracking demonstrator][traccc]
 * [GPU geometry builder][detray]
 * [GPU memory management tool][vecmem]

[Acts]: https://acts.readthedocs.io/en/latest/#
[traccc]: https://github.com/acts-project/traccc
[detray]: https://github.com/acts-project/detray
[vecmem]: https://github.com/acts-project/vecmem