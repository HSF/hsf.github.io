---
title: Monitoring DIRAC components
layout: gsoc_proposal
project: LHCb
year: 2018
organization: CERN
---

## Description

[LHCb](http://lhcb-public.web.cern.ch/lhcb-public/), the LHC "beauty" experiment, uses state of the art distributed computing technologies, integrating different kinds of computing and storage resources, including Grid and Cloud technologies. The physics data are processed and distributed using software solutions developed mostly by members of the LHCb collaboration. The [DIRAC](http://diracgrid.org/) interware is one of them. DIRAC is a complex, open source, very actively developed software, whose roles range from the submission of jobs, the management of the data produced, to the orchestration of the distributed resources, while providing active monitoring and key information for the whole LHCb collaboration. DIRAC is a generic software, used and extended by several Virtual Organizations (VO). LHCb is DIRAC's initiator and main contributor.

The student will contribute in developing DIRAC. The LHCb upgrade program will develop the LHCb detector, and the upgraded LHCb detector will record an unprecedented amount of data. Software like DIRAC will scale up to handle the increased workload. A DIRAC installation may include dozens of running components, including reactive services and proactive agents. Each component has a specific role, and can be installed, or de-installed, run, or stop, depending from its need. Most of them can be duplicated, for performance or availability reason. A single installation may need several server hosts. From a system administration point of view, managing a large installation is a challenge. For an optimal management DIRAC components should be carefully monitored. Each component may use several threads or processes, may need to use intensively the system's memory, or the network. Components may also be running on partially faulty hosts. The project aims at developing tools for collecting dynamic information about DIRAC components. Scalability of the system needs to be assured, also considering the above mentioned upgrade program. For this reason, the student will use NoSQL technologies to achieve this goal.


## Task ideas

 * Use the DIRAC's components' profiler to store components' status to an ElasticSearch backend
 * Define an optimal indexing strategy
 * Use DIRAC's Monitoring Service and web app to visualize status of running components
 * Use DIRAC's gMonitor object to send in-components information to the ElasticSearch backend


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
