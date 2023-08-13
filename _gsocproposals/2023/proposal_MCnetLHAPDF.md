---
title: MCnet/LHAPDF - Test suite and coverage for parton density calculations
layout: gsoc_proposal
project: MCnet
year: 2023
organization:
  - UofGlasgow
difficulty: easy
duration: 175
mentor_avail: June-October
---

# Description

The Large Hadron Collider smashes protons into each other at the highest
energies humanity has ever engineered. Protons are a very convenient type of
particle for our high-energy beams : they are plentiful, and they don't lose
(lots of) energy like electrons do when accelerated around the LHC ring. But
they are not _fundamental_ particles: they are made up of a tightly bound
collection of smaller particles, and to make the most out of LHC experiments we
need to understand both what we do and don't know about the internal structure
of the proton that these objects induce. We encode this through so-called parton
density functions, or PDFs.

The [LHAPDF](https://lhapdf.hepforge.org) C++ library is the LHC's standard
system for supplying PDF data to both experiments and theory calculations.
Several years ago it was rewritten from scratch to make it more flexible and
maintainable, but extensions are now needed. This project will put in place a
far more complete regression-testing suite and code-coverage monitoring to
ensure that these new developments preserve the current behaviours, which the
whole LHC programme depends on being stable.

## Task ideas

This project will add continuous-integration (CI) tests in the GitLab system, to
ensure that all aspects of the LHAPDF calculations are tested on a scalable
rota, and introduce CI testing of code quality. The intention is to ensure the
stability of LHAPDF established behaviours to high precision, to give required
confidence when making new releases and developing new features. The project can
also include more physics-oriented work for a suitable candidate.

## Expected results and milestones

- Familiarise with the LHAPDF framework from interface to calculation
  components;
- Familiarise with current LHAPDF CI tests and the GitLab config system;
- Design and present a new proposal of CI tests to provide feature coverage,
  with a CPU-efficient test schedule, targeting of change-driven tests, and a
  full-suite pre-release test-set;
- Set up a Mac-based CI test worker, either virtual or physical, and incorporate
  in the test system;
- Incorporate a trial SonarCloud scan of the LHAPDF codebase, to identify code
  quality issues.

## Requirements

- C++
- Python
- CI testing
- git

## Mentors

- **[Andy Buckley](mailto:andy.buckley@cern.ch)**
- [Max Knobbe](mailto:max.knobbe@uni-goettingen.de)

## Links

- [LHAPDF](https://lhapdf.hepforge.org)
