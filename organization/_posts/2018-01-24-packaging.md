---
title: "HSF Packaging Group Meeting #17, January 24, 2018"
layout: default
---

# HSF Packaging Group Meeting #17, January 24, 2018

#### *Present*: Graeme Stewart, Ben Morgan, Patrick Gartung, Chris Green, Oana Boeriu, Guilherme Amadio, Javier Cervantes Villanueva, Pere Mato, Marco Clemencic, Ben Couturier, Liz Sexton-Kennedy, Brett Viren.
#### [Indico Agenda and Presentations](https://indico.cern.ch/event/688097/){:target="_hsf_packaging_17"}

## Introduction (Graeme Stewart)
* Forward look at tasks for 2018
  * Complete [Use Cases Document](https://docs.google.com/document/d/1h-r3XPIXXxmr5tThIh6gu6VcXXRhBXtUuOv14ju3oTI/edit).
    No aim of complete convergence between experiments, will note where there are differences in different areas of the community.
  * Establish working version of [proposed test stack](https://docs.google.com/document/d/1LW8OsTFFA9QwsJ9fASkRoJ2E6Gk3UGnOQIcElCL8UCM/edit), compare against use cases (~March time)
  * Update [Packaging Technical Note](http://hepsoftwarefoundation.org/notes/HSF-TN-2016-03.pdf) based on work since then (Use Cases, Portage, Test Stack)
  * Release “(Test) Stack in Box” for CVMFS/Container deployment, could be used as a foundation for small experiments (Spring-Late Summer time)
* 2018 Events
  * [WLCG/HSF Workshop 26-29 March (Naples)](https://indico.cern.ch/event/658060/). Noted that early bird registration closes on Feb 16th.
    Wide agenda, inc. Software Development session, where packaging fits in.
  * [CHEP 2018, 9-13 July (Sofia)](http://chep2018.org). High level Packaging Abstract submitted. An abstract on Spack/SpackDev from FNAL has also been submitted.
* News from HSF
  * [Community White Paper](https://arxiv.org/abs/1712.06982) published (still open for signing)
  * Note Software Development Chapter and [dedicated paper from Software Development WG on ArXiv](https://arxiv.org/abs/1712.07959)
* Comments/Questions
  * Ben has a usecase for Portage (tensorflow on CentOS 6) - will communicate with Guilherme and Graeme about this offline.

## Presentation from Patrick: Spack in HEP Update
* All CMSSW libs/exes built on SL7 with Spack
  * Externals added as spack packages + scram xml for runtime paths (run/link)
  * Many deps missing
  * Scram sets up runtime
* FWLite with Spack on MacOS
  * Relocation (via install_name_tool) took long time
  * PR to Spack to simplify run of tool
* MacOS Build Distribution
  * Distribute without rpath changes
  * Allow non-admins to install a bundle via a disk image
  * Use “sparse disk image” using hdiutil: a R/W image that grows/can be compacted as needed
  * Very simple to setup!
* Disk Image for FWlite/Fireworks
  * Homebrew for clang/gfortran/cmake
  * Spack to build FWlite etc
  * Script/symlinks to `bin/` path in disk images
* Also: one with just Homebrew, one with gentoo prefix
  * Some issues with these to resolve
* Comments from Guilherme on Portage bootstrap
  * Uses system compiler to bootstrap a compiler for the prefix - you can use a Mac build of gcc4.9 to get started (will then build gcc more easily)
  * Bug reports are very welcome
* Spack binary caches do work, with Partick’s patches
* Spack have released 0.11 and plan a monthly release cycle from now on

## Presentation from Ben: ABIs and Packaging
* Binary compatibility could save a lot of build time and space (more re-use)
  * Raise topic to promote discussion and knowledge sharing
* C++ ABI compatibility is a complex subject
  * How package is written
  * What compiler/standard is used
* Topic of interest with broad discussion
  * Marco: Compatibility between gcc6.X and gcc7.X should be assured (for all X)
  * Marco: ROOT header compilation is very g++ dialect sensitive (11/14/17)
  * Pere: STL classes do layout memory differently (in general) between dialects, so this is really a danger (hence the warnings)
  * Marco: BOOST libraries also very dialect sensitive
  * Consensus that C++ dialect should be consistent
  * Chris: last few clang versions have had ‘fixes’ to name mangling, so were not fully backward compatible
  * Marco: Clang and gcc mixing in LHCb did throw up some problems (e.g., std::map use caused segfaults)
  * Marco: Needed new version of binutils to use avx2 instructions, but then linker incompatibilities were thrown up affecting static libraries built with the older linker
  * Marco: Wanted to use some system libraries, like openssl, that get, e.g., security fixes; plugins would help if dependencies could be isolated
  * Pere: be more explicit with dependencies

## Presentation from Chris: Towards a full Spack / Spackdev –based build ecosystem for art-based experiments
*

## AOB
* [Next meeting](https://indico.cern.ch/event/700265/) 7th February 2018
* Apologies to Chris Green for overrun, rescheduled to 7th Feb.
* Other agenda item is building the FCC stack with Spack.
* Will continue discussion on Use Cases and Test Stack.

