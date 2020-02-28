---
title: "HSF Weekly Meeting #181, 27 February, 2020"
layout: meetings
---

# {{page.title}}

Present/Contributors: Graeme Stewart, Andrea Valassi, Teng Jian Khoo, Pere Mato, Eduardo Rodrigues, Ben Morgan, Paul Laycock, Agnieszka Dziurda, Michel Jouvin, Stefan Roiser, Efe Yazgan, Liz Sexton-Kennedy, Chris Jones, Caterina Doglioni, Horst Severini, Martin Ritter, Sam Meehan, Michel Jouvin, Daniel Elvira

Apologies: Josh McFayden, Serhan Mete, Andrea Rizzi

## News, general matters

- ESCAPE Software Catalogue
    - HSF thoughts and inputs were passed to Kay Graf in [this Google Doc](https://docs.google.com/document/d/1mEY-jlPWa0cJT7Lkf54YfWA1YUUrpmJ1DBxpq2EK0PU/edit?usp=sharing)

- IRIS-HEP Steering Board, 18 February
    - Thanks to those who gave input, see [slides](https://indico.cern.ch/event/809181/contributions/3730802/subcontributions/299751/attachments/1989773/3316889/HSF_Feedback_for_IRIS-HEP.pdf) attached to Indico

- UK Efficient Computing in HEP meeting last week
    - Graeme gave an [HSF talk](https://indico.ph.ed.ac.uk/event/66/contributions/819/attachments/675/817/ECHEP_HSF_Talk.pdf)
    - Good progress on ideas for the UK HEP community to submit to STFC (the "Statement of Interest" or SoI)

## Google Summer of Code 2020

- Some last minute projects have been adopted by us as an umbrella organisation
- Meeting for all mentors Friday 28 February, 16h: <https://indico.cern.ch/event/891915/>
- Currently *Student Interaction Period*, until 16 March

## LHCC Review of HL-LHC Software and Computing

*Reminder*: LHCC will review software and computing plans for the HL-LHC, Amber Boehnlein (JLab) will chair, first phase will be 18-20 May 2020. Five 20 page documents provided as input to the committee, from ATLAS, CMS, WLCG, DOMA and from *Common Tools and Community Software* (the HSF takes care of the later)

Document [outline](https://docs.google.com/document/d/1ai7m7kFyiGgl2tKralJKyPX6rlD9tffU7B6wPj_vpZU/edit?usp=sharing) has been created.

We are a bit late with drafts, but they are in preparation now (see each WG below).

#### Introduction

- Text is going in to the introduction now, covering a general overview and some words on specific challenges and important topics
    - Technology Evolution
    - Accelerators
    - Software Distribution (CVMFS)
    - Software Preservation
    - Language evolution changes?

#### HSF Feedback Sessions

- Suggestion that we organise one longer meeting around beginning of April, but also decide in advance what topics need discussion time (e.g., based off Google Doc comments)

#### Discussion with CMS and ATLAS

- CMS invited us (Graeme) to report on the document and discuss with them at their next S&C week (24-27 March)
- Graeme contacted ATLAS with a view to having a similar discussion in early April


## Working Group Updates

### Data Analysis
* Draft zero of the LHCC document section on analysis being prepared 
    * Analysis computing requirements as distinct from sim/reco (but consider commonalities?)
    * Limitations on analysis code as motivation for R&D
    * Current developments and status of analysis models
    * Two main R&D projects i.e. Analysis Description Languages and Analysis Facilities
    * Offer from Eduardo to discuss PyHEP input on any overlapping topics in analysis (Python analysis tools are an obvious example)

* [Joint meeting with DOMA on March 17th](https://indico.cern.ch/event/890991/), announcement to be made in the proper lists

### Detector Simulation

- Concentrate on points that already existed in the CWP where we have made progress or their is particular interest
    - And not for areas with less interest (digi)
- Geant4 modernisation and acceleration is going to be vital
    - What did we learn from GeantV?
    - Physics improvements are difficult to quantify or predict
    - We believe that fast simulation will be critical

### Reconstruction and Software Triggers

- Added input to LHCC document
    - Also soliciting input from specific projects
- Added ideas for sessions of Lund workshop, should we start with invitations?
    - A. *Yes!*
- Next meeting: March 18th, CPU software improvements in ATLAS and CMS (CMS TBC)

### Software Tools and Packaging
- [Meeting on the 26 February](https://indico.cern.ch/event/888898/)
    - Move to responsive meetings as updates/topics to discuss arise. May have hands-on tutorials/demos as well if there's interest.
    - Short/Long term goals for Packaging discussed
    - Outline of session at HSF-WLCG meeting at Lund presented, emails for further discussion will be sent out over next week. Commonalities/Overlaps with Software Deployment BoF (packaging) and general Accelerator sessions (tools for profiling, etc).
    - Update from Patrick Gartung on Spack binary packaging. Good progress, and links with University of Oregon and [E4S project](https://e4s-project.github.io).

### PyHEP
- [PyHEP 2020 workshop](https://indico.cern.ch/e/PyHEP2020):
    - First announcement email sent out on Tuesday to the HSF forum. Please, please, broadcast to relevant mailing lists (your favourite experiment, institute, project, etc.).
    - Sponsorship finalised apart from waiting for news from the Python Software Foundation - thank you to them as we can do a no-registration-fee workshop!
    - Encourage [SciPy2020](https://www.scipy2020.scipy.org/) participation - students could look for sponsorship opprtunities
        - There is a slightly reduced rate for academics and significantly for students

### Training
 - Preservation Bootcamp last week, <https://indico.cern.ch/event/854880/>
     - Successful --> Plan next one in ~June
 - Software Carpentry is go for next month, <https://indico.cern.ch/event/882660/>
     - Registration opens Friday 28 at 10h
     - Announcements should have been made quite widely within each experiment (but please forward!)
 - IRIS-HEP had a training blueprint meeting (summary is being circulated)
     - <https://docs.google.com/document/d/1uUGOJPp0kH0kTofe5GocfRNhbxm1oPxR9KTSbzvuoIQ/edit>
 - Discussion about developing material on the hsf-training repo
     - <https://github.com/hsf-training>
     - Planning to gather hsftraining-XYZ modules here
     - Example : https://awesome-workshop.github.io/reproducible-analyses/index.html
     - Should make sure that PyHEP training material is also incorporated (Eduardo sent an email)
 - Advanced Training
     - openlab [oneAPI training](https://indico.cern.ch/event/878418/) next month
     - Hope to organise CUDA bootcamp with Nvidia at CERN before the summer (TBC)

### Event generators

- LHCC document:
  - A first draft of a note 'for the LHCC review' has been completed by the three conveners and has been circulated to a few experts in the WG for comments. Then we will circulate it more widely for comments in the WG.
  - The draft is actually quite detailed and is probably too long to be used as the generators section in the HSF document (8 pages without references, while the generator section should probably be ~4 pages in a ~20 page document). We are thinking of keeping this as a standalone paper (for arXiv or Zenodo, and/or a longer appendix to the LHCC document?), adding also a list of references and a list of authors, but still keeping the same May timescale. We will then summarise it as a 4-pager for the LHCC document.
  - Q. Could this be like the whitepaper that was intended from the Nov 2018 workshop? 
    - A. The overleaf document from then still exists, but it has a slightly different focus (would be hard to update numbers by May). Liz: this could also be a contribution to the upcoming US Snowmass process.

- Accounting:
  - Josh and Efe have analysed more in detail the ATLAS/CMS accounting for a specific process (V+jets LO), which is done with MadGraph5_aMC@NLO in both cases, but seems to be significantly slower in ATLAS. While a different filtering strategy could explain part of the difference, it is quite likely that the initial CMS numbers for this process were underestimated.
  - It is still very difficult to get precise numbers (in HS06 units) for CMS for past productions, for two reasons: first, GEN+SIM were done in the same jobs, with no separate accounting (therefore the GEN contribution has to be extrapolated from local tests); second, the data are only kept in the monitoring for 18 months. For more recent productions, the GEN and SIM steps have been split and can be accounted for separately. For these reasons, we are considering stopping analysing old CMS productions (also in the V+jets LO example), which is very time consuming and error-prone, and to wait until more data is available for the newer Grid productions with GEN and SIM split (timescale~2-3 months). 

- NNLO:
  - While preparing the document, we had some useful discussions about present and future NNLO needs. One small part of the note describes this in more detail.
  - We also contacted some theorists. In particular, Massimiliano Grazzini accepted to give a talk at the WG in June or later, specifically about ttbar calculations at NNLO.

-  GPUs:
   - Work ongoing on prototyping MadGraph on GPUs (Stefan, Olivier...).
   - Question from Josh: any news on the possibility of training for GPU development?

### Frameworks

- Working to schedule next meetings
    - BelleII would like to discuss their challenges, trying to schedule this
    - Topical metings:
        - Multi-threaded algorithm scheduling
        - Accelerator integration

## Workshops

### HSF/WLCG 2020 workshop

#### Logistics

Workshop registration is open:

<https://indico.cern.ch/event/867789/>

There is a [poster](https://indico.cern.ch/event/867789/attachments/1984157/3309134/Poster_HSFWLCG.pdf) on the website - please print and pin up! (CERN: B40, B32, B2, B1 and R1 fairly well covered - can someone do R2 and IT buildings?)

#### Scientific Programme

Organising team for HSF are: Graeme, Heather, David and Michel

**We consider the parallel timetable to now be fixed, so over to each WG to organise their sessions**

Current timetable proposal:

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
| AM Part 1   |   HSF Sim - Geant4 Modernisation |  HSF Tools & Packaging    | DOMA Plenary|
| AM Part 2   |   HSF Trigger&Reco - General    | HSF Generators Overview  | DOMA Plenary|
| PM Part 1    | HSF Sim - R&D |  HSF Generators R&D  | DOMA Plenary |
| PM Part 2    | HSF Sim - R&D |  HSF Frameworks  | DOMA Plenary |
| **Friday** | | | |
| AM     |   Wrap-up joint plenary   |     ||

- Next organisers meeting Tuesday 3 March (to work on plenaries).

#### HSF Common Session Ideas
- PyHEP talk and discussion
- Data Analysis WG talk and discussion
- Training WG talk and discussion 
- ML integration discussion (technical integration; general opportunities?)
- HSF organisation matters (if needed)
- Common Software document (input for LHCC)


#### Trigger&Reco sessions
- Session 1 (Wed): 
    - Run-3 LLP trigger and reconstruction improvements
    - Accelerators for trigger and reconstruction (joint? Plenary?)
- Session 2 (Thu): Contributed talks

Assorted:

- When do we want to meet REALTIME Advanced Study Group?  <https://realtime.blogg.lu.se/>
trigger&reco/licensing/validation chat could be useful. We could have it as an optional event at the end of a regular session (eg Tue?). However some of the participants have time constraints so an informal lunch could work too. 

## AOB

- A proposal describing how HSF delivers letters of cooperation and support:
    - <https://github.com/HSF/hsf.github.io/pull/732>

### Next Meeting

- Next regular meeeting slot is 12 March
