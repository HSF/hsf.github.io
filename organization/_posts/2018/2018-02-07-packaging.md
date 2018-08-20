---
title: "HSF Packaging Group Meeting #18, February 7, 2018"
layout: meetings
---

# HSF Packaging Group Meeting #18, February 7, 2018

#### *Present*: Graeme Stewart, Liz Sexton-Kennedy, Ben Morgan, Chris Green, Patrick Gartung, Javier Cervantes Villanueva, Guilherme Amadio, Oana Boeriu
#### [Indico Agenda and Presentations](https://indico.cern.ch/event/700265/){:target="_hsf_packaging_18"}

## Introduction (Graeme Stewart)
* Noted [FOSDEM’18 package management session](https://fosdem.org/2018/schedule/track/package_management/), inc. panel discussion.
  * Especially the “Cathedral” aspect of Package Managers vs more usual “Bazaar” in open source.
* Noted recent [CVMFS workshop](https://indico.cern.ch/event/608592/), highlighting talks relevant to packaging ([Compute Canada](https://docs.google.com/presentation/d/e/2PACX-1vR024DUiMr6__w8sY9rOPBsprhFoTqRoSHT-Ng0gyhooHotR5Aia2eSN05CMPAfHFl99ET_F0pZ8EK9/pub?start=false&loop=false&delayms=30000&slide=id.p3), [Notre Dame](https://indico.cern.ch/event/608592/contributions/2830129/attachments/1591914/2520122/ccl-cvmfs-2018.pdf))


## Presentation from Graeme: Updates to Use Case Document
* Document cleaned up, resolved open comments
* Some additional comments from Giulio expanded at end (and from discussion)
* Meaning of “Common set of requirements” in the document
  * Best common solution, common language for understanding, sharing for tangible benefits
  * When requirements overlap, opt for most stringent, use modularity
  * Don’t be driven by edge cases
* Run through of [document](https://docs.google.com/document/d/1h-r3XPIXXxmr5tThIh6gu6VcXXRhBXtUuOv14ju3oTI)
  * On using underlying system: difficult to maintain if we have binary packages cross platform due to varying
    versions/ABIs (Guilherme). Graeme: do want to support use of underlying system, we’ve noted the risk involved.
  * Sharing of artifacts, can we rely on CVMFS? (Liz). Graeme: to an extent, but have to be careful about publish time for de-duplication.
  * Guilherme: On development side, maybe use Containers as these are easier to modify than CVMFS.
  * Javier: Do tools cover everything? Need scripts on top of things like Spack to cover the deployment and development. Graeme: Probably need these, but separate from the
    (packaging) tool to keep things modular

## Presentation from Chris: Towards a full Spack / Spackdev –based build ecosystem for art-based experiments
* Goals: build/development ecosystem, for at least the experiments using the Art framework
* Replacing current system of UPS package relying on LD_LIBRARY_PATH etc (so better macOS support), cetbuildtools
* External packages building using Spack recipes, SpackDev for building development packages
* Progress:
  * 25 milestones to demonstrate that new system can replace old one
  * Addition on “buildcache” functionality to Spack
  * Trouble points id’ed, inc build dimensions (compiler, MPI, debug/profile etc), avoid un-neccessary duplication of
    non-compiler specific packages (e.g. binary only, data only, C/Python only). Constraints from need to support older OS/packages
* Currently: De-UPSing cetbuildtools, refining/reviewing/assigning priorities to requirements, implementing milestones.

## Presentation from Javier: FCC stack building with Spack
* Stack uses LCG Releases from CVMFS as an underlying system
  * Use Spack’s configuration to describe use of these packages
* FCC packages may override LCG versions, not ideal
  * Github repos for package definitions, FCC, hep-spack, spack builtins
* Workflow split:
  * Build node, creates binary tarballs (buildcache)
  * Deploy buildcaches to CVMFS Stratum0 node(s) - need to use hash to install.
  * Also create a spack view, additionally setting up LCG Release required.
* Some issues with consistency of hashes between buildcache install and view creation.
  * Discussion with Patrick: down to how Spack calculates hashes, expected to be fixed in upcoming merge (also see FOSDEM talk)
* Speeding up builds
  * Try to reduce redundant work repeated everyday
  * How to reuse binaries already installed in CVMFS?
    Several options under investigation, but so far issue with all of these related to hash calculation,
    download of binaries, write/synchronization to/with CVMFS
  * Patrick: would be good to raise an issue on Spack GitHub, FNAL would also like this sort of functionality/have this issue
* Limitations: conflict between CVMFS packages with concept of Python extensions.
  * Spack commands may try to create links on a read-only system
  * Need to create a view to prepare a suitable environment
  * Various infrastructure scripts needed: Python scripts, plus various spack YAML config files.
* Conclusions
  * Spack fully covers FCC’s basic requirements, albeit with additional scripting needed for overall workflow.
  * Do need further optimizations of build process to maintain large sets of packages.
* Questions on usage/future:
  * Higher layer to configure Spack (eg.g how to build all package in debug)?
  * How best to Manage/Maintain Spack config for build/install of full stack?
  * How to deploy software using Spack (CVMFS/build and install on same node?)?
* Liz/Graeme: Good set of questions, maybe discuss in more detail at next meeting
* Patrick: Also good to discuss/ask about these topics Spack’s Slack channel, someone from UChicago
  has been discussing using Spack w/CVMFS.

## AOB
* [Next meeting](https://indico.cern.ch/event/704402/) 21st February 2018
* Let Graeme/Ben know on any topics/talks. Possible talk from Giulio Eulisse on AliBuild experiences
