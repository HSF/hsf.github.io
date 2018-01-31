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

High Energy Physics (HEP) analysis scripts are typically written in a straightforward, procedural style, but algorithms written in this style are not always performant. Slow analysis scripts do more than slow down research— they break the concentration of the analyst. HEP can benefit from Spark-style analysis pipelining, which makes it easier to parallelize algorithms, as well as contiguous-memory and vectorization techniques from High Performance Computing (HPC). While tools to provide these features are well in development, we also need common analysis algorithms to be cast in these forms to take advantage of the new libraries.

Algorithms written in a procedural style cannot be translated into a functional or vectorized style automatically. In many cases, the logic of the analysis procedure needs to be re-thought, to compute the same quantities in a new order.

## Tasks

The proposed project would be to develop a suite of HEP analysis primitive functions that (a) can be composed as building blocks, as in a combinational library, and (b) satisfies various constraints of immutability, loop independence, associativity, vectorizability, etc.

We propose the following steps:

 * given a collection of real-world analysis scripts and explanations of their purpose, distill the common techniques into components that can be composed;
 * express these components in frameworks like [Object-Array Mapping](https://github.com/diana-hep/oamap), which allows rapid exchange between object-oriented views and vectorizable-array views of the same data, or [Histogrammar](http://histogrammar.org), which builds plots by composition, or a new, similar infrastructure;
 * demonstrate that the original analysis scripts can be cast as compositions of these components, hopefully reducing complexity and improving readability;
 * run performance tests on the original and re-expressed scripts, hopefully observing an improvement.

## Expected results

This project is conceptual. While we do expect usable, readable code, we are more interested in the development of _revised algorithms_ than a polished package with a clean interface. The algorithms developed in this summer would be subject to refactoring for inclusion in future software packages.

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
