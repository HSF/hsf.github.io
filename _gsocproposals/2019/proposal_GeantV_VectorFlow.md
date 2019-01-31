---
title: VectorFlow - a vector processing service
layout: gsoc_proposal
project: GeantV
year: 2019
organization:
  - CERN
---

## Description
Many FLOP-intensive high-energy physics algorithms could profit from the vector pipelines of modern processors; they don’t because they don’t have vectorizable inner loops. The project idea is to implement and benchmark a generic vector flow service that can non-intrusively integrate with arbitrary data processing frameworks and can expose algorithms to the higher-level event loop of these frameworks. 

The service will filter the main data stream to extract data of interest, accumulating data in vectors to transform the original scalar data flow into a vector one. After a data transformation step extracting the algorithm input data in form of structures of arrays, this can be directly fed into a vector-aware implementation of the given algorithm. The output data can be scattered in scalar form and re-integrated in the framework data flow. Depending on the intrinsic algorithm gain from SIMD vectorization and better data caching, the overheads introduced by the extra data transformations can be much smaller than the benefits.


## Task ideas
  * Provide generic templated implementations for the main components of the framework: filtering, gathering vectors from scalar data, gathering data in SIMD-friendly formats, vector executor, scattering results back into scalar data and reintegrating in the framework flow
  * Proof of concept for concrete cases, starting with an algorithm integrated in a pipeline workflow and continuing with a more complex case.

## Technology
  * C++17, template programming
  * [VecCore](https://github.com/root-project/veccore) vectorization library

## Expected results
  * Development of some of the main service components with unit tests and a basic benchmark.

## Desirable Skills
  * Advanced C++ programming skills

## Mentors
  * [Andrei Gheata](mailto:andrei.gheata@cern.ch)
  * [Guilherme Amadio](mailto:guilherme.amadio@cern.ch)

## Links
   1. [VecCore vectorization library](https://indico.cern.ch/event/570876/contributions/2347250/attachments/1359720/2057229/Portable-SIMD-and-the-VecCore-Library-2016-10-24.pdf)
