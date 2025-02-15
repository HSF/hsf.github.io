---
title: Support usage of Thrust API in Clad
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

The rise of ML has shed light into the power of GPUs and researchers are looking for ways to incorporate them in their projects as a lightweight parallelization method. Consequently, General Purpose GPU programming is becoming a very popular way to speed up execution time.

Clad is a clang plugin for automatic differentiation that performs source-to-source transformation and produces a function capable of computing the derivatives of a given function at compile time. This project aims to enhance Clad by adding support for Thrust, a parallel algorithms library designed for GPUs and other accelerators. By supporting Thrust, Clad will be able to differentiate algorithms that rely on Thrust’s parallel computing primitives, unlocking new possibilities for GPU-based machine learning, scientific computing, and numerical optimization.

## Expected Results

* Research and decide on the most valuable Thrust functions to support in Clad
* Create pushforward and pullback functions for these Thrust functions
* Write tests that cover the additions
* Include demos of using Clad on open source code examples that call Thrust functions
* Write documentation on which Thrust functions are supported in Clad
* Present the work at the relevant meetings and conferences.

## Requirements

* Automatic differentiation
* C++ programming
* Clang frontend

## Links
* [Repo](https://github.com/vgvassilev/clad)
