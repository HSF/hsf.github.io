---
title: "HSF Software Forum on Potential Gains from Modern Hardware, 10 October, 2018"
layout: meetings
---

# {{page.title}}

[Meeting Agenda and Slides](https://indico.cern.ch/event/745286/)

Introduction
============
- There is a free forum slot in 2 weeks time (24 October). Contact
  Graeme if there is interest in presenting something.
- Otherwise we should start to consider presentations for next year.

Potential Gains for Software from Modern Hardware
=================================================
-   AutoFDO
    -   FullCMS example for AutoFDO is Geant4 example with the full CMS
        geometry, but not an actual full simulation
    -   Static build is probably really needed for some of the
        optimisations
    -   Getting a large static G4 library incorporated into an ATLAS
        simulation build has not been easy
    -   AutoFDO project itself only seems to develop slowly
-   Small allocations/deallocations
    -   Initialisation and destruction is costly, especially for more
        complex objects
    -   Optimisations can be to use size knowledge (`vector::reserve()`),
        arenas, simpler objects
-   Trident
    -   Try to avoid problem of breaking hotspots into multiple smaller
        “warm” pieces
    -   Does HEPSpec model our codes well?
        -   Not at the instruction level!
    -   Geant4 is measured not to be bound by memory access speeds
        -   This is interaction with memory subsystem, not any new/free
            activity
    -   Both simulation and digi/reco show a lot of memory “port” access
        and much less arithmetic than expected
    -   Trident can be started/stopped, but not programatically at the
        moment
        -   Overheads are measured and usually \~1%
-   Haswell is much better in code page access, which is why the single
    library shows so much less gain on this architecture than Ivy
    Bridge
-   Jakob - scope of R&D and gradual improvements is quite different,
    R&D might only target one aspect, limiting the overall impact;
    where as the gradual improvements might be very generic to the
    whole code base
-   David L - HL-LHC simulation for CMS is projected to be only 5% of
    overall workload
    -   Reconstruction scales in a very non-linear way, but simulation
        not so
-   Stefan R - but for LHCb 90% is simulation!
-   ALICE clarification: x15 is speed up on a single CPU, then x10 for
    GPU on top
-   What is “exploiting modern CPU arch”, +100%?
    -   It’s re-coding for vectorisation
    -   Pere - but GeantV has put a lot of effort into doing this and does
        not even get x2 speed up.
    -   Other sciences can have different problems, more amenable to
        these improvements
        -   Working often with software engineers at centres, but our
            code has been quite optimised already
    -   LHCb got a perfect speed-up in RICH reco (x8), but this is only
        one piece of the code base, so overall impact for the application
        is much less
-   Data structures are important
    -   For GeantV, need to go beyond 1-D binning
    -   However, data access patterns can vary through the processing
        chain
-   LHC detectors are running, so we need to keep things working without
    breaking as well, stopping and rewriting everything is not going
    to happen
-   Stewart MH has been looking at LTO in ATLAS - anyone else? Could
    be an interesting topic for a future meeting
