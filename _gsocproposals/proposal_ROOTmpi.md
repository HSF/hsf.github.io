---
title: Message Passing Interface for ROOT (ROOTMpi)
layout: plain
project: ROOT
organization: CERN
---

# Description

Since 1991 an effort was made to ease the task of parallelism with the introduction of the MPI protocol. By standardizing the way different machines communicate data during a running process, now we are able to analyze bigger chunks of data in less time than before or even reach the real time illusion with more sophisticated tasks.
In the scientific community, parallelism has always been both a necessity and a headache just because there is going to be every day more data to process and it is not getting any easier to do so.
ROOT MPI lets the programmer communicate ROOT’s native objects on top of the C/C++ raw data types that MPI allows. By using ROOT’s serialization methods and a very optimal design that the new C++ standard provides, we designed an easy to use interface for the scientist to focus on the abstraction layer of the algorithm and not the old low level syntax.



## Task ideas
 * To finish communication schemas.
 * To write support for MPI files (may consider some design or idea to integrate it to TFile)
 * To write memory window, shared memory and RMA support.
 * To write support for checkpoint at least in OpenMpi and Mpich.
 * To improve the error handler system and messages in the output.
 * User tools:
    * To write a profiling tool.
    * To write a module for benchmarking.
    * To integrate valgrind command to ROOTMpi command for debug.

**Expected results**: 
* working implementation with tests and documentation
* A machine learning example integrated to TMVA that uses ROOTMpi 
* Performance comparison with a basic example between ROOTMpi and Proof. 

**Requirements**: Advance skills in C/C++, experience in parallel programming with MPI

**Mentors**: 

  * Omar Zapata  Omar.Zapata@cern.ch
  * Lorenzo Moneta  Lorenzo.Moneta@cern.ch
  * Sergei Gleyzer Sergei.Gleyzer@cern.ch

**Links**:

  * http://root.cern 
  * http://mpi-forum.org
  * http://oproject.org/ROOTMpi
  * https://root.cern.ch/proof


