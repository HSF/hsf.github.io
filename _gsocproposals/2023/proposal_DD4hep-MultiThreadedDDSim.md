---
project: DD4hep
title: Multithreaded simulations in DD4hep with DDSim
layout: gsoc_proposal
year: 2023
difficulty: medium
duration: 175
mentor_avail: May-October
organization:
  - CERN
  - UManitoba
---

## Description
DD4hep is a detector description toolkit for high energy physics used for simulations of detectors using the geant4 particles through matter simulation code. In addition to providing a detector geometry description layer on top of geant4, DD4hep provides alignment, CAD, digitization, reconstruction, and other modules. Although some projects use custom infrastructure to steer simulations, DD4hep comes standard with DDSim: a versatile python-based utility to run simulations on the command line. DDSim is currently focused on single-threaded running of geant4 simulations. In recent geant4 versions, multithreaded running of geant4 has become more common. In this project, we wish for the DDSim tool to be converted to allow the use of multithreaded geant4. The outcome of this project will allow for DD4hep simulations to run on high performance computing systems.

## Task ideas
 * Evaluate the current DDSim implementation (and underlying python module DDHepSimulation) and identify the main modes of operation.
 * Identify the changes needed to DDSim to allow for running with a multithreaded geant4 backend.
 * Identify any DD4hep plugins (e.g. IO) that are not able to support multithreaded running.
 * Ensure that at least the HepMC3 input and EDM4hep output plugins support multithreading.
 * Assess performance scaling of DDSim simulations with multithreading enabled.
 * Implemented new command line interface supports to control multithreaded operation.
 * Maintain full backwards compatibility with single-threaded operation command line interface.

## Expected results
The expected result is to be able to run DDSim with geant4 in multithreaded mode using a backwards compatible command line interface that accepts the same arguments as it does for single-threaded operation.

## Evaluation Task
Interested students please contact the mentors for more details and an evaluation task.

## Requirements
 * Knowledge of C++ is required, in particular in the context of multithreaded programs (mutexes, resource sharing).
 * Knowledge of python is required, in particular in the context of orchestration of C++ plugins.

## Mentors
 * **[Wouter Deconinck](mailto:wouter.deconinck@umanitoba.ca)** UManitoba
 * [Andre Sailer](mailto:andre.sailer@cern.ch) CERN

## Links
- https://dd4hep.web.cern.ch/dd4hep/
