---
title: MCnet/SHERPA - Accelerating Monte Carlo simulations for the LHC
layout: gsoc_proposal
project: MCnet
year: 2020
organization:
  - UDUR
---

# Description

SHERPA is a Monte Carlo event generator for collider-based particle physics experiments such as the ones performed at CERN's Large Hadron Collider (LHC).  It simulates full events, starting with the incident protons and finishing with the intricate patterns of the produced high-energetic particles that will eventually interact with the detector, thereby producing the indispensable link between theory and data, and allowing the interpretation of the latter in the light of the former.  To describe such events a variety of techniques and models must be invoked, many of which are based on the perturbative expansion of Quantum Field Theory.  This is true in particular for the starting point of the simulations where the so-called hard process defines the overall structure of the events.  To describe this central bit of the simulation, cross sections must be evaluated as integrals of the corresponding transition amplitudes over the multi-dimensional phase space of the outgoing particles.  Due to the high dimensionality of the phase space, this integration is achieved through Monte Carlo methods.

In the ongoing quest for increased precision of our understanding and modelling of the physics involved in the proton collisions, ever higher orders of the perturbation expansion must be evaluated.  This results in ever more complicated expressions for the transition amplitudes and an ever increasing number of final state particles and therefore the dimensionality of the phase space integration.  It is therefore not surprising that this first step of the event simulation is the most intensive source of CPU consumption and becoming the bottleneck for the full exploitation of future LHC results.

This project will be co-supervised by Frank Krauss, SHERPA's primary author, and Tobias Weinzierl, an expert in HPC computations and their performance optimization.  The project will focus on first steps to increase the efficiency of the SHERPA event generator, and in particular of its description of the hard process.  In a first step, the successful students will analyse the code and derive a detailed performance profile. Given the embarrassingly parallel nature of the underlying algorithmics, the studies will focus on single-node performance. In Durham, Intel's Amplifier VTune and the Allinea tools are available for this task, as well as a suite of open source helpers such as Likwid.

With a detailed performance profile at hand, the students will design an "optimisation roadmap" strategy for performance optimisation, and prototype its dominant aspects. We expect this roadmap to discuss mainly generic strategies mapped onto the particular application domain. This includes the flattening and serialisation of data structures to avoid scattered memory accesses, the reordering of data accesses, where the multi-shoot character of Monte Carlo algorithms usually provides ample space for relatively simple performance optimization.

## Task ideas

The following tasks are envisaged:

 * Overall performance profile of the SHERPA code
 * Detailed performance profile of the hard process simulation in the SHERPA code, with emphasis on data structures and access
 * Prototype code for performance improvement in performance hotspots, using data structure optimisation for vectorised CPU architectures

## Expected results

 * Improvements to SHERPA's performance, especially for the integration of cross sections for processes with multi-particle final-states
 * First draft of an Exascale Roadmap for SHERPA

## Requirements

 * Competent in OO C++
 * Experience with profiling tools
 * Performance optimisation
 * Multithreading
 * git + GitLab or similar CI configuration

## Mentors

 * [Frank Krauss](mailto:frank.krauss@durham.ac.uk)
 * [Tobias Weinzierl](mailto:tobias.weinzierl@durham.ac.uk)

## Links

 * [SHERPA](https://gitlab.com/sherpa-team/sherpa)
 * [Frank Krauss](https://www.ippp.due.ac.uk/profile/krauss)
 * [Tobias Weinzierl](http://www.peano-framework.org/index.php/tobias-weinzierl/)
