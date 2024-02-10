---
title: Implementing missing features in xeus-cpp
layout: gsoc_proposal
project: Xeus-Cpp
year: 2024
difficulty: medium
duration: 350
mentor_avail: June-October
organization:
  - CompRes
---

## Description

xeus-cpp is a Jupyter kernel for cpp based on the native implementation of the Jupyter protocol xeus. This enables users to write and execute C++ code interactively, seeing the results immediately. This REPL (read-eval-print-loop) nature allows rapid prototyping and iterations without the overhead of compiling and running separate C++ programs. This also achieves C++ and Python integration within a single Jupyter environment.

The xeus-cpp is a successor of xeus-clang-repl and xeus-cling. The project goal is to advance the project feature support to the extent of what’s supported in xeus-clang-repl and xeus-cling.

## Project Milestones

* Fix occasional bugs in clang-repl directly in llvm upstream
* Implement the value printing logic
* Advance the wasm infrastructure
* Write tutorials and demonstrators
* Complete the transition of xeus-clang-repl to xeus-cpp

## Requirements

* Python and C++ programming
* Knowledge of Clang and LLVM

## Mentors
* **[Alexander Penev](mailto:alexander.p.penev@gmail.com)**
* [Vassil Vassilev](mailto:vvasilev@cern.ch)

## Links
* [Repo](https://github.com/compiler-research/xeus-cpp)
* [Docs](https://xeus-cpp.readthedocs.io/en/latest/index.html)
