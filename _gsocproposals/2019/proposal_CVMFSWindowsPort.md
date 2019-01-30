---
title: Porting the CernVM File System Client to Windows
layout: gsoc_proposal
project: CernVM-FS
year: 2019
organization: CERN
---

## Description

The physics experiments at the Large Hadron Collider (LHC) rely on millions of lines of scientific C++ code written by thousands of developers. In order to efficiently distribute the scientific codes to a world-wide distributed network of data centers and physicist's laptops, the CernVM File System (CernVM-FS) provides a global shared software area that delivers application binaries on demand [1]. The CernVM-FS client is based on Fuse and can be mounted on Linux and macOS nodes. Scientists with a Windows laptop, however, have to resort to workarounds such as virtual machines.

Recent versions of Windows 10 ship with a new system facility called "Projected File System" (ProjFS) [2] that has been factored out from previous work on the Git virtual file system [3]. ProjFS simplifies the development of virtual user-level file systems on Windows much like Fuse does on UNIX platforms. This project aims at a proof-of-concept port of the CernVM-FS client to Windows using the ProjFS framework.

## Task ideas

A proof-of-concept port of the CernVM-FS client to Windows based on the ProjFS framework. The Windows client should be able to mount a CernVM-FS repository, browse the directory tree, read ("hydrate") files on open, and directly run binaries from the virtual file system. As the current code base is intimately tied to POSIX systems, this port should follow a clean-slate approach. The final code should demonstrate the feasibility of the approach with a limited set of features. For instance, CernVM-FS extended attributes and "chunked files" can be neglected for the time being, as well as performance considerations beyond the design of the local data cache.

## Expected results

A usable ProjFS file system that can mount and read from a CernVM-FS repository on a recent Windows 10 computer.

## Requirements
- C/C++
- Understanding of file systems, HTTP, sqlite
- A Windows 10 computer

## Mentors
- [Jakob Blomer](mailto:jblomer@cern.ch)
- [Gerardo Ganis](mailto:gerardo.ganis@cern.ch)

## Links
  1. [CVMFS](https://github.com/cvmfs/cvmfs)
  2. [Microsof Projected File System](thttps://docs.microsoft.com/en-us/windows/desktop/projfs/projected-file-system)
  3. [Git virtual file system](http://cern.ch/go/Qb8m)
