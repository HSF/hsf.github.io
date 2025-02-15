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

Clad is an automatic differentiation (AD) clang plugin for C++. Given a C++ source code of a mathematical function, it can automatically generate C++ code for computing derivatives of the function. Clad is useful in powering statistical analysis and uncertainty assessment applications.
ONNX (Open Neural Network Exchange) provides a standardized format for machine learning models, widely used for interoperability between frameworks like PyTorch and TensorFlow

This project aims to integrate Clad, an automatic differentiation (AD) plugin for Clang, with ONNX-based machine learning models. Clad can generate derivative computations for C++ functions, making it useful for sensitivity analysis, optimization, and uncertainty quantification. By extending Clad’s capabilities to ONNX models, this project will enable efficient differentiation of neural network operations within an ONNX execution environment.

## Expected Results

* Enumerate ONNX modules with increasing complexity and analyze their differentiation requirements.
* Develop a structured plan for differentiating the identified ONNX operations.
* Implement forward mode differentiation for selected ONNX operations.
* Extend support to reverse mode differentiation for more complex cases.
* Create comprehensive tests to validate correctness and efficiency.
* Write clear documentation to ensure ease of use and future maintenance.
* Present results at relevant meetings and conferences.


## Requirements

* Automatic differentiation
* Parallel programming
* Reasonable expertise in C++ programming
* Basic knowledge of Clang is preferred but not mandatory

## Links
* [Repo](https://github.com/vgvassilev/clad)
