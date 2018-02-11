---
title: Open-Source Simulations for Gas Detector on Python
layout: gsoc_proposal
project: NEXT
year: 2018
organization:
  - UTA
  - CERN
---

# Description

Magboltz solves the Boltzmann transport equations with numerical integration in order to simulate the interactions of electrons in gas mixtures under the influence of electric and magnetic fields.

Degrad calculates the cluster size distribution and primary cluster distribution in gas mixtures for minimum ionizing particles and X-rays.

Both of these programs were originally made in Fortran, the code is available in the links bellow.

The goal of this project is to begin with a test python interface for Degrad and Magboltz, to design optimized python implementations of their processes, joint functionality, and can extend to new functionality related to the calculation as well as extensive reports of the results.

R&D of gaseous detectors requires simulations like those provided by Magboltz and Degrad. An open-source, modernized and optimized incarnation of this software would be employed in many existing R&D efforts.

In addition to the mentor listed, the author of the code will be available for consultation, documentation is accessible here:

## Task ideas and expected results

  * Exploration of the existing software is encouraged.
  * Optimization ideas and python implementation plans included in proposals will be positively considered.

  * Development of a fully-functional python API for joint functionality of Magboltz and Degrad with optional GUI controls.

  * Full implementation of the Magboltz and Degrad output with optimized and fully customizable outputs concerning the calculation as well as the results.

This will be the first open-source incarnation of this software. It is important that the addition of new information to the databases be user-friendly, and that the code concerning the calculations be modular.


**Requirements**: Strong Python skills, good knowledge of Fortran, ability to learn the physics and calculations concerning the Boltzmann transport equation.

**Mentors**:
* [Fernanda Psihas](mailto:sft-gsoc@cern.ch?subject=GSoC%20Gas%20Simulation)
* [Stephen Biagi](mailto:sft-gsoc@cern.ch?subject=GSoC%20Gas%20Simulation)


**Links**:
  * [Magboltz and Degrad Software in Fortran] (http://magboltz.web.cern.ch/magboltz/)
  * [Documentation] (http://cyclo.mit.edu/drift/www/aboutMagboltz.html)
  * [Article in sciencedirect] (https://www.sciencedirect.com/science/article/pii/S0168900298012339?via%3Dihub)
