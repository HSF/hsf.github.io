---
title: "HSF Weekly Meeting #185, 23 April, 2020"
layout: meetings
---

# {{page.title}}

Present/Contributors: Graeme Stewart, Caterina Doglioni, Attila Krasznahorkay, Josh McFayden, Efe Yazgan, Witek Pokorski, Stefan Roiser, Paul Laycock, Kyle Knoepfel, Agnieszka Dziurda, Eduardo Rodrigues, Michel Jouvin, Serhan Mete, Mason Proffitt, Pere Mato, Philippe Canal, Teng Jian Khoo, Chris Jones, Gloria Corti, Guilherme Amadio, Liz Sexton-Kennedy, Daniel Elvira, Andrei Gheata

Apologies: Ben Morgan (SuperNEMO software tutorial)

## News, general matters

[Snowmass process](https://snowmass21.org), is there scope for a short HSF submission? (e.g. similar to the [paper](https://zenodo.org/record/2413005) we sent to EPPSU)

CD's opinion (1st time snowmass-er, others may have further experience): LoI + paper combination welcome (there is a Computational Frontier). Instructions in links here: <https://snowmass21.org/loi>.
Paper encourages projects to develop further within the framework with "help" of a forum (at least that's how things are working in Energy Frontier). 

- Could do more than an LoI as we have made progress (LHCC docs)
- What length? Exec summary, that then makes references to longer document(s)
- Should continue discussion in the coordination group, inviting Oli (who is a Computational Frontier convenor)

## Google Summer of Code 2020

GSoC Advisory Committee this year is Liz, Pere and Michel.

This year we have ~200 student proposals for 47 project ideas, 37 qualifying (valid student proposals that comply with the program rules). We asked for 36-37 slots and **received 36** (last year we had 33). The successful proposals will be announced on May 4, coding starts June 1st.
* Currently, we are in a phase where students confirm their participation to a selected project: always the risk of "loosing" a few students who applied to several selected projects (not the case inside HSF but no way to prevent/know in advance if they did in the project of another organization) who may have confirmed before us (but we were quick!)

## Google Season of Docs 2020

The Season of Docs program is about bringing open source and technical writer communities together, to the benefit of both.
HSF participates as umbrella organisation this year, there is an active [call for project proposals](https://hepsoftwarefoundation.org/activities/gsdocs.html#for-hsf-projects-and-mentors) expiring on May 1st! We can get up to 4 slots this year - we distributed the call via several HSF channels, asking people to re-distribute in their groups, but got only one proposal so far.

The program is more adapted for projects having documentation systems with a certain maturity, for improving them. Suggestions for technical writer proposals can include:
 * Building a documentation site (Read the Docs, static site generator, GitHub Pages, ...) and publishing an initial set of documents
 * Refactor the open source project's existing documentation to provide an improved user experience or a more accessible information architecture
 * Write a conceptual overview of, or introduction to, a product or feature
 * Create a tutorial for a high-profile use case
 * Create a set of focused how-to guides for specific task
 * Create a contributor’s guide

Projects can be standard (3 months) or long running (6 months) starting mid-September. The organization application deadline is however May 4, when Google expects us to have already a good idea (with proposals) of the projects we support.

## Alpaka Training

Event initially foreseen for 27 April had to be postponed. The new dates and a tentative agenda for the training are:

**Mon 29 June - Fri 3 July 2020, 9:00 - 10:30 CEST <https://indico.cern.ch/e/alpaka-tutorial>**

Planning for a virtual meeting with short presentations and breakout training sessions every day. Registrants of the previous event will be contacted and can be moved automatically to the new event. 

NB: No decision yet on how/when to organise the Alpaka hackathon.

## LHCC Review of HL-LHC Software and Computing

*Reminder*: LHCC will review software and computing plans for the HL-LHC, Amber Boehnlein (JLab) will chair. Five 20 page documents provided as input to the committee, from ATLAS, CMS, WLCG, DOMA and from *Common Tools and Community Software* (the HSF takes care of the later)

There will be a relatively short virtual meeting in the week of 18 May, with follow-up reviews later.

[Current HSF Document](https://docs.google.com/document/d/1ai7m7kFyiGgl2tKralJKyPX6rlD9tffU7B6wPj_vpZU/edit?usp=sharing). We had the open review and discussion [last week](https://indico.cern.ch/event/904412/), with additional points gathered in [this Google Doc](https://docs.google.com/document/d/1tnUjW7abhxZyP5lozbIT2GDCztmoU9UzlOtlk4HIFBg/edit?usp=sharing)

### Timeline

- Conclude the Google Docs phase today (Thursday 23)
- Move to LaTeX tomorrow (Friday 24)
    - Graeme will announce when that is done
    - Move into Overleaf first
    - Then, next week, migrate to the HSF docs repository
- BibTeX references at this point
- Final week to make any last changes and address points of coherence

**Current list of open points for each section:**

### General

- We are a bit long, currently:
    - Intro 2
    - Generators 5
    - Simulation 7
    - Reconstruction 6
    - Analysis 6
    - Conclusions 2
    - **Total 29**
- LaTeX should allow a squeeze (technical "solution"), but we should look out for opportunities to be more concise

### Introduction

- Reminder that we align expected hardware gains with WLCG/ATLAS/CMS
    - This was checked and is estimated at ~10% per year as the common figure to be used (the experiments also give a 20% per annum figure, but that seems over-optimistic)

### Event Generators

- Good shape, final few comments to look at, but nothing controversial

### Detector Simulation

- Some (minimal) discussion on conclusions wording needed
- References will be fixed on Overleaf
    - We need to find a few references (for the moment just mentioned, but no details written down)

### Reconstruction and Software Triggers

- DL: There are some overlapping ideas to consider consolidate with respect to the facilities document to LHCC (perhaps more general than the reco/trigger section). 
- One idea we didn't capture so well is the need to support HPC architectures. This comes out in both validation and non-x86 support. Will add a few sentences today.
 
### Data Analysis

- Improved the coherence of the document since last  week, we added several important points for ~the same word count but could maybe be more concise.  Some references need to be found/fixed.
- We could still be a little more forthright in the R&D needs section and point out what we think useful directions are. For example, pointing out how beneficial it has been to open up to new ways of thinking (DataFrames et al), this healthy competition philosophy should continue.

### ~~Conclusions~~ Summary

- *Summary* is a more appropriate way to finish the document
- Bullet points per section (aiming for 4-5 seems about right)
    - 24 month timescale (stated as 'a few years')
    - Should be realistic, but ambitious
- Final conclusion points
    - We need investment in software
    - Adaption to accelerators (particularly GPUs) is a common theme
    - Stakeholder input is key
    - HSF has a coordination role
    - Mention IRIS-HEP, SIDIS, other existing projects?
        - Could at minimum have a link to last year's JLab workshop session / European Strategy submission 
        - Prefer to mention things we know are funded
    - Mention links with ESCAPE? (currently mentioned in trigger&reco chapter)
        - As long as relevant to the HL-LHC focus

---

## Working Group Updates

### Data Analysis

Nothing to report, occupied with the LHCC report.

### Detector Simulation

For the last couple of weeks focussed on the LHCC report. Need to organize the next topical meeting asap avoiding conflicts with May workshop.

### Reconstruction and Software Triggers

#### Meetings

No meeting in May due to workshop, but some (incl. categories) potentially lined up after interactions for LHCC doc: 

- Accelerators in trigger & reconstruction (Allen/Patatrack updates since CHEP + contribution from ATLAS, topics can be chosen following HSF workshop contributions)
- [category of meetings] How experiments sharing pieces of LHC experiments can reuse LHC trigger & reco code. Cases in mind: FASER, LDMX (but maybe more, e.g. future colliders?)
- CBM experiment and 4D (time-slice) tracking reconstruction
- FASTML (HSF4ML & SONIC) for ML on accelerators
- (from earlier) Particle flow review

Would it be worth categorizing meetings according to priorities in the LHCC document? May benefit HSF PR...

*Using the LHCC document to plan the next activities for the working groups is strongly supported.*

#### Other

We have a request from someone who wanted to work in the trigger & reco area (see previous meetings). 

Idea could be to have him help with ESCAPE dark matter test case (= show an end-to-end physics analysis) and liaise with HSF WGs (especially frameworks and data analysis) on what is being done right now and what can be done in the future. Other ideas/objections? 

### PyHEP

Nothing to report.

### Software Tools and Packaging

Presentation on Spack during pre-GDB Software Development meeting on 5 May 2020 ([agenda](https://indico.cern.ch/event/813800/)):
- 10'+5' talk to be given by Ben Morgan as the expert,
- Focus on practicalities of Spack (building/installing software).

No firm release date on Spack 0.15. Having said that, it'll be a major release (will probably include new concretiser and an official binary repository).

### Event generators

We have mostly been working on the draft of our longer document (that supplements what's in the LHCC one). This has been *a lot* of work, but is now quite close to converging (after being circulated to the WG for comments).

### Frameworks

Will try to hold one more meeting (next week) before the "virtual workshop", continuing the multi-threaded scheduling discussions.

Details to be circulated soon...

---

## Workshops

### New Architectures, Portability, and Sustainability

[HSF WLCG Virtual Workshop on New Architectures, Portability, and Sustainability](https://indico.cern.ch/event/908146/)
* Tentative timetable added
* Speakers to be added soon

Workshop preparation progressing, finalising the timetable.
* ALLEN probably moved from Monday to Tuesday, to be confirmed

**We ask that people [register](https://indico.cern.ch/event/908146/registrations/)** so that we can gauge the level of interest and best organisation options.

Prepared a [virtual meeting guide](https://indico.cern.ch/event/908146/page/20187-virtual-meeting-guide) to try to make the event work as well as possible, *more suggestions and feedback very welcome here* (we are treading new ground).

### PyHEP 2020 Workshop

[Virtual Workshop Planned](https://indico.cern.ch/e/pyhep2020)

## AOB

### Next Meeting

- Next regular meeting slot is 7 May
