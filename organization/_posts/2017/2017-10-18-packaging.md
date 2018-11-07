---
title: "HSF Packaging Group Meeting #12, October 18, 2017"
layout: meetings
---

# HSF Packaging Group Meeting #12, October 18, 2017

#### *Present*: Graeme Stewart, Benedikt Hegner, Liz Sexton-Kennedy, Guilherme Amadio, Pere Mato, Patricia Mendez Lorenzo, Javier Cervantes Villanueva, Marco Clemencic, Ben Couturier, Ben Morgan, Christopher Green, Jim Amundson, Patrick Gartung, David Lange, Emil Obreshkov, Shahzad Muzaffar, Oana Boeriu, Joel Closier

#### [Indico Agenda and Presentations](https://indico.cern.ch/event/672745/){:target="_hsf_packaging_12"}

## Introduction

* It was agreed that containers are an important topic for the group.

## Progress Reports

### Spack

* PGP signing is much more important for HPCs. HEP tends to have a trusted build chain managed by the same team, from checkout to CVMFS deployment.
* Relocatable build caches added to Spack, which was one of the missing features identified during the initial review.
* Additional topic on moving CMSSW from scram to CMake. Development environment is still missing.
* Pere: questions on relocation - how is that done? A: relative RPATH and text files get a path replacement at install time (rewriting the original file).
* Guilherme: what if the relocated RPATH is bigger than the original one? A: On MacOS you can set size. On Linux patchelf allows to use a bigger one. If path bigger than place reserved, you append on the end. Thus not a problem in practice.
* RPATH vs. RUNPATH discussion: for a development environment RUNPATH would be strongly favoured.

### SpackDev

* Presented how to set up a development environment with SpackDev. There is an added tool to ease building against system packages.
* Graeme: Can the working package set be updated? A: Not at the moment, but this feature is envisaged.
* What’s the definition of a "package"? SpackDev for packages as standalone externals or experiments' notion of packages as a subset of the code in the experiment application. A: This is not entirely scoped out yet. *Agreed on follow-up discussion on that.*

### Portage

* Presentation: prefixes can depend on each other. Unclear if this just layering of one prefix on top of another or a composable set of compatible prefixes. Should be followed up.
* Pere: How likely is interference between standard environment and portage environment? A: System tries to keep this well separated, by using RPATH for its own artifacts, so it should be quite safely setup.
* Ben Morgan: how to choose between multiple versions of the same package? A: Use `eselect` to set python and/or compiler version. Not so clear for libraries.
* If one wanted to build different combinations of non-leaf packages there may be scaling issues and unnecessary builds.
* Jim: Singularity could be used as part of environment decoupling.
* Ben Morgan: reminded of views in Spack (which exist in LCGCMake as well). 
* How to define the versions to build ->  portage-sets; allows to set consistent versions

## Next Steps

* Jim/Ben - Containerisation / continuous integration as follow up items
* Meeting in two weeks again. same time, probably focusing on Spack.
* Portage will be followed up after that.
* There is an open call for a second convener for the group to join Graeme.
