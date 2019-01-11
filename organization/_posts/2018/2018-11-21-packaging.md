---
title: "HSF Packaging Group Meeting #30, November 21, 2018"
layout: meetings
---

# {{page.title}}

Agenda
=======
[*https://indico.cern.ch/event/772263/*](https://indico.cern.ch/event/772263/)

Participants: Ben Morgan, Chris Green, Guilherme Amadio, Graeme Stewart, Liz Sexton-Kennedy

Introduction
============
- Podcast from Spack at SC18:
  - [https://www.exascaleproject.org/spack-the-deployment-tool-for-ecps-software-stack/](https://www.exascaleproject.org/spack-the-deployment-tool-for-ecps-software-stack/)
- Chris: No update from FNAL attendees at SC18
- Graeme: More commits on Spack Chain PR, so good progress here


Portage - Update and Live Demo
==============================
- Recap on disto models on HEP:
  - Full OS, or VMs, or Containers
  - Gentoo Prefix?
- Can use Gentoo Prefix via CVMFS, available prefixes for:
  - Native Linux (distro independent as Gentoo ships own glibc), macOS
  - Docker container using host CVMFS
  - Includes very lightweight images like Busybox (1MB), then use tooling from prefix
- Documentation links: getting started on bare metal, Gentoo Linux image, just Gentoo Prefix on other Linuces, macOS etc.
  - "Test drive" on HSF repo on get started with Prefix
- Further guides on the basics of using Portage
  - Installing, configuration etc., plus associated tooling to help with packaging processes
- Basic installation of packages via `emerge` program, e.g. `emerge <args> package`
  - Various options to check what will be done, what is available
  - Prints flags about what will be recompiled, upgraded, newly installed
  - Arguments to search for packages, fetch distfiles, rebuild from scratch etc.
  - "Working with Portage" document shown, which has full usage and troubleshooting info
  - "Masked" packages: ones that will be ignored depending on conditions such as arch etc.
- Developer doc with links
  - Covers details of how Portages `ebuild` process works
  - Basic sequence of "phases" as per spack and other package managers: prepare, configure, build, test, install etc
  - Each phase implemented as a Python function, new ebuilds can mostly inherit defaults, but can override if package needs it
  - To create a ebuild:
    - Create a directory to hold the `.ebuild` files
    - Each version of the package has its own `.ebuild`, and each of these can have ebuild revisions (e.g. `hello-1.0-r2.ebuild`
      for the 2nd revision of the ebuild of version 1.0 of hello)
    - `.ebuild` files hold some keywords/metadata for things like where to get sources, dependencies, options,
      then functions for the phases as required
    - Link to Quickstart on Creating ebuilds
  - Can add ebuilds into Custom Repository (link to Gentoo docs given)
- Have looked at automating ebuilds with Jenkins, then publish to CVMFS prefixes
  - Very simple and fast
- Walkthrough of using `emerge` and how to query the system
  - Can have multiple GCC/Python versions installed alongside each other
  - Can share Python packages across Python versions if the packages are portable between Python versions
  - Can select default GCC/Python via "alternatives" like system, but can also emerge packages with specific GCC using CC/CXX variables
  - Uses "slots" to mark multiple versions and API/ABI compatibility
  - Example of root needing openssl, but root won’t rebuild if openssl upgrades and is ABI compatible ("slot" has not changed).
  - Up to package developer to determine when a new slot is needed by checking upstream release notes, but some tools provided by Portage to assist here
- Graeme: Interesting aspect looks to be ability to provide self-contained "mini-distro" of non-HEP software like compilers. Then could use spack on top of that.


AOB
===
- Next meeting: 5th December
