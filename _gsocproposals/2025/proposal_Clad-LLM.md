---
title: Enhancing LLM Training with Clad for efficient differentiation

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

This project aims to leverage Clad, an automatic differentiation (AD) plugin for Clang, to optimize large language model (LLM) training primarily in C++. Automatic differentiation is a crucial component of deep learning training, enabling efficient computation of gradients for optimization algorithms such as stochastic gradient descent (SGD). While most modern LLM frameworks rely on Python-based ecosystems, their heavy reliance on interpreted code and dynamic computation graphs can introduce performance bottlenecks. By integrating Clad into C++-based deep learning pipelines, we can enable high-performance differentiation at the compiler level, reducing computational overhead and improving memory efficiency. This will allow developers to build more optimized training workflows without sacrificing flexibility or precision.

Beyond performance improvements, integrating Clad with LLM training in C++ opens new possibilities for deploying AI models in resource-constrained environments, such as embedded systems and HPC clusters, where minimizing memory footprint and maximizing computational efficiency are critical. Additionally, this work will bridge the gap between modern deep learning research and traditional scientific computing by providing a more robust and scalable AD solution for physics-informed machine learning models. By optimizing the differentiation process at the compiler level, this project has the potential to enhance both research and production-level AI applications, aligning with compiler-research.org’s broader goal of advancing computational techniques for scientific discovery.


## Expected Results

* Develop a simplified LLM setup in C++
* Apply Clad to compute gradients for selected layers and loss functions
* Enhance clad to support it if necessary, and prepare performance benchmarks
* Enhance the LLM complexity to cover larger projects such as llama
* Repeat bugfixing and benchmarks
* Develop tests to ensure correctness, numerical stability, and efficiency
* Document the approach, implementation details, and performance gains
* Present progress and findings at relevant meetings and conferences

## Requirements

* Automatic differentiation
* Parallel programming
* Reasonable expertise in C++ programming
* Background in LLM  is preferred but not required

## Mentors
* **[Vassil Vassilev](mailto:vvasilev@cern.ch)**
* [David Lange](mailto:david.lange@cern.ch)

## Links
* [Repo](https://github.com/vgvassilev/clad)
