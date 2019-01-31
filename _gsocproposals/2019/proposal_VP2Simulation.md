---
title: Introduction of Time Measurements in the Pattern Recognition for LHCb's Future Vertex Detector
layout: gsoc_proposal
project: LHCb
year: 2019
organization:
  - Nikhef
---

## Description

LHCb [1] is a general purpose forward detector at CERN's Large Hadron
Collider. Research using LHCb data focusses on: high-precision
measurements of the properties and decay of particles that contain
heavy quarks such as charm and beauty quarks, extremely rare decays,
forward elektroweak physics and even the physics of heavy-ion
collisions.

The LHCb Vertex Locator is the detector closest to the point where
protons collide in the LHC and is designed to precisely measure the
trajectories of particles created in these collisions. It consist of
approximately 50 layers of silicon pixel sensors that measure the
charge deposited by particles that traverse them.

The LHCb experiment is currently being upgrade to be able to cope with
a 5 times higher number of collisions per second. To further extend
the scientific reach of the experiment, another upgrade is foreseen to
be installed in 2030, which is intended to be able to cope with
another factor of 10 increase in the number of proton-proton
collisions per second. Studies of the technology for this future
detector are now underway.

Nikhef [2] is the Dutch institure for sub-atomic physics and it's LHCb
research group is involved in designing the Vertex Detector (VP2) for
LHCb's 2030 upgrade.

For the physics research to be possible, it is of critical importance
that trajectories of particles traversing the future VP2 detector can
be found with high probability in the raw pixel data.

This project proposes to extend an existing algorithm that
reconstructs particle trajectories [3] by augmenting it with
information about the measured time of traversal of particles.

## Task ideas
  * Add time-of-traversal information to the existing algorithm
  * Test the impact on the CPU performance of the algorithm, its
    capacity for finding trajectories, and the number of wrongly found
    trajectories
  * Test the performance of the algorithm as a function of the
    accuracy of the provided time measurements
  * Test the performance of the algorithm as a function of the
    number of simultaneous proton-proton collisions

## Expected results
Assessment of the performance of a pattern-recognition algorithm that
has been augmented with the time-of-traversal of particles in terms of
computational performance and ability to find trajectories.

## Desirable Skills
  * C++ knowledge
  * Interest in pattern recognition algorithms

## Mentors
  * [Daniel Hynds](mailto:d.hynds@nikhef.nl)
  * [Roel Aaij](mailto:roelaaij@nikhef.nl)
  * [Gerhard Raven](mailto:g.raven@nikhef.nl)

## Links
   1. [https://lhcb.web.cern.ch](https://lhcb.web.cern.ch)
   2. [https://www.nikhef.nl](https://www.nikhef.nl)
   3. [https://www.nikhef.nl](https://gitlab.cern.ch/raaij/spmd_test)
