---
title: Rucio - Exascale data management
layout: gsdocs_proposal
project: Rucio
year: 2019
organization:
 - UOslo
 - CERN
 - RAL
---

## Description

Rucio is a software framework that provides functionality to organize, manage, and access large volumes of scientific data using customisable policies. The data can be spread across globally distributed locations and across heterogeneous data centers, uniting different storage and network technologies as a single federated entity. Rucio offers advanced features such as distributed data recovery or adaptive replication, and is highly scalable, modular, and extensible. Rucio has been originally developed to meet the requirements of the high-energy physics experiment ATLAS, and is continuously extended to support LHC experiments and other diverse scientific communities. For example, the ATLAS experiment orchestrated an Exabyte of data transfer and processing and is growing rapidly.

The current documentation is available from multiple places and in different formats, including readthedocs.io, Google Docs, Github, DockerHub, and Wikis. This dispersion and diversity makes it difficult to pinpoint information and to recognise which information is outdated or superseded, wrong, or simply lacking in detail. With this proposal we aim to automate this process as much as possible, as we think that the best documentation is the one which can be generated from the code itself. In addition, the manually written documentation, e.g., setup and tutorials, should also be brought into a single format from which it can be distributed automatically. We target the following structure with single entry points:

1. Service installation and configuration
  - Available for several platforms (RedHat/CentOS, Debian)
  - Using multiple technologies (PyPI, Docker, Kubernetes)
2. Client and REST API
  - Derived from the code itself, using tools, e.g., like https://swagger.io
3. Tutorials and operations
  - First steps with the system (e.g., setting up users, accounts, storage)
  - How to use the system efficiently (e.g., guidelines on data models)
  - How to monitor the system effectively (e.g., how to setup dashboards)

## Mentors
- [Vincent Garonne](mailto:vgaronne@gmail.com)
- [Mario Lassnig](mailto:Mario.Lassnig@cern.ch)
- [Martin Barisits](mailto:Martin.Barisits@cern.ch)
- [Katy Ellis](mailto:katy.ellis@stfc.ac.uk)

## Links

- [Rucio Website](https://rucio.cern.ch)
- [Rucio Documentation](https://rucio.readthedocs.io/en/latest/)
- [Rucio Github](https://github.com/rucio/rucio)
- [Rucio Docker](https://hub.docker.com/u/rucio/)
- [Rucio Workshop 2018](https://indico.cern.ch/event/676472/)
- [Rucio Workshop 2019](https://indico.cern.ch/event/773489/)
