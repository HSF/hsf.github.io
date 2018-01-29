---
title: Message Passing Interface for ROOT (ROOTMpi)
layout: gsoc_proposal
project: ROOT
year: 2018
organization:
  - OProject
  - CERN
  - UdeA
---

# Description

By standardizing the way different machines communicate during a running process, we can analyze bigger chunks of data in less time. ROOT MPI allows communication of ROOT’s native objects on top of the C/C++ raw data types. ROOT’s serialization methods and optimal design of the new C++ standard permits the user to focus on the algorithm instead of low level syntax.


## Task ideas
 * Extend existing communication schemas.
 * Write support for MPI files (may consider some design or idea to integrate it to TFile).
 * Checkpoint support at least in Open MPI and MPICH.
 * Improve the error handler system and messages in the output.
 * User tools:
    * Write a profiling tool support.
    * Write a benchmarking module.
    * Integrate valgrind command to ROOTMpi command for debug.

**Expected results**: 
* Working implementation with tests and documentation.
* Performance comparison with a basic example between ROOTMpi and Proof. 

**Requirements**: Advanced skills in C/C++, experience in parallel programming with MPI

**Mentors**: 
  * [Omar Zapata](mailto:sft-gsoc@cern.ch?subject=ROOTMpi)
  * [Lorenzo Moneta](mailto:sft-gsoc@cern.ch?subject=ROOTMpi) 
  * [Diego Restrepo](mailto:sft-gsoc@cern.ch?subject=ROOTMpi)

**Links**:

  * [http://root.cern](http://root.cern)
  * [http://mpi-forum.org](http://mpi-forum.org)
  * [http://oproject.org/pages/ROOTMpi.html](http://oproject.org/pages/ROOTMpi.html)
  * [https://root.cern.ch/proof](https://root.cern.ch/proof)

