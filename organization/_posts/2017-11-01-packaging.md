---
title: "HSF Packaging Group Meeting #13, November 1, 2017"
layout: default
---

# HSF Packaging Group Meeting #13, November 1, 2017

#### *Present*: Graeme Stewart, Patrick Gartung, Benedikt Hegner, Javier Cervantes Villaneuva, Raphal Pacholek, Guilherme Amadio, Ben Morgan, Ben Couturier, Liz Sexton-Kennedy, Lynn Garren, Jim Amundson

#### [Indico Agenda and Presentations](https://indico.cern.ch/event/674780/){:target="_hsf_packaging_13"}

## Introduction

* Ben Morgan joins Graeme as second co-convener of the group.
* Proposal for setting up a small test-stack for the packaging solutions being investigated:
  * Ben was happy to volunteer the SuperNEMO stack - it's quite small;
  * FCC was able to compile their whole stack with Spack (Gaudi + FCCSW), certainly good to get Gaudi;
  * Lynn: G4, ROOT and CLHEP would be ideal;
  * Python is also needed.
* **ACTION: Will create a doc to collect the concrete definition of the test stack**

## Spack

* Tried a few more use-cases using more libraries from the system directly. Discovered a bug in binary packaging for such cases, there are fixes on the way.
* At FNAL using dual-step bootstrap as to avoid recompilation of cmake, etc. for every compiler.
* Singularity and Spack are working together, building a stack within the singularity shell
  * Allows distribution of minimal containers
* Q by Ben M about Singularity: better from security perspective and good experience in Warwick. Are sys admins happy with that solution?
  * A by Liz: singularity is recommended by the WLCG working group. It is the solution on NSF supercomputers, DOE still to be convinced.

## Containers in SuperNEMO

* Introduction to SuperNEMO use case
* Package management with homebrew. Most packages maintained externally.
  * No bottles used yet
* Binary distribution on top of homebrew needed. 
  * Using docker containers already for TravisCI, etc. based on CentOS and Ubuntu.
  * Container building done manually and uploaded to DockerHub. CentOS 6/7 and Ubuntu 14LTS/16LTS. 
  * Usage of containers complicated by size of images. Every CI round fetches image into cache again.
* For deployment homebrew works for most users; providing a Ubuntu16LTS container of latest snapshot as well.
* Containers not used in production as no docker’ed resources available

* Discussion:
  * Best practices for layering are still not clear.
  * Noted packaging + docker don’t exclude each other; we agree that binary packaging is required for any solution.
    * For LHCb it is clear that uninstall is important as well (so need a fully featured solution for managing deployment lifecycle).
  * CVMFS:
    * Graphdriver plugin for docker is interesting as you can download only the pieces of the container that are needed at runtime (see [this presentation](https://indico.cern.ch/event/673223/contributions/2754513/attachments/1540835/2416224/slides.pdf) in the SFT group).
    * For installing onto CVMFS with Spack you need to run Spack. Difficulties if the install location is not the same as the run location (although CVMFS Stratum0 can be setup that way).
    * Small experiments sometimes do not have enough support for the server side of CVMFS.
    * Long term vision may be providing a common stack in a supported CVMFS setup.
  * Singularity is a solution for security problems in docker deployment (also mentioned above).
  * Guilherme pointed to [rkt](https://coreos.com/rkt/) as another container solution.


## AOB
* [Next meeting](https://indico.cern.ch/event/678307/) in 2 weeks, 15 November.
