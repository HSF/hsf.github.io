---
title: Local replica of JAliEn central services for research and development
layout: gsoc_proposal
project: ALICE
year: 2020
organization:
  - CERN
---

## Description
The [ALICE Experiment](https://home.cern/science/experiments/alice) at the [CERN](https://home.cern) LHC is preparing for the restart of the [LHC](https://home.cern/science/accelerators/large-hadron-collider) (Run3) in 2021. To that end, a new Grid framework [JAliEn](https://gitlab.cern.ch/jalien/jalien) with extended capabilities is being developed and tested as the successor of the [AliEn](https://alien.web.cern.ch) framework.

This framework will be deployed on a set of central services as well as on more than 80 individual [computing sites](http://alimonitor.cern.ch/map.jsp), which provide CPU and storage resources for ALICE.

To streamline the development and to give the individual developers a robust local development framework with all necessary capabilities, the core of the JAliEn system (JCentral) must be deployed individually, on a single host, with all necessary configurations.

In this project, the student will develop a procedure for creating a JCentral replica. The end goal of this project is a command line utility that lets JAliEn developers quickly start and destroy the local replicas.

## Task ideas
 * Become familiar with the existing Java based setup scripts;
 * Port the Java setup scripts to a language agnostic format;
 * Develop a command line utility that unifies the individual scripts.

## Expected results
  * a modern command line utility for creating JAliEn Grid replicas quickly and easily

## Requirements
  * Interest in distributed systems
  * Comfortable working in Linux environment
  * Experience with containerization technologies and scripting is a plus

## Mentors
 * [Nikola Hardi](mailto:nhardi@cern.ch) (primary)
 * [Costin Grigoras](mailto:consting@cern.ch) (backup)

## Links
 * [JAliEn git repository](https://gitlab.cern.ch/jalien/jalien)
 * [ALICE Grid Monitoring](http://alimonitor.cern.ch)
