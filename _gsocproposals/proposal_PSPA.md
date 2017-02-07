---
title: State-of-The-Art Web Interface for Describing Accelerator and Associated Simulation
layout: plain
project: PSPA
organization: LAL
---

# Description

[PSPA](https://groups.lal.in2p3.fr/pspa/) (Platform for Simulation of Particle Accelerators) is an original web-based interactive simulation platform for designing and modeling particle accelerators, created at Laboratoire de l’Accélérateur Linéaire (LAL), Orsay. It aims at eventually containing all the tools to make a start-to-end simulation of an accelerator, and make it possible to run interactively several open source simulations codes available worldwide. PSPA doesn't provide its own simulation tools but allows to use the existing
most appropriate tools for a given use case.

At the moment, the focus is on electron/positron accelerators. PSPA will optimize the work of accelerator designers by factoring once and for all the tedious, time-consuming and error prone process of translating data formats between the various codes involved in the modeling of a machine, controlling the repeated execution of these models by easily varying some parameter and managing the associated data. Moreover, as a truly innovative feature, it will provide a convenient means for testing different physical models of a given part of a machine. 


## Task ideas and expected results:  

The attractiveness of this platform is based on the simplicity of use and its ergonomics. The current version is a prototype demonstrating
the feasibility and usefulness of the platform. The work so far has concentrated on the integration of existing open-source simulation
tools and the translation between their native data formats.

The goal of this project is to improve the ergonomics through the redesign of the interface and its reimplementation (currently based on 
Wt) on more flexible and powerful Web application frameworks and libraries. This includes: 
* Implementation of an intuitive user interface, using JavaScript libraries, providing the currently existing features.
* Design and implementation of a graphic interface allowing to build and modify easily the graphic representation of the simulated accelerator.
  * A challenging issue is how to handle the graphic representation of large objects (particle accelerators can have hundred or thousand of building blocks) and how to manage zooming (multiple scales) in selected parts.

The new interface will have to interact with the existing code used to integrate the various simulation tools, written in C++.

## Requirements

 * At least one Web application framework
 * html5
 * JavaScript
 * css3
 * C++


## Mentors

* [François Touze](mailto:touze@lal.in2p3.fr)
* [Antoine Pérus](mailto:perus@lal.in2p3.fr)
* [Marc Nicolas](mailto:nicolas@lal.in2p3.fr)
