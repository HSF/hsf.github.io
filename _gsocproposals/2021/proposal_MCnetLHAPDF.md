---
title: MCnet/LHAPDF - Accuracy and parallel computation in parton density calculation
layout: gsoc_proposal
project: MCnet
year: 2021
organization:
  - UofGlasgow
  - CERN
---

# Description

The Large Hadron Collider smashes protons into each other at the highest energies humanity has ever engineered. Protons are a very convenient type of particle for our high-energy beams : they are plentiful, and they don't lose (lots of) energy like electrons do when accelerated around the LHC ring. But they are not *fundamental* particles: they are made up of a tightly bound collection of smaller particles, and to make the most out of LHC experiments we need to understand both what we do and don't know about the internal structure of the proton that these objects induce. We encode this through so-called parton density functions, or PDFs.

The [LHAPDF](https://lhapdf.hepforge.org) C++ library is the LHC's standard system for supplying PDF data to both experiments and theory calculations. Several years ago it was rewritten from scratch to make it more flexible and maintainable, but in the upcoming high-luminosity era of the LHC where vast numbers of events need to be processed, some of these designs are in need of updates both for speed and precision.


## Task ideas

This project will add new high-precision interpolators based on higher-order splines and Chebyshev polynomials to LHAPDF, and characterise the resulting improvements in numerical precision and performance. If there is scope within the project time, further performance work on these interpolators will be done to investigate opportunities for efficiency caching and use of GPU-based computation.


## Expected results

 * writing new LHAPDF interpolator plugin classes for higher precision and performance;
 * profiling and precision studies of the new interpolators;
 * implementing caching, and portable use of vectorization or GPU technology for performance boosts.


## Requirements

 * C++
 * Profiling
 * Vector accelerator / coprocessor techniques
 * git


## Mentors

 * **[Andy Buckley](mailto:andy.buckley@cern.ch)**
 * [Chris Gutschow](mailto:chris.g@cern.ch)


## Links

 * [LHAPDF](https://lhapdf.hepforge.org)
