---
title: MCnet/YODA - Enhance a statistical toolkit for physics analysis interpretation
layout: gsoc_proposal
project: MCnet
year: 2020
organization:
  - UGlasgow
  - CERN
  - Fermilab
---

# Description

[YODA](https://yoda.hepforge.org) is a small statistical toolkit for binned data, mainly used by the [Rivet](https://rivet.hepforge.org) package for taking Monte Carlo models of physics processes and comparing them to pre-recorded data. Rivet and YODA are used by hundreds of physicists across experiment and theory to develop, improve, test, and rule out new models. In turn this helps the LHC to use the best possible modelling, and to target our searches for physics beyond the Standard Model.

The YODA system is an attempt to do basic computational statistics objects in a new and more coherent way, clearly separating content and semantics from presentation, and emphasising the conceptual links between different types of histogram. In this way we not only improve functionality for data reinterpretation purposes, but also explore alternative ways of handling data that fit better to the requirements of future physics analyses.

## Tasks

There are three major areas where YODA currently needs work, to better handle mismatches between MC analysis implementations and "publication" presentations of particle physics data, and meet the needs of high-performance computing facilities:

 * development of a new inheritance structure in C++ and Python (via Cython) that efficiently provides functionality like N-dimensional binning of arbitrary datatypes, and expression of bin correlations, with maximum code reuse;
 * prototyping a new data format using the HDF5 library, for efficient data merging and parallel I/O on high-performance computing clusters;
 * creating a flexible, and publication quality plotting API around YODA, using matplotlib and other Python tools, to replace an old LaTeX-based plotter.

## Expected results

A prototype new version of YODA, reworked to generalise binning to arbitrary data types and dimensionalities, and integrated either with new a plotting or new I/O system.

## Requirements

 *- C++
 *- Python/Cython
 *- git

## Mentors

 * [Andy Buckley](mailto:andy.buckley@cern.ch)
 * [Louie Corpe](mailto:louie.corpe@cern.ch)
 * [Christian Bierlich](mailto:christian.bierlich@thep.lu.se)
 * [Holger Schulz](mailto:hschulz@fnal.gov)

## Links

 * [YODA](https://yoda.hepforge.org)
 * [Rivet](https://rivet.hepforge.org)
 * [Cython](https://cython.org/)
