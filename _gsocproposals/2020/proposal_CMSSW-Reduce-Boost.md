---
title: Reduce boost dependence in CMSSW
layout: gsoc_proposal
project: CMSSW
year: 2020
organization: princeton
---

## Description

The LHC smashes groups of protons together at close to the speed of light: 40 million times per second and with seven times the energy of the most powerful accelerators built up to now. Many of these will just be glancing blows but some will be head on collisions and very energetic. When this happens some of the energy of the collision is turned into mass and previously unobserved, short-lived particles – which could give clues about how Nature behaves at a fundamental level - fly out and into the detector. Our work includes the experimental discovery of the Higgs boson, which led to the award of a Nobel prize for the underlying theory that predicted the Higgs boson as an important piece of the standard model theory of particle physics.

CMS is a particle detector that is designed to see a wide range of particles and phenomena produced in high-energy collisions in the LHC. Like a cylindrical onion, different layers of detectors measure the different particles, and use this key data to build up a picture of events at the heart of the collision.

Many of CMS Software components (CMSSW) are hosted on Github. There are millions of lines of C++ and Python code created and maintained by the collaboration. It uses many advanced features in C++ that were historically only available in the boost package, such as `boost::shared_ptr`. The recent C++ standard offers the same (or similar) facilities in many cases. This project is to analyze and implement changes to CMSSW that move towards C++ standard implementations. Relying on more standard features is a good software practice and will reduce “technical debt” in CMSSW.

## Task ideas and expected results

Enumerate the set of boost C++ entities which have direct analogs in standard C++. Enumerate the set of boost C++ which have similar replacements in standard C++. Replace the enumerated boost entities and integrate the changes in mainstream CMSSW.

## Necessary skills

Intermediate C++; Understanding of boost and STL.

## Mentors

  * [Vassil Vassilev](mailto:vvasilev@cern.ch)
  * [David Lange](mailto:David.Lange@cern.ch)

## Links

  * [cmssw github page](http://cms-sw.github.io/)
  * [boost web page](https://www.boost.org/)
