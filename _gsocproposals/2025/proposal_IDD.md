---
title: Interactive Differential Debugging - Intelligent Auto-Stepping and Tab-Completion
layout: gsoc_proposal
project: CppInterOp
year: 2025
difficulty: medium
duration: 350
mentor_avail: June-October
organization:
  - CompRes
project_mentors:
  - email: vipulcariappa@gmail.com
    organization: CompRes
    first_name: Vipul
    last_name: Cariappa
    is_preferred_contact: yes
  - email: mvassilev@uni-plovdiv.bg
    organization: University of Plovdiv
    first_name: Martin
    last_name: Vasilev
---

## Description

Differential debugging is a time-consuming task that is not well supported by existing tools. Existing state-of-the-art tools do not consider a baseline(working) version while debugging regressions in complex systems, often leading to manual efforts by developers to achieve an automatable task.

The differential debugging technique analyzes a regressed system and identifies the cause of unexpected behaviors by comparing it to a previous version of the same system. The idd tool inspects two versions of the executable – a baseline and a regressed version. The interactive debugging session runs both executables side-by-side, allowing the users to inspect and compare various internal states.

This project aims to implement intelligent stepping (debugging) and tab completions of commands. IDD should be able to execute until a stack frame or variable diverges between the two versions of the system, then drop to the debugger. This may be achieved by introducing new IDD-specific commands. IDD should be able to tab complete the underlying GDB/LLDB commands. The contributor is also expected to set up the necessary CI infrastructure to automate the testing process of IDD.

## Expected Results

* Enable stream capture
* Enable IDD-specific commands to execute until diverging stack or variable value.
* Enable tab completion of commands.
* Set up CI infrastructure to automate testing IDD.
* Present the work at the relevant meetings and conferences.

## Requirements

* Python & C/C++ programming
* Familiarity debugging with GDB/LLDB

## Links
* [IDD Repository](https://github.com/compiler-research/idd)
