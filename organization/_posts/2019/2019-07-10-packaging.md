---
title: "HSF Packaging Meeting #35, 10 July, 2019"
layout: meetings
---

# {{page.title}}

## Agenda
[<span class="underline">https://indico.cern.ch/event/829817/</span>](https://indico.cern.ch/event/829817/)

Participants: Ben Morgan, Javier Cervantes, Guilherme Amadio, Graeme Stewart, Hobbs Willett, Pere Mato


## Introduction (Ben)
- Ongoing Projects: Spack
  - Build of LCG Stack with Spack ongoing, Hobbs Willett (CERN Summer Student)
    working with Javier and Graeme
  - Paper for CHEP2019 (Spack for FCC/SuperNEMO) accepted
  - SuperNEMO making last Homebrew-based release
    - Work with Spack ran into issues with ROOT on macOS due to mixed
      System/XQuartz OpenGL. Will report to Spack GitHub/Slack when diagnosed/fixed
    - Looking at Environments/Views for runtime
      - Hobbs: some issues found with views as they do not allow more general environment
        settings like ROOTSYS and similar.
      - Javier: Modules more flexible here, can provide environment specifications in recipe,
        and resultant files used by other third-party module systems
  - FNAL's MVP1a for LArSoft Spack/SPackDev released for testing and feedback
    - Ben has tried the initial setup/install with success.
- AIDA++ LoI for Turnkey Stack"
  - In to AIDA call: <https://docs.google.com/document/d/1wf9AnL2T713idpdG0qz8J2v6iPI94LZscY5PL333Ikc>
- Next meeting:
  - With summer here, provisionally reconvene on 11th September
  - Ad-hoc meetings over summer can be held if wanted, or use the
    mailing list for discussions

## Key4HEP Stack (Graeme)
- Presentation from FCC meeting
  - More than just packaging, but of interest to cover larger problem space and motivate work of packaging
  - Motivation is whole experiment software lifecycle
  - First: ideas, to concepts, to design.
    - Design needs flexibility, but lots of details to think about
  - Then:
    - Production
      - Real world: calib, align, dead/noise
      - Stability, but continually improve
    - Upgrade
      - Design and implement improvements
    - Preservation
- The HEP Application Stack
  - Familiar to the WG, Common OSS, to Core HEP (ROOT, etc), to Specific HEP (Geant4, event gen), Experiment Framework (Gaudi etc), Experiment specific (usually data representation and access), Experiment Apps
  - A true ecosystem of interacting parts
    - Packaging: building the parts in a consistent way
- Key4HEP Motivation
  - Future detector studies need well-maintained, but low maintenance stacks
  - Currently a scattered landscape of generic/specific tools
  - Aim at common stack for future colliders
- Goals:
  - Stack of packages covering different domains, avoiding AFAP overlaps
  - Turnkey stack connects packages
- Levels of Interoperability
  - 0: Common data formats
  - 1: Callable Interfaces (cross-language calls considered)
  - 2: Introspection (interaction of objects in generic manner, exemplar is PyROOT, Python -> C++)
  - 3: Component Model: General features like configuration, logging, error reporting (essentially the framework)
- Building on HSF Project Template
  - Share basic OSS setup/build interfaces
- EDM4HEP
  - Event Data Model can be main "language" that components communicate by.
  - ILC/CLIC experience of common EDM has been positive
- Implementation
  - Move from direct OO implementation to YAML based description, with automatically generated code in target languages
  - Helps in optimization, cross-language use, different persistency backends
- Exp Framework
  - Skeleton on which apps are built
  - Common cross-experiment framework helps interoperability
  - Key4HEP will use Gaudi
    - Gaudi Modernisation project underway
- Progress:
  - ILCsoft algos into key4HEP via a Marlin-to-Gaudi wrapper (code on GitHub)
  - LCIO reimplemented in PODIO
    - Example of PODIO implementing a generic data model (LCIO)
  - Spack: Building minimal stack with ROOT and all deps
    - Binary caches, module file for runtime, package relocation
    - TODO: EOS/Web for binaries, distrib. to CVMFS (hsf.org test repo in progress)
- Next Steps:
  - General agreement on moving to common HEP software stack by future experiments
  - Core features in progress: Spack for build, EDM4HEP
- Hobbs: How high does Key4HEP stack go? Graeme: from base HEP applications up to EDM
- What about database interfaces? Implementation usually at production phase, interfaces might be part of Key4HEP (e.g. Gaudi might provide these, particularly as concurrency is important)
- Ben: Has come from future colliders, but could it be used by smaller communities/experiments? Graeme: Yes, hope this is the case, advantage of Spack gives flexibility in provision and use, or even rebuild, of stack.
- Graeme: EDM coming from linear collider community, but PODIO has compositional model so allows reuse, as well are simple-to-complex designs.

## AOB
- Next meeting provisionally 11th September
