---
title: Improve user-facing documentation of the Cern-VM FileSystem
layout: gsdocs_proposal
project: cvmfs
year: 2023
organization:
---

## Description of project idea

CVMFS (current version 2.10.1, first release in 2008) is a BSD3-licensed POSIX
read-only file system in user space (a FUSE module) that is highly specialised
in distributing software. CernVM-FS is actively used by small and large High
Energy Physics (HEP) collaborations, and, to a smaller extent, in Nuclear
Physics, Astrophysics and in some High Performance Computing Centers. In many
cases, it replaces package managers and shared software areas on cluster file
systems as means to distribute the software used to process experiment data.
CVMFS has a client-server architecture, with different audiences of users for
both parts: The setup of the server is usually done by a few select specialists
who need comprehensive detailed technical information. The client has a much
wider audience of users that may just need to install the software and do a
quick setup to access the /cvmfs filesystem. While all information is present in
the user-facing documentation cvmfs.readthedocs.io, the current structure does
little to guide users and misses some “tutorial”-like sections for commonly used
tasks.

## Detailed project description

- [Please see our full proposal draft here](GoogleSeasonOfDocsHSF.pdf)

## Mentors

- Valentin Volkl [valentin.volkl@cern.ch](mailto:valentin.volkl@cern.ch) CERN
- Jakob Blomer [jakob.blomer@cern.ch](mailto:jakob.blomer@cern.ch) CERN
