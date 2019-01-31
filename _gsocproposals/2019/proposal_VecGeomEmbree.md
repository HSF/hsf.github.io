---
title: Improving scalability of navigating tessellated structures using Embree library
layout: gsoc_proposal
project: VecGeom
year: 2019
organization:
  - CERN
---

## Description
VecGeom [1] project aims at developing a high-performance library for geometry modelling, describing geometry in terms of 3D solid primitives. The library provides vectorized ray-solid intersection algorithms and other geometry-specific functionality that make use of fine-grained SIMD and SIMT parallelism.

A special category of 3D solids supported in VecGeom is the so-called tessellated solids, represented as a mesh of planar faces approximating a complex object. Such solids are frequently used for example in bio-medical or space simulations, and are usually composed by a large number of triangles. Geometrical tasks such as point/line intersections with large triangle meshes have typical scalability problems, known in literature and addressed by several approaches in computer graphics or ray-tracing simulations.

VecGeom provides an implementation [2] of such intersection algorithms, suffering of scalability issues. The project aims to utilizing open source ray-tracers such as the Embree [3] library to optimize this task, taking advantage of the existing SIMD awareness of VecGeom library.

## Task ideas
We propose the following steps for improving the current implementation:
  * Understand the implementation requirements and match with the functionality provided by the Embree library.
  * Use Embree kernels to implement line-solid intersections.
  * Integrate with VecGeom API and optimize the implementation. 

## Expected results
Optimize navigation for the existing tessellated solids and demonstrate better scalability than the current algorithms.

## Desirable Skills
  * Familiar with advanced C++ features
  * Interest in algorithms and code optimization

## Mentors
  * [Sandro Wenzel](mailto:sandro.wenzel@cern.ch)
  * [Mihaela Gheata](mailto:mihaela.gheata@cern.ch)

## Links
   1. [Gitlab repository of VecGeom](https://gitlab.cern.ch/VecGeom/VecGeom)
   2. [Presentation at CHEP2019](https://indico.cern.ch/event/587955/contributions/2937590/attachments/1679163/2702881/VecGeom_multi_facets_chep2018.pdf)
   3. [Embree high-performance ray tracing kernels library](https://embree.github.io/)
