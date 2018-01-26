---
title: Utilise RK interpolation and vectorisation for field propagation
layout: gsoc_proposal
project: Geant4
year: 2018
organization:
  - CERN
---

# Description
Geant4 offers a variety of Runge-Kutta methods to integrate the motion of charged particles in a non-uniform electromagnetic field. In GeantV adapted RK methods are being vectorised to handle
multiple tracks efficiently.  Integration is used for the motion of charged particle and to identify the intersection point between the curved track and the volume boundaries.
Due to the large number of steps and the cost of the evaluations of the field, the integration and intersection are a performance critical part of detector simulation.  So integration methods must
provide adequate accuracy while take as little computation time as possible, and thus a minimum of calls to evaluate the EM field.
Past GSoC work introduced new RK methods with an interpolation capability for intermediate points; optimally utilising this should reduce, potentially substantially, the number of field evaluations.
The potential to create a vectorised version of leading embedded RK methods for a single track could provide benefits from vectorisation to Geant4 and to the portion of GeantV tracking which occurs in single track mode.

# Task ideas
 * Adapt integration methods with interpolation into Geant4 field propagation,
 * Develop vectorised implementation of RK steppers for integration of single track using the VecCore library,
 * Create heuristics for choosing an appropriate method (helix, RK of particular order, Burlich/Stoer), using knowledge of the accuracy requirements and the variation of the derivative in the proposed step.

# Requirements
This project requires prior exposure to Numerical Analysis and familiarity with either C++, C or Java programming.
Exposure to either numerical methods for solving Ordinary Differential equations (ODEs), vectorisation techniques
or tools for analysing data such as R, numpy or ROOT will be valuable. Both programming skill and knowledge of
numerical methods for ODEs will be improved by undertaking this project. 

# Mentors 
* [John Apostolakis](mailto:sft-gsoc@cern.ch)
* [Dmitry Sorokin](mailto:sft-gsoc@cern.ch)

# Web site 
[http://cern.ch/geant4](http://cern.ch/geant4)
[http://geant.cern.ch/](http://geant.cern.ch/)

# Source code 
[https://github.com/jonapost/fieldpropagation](https://github.com/jonapost/fieldpropagation)
