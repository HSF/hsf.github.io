---
title: Implement libInterOp API exposing memory, ownership and thread safety information
layout: gsoc_proposal
project: Compiler-Research
year: 2022
difficulty: high
duration: 350
mentor_avail: May-September
organization: princeton
---

## Description

Incremental compilation pipelines process code chunk-by-chunk by building an
ever-growing translation unit. Code is then lowered into the LLVM IR and
subsequently run by the LLVM JIT. Such a pipeline allows creation of efficient
interpreters. The interpreter enables interactive exploration and makes the C++
language more user friendly. The incremental compilation mode is used by the
interactive C++ interpreter, Cling, initially developed to enable interactive
high-energy physics analysis in a C++ environment.

Clang and LLVM provide access to C++ from other programming languages, but
currently only exposes the declared public interfaces of such C++ code even when
it has parsed implementation details directly. Both the high-level and the
low-level program representation has enough information to capture and expose
more of such details to improve language interoperability. Examples include
details of memory management, ownership transfer, thread safety, externalized
side-effects, etc. For example, if memory is allocated and returned, the caller
needs to take ownership; if a function is pure, it can be elided; if a call
provides access to a data member, it can be reduced to an address lookup. The
goal of this project is to develop API for libInterOp which are capable of
extracting and exposing such information AST or from JIT-ed code and use it in
cppyy (Python-C++ language bindings) as an exemplar. If time permits, extend the
work to persistify this information across translation units and use it on code
compiled with Clang.

## Task ideas

There are several foreseen tasks:
  * Collect and categorize possible exposed interop information kinds
  * Write one or more facilities to extract necessary implementation details
  * Design a language-independent interface to expose this information
  * Integrate the work in clang-repl and Cling
  * Implement and demonstrate its use in cppyy as an exemplar
  * Present the work at the relevant meetings and conferences.

## Technology

C/C++, Python, Clang, LLVM, Cling, Clang-Repl

## Desirable Skills

 * Necessary knowledge: C++ programming; data structures and algorithms.
 * Basic knowledge of Clang and LLVM
 * Basic knowledge of Python;
 * Experience with GPU programming would be an asset.

## Expected results

  Develop a facility which is able to detect memory allocation and deletion
  patterns and provide an API able to expose this information to users. If time
  permits develop facilities which capture information such as ownership
  transfer, thread safety and side-effects.

## Candidate Guidelines and Evaluation

If you have interest in working on the project there is a list of things to do
in order to maximize your chances to get selected:

1. Contact the mentors and express interest in the project. Make sure you attach
   your CV;
2. Download the source code of the cppyy, clang and llvm projects, build it and
   run the demos;
3. Start familiarizing yourself with the codebase;
4. If you have questions you can always contact a mentor.

The mentors are interested in working with all candidates but unfortunately the
rules allow only one to be selected. There are a few tasks which give bonus
points to candidate's application:
 * Submit a valid bug -- demonstrates that the candidate has completed step 2
   and 3 from the previous section.
 * Fix a bug -- demonstrates the technical skills of the candidate and shows
   he/she can work independently on the project. The mentors can suggest looking
   at the bugtracker[here](https://bitbucket.org/wlav/cppyy/issues?status=new&status=open).
   Fixing one issue may be enough to become a successful candidate.

## Mentors
 * **[Baidyanath Kundu](mailto:baidyanath.kundu@cern.ch)** (Princeton)
 * [Wim Lavrijsen](mailto:wlavrijsen@lbl.gov) (LBL)
 * [Vassil Vassilev](mailto:vvasilev@cern.ch) (Princeton)

## Links

[Compiler-Research](https://compiler-research.org)
[libInterOp](https://compiler-research.org/libinterop/)
[clang-repl](https://root.cern/blog/cling-in-llvm/)
[cling](https://github.com/root-project/cling)
[cppyy](https://cppyy.readthedocs.io/en/latest/)
[llvm](https://llvm.org/)
[clang](https://clang.llvm.org/)
