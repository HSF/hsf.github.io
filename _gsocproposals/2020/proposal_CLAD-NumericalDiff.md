---
title: Add numerical differentiation support in clad
layout: gsoc_proposal
project: IRIS-HEP
year: 2020
organization: princeton
---

## Description

In mathematics and computer algebra, automatic differentiation (AD) is a set of techniques to numerically evaluate the derivative of a function specified by a computer program. Automatic differentiation is an alternative technique to Symbolic differentiation and Numerical differentiation (the method of finite differences). CLAD is based on Clang which will provide the necessary facilities for code transformation. The AD library is able to differentiate non-trivial functions, to find a partial derivative for trivial cases and has good unit test coverage.

Currently, clad cannot differentiate declared-but-not-defined functions. In that case it issues an error. Instead, clad should fall back to its future numerical differentiation facilities.

## Task ideas and expected results

Implement numerical differentiation support in clad. It should be available through a dedicated interface (for example clad::num_differentiate). The new functionality should be connected to the forward mode automatic differentiation. If time permits, a prototype of configurable error estimation for the numerical differentiation should be implemented. The student should be prepared to write a progress report and present the results at the end of the summer.

More detailed information about the project and applicant guidelines are available in the [clad GSoC 2020](https://github.com/vgvassilev/clad/wiki/GSoC-2020) page.

## Necessary skills

Intermediate C++; Understanding numerical differentiation; Understanding of Clang and its API.

## Mentors

  * [Vassil Vassilev](mailto:vvasilev@cern.ch)
  * [Alexander Penev](mailto:alexander_penev@yahoo.com)

## Links

  * [clad GitHub repository](https://github.com/vgvassilev/clad)
  * [clang](http://clang.llvm.org)
