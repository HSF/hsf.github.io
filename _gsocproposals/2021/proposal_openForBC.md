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

OpenForBC targets the development of a layer capable of presenting a common interface on top of such technologies in the open-source Linux KVM environment, aimed at supporting scientific and commercial applications for data centers, HPCs, distributed computing.
This approach will enable a "learn once use forever" pattern to developers and sysadmins, since the Open ForBC modularity copes well with the introduction of additional wrappers built around new and future toolsets aimed at GPU partitioning.

The Open ForBC project can be split in two subprojects:
- development of the toolset software and test against multiple models of GPU
- definition of test methodologies and comparison and benchmarking against existing solutions (e.g. ESXi)

The GSOC task will be focused on the latter, with interaction with the people involved in the first to improve the toolset based on benchmark measurements. 

## Task ideas
 * Collect literature, documentation and code for state-of-art computing and graphics benchmarks (e.g. MLPerf, PerfZero, Unigine, Passmark)
 * Create additional ML benchmarks (or tune the existing ones) based on real applications, interacting with research groups connected to the project
 * Define and develop a testing infrastructure, i.e. a software capable of sequentially running the chosen benchmarks and record the performances
 * Perform measurements of the baseline on existing solutions (e.g. VMWare) using various partitioning topologies.
 * Develop a module to produce publication-ready graphical material (such as plots, trends, graphics, tables) to present and show the test results

## Expected results

The successful student will develop and test a suite of ready-to-run benchmarks to measure the performances of various GPU partitioning options. 
The student will perform the baseline performance measurements that are necessary to test the solutions developed within OpenForBC.

## Requirements
Bash, Python (C++ optional but appreciated), familiar with Linux environment (bonus skill: KVM, ESXi) and virtualization techniques

## Mentors
  * [Federica Legger](mailto:federica.legger@cern.ch)
  * [Gabriele Gaetano Fronzé](mailto:gabriele.fronze@to.infn.it)

## Links
  * [OpenForBC](https://hackmd.io/@gfronze/r1j6FIb9U)
