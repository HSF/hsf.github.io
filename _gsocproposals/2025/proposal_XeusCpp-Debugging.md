---
title: Implementing Debugging Support
layout: gsoc_proposal
project: Xeus-Cpp
year: 2025
difficulty: medium
duration: 350
mentor_avail: June-October
organization:
  - CompRes
---

## Description

Xeus-Cpp is an interactive execution environment for C++ in Jupyter notebooks, built on top of Clang-Repl via CppInterOp. While it provides a seamless workflow for running C++ code interactively, the lack of an integrated debugging experience remains a gap, especially when dealing with dynamically compiled code through LLVM’s JIT (Just-In-Time) execution.

Jupyter’s debugging system follows the Debug Adapter Protocol (DAP), enabling seamless integration of debuggers into interactive kernels. Existing Jupyter kernels, such as the IPython & the xeus-python kernel, have successfully implemented debugging workflows that support breakpoints, variable inspection, and execution control, even in dynamically executed environments. These implementations address challenges such as symbol resolution and source mapping for dynamically generated code, ensuring that debugging within Jupyter remains intuitive and user-friendly.

However, debugging C++ inside an interactive environment presents unique challenges, particularly due to Clang-Repl’s use of LLVM’s ORC JIT to compile and execute code dynamically. To integrate debugging into Xeus-Cpp, the project will explore existing solutions for DAP implementations like `lldb_dap` and debuggers like lldb that can interface with Jupyter while effectively supporting the execution model of Clang-Repl.

## Project Milestones

* Seamless debugging integration in Xeus-Cpp establishing reliable interactions between Xeus-CPP, a Debug Adapter Protocol (DAP) implementation, and a debugger.
* Implement a testing framework through xeus-zmq to thoutest the debugger thoroughly testing everything that is supposed to work. Already done for xeus-python and we can take inspiration from there.
* Present the work at the relevant meetings and conferences.


## Requirements

* C/C++
* Basic understanding of Debug Adapter Protocol
* Basic understanding of the stack used by xeus-cpp: xeus, cppinterop, clang-repl
* Research on different DAP implementations like lldb_dap and debuggers like lldb/gdb that can be utilized for the project.

## Mentors
* **[Anutosh Bhat](mailto:anutosh.bhat@quantstack.net)**
* [Johan Mabille](mailto:johan.mabille@quantstack.net)
* [Vipul Cariappa](mailto:vipulcariappa@gmail.com)
* [Aaron Jomy](mailto:aaron.jomy@cern.ch)

## Links
* [Repo](https://github.com/compiler-research/xeus-cpp)
* [Debug Adaptor Protocol](https://microsoft.github.io/debug-adapter-protocol/)
* Debugging support through Jupyter:
    - https://jupyterlab.readthedocs.io/en/stable/user/debugger.html
    - https://jupyter-client.readthedocs.io/en/latest/messaging.html#debug-request