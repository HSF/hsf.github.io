---
title: Podman CVMFS integration
layout: gsdocs_proposal
project: CVMFS
year: 2019
organization:
 - CERN
---

## Description

[CernVM-FS (CVMFS)][cvmfs] is a globally-distributed filesystem used to lazily distribute software in different server farm.

[Podman][podman] is an utility to run and use containers.
It provides the same command line interface than Docker and it run without the need of a privileged daemon.
These two characteristics make it extremely interesting for workload in scientific data-centers.

It has been shown that only a small portion of all the files in a container images is necessary to run the image itself, this is even more accentuated in scientific images since they usually include big binaries, not always necessary.
Our goal is to merge the lazy load capabilities of CVMFS with the container workflow allowed by podman, to quickly load big scientific images while maintaining the isolation and convenience of containers.

There is already an integration for Docker, and another for containerd (kubernetes) is about ready.

The project will be mentored from both CERN and RedHat.

## Task Ideas

1. Automatically create filesystem structure in CVMFS that can be used by podman
2. Allow podman to understand the filesystem structured already present in CVMFS to load images

## Expected Result

Allow podman to load images directly from CVMFS.

## Evaluation Task

Interested students can contact me ([Simone Mosciatti][simo]) directly for an evaluation task, it will involves basic understanding of containers and FUSE filesystem.

## Requirements

The code-base will mostly be in Go(lang), hence it is necessary to know the language. It is also important to have a basic understanding of Linux.

## Mentors

 * [Simone Mosciatti (CERN)][simo]
 * [Giuseppe Scrivano (RedHat)](mailto:giuseppe@scrivano.org)
 * [Jakob Blomer (CERN)](mailto:jblomer@cern.ch@cern.ch)

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
[simo]: mailto:simone.mosciatti@cern.ch
