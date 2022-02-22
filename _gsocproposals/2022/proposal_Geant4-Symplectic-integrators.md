---
title: Symplectic integrators for Geant4
layout: gsoc_proposal
project: Geant4
year: 2022
difficulty: high
duration: 350
mentor_avail: June-September, can extend up to November. Student must start by July 1, to ensure good startup coordination during a period of frequent, potentially daily communication (when all mentors are available).
organization:
  - CERN
  - FNAL
---

## Description

The [Geant4][geant4] toolkit is the basis of the particletransport applications used in High Energy Physics (HEP) experiments, at CERN, other laboratories worldwide and in a large number of diverse applications. It provides all the capabilities needed to simulate the interactions and energy deposition in setups including HEP and Nuclear physics detectors, particle accelerators, medical imaging and treatment devices based on X-rays or particle beams, and even the probing of large structures such as the pyramids using the muons in cosmic rays.

A key ability of Geant4 is the propagation of charged particles in electromagnetic fields.  A challenging application involves the tracking of particles in accelerators for a large number of turns. 

The [g-2][g2] physics experiment at Fermilab seeks to uncover whether a yet undiscovered forces influences how the spin of the muon behaves.  To do this it measures the polarisation of the muon to seek new physics over thousands of revolutions in its custom accelerator ring.  To replicate this in Geant4, the toolkit must track muons for 5,000 turns with near-perfect energy conservation and no drift in particle momentum.

This project aims to identify and implement a small number of methods which do not accumulate errors in energy and phase space volume over many integration steps. Some derive from the development of symplectic integrators applied also to the study of the long term evolution of the motion of planets and stars. Other candidate methods are borrowed from the particle-in-cell methods used to study plasmas, such as those at the center of active galaxies or in fusion reactors.

The project aims to implement into Geant4 methods with these characteristics - potentially one of each type.

## Task ideas
 * Implement simplest general 2<sup>nd</sup>-order symplectic integration method (e.g. from Julia package)
 * Implement a low order (2<sup>nd</sup>) symplectic method specific for electromagnetic fields
 * Implement a higher order (3<sup>rd</sup>, 4<sup>th</sup>) symplectic method for electromagnetic fields
 * Identify alternative candidate integrators with different order and computational costs
A key element of each task will be to benchmark the implemented method against the 'standard' integration methods in Geant4 (such as the Dormand-Prince 5th order Runge-Kutta method - as known as DoPri or DoPri5 in other tools) comparing accuracy and computing time performance. The setups will range from the simplest (a constant magnetic field) to models of realistic accelerator setups.

## Expected results
Working implementations of symplectic integration in Geant4.

## Evaluation Task
Interested students please contact John for a warm-up and evaluation task.

## Requirements and desirable skills
- C++ : intermediate knowledge (classes, reading/writing code), 
- Basic knowledge of Numerical Methods (floating point numbers, basic numerical analysis, ability to estimate cost of operations.
- Knowledge of numerical methods to solve for differential equations would be an asset.
- Physics course on Mechanics (covering Hamiltonians) would be an asset.

## What you will learn
You will gain experience 
- to use elements of Geant4, a sophisticated toolkit for simulations of particle transport;
- about numerical integration methods for differential equations, their implementation;
- to create reliable, validated code which will be used by a leading edge physics experiment.

## Mentors
  * **[John Apostolakis](mailto:john.apostolakis@cern.ch)**
  * [Soon Yung Jun](mailto:syjun@fnal.gov)
  * [Renee Fatemi](mailto:renee.fatemi@uky.edu)

## Links
  * [Geant4](https://cern.ch/geant4/) and its module to [propagate in magnetic fields][field_propagation]
  * Tao, Molei. “Explicit High-Order Symplectic Integrators for Charged Particles in General Electromagnetic Fields.” Jour. of Comp. Phys. 327 (2016), p245–251 in [journal](https://doi.org/10.1016/j.jcp.2016.09.047), with full text also in [arXiv](https://arxiv.org/abs/1605.01458)
  * [Symplectic Integration, Z. Parsa and E. Forest](https://www.bnl.gov/isd/documents/14517.pdf)
  * Zenitani, S., & Umeda, T. (2018). "On the Boris solver in particle-in-cell simulation." [Physics of Plasmas, 25(11), 112110](https://doi.org/10.1063/1.5051077)

[geant4]: https://geant4.web.cern.ch
[g2]: https://muon-g-2.fnal.gov
[field_propagation]: https://indico.cern.ch/event/1014059/contributions/4307722/attachments/2254579/3825301/MagneticField2021.pdf
