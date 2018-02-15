---
title: Particle hunting with xtensor
layout: gsoc_proposal
project: ACTS
year: 2018
organization: LAL
---

## Description

[ACTS](http://cern.ch/acts) is a free and open-source software project for
track reconstruction in high-energy physics experiments. As a modernized
version of the particle tracking code used by the ATLAS experiment at the
Large Hadron Collider, the project is focused on adoption of modern C++
standards, usability in multi-threaded workflows, and increased use of
vectorization.

The fitting step of track reconstruction, in which particle track hypotheses
are confronted to experimental data, uses the Kalman Filter algorithm in the
5-dimensional space of possible track parameters. This entails performing
linear algebra operations on a large amount of 5x5 matrices, a problem which
has only received a limited amount of scrutinity from the linear algebra
community in the past. We are thus evaluating the relative performance of
multiple linear algebra toolikts on this problem, using realistic input data
matching typical ACTS use cases.

The linear algebra operations of ACTS are currently implemented using
[Eigen](http://eigen.tuxfamily.org/index.php?title=Main_Page). In this
project, we want to investigate the use of
[xtensor](https://github.com/QuantStack/xtensor), another C++ library for
linear algebra, which has the advantage of being designed for interface and
implementation compatibility with the NumPy library that is popular in the
Python scientific ecosystem.

We already have a benchmarking infrastructure in place for comparing Eigen
with custom SIMD instructions written using the
[Boost.SIMD](https://github.com/NumScale/boost.simd) library, in the Kalman
Filter use case. In this project, we want to write an xtensor version to this
benchmark, and compare the performance of this library with the alternatives.
If the performance is satisfactory, or can be made so through reasonable
contributions to the xtensor project, the next step will be to investigate to
which extent xtensor and Eigen can coexist in the ACTS codebase, as a way to
avoid an impractical replacement of all uses of Eigen in ACTS in one go.

In the context of a key step of particle hunting, this project gives the
opportunity to compare several C++ linear algebra libraries (especially a
NumPy inspired one), experience their mixed use, and eventually invent some new optimizations for the 5x5 operations.


## Task ideas
 * Reimplement our benchmark with xtensor, and compare performance with
   other existing implementations (eigen, and custom Boost.SIMD code).
 * Study interoperability with eigen.
 * Prototype use of xtensor within ACTS.

## Expected results
 * Performance comparison between xtensor & eigen for our 5x5 algebra.
 * ACTS demonstrator mixing eigen and xtensor.
 * Eventually, suggestions of implementation improvements for 5x5 vectorized algebra ?

## Requirements
C++, SIMD Vectorisation, Linear Algebra.

## Mentors 
  * [David Chamont](mailto:david.chamont@lal.in2p3.fr)
  * [Hadrien Grasland](mailto:hadrien.grasland@lal.in2p3.fr)
  * [David Rousseau](mailto:david.rousseau@lal.in2p3.fr)
  * [Andreas Salzburger](mailto:Andreas.Salzburger@cern.ch)

## Links
  * [acts](http://cern.ch/acts)
  * [xtensor](https://github.com/QuantStack/xtensor)
  * [eigen](http://eigen.tuxfamily.org)
