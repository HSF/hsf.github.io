---
title: Evaluate Distribution of ML model files on CVMFS
layout: gsoc_proposal
project: CernVM-FS
year: 2025
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
CVMFS is an optimised shared file system developed specifically for this purpose: it is implemented as a POSIX read-only file system in user space (a FUSE module).
Files and directories are hosted on standard web servers and mounted in the universal namespace `/cvmfs`.
In many cases, it replaces package managers and shared software areas on cluster file systems as means to distribute the software used to process experiment data.

## Task idea

CVMFS is optimized for the distribution of software (header files, scripts and libraries), taking advantage of the repeated access pattern for its caching, and the possibility to deduplicate files present in several versions. 
CVMFS is capable to provide a general read-only POSIX file system view on data in external storage. A very common use case is to make conditions databases available to workloads running in distributed computing infrastructure, but various datasets have been published in CVMFS.
How efficient CVMFS can be always depends on the details in these use cases - often the benefit for the users is simply in leveraging the existing server and proxy infrastructure.


In this project proposal, we'd like to evaluate CVMFS as a means to distribute machine learning model files used in inference, for example .onnx files. The main focus will be on creating a test deployment and benchmarking the access, as well as possible coding utilities and scripts to aid in the deployment of models on CVMFS. We'd also like to contrast  CVMFS to existing inference servers like KServe, and see if it could integrate as a backend storage.




## Expected results and milestones

 * Familiarization with the CVMFS server infrastructure 
 * Familiarization with the ML model usage at CERN, Survey of different common inference model file formats.
 * 
 * Test deployment of models relevant to ML4EP 
 * Benchmark and evaluation of inference using models served from CVMFS
 * Addition of the benchmark to the CVMFS continuous benchmarking infrastructure
 * Writing a best practices document for the CVMFS documentation 


## Requirements

 * UNIX/Linux
 * Interest in scientific computing devops
 * Familiarity with common ML libraries, in particular ONNX


## Mentors

 * **[Valentin Volkl](mailto:valentin.volkl@cern.ch)**
 * [Lorenzo Moneta](mailto:lorenzo.moneta@cern.ch)


## Links

 * [CVMFS](https://cernvm.cern.ch/fs/)
 * [KServe](https://kserve.github.io/website)
