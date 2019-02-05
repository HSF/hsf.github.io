---
title: Optimisation of small matrix operations using Eigen on GPU
layout: gsoc_proposal
project: Patatrack
year: 2019
organization: CERN
---

## Description
Eigen is a high-level C++ library of template headers for linear
algebra, matrix and vector operations, geometrical transformations,
numerical solvers and related algorithms. It is extensively used
within all high energy physics software frameworks. These frameworks
are starting to take advantage of hardware accelerators, like GPUs.
At present, existing GPU-aware libraries are supporting in an
efficient way a single operation on large matrices. The
reconstruction of LHC events, however, involves multiple operations
on many small matrices.

The goal of the project is to optimise small-to-mid size matrix and
vector operations by mapping matrices to groups of GPU threads.

## Task ideas
 * Implement small-size matrix operations with a block of CUDA threads
 * Extend to a CUDA grid
 * Operate on multiple matrices at the same time
 * Evaluate performance

## Expected results
 * High performance small matrix operations on GPUs achieved with low register usage

## Requirements
 * C++, python, CUDA, Eigen

## Mentors
  * [Felice Pantaleo](mailto:Felice.Pantaleo@cern.ch)
  * [Marco Rovere](mailto:Marco.Rovere@cern.ch)
  * [Andrea Bocci](mailto:Andrea.Bocci@cern.ch)

## Links
  * [Eigen](http://eigen.tuxfamily.org/index.php?title=Main_Page)
  * [CUDA](https://developer.nvidia.com/cuda-zone)
