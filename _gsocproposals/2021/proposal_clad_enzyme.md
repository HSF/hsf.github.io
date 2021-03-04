---
title: Add initial integration of Clad with Enzyme
layout: gsoc_proposal
project: IRIS-HEP
year: 2021
organization: princeton
---

## Description

In mathematics and computer algebra, automatic differentiation (AD) is a set of techniques to numerically evaluate the derivative of a function specified by a computer program. Automatic differentiation is an alternative technique to Symbolic differentiation and Numerical differentiation (the method of finite differences). Clad is based on Clang which provides the necessary facilities for code transformation. The AD library is able to differentiate non-trivial functions, to find a partial derivative for trivial cases and has good unit test coverage. Enzyme is a prominent autodiff framework which works on LLVM IR. 

Clad and Enzyme can be considered as a C++ frontend and a backend automatic differentiation framework. In many cases, when clad needs to fall back to numeric differentiation it can try configuring and using Enzyme to perform the automatic differentiation on lower level.


## Task ideas and expected results

Understand how both systems work. Define the Enzyme configuration requirements and enable Clad to communicate efficiently with Enzyme. That may require several steps: start building and using the optimization pass of Enzyme as part of the Clad toolchain; use Enzyme for cross-validation derivative results; etc. The student should be prepared to write a progress report and present the results.

## Necessary skills

Intermediate C++; Understanding basic differential calculus; intermediate knowledge of clang and llvm.


## Mentors
  * **[William Moses](mailto:wmoses@mit.edu)**
  * [Vassil Vassilev](mailto:vvasilev@cern.ch)

## Links
  * [clad](https://github.com/vgvassilev/clad)
  * [clad gsoc page](https://github.com/vgvassilev/clad/wiki/GSoC-2021)
  * [enzyme](https://github.com/wsmoses/Enzyme)
  * [enzyme web](https://enzyme.mit.edu)
  * [clang](http://clang.llvm.org/)
  * [llvm](http://llvm.org/)
