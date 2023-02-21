---
title: Add support for SYCL alpaka backend to Patatrack Pixel Track reconstruction 
layout: gsoc_proposal
project: Patatrack
year: 2022
difficulty: medium
duration: 175
mentor_avail: June-October
organization:
  - CERN
---

## Description

For CMS, Heterogeneous Computing is a powerful tool to face the computational challenges  posed  by  the  upgrades  of  the  LHC,  and  will  be  used  in  production  at  the  HLT during  Run  3.   In  principle,  to  offload  the  computational  work  on  non-CPU  resources,  while retaining their performance, different implementations of the same code are required. This would introduce code-duplication which is not sustainable in terms of maintainability and testability of the software.  Performance Portability Libraries allow to write code once and run it on different architectures with close-to-native performance. 
During the LHC Run3 CMS experiment will use the [Alpaka][alpakapaper] portability library to offload parallel computation to GPUs while keeping the ability to run the same code on CPUs. A standalone version of the CMS Patatrack reconstruction has been already ported in Alpaka supporting the CPU serial backend and the GPU CUDA backend. 
The goal of the project is to introduce support for Intel accelerator devices via the [SYCL][sycl] backend. 

## Expected Results

* Development of a small alpaka demonstrator that can compile for CPU, NVIDIA GPU, Intel accelerators
* Patatrack reconstruction work division can be configured to run efficiently on Intel hardware
* Patatrack reconstruction can be compiled and execute on Intel accelerators

## Evaluation Task

Interested students please contact: 

 * [Felice Pantaleo](mailto:felice.pantaleo@cern.ch) (CERN)
 * **[Tony Di Pilato](mailto:tony.dipilato@cern.ch) (CERN CASUS)**
 * [Wahid Redjeb](mailto:wahid.redjeb@cern.ch) (CERN RWTH)

## Technologies

 * C++, Makefile, gcc, C++ smart pointers, C++ templates, bash shell scripting

## Desirable Skills

 * Experience with C++
 * Experience with GNU Makefile

## Mentors

 * [Felice Pantaleo](mailto:clue-dev@cern.ch) (CERN)
 * [Tony Di Pilato](mailto:clue-dev@cern.ch) (CASUS HZDR)
 * [Wahid Redjeb](mailto:clue-dev@cern.ch) (CERN RWTH)

## Links

 * [alpaka][alpaka]
 
[alpakapaper]: https://arxiv.org/abs/1602.08477
[alpaka]: https://github.com/alpaka-group/alpaka
[cmssw]: https://github.com/cms-sw/cmssw/
[sycl]: https://www.khronos.org/sycl/