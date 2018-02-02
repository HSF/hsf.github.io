---
title: DIANA-HEP/analysisfunctions - Translate HEP analysis functions to modern paradigms
layout: gsoc_proposal
project: DIANA-HEP
year: 2018
organization:
  - DIANA-HEP
  - Princeton
---

# Description

High Energy Physics (HEP) analysis functions are typically written in a straightforward, procedural style, but algorithms written in this style are not always performant. Slow analysis code does more than slow down research— it breaks the concentration of the analyst. HEP can benefit from Spark-style analysis pipelining, which makes it easier to parallelize algorithms, as well as contiguous-memory and vectorization techniques from High Performance Computing (HPC). While tools to provide these features are well in development, we also need domain-specific analysis algorithms to be cast in these forms to take advantage of the new libraries. The goal of this project is to reimplement a suite of HEP functions and demonstrate the improvements possible with functional, pipelined, and vectorized approaches.

Algorithms written in a procedural style cannot be translated into a functional/pipelined/vectorized style automatically. In many cases, the logic of the analysis procedure needs to be re-thought, to compute the same quantities in a new way.

## Tasks

The proposed project would be to develop a suite of HEP analysis primitive functions that (a) can be composed as building blocks, as in a combinational library, (b) satisfies various constraints of immutability, loop independence, associativity, vectorizability, etc., and (c) reproduces the original HEP functionality.

We propose the following steps:

 * given a collection of real-world analysis scripts and explanations of their purpose, distill the common techniques into components that can be composed;
 * express these components in frameworks like [Object-Array Mapping](https://github.com/diana-hep/oamap), which allows rapid exchange between object-oriented views and vectorizable-array views of the same data, or [Histogrammar](http://histogrammar.org), which builds plots by composition, or a new, similar infrastructure;
 * demonstrate that the original analysis code can be expressed as compositions of these components, hopefully reducing complexity and improving readability;
 * run performance tests on the original and re-expressed scripts, hopefully observing an improvement.

## Expected results

At the end of this project, we expect a first draft of a functional/pipelined/vectorized HEP library. We are more interested in the _way_ the successful applicant implements these functions than a polished package, as the results may be repurposed in other libraries.

## Requirements

- Python
- Numpy
- git

## Mentors

  * [Jim Pivarski](mailto:pivarski@fnal.gov)
  * [David Lange](mailto:david.lange@cern.ch)

## Links

  * [Object-Array Mapping](https://github.com/diana-hep/oamap)
  * [Histogrammar](http://histogrammar.org)
