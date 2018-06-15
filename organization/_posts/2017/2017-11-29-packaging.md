---
title: "HSF Packaging Group Meeting #15, November 29, 2017"
layout: default
---

# HSF Packaging Group Meeting #15, November 29, 2017

#### *Present*: Graeme Stewart, Lukas Heinrich, Oana Boeriu, Rafal Pacholek, Jakob Blomer, Geri Ganis, Javier Cervantes Villanueva, Guilherme Amadio, Giulio Eulisse, Ben Morgan, Radu Popescu, Ben Couturier, Attila Krasznahorkay, Emil Obreshkov, Chris Green, Patrick Gartung, Pere Mato

#### [Indico Agenda and Presentations](https://indico.cern.ch/event/681894/){:target="_hsf_packaging_15"}

## Introduction
* Next meeting scheduled for [13th December 2017](https://indico.cern.ch/event/684972/)
  * Will focus on CVMFS/Containers/Deployment, with presentation from CVMFS developers.
* Graeme and Ben will draft an abstract on Packaging Use Cases/Tool Assessment for [CHEP 2018](http://chep2018.org)
  * Will present at next meeting for comments/feedback
  * Not a paper on any specific tool - expect that people will submit their own abstracts on those.
* Noted second draft of HSF White Paper open.
  * Encourage people in this WG to read and comment, especially Software Development.
  * Also for people to sign - don’t have to have contributed to the content to sign.
* Update on Use Cases Document
  * Good feedback and comments since last time, thanks to contributors!
  * Common agreement on "must have" requirements: specify build options for dependencies,
    reuse of binary artifacts, setup of runtime "views".
  * Clarification on: global build options, recipe hierarchy, install relocation (with example
    implementations), development environment.
  * Many comments are useful in their own right, so need to capture this information
    somewhere other than a Google Docs comment thread.
  * Clarifications with Giulio Eulisse on his comments
    * On sources, felt important to have a self-managed backup of third-party sources.
      Guarantees future availability, plus allowing patching. Comment from ATLAS
      that they also install package sources as part of their package/distribution
      pipeline.
    * On reducing command line options, this is to keep major things like switching
      compiler part of the recipe.
    * On recipes, importance is to ensure that older packages can be rebuilt in the future.
      E.g. in Alibuild, Alibuild as it is now can build Alibuild recipes from N years ago.
  * Clear that we need to identify "actors" in the Use Cases, e.g. librarian, end user.

## Presentation from Oana: ATLAS Releases: Build, Packaging and Deployment - short overview
* ATLAS offline code is split into many, many units of code called “packages” (usually implementing some particular classes and building a small number of libraries). The full offline Athena release has about 2000 packages.
* New way of building Athena is quite simple. LCG release is a base, then build AtlasExternals, then Gaudi, then the rest of Athena.
* Build of Athena bootstraps using AtlasSetup  (sets up gcc, cmake version etc). A few helper scripts used for building whole of Athena, or subsets - output is rpm, from CPack.
* Nightly rpms are release candidates - copied to EOS. Distribution to CVMFS via Python script. Each nightly build put into date-time tagged directories, under this are the Athena, AthenaExternals, Gaudi. LCG, Externals, tdaq are common over a range of Nightlies
* Also allow private builds to be distributed over CVMFS
* Future: looking at ways to save AtlasExternals binary artifacts. Reuse? Looking at Nexus, git LSF. Breaking up large rpms. Include build of LCG

### Discussion
* Microsoft has released [source code](https://github.com/Microsoft/GVFS) for their Git virtual filesystem (GVFS). There is a [project with GitHub to port this to Mac and then Linux](https://arstechnica.com/gadgets/2017/11/microsoft-and-github-team-up-to-take-git-virtual-file-system-to-macos-linux/). Will be a talk on this at CVMFS Workshop in January. Background: Windows source code is very large, so using a Virtual File System to only checkout files when touched.
* In ATLAS, nightlies always built from scratch both for security and to work around some issues with incremental builds seen in continuous integration. But now in a position to seriously consider incremental nightlies as well.
* Discussion on installing directly on CVMFS: Is an issue with relocatability, need to have consistent mount points, and of course a writable CVMFS repository. Currently binaries local to build machine, packaged, then uploaded to EOS.
* Nexus: can store binary artifacts, then can check existence of required binary when/if needed later. Tool to be investigated.

## Presentation from Lukas: Containers in ATLAS
* Containers and Package Managers solve related, but largely orthogonal problems
* PMs main unit of distribution is a software package with declared dependencies,
  each operation is a filesystem change. Packages interface with each other via
  low level ABIs.
* Containers main unit of distribution is an filesystem, image of which is sequence
  of package manager and other operations. Containers interface with each other via
  abstract file/REST/data server/message queues.
* Good fit in HEP: global distribution of a complex stack that uses significant OS component to a wide range of systems that we don’t manage like the Grid, HPC user laptops.
* User developed analysis software has different requirements - often a mix between stages inside release, own code that might require specific directory structure.
  Physics reproducibility is important.
* Two approaches in ATLAS for images:
  * "Fat": Completely self-contained, local on disk, no network or local cvmfs install needed. But large (10GB+).
  * "Thin": Only provide OS, domain software from host install of CVMFS - needs network, and no immediate knowledge of what bits in CVMFS are used.
* Build both as part of nightlies for offline and analysis releases, distributed via Docker Hub.
* Work on CVMFS Graph Driver - “Fat” Image, can be used directly, but also deployed over CVMFS. Docker can then just pull the bits it needs.
* In use for local development, especially on non-supported platforms.
* In use for CI - easy integration on common platforms
* Also for grid deployment - using Singularity as container runtime. HPC may lack networked filesystems like CVMFS, but can support containers
* Using for Analysis Preservation - CERN Analysis Preservation Portal. Kubernetes cluster.
* Training: Easy entry point for new collaboration members.

### Discussion
* Size of "Fat" images depends on domain: User Analysis (small, ~2GB total) and Reconstruction (large ~20GB).
* How to track provenance of an image? In Images, have each layer was created, but not deterministic. Then the package manager layer, e.g. graph based deterministic.
* Some development to run docker images without root privileges, e.g. uDocker.

## AOB
* [Next meeting](https://indico.cern.ch/event/684972/) in 2 weeks, 13th December.
* Apologies to Guilherme on overrun - guide to using demo Portage Docker/CVMFS
  installs will be distributed, presentation at next meeting.

