---
title: Integrate a Large Language Model with the xeus-cpp Jupyter kernel
layout: gsoc_proposal
project: Xeus-Cpp
year: 2024
difficulty: medium
duration: 350
mentor_avail: June-October
organization:
  - CompRes
---

## Description

xeus-cpp is a Jupyter kernel for cpp based on the native implementation of the Jupyter protocol xeus. This enables users to write and execute C++ code interactively, seeing the results immediately. This REPL (read-eval-print-loop) nature allows rapid prototyping and iterations without the overhead of compiling and running separate C++ programs. This also achieves C++ and Python integration within a single Jupyter environment.

This project aims to integrate a large language model, such as Bard/Gemini, with the xeus-cpp Jupyter kernel. This integration will enable users to interactively generate and execute code in C++ leveraging the assistance of the language model. Upon successful integration, users will have access to features such as code autocompletion, syntax checking, semantic understanding, and even code generation based on natural language prompts.

## Project Milestones

* Design and implement mechanisms to interface the large language model with the xeus-cpp kernel. [Jupyter-AI](https://github.com/jupyterlab/jupyter-ai) might be used as a motivating example
* Develop functionalities within the kernel to utilize the language model for code generation based on natural language descriptions and suggestions for autocompletion.
* Comprehensive documentation and thorough testing/CI additions to ensure reliability.
* [Stretch Goal] After achieving the previous milestones, the student can work on specializing the model for enhanced syntax and semantic understanding capabilities by using xeus notebooks as datasets.

## Requirements

* Python and C++ programming
* Basic knowledge of Large Language Models 
* Familiarity with the API's of Bard/OpenAI is a plus

## Mentors
* **[Vassil Vassilev](mailto:vvasilev@cern.ch)**
* [Aaron Jomy](mailto:aaron.jomy@cern.ch)
* [David Lange](mailto:david.lange@cern.ch)

## Links
* [Repo](https://github.com/compiler-research/xeus-cpp)
* [Docs](https://xeus-cpp.readthedocs.io/en/latest/index.html)
