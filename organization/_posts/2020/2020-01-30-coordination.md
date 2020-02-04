---
title: "HSF Weekly Meeting #179, 30 January, 2019"
layout: meetings
---

# {{page.title}}

Present/Contributors: Graeme Stewart, Witek Pokorski, Caterina Doglioni, David Lange, Efe Yazgan, Mason Proffitt, Andrea Valassi, Philippe Canal, Stefan Roiser, Kyle Knoepfel, Eduardo Rodrigues, Ben Morgan, Teng Jian Khoo, Andrea Rizzi, Danilo Piparo, Liz Sexton-Kennedy, Gloria Corti, Attila Krasznahorkay

Apologies: Agnieszka Dziurda, Pere Mato, Serhan Mete

## News, general matters

- Letters of Collaboration and Support
    - Signed off on 3 of these at the beginning of the week
    - *Please try to make such requests in a timely fashion - ideally 2 weeks before any deadlines*

- ESCAPE Software Catalogue, <https://projectescape.eu/escape-catalogue>
    - Caterina and Graeme met with Kay Graf from the ESCAPE project
    - They have a deliverable to provide a "software catalogue" for the project
        - "ESCAPE services will be part of the global EOSC (European Open Science Cloud) catalogue of scientific software, to ensure global open access and long-term usability."
    - This would be a good opportunity to have a more central place where software projects could be publicised
    - *What would the HSF want from this?*
        - Concentrate mainly on reusable software
            - i.e. not experiments or institutes
        - Sustainability important
            - Should not be "one-shot" then never updates
            - Metadata tied to code base of projects (we think there has been some work done here, could ask people like Dan Katz)
        - Documentation of workflows
            - Virtual environment for Dark Matter, for end-2-end studies
            - Caterina and Lukas looking into using Recast, PyHF and ReAna incorporated
        - Other considerations...?
        - Try to give *inputs in next two weeks* if you can

## Google Summer of Code 2020

*Reminder*: the deadline for submitting proposals is **Feb 4**!


## LHCC Review of HL-LHC Software and Computing

*Reminder*: LHCC will review software and computing plans for the HL-LHC, Amber Boehnlein (JLab) will chair, first phase will be 18-20 May 2020. Five 20 page documents provided as input to the committee, from ATLAS, CMS, WLCG, DOMA and from *Common Tools and Community Software* (the HSF takes care of the later)

Document [outline](https://docs.google.com/document/d/1ai7m7kFyiGgl2tKralJKyPX6rlD9tffU7B6wPj_vpZU/edit?usp=sharing) has been created.

- Introduction
    - Should certainly cover important pieces of infrastructure software, such as CVMFS
- Physics Event Generation
    - Not yet planned in great detail, will certainly update from CWP
- Detector Simulation
    - Convenors meet today, so will discuss this then
    - Accelerators are going to be important, lacking a clear direction for now
- Reconstruction and Software Triggers
    - Will work on LHC review document starting next week, initial (incomplete) list of "common software" topics to mention:
       * ACTS
       * Allen
       * Patatrack
    - Is it an option to connect this (& other WG software) to the Software Catalogue (they all have git repos and we could nudge them in the direction of providing documentation/test case)?
        - Yes (albeit this is not connected to the review)
- Data Analysis
    - Want to fold in feedback from meetings planned in the next few weeks/months and with the pre-CHEP workshop (analysis facilties, analysis language)
    - Iterative process envisaged
        - Meeting supportive of this approach
- Conclusions

Outline - cross cutting topics like accelerators and machine learning; how could we best incorporate these? Do it area by area or have a general sub-section?

We shall iterate with Amber as well that should help clarify.

## Working Group Updates

### Data Analysis
- We had planning meeting last week to organize two events:
    - analysis language workshop (couple of days)
    - analysis facilities/infrastructures meeting with DOMA
- During the various discussions a question was raised about the right forum to discuss Machine Learning frameworks for usage for sim/reco/analysis. It involves multiple groups (reco, sim, gen, ana, pyhep, fwk).
    - consider for Lund? or later in wider software meeting?


### Detector Simulation
- Convenors meet together this week

### Reconstruction and Software Triggers

Next meeting: Feb 12th, on tracking for HL-LHC upgrade. <https://indico.cern.ch/event/882106/>

Waiting to converge on follow-up of LHCb CPU meeting (March 18th), ATLAS speaker available but CMS speaker/input still missing.

Sentences about the Lund workshop:

- One session on tracking and triggering for long-lived particles and unusual signatures, focusing on what we are missing (brief overviews of what is done will be possible, but we want to focus on what we may be missing)
- Some space for contributed talks on trigger and reconstruction
- Are Frameworks/Analysis interest in a common session on tracking on CPU/GPU [FPGA?] + sufficient time for discussion 

### Software Tools and Packaging
- Startup meeting between convenors last week
    - Will send round email on restarting meetings (provisionally 26th February due to many upcoming experiment weeks)
    - Identified a few topics from last year to follow up on (Buildsystem good practice, contacts with openLab/Intel/Nvidia)
    - Discussed ideas for session at Lund workshop. 3 main topics of Packaging, Tools for profiling code especially on accelerators, use of IDEs for integrating these
    - Will ask via mailing lists for other ideas/discussion topics

### PyHEP
- PyHEP 2020 workshop in Austin:
    - Venue is now settled.
    - Looking at costs and sponsorships.
    - First announcement to go out very soon.
- We would like to organise a topical meeting together with the Data Analysis WG on fitting and statistical tools, cf. ATLAS publishing full likelihoods for the first time. Timely to take a look at likelihood preservation and the tools needed (see suggestion in roundtable section of Live Notes of DA meeting <https://indico.cern.ch/event/880410/>).

### Event generators

- Very intense and useful meeting last week.
    - Andrea: will upload the minutes soon, sorry for not doing that yet.

### Frameworks

- Yesterday, we completed the survey of experiment frameworks with presentations from the GlueX experiment at Jefferson Laboratory and the _art_ framework.
- Will now pursue topic-based meetings instead of general overviews of framework efforts.

## Workshops

### HSF/WLCG 2020 workshop

#### Logistics

The workshop will start Monday after lunch and end Friday at lunchtime.

We hope to open registration rather soon now... start of February

<https://indico.cern.ch/event/867789/>

There will be a poster...

#### Scientific Programme

Organising team for HSF are: Graeme, Heather, David and Michel

After organisers meeting this Tuesday, the timetable proposal is converging:

<https://docs.google.com/spreadsheets/d/15CtFTyINW96yZnyvx4jxSGPnaRpBqVQnLW_8lpUwvqY/edit?usp=sharing>

{:.table .table-condensed .table-striped}
| Day | Room 1 | Room 2 | Room 3 |
| -------- | :--------: | :--------: | :--------: |
| **Monday** |  |  | |
| AM     |   [Free for parallel sessions]   |      |
| PM Part 1    | HSF+WLCG Plenary|    | 
| PM Part 2    | HSF+WLCG Plenary|    | 
| **Tuesday** | | | |
| AM Part 1     |   New arch/portability/sustainability    |      ||
| AM Part 2     |   New arch/portability/sustainability    |      ||
| PM Part 1    | New arch/portability/sustainability |    | 
| PM Part 2    | New arch/portability/sustainability|    | 
| **Wednesday** | | | |
| AM Part 1     |   HSF Plenary    |  WLCG infrastructure and services    ||
| AM Part 2     |   HSF Plenary    |  WLCG infrastructure and services    ||
| PM Part 1    | Simulation |  WLCG infrastructure and services  | 
| PM Part 2    | Trigger&Reco |  WLCG infrastructure and services  | 
| **Thursday** | | | |
| AM Part 1   |   Simulation    |  Tools     | DOMA Plenary|
| AM Part 2   |   Reconstruction    | Training    | DOMA Plenary|
| PM Part 1    | Simulation |  Frameworks  | DOMA Plenary |
| PM Part 2    | Simulation |  Generators  | DOMA Plenary |
| **Friday** | | | |
| AM     |   Wrap-up joint plenary   |     ||

    
- Whole day shared session on new architectures (I assume also meaning computing resource centres, like HPCs), heterogeneous computing and portability was a popular choice
- One session slot for frameworks? (Could cover more technical topics than get touched on for plenary new arch)
- HSF "Plenary" is 2 sessions for now, do we need them both?
    - Something on machine learning integration in general, see Analysis discussion above
- Generators might want a second, discussion session - how to squeeze this in?

Can WGs with confirmed sessions send a sentence or two about the topics to be covered, that can be put into the Indico session blocks?

### PyHEP 2020 workshop

See above...

## AOB

### Next Meeting

- Next regular meeeting slot is 13 February
