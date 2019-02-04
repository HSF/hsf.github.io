---
title: GPU Race for Particle Hunting
layout: gsoc_proposal
project: Acts
year: 2019
organization: 
 - LAL
 - MdS
---

## Description

[Acts](http://acts.web.cern.ch) is a free and open-source software project for
track reconstruction in particle physics experiments. As a modernized
version of the particle tracking code used by the ATLAS experiment at the
CERN Large Hadron Collider, the project is focused on adoption of modern C++
standards, usability in multi-threaded workflows, and increased use of
vectorization and accelerators (gpgpu).

The fitting step of track reconstruction, in which particle track hypotheses
are confronted to experimental data, uses the Kalman Filter algorithm in the
5-dimensional space of possible track parameters. This entails performing
linear algebra operations on a large amount of 5x5 matrices, a problem which
has only received a limited amount of scrutinity from the linear algebra
community in the past. We are thus evaluating the relative performance of
multiple linear algebra toolkits on this problem, using realistic input data
from typical Acts use cases.

Until now, Acts has only been able to perform computations on CPUs. In this
project, we aim to investigate the use of GPUs, yet we would like to share
one single codebase across all target hardware configurations, and to this
end we want to first focus on the [Kokkos](https://github.com/kokkos/)
toolkit, which promises to permit the development of performance-portable
codebases by easily adapting several key characteristics, including data
layout, to the target hardware architecture.

We want to start by writing a Kokkos-based version of the Kalman Filter
benchmark, and see how well it performs with respect to CPU-based versions. We
also want to evaluate the portability of this version by testing it on the
various accelerators available in the GridCL/ACP facility (NVIDIA V100 and
K20, GeForce GTX Titan, AMD FirePro S9170). After this, we want to prototype
integration of the kokkos-based computations in the Acts codebase, and see how
well it performs in a more realistic use case.

In the context of a key step of particle hunting, this project gives the
opportunity to implement 5x5 linear algebra optimizations, and evaluate
their performance portability with a large diversity of GPUs.


## Task ideas
 * Reimplement our benchmark with kokkos.
 * Run the benchmark on the various accelerators of our GridCL/ACP facility,
   and evaluate ease of portability.
 * Compare results and performance between accelerators, and with other
   existing CPU implementations.
 * Prototype use of kokkos within Acts (for Kalman Filtering Update),
   and study the penalty of mixing the accelerated computing
   with other cpu-based computations.

## Expected results
 * Benchmark able to run on various GridCL/ACP accelerators.
 * Acts demonstrator including some kokkos offloaded computing.

## Requirements
C++ Templates, Computing with GPU, Linear Algebra.

## Mentors 
  * [David Chamont](mailto:david.chamont@lal.in2p3.fr)
  * [Pierre Kesterner](mailto:pierre.kestener@cea.fr)
  * [David Rousseau](mailto:david.rousseau@lal.in2p3.fr)

## Links
  * [Acts](http://acts.web.cern.ch)
  * [Kokkos](https://github.com/kokkos/)
