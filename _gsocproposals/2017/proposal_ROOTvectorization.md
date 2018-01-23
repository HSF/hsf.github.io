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
of cores rather than an improvement in the performance of each core. To tackle
these challenges, the ROOT project has been undertaking a re-engineering to adapt
its Math libraries to run in multiple concurrent threads and make an efficient
use of the vector units (SIMD).

The chosen candidate will continue the re-engineering made on vectorization of
the Mathematical function interfaces and the fitting functions plus parallelization
of the last one.

## Task ideas

  * Completion of parallelization and vectorization of all the fitting methods available
    in ROOT. 
  * Adapt gradient function interfaces for thread-based parallelization and vectorization.
  * Vectorization of TFormula and “predefined ROOT functions”.
  * Vectorization of most used mathematical and statistical functions in ROOT::Math and TMath.

## Expected results
For each one of these areas the student will be expected to provide tests, reliable
benchmarks and speed-up results. At the end of GSoC, ROOT should be capable of fitting
in parallel and making use of vectorization to evaluate both user-specified and predefined formulas.

## Requirements
Strong knowledge of C++11; being able to produce clean, reliable code; No need for
background in math, although basic understanding of equations is expected. Basic
notions of vectorization are a plus.

## Mentors

  * [Xavier Valls](mailto:xavier.valls.pla@cern.ch)
  * [Lorenzo Moneta](mailto:Lorenzo.Moneta@cern.ch)

## Links

  * [ROOT](https://root.cern/)
  * [VecCore](https://github.com/amadio/vecgeom)
  * [Vc](https://github.com/VcDevel/Vc)
