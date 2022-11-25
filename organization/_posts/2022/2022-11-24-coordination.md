---
title: "HSF Coordination Meeting #240, 24 November 2022"
layout: plain_toc
---

## Attending

Present/Contributing: Graeme Stewart, Benedikt Hegner, Ben Morgan, Efe Yazgan, Paul Laycock, Eduardo Rodrigues, Wouter Deconic, Sudhir Malik, Valentin Volkl, Michael Hernendez

Apologies/Contributing: Markus Diefenthaler, Josh McFayden, Nicole Skidmore


## News, general matters, announcements

### IRIS-HEP/HSF Joint meeting on Software Citation and Recognition

[Workshop](https://indico.cern.ch/event/1211229/) happened 22-23 November, with a wide range of participants from software projects, experiments, INSPIRE, Zenodo, journals. We covered a lot of topics, including having breakout sessions that touched on a few key points:

- A history of work and development in this area (see [Dan's opening talk](https://indico.cern.ch/event/1211229/contributions/5120849/attachments/2551669/4397173/software%20citation%20introduction.pdf))
  - A lot of good background to get to the current "state-of-the-art"
- What purpose do we foresee for software citations - it is for recognition? reproducibility? These are different things.
- What should we be citing? Academic articles? Software DOIs? Something in-between, like JOSS papers?
  - Should follow the recommendations of the software's authors, usually
  - Distinction between conference proceedings and journal articles is made in HEP (unlike CS); even refereed proceedings seem under-weighted
  - Some feedback from RSEs (not specifically HEP) is that they do not want to write journal articles!
- Experiments do have editorial guidance on what to cite, which varies from experiment to experiment
  - There would be value in having a set of overarching guidelines (e.g., curated by the HSF); which also gives software package authors a ~single point of contact
- Software DOIs are not really indexed at the moment, but they will be in the next round of INSPIRE developments
  - In an automated fashion only
- The mechanics of providing information on software citation has improved a lot (`CITATION.cff` files; Zenodo release harvesting, with authorship)
  - Can foresee some improvements, e.g., better handling of the *Concept* (all versions) DOI in Zenodo

There will be a report developed in the next few months (see final section of [Live Notes](https://docs.google.com/document/d/1AN-Kv59kkz3vyVLImeA3nehcyUfM2WEGnaCNBJRy7q4/edit?usp=sharing) for skeleton). The organisers also will submit a CHEP abstract.

Sudhir - important to also invite people who make the decisions in the experiments, e.g., Pub Com and Spokespersons.

Graeme - we did not bad for Pub Com Chairs. Generally got a good feeling on the openness of experiments to improve in this area.

### HSF Talk at SMARTHEP network kick-off

Benedikt gave a [talk at this event](https://indico.cern.ch/event/1204125/timetable/#30-the-hep-software-foundation) - thank you to Caterina for the invitation.

## Working Group Updates

### General

We now have a good number of nominations; however, we are awaiting some final nominations from the experiments this week.

Search committee will meet next week.

In January we will have a review of the year gone, as well as looking forward to 2023 - so please think about it.

#### Meetings

*Reminder:* Please try and book meetings in Indico at least 2 weeks in advance!

That way they go into the calendar early and they will be included in the weekly email announcement that goes to HSF Forum.

### Data Analysis

- Abstract for a talk on experiment training and on-boarding submitted to CHEP - this talk will accompany the paper that was discussed last time. All paper contributors are added as talk authors
- Still need to establish a timeline for the paper given everyone's busy work-loads

### Detector Simulation

- Next meeting on 28th November on Differentiable Computing for Simulation
  - <https://indico.cern.ch/event/1212880/>
- Last meeting of the year on 12th December covering Geant4 Physics Model Parameter variation
  - <https://indico.cern.ch/event/1216295/>
- Anticipate Geant4 Technical Forum in early December covering latest 11.1 release

### Reconstruction and Software Trigger

- Topical meeting on PID with RICH detectors yesterday, focusing on LHCb and EIC: <https://indico.cern.ch/event/1218610/>

### PyHEP

- [Next topical meeting](https://indico.cern.ch/event/1222913/) is taking place Wednesday December 7th. The tool RootInteractive, from ALICE colleagues, will be presented.
- We plan to organise in 2023 some of the meetings jointly with IRIS-HEP, given the regular overap in terms of topics presented and meeting attendees.

Benedikt - is the Python 3.11 speed-up "real" in HEP use cases? See talk from [Henry at PyHEP](https://indico.cern.ch/event/1150631/timetable/#34-whats-new-in-python-311). Caution - this is speed-up of CPython, would not necessarily be reflected in code using pandas, numpy heavily. <!-- markdown-link-check-disable-line -->

### Event Generators

HSF co-organized with CTEQ, EICUserGroup, and MCnet [MC4EIC](https://indico.bnl.gov/event/17608/), a workshop on event simulation for the EIC. The workshop covered:

- In-depth reports on the precision of foreseen measurements and the related MC event generator (MCEG) needs: Inclusive deep-inelastic scattering (DIS), semi-inclusive DIS, exclusive processes, jets and heavy flavor, BSM.
- Status of MCEG projects and the thrust of future R&D: Herwig, Phythia, Sherpa, BeAGLE, CASCADE, eHIJING, ePIC, eSTARlight, MadGraph5 aMC@NLO, MLEG, and SARTRE.
- Connection between formal QCD theory and its implementation in MCEGs:
  - Is there a QCD-based computational framework that allows easy implementation of new theoretical developments, while also making MCEGs predictive and versatile enough to be used successfully by experiments?
  - How can we make use of existing expertise, experience and technology to advance the construction of MCEGs for the EIC? 
  - What measurements will be essential for tuning the MCEGs?

A workshop report is in preparation.

We are still working on a meeting in December and aim for a tuning tutorial in February.

### Software Training

- Upcoming data preservation training week: Jan 16 - 20, 2023, on topics of docker, singularity, CI/CD etc.
  - modified format: self-training with videos followed by discussion by experiment experts
- Data preservation hackathon: Wed 7 Dec
  - focus on getting training materials ready for training week
  - <https://indico.cern.ch/event/1224647/>
- Attended EuSSI Training Bazaar where similar challenges were discussed (instructor pool, retention and attrition of participants)
  - <https://www.eventbrite.co.uk/e/eussi-training-bazaar-tickets-440454480207>
  - [HSF talk given by Michael](https://docs.google.com/presentation/d/1dTUSyJAEZoOy65Yp6bpD_GudrRZq2eT5thsce1DPPSc/edit?usp=sharing).
  - Graeme - We said we would like to cooperate on developing training materials. Particularly in less popular areas, like C++. Remains to be see if anything concrete comes from that.
  - Ben - Midlands RSE group were interested in this also
- Submitting multiple CHEP abstracts on sustainability of training efforts.

#### C++ Course and Hands-on Training

- (Sudhir on behalf of C++ team)- 5th HEP C++ Course, post-training discussion (Advance the HEP C++ Course - fixed monthly meeting) <https://indico.cern.ch/event/1203350/>
  - Please have a look at [slides](https://indico.cern.ch/event/1203350/contributions/5060368/attachments/2548822/4389866/20221116-HepCppCourse-5thCoursePostTraining.pdf)

- How many people have been trained to date?
  - Registration has been 75-100 for each course, so 375-500, *but there is attrition wrt. original registration numbers*

## Other Interest and Activity Areas

### Compute Accelerator Forum

- 2022 Calendar
  - Next meeting will be on [ACTS track reconstruction on GPUs](https://indico.cern.ch/event/1160623/), 14 December
- 2023 Calendar
  - [Madgraph5_aMC@NLO](https://indico.cern.ch/event/1207838/), 8 February
  - [Hepix Benchmarking](https://indico.cern.ch/event/1207839/), 8 March

- Do get in touch with Graeme, Ben, Stefan if you have an idea or a topic to present

### Software and Computing Roundtable

The Software and Computing Roundtable restarts on Dec. 13 with an update on EIC Software. There will be presentations on the [EIC Software: Statement of Principles](https://eic.github.io/activities/principles.html) and the software stack. The "Year in Review" event with contributions from the HEP Software Foundation, Brookhaven National Laboratory, and Jefferson Lab will be on Jan. 17.

## AOB

### HSF Calendar

We started filling in the calendar for 2023.

- [x] ALICE
- [x] ATLAS
- [x] CMS
- [x] LHCb
- [x] Belle II
- [x] DUNE
- [x] EIC

- [x] CHEP and other conferences...

Should now be done!

### Next Meeting

Our next coordination meeting is 8 December - this will be the last one of 2022.

Meetings for 2023 are now [booked in Indico](https://indico.cern.ch/category/7970/). We follow the tradition of meetings on the [odd weeks of the year](https://en.wikipedia.org/wiki/ISO_week_date).

The first meeting next year is January 19, where we will start by reviewing 2022 and planning for 2023.
