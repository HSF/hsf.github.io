---
title: Implement a GlobalModuleIndex in ROOT and Cling
layout: gsoc_proposal
project: ROOT
year: 2019
organization:
  - CERN
  - UNL
---

## Description
This project aims to implement a GlobalModuleIndex [1],[2], which is expected to speed up ROOT’s [3] startup time two times. ROOT has its own C++ interpreter called Cling [4] for getting the reflection information.

We have been implementing C++ modules support in ROOT for the last few years, and we have recently reached the production level. However, there is still a room for optimization, and one of the possible solutions could be the implementation of GlobalModuleIndex. It is a mechanism to create the table of symbols and PCM names, so that ROOT will be able to load a corresponding library when a symbol lookup failed. This project will give the selected student an opportunity to contribute to two large and widely-used open source projects: ROOT and Clang/LLVM [5]. Moreover, the student will get a deep knowledge of C++ compiler and interpreter technology throughout this project.

## Task ideas
  * Implement a lazy loading of PCMs in GlobalModuleIndex.
  * Instantiate GlobalModuleIndex class in ROOT.
  * Register identifiers and modules of ROOT.
  * Implement a callback in Cling, which gets a callback when an identifier lookup was failed.
  * Deprecate startup modules loading step in ROOT, test a new implementation and provide performance measurements.

## Expected results
Implement GlobalModuleIndex in ROOT/Cling, provide a performance tuning for preloading of PCMs.

## Desirable Skills
  * Patience
  * C++ knowledge
  * Interest in Compiler technology

## Mentors
  * [Yuka Takahashi](mailto:yuka@cern.ch)
  * [Oksana Shadura](mailto:oksana.shadura@cern.ch)
  * [Vassil Vassilev](mailto:vvasilev@cern.ch)

## Links
  1. [GlobalModuleIndex](https://clang.llvm.org/doxygen/classclang_1_1GlobalModuleIndex.html)
  2. [Modules](https://clang.llvm.org/docs/Modules.html)
  3. [ROOT](https://github.com/root-project/root)
  4. [Cling](https://github.com/root-project/cling)
  5. [Clang/LLVM](https://clang.llvm.org/)
