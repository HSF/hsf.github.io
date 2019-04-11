---
title: Rucio - Exascale data management
layout: gsdocs_proposal
project: Rucio
year: 2019
organization:
 - UOslo
 - CERN
 - RAL
 - UWuppertal
 - UInnsbruck
---

## Description

Rucio is a software framework that provides functionality to organize, manage, and access large volumes of scientific data using customisable policies. The data can be spread across globally distributed locations and across heterogeneous data centers, uniting different storage and network technologies as a single federated entity. Rucio offers advanced features such as distributed data recovery or adaptive replication, and is highly scalable, modular, and extensible. Rucio has been originally developed to meet the requirements of the high-energy physics experiment ATLAS, and is continuously extended to support LHC experiments and other diverse scientific communities. For example, the ATLAS experiment orchestrated an Exabyte of data transfer and processing and is growing rapidly.

The current documentation is available from multiple places and in different formats, including [scientific articles](https://arxiv.org/abs/1902.09857), [readthedocs.io](https://rucio.readthedocs.io/en/latest/) with source in the [code](https://github.com/rucio/rucio/tree/master/doc/source), [Google Drive](https://drive.google.com/drive/folders/1EEN8l1dFjDSgavPrAMMooDjEodHP7aU7?usp=sharing), [Github](https://github.com/rucio/rucio), [DockerHub](https://hub.docker.com/u/rucio), or [Wikis](https://twiki.cern.ch/twiki/bin/view/AtlasComputing/AtlasDistributedComputing). This dispersion and diversity makes it difficult to pinpoint information and to recognise which information is outdated or superseded, wrong, or simply lacking in detail. Especially in Wikis the information is usually directed towards a single experiment instance of Rucio, however the underlying concepts can be applicable to multiple different instances. With this proposal we aim to consolidate and automate the documentation as much as possible. We believe that the best documentation is the one which can be generated from the code itself. In addition the manually written documentation, e.g. setup and tutorials, should also be brought into a single format from which it can be distributed automatically.


## Tasks

1. Consolidate and rewrite the service installation and configuration documentation
  - Several platforms need to be supported. Most importantly RedHat/CentOS, but also Debian and derivatives. Documentation for the setting up development environments should encompass even more platforms, such as macOS.
  - Multiple technologies are available such as PyPI, Docker, and Kubernetes. The documentation should be consistent across all of them.
2. Improve the client and REST API documentation
  - This is mostly derived from the code itself, however the process is still manual. This could be approached by either modifying the code to use tools like [Swagger](https://swagger.io), or prepare templates such that such tools can be used in the future.
3. Consolidate and rewrite the tutorials and operations manuals
  - First steps with the system (e.g. setting up users, accounts, storage)
  - How to use the system efficiently (e.g. guidelines on data models)
  - How to monitor the system effectively (e.g. how to setup dashboards)

## Mentors
- [Vincent Garonne](mailto:vgaronne@gmail.com), University of Oslo
- [Mario Lassnig](mailto:Mario.Lassnig@cern.ch), CERN
- [Martin Barisits](mailto:Martin.Barisits@cern.ch), CERN
- [Katy Ellis](mailto:katy.ellis@stfc.ac.uk), STFC RAL
- [Thomas Beermann](mailto:thomas.beermann@cern.ch), University of Wuppertal
- [Cedric Serfon](mailto:cedric.serfon@cern.ch), University of Innsbruck

## Links

- [Rucio Website](https://rucio.cern.ch)
- [Rucio Documentation](https://rucio.readthedocs.io/en/latest/)
- [Rucio Documentation Source](https://github.com/rucio/rucio/tree/master/doc/source)
- [Rucio Journal Article](https://arxiv.org/abs/1902.09857)
- [Rucio Github](https://github.com/rucio/rucio)
- [Rucio Docker](https://hub.docker.com/u/rucio/)
- [Rucio Workshop 2018](https://indico.cern.ch/event/676472/)
- [Rucio Workshop 2019](https://indico.cern.ch/event/773489/)
