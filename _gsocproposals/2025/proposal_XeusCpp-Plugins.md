---
title: Enable GPU support and Python Interoperability via a Plugin System
layout: gsoc_proposal
project: Xeus-Cpp
year: 2025
difficulty: medium
duration: 350
mentor_avail: June-October
organization:
  - CompRes
project_mentors:
  - email: anutosh.bhat@quantstack.net
    organization: QuantStack
    first_name: Anutosh
    last_name: Bhat
    is_preferred_contact: yes
  - email: johan.mabille@quantstack.net
    organization: QuantStack
    first_name: Johan
    last_name: Mabille
  - email: vipulcariappa@gmail.com
    organization: CompRes
    first_name: Vipul
    last_name: Cariappa
  - email: aaron.jomy@cern.ch
    organization: CERN
    first_name: Aaron
    last_name: Jomy
---

## Description

Xeus-Cpp integrates [Clang-Repl](https://clang.llvm.org/docs/ClangRepl.html) with the [xeus](https://github.com/jupyter-xeus/xeus) protocol via [CppInterOp](https://github.com/compiler-research/CppInterOp/), providing a powerful platform for C++ development within Jupyter Notebooks.

This project aims to introduce a plugin system for magic commands (cell, line, etc.), enabling a more modular and maintainable approach to extend Xeus-Cpp. Traditionally, magic commands introduce additional code and dependencies directly into the Xeus-Cpp kernel, increasing its complexity and maintenance burden. By offloading this functionality to a dedicated plugin library, we can keep the core kernel minimal while ensuring extensibility. This approach allows new magic commands to be developed, packaged, and deployed independently—eliminating the need to rebuild and release Xeus-Cpp for each new addition.
Initial groundwork has already been laid with the Xplugin library, and this project will build upon that foundation. The goal is to clearly define magic command compatibility across different platforms while ensuring seamless integration.
A key objective is to reimplement existing features, such as the LLM cell magic and the in-development Python magic, as plugins. This will not only improve modularity within Xeus-Cpp but also enable these features to be used in other Jupyter kernels.

As an extended goal, we aim to develop a new plugin for GPU execution, leveraging CUDA or OpenMP to support high-performance computing workflows within Jupyter.


## Project Milestones

* Move the currently implemented magics and reframe using xplugin
* Complete the on-going work on the Python interoperability magic
* Implement a test suite for the plugins
* Extended: To be able to execute on GPU using CUDA or OpenMP
* Optional: Extend the magics for the wasm use case (xeus-cpp-lite)
* Present the work at the relevant meetings and conferences

## Requirements

* Python
* C/C++
* GPU programming; CUDA/OpenMP

## Links
* [Repo](https://github.com/compiler-research/xeus-cpp)
* Related Issues:
    - https://github.com/compiler-research/xeus-cpp/issues/4
    - https://github.com/compiler-research/xeus-cpp/issues/140
