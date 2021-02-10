---
title: Awkward Array GPU kernels
layout: gsoc_proposal
project: IRIS-HEP
year: 2020
organization: princeton
---

## Description

The [Awkward Array](https://github.com/scikit-hep/awkward-array#readme) library provides a NumPy-like interface to the nested and unequal-length datasets that are often required by particle physicists. Since its release in September 2018, it has been used in a variety of particle physics analyses. In late 2019/early 2020, it was [rewritten in C++ as Awkward 1.x](https://github.com/scikit-hep/awkward-1.0#readme), and the transition from Awkward 0.x to Awkward 1.x is ongoing.

Since Awkward Array encourages array-at-a-time programming, analysis scripts that use it are already in a good position to take advantage of GPUs. Algorithms designed for GPUs also operate array-at-a-time because this permits threads to run independently and thus achieve better performance. Awkward 1.x's C++ implementation provides a good starting point for adding GPU kernels in CUDA and/or OpenCL.

The goal of this project is to add a GPU backend to Awkward Array 1.x. With such a backend, the library would have a unique capability of processing complex, JSON-like data that is wholly resident on GPUs, in an efficient way, without specialized compilation or even leaving the Python prompt.

## Task ideas

   * Track "memory location" through Awkward Array classes: main memory versus GPU (and which GPU). Arrays derived from GPU arrays should live on the same GPU, and operations involving a CPU array and a GPU array should be handled intelligently.
   * Characterize the "CPU kernels" in a way that documents them and facilitates bulk translation to "GPU kernels." Maybe create a tool that performs a naive translation for most existing and any new CPU kernels.
   * Identify kernels whose naive translations are already optimal on GPUs and those that can be improved by GPU-specific algorithms. For example, some kernels are prefix sums, implemented on the CPU by a loop-carried dependency, which can be dramatically improved by a [Hillis-Steele prefix sum](https://en.wikipedia.org/wiki/Prefix_sum#Algorithm_1:_Shorter_span,_more_parallel) on the GPU. Other examples may be evident.
   * Develop a deployment strategy for users with GPUs and users without GPUs (and users with non-Nvidia GPUs). CUDA and OpenCL should be actively compared.
   * Measure performance of array operations with and without a GPU, including memory transfer time.

## Expected results

By the end of the summer, we would like to see a complete implementation of Awkward Array GPU kernels. It should be reasonably performant, though it need not have the best possible performance.

## Evaluation tasks

Contact the mentors for a task that we'll use to evaluate candidates.

## Requirements

   * Good software engineering skills; well-organized coding.
   * Rigorous testing and documentation.
   * Familiarity with CUDA and/or OpenCL and C++.
   * Interest in parallel algorithms.

## Mentor

  * [Jim Pivarski](mailto:pivarski@princeton.edu)
  * [David Lange](mailto:david.lange@cern.ch)
