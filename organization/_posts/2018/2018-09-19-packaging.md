---
title: "HSF Packaging Group Meeting #27, September 19, 2018"
layout: meetings
---

# {{page.title}}


Agenda
=======

[https://indico.cern.ch/event/754985/](https://indico.cern.ch/event/754985/)

Participants: Graeme Stewart, Ben Morgan, Guilherme Amadio, Javier Cervantes Villanueva, Patrick Gartung, Liz Sexton-Kennedy, Ben Couturier, Marco Clemencic, Martin Ritter, Jim Amundson, Hadrian Grasland, Todd Gamblin, Oana Boeriu

[Introduction - Graeme](https://indico.cern.ch/event/754985/contributions/3128664/attachments/1709906/2774762/HSF_Packaging_Group_Intro_2018-09-191.pdf)
=====================
- CHEP Presentations x5 on packaging topics
- Liz asked about how IceCube discovered Spack (was it via HSF?)
  - Not clear at the moment
- Report to LHCC on Software
  - Packaging included: main feedback, “when will conclusions be reached?”
  - For us, means we need to start delivering working prototypes
- Today: Two updates on Spack work



[Spack and FCC Update - Javier](https://indico.cern.ch/event/754985/contributions/3128668/attachments/1718723/2773707/SpackHSFMeeting-SummerStudent2018.pptx.pdf)
=============================
- FCC Use Case:
  - Use LCG CVMFS install (base), plus Spack "packages.yaml" describing them as “system” packages
    - Graeme: is there a script to generate this? Yes.
  - Allows override of LCG packages as required
  - Layered config: FCC specific packages used first, then LCG then Spack base
- Workflow:
  - From CVMFS, merge LCG and FCC packages.yaml
  - Run `spack install <metapackage>` using this, outputting binary tarballs
  - Binary tarballs deployed/published on CVMFS, plus spack view creation
  - Graeme: We have tested parallel publication to CVMFS from many
    nodes that not only performs better, but simplifies the workflow
    as the build node can also take care of publishing the results
    (see [presentation](https://indico.cern.ch/event/746546/contributions/3086271/attachments/1708942/2754445/Deployment_of_ATLAS_releases.pdf) from Tomas Stefan's summer student project).
- Next: speed up builds, try to avoid rebuilds of things already in CVMFS
  - Spack cache to use ccache (since July in Spack). Easy to setup, integrate with Jenkins. Up to 30% speedup found
  - Spack chain: still in development in Spack (Spack PR#8772). Provides concatenation of N install trees. Allows incremental builds via reuse of existing install trees. See Spack PR#8014 for use cases. FCC use is two-link: CVMFS tree + Build node tree
- Results with spack chain
  - Reduced build time from 52 minutes to 1 minute. Down to 28 seconds if fccdevel is also in CVMFS
- CDash integration: currently not working, but several ongoing Spack PRs (see PR #7114) for details.
- Summary: FCC using Spack + scripts to complete workflow, recent spack developments have helped to speed up builds.
- Patrick: current holdup on spack chain is related to recording of installation database
- Todd: Very useful contributions from HEP. More work next year on HPC deployments, also working with CEA on their requirements.
- Ben C: How difficult was it to reuse the LCG CVMFS stack? O.k., but some issues due to underlying differences between LCG/Spack ways of doing things.
- Graeme: Would be great to see spack used to build the LCG set of packages as the base of a chain. Javier: Can share recipes/scripts.

[Dockter Spacklove - Hadrien](https://indico.cern.ch/event/754985/contributions/3144307/attachments/1718025/2772358/Spackaging.pdf)
===========================
- Basis for work: long term issue of building/portability in HEP, toolchain improvements to help this
- Portablitity from CERN/WCLG p.o.v: Portable if SLC6, have CVMFS
- Rest of world p.o.v: Portable if runs on my computer. Many Linuces/Unices, offline working
- User profiles
  - Testers: quick setup, o.k. With lack of host OS integration
  - Developers: use “full” system (dev/GUI/drivers), o.k. With large builds if infrequent and automated.
  - Both: can assume some computing proficiency
- For testers: Containers best solution? Singularity good for scientific use, but Docker better for usability (at present)
  - Graeme: may have Docker for development, Singularity for runtime. Hadrien: have seen some issues with running Singularity containers
- Developers: Custom build on base system, avoid too much isolation.
  - Playoff between integration/reproducibility.
  - Main dependencies plus opt-in use of system packages
- Package managers: various forms of flexibility needed for these use cases
  - Languages, portability, environment, opt-in use of system.
  - "Cousin" builds: Same package versions apart from build options.
  - Spack seems most appropriate here
- PMs + Containers:
  - Big dockerfile -> few pm commands
  - Testers -> devs easily via set of PM commands (vs different distros)
- Work so far: Simplification via moving build recipes -> Dockerfiles. Trying to move most shell scripting to Spack commands.
  - Testing by installing Verrou, Templight, ACTS, Gaudi
- Example of Dockerfile for Gaudi: huge reduction in SLOC: 234 -> 234 (⅔ comments)
- Conclusion: Containers + PMs help the Tester/Developer use cases and ease transition back and forth between them.
- Javier: Will update Spack ROOT recipe ASAP.
  - Patrick: [FNAL also have a ROOT recipe](https://github.com/FNALssi/spack/blob/fnal-develop/var/spack/repos/builtin/packages/root/package.py)
- Ben C: Agree on Containers+PMs being friends, have seen issues with trying to run modern code natively on old (in this case SLC5) grid nodes.
- Todd: Would like to get glibc dependency in Spack at some point.
- Hadrien: One other use case, somewhat specific, for containers is when using a rolling Linux distro. When rolling updates compiler etc, spack etc may want/need to update/rebuild everything.

AOB
===
- Next meeting 3 October: [https://indico.cern.ch/event/758817/](https://indico.cern.ch/event/758817/)
  - One presentation from FNAL on Spack/Spack-dev
  - As ever, more contributions welcome, contact Graeme and Ben
- Todd: very happy with collaboration with HEP so far, would like
  to prioritise important HEP use cases (very good PRs received)
  - Graeme and Todd will keep in touch to better communicate and align goals and developments
