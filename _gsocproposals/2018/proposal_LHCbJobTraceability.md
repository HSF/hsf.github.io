---
title: Monitoring and traceability of jobs in a large distributed computing Grid
layout: gsoc_proposal
project: LHCb
year: 2018
organization: CERN
---

## Description

[LHCb](http://lhcb-public.web.cern.ch/lhcb-public/), the LHC "beauty" experiment, uses state of the art distributed computing technologies, integrating different kinds of computing and storage resources, including Grid and Cloud technologies. The physics data are processed and distributed using software solutions developed mostly by members of the LHCb collaboration. The [DIRAC](http://diracgrid.org/) interware is one of them. DIRAC is a complex, open source, very actively developed software, whose roles range from the submission of jobs, the management of the data produced, to the orchestration of the distributed resources, while providing active monitoring and key information for the whole LHCb collaboration. DIRAC is a generic software, used and extended by several Virtual Organizations (VO). LHCb is DIRAC's initiator and main contributor.

The student will contribute in developing DIRAC. Communities use DIRAC to submit jobs to hundreds of heterogeneous computing resources, with several tens of thousands of jobs running concurrently. Monitoring is essential. Traceability of each of the submitted jobs is key when security checks are needed. The student will extend the current job monitoring system, currently based upon relational databases, by using non-relational state-of-the-art solutions.

The student will have the opportunity to see at work a large distributed computing infrastructure, and to understand the needs for it. The student will discover different ways of computing, including Grid and Cloud.


## Task ideas

 * Store DIRAC jobs' parameters in the ElasticSearch backend
 * Define an optimal indexing strategy
 * Assure backword-compatibility with SQL-based solution

## Expected results
* working implementation with tests and documentation


## Requirements

* python
* git
* Linux
* some experience with non-relational database
* some experience with real-time and/or distributed computing software is preferred


## Mentors

 * [Federico Stagni](mailto:federico.stagni@cern.ch)
 * [Zoltan Mathe](mailto:zoltan.mathe@cern.ch)
 * [Christophe Haen](mailto:christophe.denis.haen@cern.ch)


## Links
 * [diracgrid.org](http://diracgrid.org/)
 * [source code](https://github.com/DIRACGrid)
