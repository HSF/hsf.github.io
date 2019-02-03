---
title: Speedup KM3NeT's Pattern Recognition
layout: gsoc_proposal
project: KM3NeT
year: 2019
organization:
  - Nikhef
---

## Description

KM3NeT [1] will house two next-generation underwater neutrino
experiments. Two detectors are being constructed at two deep sites in
the Mediterranean Sea, one of the coast of Sicily and the other south
of Toulouse in Southern France. Nikhef [2] is involved the design and
construction of the detectors and in the JPP software framework used
to reconstruct signals from neutrinos.

Neutrino's traversing the earth sometimes interact with material in
the ground or atmosphere to produce a muon or electron. The KM3NeT
detectors search for the signature of light emitted by these muons and
electrons as they traverse the its volumes.

One of the main algorithms that is used to detect such electrons and
muons assumes many possible directions they might originate from.  It
first transforms the orientation and position of the detectors'
sensors, and then searches for signatures of emitted light that match
electrons and muons.

The current implementation of this algorithm is not optimized to use
modern CPU features. This project proposes to benchmark the
performance of the algorithm and to investigate opportunities for
improvements by introducing vector instructions and optimization of
data structures.

## Task ideas
  * Benchmark the existing algorithm with simulated data
  * Profile the algorithm and identify vectorization opportunities
  * Introduce vector instructions through use of intrinsics or
  suitable libraries
  * Optimize data structures for use with the improved algorithm

## Expected results
A clear picture of performance bottlenecks in the algorithm and
a implementation of a vectorized version.

## Desirable Skills
  * C++ knowledge
  * Interest in pattern recognition algorithms
  * Knowledge of writing C++ for vector instruction sets

## Mentors
  * [Roel Aaij](mailto:roelaaij@nikhef.nl)
  * [Ronald Bruijn](mailto:r.bruijn@nikhef.nl)
  * [Maarten de Jong](mailto:m.de.jong@nikhef.nl)

## Links
   1. [https://www.km3net.org](https://www.km3net.org)
   2. [https://www.nikhef.nl](https://www.nikhef.nl)
