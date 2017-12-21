---
title: "HSF Packaging Group Meeting #16, December 13, 2017"
layout: default
---

# HSF Packaging Group Meeting #16, December 13, 2017

#### *Present*: Graeme Stewart, Ben Morgan, Jakob Blomer, Guilherme Amadio, Patrick Gartung, Javier Cervantes Villanueva, Rafal Pacholek, Chris Green, Pere Mato, Geri Ganis, Xavi (vidyo), Oana Boeriu
#### [Indico Agenda and Presentations](https://indico.cern.ch/event/684972/){:target="_hsf_packaging_16"}

## Introduction
* Updates on [Use Cases document](https://docs.google.com/document/d/1h-r3XPIXXxmr5tThIh6gu6VcXXRhBXtUuOv14ju3oTI/edit), still open for comments and feedback
* [Draft of CHEP abstract](https://docs.google.com/document/d/1f2NLMOIzvG6Tsvq821eJjWKNtJRb_McpVArUVpOHSbs/edit) presented, feedback by Wednesday 20th December

## Presentation from Guilherme: Gentoo Prefix on CVMFS to Manage HEP Software
* Overview of Portage, including links to docs
* Distribution models in HEP
  * Base Image via binaries, images (automated with Catalyst)
  * Gentoo Prefix environments - non-root installs, can support macOS
* Portage for LCG
  * No setup (inc `LD_LIBRARY_PATH`)
  * Only dependendency is kernel, single install for all Linux, multiple compilers
  * Maybe support macOS
  * Could be deployed through CVMFS
* Usage examples demonstrated
  * From CVMFS (from sft.cern.ch repo)
  * From a busybox container (using host CVMFS)
  * Gentoo HSF test stack docker container
* Comments from Patrick on staged installation:
  * Guilherme: Portage uses `DESTDIR` to stage installs, but can’t move installation from one prefix to another.
  * For different installation locations need to rebuild (or post-facto hack the `RPATH` setup)
* Starting the prefix environment boots the built shell, which has a `PATH` to the prefix area; binaries in the prefix area use the prefix dynamic loader, so this is what picks up the requisite prefix libraries (Linux). In this case, uses its own libc. Use of `RUNPATH` also supported on Linux or macOS.
* Starting container basically the same effect as starting the prefix environment
* Support for other setups (Java, Go, Python) can be done, standard way to interact with /etc files.

## Presentation from Jakob: CVMFS Evolution and Docker Support
* Problem of large images (i.e. multi-GB) both for distribution and management
* Would like to split tasks up:
  * Container for isolation and basic tooling
  * CVMFS for distributing image contents, using caching and only parts of image needed
    at runtime to reduce effective size
* CVMFS Graph Driver
  * Singularity and CVMFS work together "out the box"
  * Docker is more complex due to client/host interactions
* Get "thin layer" with CVMFS graph driver plugin
  * Docker graph driver plugins allow use of different storage driver
* Install of plugin demonstrated through use of `docker plugin` plus small edits to docker “daemon.json” configuration file (cvmfs graph driver is still experimental). Very small (~20MB).
* Run using `cvmfs/thin_image` container. Despite name, total image size is 7.9GB, but pull is very fast.
* Easy to convert existing image to “thin” form, though some tooling still needed to streamline this.
* Benchmarking on Cloud (CERN/Commercial): 90 VMs, 1GB images, drops startup time from 5min to 5s.
* Question from Graeme on comparison to light docker container mounting CVMFS.
  * Jakob: integrates better with Docker infrastructure
* Current status is close to production, still work on publication (docker2cvmfs, docker push). Also looking at `containerd` support
* HSF container service on AWS? Useful service, but cost needs thought.


## AOB
* [Next meeting](https://indico.cern.ch/event/688097/) provisionally 17th January 2018.

