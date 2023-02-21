---
title: Extend the Cppyy support in Numba
layout: gsoc_proposal
project: Cppyy
year: 2023
difficulty: medium
duration: 350
mentor_avail: June-October
organization:
  - CompRes
---

## Description

Numba is a JIT compiler that translates a subset of Python and NumPy code into fast machine code. Cppyy is an automatic, run-time, Python-C++ bindings generator, for calling C++ from Python and Python from C++. 

Cppyy has to pay a time penalty each time it needs to switch between languages which can multiply into large slowdowns when using loops with cppyy objects. This is where Numba can help. Since Numba compiles the code in loops into machine code it only has to cross the language barrier once and the loops thus run faster.

Initial support for Cppyy objects in Numba enabled the use of builtin types and classes (see [cppyy docs](https://cppyy.readthedocs.io/en/latest/numba.html)), but some essential C++ features, such as references and STL classes, are not yet supported.


## Project Milestones

* Add support for C++ reference types in Numba through Cppyy
* Add general support for C++ templates in Numba through Cppyy
* Add tests and documentation

## Requirements

* C++ programming
* Python programming
* Knowledge of LLVM IR (Optional)

## Mentors
* **[Baidyanath Kundu](mailto:baidyanath.kundu@cern.ch)**
* [Wim Lavrijsen](mailto:wlavrijsen@lbl.gov)
* [Vassil Vassilev](mailto:vvasilev@cern.ch)

## Links
* [Repo](https://github.com/wlav/cppyy)
