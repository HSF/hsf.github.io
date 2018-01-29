---
title: Message Passing Interface for ROOT (ROOTMpi)
layout: gsoc_proposal
project: ROOT
year: 2017
organization:
  - UdeA
  - CERN
---

# Description

By standardizing the way different machines communicate during a running process, we can analyze bigger chunks of data in less time. ROOT MPI allows to communicate ROOT’s native objects on top of the C/C++ raw data types. ROOT’s serialization methods and optimal design of the new C++ standard permits the user to focus on the the algorithm instead of low level syntax.


## Task ideas
 * Extend existing communication schemas.
 * Write support for MPI files (may consider some design or idea to integrate it to TFile)
 * Write a memory window, shared memory and RMA support.
 * Checkpoint support at least in OpenMpi and Mpich.
 * Improve the error handler system and messages in the output.
 * User tools:
    * Write a profiling tool.
    * Write a benchmarking module.
    * Integrate valgrind command to ROOTMpi command for debug.

**Expected results**: 
* working implementation with tests and documentation
* A machine learning example integrated with TMVA that uses ROOTMpi 
* Performance comparison with a basic example between ROOTMpi and Proof. 

**Requirements**: Advance skills in C/C++, experience in parallel programming with MPI

**Mentors**: 

  * Omar Zapata  Omar.Zapata@cern.ch
  * Diego Restrepo restrepo@udea.edu.co
  * Lorenzo Moneta  Lorenzo.Moneta@cern.ch

**Links**:

  * http://root.cern 
  * http://mpi-forum.org
  * http://oproject.org/ROOTMpi
  * https://root.cern.ch/proof

