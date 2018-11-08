---
title: "HSF Packaging Group Meeting #29, November 7, 2018"
layout: meetings
---

# {{page.title}}

Agenda
=======
[*https://indico.cern.ch/event/766022/*](https://indico.cern.ch/event/766022/)

Participants: Graeme Stewart, Pere Mato, Patrick Gartung, Ben Morgan, James Amundson, Emil Obreshkov, Guilherme Amadio, Martin Ritter, Chris Green, Oana Boeriu

Introduction
============
- Next HSF workshop is going to be 18-22 March 2019 at JLab
  - Will be held jointly with WLCG and OSG
  - More information to follow, but save the date


SFT Spack Update
=================
- SFT group looking at other approaches to stack building, Spack continues as most promising tool/approach.
- New features coming (upstream) that help
  - Chains
  - Fuzzy concretization
- Synergy with HEP/Science communities
- Goal of LCG/Spack
  - Fairly complete current LCG release, built with Spack
- Use this as “base” for
  - Production runtime
  - Developer buildenv
- Initially targeting CentOS7 + GCC 8.2
- Package sets:
  - Gaudi+Externals (broad, but not huge, number)
  -FCC Software (already using Spack, so this exercises Spack Chains, lower chain being Gaudi)
  - ATLAS externals (using ATLAS’s CMake recipes)
- Bootstrap:
  - Graeme has CentOS7 Docker image
  - Add recent Spack develop branch, plus patches for Chain, ROOT recipe, from current upstream PRs
- Using Docker on a macOS laptop, mounting Spack from main laptop filesystem
  - Different mount points for build/install
- Spack-Config setup under HSF github
- Not without issues, but mostly related to Docker/macOS
  - Problem of building ncurses/termcap on APFS filesystem
  - Needed to use disk image that is explicitly case sensitive in this case.
  - Something to be aware of in future
- After that, went well
  - GCC 8 bootstrap from system compiler fine
  - Minor issues with tar/fifos, possible due to docker/permissions
  - Still need RELAX, but with that will complete Gaudi externals layer
- Apart from issues noted, very happy with ease of use and package availability.
- Jim: have preliminary work to query system for availability of system packages. Would it be better to set up a user other than root in the Docker image? Graeme: yes, just did the easiest thing to get things working.
  - Jim will send Graeme the system query work.
- Patrick: Spack have some Dockerfiles for various platforms. Some issues with binary caches though (absolute links in bzip2 for example)
- Pere: Would like to get the prototype to the point that experiments wouldn’t have to care whether packages were built from LCGCMake or Spack.
  - Patrick: Only major difference in binary tarballs would be rpaths in binaries. Using rpaths from binaries would require following spack’s install layout.
  - Graeme: Views would help here


LCGCMake Update
===============
- Quick recap: based on CMake ExternalProject, uses single to define package lists and versions.
- Delivery process is split to:
  - Build nodes running LCGCmake, pushes binaries to EOS
  - Install on CVMFS release nodes
  - Publication CVMFS
- Views are used to provide single rooted view (bin/ lib/ include/ so on) of coherent set of packages/views
  - Activated by single setup script
- Non-CVMFS releases?
  - For local installs, networkless, don’t have matching os/compiler
- Now have direct `lcgcmake` command that can provide local installs on demand
  - Supports reuse of binaries when possible, build-from-source otherwise, or mix.
  - Simple to use, just clone lcgcmake repo and run command.
  - Provides subcommands for tasks and queries (e.g. install, show)
  - Can install packages in one go, or one-by-one
  - Various options to install different versions etc
- Example use for GeantV Externals
  - Relatively large set: ROOT, Geant4, VecGeom, devtools (and all their deps)
  - Can use `lcgcmake install GeantV-externals`
  - Development can then proceed natively
- Lcgcmake currently tested on most common platforms (Ubuntu,SL,CentOS,macOS) but some prerequisites needed.
  - Longer term, and in general for all packaging, have to think about what those prerequisites are.
- Use and feedback is welcome!
- Ben: is GeantV-externals a "metapackage"? Pere: effectively yes, uses a CMake custom target as the implementation.
- Patrick: If there are rpms, can there be post-install scripts? Pere: yes, can have postinstall either in rpms or via extra steps for the CMake ExternalProject.


AOB
===
- Anyone going to SC2018?
  - No one from SFT/FNAL at least directly involved in Packaging work (Marc Paterno from FNAL is going). Possibly some
    participants from CERN OpenLab.
  - Noted that we have good ongoing contacts with Spack community
- Patrick: Packaging meeting at HSF meeting at JLAB? Graeme: Yes, could do so, even a hackathon?
- Next meeting: Provisionally 21st November [*https://indico.cern.ch/event/772263/*](https://indico.cern.ch/event/772263/)
. Guilherme: Can give update on Portage/Docker.

