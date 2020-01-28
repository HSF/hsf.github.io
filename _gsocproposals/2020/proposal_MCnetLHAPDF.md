---
title: MCnet/LHAPDF - Make the Large Hadron Collider's proton structure library FAST!
layout: gsoc_proposal
project: MCnet
year: 2020
organization:
  - CERN
---

# Description

The Large Hadron Collider smashes protons into each other at the highest energies humanity has ever engineered. Protons are a very convenient type of particle for our high-energy beams : they are plentiful, and they don't lose (lots of) energy like electrons do when accelerated around the LHC ring. But they are not *fundamental* particles: they are made up of a tightly bound collection of smaller particles, and to make the most out of LHC experiments we need to understand both what we do and don't know about the internal structure of the proton that these objects induce. We do this through so-called parton density functions, or PDFs.

The [LHAPDF](https://lhapdf.hepforge.org) C++ library is the LHC's standard system for supplying PDF data to both experiments and theory calculations. Several years ago it was rewritten from scratch to make it more flexible and maintainable, but in the upcoming high-luminosity era of the LHC where vast numbers of events need to be processed, some of these designs are in need of updates both for speed and precision.

In this project, you will work on profiling and re-designing aspects of LHAPDF to make it much faster, adding caching, vectorisation, and GPU compatibility. This work has the potential to save huge amounts of CPU time for LHC experiments, and to enhance the physics we can do in the next LHC runs.

## Tasks

The following tasks are envisaged:

 * profiling of LHAPDF in realistic use-cases, to identify computational bottlenecks;
 * rewriting some unused polymorphism features to emphasise efficiency, while retaining sufficient flexibility;
 * implementing caching, and portable use of vectorization or GPU technology for performance boosts.

## Expected results

A prototype new version of LHAPDF, with improved performance via caching and exploratory accelerator technologies.

## Requirements

- C++
- Python/Cython
- Profiling
- Vector accelerator / coprocessor techniques
- hg/git

## Mentors

  * [Andy Buckley](mailto:andy.buckley@cern.ch)

## Links

  * [LHAPDF](https://lhapdf.hepforge.org)
