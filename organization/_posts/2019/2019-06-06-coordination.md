---
title: "HSF Weekly Meeting #167, 6 June, 2019"
layout: meetings
---

# {{page.title}}

*Present/Contributors*: Graeme Stewart, Pere Mato, Witek Pokorski,
Daniel Elvira, Andrea Rizzi, Michel Jouvin, Martin Ritter, Paul Laycock,
Gloria Corti, Caterina Doglioni

*Apologies*: Agnieszka Dziurda

## News, general matters
  - LHCC this week, Graeme gave the software presentation update:
      - [<span class="underline">https://indico.cern.ch/event/754732/</span>](https://indico.cern.ch/event/754732/)
      - Thanks to everyone for comments and suggestions.
      - Feedback during the meeting:
        1.  Generators - emphasise to the generator developers that
            negative event weights have a huge adverse effect (are
            there ways to minimise this by tackling the phase space
            differently?)
              - A. Pass this message on via EG WG.
        2.  ML Simulation of calorimeters - will the work be portable
            to different detectors?
              - A. We understand this is the intention of the
                OpenLab/SFT efforts, but not yet there; for future
                R&D.
        3.  Accelerators - do people develop the code in portable
            ways, avoiding tuning to a particular GPU architecture?
              - A. This is an issue people are aware of - try to
                separate physics code from device code. R&D starting
                on abstraction layers to insulate us a bit more. (CMS
                showed some work with Kokkos and Alpaka that looked
                quite hopeful.)
      - Referees’ Recommendations (with emphasis for software issues):
        4.  2021 requirements should be firmed up, based on the latest
            understanding of the likely machine performance.
        5.  A timetable for Phase-2 computing model reviews should now
            be established.
        6.  Discussions with funding agencies should continue,
            regarding the provision of resources when future cost
            estimates are very uncertain.
        7.  The discussion around the use of HPC should continue.
            **How can we adapt to use HPC resources and/or have more
            influence over how they are setup**?
        8.  **Work on hardware acceleration (GPU, FPGA) holds the
            promise of a big leap in performance. This work should be
            encouraged and coordinated across experiments.**
  - Simulation on accelerators caught people’s eye for sure. We have to
    take this seriously and do R&D, but not allow inflated
    expectations. x100 speed-ups are not going to come and the costs
    of the re-coding will be enormous. We should  discuss
    this seriously because HSF can help to coordinate answers here.

## Google Summer of Code 2019
  - Coding period has started.

### Google Season of Docs
  - In proposal period.

## Activity and Working Group Updates

### Data Analysis
  - Nothing particular to report. Discussions ongoing in multiple
    threads on the google groups

### Detector Simulation
  - Topical meeting [<span class="underline">next
    week</span>](https://indico.cern.ch/event/816485/) on geometry.
      - DD4hep, Geometry optimisation in ATLAS, VecGeom.
  - There is a topic of CAD-\>GDML tool, but probably no time for it
    next week.
  - Foresee another geometry meeting after the summer, but with a
    different focus, e.g., visualisation of geometry.

### Reconstruction and Software Triggers
  - Yesterday’s topical meeting:
    [<span class="underline">https://indico.cern.ch/event/823263/</span>](https://indico.cern.ch/event/823263/)
  - Topic: Algorithmic approaches and data structures to efficiently
    exploit accelerators and many-core architectures
  - LHCb presented their experience: reached the milestone of 30MHz
    after SoA/SIMD event model changes.
  - Meeting very well attended \~50 people.
  - Presentations very well received - a lively discussion (meeting
    took 2h\!)
  - Request to follow up SoA/AoS with ATLAS/CMS
  - Live notes:
    [<span class="underline">https://docs.google.com/document/d/1IcvpsgOPpVfaBeZpSCcKD6i1y4HesA-VJopOYV4S\_7c/edit</span>](https://docs.google.com/document/d/1IcvpsgOPpVfaBeZpSCcKD6i1y4HesA-VJopOYV4S_7c/edit)
    (still needs to be filled and cleaned in some places)
  - To-do: need to add indico/lives notes to the website

### Software Tools
  - Organising meeting following up on potential meeting topics with
    speakers.

### Training
  - New training Indico category created at HSF top level:
      - [<span class="underline">https://indico.cern.ch/category/5816/</span>](https://indico.cern.ch/category/5816/).
  - Need to follow up on possible training events at CERN.

### Packaging
  - Meeting 29 May, minutes available:
      - [<span class="underline">https://hepsoftwarefoundation.org/organization/2019/05/29/packaging.html</span>](https://hepsoftwarefoundation.org/organization/2019/05/29/packaging.html)
  - Next meeting planned for 3 July.

### Frameworks
  - Reminder that call for nominations is open until tomorrow.
      - Mandate:
        [<span class="underline">https://hepsoftwarefoundation.org/workinggroups/frameworks.html</span>](https://hepsoftwarefoundation.org/workinggroups/frameworks.html)
  - So far 10 nominations received.
  - Some people who are HSF Coordinators, so we will establish a
    search committee again to propose from the nominees.

## Workshops

### Pre-CHEP (2-3 November)
  - Organising meeting happened this week:
    [<span class="underline">Document</span>](https://docs.google.com/document/d/1aEFJgpTpTtXtTpyf9QXRYAN8X4j--1yFiwNR3HRjtsU/edit#)
    created to track decision and progress.
  - Proposed title: *Analysis Systems: From Future Facilities to Final
    Plots*.
  - Main high-level items for the HSF and DOMA sides identified: we
    have a good list\!
      - Still have to group them into sessions: goal is to mix HSF and
        DOMA topics in each session so that the full audience is
        motivated to attend the whole event.
  - Drafting a description of the workshop for the next CHEP bulletin
    planned before the end of June.
      - Will also start to fill blocks in Indico and refine them as
        soon as we progress with session definitions.
      - Saturday will be 1-6pm, Sunday will be 9am - 1pm.

### Next HSF/WLCG Workshop
  - We are making a formal call now for interest in hosting this
    event. Parameters are:
      - Facilities for 1 whole week, in May or June 2020
          - Monday morning -\> Friday lunchtime
          - Known weeks to try to avoid so far: w/b 18 May (Ascension Holiday);
            w/b 1 June (LHCC); w/b 22 June (ATLAS Week)
      - 1 plenary room, capacity min 250
      - 2 additional parallel rooms, capacity min 100 each
      - Vidyo connection in these 3 rooms for the week
      - *Optional* breakout rooms \~3x30 people would be nice (vidyo
        there optional)
      - Low costs favoured (€200 ideal, €300 acceptable)
      - Lunch options to be specified - on site and included in
        registration favoured
      - One reception event on Monday, costs included; one dinner,
        could be billed separately if necessary
      - Some indications of typical local accommodation costs and
        travel options
      - A European location is favoured this time
  - Please express interest by 12 July to
    [<span class="underline">hsf-coordination@googlegroups.com</span>](mailto:hsf-coordination@googlegroups.com).
  - We will need a small organising team for HSF.

## AOB
  - ECFA special session at EPS-HEP on “Toward the Update of the
    European Particle Physics Strategy” (13 July).
      - Graeme invited to give the talk on Computing and Software
        challenges.
  - AIDA++ follow up call for expressions of interest has been made.
    There is a f2f meeting at CERN on 17-18 June:
      - [<span class="underline">https://indico.cern.ch/event/822748/</span>](https://indico.cern.ch/event/822748/).
      - Contact Witek, Frank and Graeme to make an EoI (due beginning
        of July) and plan to attend that meeting if possible as it
        will help to build a consistent program.
      - Note, you can attend the meeting even if you do not have an EoI
        to present. General input from the community is important to
        define the right programme.
  - Having coordination meetings every two weeks seems to be a good
    rhythm at the moment.
      - Should we formalise this and adjust the meeting planning from
        now on?
      - It frees this slot for any WG that wants it.
      - We can always have an additional “odd” coordination meeting
        again as needed.
      - Agreed that we try this cadence for now.
      - -> Next meeting 20 June.
