---
title: MCnet/LHAPDF - online dashboard and data-visualisation for parton density functions
layout: gsoc_proposal
project: MCnet
year: 2024
organization:
  - UofGlasgow
difficulty: medium
duration: 175
mentor_avail: June-October
---

# Description

The Large Hadron Collider smashes protons into each other at the highest
energies humanity has ever engineered. Protons are a very convenient type of
particle for our high-energy beams : they are plentiful, and they don't lose
(lots of) energy like electrons do when accelerated around the LHC ring. But
they are not *fundamental* particles: they are made up of a tightly bound
collection of smaller particles, and to make the most out of LHC experiments we
need to understand both what we do and don't know about the internal structure
of the proton that these objects induce. We encode this through so-called parton
density functions, or PDFs.

The [LHAPDF](https://lhapdf.hepforge.org) C++ library, wrapped with a
Python interface, is the LHC's standard system for supplying PDF data
to both experiments and theory calculations. Over 1000 sets of PDF fits
are available in the LHAPDF data collection.

## Task ideas

This project will build on the LHAPDF test suite to report the current status
of PDF data files and validation, and allow online exploration, comparison
and plotting of PDF functions.


## Expected results and milestones

 * Familiarise with the LHAPDF framework from interface to calculation components;
 * Familiarise with current LHAPDF CI and regression tests;
 * Design and present a Web dashboard of PDF datasets and their validation status;
 * Add a live PDF plotting tool to the Web interface, including 1D and 2D
   comparisons of PDF functions.

## Requirements

 * Python
 * Web coding and visualisation libraries
 * CI testing
 * git


## Mentors

 * **[Andy Buckley](mailto:andy.buckley@cern.ch)**


## Links

 * [LHAPDF](https://lhapdf.hepforge.org)
