---
title: Improve Cling’s Development Lifecycle
layout: gsoc_proposal
project: IRIS-HEP
year: 2021
organization: HZDR
---

Redefinition of CUDA functions

## Description

Cling is an interactive C++ interpreter, built on top of Clang and LLVM compiler
infrastructure. Cling realizes the read-eval-print loop (REPL) concept, in order
to leverage rapid application development. Implemented as a small extension to
LLVM and Clang, the interpreter reuses their strengths such as the praised
concise and expressive compiler diagnostics.
               
Since the development of Cling started, it got some new features to enable new
workflows. One of the features is CUDA mode, which allows you to interactively
develop and run CUDA code on Nvidia GPUs. Another feature is the redefinition of
functions, variable classes and more, bypassing the one-definition rule of C++.
This feature enables comfortable rapid prototyping in C++. Currently, the two
features cannot be used together because parsing and executing CUDA code behaves
differently compared to pure C++.

## Task ideas and expected results

The student's task is to adapt the redefinitions feature of the pure C++ mode
for the CUDA mode. To do this, the student must develop solutions to known and
unknown problems that parsing and executing CUDA code causes. The student should
be prepared to write a progress report and present the results.

## Necessary skills
                   
Good knowledge of C++, basic CUDA skills, knowledge of compiler construction,
experience with the LLVM library not mandatory but recommended.


## Mentors
* **[Simeon Ehrig](mailto:s.ehrig@hzdr.de)**
* [Vassil Vassilev](mailto:vvasilev@cern.ch)

## Links
* [cling](https://github.com/root-project/cling)
* [CUDA mode in cling](https://zenodo.org/record/4021877#.YDFNMuoo-Xw)
* [Paper on of redefinition in cling](https://www.researchgate.net/publication/339463915_Relaxing_the_one_definition_rule_in_interpreted_C)
* [Initial feature implementation](https://github.com/root-project/root/pull/4214)
