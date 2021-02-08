---
title: MCnet/YODA - Add parallel weight streams to a statistical analysis toolkit
layout: gsoc_proposal
project: MCnet
year: 2021
organization:
  - UofGlasgow
  - UCL
---

# Description

[YODA](https://yoda.hepforge.org) is a statistical toolkit for binned data,
mainly used by the [Rivet](https://rivet.hepforge.org) analysis package. Rivet
takes simulated events from Monte Carlo models of physics processes, and
statistically compares them to pre-recorded data via YODA: this combination is
used by hundreds of physicists across experiment and theory to develop, improve,
test, and rule out new models. In turn this helps the LHC to use the best
possible modelling, and to target searches for new physics.

The YODA system is an attempt to do basic computational statistics objects in a
new and more coherent way, clearly separating content and semantics from
presentation, and emphasising the conceptual links between different types of
histogram. In this way we not only improve functionality for data
reinterpretation purposes, but also explore alternative ways of handling data
that fit better to the requirements of future physics analyses.


## Task ideas

A new C++ inheritance structure was added to YODA in GSoC 2020, enabling
efficient and flexible binned storage and manipulation of arbitrary data types,
and we now want to use this generalised design to handle multiple parallel
streams of event weights in a novel way. This will enable more powerful uses of
event variations, including a) estimating statistical correlations via Poisson
bootstrapping, b) and transparent handling of modelling variations without need
for histogram wrappers. These features will be useful for many areas of MC
phenomenology, e.g. in designing new physics analyses.


## Expected results

 * A set of new multi-weighted statistical summary objects, usable in YODA's generic binning API;
 * A prototype bootstrapping histogram class, using the new multi-weight objects; and
 * Integration of multiweights and other generic storage types into the YODA I/O system.


## Requirements

 * C++
 * Python
 * Cython
 * git


## Mentors

 * [Andy Buckley](mailto:andy.buckley@cern.ch)
 * [Chris Gutschow](mailto:chris.g@cern.ch)


## Links

 * [YODA](https://yoda.hepforge.org)
 * [Rivet](https://rivet.hepforge.org)
 * [Cython](https://cython.org/)
