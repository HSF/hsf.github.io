---
title: A parallel-I/O binary histogram data format
layout: gsoc_proposal
project: MCnet
year: 2022
difficulty: medium
duration: 350
mentor_avail: June-July, September-October
organization:
  - UofGlasgow
  - UCL
---

# Description

[YODA](https://yoda.hepforge.org) is a statistical toolkit for binned data,
mainly used by the [Rivet](https://rivet.hepforge.org) collider-event analysis
package. Rivet analyses simulated events from new models of physics processes,
and statistically compares them to LHC data via YODA: this is a key way in which
we test LHC data against ever-improving theory models, including proposals of
new physics beyond the Standard Model.


## Why a new format?

YODA was initially designed with a focus on 1D histograms, for which it was
feasible to use a structured-text data format, that could be easily read and
edited by hand. But the increasing precision and detail of LHC data and
modelling has led to an increase in both uncertainty calculations and
multi-dimensional histogramming.

A new C++ structure was added to YODA in GSoC 2020, generalising the data types
and in particular allowing binned storage and manipulation of arbitrary data
types. But (even with gzipping) the data format is now straining under the
number and size of data objects that need to be stored. We also currently have
no way to connect the arbitrary stored types to the I/O system. A better
binary format is needed, both for performance and flexibility.


## Task ideas

This project will connect the YODA statistics objects to an efficient,
parallel-writeable I/O format.

To be compatible with needs for data simulation and analysis on large
parallel-computing (HPC) facilities, we have chosen the HDF5 data standard as
the basis for the new YODA format. This is a binary format with strong support
in data-science, programming models in C, C++ and Python, and which supports
parallel writing from multiple processes.


## Expected results

 * A consistent design and codebase for mapping YODA in-memory histograms and scatterplot data to HDF5;
 * A well-defined C++ code interface for allowing user-specified reading and writing of custom stored types;
 * Integration of the new format with existing YODA Python and command-line tools for data-format manipulations.


## Requirements

 * C++
 * Python
 * Cython
 * HDF5
 * git

Familiarity with C++ and git are essential; HDF5 and Cython (for connecting C++ to Python) can be learned in-situ.


## Mentors

 * **[Andy Buckley](mailto:andy.buckley@cern.ch)**
 * [Chris Gutschow](mailto:chris.g@cern.ch)


## Links

 * [YODA](https://yoda.hepforge.org)
 * [Rivet](https://rivet.hepforge.org)
 * [HDF5](https://www.hdfgroup.org/solutions/hdf5/)
 * [HighFive](https://github.com/BlueBrain/HighFive)
 * [Cython](https://cython.org/)
