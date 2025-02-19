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
project_mentors:
  - email: anutosh.bhat@quantstack.net
    organization: QuantStack
    first_name: Anutosh
    last_name: Bhat
    is_preferred_contact: yes
  - email: johan.mabille@quantstack.net
    organization: QuantStack
    first_name: Johan
    last_name: Mabille
  - email: vipulcariappa@gmail.com
    organization: CompRes
    first_name: Vipul
    last_name: Cariappa
  - email: aaron.jomy@cern.ch
    organization: CERN
    first_name: Aaron
    last_name: Jomy
---

## Description

xeus-cpp is an interactive execution environment for C++ in Jupyter notebooks, built on the Clang-Repl C++ interpreter, provided by [CppInterOp](https://github.com/compiler-research/CppInterOp/). While xeus-cpp enables a seamless workflow for running C++ code interactively, the lack of an integrated debugging experience remains a gap, especially when dealing with code that is dynamically compiled and executed through LLVM’s JIT(Just-In-Time) infrastructure.

Jupyter’s debugging system follows the Debug Adapter Protocol (DAP), enabling seamless integration of debuggers into interactive kernels. Existing Jupyter kernels, such as the IPython & the xeus-python kernel, have successfully implemented debugging workflows that support breakpoints, variable inspection, and execution control, even in dynamically executed environments. These implementations address challenges such as symbol resolution and source mapping for dynamically generated code, ensuring that debugging within Jupyter remains intuitive and user-friendly.

However, debugging C++ inside an interactive environment presents unique challenges, particularly due to Clang-Repl’s use of LLVM’s ORC JIT to compile and execute code dynamically. To integrate debugging into xeus-cpp, the project will explore existing solutions for DAP implementations like `lldb_dap` and debuggers like lldb that can interface with Jupyter while effectively supporting the execution model of Clang-Repl.

## Project Milestones

* Seamless debugging integration, establishing reliable interactions between xeus-cpp, a Debug Adapter Protocol (DAP) implementation, and a debugger.
* Implement a testing framework through `xeus-zmq` to thoroughly test the debugger. This can be inspired by an existing implementation in `xeus-python`. 
* Present the work at the relevant meetings and conferences.

## Requirements

* C/C++
* Basic understanding of the Debug Adapter Protocol
* Basic understanding of the stack used by xeus-cpp: xeus, cppinterop, clang-repl
* Research on different DAP implementations like lldb_dap and debuggers like lldb/gdb that can be utilized for the project.

## Links
* [Repo](https://github.com/compiler-research/xeus-cpp)
* [Debug Adaptor Protocol](https://microsoft.github.io/debug-adapter-protocol/)
* Debugging support through Jupyter:
    - https://jupyterlab.readthedocs.io/en/stable/user/debugger.html
    - https://jupyter-client.readthedocs.io/en/latest/messaging.html#debug-request
