---
title: Unifying the CVMFS Build Flow for Dependencies
layout: gsoc_proposal
project: CernVM-FS
year: 2026
organization:
  - CERN
difficulty: medium
duration: 175
mentor_avail: June-October
project_mentors:
  - email: valentin.volkl@cern.ch
    first_name: Valentin
    last_name: Volkl
    organization: CERN
  - email: georgios.christodoulis@cern.ch
    first_name: George
    last_name: Christodoulis
    organization: CERN
  - email: shivammadlani5@gmail.com
    first_name: Shivam
    last_name: Madlani
    organization: CERN
    is_preferred_contact: yes

---

# Description

Particle physicists studying nature at the highest energy scales at the Large Hadron Collider rely on simulations and data processing for their experiments.
These workloads run on the "computing grid", a massive globally distributed computing infrastructure.
Deploying software efficiently and reliably to this grid is an important and challenging task.
CVMFS is an optimised shared file system developed specifically for this purpose: it is implemented as a POSIX read-only file system in user space (a FUSE module).
Files and directories are hosted on standard web servers and mounted in the universal namespace `/cvmfs`.
In many cases, it replaces package managers and shared software areas on cluster file systems as means to distribute the software used to process experiment data.

## Task idea

CVMFS currently uses CMake as a build system. However, the installation of external vendored dependencies relies on a custom legacy script. In order to successfully build CVMFS, the vendored dependencies are built first and then linked to CVMFS by CMake.

In this project proposal, we’d like to completely move away from legacy install scripts and leverage CMake entirely for building CVMFS. At the same time, we also want to evaluate potential alternatives of dependencies used to increase performance and reliability either through build system improvements or adapting newer testing methods.

## Expected results and milestones

* Familiarisation with CVMFS and build systems
* Retire legacy build scripts
* Ensure successful CI runs for newer build system
* A new CI workflow that runs against “bleeding edge” version of dependencies
* Investigation of alternate dependencies
* Investigation of test environment improvements
* Updating developer documentation with the new changes

## Requirements

* Familiarity with UNIX/Linux, C/C++ and CMake
* Interest in Linux kernel internals

## How to apply

Once CERN/HSF is accepted as a GSoC org, please write an email with a short introduction to your interests and background to the mentors with the string "gsoc26" in the subject.
There will be a small evaluation task that we will mail to you then.

## Links

* [CVMFS](https://cernvm.cern.ch/fs/)
* [CMAKE](https://cmake.org/cmake/help/latest/)
