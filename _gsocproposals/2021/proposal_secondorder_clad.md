---
title: Utilize second order derivatives from Clad in ROOT
layout: gsoc_proposal
project: IRIS-HEP
year: 2021
organization: princeton
---

## Description

In mathematics and computer algebra, automatic differentiation (AD) is a set of techniques to numerically evaluate the derivative of a function specified by a computer program. Automatic differentiation is an alternative technique to Symbolic differentiation and Numerical differentiation (the method of finite differences). Clad is based on Clang which provides the necessary facilities for code transformation.

ROOT is a framework for data processing, born at CERN, at the heart of the research on high-energy physics. Every day, thousands of physicists use ROOT applications to analyze their data or to perform simulations. ROOT has a clang-based C++ interpreter Cling and integrates with Clad to enable flexible automatic differentiation facility.

## Task ideas and expected results

TFormula is a ROOT class which bridges compiled and interpreted code. Teach TFormula to use second order derivatives (using clad::hessian). The implementation should be very similar to what was done in [this pull request](https://github.com/root-project/root/pull/2745). The produced code should be well tested and documented. The student should be prepared to write a progress report and present the results. If time permits, we should pursue converting the C++ gradient function to CUDA device kernels. The integration of that feature should be comparable in terms of complexity to integrating 'clad::hessians'.

## Mentors

  * **[Vassil Vassilev](mailto:vvasilev@cern.ch)**
  * [Ioana Ifrim](mailto:ioana.ifrim@cern.ch)

## Links

  * [CLAD page](https://compiler-research.org/clad/)
  * [Cling](https://rawgit.com/root-project/cling/master/www/index.html)
  * [Clang](http://clang.llvm.org)
  * [ROOT](http://root.cern)
  * [ROOT github](https://github.com/root-project/root)
  
