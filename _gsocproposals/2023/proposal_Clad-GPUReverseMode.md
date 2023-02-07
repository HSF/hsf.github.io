---
title: Enable reverse-mode automatic differentiation of (CUDA) GPU kernels using Clad
layout: gsoc_proposal
project: Clad
year: 2023
difficulty: medium
duration: 350
mentor_avail: June-October
organization:
  - CompRes
---

## Description

Clad is an automatic differentiation (AD) clang plugin for C++. Given a C++ source code of a mathematical function, it can automatically generate C++ code for computing derivatives of the function. Clad has found uses in statistical analysis and uncertainty assessment applications. In scientific computing and machine learning, GPU multiprocessing can provide a significant boost in performance and scalability. This project focuses on enabling the automatic differentiation of CUDA GPU kernels using Clad. This will allow users to take advantage of the power of GPUs while benefiting from the accuracy and speed of automatic differentiation.

## Project Milestones

* Research about automatic differentiation of code involving CUDA GPU kernels. Prepare a report and an initial strategy to follow.This may involve brainstorming and the need for innovative solutions. 
* Enable reverse-mode automatic differentiation of CUDA GPU kernels and calls to CUDA GPU kernels from the host code.
* Add proper tests and documentation.

## Requirements

* Automatic differentiation
* CUDA C++ programming
* C++ programming and Clang frontend

## Mentors
* **[Parth Arora](mailto:partharora99160808@gmail.com)**
* [Vassil Vassilev](mailto:vvasilev@cern.ch)

## Links
* [Repo](https://github.com/vgvassilev/clad)
