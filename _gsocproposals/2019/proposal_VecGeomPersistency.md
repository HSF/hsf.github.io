---
title: Persistency for VecGeom geometry
layout: gsoc_proposal
project: VecGeom
year: 2019
organization:
  - CERN
---

## Description
VecGeom [1, 2] project aims at developing a high-performance library for geometry modelling, describing geometry in terms of 3D solid primitives. The library provides vectorized ray-solid intersection algorithms and other geometry-specific functionality that make use of fine-grained SIMD and SIMT parallelism.

Persistency is a very important feature for a detector geometry package: it allows improving both portability of geometry representations and performance for the initialization phase. VecGeom can currently handle reading the GDML format [3] and ROOT [4] binary representation. These implementations are partial in the current state - only reading is possible in case of GDML, while the ROOT persistency is still in development. The goal of the project is to contribute to completing these implementations and demonstrate reading/writing geometry of different HEP detectors

## Task ideas
We propose the following steps:
  * Implementation of GDML writer for VecGeom geometry.
  * Complete the implementation of ROOT-based VecGeom persistency.

## Expected results
  * Demonstrating GDML-based read/write cycle.
  * Demonstrating ROOT-based read/write cycle.

## Desirable Skills
  * Familiar with advanced C++ features
  * Knowledge of ROOT is a plus

## Mentors
  * [Andrei Gheata](mailto:andrei.gheata@cern.ch)
  * [Gabriele Cosmo](mailto:gabriele.cosmo@cern.ch)

## Links
   1. [Gitlab repository of VecGeom](https://gitlab.cern.ch/VecGeom/VecGeom)
   2. [VecGeom papers and presentations](http://geant.cern.ch/content/publications#toc-vecgeom-publications-proceedings-and-presentations-in-20-eezmUTK1)
   3. [Geometry Description Markup Language (GDML)](http://gdml.web.cern.ch/GDML/)
   4. [ROOT framework](https://root.cern/)
