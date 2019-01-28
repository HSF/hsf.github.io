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

[Athena](https://gitlab.cern.ch/atlas/athena) is the name of the ATLAS software framework that manages almost all ATLAS production workflows: event generation, simulation, reconstruction and derivation production.
It is written in C++ and Python and based on the [Gaudi](https://gitlab.cern.ch/gaudi) framework that is also used by the [LHCb](http://lhcb.cern.ch/) experiment.
As part of the readiness for the LHC Run-3 data-taking that is expected to begin in 2021, the Athena framework is being upgraded to run in multi-threaded (MT) enviroment, the project is also named AthenaMT.  

## Description
It goes without saying that measuring and profiling the software performance of the ATLAS code is of utmost importance. 
It does not only guide the developers to improve the quality of the software but also ensures the ATLAS production workflows can run smoothly on the existing computing infrastructure.
It is essentialy to closely monitor the cpu, memory, and disk usage, identify the bootlenecks as they appear and fix the issues immediately.
Failing this, repercussions as sever as loosing data can arise.

Current Athena infrastruction that is in place to monitor the resoruce usage of ATLAS jobs can only handle single-thread tasks.
The goal of this project is to upgrade the Athena monitoring infrastruction such that it can handle MT jobs, natively.  
Although the monitoring software is closely tied to the Gaudi/Athena frameworks, it would require some minimal understand of the underlying code base.
However, the project is expected to be fairly self-contained. 
The code development will predominantly be in C++. 

## Task ideas
 * C++ implementation of the MT-safe performance (cpu, memory, IO) monitoring (per domain/algorithm counters),
 * Publishing the results (both in human-readable and non-human-readable formats), 
 * Data visualization (e.g. elasticsearch/kibana),
 * Testing the implementation various ATLAS production workflows.
 
## Expected results
 * The core of the MT-safe performance monitoring infrastructre,
 * Demonstration/validation of the implemented software.

## Requirements
C++
Python

## Mentors 
  * [Alaettin Serhan Mete](mailto:serhanmete@gmail.com)
  * [Davide Costanzo](mailto:davide.costanzo@gmail.com)
  * [James Catmore](mailto:james.catmore@cern.ch)

## Links
  * [Athena](https://gitlab.cern.ch/atlas/athena)

{% include gsoc_project.ext %}
