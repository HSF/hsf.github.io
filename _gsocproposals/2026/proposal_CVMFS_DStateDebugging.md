---
title: Debugging CVMFS processes in D-state
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
    is_preferred_contact: yes
---

# Description

Particle physicists studying nature at highest energy scales at the Large Hadron Collider rely on simulations and data processing for their experiments.
These workloads run on the "computing grid", a massive globally distributed computing infrastructure.
Deploying software efficiently and reliable to this grid is an important and challenging task.
CVMFS is an optimised shared file system developed specifically for this purpose: it is implemented as a POSIX read-only file system in user space (a FUSE module).
Files and directories are hosted on standard web servers and mounted in the universal namespace `/cvmfs`.
In many cases, it replaces package managers and shared software areas on cluster file systems as means to distribute the software used to process experiment data.

## Task idea

CVMFS is implemented as a FUSE filesystem, which are surprisingly easy to deadlock. While it's a rare occurence in production, if a kernel deadlock occurs, debugging the cause is very difficult. This is because debuggers like gdb rely on sending a PTRACE signal to the process.

In this project proposal, we'd like to investigate ways of obtaining a stacktrace and other possibilities of getting diagnostic information from a stuck process. Even if the process is stuck in a kernel call it *should* still be possible to trigger a coredump and load it with a debugger to get a stacktrace, but we are not aware of any easy way to do this. The resulting utility would be generally useful for FUSE filesystems, but we would want to integrate it into CVMFS.


## Expected results and milestones

 * Familiarization with the CVMFS and FUSE file-system
 * Creation of a toy file system that can get stuck
 * Investigation of ways to get a stacktrace from the stuck filesystem
 * Integration of the solution in a convenient way in CVMFS
 * Writing a debugging "cheat sheet" for the CVMFS documentation 


## Requirements

 * Familiarity with UNIX/Linux, C/C++
 * Interest in Linux Kernel internals


## Links

 * [CVMFS](https://cernvm.cern.ch/fs/)
 * [Reliably creating d-state processes - Blog post by Chris Down](https://chrisdown.name/2024/02/05/reliably-creating-d-state-processes-on-demand.html)
