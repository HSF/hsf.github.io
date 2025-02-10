---
title: Integrate Clad to PyTorch and compare the gradient execution times
layout: gsoc_proposal
project: Clad
year: 2025
difficulty: medium
duration: 350
mentor_avail: June-October
organization:
  - CompRes
---

## Description

PyTorch is a popular machine learning framework that includes its own automatic differentiation engine, while Clad is a Clang plugin for automatic differentiation that performs source-to-source transformation to generate functions capable of computing derivatives at compile time.

This project aims to integrate Clad-generated functions into PyTorch using its C++ API and expose them to a Python workflow. The goal is to compare the execution times of gradients computed by Clad with those computed by PyTorch’s native autograd system. Special attention will be given to CUDA-enabled gradient computations, as PyTorch also offers GPU acceleration capabilities.

## Expected Results

* Incorporate Clad’s API components (such as `clad::array` and `clad::tape`) into PyTorch using its C++ API
* Pass Clad-generated derivative functions to PyTorch and expose them to Python
* Perform benchmarks comparing the execution times and performance of Clad-derived gradients versus PyTorch’s autograd
* Automate the integration process
* Document thoroughly the integration process and the benchmark results and identify potential bottlenecks in Clad’s execution
* Present the work at the relevant meetings and conferences.


## Requirements

* Automatic differentiation
* C++ programming
* Clang frontend

## Mentors
* **[Vassil Vassilev](mailto:vvasilev@cern.ch)**
* [Christina Koutsou](mailto:@christinakoutsou22@gmail.com)

## Links
* [Repo](https://github.com/vgvassilev/clad)
