---
title: Hardware acceleration of scattering routines in SixTrack
layout: gsoc_proposal
project: SixTrack
year: 2019
organization: CERN
---

## Project Description

When high energy protons in the LHC are intercepted by the collimator jaws, they undergo scattering due to the interactions of the incoming protons with either the electromagnetic field of the atoms, or the strong potential of the nucleus. Presently, a physics model for the scattering mechanisms is implemented in SixTrack using a Monte-Carlo code. The interactions fall into four categories: nuclear interaction, coulomb scattering, ionization and hard electromagnetic processes (e.g. pair production).

A strong background in computer science and programming languages as well the
interest to understand computational physics methods implemented in the code are
sought. The unique challenge will be offered to work with a high-performance
production code that is used for the highest energy accelerator in the world -
and thus the code's reliability and backward compatibility cannot be
compromised. There will be the opportunity to learn about methods used in
simulating the motion of particles in accelerators.



## Expected results
Demonstrate that the C code running on a GPU can run the scattering routines at the same speed or faster than on CPU, while keeping bit-level identical results.

## Mentors

  * [Johann A. Briffa](mailto:johann.briffa@cern.ch)
  * [Riccardo De Maria](mailto:Riccardo.De.Maria@cern.ch)
  * [Gianluca Valentino](mailto:Gianluca.Valentino@cern.ch)

## Requirements
Experience with Fortran, C, OpenCL and/or CUDA, vectorization techniques.

## Web Page
[cern.ch/sixtrack](http://cern.ch/sixtrack)

## Source Code 
[github.com/SixTrack/SixTrack](http://github.com/SixTrack/SixTrack)
