---
title: Real-time conditions data distribution for the Online data processing of the ALICE experiment
layout: gsoc_proposal
project: ALICE
year: 2019
organization:
  - CERN
---

## Description
The new ALICE [1] synchronous data reconstruction facility for Run 3 [2] needs a real-time conditions and calibration data distribution mechanism. New calibration objects are produced at up to 50Hz and have to be propagated to about 2000 servers. For efficient data distribution in this environment a network multicast delivery mechanism has to be used. There will be two sides to be implemented for this project: a library to send the newly produced objects and a caching service to run on each of the 2000 servers to receive and keep in memory the objects, making them available to the localhost running processes via a REST API (already defined for the central repository implementation [3, 4]).

## Task ideas
  * Find a reliable way to fragment and reassemble large objects (10MB or more) via UDP multicast
  * Develop a C++ library that implements the fragmented sending of objects
  * Develop a similar library in Java
  * Implement the multicast receiver of such objects, in Java
  * Implement the REST API giving access to the cached objects in memory, based on Tomcat
  * Implement the fallback to reading the full object content from the central repository (using the same REST API upstream)

## Expected results
Two multicast sending libraries and a receiving service that also implements a REST API for serving the objects from memory.

## Desirable Skills
  * C++
  * Java
  * Git
  * Network programming

## Mentors
  * [Costin Grigoras](mailto:costin.grigoras@cern.ch)
  * [Latchezar Betev](mailto:latchezar.betev@cern.ch)

## Links
   1. [ALICE experiment at CERN](https://home.cern/science/experiments/alice)
   2. [ALICE Run 3 upgrade Technical Design Report](https://cds.cern.ch/record/2011297/files/ALICE-TDR-019.pdf)
   3. [ALICE CCDB status](https://docs.google.com/presentation/d/1RMIzqHL1JnDhwmqGj_yTmxqjNb54hNoJwvFIgtldR6g/edit#slide=id.g25765cf80e_0_3)
   4. [ALICE CCDB repository](https://gitlab.cern.ch/grigoras/ccdb-local)
