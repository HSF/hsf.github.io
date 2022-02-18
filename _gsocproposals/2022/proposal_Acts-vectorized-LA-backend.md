---
title: Vectorized linear algebra implementation for Acts
layout: gsoc_proposal
project: Acts
year: 2022
organization: CERN
difficulty: medium
duration: 350h
mentor_avail: June-August
---

## Description

Data taking and analyses in high energy physics critically rely on a precise reconstruction of particle trajectories through a detector geometry. Given the amount of data to be processed and the rising combinatorics in future experiments, track finding and fitting tasks need to be implemented as efficiently as possible, making use of state of the art computing hardware. The [ACTS](https://cern.ch/acts) project (A Common Tracking Software) provides highly optimized implementations of tracking algorithms written in C++ that are designed to be integrated into the reconstruction software of high energy physics experiments.

A key role in optimizing performance of tracking software is the deployment of hardware based parallelization, which requires an adaptation of the existing code base to the specific technology in certain places. Making heavy use of linear algebra routines throughout the algorithmic code, and given the inherent parallel nature of such computations, it is expected that ACTS will benefit from the integration of a dedicated parallelized implementation in this area.

CPUs are equipped with inbuilt data vectorization capabilities, a form of parallelization that allows to apply a single instruction to multiple data (SIMD). In order to make use of vectorization, special instructions need to be used and further requirements regarding memory layout need to be observed. Multiple library implementations exist which expose a C++ style API and provide a portable solution to deploy explicitly vectorized code for larger projects.

## Task ideas
We propose the development of a linear algebra plugin for ACTS, which makes use of explicit vectorization.

* Port a similar existing library implementation ([fast5x5](https://gitlab.in2p3.fr/CodeursIntensifs/Fast5x5/)/[xsimd](https://github.com/xtensor-stack/xsimd)) to a suitable library backend (can be decided upon together with the student).
* Adapt the implementation to the linear algebra operations needed in the ACTS numerical integration for particle propagation.
* Validate the approach and its performance and possibly optimize the performance further.
* Given enough time, find a way to make the implementation available to ACTS as a compute backend and run it in ACTS example code.

## Expected results
Working prototype implementation that contains all necessary operations and performance statement

## Requirements
C++, experience with code optimization/performance tools, such as perf or vtune, and vectorization would be an asset

## Mentors
  * **[Joana Niermann](mailto:joana.niermann@cern.ch)** (CERN)
  * [Hadrien Grasland](mailto:hadrien.grasland@ijclab.in2p3.fr) (IJCLab)
  * [Paul Gessinger](mailto:paul.gessinger@cern.ch) (CERN)

## Links
  * [Acts](https://github.com/acts-project/acts)
  * [fast5x5](https://gitlab.in2p3.fr/CodeursIntensifs/Fast5x5/)
  * [xsimd](https://github.com/xtensor-stack/xsimd)
