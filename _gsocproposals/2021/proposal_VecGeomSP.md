---
title: Single-precision floating-point support for GPU acceleration in VecGeom
layout: gsoc_proposal
project: VecGeom
year: 2021
organization:
    - CERN
---

## Description

The [VecGeom][1] project aims at developing a high-performance library for
geometry modeling, describing geometry in terms of 3D solid primitives. Fast
geometry queries are crucial in high energy physics (HEP) detector simulations.
The VecGeom library provides vectorized implementations of ray-solid
intersection algorithms and other functionality that make use of fine-grain
SIMD and SIMT parallelism.

VecGeom is being used as a geometry backend engine in [Geant4][2] for CPU-based particle
detector simulation applications, but also in [prototypes][3] aiming to accelerate such
applications on GPUs. VecGeom currently only supports double-precision arithmetics,
while most of the simulation input parameters in standard setups are known with much
lower precision. In particular, geometry algorithms can be substantially accelerated
on commodity GPUs by using single precision.

The project proposes an analysis of the numerical instability due to single-precision
[round-off error][4] divergence for existing geometry algorithms. We will use a single-precision,
GPU-enabled VecGeom build, and we expect the implementation of stability fixes for a
few major use cases. 

## Task ideas

We propose the following steps:
 * Adapting the current VecGeom 3D-solid testing framework assertions for single-precision use.
 * Running the testing framework and spotting the unstable algorithms.
 * Fixing the unstable algorithms for a set of simple solid types (such as tubes, cones, trapezoids).
 * Adapt global ray-model intersection algorithms to single-precision use. Developing a simple
 test benchmark demonstrating the ray traversal of geometry models having multiple components.
 * Performance comparison on GPU compared to double-precision mode.

## Technology
 * C++11, template programming

## Desirable Skills
 * Advanced C++ programming skills
 * Experience with numerical algorithms

## Expected results
 * Fixing the geometry algorithm rounding divergence related to single-precision use
 for the most important use cases. A detailed report of the stability analysis including:
    * performance impact on GPUs
    * status for the remaining unfixed cases, proposing possible solutions.

## Mentors
 * [John Apostolakis](mailto:john.apostolakis@cern.ch) (CERN)
 * **[Andrei Gheata](mailto:andrei.gheata@cern.ch)** (CERN)

## Links
 1. [VecGeom Gitlab Repository][1]
 2. [Geant4 Simulation Toolkit][2]
 3. [AdePT Gitlab Repository][3]
 4. [Round-of error in Wikipedia][4]

[1]: https://gitlab.cern.ch/VecGeom/VecGeom
[2]: https://geant4.web.cern.ch
[3]: https://github.com/apt-sim/AdePT
[4]: https://en.wikipedia.org/wiki/Round-off_error
