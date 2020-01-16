---
title: Podman CVMFS integration
layout: gsdocs_proposal
project: CVMFS
year: 2019
organization:
 - CERN
---

## Description

[CernVM-FS (CVMFS)][cvmfs] is a globally-distributed filesystem used to distribute software in different server farm. 

[Podman][podman] is an utility to run and use containers.
It provides the same command line interface than Docker and it run rootless. 
These two caratheristics make it extremelly interesting for workload in scientific datacenters.

In order to allow scientist to take advantage of existing container solutions (docker, Kubernetes), the CernVM team at CERN is developing integration between containers runtimes and CernVM-FS.

There is already an integration for Docker, and another for containerd (kubernetes) is about to be merged.

This project aims to provide the same level of integration also for podman.

The project will be mentored from both CERN and RedHat.

## Tasks

TO_BE_DEFINE

## Mentors

 * [Simone Mosciatti](mailto:simone.mosciatti@cern.ch)
 * [Giuseppe Scrivano](mailto:giuseppe@scrivano.org)
 * [Jakob Blomer](mailto:jblomer@cern.ch@cern.ch)

## Links

 * [CernVM-FS][cvmfs]
 * [CVMFS Github][cvmfs-repo]
 * [podman][podman]
 * [podman Github][podman-repo]
 * [podman storage][podman-storage]

[cvmfs]: http://cernvm.cern.ch/portal/filesystem
[cvmfs-repo]: https://github.com/cvmfs/cvmfs
[podman]: https://podman.io/
[podman-repo]: https://podman.io/
[podman-storage]: https://github.com/containers/storage
