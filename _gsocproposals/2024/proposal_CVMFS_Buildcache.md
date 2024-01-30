---
title: CernVM-FS - Buildcache of vendored dependencies
layout: gsoc_proposal
project: CernVM-FS
year: 2024
organization:
  - CERN
difficulty: medium
duration: 175
mentor_avail: June-October
---

# Description

Particle physicists studying nature at highest energy scales at the Large Hadron Collider rely on simulations and data processing for their experiments.
These workloads run on the "computing grid", a massive globally distributed computing infrastructure.
Deploying software efficiently and reliable to this grid is an important and challenging task.
CVMFS is an optimised shared file system developed specifically for this purpose: It is implemented as a POSIX read-only file system in user space (a FUSE module).
Files and directories are hosted on standard web servers and mounted in the universal namespace `/cvmfs`.
In many cases, it replaces package managers and shared software areas on cluster file systems as means to distribute the software used to process experiment data.

## Task ideas


The CVMFS client application is a FUSE file system, mostly written in C++.
It takes advantage of system packages on major linux distributions, but also statically links some selected vendored dependencies.
These dependencies are updated much less frequently than the cvmfs source itself, and caching the build products can therefore speed up any workflow that involves compiling cvmfs from source. The goal of this project is to create such a buildcache for commonly used platforms.
The student should first investigate existing tools (Spack, Easybuild) that implement hashing and caching of build products, and then integrate them into the CVMFS build system.
Additionally, these tools could be used for automated tests over matrices of dependency versions.




## Expected results and milestones

 * Familiarization with the CVMFS build system
 * Evaluation of possible tools to create build caches
 * Design and present a new proposal of building dependencies
 * Implement the chosen solution in the CVMFS build systems.
 * Benchmark build times with caching enabled.


## Requirements

 * UNIX/Linux
 * CMake
 * Bash
 * Experience with Spack or Easybuild is of advantage


## Mentors

 * **[Valentin Volkl](mailto:valentin.volkl@cern.ch)**
 * [Jakob Blomer](mailto:jakob.blomer@cern.ch)


## Links

 * [CVMFS](https://cernvm.cern.ch/fs/)
 * [Spack](https://spack.io)
 * [Easybuild](https://docs.easybuild.io/)
