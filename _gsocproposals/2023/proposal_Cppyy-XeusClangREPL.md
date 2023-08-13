---
title:
  Enable cross-talk between Python and C++ kernels in xeus-clang-REPL by using
  Cppyy
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

xeus-clang-REPL is a C++ kernel for Jupyter notebooks using clang-REPL as its
C++ Interpreter. Cppyy is an automatic, run-time, Python-C++ bindings generator,
for calling C++ from Python and Python from C++.

Allowing C++ and Python to talk between themselves in a Jupyter notebook will
allow users to switch between Python and C++ at will. This means that data
analysts can set up their analysis in Python while running the actual analysis
in C++. Thus reducing the time to write and debug their analysis pipeline.

Initial support of cross talk between the two kernels has been implemented (see
here) but this only supports passing primitive data types. This project aims to
use Cppyy to extend this to support classes and functions.

## Project Milestones

- Automate creation of equivalent Cppyy objects in the Python kernel when
  objects are created in the C++ kernel
- Automate the creation of equivalent C++ objects in the xeus-clang-REPL kernel
  when Python objects are created
- Add documentation

## Requirements

- C++ programming
- Python programming

## Mentors

- **[Vassil Vassilev](mailto:vvasilev@cern.ch)**
- [Alexander Penev](mailto:alexander.p.penev@gmail.com)

## Links

- [Cppyy Repo](https://github.com/wlav/cppyy)
