---
title: Jet clustering optimizations in fads
layout: gsoc_proposal
project: GoHEP
year: 2017
organization: LPC-Clermont
---

# Description

Fast simulation is an essential first step in many HEP analyses.
However, the current fast detector simulation toolkits have been written when parallelization and concurrency programming were not yet widely shared concerns.

[fads](https://go-hep.org) is a re-engineering in [Go](https://golang.org), addressing such concerns.
`fads` is heavily inspired from [Delphes](https://cp3.irmp.ucl.ac.be/projects/delphes) and tries to match bit-by-bit the physics results of its `C++` counterpart, with a better multicore scalability, leveraging the concurrency features of Go.

`fads` currently uses a very naive and CPU hungry jet clustering scheme which scales badly with the combinatorics involved at LHC multiplicities.
For `fads` to be competitive in real life scenarii, this needs to be fixed.

## Tasks

The proposed project aims at implementing a faster jet clustering strategy, using Delaunay triangulation.
[FastJet](http://fastjet.fr) uses [CGAL](http://www.cgal.org) to achieve performances in _O(N ln N)_ for Cambridge/Aachen and _O(N^{3/2})_ for anti-kt.

We propose the following steps:

  * implement and augment the unit tests for the current jet clustering strategy (in _O(N^3)_)
  * implement performance regression tests using the Go `testing` benchmark suite
  * implement Delaunay triangulation, using the [Gonum](https://github.com/gonum) numerical libraries
  * integrate the new clustering strategy into `fads` and plug it into the performance regression tests
  * leverage Go builtin features to make the clustering concurrent and scalable

## Expected results

Working implementation of a _O(N ln N)_ clustering strategy.

## Requirements

Go, C/C++ (to read legacy code and translate it into Go), git.

## Mentors

  * [Sebastien Binet](mailto:binet@cern.ch)
  * [Emmanuel Busato](mailto:emmanuel.busato@clermont.in2p3.fr)

## Links

  * [Go](https://golang.org)
  * [GoHEP](https://go-hep.org)
  * [fads](https://go-hep.org/x/hep/fads)
  * [Delphes](https://cp3.irmp.ucl.ac.be/projects/delphes)
  * [FastJet](http://fastjet.fr)
  * [CGAL](http://www.cgal.org)
  * [Gonum](https://github.com/gonum)
