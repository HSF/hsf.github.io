---
title: Rucio - Exascale data management
layout: gsoc_proposal
project: Rucio
year: 2019
organization:
 - CERN
---

## Description

Rucio is a data management system for modern large-scale scientific experiments. It allows experiments to deal with vast amounts of data in a scalable, modular, and flexible way. For example, the ATLAS experiment orchestrated an Exabyte of data transfer and processing and is growing rapidly. Many exciting experiments have adopted Rucio or are actively evaluating it. We seek a student to help us out with designing, developing, testing, and putting in production several highly sought after features in the Rucio core to be prepared for the future. Concepts like horizontal scalability, distributed algorithms, large scale databases, performance optimisation, or network communication protocols interest you? Then you are the GSoC student we seek! Come and join an open development team, contribute to our Github repository, and help improve the world of scientific data management!

## Task ideas

- Automatic recovery of suspicious files on storage
- Automatic request queue shuffling based on storage type
- Diagnosis and rerouting of impossible transfer rules
- Protect storage access from too many concurrent requests
- Transform database-specific PL/SQL into Python code for better database compatibility
- Develop a call graph interface to show code dependencies for external systems
- Follow-mode to notify users in more detail what happens with their data due to dataflow policies
- Cloud computing extensions for data transfer and deletion
- Web-UI overhaul for multiple scientific experiments
- Web-UI Single-Sign On
- And many many more on the [tracker](https://github.com/rucio/rucio/issues)

## Expected results

### Objective 1 - Setup a Rucio development environment

- We can serve either Docker-based development environments, or completely custom installations on UNIX-based systems.

### Objective 2 - Select and work on core features

- We have a large selection of features planned in the Rucio core, each of which can be tackled individually. We would select together with the student interesting features and guide the design, implementation, documentation, and testing. We follow a fully open Github workflow using code review. It is important for us that the student has a choice in selecting the work. The usual turntime per task is expected to be 2 weeks, which allows us to focus on multiple interesting tasks.

### Objective 3 - Report

- We host weekly collaboration meetings, and we would like that the student presents at the end of GSoC a talk about the experience.

## Requirements

- Python
- Linux development environment (bash, git, ...)

## Mentors

- [Mario Lassnig](mailto:Mario.Lassnig@cern.ch)
- [Martin Barisits](mailto:Martin.Barisits@cern.ch)
- [Cedric Serfon](mailto:Cedric.Serfon@cern.ch)
- [Tomas Javurek](mailto:Tomas.Javurek@cern.ch)
- [Tobias Wegner](mailto:Tobias.Wegner@cern.ch)
- [Thomas Beermann](mailto:Thomas.Beermann@cern.ch)

## Links

- [Rucio Website](https://rucio.cern.ch)
- [Rucio Github](https://github.com/rucio/rucio)
- [Rucio Documentation](https://rucio.readthedocs.io/en/latest/)
- [Rucio Workshop 2018](https://indico.cern.ch/event/676472/)
