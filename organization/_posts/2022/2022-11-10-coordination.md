---
title: "HSF Coordination Meeting #239, 10 November 2022"
layout: plain_toc
---

Present/Contributing: Graeme Stewart, Markus Diefenthaler, Pere Mato, Nicole Skidmore, Valentin Volkl, Kyle Knoepfel, Krzysztof Genser, Ben Morgan, Michel Jouvin, Josh McFayden, Stefan Roiser, Sudhir Malik, Caterina Doglioni, Dorothea vom Bruch, Eduardo Rodrigues, Pete Elmer, Kevin Pedro, Mason Proffitt, Matti Kortelainen, Pradeep Tripathi, Daniel Elvira, Andi Salzburger, Jin Huang, Mark Neubauer

Apologies/Contributing: Benedikt Hegner, Michel Villanueva, Efe Yazgan

## News, general matters, announcements

### IRIS-HEP/HSF Joint meeting on Software Citation and Recognition

This will go ahead as a 2 x 1/2 day meeting, 22-23 November - there was too much material to fit into a single afternoon/morning slot.

This has been properly announced and the timetable published in Indico: <https://indico.cern.ch/event/1211229/>.

Contributions from experiments, projects, publishers, ... with lots of time for discussion.

Output will be a report on the discussion and best practice recommendations.

Registration is open - so far 53 people are registered.

## Working Group Updates

### General

We have a reply by all conveners regarding continuations. The search is ongoing. So far not very many nominations.

#### Meetings

Please try and book meetings in Indico at least 2 weeks in advance!

That way they go into the calendar early and they will be included in the weekly email announcement that goes to HSF Forum.

### Data Analysis

- Status of paper that will detail the training meeting series we had before the Summer and give guidelines for onboarding "best-practices"

Quick reminder:

> Before the summer, we had HSF Data Analysis WG sessions dedicated to experiments’ training/on-boarding of new collaboration members
>
> <https://indico.cern.ch/event/1175096/>
> <https://indico.cern.ch/event/1175097/>
>
> We would like to turn this into a published document describing each experiment’s approach, analysing similarities/differences and (hopefully) summarising “best practices” for future endeavours. We believe these initiatives, and the people behind them, deserve such recognition.
>
> We envisage letting each experiment have a dedicated section (<2 pages) in the document to describe their schemes. Then we will formulate an introduction, analysis, “best practice” and summary section. We hope that this document could act as the official reference for some experiments’ initiatives as AFAIK some are not documented elsewhere.

- Approached training WG who are on-board
- [Template](https://www.overleaf.com/read/hxmfpckhkydf) in Overleaf exists and is ready to be populated
- Have now emailed speakers who generally are very keen but also very busy so need to think about timescales

Graeme suggested that the group could connect this work to a paper at CHEP, in Track 8 (Collaboration, Reinterpretation, Outreach and Education).

### Detector Simulation

- Had a well attended [meeting on FLUKA.CERN](https://indico.cern.ch/event/1196629/) on October 31st
- Next meeting: differentiable simulation, Nov 28, <https://indico.cern.ch/event/1212880/>
  - speakers confirmed & finalized, will be broadly announced today
- A future session (most likely on December 12) will be on varying Geant4 parameters

### Reconstruction and Software Trigger

- PID meeting settled, Wed Nov 23:
  - <https://indico.cern.ch/event/1218610/>
  - Two talks: LHCb RICH and AI-based RICH reco
- Working towards last meeting of this calendar year. Preliminary idea is resonance reconstruction

### PyHEP

- Topical meeting yesterday on [Julia in HEP](https://indico.cern.ch/event/1216692/)
  - Report from Pere on experience porting VecGeom to Julia
  - Report from Philippe on continuing work implementing jet clustering in Julia (anti-kt)
  - Report on lessons learned from the UnROOT development from Jerry
- Conclusion that achieving optimised C++ performance for non-trivial code requires quite some work, with a different set of skills than used to optimise C++
- Draft of the Julia in HEP report is very close to finalised, hoping to submit it soon to CSBS and maybe a CHEP paper

### Software Tools and Packaging

- PUNCH Lunch talk was well received
  - longer discussion about future of linux distros in HEP
  - possible future meeting
    - input/discussion with/from smaller communities and experiments would be welcome
  - rebuild clones seem to be favoured
- Todd Gamblin again available for a Spack talk, narrowed possible dates down to 9th till 16th Jan 2023
- Working on Spack training materials now

### Event Generators

- Co-organizing [MC4EIC](https://indico.bnl.gov/event/17608/) with CTEQ, EICUG, MCnet. Online workshop on MC event simulation for the EIC on November 16–18.
- Continuing discussion on ML for MCEGs in December, aiming for discussion on ML for hadronization models.
- No meeting planned for January.
- Planning on tuning tutorial in February.

### Frameworks

- Nothing to report.  We are still open to receiving suggestions for presentations from small experiments.  If we hear nothing in the next few weeks, we might schedule another C++20 talk.

### Software Training

- We organized an Analysis Preservation Hackathon on Nov 1, 2022.
  - <https://indico.cern.ch/event/1214642/>
  - Focused on improving our training modules for Docker, Singularity, CI/CD with GitHub and GitLab.
  - Several issues closed, major improvements in our Singularity module ([link](https://hsf-training.github.io/hsf-training-singularity-webpage/)).
  - A few remaining issues for moving Singularity/Apptainer training from alpha to beta version.
- Organizing an Analysis Preservation training event.
  - Tentatively Jan 16 - 20, 2023.
  - Preparing material, list of invited speakers.

- Pete, would like to find ways to support training material development (discussed recently)

#### 5th HEP C++ Course and Hands-on Training

- Course ran a few weeks ago, much appreciated by the people who attended. However, there were a lot of no-shows - perhaps the level was too high?

## Other Interest and Activity Areas

### Compute Accelerator Forum

- 2022 Calendar
  - Meeting with [Meteo Swiss](https://indico.cern.ch/event/1160622/) happened yesterday (9 Nov)
  - Next meeting will be on [ACTS track reconstruction on GPUs](https://indico.cern.ch/event/1160623/), 14 December
- 2023 Calendar
  - [Madgraph5_aMC@NLO](https://indico.cern.ch/event/1207838/), 8 February
  - [Hepix Benchmarking](https://indico.cern.ch/event/1207839/), 8 March

- Do get in touch with Graeme, Ben, Stefan if you have an idea or a topic to present

### HSF-India

No news recently, would be good to check with David about progress on the project registry.

---

## AOB

- Research Software Engineering in Data & AI Workshop 2023 @ University of Warwick, UK, 15-17th February 2023
  - _Collaboration between Warwick and Alan Turing Institute: "... workshop for Research Software Engineers (RSEs) and other Digital Research Infrastructure professionals (DRIs) who support research in the field of Data Science and Artificial Intelligence"_
  - _Participants are invited to propose talks that highlight the contribution of RSEs/DRIs in facilitating Data & AI research, for example:_
    - _Tools, software, and pipelines developed for applications in data & AI_
    - _Data stewarding/management_
    - _Systems for big data_
    - _Good practices for open and reproducible research_
    - _Software sustainability and contribution to open source_
    - _Communicating with academics and industrial partners_
    - _Training in data science skills._
  - Organizers would be interested in hearing from HEP field, so if anyone would be interested in covering HSF and how HEP is approaching the above, please let me (Ben Morgan) know in the next few days. Can be remote.

### HSF Calendar

We started filling in the calendar for 2023.

- [ ] ALICE
- [x] ATLAS
- [x] CMS
- [x] LHCb
- [x] Belle II
- [ ] DUNE
- [ ] EIC

- [x] CHEP and other conferences...

But please check and help!

### Next Meeting

Our next coordination meeting is on 24 November, which is Thanksgiving. US colleagues are excused!
