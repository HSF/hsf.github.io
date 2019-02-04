---
title: "HSF Packaging Group Meeting #31, January 30, 2019"
layout: meetings
---

# {{page.title}}

Agenda
=======
[*https://indico.cern.ch/event/790021/*](https://indico.cern.ch/event/790021/)

Participants: Graeme Stewart, Chris Burr, Guilherme Amadio, Ben Morgan, Marco Clemencic, Patrick Gartung, Chris Green, Geri Ganis, Pere Mato, Henry S, Ben Couturier.

[Introduction](https://indico.cern.ch/event/790021/contributions/3301107/attachments/1787837/2911508/HSF_Packaging_Group_Intro_2019-01-30.pdf)
============
- Group plans for 2019
  - Primary: provide meaningful, testable, solutions based on the HEP use cases identified last year
  - Updates from each project every few months
  - Longer term: CHEP2019 paper? Updating technical note (now ~3yrs old)
- Ongoing projects:
  - LCG-like stack with Spack (Graeme and Javier)
    - ATLAS/FCC as first clients
    - Now building Gaudi dependencies
    - Tidying hep-spack package repo, some to upstream spack, use as community repo as holding place
    - HSF spack-config repo for sharing
  - SuperNEMO
    - Migrating from Homebrew to Spack to better support from-source builds and to benefit from
      work of this group
    - Want to also support end user installs as currently no CVMFS, though Docker/Singularity images published
  - Others:
    - FNAL Spack/SpackDev
      - Chris: Getting back to it, need more feedback on MVP
      - Working on LArSoft stack, which is more complex in terms of dependencies
      - Looking at adding spack-dev as a spack extension to ease use
      - Patrick: working with buildcaches, found a bug that’s been reported and fix submitted. Caused by compiler path outside spack.
    - LHCb: Nix/Conda, presentations today
    - Portage: tutorial from Guilherme at last meeting
    - EasyBuild maybe also worth looking at?
      - Chris Burr: Compute Canada using Nix as base system, plus EB on top.
- Now in phase of working rather than discussing, so propose move to a baseline of 1 meeting per month
  - Can have additional meetings if people want/have topics to discuss. Just let Graeme and Ben know.
- [HOW2019 Workshop](https://indico.cern.ch/event/759388/)
  - Software Tools session where packaging will give an update


[Conda (Chris Burr)](https://indico.cern.ch/event/790021/contributions/3301108/attachments/1787718/2911364/2019-01-30_HSF-Packaging-Conda.pdf)
==================
- PM that is language agnostic, Multi-Platform/Architecture
- Installs binaries (no install from source support)
- Very popular in academic/data science
- Very simple to install, no root/sudo, any location supported
  - Graeme: is the shell function for packages? No, just to assist in setting up “environments”
- Conda environment:
  - Just a folder, switch between via “activate/deactivate” commands
  - Create with “conda create”
  - Then install packages in environment with “conda install”
- Packages come from "channels":
  - Anaconda Distribution (OSS/Commercial, mostly Python/R)
    - Can include proprietary software like Intel/CUDA
    - GUI for managing environments
  - Anaconda.org: Can set up yourself, but limited storage (3-5GB)
  - Any HTTP(S) can be used as a channel, provided correct structure is present
- Community Channel: [Conda Forge](https://conda-forge.org)
  - GitHub org plus various CI providers for builds
  - One Git repo per package
  - Lots of automation
- Specialized "forges": Bioconda, AstroConda (AstroPy seem to be setting one up)
  - Can specify priorities for channels to over/underride packages
- Package "recipe" is a folder containing a file `meta.yaml` (uses Jinja2 templates)
  - Defined with cross-compilation in mind (build/host/run dependencies)
  - Builds done with a shell script `build.sh/bat`
  - Build/Install environment, tested by installed to later environment
  - Lots of checks to ensure relocatability
- Used to rely on system compilers (effectively CentOS5, rely on ABI versioning)
  - Now more maintainable, with Anaconda 5, conda-forge migration (gcc 7)
- Now uses "Core Dependency Trees" (CDTs)
  - Repackages CentOS6 package into a sysroot of conda’s pseudo-cross compilers
  - Chosen because of lack of resources, possible better performance from host libraries
- All conda packages must be relocatable
  - RPATH tricks
  - Build/Install into very long (255 char) path
  - Sed/replace on install on both text/binaries (latter appends null bytes)
- Conda in HEP?
  - Huge number already using for analysis (and some experiments, Xenon1T, NEXT)
  - Lack of ROOT inconvenient (was a Netherlands e-Science one, but no longer maintained), but already have cling in conda-forge
  - However, now have ROOT 6.16 with gcc7 and Python 2.7/3.6/3.7
    - Though need to use CC/CXX env vars to access compiler
- Currently conda-forge doesn’t support unreleased versions, and struggle with CI resources
  - Builds of conda package in ROOT Nightlies to be added
- Conclusions
  - Conda very young, but lots of progress recently, especially on compilers and binary compatibility
  - Does support build variants, version pinning, exporting/importing environments
- Pere: How are versions controlled?
  - Can specify version when building, as long as binary compatibility is specified
  - Don’t have to rebuild everything if versions are pinned
- Patrick: How is ABI compatibility managed?
  - Relies on package maintainer and upstream looking after this and being honest about it
- Graeme: Is Conda now capable of managing multiple environments?
  - Yes, just activate/deactivate as needed
  - Patrick: very similar to Spack’s environments (Spack may even been inspired by Conda)
- Ben C: How are binaries similar to Python wheels?
  - Similar, just rely on a few expected system packages (derived from CentOS5, but patches on top to allow, e.g. C++11)
  - Chris: nothing limits how “deep” Conda can go, so could build down to libc if needed
- Graeme: How are dependencies specified?
  - In the `meta.yaml` file under `requirements` section
  - Can also track features in this way like `debug` `opt`, `avx` for example
  - Graeme: are variants combinable? Yes


Nix (Chris Burr)
================
- Deferred to next meeting


AOB
===
- Next meeting: [27th February](https://indico.cern.ch/event/796240/)
