---
title: "HSF Packaging Meeting #36, 11 September, 2019"
layout: meetings
---

# {{page.title}}

## Agenda
[<span class="underline">https://indico.cern.ch/event/835207/</span>](https://indico.cern.ch/event/835207/)

Participants: Ben Morgan, Graeme Stewart, Hobbs Willett, Javier Cervantes, Ben Couturier, Marco Clemencic, Chris Burr, Pere Mato, André Sailer, Chris Green, Martin Ritter, Geri Ganis, Brinick Simmons


## Introduction (Graeme)
- CERN EP R&D has received funding, including efforts on software
  - Includes Turnkey Software Stacks, which will have strong relationship with work in this group
  - Will cover not just the build aspect, but also build reliability, correctness, and the
    distribution and runtime issues
- UK RSE conference next week [https://rse.ac.uk/conf2019/](https://rse.ac.uk/conf2019/), at least one speaker from HSF (Stefan Roiser)
- Spack won an Outstanding Technology Development award from the FLC Far West
- Other Items:
  - Chris Green: Paper accepted in CHEP on Spack-Dev
  - Next Meeting: 9th October, let Graeme and Ben know if you have anything to present

## Key4HEP Stack Update (Hobbs)
- Idea: One set of ready-to-use software for use by future experiments, improve reuse, reproducibility etc
- Workflow is build -> binary repo -> CVMFS
- Project work: Reproduce LCG stack in Spack, use at runtime, distribution
- Prototype via "spack install key4hep": a dependency only package
  - 100 or so packages
  - Packages.yaml to provide specifics (system etc)
- Internal/External compilers
  - Chose Internal (Spack supplied) for clarity, and does not require existing LCG as dependency
- View/Modulefile runtime environments trialled
  - View issues: merge conflicts between files amongst dependencies, manual setup for some environment variables
  - Modulefile issues: Can get very long PATHs
- Use cases:
  - Runtime: views simpler cleaner, albeit how to set some environment variables (like ROOTSYS)
  - Development: modulefiles better to give fine control
- Distribution: tested by two systems (publish/subscribe) that are independent
- Spack environments: like conda environments, allows a certain subset of packages to be "installed" in a View. Can share/preserve an environment through an environment file.
  - Some discussion about how these relate LCG-views, Conda environments.
  - Environments more a "librarian" level tool.
  - Use of Spack-Environments in HEP use cases to be clarified, questions of scalability vs use
- Still to do: Publishing on CVMFS for testing/use, complementary versions between Views/Modulefiles
- Chris Green: On binary distribution, were binaries removed on publish side, as subscribe side might accidentally use paths that still exist. Hobbs/et al, there are checks on this, testing ongoing
- Graeme: As recipes encode the awkward env vars to export to Modulefiles, could we write something (a spack plugin?) that would write a script to e.g., create the view and source a setup script? Should be possible.
- Pere: shouldn’t, or try to avoid, having to set these custom environment variables. All: many cases where this is not possible, or unclear, comes back to relocatability issues.
- Graeme: In LCG-cmake is the problem of packages touching the same file in a view? Pere: yes, and usual have to workaround these cases.
- Ben: would be good to get a blacklist of packages that cause problems for creating views. Identify whether package or packaging system causes issues, and report upstream as needed.


## AOB
- Next meeting provisionally 11th September
