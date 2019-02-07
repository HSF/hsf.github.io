---
title: Implementation of an HDF5 IO layer for PODIO
layout: gsoc_proposal
project: HSF
year: 2019
organization:
  - CERN
  - BNL
  - DESY
---

## Description
PODIO, or plain-old-data I/O, is a C++ library to support the creation
and handling of data models in particle physics. It is based on the idea
of employing plain-old-data (POD) data structures wherever possible,
avoiding deep-object hierarchies and virtual inheritance. This is
to improve runtime performance and simplify the implementation of
persistency services (writing the in-memory objects to disk). To support the usage of modern software
technologies, PODIO was written with concurrency in mind and gives basic
support for vectorisation technologies. PODIO is already actively used
by the Future Circular Collider (FCC) project and is under evaluation by
the Linear Collider community (ILC).

PODIO already has a persistency implementation based on ROOT I/O, but is coded
in such a way that adding other persistency backends is quite
straightforward.

*Hierarchical Data Format* (or HDF5) is a generic data format
used for scientific data in many fields. It enjoys wide support, with many
different implementations and optimisations; it is an ideal format
to store PODIO data in.

This GSoC task is to implement an HDF5 backend for PODIO.

## Task ideas
 * Develop a data model description for PODIO in HDF5, reading the PODIO
   YAML data description and outputting HDF5 C++ code
 * Develop persistency code for PODIO to serialise a data model into
   HDF5 format
 * Develop persistency code for PODIO to deserialise from
   HDF5 format into PODIO in-memory layout
 * Write unit tests to ensure the correct functioning of the HDF5
   PODIO persistency layer

## Expected results
 * An HDF5 persistency module for PODIO
 * Appropriate unit tests for the module

## Requirements
* C++
* Python
* Optional: Some experience with CMake, git and GitHub would be useful

## Mentors
  * [Graeme A Stewart](mailto:graeme.andrew.stewart@cern.ch)
  * [Frank Gaede](mailto:frank.gaede@desy.de)
  * [Benedikt Hegner](mailto:benedikt.hegner@cern.ch)

## Links
  * [PODIO](https://github.com/AIDASoft/podio)
  * [HDF](https://www.hdfgroup.org)
  * [FCC](https://fcc.web.cern.ch/Pages/default.aspx)
  * [ILC](http://www.linearcollider.org)
