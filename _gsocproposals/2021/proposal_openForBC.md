---
title:  Partitioning GPUs for graphical and computing applications under Linux KVM
layout: gsoc_proposal
project: OpenForBC
year: 2021
organization: INFN
---

## Description

The GPU development and evolution of the last years has shown a much stronger peak performance growth with respect to CPUs. 
The performance growth, driven mainly by technological improvements in the transistor’s sizes, forced hardware producers to introduce hardware 
and low level software functionalities capable of enabling the GPU partitioning “à la CPU”. Such solutions (e.g. AMD MxGPU, Nvidia vGPU) are currently available in payware environments such as VMware ESXi and CITRIX, while these are marginally (or not) available inside Linux KVM. 

The aim of the project is to develop a layer capable of presenting a common interface on top of such technologies in the open-source Linux KVM environment, targeting both  scientific and commercial applications.
This approach will enable a "learn once use forever" pattern to sysadmins, since the Open ForBC modularity copes well with the introduction of additional wrappers built around new and future toolsets aimed at GPU partitioning.

The Open ForBC project can be split in two subprojects:
- development of the toolset software and test against multiple models of GPU
- definition of test methodologies and comparison and benchmarking against existing solutions (e.g. ESXi)

The GSOC task will be focused on the latter, with possible interaction with the people involved in the first to improve the toolset based on benchmark measurements.

## Task ideas
 * Collect literature, documentation and code for state-of-art computing and graphics benchmarks (e.g. MLPerf, PerfZero, Unigine, Passmark)
 * Create additional ML benchmarks (or tune the existing ones) based on real applications, interacting with research groups connected to the project
 * Define and develop a testing infrastructure, i.e. a software capable of sequentially running the chosen benchmarks and record the performances
 * Perform measurements of the baseline on existing solutions (e.g. VMWare) using various partitioning topologies.
 * Perform measurements on Linux KVM with and without Open ForBC
 * Interact with the staff handling Open ForBC development and participate to test-driven rounds of optimizations and bug fixing
 * Compare the obtained results and produce graphical material (plots, trends) for the publication of a scientific paper

## Expected results
Along the efforts of the Open ForBC staff, this GSOC proposal will provide the much needed comparative results between our solution and the existing commercial ones, enabling the release of the software as a production-ready tool.
The measurements performed by the GSOC candidate will be necessary for the publication of a white paper needed to enshrine the capabilities of the project.

## Requirements
Bash, Python (C++ optional but appreciated), familiar with Linux environment (bonus skill: KVM, ESXi) and virtualization techniques

## Mentors
  * [Federica Legger](mailto:federica.legger@cern.ch)
  * [Gabriele Gaetano Fronzé](mailto:gabriele.fronze@to.infn.it)

## Links
  * [OpenForBC](https://hackmd.io/@gfronze/r1j6FIb9U)
