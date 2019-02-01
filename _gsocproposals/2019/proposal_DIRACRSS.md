---
title:  "Distributed Computing Resources: aggregation, usage, monitoring"
layout: gsoc_proposal
project: DIRAC
year: 2019
organization: CERN
---

## Description

[LHCb](http://lhcb-public.web.cern.ch/lhcb-public/), the LHC "beauty" experiment, uses state of the art distributed computing technologies, integrating different kinds of computing and storage resources, including Grid and Cloud echnologies. The physics data are processed and distributed using software solutions developed mostly by members of the LHCb collaboration. The DIRAC interware is one of them. DIRAC is a complex, open source, very actively developed software, whose roles range from the submission of jobs, the management of the data produced, to the orchestration of the distributed resources, while providing active monitoring and key information for the whole LHCb collaboration. DIRAC is a generic software, used and extended by several Virtual Organizations (VO). LHCb is DIRAC's initiator and main contributor. The student will contribute in developing DIRAC.

DIRAC acts as an IT resources aggregator. Resources can be computing, storage, or catalog resources. But resources can also be networks, information providers, file transfer services, message queues or databases services. For an optimal management DIRAC resources should be carefully categorized, and monitored. Organizations using a distributed computing model are faced with non-traditional administrative challenges: the heterogeneous nature of the underlying resources requires professionals acting as resource administrators. Members of a VO can use a mask composed by services exposed by local resources. Experienced Grid administrators apply procedures for managing such services, based on their status, as it is reported by an ever-growing set of monitoring tools. When a procedure is agreed and well-exercised, a formal policy could be derived.

For this reason, using the DIRAC framework in the LHCb collaboration, we developed a policy system that can enforce management and operational policies, in a VO-specific fashion. The student will contribute in the developing of such a system, that applies autonomic computing technologies for a better management of the VO resources and services. Autonomic computing is a field gaining more and more interests in the distributed computing community.

## Task ideas

 * Modify DIRAC RSS MySQL database for hosting VO-dependent status
 * Unify sqlAlchemy frontend
 * Develop code compatible with python 3

## Expected results
 * working implementation with tests and documentation

## Requirements

 * python
 * git
 * Linux
 * some experience with relational database (MySQL)
 * experience with sqlAlchemy is a plus

## Mentors

 * [Federico Stagni](mailto:federico.stagni@cern.ch)
 * [Christophe Haen](mailto:christophe.denis.haen@cern.ch)
 * [Zoltan Mathe](mailto:zoltan.mathe@cern.ch)

## Links

 * [diracgrid.org](http://diracgrid.org/)
 * [source code](https://github.com/DIRACGrid)
