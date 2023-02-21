---
title: Explore advanced activity-analysis and optimizations in reverse-mode automatic differentiation.
layout: gsoc_proposal
project: Clad
year: 2023
difficulty: high
duration: 350
mentor_avail: June-October
organization:
  - CompRes
---

## Description

Clad is an automatic differentiation (AD) clang plugin for C++. Given a C++ source code of a mathematical function, it can automatically generate C++ code for computing derivatives of the function. Clad has found uses in statistical analysis and uncertainty assessment applications.

Automatic differentiation techniques involve computing partial derivatives of each intermediate variable encountered while automatically differentiating a function. Users are generally interested in the derivatives of a subset of the output variables with respect to a subset of the input variables. In this case, partial derivatives of many intermediate variables may not contribute to final derivatives and therefore can be ignored and not computed. Activity analysis finds intermediate variables whose partial derivatives contribute to the final required derivatives. It allows the AD tool to only compute the set of partial derivatives that are required. By not computing partial derivatives for such intermediate variables, both the memory requirement and the run time of the generated program can be reduced.

## Project Milestones

* Research about automatic differentiation activity analysis techniques. Prepare an activity analysis model report with an initial strategy to follow. This may involve brainstorming and the need for innovative solutions.
* Implement the proposed activity analysis mode.
* Add tests and documentation.

## Requirements

* Automatic differentiation
* Program analysis techniques
* C++ programming and Clang frontend

## Mentors
* **[Parth Arora](mailto:partharora99160808@gmail.com)**
* [Vassil Vassilev](mailto:vvasilev@cern.ch)

## Links
* [Repo](https://github.com/vgvassilev/clad)
