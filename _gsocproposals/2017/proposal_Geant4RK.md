---
title: New error control methods for integration of trajectories
layout: gsoc_proposal
project: Geant4
year: 2017
organization:
  - CERN
---

## Description
Geant4 and GeantV use Runge-Kutta methods to integrate the motion of charged particles in a non-uniform electromagnetic field.  Methods must provide good integration accuracy for the integration and to cost a minimum of computation time.  Integration is used to identify the intersection point between the curved track and the volume boundaries.  Due to the large number of steps and the cost of the evaluations of the field, the integration and intersection are a performance critical part of detector simulation. Recent work has introduced new RK methods which reduce the number of field evaluations required, and has the potential to decreased the computation time.

## Task ideas
 * Introduce new methods for the control of integration error of existing integration Runge Kutta methods.
 * Create heuristics for choosing an appropriate method (helix, RK of particular order, Burlich/Stoer), using knowledge of the accuracy requirements and the variation of the derivative in the proposed step.
 
## Expected results
Working implementation of:

* improved alternative error control methods for RK integration, and/or 
* integration methods which combine different methods, e.g. RK methods of different order for improved performance.

## Requirements
This project requires prior exposure to Numerical Analysis and familiarity with either C++, C or Java programming.  Exposure to either numerical methods for solving Ordinary Differential equations (ODEs) or tools for analysing data such as ROOT or R will be valuable. Both programming skill and knowledge of numerical methods for ODEs will be improved by undertaking this project.

## Mentor 
[John Apostolakis](mailto:sft-gsoc@cern.ch)

## Web site
[http://cern.ch/geant4](http://cern.ch/geant4)

## Source code
[https://github.com/jonapost/field_propagation](https://github.com/jonapost/field_propagation)
