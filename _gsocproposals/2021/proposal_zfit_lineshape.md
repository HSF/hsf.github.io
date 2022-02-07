---
title: Implementation of physical shape function
layout: gsoc_proposal
project: zfit
year: 2021
organization:
  - UZH
---

## Description

[zfit](https://github.com/zfit/zfit) is a highly scalable and customizable model manipulation and fitting library. 
It uses TensorFlow as its computational backend and is optimised for simple and direct manipulation of probability density functions.
Purely built in Python, the usage is targeted towards the High Energy Physics analysis ecosystem.

While zfit in the core is focused to provide the basic building blocks, it misses compared to other libraries functions that are especially useful in physics.
Since it is built on top of TensorFlow, which has a performance penalty when using normal Python, these functions have to be implemented in zfit.


This project aims at implementing a more difficult lineshape, namely the faddeeva or voigt profile. This can either be done by creating a C++ kernel for CPU as well as GPU or by implementing it using the TensorFlow library.

## Task ideas
 * Implement a version of the faddeeva function or similar.
 * Measure the performance by profiling the code and try to find bottlenecks.
 * Since TensorFlow can also be run natively on the GPU, this will be profiled as well.
 * As TensorFlow provides automatic gradients, a custom, improved gradient may be integrated.
 * The function is finally wrapped inside a PDF and, together with tests and docs, added to the zfit library.

## Expected results
Working faddeeva function, implemented using the low-level functionality of TensorFLow (which is Numpy-like).

## Requirements
Python, Numpy, (maybe C++ and CUDA)

## Mentors
  * **[Jonas Eschle](mailto:Jonas.Eschle@cern.ch)**
  * [Rafael Silva Coutinho](mailto:rafael.silva.coutinho@cern.ch)

## Links
  * [zfit](https://github.com/zfit/zfit)
  * [zfit-physics](https://github.com/zfit/zfit-physics)
  * [faddeeva](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.wofz.html)
 
