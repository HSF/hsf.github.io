---
title: Implement CppInterOp API exposing memory ownership and thread safety
layout: gsoc_proposal
project: CppInterOp
year: 2026
difficulty: medium
duration: 350
mentor_avail: June-October
organization:
  - CompRes
project_mentors:
  - email: aaron.jomy@cern.ch
    organization: CERN
    first_name: Aaron
    last_name: Jomy
    is_preferred_contact: yes
  - email: vipul.cariappa@gmail.com
    organization: CERN
    first_name: Vipul
    last_name: Cariappa
  - email: vvasilev@cern.ch
    organization: Princeton University
    first_name: Vassil
    last_name: Vassilev
---

## Description

Incremental compilation pipelines process code chunk-by-chunk by building an ever-growing translation unit. Code is then lowered into the LLVM IR and subsequently run by the LLVM JIT. Such a pipeline allows creation of efficient interpreters. The interpreter enables interactive exploration and makes the C++ language more user friendly. The incremental compilation mode is used by the interactive C++ interpreter, Cling, initially developed to enable interactive high-energy physics analysis in a C++ environment.

Clang and LLVM provide access to C++ from other programming languages, but currently only exposes the declared public interfaces of such C++ code even when it has parsed implementation details directly. Both the high-level and the low-level program representation has enough information to capture and expose more of such details to improve language interoperability. Examples include details of memory management, ownership transfer, thread safety, externalized side-effects, etc. For example, if memory is allocated and returned, the caller needs to take ownership; if a function is pure, it can be elided; if a call provides access to a data member, it can be reduced to an address lookup. The goal of this project is to develop API for CppInterOp which are capable of extracting and exposing such information AST or from JIT-ed code and use it in cppyy (Python-C++ language bindings) as an exemplar. If time permits, extend the work to persistify this information across translation units and use it on code compiled with Clang.

## Project Milestones

* Collect and categorize possible exposed interop information kinds
* Write one or more facilities to extract necessary implementation details
* Design a language-independent interface to expose this information
* Integrate the work in clang-repl and Cling
* Implement and demonstrate its use in cppyy as an exemplar
* Present the work at the relevant meetings and conferences.

## Requirements

* C++ programming
* Python programming
* Familiarity with Clang and LLVM IR

## Links
* [Repo](https://github.com/compiler-research/CppInterOp)

## AI Policy

AI assistance is allowed for this contribution. The applicant takes full responsibility for all code and results, disclosing AI use for non-routine tasks (algorithm design, architecture, complex problem-solving). Routine tasks (grammar, formatting, style) do not require disclosure.

## How to Apply

In addition to reaching out to the mentors by email, prospective candidates are required to complete [this form](https://forms.gle/AYgrJthYCRmBwwFL8)
