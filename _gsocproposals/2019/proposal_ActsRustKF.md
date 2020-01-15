---
title: Kalman Filter in Rust
layout: gsoc_proposal
project: Acts
year: 2019
organization: CERN
---

## Description

[ACTS](http://cern.ch/acts) is a free and open-source software project for
track reconstruction in particle physics experiments. As a modernized version
of the particle tracking code used by the ATLAS experiment at the CERN Large
Hadron Collider, the project is focused on adoption of modern C++ standards,
usability in multi-threaded workflows, and increased use of vectorization.

An essential part of track reconstruction is track fitting. In this step, a
hypothetical track is refined and updated using measurements from the detector.
A commonly used procedure used for fitting is a Kalman filter. This filter
iteratively updates a predicted track. Typically, this consists of linear
algebra operations on 1-6 dimensional track parametrizations and corresponding
up to 6x6 covariance matrices. After a final smoothing process, the optimal track
parameters can be extracted.

Rust is a modern compiled programming language designed for system
programming.  It is multi-paradigm and focused on sane and safe memory
management and robust concurrency. Runtime performance is comparable to
established languages such as C++. As such, it seems like a promising candidate
for future developments of highly performant tracking software with modern
design and principles.

The primary objective of this project is to establish a minimal implementation
of the components necessary to assess viability of Rust as a language for
future developments. This entails comparing runtime performance, as well as the
quality of results to the existing C++ implementations in Acts. Key aspects
will be an evaluation of solutions for linear algebra operations in Rust.
Additionally, an exploration of possibilities to interface components written
in Rust with C++ code can be conducted. Implications and requirements on the C++
event data model with respect to optimal communications between components can
be studied.

## Task ideas
 * Implement planar n-layer geometry in Rust
 * Evaluate / integrate library for or implement required linear algebra functionality
 * Implement Kalman filter for track fit in Rust
 * Investigate interfacing with Acts in C++, evaluate tentative event data model

## Expected results
 * Established baseline implementation of a Kalman Filter in Rust
 * Comparison of performance and numerical results with Acts KF implementation
 * Evaluation of suitability of EDM design for interface

## Requirements
C++ and or Rust, linear algebra

## Mentors 
  * [Paul Gessinger](mailto:paul.gessinger@cern.ch)
  * [Andreas Salzburger](mailto:Andreas.Salzburger@cern.ch)
  * [Hadrien Grasland](mailto:grasland@lal.in2p3.fr)

## Links
  * [Acts](http://cern.ch/acts)
  * [Rust](https://www.rust-lang.org)
