---
title: CernVM-FS - Benchmarking of new FUSE features
layout: gsoc_proposal
project: CernVM-FS
year: 2024
organization:
  - CERN
difficulty: high
duration: 175
mentor_avail: June-October
---

# Description

Particle physicists studying nature at highest energy scales at the Large Hadron Collider rely on simulations and data processing for their experiments. These workloads run on the "computing grid", a massive globally distributed computing infrastructure. Deploying software efficiently and reliable to this grid is an important an challenging task. CVMFS is an optimised shared file system developed specifically for this purpose: It is implemented as a POSIX read-only file system in user space (a FUSE module). Files and directories are hosted on standard web servers and mounted in the universal namespace /cvmfs. In many cases, it replaces package managers and shared software areas on cluster file systems as means to distribute the software used to process experiment data.

## Task ideas

As a FUSE file system, CVMFS critically depends on the performance and capabilities of libfuse. Since CVMFS was first created, several new features were added to libfuse - in particular FUSE_CAP_SPLICE_MOVE could potentially improve performance of CVMFS. In this project, the student should investigate the use of splice+move instead of copy and other new features of libfuse as well as set up and run a complete benchmark of relevant workloads.


## Expected results and milestones

 * Familiarization with the use of libfuse in CVMFS
 * Design and implementation of a relevant benchmark
 * Adapt and build CVMFS using FUSE_CAP_SPLICE_MOVE
 * Investigate other new features of libfuse
 * Present results of findings 


## Requirements

 * UNIX/Linux
 * C/C++
 * Experience with libfuse or developing other file systems is of advantage


## Mentors

 * **[Valentin Volkl](mailto:valentin.volkl@cern.ch)**
 * [Jakob Blomer](mailto:jakob.blomer@cern.ch)


## Links

 * [CVMFS](https://cernvm.cern.ch/fs/)
 * [libfuse](https://github.com/libfuse/libfuse/blob/master/include/fuse_lowlevel.h)
