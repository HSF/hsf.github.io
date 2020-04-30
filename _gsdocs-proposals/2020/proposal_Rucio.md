---
title: Rucio - Exascale data management
layout: gsdocs_proposal
project: Rucio
year: 2020
organization:
  - CERN
---

## Description of project idea

Rucio is a software framework that provides functionality to organize, manage, and access large volumes of scientific data using customisable policies. The data can be spread across globally distributed locations and across heterogeneous data centers, uniting different storage and network technologies as a single federated entity. Rucio offers advanced features such as distributed data recovery or adaptive replication, and is highly scalable, modular, and extensible. Rucio has been originally developed to meet the requirements of the high-energy physics experiment ATLAS, and is continuously extended to support LHC experiments and other diverse scientific communities. For example, the ATLAS experiment orchestrated an Exabyte of data transfer and processing and is growing rapidly.

The current documentation is available from multiple places and in different formats, including [scientific articles](https://arxiv.org/abs/1902.09857), [readthedocs.io](https://rucio.readthedocs.io/en/latest/) with source in the [code](https://github.com/rucio/rucio/tree/master/doc/source), [Google Drive](https://drive.google.com/drive/folders/1EEN8l1dFjDSgavPrAMMooDjEodHP7aU7?usp=sharing), [Github](https://github.com/rucio/rucio), [DockerHub](https://hub.docker.com/u/rucio), or [Wikis](https://twiki.cern.ch/twiki/bin/view/AtlasComputing/AtlasDistributedComputing). This dispersion and diversity makes it difficult to pinpoint information and to recognise which information is outdated or superseded, wrong, or simply lacking in detail. Especially in Wikis the information is usually directed towards a single experiment instance of Rucio, however the underlying concepts can be applicable to multiple different instances.

With this proposal we aim to achieve the following tasks:

  * Due to this wide dispersion of different documentation pieces, we want to move our documentation to one central place. Possibly based on mkdocs, but we are open to other documentation technology.
  * Restructure the documentation into clear and distinct parts. (User Howtos, Setup and tutorials, Operators documentation, Developer documentation, etc.)
  * Consolidate the different sources and integrate them into this new structure.
  * Write new documentation, to connect the different pieces where applicable.

## Project duration

We are open to both 3 month and 6 month projects, depending on what you think is required to achieve these tasks.

## Related material

- [Rucio Website](https://rucio.cern.ch)
- [Rucio Documentation](https://rucio.readthedocs.io/en/latest/)
- [Rucio Documentation Source](https://github.com/rucio/rucio/tree/master/doc/source)
- [Rucio Journal Article](https://arxiv.org/abs/1902.09857)
- [Rucio Github](https://github.com/rucio/rucio)
- [Rucio Docker](https://hub.docker.com/u/rucio/)
- [Rucio Workshop 2018](https://indico.cern.ch/event/676472/)
- [Rucio Workshop 2019](https://indico.cern.ch/event/773489/)
- [Rucio Workshop 2020](https://indico.cern.ch/event/867913/)

## Expected results
One central documentation page servicing the different types of users. The different existing documentation sources should all be consolidated in this documentation page and restructured. New documentation, especially to support the information flow, should be written.

## Experience required
General knowledge of Python, Docker, GIT is required.

## Mentors
  * [Martin Barisits](mailto:Martin.Barisits@cern.ch), CERN
  * [Mario Lassnig](mailto:Mario.Lassnig@cern.ch), CERN
