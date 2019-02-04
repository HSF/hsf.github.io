---
title: Improving the precision of algorithms to hunt particles
layout: gsoc_proposal
project: Acts, IRIS-HEP
year: 2019
organization:
- CERN
- UC Berkeley
- LBNL
---

## Description

Particle trajectories are determined by so-called pattern recognition algorithms, which use a multi-step process to join the dots corresponding to energy deposits in the detector from each particle (hits). Typically, this is done using the equations of motion of a particle in a non-uniform magnetic field implemented with a Kalman filter formalism. This project will focus on a simplified case of the algorithm, with a simple detector set up and no magnetic field, which means that the particles follow straight lines (instead of curves) through the detector, such as what is used in test-beam studies. A key element of this procedure is an accurate knowledge of position of the detector elements. This is determined by solving a high-dimensional minimisation problem, which will be a key element of this project. This is a non-trivial challenge due to degeneracies in the minimisation problem for such a geometry that require external constraints and in situ data.

[ACTS](http://cern.ch/acts) is a free and open-source software project for track reconstruction in particle physics experiments. As a modernized version of the particle tracking code used by the ATLAS experiment at the CERN Large Hadron Collider, the project is focused on adoption of modern C++ standards, usability in multi-threaded workflows, and increased use of vectorization.

This project gives a unique opportunity to contribute to the development of a key component of the pattern recognition of ACTS.

## Task ideas
 *
 * Evaluate current track following algorithms for test-beam geometries
 * Design event data model for detector alignment in ACTS
 * Establish strategies to solve higher dimensional minimisation alignment problems for test-beam geometries

## Expected results
An alignment package within ACTS that can be used to data from test-beam studies and used within track following algorithms.

## Requirements
C++

## Mentors
  * [Heather Gray](mailto:heather.gray@berkeley.edu)
  * [Xiaocong Ai](mailto:xiaocong.ai@cern.ch)

## Links
  * [Acts](http://cern.ch/acts)
  * [Telescope](https://telescopes.desy.de/Main_Page)
