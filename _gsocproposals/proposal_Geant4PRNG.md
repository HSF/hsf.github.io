---
title: Using Pseudo-random numbers repeateably in a fine-grain multithreaded simulation
layout: plain
project: Geant4
organization:
  - CERN
---

# Description

Particle transport Monte Carlo simulations are a key tool for High Energy Physics experiments, including the LHC experiments at CERN. All Monte Carlo (MC) simulations depend vitaly on Pseudo-Random Number Generators (PRNGs) used to sample many distributions.
Each LHC experiments generates 5-10 Billion sampled physics events a year using around 10^18 sampled values from PRNGs. PRNGs take 1-5% of CPU time. PRNGs used must possess very large periods, fast execution, the ability to create a large number of streams, and very good correlation properties between streams and sampled values. It must be possible to reproduced a simulated event any time, for reexamination or debugging.


## Task ideas
 * Create a prototype that changes the use of random number generation in a Geant simulation so that the RNG state is associated with each track:
    * When a secondary is created, attach to it either a seed or a new state for PRNG, for use in that track.
    * Participating in extending the interface different PRNGs to provide different ways to choose the state of PRNG for a secondary.
    * Create implementations including MCRGs, counter-based PRNGs and novel PRNGs with guarantees of stream independence.
 

**Requirements**: programming in C/C++ or Java at least for class projects is required. Use of Linux/Unix, cmake and/or a coding IDE (Eclipse, Xcode) will be assets.
Knowledge gained: use of Pseudo-Random Number Generators and state of the art of PRNGs.

**Mentor**: 
* John Apostolakis​ sft-gsoc@cern.ch
* Sandro Wenzel    sft-gsoc@cern.ch
**Web site**: http://cern.ch/geant4
**Source code**: https://github.com/Geant4/geant4

