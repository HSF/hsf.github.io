---
title: Julia Interfaces to HepMC3
layout: gsoc_proposal
project: JuliaHEP
year: 2025
organization:
  - CERN
difficulty: medium
duration: 175
mentor_avail: June-July- August
project_mentors:
  - email: graeme.andrew.stewart@cern.ch
    organization: CERN
    first_name: Graeme
    last_name: Stewart
    is_preferred_contact: yes
  - email: mateusz.jakub.fila@cern.ch
    organization: CERN
    first_name: Mateusz
    last_name: Fila
---

## Description

In high-energy physics experiments at [CERN](https://home.cern/) it is necessary to simulate physics events in order to compare predicted observations with those that the LHC experiments actually observe. A key piece of the software chain used to do that is the [HepMC3](https://arxiv.org/abs/1912.08005) event record library, which encodes the output from physics event generators in a standard way, so that they can be used by downstream detector simulation and analysis codes.

There is now [increasing interest](https://doi.org/10.1007/s41781-023-00104-x) in using [Julia](https://julialang.org/) as a language for HEP software, as it combines the ease of programming in interactive languages, e.g., Python, with the speed of compiled language, such as C++. As part of building up the ecosystem of supporting packages for Julia in high-energy physics, developing interfaces to read, manipulated and write HepMC3 event records in Julia is the aim of this project.

## Task ideas

This project would develop a wrapper library for [HepMC3](https://gitlab.cern.ch/hepmc/HepMC3) allowing the HepMC3 data objects and methods, in C++, to be called from Julia.

It would utilise the general underlying wrapper interfaces in [CxxWrap](https://github.com/JuliaInterop/CxxWrap.jl) and the automated wrapper code generator [WrapIt!](https://github.com/grasph/wrapit) to allow for as easy and maintainable an interface as possible.

A key outcome would be a set of unit tests and examples, based on the HepMC3 ones, demonstrating how to use the library and proving that the code is correct.

## Expected results and milestones

- Reading of HepMC3 event files
    - Particularly the ASCII format will be targeted first
- Access to event data structures
    - Access to particle properties
    - Navigation of the event and the vertices between parent and child particles
    - Access to run information
- Update of HepMC3 data structures
- Creation of new HepMC3 events
- Re-serialisation of these events to file
    - Initially ASCII
- Documentation and examples on how to use the Julia interfaces
- HepMC3.jl package registered in the Julia general registry
- Extension of serialisation to ROOT format (stretch goal)

## Requirements

- Programming experience in C++
- Prior experience in Julia (very advantageous)
- A background understanding of high-energy physics (advantageous)

## Links

- [Julia Programming Language](https://julialang.org/)
- [JuliaHEP HSF Group](https://hepsoftwarefoundation.org/activities/juliahep.html)
- [HepMC3 Repository](https://gitlab.cern.ch/hepmc/HepMC3)
- [CxxWrap](https://github.com/JuliaInterop/CxxWrap.jl)
- [WrapIt!](https://github.com/grasph/wrapit)
