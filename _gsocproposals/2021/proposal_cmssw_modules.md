---
title: Developing C++ modules support in CMSSW and Boost
layout: gsoc_proposal
project: IRIS-HEP
year: 2021
organization: princeton
---

## Description

The LHC smashes groups of protons together at close to the speed of light: 40 million times per second and with seven times the energy of the most powerful accelerators built up to now. Many of these will just be glancing blows but some will be head on collisions and very energetic. When this happens some of the energy of the collision is turned into mass and previously unobserved, short-lived particles – which could give clues about how Nature behaves at a fundamental level - fly out and into the detector. Our work includes the experimental discovery of the Higgs boson, which leads to the award of a Nobel prize for the underlying theory that predicted the Higgs boson as an important piece of the standard model theory of particle physics.

CMS is a particle detector that is designed to see a wide range of particles and phenomena produced in high-energy collisions in the LHC. Like a cylindrical onion, different layers of detectors measure the different particles, and use this key data to build up a picture of events at the heart of the collision.

Last year, thanks to [Lucas Calmolezi and GSoC](https://summerofcode.withgoogle.com/archive/2020/projects/5397144158076928/),
the usage of boost in CMSSW was modernized. It improved the C++ modules support of local boost fork.

## Task ideas and expected results

Many of the accumulated local patches add missing includes to the relevant boost header files. The candidate should start by proposing the existing patches to the boost community. Try to compile more boost-specific modules which is mostly a mechanical task. The student should be ready to work towards making the C++ module files more efficient containing less duplications. The student should be prepared to write a progress report and present the results.


## Mentors

  * **[David Lange](mailto:david.lange@cern.ch)**
  * [Vassil Vassilev](mailto:vvasilev@cern.ch)

## Links
  * [cmssw github page](http://cms-sw.github.io/)
  * [boost web page](https://www.boost.org/)
  