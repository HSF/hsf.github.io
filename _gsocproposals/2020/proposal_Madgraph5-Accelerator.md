---
title: MadGraph5 - offload event execution to accelerator devices
layout: gsoc_proposal
project: MadGraph5
year: 2020
organization:
  - CERN
---

## Description
High energy physics experiments such as the Large Hadron Collider (LHC) experiments at CERN rely heavily on so called “Monte Carlo (MC) Simulations” to achieve their physics research goals. MC simulations mimic in a computer program the initial collision of particles in a high energy physics collider and their subsequent response inside a physics detector.

LHC experiments use a distributed computing environment of up to 500.000 computing cores and several exa-bytes of disk and tape storage for its data processing and the vast majority of the available CPU power (70 - 80 %) is used for MC simulations. Recently the provisioning of compute accelerators, such as General Purpose Graphics Processing Units (GPUs), has become popular in this computing infrastructure in addition to classical x86 Intel CPUs.

Looking at the workflow of a simulation program, the very first step of it is the so called “event generation” where the initial collision of the particles in the collider is simulated. These event generators are historically written for classical x86 intel compatible architectures. With the shift of the distributed computing environment towards GPUs it is essential to make MC Generators also fit for use on those architectures.

## Task ideas
The student will work with one of the most utilised MC Generators, called Madgraph. The tasks to be executed include

 * Profile Madgraph in view of CPU consumption
 * Investigate the possibility of reengineering generator code to implement data parallelism
 * Prototype code for the offloading of the above identified parts onto an accelerator device

## Expected results
The deliverable of the project is a performance study of the Madgraph5 event generator showing hotspots in the CPU consumption during the execution. One or several of those hotspots shall be implemented on an accelerator device and integrated into the overall program workflow. 

## Requirements
We're seeking a candidate proficient in Python and C. Knowledge in GPU programming (preferably Cuda) and performance measurement tools is advantageous.

## Mentors
  * [Olivier Mattelaer](mailto:olivier.mattelaer@uclouvain.be)
  * [Stefan Roiser](mailto:stefan.roiser@cern.ch)
  * [Andrea Valassi](mailto:andrea.valassi@cern.ch)

## Links
  * [MadGraph5](https://launchpad.net/mg5amcnlo)
