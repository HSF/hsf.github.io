---
title: Enable automatic differentiation of OpenMP programs with Clad
layout: gsoc_proposal
project: Clad
year: 2025
difficulty: medium
duration: 350
mentor_avail: June-October
organization:
  - CompRes
---

## Description

Clad is an automatic differentiation (AD) clang plugin for C++. Given a C++ source code of a mathematical function, it can automatically generate C++ code for computing derivatives of the function. Clad is useful in powering statistical analysis and uncertainty assessment applications.
OpenMP (Open Multi-Processing) is an application programming interface (API) that supports multi-platform shared-memory multiprocessing programming in C, C++, and other computing platforms. 

This project aims to develop infrastructure in Clad to support the differentiation of programs that contain OpenMP primitives.

## Expected Results

* Extend the pragma handling support 
* List the most commonly used OpenMP concurrency primitives and prepare a plan for how they should be handled in both forward and reverse accumulation in Clad
* Add support for concurrency primitives in Clad’s forward and reverse mode automatic differentiation.
* Add proper tests and documentation.
* Present the work at the relevant meetings and conferences.

## Requirements

* Automatic differentiation
* C++ programming
* Parallel Programming

## Mentors
* **[Vassil Vassilev](mailto:vvasilev@cern.ch)**
* [David Lange](mailto:david.lange@cern.ch)

## Links
* [Repo](https://github.com/vgvassilev/clad)
