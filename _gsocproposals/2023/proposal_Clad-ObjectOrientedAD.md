---
title: Improve automatic differentiation of object-oriented paradigms using Clad
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

Clad is an automatic differentiation (AD) clang plugin for C++. Given a C++ source code of a mathematical function, it can automatically generate C++ code for computing derivatives of the function. Clad has found uses in statistical analysis and uncertainty assessment applications.

Object oriented paradigms (OOP) provide a structured approach for complex use cases, allowing for modular components that can be reused & extended. OOP also allows for abstraction which makes code easier to reason about & maintain. Gaining full OOP support is an open research area for automatic differentiation codes.

This project focuses on improving support for differentiating object-oriented constructs in Clad. This will allow users to seamlessly compute derivatives to the algorithms in their projects which use an object-oriented model. C++ object-oriented constructs include but are not limited to: classes, inheritance, polymorphism, and related features such as operator overloading.


## Project Milestones

* Study the current object-oriented differentiable programming support in Clad. Prepare a report of missing constructs that should be added to support the automatic differentiation of object-oriented paradigms in both the forward mode AD and the reverse mode AD.
* Some of the missing constructs are: differentiation of constructors, limited support for differentiation of operator overloads, reference class members, and no way of specifying custom derivatives for constructors.
* Add support for the missing constructs.
* Add proper tests and documentation.


## Requirements

* Automatic differentiation
* C++ programming
* Clang frontend

## Mentors
* **[Parth Arora](mailto:partharora99160808@gmail.com)**
* [Vassil Vassilev](mailto:vvasilev@cern.ch)

## Links
* [Repo](https://github.com/vgvassilev/clad)
