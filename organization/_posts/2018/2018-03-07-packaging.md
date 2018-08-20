---
title: "HSF Packaging Group Meeting #20, March 7, 2018"
layout: meetings
---

# {{page.title}}

Agenda
======
[https://indico.cern.ch/event/708110/](https://indico.cern.ch/event/708110/)

Participants: Ben Morgan, Graeme Stewart, Lucio Anderlini, Patrick
Gartung, Oana Boeriu, Giulio Eulisse, Pere Mato, Shazad Malik Muzaffar,
Emil Obreshkov, Guilherme Amadio, Geri Ganis, Emil Obreshkov

Introduction - Graeme
=====================
-   Group invited to Naples WLCG/HSF Software Development session
    -   All welcome, though time (AM Central Europe) not optimal for all
        people!
-   As always, suggestions for additional talks in future welcome.

Use Cases - Graeme
==================
-   [Document](https://docs.google.com/document/d/1h-r3XPIXXxmr5tThIh6gu6VcXXRhBXtUuOv14ju3oTI/edit?usp=sharing)
    at "v0.99"
    -   Refined to remove (but
        [archive](https://docs.google.com/document/d/1dsgq_ba9WYd69yX6EKOwwaZCT26LJ3UbS7WTrlzXEZc/edit?usp=sharing))
        useful discussion on ease of use by end clients.
    -   Editing to focus on Use Cases rather than Requirements, though
        some blurring.
    -   Any remaining questions to go from 0.99-\>1.00?
-   Look through of document:
    -   Build section mostly unchanged, some additions on
        interoperability between different via build config files
        (pkg-config/CMake)
        -   Want to be clear on separation between responsibility of
            build system (developer) vs package manager (librarian)
        -   Comments that this is more on Software Development side.
    -   Install time relocatability not always required by all
        experiments, but keep it in to cover everyone.
        
Test Stack - Ben
================
-   List of packages now in a reasonable state.
-   Ben will send round a mail requesting input on "how to" on
    installing stack through considered package managers. Only
    consider install/build from scratch, no CVMFS just yet, just build
    from scratch on a bare metal Linux/macOS box.
    
Spack Status/Open Issues Discussion - All
=========================================
-   Starting point using Javier's presentation, initially three
    questions:
    -   Need a higher/more generic layer of software to configure Spack?
        -   Patrick: almost certainly if we don't want spack itself to
            become a kitchen sink.
        -   From developer point of view, likely not going to run spack
            directly.
        -   Main config: `packages.yaml` file to use/reuse packages from
            system or LCG. Right now this is awkward. Solution could
            be, e.g., SpackDev may generate this automatically.
    -   How do you manage the Spack configuration when building full
        stack?
        -   Patrick: Looking at [Lmod](https://lmod.readthedocs.io/en/latest/)
            to configure used packages, but
            issues with tracking a large number of dependencies and
            more than one core compiler. Also, "stack" spack on top of
            system by linking/softlinking system packages into area
            known by spack. Jim A looking at better way of doing this
            to track dependencies better than simple links; idea is to
            allow spack to read multiple spack-db files (i.e., local
            and pre-installed).
        -   Patrick: Lmod seems to be the way to go for setting up an
            environment portability across systems (local vs
            supercomputing) compared with say Scram/UPS. Question:
            what does lmod add vs EnvModules? Patrick: Use Lua rather
            than TCL, plus extra features such as "axes" for
            compiler/system etc. (though only three axes at the
            moment).
    -   How to distribute software using Spack?
        -   Patrick: Benedikt Riedel, from IceCube, was 
            trying install/use of spack on CVMFS.
        -   Question: Is spack not relocatable on CVMFS? Patrick: yes,
            apart from a few cases where absolute paths are compiled
            in (e.g., TCL). O.k. if can guarantee CVMFS mount point.
        -   Patrick: looking at checking/editing binaries (via strings)
            to see/fix up packages. Giulio: In AliBuild, store all
            path info hash, and have only use of dynamic loader path.
            CMSSW: Install part, relocate part, so can handle install
            not equal to relocate path.
    -   General discussion:
        -   Giulio: Good to have generated files to help pick up
            packages from system. Patrick: Jim A has something in
            SpackDev to do this.
        -   Patrick: Will probably find more issues as we go along at
            FNAL.
            
AOB
===
Next Meeting: 21 March 2018. Look again at Nix from Chris Burr.
