---
title: Surface-based geometry modelling in VecGeom
layout: gsoc_proposal
project: VecGeom
year: 2022
difficulty: high
duration: 350
mentor_avail: June-August, September-October
organization:
    - CERN
---

## Description

For describing detector geometry, LHC experiments have used the constructive solid geometry ([CSG][csg]) approach successfully during the past decade to undertake detailed simulation of 10-20 billion proton-proton collisions each year. These rely on detector models with deep volume hierarchies composed of around 10 thousand volumes, which describe the millions of physical elements. The [VecGeom][vecgeom] project aims at developing a high-performance library for geometry modelling, describing geometry in terms of 3D solid primitives, such as boxes, tubes, or cones.

Using the existing CSG approach to undertake simulations on GPUs has resulted in poor performance, due to thread divergence and poor work balancing. This student project will be part of the new approach for geometry navigation in particle transport, which creates a ‘flatter’ surface-focused description (a “bounded-surface” model), and brings existing geometry descriptions onto it while looking to better leverage the massive potential of GPUs. This model will be based on a small number of simpler data structures, surface types and constructs, in order to ensure that it is performant on current GPUs and other future accelerators. It must provide the same navigation functionality as the existing geometry modeller.

## Task ideas

The student will be expected to work in close collaboration with the team developing this new geometry modeller for use on GPUs, writing code that uses simple data structures and is portable between CPU and GPUs. The concrete student project should consider planning based on the following tasks:
 * Generate the list of surfaces patches (i.e surface and outline on it) for the supported primitive solids.
 * Generate the list of surface patches for composite solids created by boolean operations on primitive solids (or other composite solids).
 * Create an algorithm that, given a list of surface patches, identifies which are duplicates or overlaps, and accumulates their information onto new data structures.
 * Select criteria (for a heuristic-based algorithm) to select which volume elements represent a large number of copies of daughter and progeny volumes within a setup. 
 * Use the criteria identified to ‘flatten’ an existing hierarchical detector geometry, into a higher-level scene and one or more lower-level detailed scenes. Reshuffle surfaces into one of these scenes.
 * Optimisations for generating bounded-volume hierarchies (BVH) on top of scenes containing several thousands of surfaces.
 * Benchmark examples with the new model implementation and compare correctness and performance with the previous implementation.

## Technology
 * C/C++, template programming, GPU programming.

## Desirable Skills
 * Necessary knowledge: C, Java or C++ programming; data structures and algorithms.
 * Knowledge of geometry modelling or projects on graphics would be very beneficial.
 * Experience with GPU programming or numerical analysis would be an asset.

## Expected results
 * Representing existing geometry setups in the new model description. A demonstrator example based on a subset of supported solids is the main deliverable.
 * Demonstrating navigation functionality (computation of distances) for simple setups.
 * Benchmark the GPU performance of the new model compared to the previous one.

## Evaluation Task
Interested students please contact Andrei for a warm-up and evaluation task.

## Mentors
 * **[Andrei Gheata](mailto:andrei.gheata@cern.ch)** (CERN)
 * [John Apostolakis](mailto:john.apostolakis@cern.ch) (CERN)
 
## Links
 * [VecGeom Gitlab Repository][vecgeom]
 * [Geant4 Simulation Toolkit][geant4]
 * [Boundary representation models][brep]
 
[csg]: https://en.wikipedia.org/wiki/Constructive_solid_geometry
[brep]: https://en.wikipedia.org/wiki/Boundary_representation
[vecgeom]: https://gitlab.cern.ch/VecGeom/VecGeom
[geant4]: https://geant4.web.cern.ch
