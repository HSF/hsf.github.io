---
title: Improve Cling’s Development Lifecycle
layout: gsoc_proposal
project: IRIS-HEP
year: 2021
organization: unl
---

Improve Cling’s Development Lifecycle

## Description

Cling is an interactive C++ interpreter, built on top of Clang and LLVM compiler infrastructure. Cling realizes the read-eval-print loop (REPL) concept, in order to leverage rapid application development. Implemented as a small extension to LLVM and Clang, the interpreter reuses their strengths such as the praised concise and expressive compiler diagnostics.


## Task ideas and expected results

The project foresees to enhance the Github Actions infrastructure by adding development process automation tools:
 * Code Coverage information (codecov)
 * Static code analysis (clang-tidy)
 * Coding conventions checks (clang-format)
 * Release binary upload automation

The student should be prepared to write a progress report and present the results.

## Necessary skills
Understanding of:
 * CMake
 * GitHub and GitHub Actions
 * codecov
 * clang-tidy and clang-format

## Mentors
* **[Oksana Shadura](mailto:oksana.shadura@cern.ch)**
* [Vassil Vassilev](mailto:vvasilev@cern.ch)

## Links
1. [Cling Github repository](https://github.com/root-project/cling)
2. [clang-format documentation](https://clang.llvm.org/docs/ClangFormat.html)
3. [clang-tidy documentation](https://clang.llvm.org/extra/clang-tidy/)
4. [codecov](https://codecov.io/)
