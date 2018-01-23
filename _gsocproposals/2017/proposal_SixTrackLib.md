---
title: Optimize and Integrate Standalone Tracking Library (SixTrackLib)
layout: gsoc_proposal
project: SixTrack
year: 2017
organization: CERN
---

## Project Description
Optimize data structure and source code of a standalone tracking library in C
in order to take advantage of automatic vectorization offered by GCC and CLang
for CPU and explicit vectorization from OpenCL and CUDA for GPU. The code must
then be linked with the legacy SixTrack code and replace the inner loop.

## Expected results 
Demonstrate that the C code can run existing simulation at the same or faster
speed on CPU and can saturate the computing capacity of GPU, while keeping
bit-level identical results.

## Mentors

  * [Riccardo De Maria](mailto:Riccardo.De.Maria@cern.ch)
  * [Giovanni Iadarola](mailto:giovanni.iadarola@cern.ch)

## Requirements
Experience with Fortran, C, OpenCL, CUDA, vectorization techniques.

## Web Page
[cern.ch/sixtrack](http://cern.ch/sixtrack)

## Source Code 
[github.com/SixTrack/SixTrack](http://github.com/SixTrack/SixTrack)
