---
title: Design and Develop a CUDA engine working along with C/C++ mode in clang-repl
layout: gsoc_proposal
project: Compiler-Research
year: 2022
difficulty: high
duration: 350
mentor_avail: May-September
organization:
    - princeton
---

## Description

Incremental compilation pipelines process code chunk-by-chunk by building an ever-growing translation unit. Code is then lowered into the LLVM IR and subsequently run by the LLVM JIT. Such a pipeline allows creation of efficient interpreters. The interpreter enables interactive exploration and makes the C++ language more user friendly. The incremental compilation mode is used by the interactive C++ interpreter, Cling, initially developed to enable interactive high-energy physics analysis in a C++ environment.

Our group puts efforts to incorporate and possibly redesign parts of Cling in Clang mainline through a new tool, clang-repl. The project aims to generalize the IncrementalCUDADeviceCompiler of Cling and add this functionality in clang-repl.

## Task ideas

There are several forseen tasks:

 * Write a detailed request for comment (RFC) document on the design choices and gather feedback from the LLVM community.
 * Implement the necessary functionality to support existing test cases available here.
 * Develop clang-repl-based tutorials for the CUDA backend.
 * Investigate the requirements for supporting a HIP backend.
 * Present the work at the relevant meetings and conferences.

## Technology
 * C/C++, CUDA

## Desirable Skills
 * Necessary knowledge: C++ programming; data structures and algorithms.
 * Basic Knowledge of Clang and LLVM 
 * Experience with GPU programming would be an asset.

## Expected results
 * Demonstrate necessary functionality for existing test cases.
 * Demonstrate a CUDA-executed gradient computed by the Clad automatic differentiation plugin.

## Evaluation Task
Interested students please contact the mentors for an evaluation task.

## Mentors
 * **[Ioana Ifrim](mailto:ioana.ifrim@cern.ch)** (Princeton)
 * [Vassil Vassilev](mailto:vvasilev@cern.ch) (Princeton)
 
## Links
 * [Compiler-Research][compiler-research]
 * [Clang Compiler][clang]
 * [Cling Repository][cling]
 * [Cling Introduction][cling-intro]
 * [LLVM][llvm]
 * [CUDA mode in Cling][cuda]
 * [Clad Repository][clad]
 

[compiler-research]: https://compiler-research.org
[clang]: https://clang.llvm.org
[cling]: https://github.com/root-project/cling
[cling-intro]: https://root.cern/primer/#learn-c-at-the-root-prompt
[llvm]: https://llvm.org/
[cuda]: https://zenodo.org/record/4021877#.Yg9zSC0RqRt
[clad]: https://github.com/vgvassilev/clad
