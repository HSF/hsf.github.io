---
title: "HSF Software Tools Meeting, 14 June, 2018"
layout: meetings
---

# {{page.title}}

Agenda
======
[https://indico.cern.ch/event/735132/](https://indico.cern.ch/event/735132/)


Profilers
=========
-   Andrea - main goal is to correlate with a line of code. There is an overlap with
    deployment and infrastructure monitoring. How well does an
    application work on different architectures? Performance and Cost
    Model Group (in WLCG) looking at this.
-   Hooks to understand where certain parts of an application start/end
    are useful. E.g., identify the start of the event loop.
    -   Would like to be able to profile (if needed) on the grid. Debug
        end to end performance, not just on development machine.
-   Is the idea of a warehouse useful? Could this be a service from CERN
    IT?
    -   It's useful. Needs to be a concrete proposal.
-   How do you want to analyse the data? This informs what we want to
    store. Maybe not so much need for long term archiving of the detailed data.
    -   Need a lot of metadata to link it back to the right code
        versionin git.
    -   Software in production becomes of historical interest; at least
        some summary data is important.
    -   The bleeding edge has a useful lifetime of only a few days/weeks
        during the development cycles. A lot of churn on HEAD and code
        often broken or unstable.
-   Some vision of how to come up with common formats, but needs some
    expert input to turn this into a DB schema that would scale.
-   Is it really worthwhile to compare *between* different tools - they measure
    different things (explains the zoo of the tools - they do
    different things).
    -   There have been some useful examples of cross profiling in ALICE.
    -   Also now much easier to analyse large profile dumps.
        -   Keep more 'raw' data and analyse on the fly.
-   Is it possible extract data from VTune? Probably not - proprietary.
-   Comparison between different developers' work could also be useful as
    a collaborative tool.
    -   e.g., ATLAS SPOT monitoring is just a 'red flag' style - something more generic would help and share efforts between
        experiments.
-   Progress by gathering people who could work on a prototype of the
    web based presentation. Concentrate on one or two profilers first.
-   Bootstrap guide for different tools would be useful.
    -   There is some training that people have developed and we should
        inventory that and point to it.
    -   Getting users started is a very good thing to contribute to.
-   Peter - as a developer got some very incomprehensible information
    back to try and understand a difficult problem. Developers are
    very busy and under a lot of pressure, not profiling experts.
    -   Need to optimise the efficiency of our coders - what we want to
        develop has to help that.
    -   CMS igprof experience was that providing a *service* to
        developers did help a lot.
        
Static Analysers
================
Presentation held back until the next meeting.
