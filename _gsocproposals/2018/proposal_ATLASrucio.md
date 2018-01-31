---
title: Rucio - Exascale data management
layout: gsoc_proposal
project: ATLAS
year: 2018
organization:
 - CERN
---

## Description

Rucio is a data management system for modern large-scale scientific experiments. It allows experiments to deal with vast amounts of data in a scalable, modular, and flexible way. Our primary instance for the ATLAS experiment orchestrated an Exabyte of data transfer and processing in 2017. We seek a student to help us out with designing, developing, testing, and putting in production several highly sought after features in the Rucio core to be prepared for the future. Concepts like horizontal scalability, distributed algorithms, large scale databases, performance optimisation, or network communication protocols are your forte? Then you are the GSoC student we seek! Come and join an open development team, contribute to our free and open-source Github repository, and help change the scientific world.

## Task ideas

- Automatic recovery of suspicious files on storage
- Automatic request queue shuffling based on storage type
- Diagnosis and rerouting of impossible transfer rules
- Protect storage access from too many concurrent requests
- Transform database-specific PL/SQL into Python code for better database compatibility
- And many many more on the [tracker](https://github.com/rucio/rucio/issues)

## Expected results

### Objective 1 - Setup a Rucio development environment

- We can serve either Docker-based development environments, or completely custom installations on UNIX-based systems.
- Estimated time: 1 week

### Objective 2 - Select and work on core features

- We have a large selection of features planned in the Rucio core, each of which can be tackled individually. We would select together with the student interesting features and guide the design, implementation, documentation, and testing. We follow a fully open Github workflow using code review. It is important for us that the student has a choice in selecting the work.
- Estimated time: The usual turn per feature is expected to be 2 weeks.

### Objective 3 - Report

- We host weekly collaboration meetings, and we would like that the student presents at the end of GSoC a 10 minute talk about the experience.

## Requirements

- Python
- Linux development environment (bash, git, ...)

## Mentors

- [Mario Lassnig](mailto:Mario.Lassnig@cern.ch)
- [Martin Barisits](mailto:Martin.Barisits@cern.ch)

## Links

- [Rucio Website](https://rucio.cern.ch){:data-proofer-ignore=""}
- [Rucio Github](https://github.com/rucio/rucio)
