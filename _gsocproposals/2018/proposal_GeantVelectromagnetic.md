---
title: Vectorization of electromagnetic physics models within the GeantV simulation vector prototype

layout: gsoc_proposal
project: GeantV
year: 2018
organization: CERN
---

## Description

The [GeantV](http://geant.web.cern.ch) simulation R&D aims to improving the performance of particle transport simulation programs for the high-luminosity phase of the LHC. This is leveraged by implementing explicit type-based vectorization using the [VecCore](https://github.com/root-project/veccore) library, applied already for some components such as the detector geometry and propagation in magnetic field. In the current phase of the R&D, an important effort is devoted to vectorising the different electromagnetic physics models developed within the prototype.

The task aims to modularize the common components used by these models and vectorize them, aiming to bring up the performance of this code. The project will benefit from existing implementations of other vectorized components and will integrate with the GeantV prototype.

## Task ideas

* Use explicit SIMD vectorization applied to concrete physics models code
* Optimize performance of existing scalar code

## Expected results

* Implementing the vector version of one or more electromagnetic physics models used currently in scalar mode in GeantV

## Requirements

* C++
* git
* Linux
* Some experience with vectorization
* Some experience with performance profiling tools

## Mentors

* [Andrei Gheata](mailto:andrei.gheata@cern.ch)
* [Witold Pokorski](mailto:witold.pokorski@cern.ch)

## Links

[source code](https://gitlab.cern.ch/GeantV/geant.git)
[GeantV page](http://geant.web.cern.ch/) 
