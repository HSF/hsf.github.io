---
title: MCnet/Rivet - multiarch Docker images from CI
layout: gsoc_proposal
project: MCnet
year: 2024
organization:
  - UofGlasgow
difficulty: medium
duration: 175
mentor_avail: June-October
---

# Description

[Rivet](https://rivet.hepforge.org) is a toolkit for analysing
simulated collider events. It reconstructs the main physics processes
underlying the many particles in Monte Carlo event graphs, in a way
that allows new theories to be easily compared to experimental
data. This is a key way in which we test Large Hadron Collider (LHC)
data against ever-improving theory models, including proposals of new
physics beyond the Standard Model.


## Task ideas

This project will improve the Rivet documentation and release system
by automating generation and sharing of multi-architecture Docker images
from the GitLab continuous integration system, along with updated,
automatically generated documentation and web pages.


## Expected results and milestones

 * Familiarise with the Rivet framework;
 * Familiarise with the Rivet release process, including current CI, documentation, and Docker build scripts;
 * Migrate Docker build scripts into CI, automating and removing the need for local builds;
 * Extend Docker builds to multi-architecture images optimised for x86 and Mac M1/2 processors;
 * Complete web docs migration into CI builds, enabling new website deployment.

## Requirements

 * Python
 * Docker
 * CI testing
 * git


## Mentors

 * **[Andy Buckley](mailto:andy.buckley@cern.ch)**
 * [Chris Gutschow](mailto:chris.g@cern.ch)


## Links

 * [Rivet](https://rivet.hepforge.org)
