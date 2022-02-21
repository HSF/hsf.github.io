---
title: CernVM-FS integration test framework powered by Firecracker VM
layout: gsoc_proposal
project: CernVM-FS
year: 2022
organization: CERN
difficulty: medium
duration: 350
mentor_avail: June-August
---

## Description

[The CernVM File System (CVMFS)](https://cernvm.cern.ch/fs) provides a scalable,
reliable and low-maintenance software distribution service. It was developed to
assist High Energy Physics (HEP) collaborations to deploy software on the
worldwide-distributed computing infrastructure used to run data processing
applications.

The architecture of the system comprises a number of different components
(servers, file-system clients, command-line writer tools, etc.) which are
designed to run on separate machines. A rigorous integration testing protocol is
essential for maintaining the quality of such a complex distributed system.

The goal of this project is to overhaul the integration testing framework used
in CVMFS, making use of novel technologies such as the [Firecracker
micro-VM](https://firecracker-microvm.github.io/) to improve efficiency (fewer
resources used per test case), precision (run each test case in complete
isolation) and usability (run integration tests easily on a development
machine).

## Task outline
* Develop a tool to produce a VM image in QCOW2 format for a specific Linux
  distribution, containing an installation of the desired CernVM-FS version or
  tag (ex: Ubuntu 20.04 + CernVM-FS 2.9.1).
* Use the produced VM image with Firecracker VM on a Linux host and run a single
  integration test case, powering down the VM after the test case was run;
  changes to the VM image occurring during the test should not be persisted.
* Develop the needed scaffolding to run individual test cases, collect their
  results and present a summary of a complete test run. Each test case should be
  run in a VM with a clean initial state.
* Deploy the new integration test system in the CernVM-FS CI infrastructure at
  CERN.

## Expected results

A usable system for running CernVM-FS integration tests with isolation between
test cases, powered by Firecracker VM, and running on CERN Openstack
infrastructure.

## Requirements
Linux, shell scripting, basic networking, VMs, containers

## Mentors
  * **[Radu Popescu](mailto:radu.popescu@cern.ch)** (CERN)
  * [Jakob Blomer](mailto:jakob.blomer@cern.ch) (CERN)

## Links
  * [CernVM-FS](https://cernvm.cern.ch/fs)
  * [Firecracker VM](https://firecracker-microvm.github.io/)
