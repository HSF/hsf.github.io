---
title: "HSF Packaging Group Meeting #28, October 3, 2018"
layout: meetings
---

# {{page.title}}

Agenda
=======
[*https://indico.cern.ch/event/758817/*](https://indico.cern.ch/event/758817/)

Participants: Graeme Stewart, Pere Mato, Gerri Ganis, Liz Sexton-Kennedy,
Patrick Gartung, Guilherme Amadio, Lynn Garren, Chris Green, Jim
Amundson, Benedikt Hegner

Introduction
============
-   We can have another meeting in 2 weeks time, if people have
    contributions to make.
    -   Guilherme could report on Portage stack.
    -   Pere can report on LCGCMake updates.

FNAL Spack Update
=================
-   MVP = Minimum Viable Product.
    -   This is for experiments to try and give feedback.
    -   SLC7, gcc7.3 with C++17, “prof” optimisation level.
    -   Top package is the art suite, should be good for interesting
        development.
    -   N.B. LArSoft can’t yet be used as the external requirements are
        large.
-   Feedback on instructions and documentation as well as MVP itself
    welcome.
-   When you install an MVP it’s self-contained - it downloads things to
    your local system and builds them.
    -   There are a few pre-requisites (gzip, tar) needed from the
        system and the bootstrapper checks that.
    -   As gcc gets built from source it all takes an hour on a powerful
        machine.
-   In `srcs/` there is a top level CMakeLists.txt that orchestrates the build
    of all of the local packages here.
    -   The CMakeLists.txt is constructed from the Spack recipe for each
        of the packages.
    -   Captures any dependencies between these local packages.
    -   Spackdev requires spack concretisation, so it can get slow for
        deep/wide dependencies.
-   Dependencies need to be fully built and installed before any
    dependent package can proceed with its build.
-   For Python packages?
    -   Only CMake supported (at the moment), so not possible to do
        this, but this is a future feature.
    -   Extraction of the build recipe from Spack to push into
        CMakeLists.txt makes things more complex than normal - not
        using all the ‘native’ features of `ExternalProject_Add()`.
-   Pere: Bootstrap of CMakeLists from Spack seems the wrong way around.
    Developer should start with CMake and then develop a Spack recipe
    to share the package.
    -   Key feature is the ability to work on multiple developments and
        have all dependencies resolved, so that requires Spack-level
        information to bootstrap.
    -   Allows developments and dependencies to be handled more easily
        than in ‘native’ Spack.
        -   This is a feature of the current FNAL development
            environment and experiments wanted this to be reproduced.
    -   It’s hard to make Spack itself build from a checked out and
        modified code base instead of from a git reference.
        -   Could that be an extension for Spack?
        -   Patrick - not a feature in Spack right now.
        -   Jim - Todd G is supportive of managing this external to
            Spack.
-   SpackDev as a Spack extension would allow this all to look more
    natural (`spack dev ...`) and improve performance (only one
    concretisation process).
-   Guilherme: Can Spack update itself?
    -   This essentially a `git pull`; but then any updated recipe
        changes hashes and would bring a lot of rebuilds along.
    -   Would maybe be useful to separate the recipes and the core Spack
        code (Jim was supportive of this idea).
        -   Although you can override any recipes with your own (and
            keep them the same).
-   SpackChains and BuildCache demonstrate a good and healthy
    interaction between HEP and Spack developers.
-   Many other developments needed to move to a full product and working
    ecosystem.
-   Patrick: a Spack environment command is being development and would
    be able to record and lock versions, for making releases (writes a
    packages.yaml).
    -   A packages.yaml file declares paths and versions only, so system
        updates can happen (but update the version if something is
        incompatible!). Full implications should be explored though,
        we don’t really have experience of this.

AOB
===
-   With Pere and Guilherme’s updates we plan to have the [*next
    meeting*](https://indico.cern.ch/event/762971/) in 2 weeks time.
