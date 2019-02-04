---
title: Rucio - WebDAV/HTTP-based transfer orchestration
layout: gsoc_proposal
project: Rucio
year: 2019
organization:
 - CERN
---

## Description

Rucio is a data management system for modern large-scale scientific experiments. It allows experiments to deal with vast amounts of data in a scalable, modular, and flexible way. For example, the ATLAS experiment orchestrated an Exabyte of data transfer and processing and is growing rapidly. Many exciting experiments have adopted Rucio or are actively evaluating it. To orchestrate these global transfers between data-centres, Rucio supports pluggable external transfer tools dedicated to large-scale experiments. However, especially for smaller communities the deployment and operation of such an external transfer tool involves a significant amount of operations and resources. For this reason we are seeking a motivated student to design, implement, and test a lightweight WebDAV/HTTP-based transfer tool that supports the Rucio transfertool API natively and internally. If you are interested in large-scale data management, networked systems, and open protocols then come and join our open development team and contribute to Github repository!

## Task idea

Development of a plugin module for the Rucio transfer system, which can enable third-party copy of files using the WebDAV/HTTP standard.

## Expected results

### Objective 1 - Setup a Rucio development environment

- We can serve either Docker-based development environments, or completely custom installations on UNIX-based systems.

### Objective 2 - Design an architecture for a lightweight WebDAV/HTTP-based transfer tool

- There are template transfer tools available to guide the student, to help with the design.
- There exists an RFC for a WebDAV/HTTP third party copy verb, which might be useful to evaluate.

### Objective 3 - Implement the lightweight WebDAV/HTTP-based transfer tool

- We can provide test endpoints to the student, to implement the transfer tool under real experiment conditions.
- Successfully enable periodic functional test in our production environment.

### Objective 4 - Report

- We host weekly collaboration meetings, and we would like that the student presents at the end of GSoC a talk about the experience.

## Requirements

- Python
- Linux development environment (bash, git, ...)

## Mentors

- [Martin Barisits](mailto:Martin.Barisits@cern.ch)
- [Mario Lassnig](mailto:Mario.Lassnig@cern.ch)
- [Cedric Serfon](mailto:Cedric.Serfon@cern.ch)

## Links

- [Rucio Website](https://rucio.cern.ch)
- [Rucio Github](https://github.com/rucio/rucio)
- [Rucio Documentation](https://rucio.readthedocs.io/en/latest/)
- [Rucio Workshop 2018](https://indico.cern.ch/event/676472/)
