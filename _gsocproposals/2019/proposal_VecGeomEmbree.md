---
title: Improved usage of Intel Embree ray-tracing kernels in VecGeom
layout: gsoc_proposal
project: VecGeom
year: 2019
organization:
  - CERN
  - ISS
---

## Description
VecGeom [1] project aims at providing a high-performance library for geometry modelling and geometry queries in the context of particle transport simulation in hierarchic 3D geometries, described in terms of solids. The library provides vectorized ray-solid intersection algorithms and other geometry-specific functionality that make use of fine-grained SIMD and SIMT parallelism.

Core tasks of VecGeom are similar to the ones used in ray-tracing. The project aims to study how we can yet better profit from interfacing with specialized ray-tracing kernel libraries such as Intel Embree [2]. The student is expected to push the effort based on a prototype interface already available in our code.
This project should be good for anyone interested in computer graphics, ray-tracing, particle simulation, etc.

## Task ideas
  * Improve VecGeom’s tessellated solid: implement a special version of a meshed (tessellated) solid using Intel Embree to find a rough intersection point in floating point precision, then dispatch to a higher precision distance calculation.
  * Directly query Embree’s in-memory bounding box acceleration structure from within VecGeom. At the moment this is only done indirectly, restricting the performance gains.
  * Implement a fast “isotropic minimal” distance calculation based on the in-memory Embree acceleration structure.

## Expected results
Improve compute performance of VecGeom in certain areas as well as reduce long-term code maintenance.

## Desirable Skills
  * Familiar with advanced C++ features (at least templates)
  * Interest in algorithms and code optimization

## Mentors
  * [Sandro Wenzel](mailto:sandro.wenzel@cern.ch)
  * [Mihaela Gheata](mailto:mihaela.gheata@cern.ch)

## Links
   1. [Gitlab repository of VecGeom](https://gitlab.cern.ch/VecGeom/VecGeom)
   2. [Embree high-performance ray tracing kernels library](https://embree.github.io/)
