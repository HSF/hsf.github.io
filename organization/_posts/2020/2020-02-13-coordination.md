---
title: "HSF Weekly Meeting #180, 13 February, 2020"
layout: meetings
---

# {{page.title}}

Present/Contributors: Graeme Stewart, Agnieszka Dziurda, Ben Krikler, David Lange, Andrea Rizzi, Maria Girone, Liz Sexton-Kennedy, Efe Yazgan, Stefan Roiser, Andrea Valassi, Witek Pokorski, Kyle Knoepfel, Caterina Doglioni, Teng Jian Khoo, Ben Morgan, Philippe Canal, Mark Neubauer, 

Apologies: Pete Mato, Gloria Corti

## News, general matters

- Reminder: ESCAPE Software Catalogue, <https://projectescape.eu/escape-catalogue>,
    is gathering requirements
    - *What would the HSF want from this?*
        - Concentrate mainly on reusable software
            - i.e. not experiments or institutes
        - Sustainability important
            - Should not be "one-shot" then never updates
            - Metadata tied to code base of projects?
        - Documentation of workflows
            - Virtual environment for Dark Matter, for end-2-end studies
            - Caterina and Lukas looking into using Recast, PyHF and ReAna incorporated
            - Workflows for generators
        - Any further ideas or inputs?
        - Got some general thoughts from Dan Katz that software catalogues take too much work for too little real value (!)
        - `libraries.io` worth looking at, monitors many open source repositories

- IRIS-HEP Steering Board, 18 February
    - HSF were asked for feedback for IRIS-HEP
    - Please send any comments you have to Graeme

## Google Summer of Code 2020

Now live on the HSF website: *29 Organisations*, *22 Projects*, *45 proposals*

Students will now start to get in touch, next deadline March 20, your evaluation
of students *based on your interactions and a test*


## LHCC Review of HL-LHC Software and Computing

*Reminder*: LHCC will review software and computing plans for the HL-LHC, Amber Boehnlein (JLab) will chair, first phase will be 18-20 May 2020. Five 20 page documents provided as input to the committee, from ATLAS, CMS, WLCG, DOMA and from *Common Tools and Community Software* (the HSF takes care of the later)

Document [outline](https://docs.google.com/document/d/1ai7m7kFyiGgl2tKralJKyPX6rlD9tffU7B6wPj_vpZU/edit?usp=sharing) has been created.

Our timeline:
* February - first drafts
* March - incorporate feedback
* April - consolidation and concensus
* 1 May - document ready for LHCC

Outline - cross cutting topics like accelerators and machine learning; how could we best incorporate these? Do it area by area or have a general sub-section?

- Met with Ian and Simone and we decided that we should touch on these in the HSF document and then some light consolidation between documents is foreseen in April

Not a lot of progress so far, though some groups did start to think about things. How to progress significantly in the next 2 weeks?

Maria - DOMA are preparing a document and their WGs are gathering inputs in parallel

ATLAS and CMS documents will be public only after the review

## Working Group Updates

### Data Analysis

* Based on doodle, we established a date for a meeting between HSF DAWG and DOMA-Access, which will be Tue, 17 March at 14.00
* Will start planning for the analysis languages workshop, beginning to narrow down dates.

### Detector Simulation

* Planning LHCC inputs
* Plan forming for the Lund workshop - quite a lot, 4 sessions (see below)
    * 2 sessions for R&D on GPUs, very open for people to discuss "crazy" ideas

### Reconstruction and Software Triggers

* We had a meeting yesterday (at the end it was joint with IRIS-HEP) about HL-LHC Tracking challenges:
  * indico: <https://indico.cern.ch/event/882106/>
  * minutes: in preparation 
  * about 25 participants in Vidyo + 25 people at CERN 

* We plan to follow up with other experiments (we had a last minute cancellation)
* Positive outcome of the meeting: we do not need to sacrifice performance when speeding up reconstruction i.e., possible gain in both CPU and physics 
* Convenors meeting early next week to target LHCC report 

### Software Tools and Packaging
* Next meeting announced for 26th February, 15:00 CERN time:
    * <https://indico.cern.ch/event/888898/>
    * Contact Serhan, Ben and Martin if you want to present something
    * Will discuss topics for Lund (roughly Packaging, Tools for Accelerators, IDEs)

### PyHEP
* Preparation for PyHEP2020 well underway, colocated with Scipy, 11-13th July
    * <https://indico.cern.ch/e/PyHEP2020>
* Poster to go out next Monday
* Sponsorship being finalised
* One topical meeting pre-Lund


### Training

- Software Carpentry in March (Carpentries just confirmed tutors)
- Discussions on more advanced training are happening
    - [Alpaka general day](https://indico.cern.ch/event/858758/), 27 April
    - [Openlab oneAPI training](https://indico.cern.ch/event/878418/), 24-26 March
    - Hope to have some opportunities for training with Nvidia, boot camp style

### Event generators

- Working on a first draft/skeleton of the contribution to the HL-LHC document for the LHCC review. Should be able to have a first version for discussion between conveners by the end of this week, then forward for WG comments/feedback next week
- Following up on the GPU port of MadGraph, some of us had a vidyo discussion yesterday about architectural approach (event-level data parallelism, basically), software technicalities and workplan for GSOC student
- Also continuing the follow up of ATLAS/CMS accounting, so that we can present more refined numbers in Lund and in the HL-LHC document

### Frameworks

We are done with our experiment framework surveys; we will now focus on specific topics for our next meetings. We are trying to determine what those topics are based on the experiment survey talks.

The frameworks working group has been asked to participate in the Software & Computing Round Table at Jefferson Lab on March 10 on the topic of "Frameworks for Greenfield Experiments".  The topic is motivated by software and computing discussions for the upcoming electron ion collider.

- Might also be good to discuss the Key4hep project at that time

## Workshops

### HSF/WLCG 2020 workshop

#### Logistics

Workshop registration is opening as we speak...

<https://indico.cern.ch/event/867789/>

The workshop fee will be:

2800 SEK (approx. 260 EUR) if paid before April 1st,
3200 SEK (approx. 300 EUR) If paid after April 1st and before April 20th.

The conference dinner, prepared with local ingredients and hosted at the Lund Grand Hotel, can also be paid from the payment page (approx. 50 EUR).

There is a [poster](https://indico.cern.ch/event/867789/attachments/1984157/3309134/Poster_HSFWLCG.pdf) on the website - please print and pin up!

#### Scientific Programme

Organising team for HSF are: Graeme, Heather, David and Michel

We adjusted the timetable proposal a little:

| Day | Room 1 | Room 2 | Room 3 |
| -------- | :--------: | :--------: | :--------: |
| **Monday** |  |  | |
| AM     |   [Free for workshops and BoFs]   |      |
| PM Part 1    | HSF+WLCG Plenary|    | 
| PM Part 2    | HSF+WLCG Plenary|    | 
| **Tuesday** | | | |
| AM Part 1     |   New arch/portability/sustainability    |      ||
| AM Part 2     |   New arch/portability/sustainability    |      ||
| PM Part 1    | New arch/portability/sustainability |    | 
| PM Part 2    | New arch/portability/sustainability|    | 
| **Wednesday** | | | |
| AM Part 1     |   HSF Common Session    |  | WLCG infrastructure and services    |
| AM Part 2     |   HSF Common Session    |  | WLCG infrastructure and services    |
| PM Part 1    | HSF Trigger&Reco - General |  | WLCG infrastructure and services  | 
| PM Part 2    | HSF Sim - Fast Sim | HSF Training | WLCG infrastructure and services  |
| **Thursday** | | | |
| AM Part 1   |   HSF Sim - Geant Modernisation |  HSF Tools & Packaging    | DOMA Plenary|
| AM Part 2   |   HSF Trigger&Reco - General    | HSF Generators Overview  | DOMA Plenary|
| PM Part 1    | HSF Sim - R&D |  HSF Generators R&D  | DOMA Plenary |
| PM Part 2    | HSF Sim - R&D |  HSF Frameworks  | DOMA Plenary |
| **Friday** | | | |
| AM     |   Wrap-up joint plenary   |     ||

Two HSF sessions at the same time became inevitable, but can be reorganised a bit if there is a more optimal distribution of what we run in parallel

Topics for plenary sessions:

- Monday PM
    - Introduction and welcome from Lund
    - HSF Overview
    - WLCG Overview
    - Other Communities
        - Nuclear (FAIR), Astroparticle/SKA, Dark Matter
    - Machine Learning (common challenges and opportunties, TBD)
    - CVMFS, Containers and future software distrubution

- Tuesday 
    - Please send any suggestions as this is rather a cross-cuttting topic
    - Review, in particular, workloads that might be suitable for HPCs with non-x86 architectures (GPUs, ARM, Power9...)

- Friday AM
    - Session on newly funded projects
        - ESCAPE
        - DOE HEP-CCE
        - IRIS-UK / ExCALIBER
    - Vision and Outlook talk or Review talk
        - Ideas welcome here

#### BoFs and Other Events

- Software Deployment BoF
- Training Hackathon (TBC)
- WLCG AuthN/Z Hackathon
- LHCOPN and LHCONE Meeting

### PyHEP 2020 workshop

- See WG report above!

## AOB

### Next Meeting

- Next regular meeeting slot is 27 February
