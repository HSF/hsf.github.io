---
title: MCnet/Rivet - Speed and accuracy in the LHC's MC analysis tool
layout: gsoc_proposal
project: MCnet
year: 2020
organization:
  - UGlasgow
  - CERN
---

# Description

Rivet is a software package for performing data analysis on simulated particle collision events like those in the Large Hadron Collider. Analyses of real data have to deal with the effects of the giant, complex particle detectors that surround the beam interaction points, which are expensive to simulate, but use of statistical techniques allows much faster methods to be employed for testing theory models against data measurements. Rivet is the LHC's principle tool for such lightweight model testing, using events simulated using Monte Carlo (MC) methods. There are currently nearly 900 analysis routines registered on the Rivet platform.

However, as MC models get more complex and detailed, Rivet's features --- designed more for accuracy than raw speed --- are struggling. We need to up our technical game to keep up with ever larger datasets and user demands. We also need to be able to use Rivet efficiently on high-performance computing clusters, so it can be embedded into parallel codes that explore high-dimensional model parameter spaces, such as "global fits" of new-physics theories.

This project will focus on making Rivet performant on modern CPU architectures in HEP and HPC compute facilities, particularly ensuring that the central result caching and dispatching system is thread-safe and amenable to vectorized compiler optimizations. This will not only allow Rivet to be used in global fits, but also open new avenues for smaller-scale users, by transparently multiplexing event processing across multiple threads. As such re-engineering introduces risks that physics results will change, invalidating hundreds of analyses --- maybe in subtle ways --- we will also enhance the continuous integration system to include physics validation tests.

## Task ideas

The following tasks are envisaged:

 * thread-safety for high-performance applications
 * seamless multiplexing over many input streams
 * profiling and optimization of expensive computational components (caching, vector optimization)
 * continuous integration testing for continuous physics regression checks
 * Web interface UI upgrades

## Expected results

Improvements to Rivet's computational performance, in particular thread-safety, and a coherent system for ensuring continuity of physics behaviour via the Gitlab CI engine.

## Requirements

 * C++
 * Profiling
 * Performance optimization
 * Multithreading
 * git + gitlab or similar CI configuration

## Mentors

 * [Andy Buckley](mailto:andy.buckley@cern.ch)
 * [Louie Corpe](mailto:louie.corpe@cern.ch)

## Links

 * [Rivet](https://rivet.hepforge.org)
 * [Contur](https://contur.hepforge.org)
