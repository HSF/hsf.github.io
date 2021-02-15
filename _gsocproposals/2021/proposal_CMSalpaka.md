---
title: Portability for the Patatrack Pixel Track Reconstruction with Alpaka
layout: gsoc_proposal
project: CMS
year: 2021
organization: CERN
---

## Description

The CMS Software, [CMSSW](https://github.com/cms-sw/cmssw), is the framework utilized by the CMS experiment for the Data Acquisition, Trigger and Event Reconstruction. With the future upgrade of the Large Hadron Collider, the CMS detector will face a new challege for the event processing, due to the larger amount of data that will be produced. 

Heterogeneous Computing and Parallel Progamming will be the solution to that problem, and several efforts have been focused in offload the work from the common CPU to co-processors as GPUs. Around the 25% of the CMSSW have been ported on NVIDIA GPUs via the CUDA API, but more efforts are needed to simplify new co-processors implementation.

This project aims to use Portability Libraries like [Alpaka](https://github.com/alpaka-group/alpaka), to enable portability of the Patatrack Pixel Track Reconstruction with a single source code that can be executed across multiple processors (e.g. NVIDIA GPUs, x86 CPUs). One of the goals is to simplify the development of the CMS Patatrack reconstruction software with Alpaka, designing user-friendly interfaces for common tasks such as memory operations, work division optimisation and kernel launches, always aiming for high performance.


## Task ideas
  * Make algorithms in the Patatrack Pixel Track Reconstruction portable by using Alpaka
  * simplify development by designing simpler interfaces in alpaka
## Expected results
  * Run ported algorithms on CPU/GPU and compare performance with native CUDA implementation  
## Requirements
C++ (smart pointers and template), gcc, Makefile
## Mentors
  * [***Felice Pantaleo***](mailto:felice.pantaleo@cern.ch)
  * [Wahid Redjeb](mailto:wahid.redjeb@cern.ch)

## Links
  * [CMSSW](https://github.com/cms-sw/cmssw)
  * [Alpaka](https://github.com/alpaka-group/alpaka)

