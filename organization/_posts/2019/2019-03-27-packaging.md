---
title: "HSF Packaging Meeting #33, 27 March, 2019"
layout: meetings
---

# {{page.title}}

## Agenda
[<span class="underline">https://indico.cern.ch/event/802100/</span>](https://indico.cern.ch/event/802100/)

Participants: Graeme Stewart, Ben Morgan, Javier Cervantes, Pere Mato,
Patrick Gartung, Chris Green, Geri Ganis

## Introduction / JLab Summary (Graeme)
  - HOW2019 Workshop last week, 246 people, and lots of non-LHC and
    even non-HEP contributions
  - HSF Sessions as plenary, so didn’t clash with other software
    topics
  - Packaging covered under
    [Tools and Packaging](https://indico.cern.ch/event/759388/timetable/?view=standard#b-318083-hsf-parallel-software)
    session
  - Also for this WG: [PyHEP session](https://indico.cern.ch/event/759388/timetable/?view=standard#b-318084-hsf-parallel-pyhep) had two contributions on Conda
    related topics
  - Contribution from this group:
      - Activities
      - Packaging Tool Projects
      - Lots of discussion
          - Quite a bit covered things we’ve discussed/decided, but
            good to have it presented more widely
      - Key points:
          - Conda as a production release? Yes, it can lock/freeze
            versions. Issues to look at include release management,
            deployment to CVMFS
          - One tool or a suite? Open question, requirements differ
            between librarians and analysts. Single tool would
            concentrate expertise.
          - Why Spack AND Conda? Lots of history, e.g. no tool which
            does what Spack does when it started. Lots of
            updates/improvements to Conda recently
          - Can we adapt package recipes? Yes in Spack via specs/yaml
            files. Conda can have recipe parameters.
              - Patrick: spack package variants come at cost of
                concretization time (more paths to try)
          - Interactions with underlying system? HepOSLibs vs RPath
            (and the Shallow vs Deep build argument). Package group
            support RPath to cleanly separates different environment.
            ATLAS: workflow relies on LD\_LIBRARY\_PATH to override
            for testing local rebuilds.
  - Today: SuperNEMO+Spack, Spack and ROOT matters.
  - Next meeting: 24th April, though potential clashes with FR/CH
    school holidays

## SuperNEMO (Ben)
  - Homebrew becoming less friendly for SuperNEMO
      - Removing options to build from source
      - No variants - builds becoming very large
  - Need to be more flexible for the coming phase of the experiment
  - Forked from main Spack repo for first trial
      - Taking some things from the system as needed
  - Defined a Spack package repo for the experiment, so that it was
    under expt control and was easier to mimic current brew setup
      - Package repo added manually - probably a better way for longer
        term
  - Did submit some PRs for `cxxstd` issues to upstream spack
  - OS X library path issues come up and are tricky
      - This is annoying - best option is to submit PRs when
        problematic packages are found
  - Easy to create containers using Spack, as yet limited use of build
    caches
  - Current containers are completely self-contained - use of CVMFS
    for large packages like G4 would be useful
  - Would like to test a lot more Spack features and spack-dev
  - LArSoft will be supported soon in the FNAL MVP - useful for DUNE
  - CVMFS - who can run this for us?
      - EGI might help, or GridPP
      - OSG is US only
      - SuperNEMO not recognised by CERN
      - `/cvmfs/hsf.org` is partially setup
          - Geri - this is quite close to being ready now and can be
            used for testing soon
  - How do you keep track of the versions you want to install?
      - At the moment it’s not done - use packages.yaml to fix a few
        versions, but mainly relying on having a controlled fork where
        updates don’t happen in an automatic way
      - Could also do this with a SuperNEMO fork, that only syncs with
        Spack develop branch occasionally
      - Patrick - there was a bug where packages would have their
        dependency hashes change because of patch ordering and trigger
        lots of rebuilds
          - (fix is not yet merged,
            <https://github.com/spack/spack/pull/10879>)

## Spack ROOT Recipe (Javier, Patrick, Chris)
  - Context: ROOT recipe update in Spack PR [\#8428](https://github.com/spack/spack/pull/10879)
      - Merged in February
      - Focused on creating a good default recipe
          - Build options as variants (mostly OFF)
          - Use Spack dependencies instead of ROOT downloading them as
            builtins
          - Based on Gentoo/Portage recipe from Guillherme Amadio for
            default build options (on or off)
          - Fixes for removing deprecated options
      - gminimal request: Fermilab uses slightly different recipe
          - Should it be on or off?
          - “ON” version includes X11, but doesn’t automatically
            search for other support libraries
          - May be better as it gives you a known starting point for
            adding extras
          - Otherwise, might get odd builds if it enables an option
            because it found a system library, or activates a
            download.
          - Meeting agrees this should be a variant, set to ON by
            default, to avoid accidental inclusion of build options
            that happen to be on the build machine (but might be missing on
            deployment)
      - \-isystem support in Spack
          - \-isystem dir means “Search dir for headers after all
            directories specified by -I but before standard system
            dirs
          - ROOT (6.13.02-6.16.0) now uses this
          - Problem \#10850 on Spack with ROOT recipe
          - Triage: Spack compiler wrapper ignores -isystem option
            (correctly) defined by packages and uses -I instead
      - WIP:
          - Spack should support this option
          - Chris Green currently working on spack internals in an
            attempt to solve this issue
          - Need further discussion with Spack team
          - Follow things on the Spack\#HEP channel in Slack

## AOB
  - Next meeting proposed for 24th April
