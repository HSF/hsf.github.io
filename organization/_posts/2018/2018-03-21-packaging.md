---
title: "HSF Packaging Group Meeting #21, March 21, 2018"
layout: meetings
---

# {{page.title}}

Agenda
======
[https://indico.cern.ch/event/712739/](https://indico.cern.ch/event/712739/)

Participants: Ben Morgan, Graeme Stewart, Guilherme Amadio, Javier Cervantes Villanueva, Martin Ritter, Oana Boeriu, Patricia Mendez, Patrick Gartung, Pere Mato, Shahzad Malik Muzaffar, Chris Green, Emil Obreshkov, Gerardo Ganis, Benda Xu, Radu Popescu, Giulio Eulisse, Ben Couturier, Marco Clemencic, Chris Burr

Introduction - Graeme & Ben
===========================
- CHEP paper accepted as a presentation: showcase work and attract more interest. Nice target to work towards testing.
- HSF Workshop next week - this WG will contribute to the Software Development stream
- [Use Cases Document](https://docs.google.com/document/d/1h-r3XPIXXxmr5tThIh6gu6VcXXRhBXtUuOv14ju3oTI/)
  - Some clarification on install time relocation
  - Version 1.0, but further additions to make 1.1 etc anticipated
- Sprint Workshop for SPI project (CERN/SFT team that produces LCG Stack, and work with GENSER team for generators)
  - Goal is consensus and common perspective for SPI over next 2-3 years
  - Synergy with this group, so input welcome, Graeme/Ben will contribute/attend
- HSF rebranding: “hep-sf” -> “hsf”
  - For this WG, Github organization is now at [https://github.com/HSF](https://github.com/HSF)
  - There are redirects, but check your remotes
  - Mailing list is now: hsf-packaging-wg@googlegroups.com
- Today: Intro/test stack(Ben), Nix package manager (Chris), as always proposals for future contributions welcome, contact Graeme and Ben.


Test Stack - Ben
================
- [Document](https://docs.google.com/document/d/1LW8OsTFFA9QwsJ9fASkRoJ2E6Gk3UGnOQIcElCL8UCM/edit) updated: Idea is to have a standard way that people can contribute builds of the test stack with the different package managers that can be easily tested by the wider group.
- Linux containers are a good idea to have a controlled environment and to make sure dependencies on the system are well expressed.
- Will make things more sophisticated later, but have a good test setup to begin with.
- There is a template that shows how to describe the installation and build environment for people.
- Use of the GitHib packaging repo can be a central place to work and share information:
  [https://github.com/HSF/packaging](https://github.com/HSF/packaging)
- Can one use the Gentoo image? Maybe not the best as it’s little used in HEP.
- Suggestion to target CentOS7 as the “standard candle”.
  - Next Ubuntu LTS will be out soon (18.04).
- This is only a bootstrap step - then we need to look at the use cases and see how well they are satisfied.
- Martin: Centos7 seems the easiest, SLC6 is hard because it’s very old, Ubuntu (latest) is hard because it’s very new.
  - Again, CentOS7 is a good place to start, but then diversify.


Nix package manager in LHCb - Chris
===================================
- Starting point: analysis preservation
  - Post-DaVinci environment tricky
  - Can’t run Docker everywhere
- [Nix](https://nixos.org/nix/manual/): "purely functional package manager"
  - Source based, but binary caches as well
- Package recipes:
  - Nix "expressions"
  - Few lines long in custom functional language
- Builds aim to be portable/reproducible/deterministic
- Everything stored in /nix by default
  - Each package lives in a directory named by hash of "how built"
- Collection of nix expressions = “channel”
  - Core/common is on [github NixOS/nixpkgs](https://github.com/NixOS/nixpkgs)
- Nixpkgs also provides helper functions for environment/symlinks for build/runtime
- Example expression show for Gaudi
  - Functional language => recipe is a function whose inputs are things like dependencies, sources, patches, etc
- Work so far
  - Nix in Docker without cvmfs mounted, but changing nix store to /cvmfs/lhcb.../nix (mock /cvmfs, not actually distributing over CVMFS yet)
  - Change in store root => official binary cache can’t be used, so need to rebuild (Chris: You can change store root if new path is same length!)
    - Graeme: so hash contains path prefix? Yes..
    - Binary cache is then install location dependent
      - Marco - so then a binary cache is a specific install location cache
      - /cvmfs/nix (or something like that) would be needed to share
    - Patrick: Supercomputers use "uncvmfs"; user space filesystems also help (e.g., parrot)
    - Total recompile does mean that it’s very clean, albeit with CPU cost for rebuilding
    - You don’t need to worry about platform variants (SLC6, CentOS7, etc.) as single build is self contained.
  - Package builds using Nix “Hydra” tool on openstack. Uses local machine for build, but easy to add additonal worker(s)
    - Also supports for workers with different archs (darwin, or CPU variants etc)
  - Overlays: Take main NixPkgs repo, then apply your changes on top of this. Can extend or override.
    - Graeme: So can take things from base, but then change a few options? Yes.
  - Environment Overlays
    - "buildEnv" used to create environments. Symlinked to the store directory, similar to an LCG view.
    - Also allows integrating with package overlays, and special treatment for languages that have their own conventions like Python/Haskell.
- Examples given for installing Nix in Docker images, noted current limitations
  - Binary downloads are slow
  - Package signatures aren’t checked yet
  - Some packages have issues when built inside Docker images (test suites that require privileges)
- Why use nix?
  - Built software should run on “any” Linux flavour (own libc, "build almost everything" approach)
  - Simpler environments
  - Many packages already upstream in NixPkgs
  - Adding new packages is straight forward (many things like shbang patching, RUNPATH etc automagically handled)
  - Active community
- What isn’t so good
  - Documentation lacking, but is improving and many examples help
  - Nix language has a steep learning curve, but not so bad if just writing expressions
  - Some issues with independence from host system
    - Graphics, kernel (but no worse that others)
  - Sometimes reproducible builds aren’t reproducible (mostly due to remote file URLs being changed)
- Giulio
  - Not easy to use “system” or “private” pieces, e.g., a local compiler
  - Rebuild time is very long, if something changes
    - Incremental build use case
  - How to do my day to day development work?
    - Especially changing some mid-level component, e.g. ROOT but checking impact on AliPhysics (without rebuilding everything?)
      - AliBuild takes care of this
    - Chris - Hydra will allow you to download a bootstrap script that gives a local build environment, that could be tweaked locally
- Marco
  - User development should be in nix-shell
  - At the moment we are trapped on a single well controlled environment (e.g., lxplus) as we can’t really support non-native systems
  - Single tool to build and give a development environment is a big plus
- Pere
  - To build Gaudi, source an lcgview, then cmake && make - there is nothing easier
  - We are schizophrenic - we want perfect reproducibility, but also want to be able to patch things (e.g., new xrootd client)
  - How do we solve that problem?
  - Ben: lifecycle of different pieces is very different, physics makes numbers, middleware is a different matter (and breaks, can need changed)
  - This has pushed use from the system, instead of building everything
  - In nix can rebuild xrootd, but with new version?
- Marco - don’t like to have openssl, etc. in our stack as we are not in charge of updating them
  - How to install xrootd without recompiling everything?
  - Divide package sets in two and don’t introduce unnecessary dependencies (careful package management)
    - Setup a runtime that separates ROOT with ROOT xrootd plugin
    - Only rebuild pieces needed, recreate views
    - Does this actually work?
In favour of building everything, once, instead of having to support patching on many platforms.
- Guilherme - change openssl, it rebuilds, but only for packages with a direct dependency, otherwise not
- Can nix use system packages? On Mac, can use system libraries for Cocoa etc. No on Linux. Giulio: Might be possible to do this on Linux, but not the default.
- Boundary between package management and development - treat this with care…
- Graeme: We’re likely missing a few use cases, or rather, stories, that would be useful to enumerate. For example, if we have a reproducible rebuild, perhaps we shouldn’t be so afraid of rebuilding.


AOB
===
Next Meeting: [4th April 2018](https://indico.cern.ch/event/716297/).
