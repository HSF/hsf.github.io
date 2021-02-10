---
title: Implementation of Gilbert-Johnson-Keerthi Algorithm for Convex Shapes in VecGeom
layout: gsoc_proposal
project: VecGeom
year: 2020
organization:
    - CERN
---

## Description

The [VecGeom][1] project aims at developing a high-performance library for
geometry modelling, describing geometry in terms of 3D solid primitives. Fast
geometry queries are crucial in high energy physics (HEP) detector simulations.
The VecGeom library provides vectorized implementations of ray-solid
intersection algorithms and other functionality that make use of fine-grained
SIMD and SIMT parallelism.

The [Gilbert-Johnson-Keerthi algorithm][2] is a fast algorithm for general
convex shapes. The goal of this project is to implement the GJK algoritm in
VecGeom/Geant4 to allow for the simplification and potentially speedup of
several geometry primitives by sharing the same algorithm for their
implementation. Using a common implementation is also helpful to run simulations
on the GPU in the future.

## Task ideas

We propose the following steps:
 * Implementation of the GJK distance and ray-casting algorithms
 * Implementation of validation and performance tests
 * Performance comparison with current algorithms

## Technology
 * C++11, template programming

## Desirable Skills
 * Advanced C++ programming skills
 * Experience with numerical algorithms

## Expected results
 * Development and validation of the GJK algorithm in Geant4/VecGeom

## Mentors
 * [Guilherme Amadio](mailto:guilherme.amadio@cern.ch)
 * [Andrei Gheata](mailto:andrei.gheata@cern.ch)

## Links
 1. [VecGeom Gitlab Repository][1]
 2. [Gilbert-Johnson-Keerthi Distance Algorithm (Wikipedia)][2]
 3. [Improving the GJK Algorithm for Faster and More Reliable Distance Queries Between Convex Objects][3]
 4. [Real-Time Collision Detection by Christer Ericson (Morgan Kaufmann, 2005)][4]

[1]: https://gitlab.cern.ch/VecGeom/VecGeom
[2]: https://en.wikipedia.org/wiki/Gilbert%E2%80%93Johnson%E2%80%93Keerthi_distance_algorithm
[3]: https://dl.acm.org/doi/10.1145/3072959.3083724
[4]: http://realtimecollisiondetection.net
