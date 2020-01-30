---
title: Podman CVMFS integration
layout: default
project: CernVM-FS
year: 2020
organization:
 - CERN
---

## Description

[CernVM-FS (CVMFS)][cvmfs] is a globally-distributed filesystem used to lazily distribute software in different server farm.

[Podman][podman] is an utility to run and use containers.
It provides the same command line interface than Docker but it runs without the need of a privileged daemon.
These two characteristics make it extremely interesting for workload used in scientific data-centers.

It has been shown that only a small portion of all the files in a container images is necessary to run the image itself.
This is even more accentuated in scientific container images since they usually include big binaries, not always used by the specific task.
Our goal is to merge the lazy load capabilities of CVMFS with the container workflow allowed by podman, to quickly load big scientific container images while maintaining the isolation and convenience of containers.

There is already an integration for Docker, and another for __containerd__ (kubernetes) is about ready.

The filesystem in CVMFS has the following structure:

```

/cvmfs/unpacked.cern.ch/
│ 
├─ .layers
│  ├── 00
│  │   ├── 001dba6e0b44ff57a26d944d9a307ef39927e4882b45eb9d3c9257d754ef7d56
│  │   │   └── layerfs
│  │   │       ├── etc
│  │   │       ├── home
│  │   │       └── opt
│  │   └── 008deed8f79c35003fb8808e37c39245e244cd6af7498e5b7874ac7e186c7307
│  │       └── layerfs
│  │           └── code
│  └─ ... many more ...
└─ .flat
   ├── 02
   │   ├── 0212054c85a9b966aa4f9c08048686603c7d0583067b759d14633070fcea30a1
   │   │   ├── bin
   │   │   ├── dev
   │   │   ├── etc
   │   │   ├── home
   │   │   ├── lib
   │   │   └── var
   │   └── 027998886ae41faa55490baeb6b5e37f4295375ac5dcae5bcf3fe91f141687c2
   │       ├── bin
   │       ├── boot
   │       ├── dev
   │       ├── etc
   │       ├── home
   │       ├── lib
   │       ├── lib64
   │       ├── lost+found
   │       ├── media
   │       ├── pool
   │       ├── root
   │       ├── sbin
   │       ├── tmp
   │       ├── usr
   │       └── var
   └─ ... many more ...
```

Where the `.layer` directory store the content of the layers unpacked in an ordinary directory and the `.flat` directory stores the content of a whole container images, with each layer unpacked one of top of each other.


The project will be mentored from both CERN and RedHat.

## Task Ideas

1. Write software to automatically create filesystem structure in CVMFS that can be used by podman
2. Allow podman to understand the filesystem structure already present in CVMFS to load container images

## Expected Result

Allow podman to run container images directly from CVMFS exploiting its lazy loading capabilities.

## Evaluation Task

Interested students can contact me ([Simone Mosciatti][simo]) directly for an evaluation task, it requires basic understanding of containers and FUSE filesystem.

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
