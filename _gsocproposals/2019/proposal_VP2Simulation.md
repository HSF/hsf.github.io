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
Collider. To further extend the scientific reach of the experiment, a
future upgrade is foreseen to be installed in 2030, which is intended
to be able to cope with a factor of 10 increase in the number of
proton-proton collisions per second. Studies of the technology for
this future detector are now underway.

Nikhef [2] is the Dutch institute for sub-atomic physics and its LHCb
research group is involved in designing the Vertex Detector (VP2) for
LHCb's 2030 upgrade.

For the physics research to be possible, it is of critical importance
that trajectories of particles traversing the future VP2 detector can
be found with high probability in the raw pixel data.

This project proposes to extend an existing algorithm that
reconstructs particle trajectories [3] by augmenting it with
information about the measured time of traversal of particles.

The initial goal of the project is a working algorithm that can be
used to optimize the design of the VP2 detector. A secondary goal is
to optimize the performance of the developed algorithm to approach the
goal of processing data from at least 100,000 batches of 50
simultaneous collisions per second on a fully-loaded PC-server in
2030.

## Task ideas
  * Add time-of-traversal information to the existing algorithm
  * Using on the time information, optimize the CPU performance of the
    algorithm, together with its capacity for finding trajectories and
    rejecting wrongly found trajectories
  * Analyze the performance of the algorithm as a function of the
    accuracy of the provided time measurements

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
  * [Gerhard Raven](mailto:gerhard.raven@nikhef.nl)

## Links
   1. [https://lhcb.web.cern.ch](https://lhcb.web.cern.ch)
   2. [https://www.nikhef.nl](https://www.nikhef.nl)
   3. [https://gitlab.cern.ch/raaij/spmd_test](https://gitlab.cern.ch/raaij/spmd_test)
