---
title: Rucio - 'Sync & Share' interface for exabyte-scale multi-location data management
layout: gsoc_proposal
project: ATLAS
year: 2018
organization:
 - UOslo
 - CERN
---

## Description

Rucio is a multi-location data management system for large-scale scientific experiments. It allows experiments to deal with vast amounts of data in a scalable, modular, and flexible way, and provides a flat namespace to its data. The goal of this project is to build up a Sync & Share interface to Rucio by using open source tools and frameworks.


## Task ideas

- The first part of the work would be to evaluate a list of popular open source Sync & Share projects like OwnCloud, Seafile, or Pydio, and evaluate the corresponding libraries and dependencies.
- The second part will be to interface Rucio with the chosen project for the most common use cases like uploading or downloading data.

## Expected results

### Objective 1 - Setup a Rucio development environment and familiarise with the Rucio code

- We can serve either Docker-based development environments, or completely custom installations on UNIX-based systems.
- Estimated time: 1 week

### Objective 2 - Survey on open source Sync & Share projects

### Objective 3 - Interface Rucio with the selected project

### Objective 4 - Implement basic data management workflows

- As a first step, synchronous upload and download of files.
- At later stages, asynchronous upload and download of collections of files, so called datasets.

### Objective 5 - Report

- We host weekly collaboration meetings, and we would like that the student presents at the end of GSoC a 10 minute talk about the experience.

## Requirements

- Python
- Linux development environment (bash, git, ...)

## Mentors

- [Vincent Garonne](mailto:vgaronne@gmail.com)
- [Thomas Beermann](mailto:Thomas.Beermann@cern.ch)

## Links

- [Rucio Website](https://rucio.cern.ch){:data-proofer-ignore=""}
- [Rucio Github](https://github.com/rucio/rucio)
