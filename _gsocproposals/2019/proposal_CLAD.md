---
title: Extend clad - The Automatic Differentiation
layout: gsoc_proposal
project: ROOT
year: 2019
organization: Princeton
---

# Description

In mathematics and computer algebra, automatic differentiation (AD) is a set of techniques
to numerically evaluate the derivative of a function specified by a computer program. Automatic
differentiation is an alternative technique to Symbolic differentiation and Numerical
differentiation (the method of finite differences). [CLAD](https://github.com/vgvassilev/clad)
is based on Clang which will provide the necessary facilities for code transformation.
The AD library is able to differentiate non-trivial functions, to find a partial derivative for
trivial cases and has good unit test coverage.


## Task ideas and expected results:
  * The student should teach AD how to generate hessian computation in one function
  for a given function to differentiate.
  * The implementation should be very well-tested and documented. The student should prepare a
  final poster of the work and be ready to present it.

## Requirements:
 Advanced C++, Clang abstract syntax tree (AST), basic math.

## Mentors:

  *  [Vassil Vassilev](mailto:vvasilev@cern.ch)
  *  [Oksana Shadura](mailto:oksana.shadura@cern.ch)
