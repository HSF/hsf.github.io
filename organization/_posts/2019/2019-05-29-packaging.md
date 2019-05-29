---
title: "HSF Packaging Meeting #34, 29 May, 2019"
layout: meetings
---

# {{page.title}}

## Agenda
[<span class="underline">https://indico.cern.ch/event/819329/</span>](https://indico.cern.ch/event/819329/)

Participants: Ben Morgan, Patrick Gartung, Graeme Stewart, Javier Cervantes, Chris Burr,
Pere Mato, Dimitri, Geri Ganis, Guilherme Amadio, Marco Clemencic, Chris Green, Elizabeth Sexton-Kennedy

## Introduction (Graeme)
- Ongoing Projects: FCC/LCG
  - LCG stack with Spack (+ CERN summer student from June/July)
    - Javier: some issues with ROOT, but everything below o.k.
  - CHEP abstract submitted (+ wider WG topics), additional collaboration welcome
- Any other CHEP abstracts submitted?
  - Chris Burr: one on Conda/ROOT + CVMFS
  - Guilherme: Maybe one from Gentoo/Portage
  - Patrick/Chris: One on SpackDev
- Next meeting options: 19th/26th June/3 July
  - 19th maybe too soon?
  - 26th awkward due to many people travelling
  - 3rd July looking best

## Spack/SpackDev (Chris Green)
- Improvements to Spack core
  - "VISUAL" env var for recipe editing
  - Better saving of environment plus PATH-like var manipulation
  - Better CMake builds
- Core recipe improvements
  - Inc: mysql, mariadb, postgresql, intel-tbb, cppunit, gl2ps, range-v3, nix, boost, sqlite, numpy
  - Reconciled FNAL root recipe with upstream
  - Resolved "-isystem" issue with ROOT/Spack
- Other news
  - Work Items doc updated to version 0.4
  - Bi-weekly production meetings with Peter Scheibel (Spack principal), inc. discussion on items in above doc, with WIP/AIP on requirements
  -  AIP to merge SpackDev into core, telcon with Elizabeth Fischer (Spack contributor) who’s working on similar topic
- SpackDev progress
  - Accuracy/Speed improvements for consistent package checkout
  - Package names can have hyphens
  - Accommodate changes to upstream Spack
  - Print "spec tree" for packages specified for development
  - Input DAG (everything need for a release) can have several top-level packages with co-concretization
  - Package checkout improvements, e.g. require that development packages come from VCS systems.
  - Global build can handle tests in parallel
- MVP1a
  - Integration testing round that identified previously mentioned updates
  - LArSoft now building with Art 3.02.04 (but will go to 3.02.05 for MVP)
  - Remaining issue with "wirecell" package, need to support Git submodules
    - Spack supports submodules, but wirecell needs a additional manual step.
    - Guilherme: Could create tarballs? Chris: Would imply FNAL becomes maintainer of those tarballs. Fix locally in Spack to get MVP progressing
- Chris: some issues still require updates to the core concretization system, aim is end of US fiscal year, but may slip.

## Distributing CMS FWLite with Conda (Patrick)
- Conda recap:
  - Latest uses gcc 7.3/clang 4.0.1 (with SDK from OSX 10.9)
  - Everything linked under one prefix
- FWLite with scram in Conda?
  - Conda prefix + ROOT installed
  - Linux: Trivial
  - OSX: issues with Scram going into infinite (with/without SIP)
- Went to CMake using scram2cmake tool
  - See https://github.com/gartung/fwlite
  - Some tweaking needed for CMake FindXXX
  - Some tweaking need for fwlite sources
- Conda-forge: “feedstocks”: repos for each package + builds for platforms
  - Updates for conda-forge and additions needed for fwlite dependencies
- Guide for installing miniconda + up to fwlite
- Summary:
  - Can install FWlite with Conda!
  - Generated conda environment not intended to be a development environment (e.g. conda compiler wrappers not included in install prefix)
  - But should work for analysis
- Questions:
  - Pere: What are the caveats on ROOT macros? Patrick/Chris B: Issues with the macOS SDK on 10.14
  - Graeme: Why the old SDK? Chris B: for compatibility with older systems
  - Ben: Why the old Clang? Chris B: Seems to work well enough at the moment.
  - Graeme: Is there an issue with not having a development environment? Patrick: Seems to be o.k. for Python tools, and when building an application on top of the environment.
  - Ben: Can it work to develop single packages (i.e. env contains the compilers etc). Chris B: Yes, a bit flaky on macOS, but getting better.


## AOB
- With summer holiday/meetings dates starting to encroach on dates for next WG meeting,
  will see how updates progress.
  - Can have responsive meetings as/if required.

