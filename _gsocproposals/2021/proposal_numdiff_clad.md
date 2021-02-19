---
title: Add numerical differentiation support in clad
layout: gsoc_proposal
project: IRIS-HEP
year: 2021
organization: princeton
---

## Description

In mathematics and computer algebra, automatic differentiation (AD) is a set of techniques to numerically evaluate the derivative of a function specified by a computer program. Automatic differentiation is an alternative technique to Symbolic differentiation and Numerical differentiation (the method of finite differences). Clad is based on Clang which provides the necessary facilities for code transformation. The AD library is able to differentiate non-trivial functions, to find a partial derivative for trivial cases and has good unit test coverage. In a number of cases, due different limitations, it is either inefficient or impossible to differentiate a function. For example, clad cannot differentiate declared-but-not-defined functions. In that case it issues an error. Instead, clad should fall back to its future numerical differentiation facilities.

## Task ideas and expected results

Implement numerical differentiation support in clad. It should be available through a dedicated interface (for example clad::num_differentiate). The new functionality should be connected to the forward mode automatic differentiation. If time permits, a prototype of configurable error estimation for the numerical differentiation should be implemented. The student should be prepared to write a progress report and present the results.

## Necessary skills

Intermediate C++; Understanding basic differential calculus; intermediate knowledge of clang.

## Mentors

  * **[Vassil Vassilev](mailto:vvasilev@cern.ch)**
  * [Alexander Penev](mailto:alexander_penev@yahoo.com)

## Links

  * [CLAD page](https://compiler-research.org/clad/)
  * [clad gsoc page](https://github.com/vgvassilev/clad/wiki/GSoC-2021)
  * [Cling](https://rawgit.com/root-project/cling/master/www/index.html)
