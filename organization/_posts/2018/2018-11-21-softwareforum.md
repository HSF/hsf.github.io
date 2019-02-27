---
title: "HSF Software Forum on EIC Software Consortium, November 21, 2018"
layout: meetings
---

# {{page.title}}

[Meeting Agenda and Slides](https://indico.cern.ch/event/746526/)

Introduction
============
-   Reminder about the [*HSF/OSG/WLCG
    Workshop*](https://indico.cern.ch/event/759388/), 18-22 March 2019
    at JLab
    -   We hope to open registration soon - before Christmas
-   [*Physics Event Generator
    workshop*](https://indico.cern.ch/event/751693/) is next week at
    CERN

EIC Software Consortium
=======================
-   All current frameworks are more or less based on ROOT.
-   Are the detector concepts designed to read out cleanly,
    event-by-event? A lot of Nuclear Physics experiments have slow detectors that
    read-out many BCs in a single “chunk” (ALICE, FAIR Experiments).
    -   No pile-up at EIC - physics happens every 5th bunch crossing.
    -   DAQ chain and possibilities for real-time processing will drive
        the detector design (e.g., favour silicon over TPCs).
    -   EIC concept is much more integrated design between the
        accelerator, detector and the software stack.
-   Protobuf - nice and fast, lightweight; is it sufficiently flexible?
    -   Would like to avoid ROOT IO as we think this would be limiting
        in what we can achieve, limited by computing infrastructure
        and the need to "fit in". How can we make things easier for
        the user? Think about new ways to do things. Protobuf buys
        language agnosticism, and that's very useful also for
        transferable skills.
    -   Flexible and modular approach - interoperability is very
        important (C++ to Go).
    -   It’s also good for streaming readouts.
    -   Sebastien - how many people are trying out these different
        languages and backends?
        -   This will be an outcome of working in the user group as
            people get started.
        -   Current packages (EicRoot, Fun4All, GEMC) are actually very
            successful. ANL software is the most modular. Here C++
            dominates as it is what's been used historically.

AOB/Discussion
==============
-   Next meeting is 5 December - Spark based analysis in HEP (ROOT) and
    LSST
    -   [*https://indico.cern.ch/event/754811/*](https://indico.cern.ch/event/754811/)
