---
title: "HSF Software Tools and Packaging Working Group Meeting #1, 26th February 2020"
layout: meetings
---

# {{page.title}}

## Agenda
[<span class="underline">https://indico.cern.ch/event/888898/</span>](https://indico.cern.ch/event/888898/)

Present/Contributors: Serhan Mete, Ben Morgan, Patrick Gartung, Martin Ritter, Graeme Stewart, Guilherme Amadio, Hadrien Grasland, Andre Sailer, Liz Sexton-Kennedy, Pere Mato, Lukasz Kreczko

Apologies: 

## Introduction

- What about some CI for important HEP packages in Spack? Try to make sure that things don't break when dependencies get updates.
    - Sounds useful, at least for tagged releases of Spack
- Software Tools can piggyback on other events, e.g. the HSF workshop, but good topics to cover:
    - Static analysers
    - Linters
    - IDEs
- HSF Workshop
    - Note the software deployment BoF on Monday morning, important overlap with packaging and maybe IDEs (developer environment)
    - Graeme: On Accelerator profiling tools, maybe a place for this on Tuesday session on "end-to-end" use of these devices.
    - Serhan: names (ATLAS-centric) for accelerators include Attila, like to identify more.
- Upcoming Events
    - Intel workshop focussing on oneAPI and optimization (24-26 March at CERN). Places limited, so register early!
    - Software Carpentry (24-27 March 2020 at CERN) organised by HSF, IRIS-HEP. Excellent for newcomers, non-experts, but opportunity to volunteer for tutoring.

## Spack Buildcache Updates
- Prompted by feedback on Spack Slack:
    - University of Oregon: contact about setting up CI pipelines to build packages (for E4S project)
    - See slides for links to public cache/key
    - Pipeline cache-only install for deps, then build from source for package. Binary pushed to mirror
- Cache-only installs were inefficient as **all** `spec.yaml` files were downloaded (including across all platforms)
    - Ended up spending more time downloading spec files than installing/building
- PRs on Spack GitHub to only download specs for current OS+arch
- Additional PRs to only find spec(s) needed by concretized package, and use internal cache correctly
- Testing found other issues, now fixed and available on Spack v0.14
    - Command line constraints
    - Better `patchelf` error handling (full statically linked executables have no rpaths)
    - Handle hardlinks correctly to avoid direct copies (and large buildcaches)
- Further work in progress
    - Handle installing buildcaches in non-default directory layout (arch/compiler/compilerver etc)
    - Several different implementations trialled, focused on handling different prefixes and resulting rpaths
    - Awaiting review
- Other items
    - Require -d flag when creating buildcache directory
    - Allow install of, e.g. macOS, buildcache on, e.g. Linux (and vice versa). Helps with installing on CVMFS
- Ben: is Oregon work essentially Ben's "full lifecycle" note. Yes.
- Patrick: Some devs form Kitware working on same topic. Also work at FNAL on publishing buildcaches to CVMFS. 
- Univ of Oregon contact: eugeneswalker on github, Luke on spack slack
- Kitware contacts: opadron on github and spack slack, scottwittenburg on github scott.wittenburg on spack slack

## AOB
