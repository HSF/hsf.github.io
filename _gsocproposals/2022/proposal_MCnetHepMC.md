---
title: Dataset-manipulation tools for simulated collider events
layout: gsoc_proposal
project: MCnet
year: 2022
difficulty: medium
duration: 175
mentor_avail: June-July, September-October
organization:
  - UofGlasgow
---

# Description

Simulated collider events are an essential tool in particle physics: most
physics data-analyses are based around comparisons of data from the real
particle accelerator to simulations made in "Monte Carlo (MC) generator" programs, as
are studies to design new analyses, detectors, or colliders. They are also an
essential method of communication between experimental and theoretical
physicists.

At present there are two main data formats for MC event datasets &mdash; HepMC
and LHE, for full-detail and much smaller "hard process" event types
respectively &mdash; and a newer HDF5-based format for hard-process calculations
on massive parallel-computing (HPC) facilities. But while programming interfaces
exist for these (in particular the main formats), there is an absence of
user-friendly, command-line tools for event-file inspection, visualisation, and
manipulation.


## Task ideas

This project will provide a coherent set of command-line tools for inspecting,
manipulating, and displaying MC event datasets, bringing together existing code
snippets into an official set of standard commands to be used across particle
physics.


## Expected results

 * C++ and Python functions for efficiently inspecting, filtering, and combining MC event files/streams;
 * Command-line tools for listing, splitting, filtering, and combining MC event files;
 * An official cross-format version of the `mcdot` event visualisation tool, based on `graphviz`.


## Requirements

 * C++
 * Python
 * bash scripting
 * Graphviz
 * HDF5
 * git

Familiarity with C++, Python, bash, and git are essential; Graphviz and HDF5 can be learned in-situ.


## Mentors

 * **[Andy Buckley](mailto:andy.buckley@cern.ch)**
 * [Chris Gutschow](mailto:chris.g@cern.ch)


## Links

 * [HepMC](https://hepmc.web.cern.ch/hepmc/)
 * [LHE](http://home.thep.lu.se/~leif/LHEF/)
 * [HDF5](https://www.hdfgroup.org/solutions/hdf5/)
 * [PyHepMC](https://github.com/scikit-hep/pyhepmc)
