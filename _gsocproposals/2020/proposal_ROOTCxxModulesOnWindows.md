---
title: Enable Modules on Windows
layout: gsoc_proposal
project: ROOT
year: 2020
organization: princeton
---

## Description

ROOT has several features which interact with libraries and require implicit header inclusion. This can be triggered by reading or writing data on disk, or user actions at the prompt. Often, the headers are immutable and reparsing is redundant. C++ Modules are designed to minimize the reparsing of the same header content by providing an efficient on-disk representation of C++ Code.

In ROOT v6.20 C++ modules are default on UNIX and will be default on OSX in the next release. The next challenge is C++ Modules on Windows.

## Task ideas and expected results

The main task is to investigate the feasibility of the C++ modules technology on Windows. This can be done by trying to compile ROOT on windows with -Druntime_cxxmodules=On.

The expected results is to enumerate a set of Windows-specific issues and implement compatible solutions to the UNIX baseline. The student should be prepared to write a progress report and present the results at the end of the summer.

## Necessary skills

Intermediate C++; Understanding of Clang; Understanding of C++ Modules.

## Mentors

  * [Vassil Vassilev](mailto:vvasilev@cern.ch)
  * [Bertrand Bellenot](mailto:Bertrand.Bellenot@cern.ch)

## Links

  * [ROOT](http://root.cern)
  * [clang](http://clang.llvm.org)
