---
title: Multi-thread safe resource monitoring infrastucture for the ATLAS experiment
layout: gsoc_proposal
project: ATLAS
year: 2019
organization:
  - UCIrvine
  - UOslo
  - USheffield
---

## Introduction
[ATLAS](http://atlas.cern) is one of the four major experiments at the [Large Hadron Collider](http://home.web.cern.ch/topics/large-hadron-collider) (LHC) at [CERN](http://home.cern/).
It is a general-purpose particle physics experiment run by an international collaboration and is designed to exploit the full discovery potential and the huge range of physics opportunities that the LHC provides.

[Athena](https://gitlab.cern.ch/atlas/athena) is the ATLAS software framework that manages almost all ATLAS
bulk production workflows: the simulation of LHC events inside the ATLAS detector,
the reconstruction of physics quantities from the detector's output, and the
preparation of slimmed down files that physicists use for their analysis.
It is written in C++ and Python and based on the [Gaudi](https://gitlab.cern.ch/gaudi) framework that is also used by the [LHCb](http://lhcb.cern.ch/) experiment.
As part of the readiness for the LHC Run-3 data-taking, which is expected to
begin in 2021, the Athena framework is being upgraded to run in multi-threaded
(MT) environment, the project is named *AthenaMT*.

## Description
Performance of ATLAS simulation and reconstruction code is of immense importance in order to work with ever-growing datasets within constrained computing resources, even more so as we look forward to data from the next
stage of the LHC, the high-luminosity upgrade (HL-LHC).
Understanding Athena's performance guides the developers to improve the quality of the software and also ensures the ATLAS production workflows can run smoothly on the existing computing infrastructure.
It is essential to closely monitor the CPU, memory, and disk usage, identify bottlenecks as they appear and fix any issues rapidly.
Without this monitoring, repercussions as severe as loosing data can arise.

The current Athena infrastructure that is in place to monitor the resource usage of ATLAS jobs can only handle single-thread tasks.
The goal of this project is to upgrade the Athena monitoring infrastructure such that it can handle MT jobs, natively.
Although the monitoring software is closely tied to the Gaudi/Athena framework, it requires only minimal understand of the underlying code base
and the project is fairly self-contained.
The code development will predominantly be in C++.

## Task ideas
 * C++ implementation of the MT-safe performance (CPU, memory, IO) monitoring (per domain/algorithm counters).
 * Publishing the results (both in human-readable and non-human-readable formats).
 * Data visualization (e.g. elasticsearch/kibana).
 * Testing the implementation various ATLAS production workflows.

## Expected results
 * The core of the MT-safe performance monitoring infrastructure,
 * Demonstration/validation of the implemented software.

## Requirements
 * C++
 * Python

## Mentors
  * [Alaettin Serhan Mete](mailto:serhanmete@gmail.com)
  * [Davide Costanzo](mailto:davide.costanzo@gmail.com)
  * [James Catmore](mailto:james.catmore@cern.ch)

## Links
  * [Athena](https://gitlab.cern.ch/atlas/athena)
