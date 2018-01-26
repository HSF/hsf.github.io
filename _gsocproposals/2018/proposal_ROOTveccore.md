---
title: Improvements in vectorization and parallelization of ROOT Math libraries
layout: gsoc_proposal
project: ROOT
year: 2017
organization: 
 - CERN
 - UJI
---

## Project Description

HEP software applications require a large amount of computing resources,
and their computing performance is an important issue, in particular to satisfy
their ever-increasing requirements. Since 2005, we no longer benefit from the
automatic gains due to the increase in processor clock frequency. The growth in
the number of transistors on a chip now translates into an increase in the number
of cores and their complexity rather than an improvement in the performance of
each core. To tackle these challenges, the ROOT project has been undertaking a
re-engineering to adapt its Math libraries to run in multiple concurrent threads
and make an efficient use of the vector units (SIMD).

The chosen candidate will continue the re-engineering made on vectorization of
the Mathematical functions extending VecCore to implement a SIMD version of the
ROOT:TMath namespace.

## Task ideas

  * Evaluate the dependencies of the TMath Functions available in ROOT. 
  * Add a vectorized implementation of the ROOT::TMath functions in VecCore.
  * Benchmark performance in different architectures and instruction sets.
  * Integrate the new VecCore implementations in ROOT.
  * Benchmark VecCore TMath implementation in ROOT.
  * Vectorize “predefined ROOT functions”.

## Expected results
For each one of these areas the student will be expected to provide tests, reliable
benchmarks and speed-up results for each SIMD-enabled mathematical function.
At the end of GSoC, VecCore should contain a vectorized implementation of all the
TMath functions.

## Requirements
Strong knowledge of C++11; being able to produce clean, reliable code; No need for
background in math, although basic understanding of equations is expected. Basic
notions of vectorization are a plus.

## Mentors

  * [Guilherme Amadio](mailto:guilherme.amadio@cern.ch)
  * [Xavier Valls](mailto:xavier.valls.pla@cern.ch)
  * [Lorenzo Moneta](mailto:Lorenzo.Moneta@cern.ch)

## Links

  * [ROOT](https://root.cern/)
  * [VecCore](https://github.com/amadio/vecgeom)
  * [Vc](https://github.com/VcDevel/Vc)
