---
title: Extend clad to compute Jacobians
layout: gsoc_proposal
project: IRIS-HEP
year: 2020
organization: princeton
---

## Description

In mathematics and computer algebra, automatic differentiation (AD) is a set of techniques to numerically evaluate the derivative of a function specified by a computer program. Automatic differentiation is an alternative technique to Symbolic differentiation and Numerical differentiation (the method of finite differences). CLAD is based on Clang which will provide the necessary facilities for code transformation. The AD library is able to differentiate non-trivial functions, to find a partial derivative for trivial cases and has good unit test coverage.

Currently, clad does not provide an easy way to compute Jacobians.

## Task ideas and expected results

Implement Jacobian computation interface (similar to clad::hessian) in clad. The implementation should be very well-tested and documented. The student should be prepared to write a progress report and present the results at the end of the summer.

More detailed information about the project and applicant guidelines are available in the [clad GSoC 2020](https://github.com/vgvassilev/clad/wiki/GSoC-2020) page.

## Necessary skills

Intermediate C++; Understanding clad; Understanding of Clang and its API.

## Mentors

  * [Vassil Vassilev](mailto:vvasilev@cern.ch)
  * [Alexander Penev](mailto:alexander_penev@yahoo.com)

## Links

  * [clad GitHub repository](https://github.com/vgvassilev/clad)
  * [clang](http://clang.llvm.org)
