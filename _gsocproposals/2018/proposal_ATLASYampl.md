---
title:  Yampl - an inter-process communication library for ATLAS
layout: gsoc_proposal
project: ATLAS
year: 2018
organization:
  - LBNL
  - ANL
---

## Introduction

The ATLAS experiment on the Large Hadron Collider at CERN processes its data at more than 100 computing centers around the world. When an ATLAS application runs on a compute node, it utilizes all available CPU cores by leveraging process-based parallelism. In this mode multiple processes run simultaneously on the same machine and exchange data via Linux Interprocess Communication (IPC) mechanisms. In order to support this mode of operation, ATLAS has developed a lightweight and robust IPC library called [Yampl](https://github.com/vitillo/yampl). Yampl provides a simple C++ API for developing client-server applications in which various components can run either on the same compute node or in a distributed environment. Yampl supports a number of IPC backends for collocated (e.g. shared memory, pipe) as well as distributed (e.g. linux sockets) processes. Yampl also comes with a python interface, which is currently implemented as a separate package called [python-yampl](https://github.com/vitillo/python-yampl).
 
## Task 

Yampl has been serving us well over past several years. However, there is a number of requirements coming from the ATLAS computing community which require substantial code modification and refactoring:

- Selection of IPC backends at run time. Currently Yampl is a monolithic library containing all backend-specific code. Any fix or update of the backend code requires making a new version for the entire library. Such architecture also prevents us from adding support for new backends without changing the existing code. In order to deal with these limitations we want to redesign the Yampl library, such that it will become more modular and various backends will be implemented as plug-ins.

- Python interface to Yampl is implemented as a separate package. We want to integrate the python interface with the main Yampl library and develop a simple procedure for building the C++ library and its python binding in one go. This process may also involve a substantial redesign of python bindings for Yampl.

## Expected results

- Modular Yampl library with the backend-specific code implemented as plug-ins.

- Integration of python-yampl with the main yampl package. A simple and straightforward procedure for building C++ yampl and Python yampl in one go.

- New design and implementation of Python bindings for Yampl.

## Requirements

- C++
- python
- Linux IPC

## Mentors

 * [Vakho Tsulaia](mailto:vtsulaia@lbl.gov)
 * [Peter Van Gemmeren](mailto:gemmeren@anl.gov)

## Links

 * [Yampl](https://github.com/vitillo/yampl)
 * [Python-yampl](https://github.com/vitillo/python-yampl)
