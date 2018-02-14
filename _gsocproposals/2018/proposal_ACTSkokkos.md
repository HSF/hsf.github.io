---
title: Particle hunting with kokkos
layout: gsoc_proposal
project: ACTS
year: 2018
organization: LAL
---

## Description

[ACTS](http://cern.ch/acts) is a free and open-source software project for
track reconstruction in high-energy physics experiments. As a modernized
version of the particle tracking code used by the ATLAS experiment at the
Large Hadron Collider, the project is focused on adoption of modern C++
standards, usability in multi-threaded workflows, and increased use of
vectorization and accelerators (gpgpu).

The fitting step of track reconstruction, in which particle track hypotheses
are confronted to experimental data, uses the Kalman Filter algorithm in the
5-dimensional space of possible track parameters. This entails performing
linear algebra operations on a large amount of 5x5 matrices, a problem which
has only received a limited amount of scrutinity from the linear algebra
community in the past. We are thus evaluating the relative performance of
multiple linear algebra toolikts on this problem, using realistic input data
matching typical ACTS use cases.

Until now, ACTS has only been able to perform computations on CPUs. In this
project, we aim to investigate the use of extra accelerator hardware, such as
GPUs and Intel's Xeon Phis. We would like to retain the desirable property of
sharing one single codebase across all target hardware configurations, and to
this end we want to first focus on the [Kokkos](https://github.com/kokkos/)
toolkit, which promises to permit the development of performance-portable
codebases by easily adapting several key characteristics, including data
layout, to the target hardware architecture.

We want to start by writing a Kokkos-based version of the Kalman Filter
benchmark, and see how well it performs with respect to CPU-based versions. We
also want to evaluate the portability of this version by testing it on the
various accelerators available in the GridCL/ACP facility (Xeon Phi 5110P, AMD
FirePro S9170, NVIDIA K20, GeForce GTX Titan and hopefully V100). After this,
we want to integrate kokkos-based computations in the ACTS codebase, and see
how well it performs in a more realistic use case where it is mixed with other
computations and more accelerator-CPU I/O and synchronization is needed.

In the context of a key step of particle hunting, this project gives the
opportunity to invent new optimizations for 5x5 linear algebra, and evaluate
them with a large set of cutting-edge accelerators.


## Task ideas
 * Reimplement our benchmark with kokkos.
 * Run the benchmark on the various accelerators of our GridCL/ACP facility,
   and evaluate ease of portability.
 * Compare results and performance between accelerators, and with other
   existing CPU implementations.
 * Prototype use of kokkos within ACTS (for Kalman Filtering Update),
   and study the (expected bad) effect of mixing the accelerated computing
   with other cpu-based computations.

## Expected results
 * Benchmark able to run on various GRidCL/ACP accelerators.
 * ACTS demonstrator including some kokkos offloaded computing.

## Requirements
C++, Computing with GPU, Linear Algebra.

## Mentors 
  * [David Chamont](mailto:david.chamont@lal.in2p3.fr)
  * [Hadrien Grasland](mailto:hadrien.grasland@lal.in2p3.fr)
  * [David Rousseau](mailto:david.rousseau@lal.in2p3.fr)
  * [Andreas Salzburger](mailto:Andreas.Salzburger@cern.ch)

## Links
  * [acts](http://cern.ch/acts)
  * [kokkos](https://github.com/kokkos/)
