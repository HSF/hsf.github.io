---
title: Adoption of CppInterOp in ROOT
layout: gsoc_proposal
project: Cppyy
year: 2024
difficulty: medium
duration: 350
mentor_avail: June-October
organization:
  - CompRes
---

## Description

Incremental compilation pipelines process code chunk-by-chunk by building an ever-growing translation unit. Code is then lowered into the LLVM IR and subsequently run by the LLVM JIT. Such a pipeline allows creation of efficient interpreters. The interpreter enables interactive exploration and makes the C++ language more user friendly. The incremental compilation mode is used by the interactive C++ interpreter, Cling, initially developed to enable interactive high-energy physics analysis in a C++ environment. The CppInterOp library provides a minimalist approach for other languages to identify C++ entities (variables, classes, etc.). This enables interoperability with C++ code, bringing the speed and efficiency of C++ to simpler, more interactive languages like Python. CppInterOp provides primitives that are good for providing reflection information.

The ROOT is an open-source data analysis framework used by high energy physics and others to analyze petabytes of data, scientifically. The framework provides support for data storage and processing by relying on Cling, Clang, LLVM for building automatically efficient I/O representation of the necessary C++ objects. The I/O properties of each object is described in a compilable C++ file called a /dictionary/. ROOT’s I/O dictionary system relies on reflection information provided by Cling and Clang. However, the reflection information system has grown organically and now ROOT’s core/metacling system has been hard to maintain and integrate. 

The goal of this project is to integrate CppInterOp in ROOT where possible.

## Project Milestones

* To achieve this goal we expect several infrastructure items to be completed such as Windows support, WASM support
* Make reusable github actions across multiple repositories
* Sync the state of the dynamic library manager with the one in ROOT
* Sync the state of callfunc/jitcall with the one in ROOT
* Prepare the infrastructure for upstreaming to llvm
* Propose an RFC and make a presentation to the ROOT development team

  
## Requirements

* C++ programming
* Python programming
* Knowledge of Clang and LLVM

## Mentors
* **[Vassil Vassilev](mailto:vvasilev@cern.ch)**
* [David Lange](mailto:david.lange@cern.ch)

## Links
* [Repo](https://github.com/compiler-research/CppInterOp)
