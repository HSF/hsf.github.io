---
title: Electron-ion collisions in Pythia 8
layout: plain
project: Pythia
organization: MIT
---

# Description

The Pythia 8 Monte Carlo event generator is the most popular one used in particle physics today; however, it does not support electron-ion collisions. It's predecessor did, and porting that functionality to the modern Pythia would be of great use. This is especially true, since building an electron-ion collider is the main focus of the US nuclear physics community for the coming decades, and having access to the best possible Monte Carlo is critical for designing the detectors that will one day record data from its collisions.

## Task ideas
 * Port all major electron-ion processes from the FORTRAN-based Pythia 6 to the C++-based Pythia 8.
 * Add other physics reactions of interest.
 * Tune the physics parameters using existing data, e.g. from HERA. This will involve comparing the output of the generator to measured observable distributions (potentially using Bayesian optimization as in arxiv:1610.08328).
 * Compare the results to competing electron-ion event generators. Are there any major differences? Do any of these impact the design of future electron-ion-collider experiments?

**Expected results**:

Working implementation of electron-ion collisions in Pythia 8.

**Requirements**: C++

**Mentors**:

  * Mike Williams  mwill@mit.edu
  * Phil Ilten  philten@cern.ch

**Links**:

  * http://home.thep.lu.se/Pythia/
