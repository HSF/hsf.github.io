---
title: Native Julia HEP Geometry package
layout: gsoc_proposal
project: JuliaHEP
year: 2026
organization:
  - CERN
  - TUM
  - MPP
difficulty: medium
duration: 350
mentor_avail: June-July, September-October
project_mentors:
  - email: florian.henkes@tum.de
    organization: TUM
    first_name: Florian
    last_name: Henkes
    is_preferred_contact: yes
  - email: pere.mato@cern.ch
    organization: CERN
    first_name: Pere
    last_name: Mato
  - email: oschulz@mpp.mpg.de
    organization: MPP
    first_name: Oliver
    last_name: Schulz
---

## Description
The Julia programming language offers a unique combination of speed, interoperability, ease of use, and flexibility, making it an attractive option for High Energy Physics (HEP) research. Within the HSF context, the [JuliaHEP](https://github.com/JuliaHEP) initiative aims to develop a set of foundational packages in the Julia ecosystem that provide the essential functionality required by HEP researchers.
In simulation and reconstruction codes, it is necessary to describe the detailed geometry of the detector, including both its spatial structure and the associated materials, surfaces, and other properties. This is typically achieved using a hierarchical Constructive Solid Geometry (CSG) representation, as implemented in frameworks like [Geant4](https://geant4.web.cern.ch). Reconstruction codes may, however, require a simplified version of this geometry.

The [Geant4.jl](https://github.com/JuliaHEP/Geant4.jl) wrapper package currently leverages the geometry modeling capabilities of the C++ Geant4 library. However, if we wish to develop physics process simulations natively in Julia and independent of Geant4, a geometry package implemented directly in Julia will be required. Such a package should aim to be user-friendly, high-performance, and compatible with hardware accelerators such as GPUs. An early effort in this direction is the [Geom4hep](https://github.com/peremato/Geom4hep) package, which could serve as a potential foundation for further development.

## Task ideas

- ...
- ...

## Expected results and milestones

- Successful development of a package with the basic geometry shapes
- Development of a set of benchmarks for comparing the performance with respect other packages (e.g. Geant4.j)

## Requirements

- Programming experience with C++ (in order to be able to understand existing HEP codes)
- Prior experience in Julia (very advantageous)
- A background understanding of high-energy physics (advantageous)

## How to apply

Once CERN/HSF is accepted as a GSoC org, please write an email with a short introduction to your interests and background to the mentors with the string "gsoc26" in the subject.
There will be a small evaluation task that we will mail to you then.

## Links

- [Julia Programming Language](https://julialang.org/)
- [JuliaHEP HSF Group](https://hepsoftwarefoundation.org/workinggroups/juliahep.html)
