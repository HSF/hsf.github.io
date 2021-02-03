---
title: New protocols for exascale data management with Rucio
layout: gsoc_proposal
project: Rucio
year: 2021
organization:
    - CERN
    - UWuppertal
---

## Description

[Rucio](https://rucio.cern.ch) is an open-source software framework that provides functionality to scientific collaborations to organize, manage, monitor, and access their distributed data and dataflows across heterogeneous infrastructures. Rucio was originally developed to meet the requirements of the high-energy physics experiment ATLAS, and is continuously enhanced to support diverse scientific communities. Since 2016 Rucio orchestrated multiple Exabytes of data access and data transfers globally.

With this project we seek to enhance Rucio clients to make them easier to use in heterogeneous environments, especially with the availability of different transfer tools. Within High-Energy Physics (HEP) we are well-covered with the [GFAL](https://linux.die.net/man/3/gfal) libraries, however there are diverse communities outside HEP which are relying on more widely-deployed tools, each with their own quirks and peculiarities. It is therefore important to add support for them in Rucio, most importantly [scp](https://en.wikipedia.org/wiki/Secure_copy_protocol), [rsync](https://en.wikipedia.org/wiki/Rsync), and [rclone](https://en.wikipedia.org/wiki/Rclone). Rucio should then be made more customisable such that the optimal transfer tool is automatically used for a given environment.

## Tasks

The tasks are as follows:
 * Refactor the mapping of Rucio Storage Elements and associated protocols
 * Implement protocol support for scp
 * Implement protocol support for rsync
 * Implement protocol support for rclone
 * Design a smart transfer protocol algorithm based on system and user configuration
 * Document the new protocols

## Requirements

 * Mandatory
   * Python 3
   * Linux, Git, and Docker
 * Basic understanding
   * Transfer protocols (FTP, HTTP, WebDAV, SCP, ...)
   * HTTP REST APIs
   * X.509-based authentication
   * Token-based authentication

## Expected results

By the end of GSoC'21 we expect to have a fully working Rucio client that can smartly use the available transfers tools, based on local and remote system configurations, and runs under a variety of different Linux distributions. As a stretch goal, performance optimisation for high throughput Exascale data management is of course very appreciated.

## Mentors
 * [Martin Barisits](mailto:martin.barisits@cern.ch)
 * [Thomas Beermann](mailto:thomas.beermann@cern.ch)
 * **[Mario Lassnig](mailto:mario.lassnig@cern.ch)**

## Links
 1. [Rucio GitHub](https://github.com/rucio/rucio)
 2. [Rucio Documentation](https://rucio.readthedocs.io/en/latest/)
 2. [Rucio system overview journal article (Springer)](https://doi.org/10.1007/s41781-019-0026-3)
 3. [Rucio operational experience article (IEEE Computer Society)](http://sites.computer.org/debull/A20mar/p9.pdf)
