---
title: CernVM-FS - Improve integration test isolation
layout: gsoc_proposal
project: CernVM-FS
year: 2023
organization:
  - CERN
difficulty: medium
duration: 350
mentor_avail: June-October
---

# Description

Particle physicists studying nature at highest energy scales at the Large Hadron Collider rely on simulations and data processing for their experiments. These workloads run on the "computing grid", a massive globally distributed computing infrastructure. Deploying software efficiently and reliable to this grid is an important an challenging task. CVMFS is an optimised shared file system developed specifically for this purpose: It is implemented as a POSIX read-only file system in user space (a FUSE module). Files and directories are hosted on standard web servers and mounted in the universal namespace /cvmfs. In many cases, it replaces package managers and shared software areas on cluster file systems as means to distribute the software used to process experiment data.

CVMFS has a large integration test suite, but the tests often need to make extensive changes to the systems or setup test services. One failed tests that does not clean up correctly can fail the whole test suite, making test results harder to interpret and the tests less effective overall.

## Task ideas

 This project aims at improving the isolation of individual integration tests of CVMFS. Virtualization technologies like containers or lightweight VMs (Firecracker) should be evaluated for performance and suitability for running CVMFS tests. Individual tests can be investigated and improved. Finally, the solution should be implemented in the CVMFS Jenkins continuous integration infrastructure. 



## Expected results and milestones

 * Familiarization with the CVMFS test infrastructure and failure modes
 * Evaluation of possible virtualization technologies
 * Design and present a new proposal of isolating integration tests
 * Implement the chosen solution in the Jenkins-based continuous integration infrastructure.


## Requirements

 * UNIX/Linux
 * Containers
 * Bash
 * Jenkins Experience is of advantage


## Mentors

 * **[Valentin Volkl](mailto:valentin.volkl@cern.ch)**
 * [Jakob Blomer](mailto:jakob.blomer@cern.ch)


## Links

 * [CVMFS](https://cernvm.cern.ch/fs/)

