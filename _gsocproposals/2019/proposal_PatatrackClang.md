---
title: Improve support for CUDA in Clang
layout: gsoc_proposal
project: Patatrack
year: 2019
organization: CERN
---

## Description
Clang is a compiler front end for the C, C++, Objective-C and
Objective-C++ programming languages, as well as the OpenMP, OpenCL,
RenderScript and CUDA frameworks. CUDA is a parallel computing
platform and application programming interface model created by
Nvidia. It allows software developers and software engineers to use
a CUDA-enabled graphics processing unit for general purpose
processing. While Clang supports compiling CUDA C++ code in simple
workflows, more work is needed to enable features like separate
compilation and linking.

The goal of this project is to write a front end for Clang that
supports more advanced the CUDA tools.

## Task ideas
 * Implement support for separate compilation and linking
 * Implement support for padding and alignment of data structures.

## Expected results
 * Implementation of a front-end for clang and the relevant CUDA tools in a scripting language (python, etc.)
 * Optionally, integrate the same features in the clang driver itself

## Requirements
 * C++, python, CUDA, Clang, compilers

## Mentors
  * [Felice Pantaleo](mailto:Felice.Pantaleo@cern.ch)
  * [Marco Rovere](mailto:Marco.Rovere@cern.ch)
  * [Andrea Bocci](mailto:Andrea.Bocci@cern.ch)

## Links
  * [Clang](https://clang.llvm.org/)
  * [CUDA](https://developer.nvidia.com/cuda-zone)
