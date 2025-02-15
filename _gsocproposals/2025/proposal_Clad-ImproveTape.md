---
title: Implement and improve an efficient, layered tape with prefetching capabilities
layout: gsoc_proposal
project: Clad
year: 2025
difficulty: medium
duration: 350
mentor_avail: June-October
organization:
  - CompRes
project_mentors:
  - email: vvasilev@cern.ch
    first_name: Vassil
    last_name: Vassilev
    is_preferred_contact: yes
  - email: david.lange@cern.ch
    first_name: David
    last_name: Lange
---

## Description

In mathematics and computer algebra, automatic differentiation (AD) is a set of techniques to numerically evaluate the derivative of a function specified by a computer program. Automatic differentiation is an alternative technique to Symbolic differentiation and Numerical differentiation (the  method of finite differences). Clad is based on Clang which provides the necessary facilities for code transformation. The AD library can differentiate non-trivial functions, to find a partial derivative for trivial cases and has good unit test coverage.

The most heavily used entity in AD is a stack-like data structure called a tape. For example, the first-in last-out access pattern, which naturally occurs in the storage of intermediate values for reverse mode AD, lends itself towards asynchronous storage. Asynchronous prefetching of values during the reverse pass allows checkpoints deeper in the stack to be stored furthest away in the memory hierarchy. Checkpointing provides a mechanism to parallelize segments of a function that can be executed on independent cores. Inserting checkpoints in these segments using separate tapes enables keeping the memory local and not sharing memory between cores. We will research techniques for local parallelization of the gradient reverse pass, and extend it to achieve better scalability and/or lower constant overheads on CPUs and potentially accelerators. We will evaluate techniques for efficient memory use, such as multi-level checkpointing support. Combining already developed techniques will allow executing gradient segments across different cores or in heterogeneous computing systems. These techniques must be robust and user-friendly, and minimize required application code and build system changes.

This project aims to improve the efficiency of the clad tape and generalize it into a tool-agnostic facility that could be used outside of clad as well.

## Expected Results

* Optimize the current tape by avoiding re-allocating on resize in favor of using connected slabs of array
* Enhance existing benchmarks demonstrating the efficiency of the new tape
* Add the tape thread safety
* Implement multilayer tape being stored in memory and on disk
* [Stretch goal] Support cpu-gpu transfer of the tape
* [Stretch goal] Add infrastructure to enable checkpointing offload to the new tape
* [Stretch goal] Performance benchmarks


## Requirements

* Automatic differentiation
* C++ programming
* Clang frontend

## Links
* [Repo](https://github.com/vgvassilev/clad)
