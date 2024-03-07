---
title: Implement Differentiating of the Kokkos Framework
layout: gsoc_proposal
project: Clad
year: 2024
difficulty: medium
duration: 350
mentor_avail: June-October
organization:
  - CompRes
---

## Description

In mathematics and computer algebra, automatic differentiation (AD) is a set of
techniques to numerically evaluate the derivative of a function specified by a
computer program. Automatic differentiation is an alternative technique to
Symbolic differentiation and Numerical differentiation (the method of finite
differences). Clad is based on Clang which provides the necessary facilities for
code transformation. The AD library can differentiate non-trivial functions, to
find a partial derivative for trivial cases and has good unit test coverage.

The Kokkos C++ Performance Portability Ecosystem is a production level solution
for writing modern C++ applications in a hardware agnostic way. It is part of
the US Department of Energies Exascale Project – the leading effort in the US to
prepare the HPC community for the next generation of super computing
platforms. The Ecosystem consists of multiple libraries addressing the primary
concerns for developing and maintaining applications in a portable way. The
three main components are the Kokkos Core Programming Model, the Kokkos Kernels
Math Libraries and the Kokkos Profiling and Debugging Tools.

The Kokkos framework is used in several domains including climate modeling where
gradients are important part of the simulation process. This project aims at
teaching Clad to differentiate Kokkos entities in a performance portable way.

## Expected Results

* Implement common test cases for Kokkos in Clad
* Add support for Kokkos functors
* Add support for Kokkos lambdas
* Incorporate the changes from the [initial Kokkos PR](https://github.com/vgvassilev/clad/pull/783).
* Enhance existing benchmarks demonstrating effectiveness of Clad for Kokkos
* [Stretch goal] Performance benchmarks


## Requirements

* Automatic differentiation
* C++ programming
* Clang frontend

## Mentors
* **[Vaibhav Thakkar](mailto:vaibhav.thakkar@cern.ch)**
* [Petro Zarytskyi](mailto:petro.zarytskyi@gmail.com)
* [Vassil Vassilev](mailto:vvasilev@cern.ch)

## Links
* [Repo](https://github.com/vgvassilev/clad)
* [Kokkos](https://kokkos.org/)
* [Initial Kokkos PR](https://github.com/vgvassilev/clad/pull/783)
