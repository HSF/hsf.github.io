---
title: "HSF Packaging Group Meeting #23, May 2, 2018"
layout: meetings
---

# {{page.title}}

Agenda
======
[https://indico.cern.ch/event/719557/](https://indico.cern.ch/event/719557/)

Participants: Graeme Stewart, Pere Mato, Guilherme Amadio, Benedikt Hegner, Chris Burr, Ben Morgan, Liz Sexton-Kennedy, Raphal Pacholek, Emil Obreshkov, Ben Couturier, Geri Ganis, Chris Green, Giulio Eulisse, Patricia Mendez, Marco Clemencic, Lynn Garren, Jim Amundson, Patrick Gartung

[Introduction - Graeme](https://indico.cern.ch/event/719557/contributions/2957742/attachments/1626928/2624333/HSF_Packaging_Group_Intro_2018-05-02.pdf)
===========================
- [Guix presentation tomorrow](https://indico.cern.ch/event/719851/)
  - GNU reimplementation of Nix?
    - Chris thinks it may be a fork from Nix in the past
    - No non-GPL software allowed?
  - Graeme will attend
- [UK RSE](http://rse.ac.uk) - [2018 conference in Birmingham 3-4th September](http://rse.ac.uk/conf2018/)
  - Abstracts submitted: one on HSF generally, and one on Packaging
  - Will hear if accepted by end of May
- Moving onto today’s agenda, as ever, contact Graeme and Ben if you have contributions, updates for future meetings

[Support for multiple micro-architectures - Pere](https://indico.cern.ch/event/719557/contributions/2965980/attachments/1642767/2624258/HSF-Packaging-20180502.pdf)
===============================================
- Need separate stacks for instruction sets (e.g fma, avx etc)
  - How to make available on CVMFS?
  - Select stack at runtime from CPU detection
  - Not all packages need/use these specialist instructions
- Implementing this in LCGMake - recap given on recipes and views
- Naming platforms - packages tagged on `arch-os-compiler-optimization`
  - Extend arch with `arch+iset1+iset2+...+isetN` to describe which instruction sets
    the package was compiled with
- In LCGMake, new argument to package to select full instruction set build
  (via compiler wrapper), which adds platform tag extension
  - Some issues with static libraries: rebuilding dependencies can pull in new instruction sets unwittingly, so this dependency needs to be expressed
    correctly in the dependent build
- Packages not using this are placed under arch-only tag
- Setting up the environment - use views to allow transparent set of instruction set dependent packages combined with those that don’t require specific instruction sets.
- System now in use is minimalistic and only builds a subset of packages
- Is working, and used for GeantV nightlies.
- As we have to define built instruction sets, need to define the default/minimal we can expect
- Still need a tool to discover runtime discovery and selection of "best" match.
- Question: How to manage the dependencies between packages?
  - Change of a low lying library - do you need to build all of the dependencies to be really sure (e.g., inlining)
- Building ROOT is problematic
  - Due to the fact that to generate a ROOT dictionary you have to run some code that has been previously compiled. This creates some problems on
    cross-compiling because the code to generate the dictionary may use instructions that cannot be executed.
- For "bare" packages, does choice of instruction set/optimization level influence interface?
- HSF note was rather blocked by these dependency issues
- What about fat binaries, that support multiple micro-architectures in one library/binary?
  - Larger binaries and cost of runtime switching - though these are not well quantified for our environment
  - Adding support to new micro-architectures later will need to modify long time released software, which is a serious risk in reproducibility.
  - LHCb had reproducibility issues with fat libraries
- C library has vectorised maths from v2.22 - picking from the system could produce similar problems
- Patrick: In Spack, flags are consistent through stack. Possibly some ordering issues (e.g. packages might override, put flags at end, last wins issue)
- One way to try to anticipate problems is to scan the binaries for the instructions they use.

[Spack/SpackDev update](https://indico.cern.ch/event/719557/contributions/2974886/attachments/1642912/2624529/HEP_Packaging_meeting_2018-05-02.pdf) - Chris
=============================
- Current effort to provide "minimum viable product" so narrow first goal with:
  - One OS/compiler/C++/optimization
  - ROOT at top of stack
    - Then build art from there
- Built "our way" to maximize use by supported experiments
  - Use `packages.yaml` to maximize use of system packages
  - Will need/ship one of these per supported platform. Done in existing system (scripts to check installed rpms etc)
  - "Cetmods" CMake glue package
  - Not yet: multiple releases, a collection of every bit of software end users likely need
- Progress:
  - Enhancements submitted to spack for needed packages (Boost, {maria,postgre}sql, xrootd, TBB, ROOT
  - Common issues: Specs often missing dependencies, Python system vs spack. Not enough flexibility in specs for our needs
- Problems:
  - Adding variant to package changes hash, even if default is off. Concretization also has issues here. (so triggers rebuilds)
  - Versions not tied down.
  - Issues with c++ standard, especially in concretization, many packages need to be told explicitly
  - Issues with GPL - default builds of things like readline, gettext, gsl not LGPL compatible
  - Not yet looking at optimization levels, relocatability, buildcache
- Why is the C++ standard an issue?
  - Need to be consistent through graph - some packages need to be told, whilst higher ones may not. Spack may then
    not transmit this need "down" the dependency graph consistently. Example: Build a client of Boost against C++14,
    Spack will not require "Boost+cxx14" without explicitly being told in package.py.

Test Driving Round Table
========================
- Out of time by this point, so deferred to the 16th May


AOB
===
Next Meeting: [16 May 2018](https://indico.cern.ch/event/727088/).
