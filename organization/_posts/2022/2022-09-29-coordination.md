---
title: "HSF Coordination Meeting #236, 29 September 2022"
layout: plain_toc
---

## Attending

Present/Contributing: Graeme Stewart, Dorothea Vom Brush, Efe Yazgan, Nicole Skidmore, Kyle Knoepfel, Eduardo Rodrigues, Matti Kortelainen, Michel Jouvin, Valentin Volkl, Kilian Lieret, Alessandra Forti, Liz Sexton-Kennedy, Daniel Elvira

Apologies/Contributing: Kevin Pedro, Ben Morgan, Krzysztof Genser, Markus Diefenthaler, Benedikt Hegner, Pere Mato

## News, general matters, announcements

### Events

Many ongoing meetings this week: Geant4 collaboration meeting, Future Trends in NP, ACTS hackathon, Software Carpentry Training.

Next week:

- [ECFA workshop on e+e- Higgs/EW/Top factories](https://indico.desy.de/event/33640/), with several software talks
- [Fast Machine Learning for Science](https://indico.cern.ch/event/1156222/)

## Working Group Updates

### Data Analysis

- Were not able to meet due to various hackathons. Will meet Monday to discuss how to build on training series

- Graeme: we should also discuss the outcomes of the AFII workshop soon and make sure that items are followed up

### Detector Simulation

- Geant4 Collaboration meeting is in progress
- Contacted possible speakers for differentiable simulation, awaiting proposals of possible dates
- Next meeting on October 31st on FLUKA.CERN: <https://indico.cern.ch/event/1196629/>

### Reconstruction and Software Trigger

Continue to put together the fall meeting line up:

- Oct: GNN tracking, speakers confirmed, Finalizing dates (Proposing Oct 19 4-5PM CET)
- Nov: RICH PID reconstruction. speakers confirmed, Finalizing dates
- Dec: KFParticle + HF tagging: Reaching out to speakers

### PyHEP

Workshop held 2 weeks ago, with 420 people attending at some point (peak ~250 on the Monday, later days ~60-70). Success for the community.

Videos all now posted on [YouTube](https://www.youtube.com/playlist?list=PLKZ9c4ONm-VkohKG-skzEG_gklMaSgaO7).

Post workshop survey ongoing, full report later.

### Software Tools and Packaging

Will do a punch lunch (lunchtime meeting) with <https://www.punch4nfdi.de/> on packaging later in the year

Lining up spack talks

### Event Generators

- [Electron Ion Collider and Nuclear Physics Generator](https://indico.cern.ch/event/1200496/) by Markus Diefenthaler (6 Oct.) 
- November/December:
  - Follow up snowmass topics (will contact Josh Isaacson, Stefan Hoeche, et al.)
  - Also, will (probably) organize meetings to follow up on generators with ML (e.g. hadronization).  
  - Need to discuss MC4EIC (November) workshop 

### Frameworks

We met [last week](https://indico.cern.ch/event/1196608/) to hear from David Lawrence (JLab) regarding the JANA2 framework.

- Roughly a dozen participants.
- It was a similar talk to a couple years ago, but there were some updates wrt the EIC adopting JANA2.
- Much of the existing EIC code uses Gaudi, so they are working on understanding conceptual differences between Gaudi and JANA2 and what migration layers are necessary.

### Software Training

- Currently ongoing: [Software Basics Training](https://indico.cern.ch/event/1190572/) (formerly called "Software carpentry event")
  - Two days (Git/Python/bash) taught by Software Carpentry
    - Final day: PyROOT and Scikit-HEP taught by our community
  - 80 registrants, but only O(25) participants (unusually high attrition rate, usually we have 50%). Very basic training: is it something to review? Is it still useful?
  - Really good participation in the lectures though
- Please follow us on [twitter @HSFTraining](twitter.com/hsftraining)
- Hacktoberfest participation planned (see below)

#### 5th HEP C++ Course and Hands-on Training

- October 11-13: Advanced C++ Training, 100 students registered
  - More tutors would be really welcome (contact Stefan Roiser), doodle for sign-up <https://doodle.com/meeting/participate/id/dwm961ma>

## Other Interest and Activity Areas

### Analysis Facilities

A few recent meetings:

- Containers and CVMFS: <https://indico.cern.ch/event/1202055/>
- Planning meeting: <https://indico.cern.ch/event/1200052/>

---

## AOB

### Hacktoberfest

Kilian noted:

> "As in the last year, there is the https://hacktoberfest.com/ coming up in October, encouraging open source contributions from new contributors.
>
> "To mark projects as eligible, we can simply add the hacktoberfest topic to a github/gitlab repository and the "hacktober" label to issues.
>
> "However, I was wondering whether we want to organize an HSF-wide Hacktoberfest event? This would basically be a short event where we present a few introductory slides about collaborative git and then show a few demo issues for participants to work on, then let everyone work on things by themselves.
>
> "For slides, we could take the slides that Aman Goel just recently showed at PyHEP.
> 
> "The few events that are listed so far on https://hacktoberfest.com/events/ all seem to be of mostly-global scope, but we might still just add ours.
>
> "As this is a really big global event, the attendance might also be really large, though I've heard people dampen the expectation for high-quality PRs.  However, I still think this might be a good opportunity for us."

- If we join, should market it to our HEP students and advertise it as "this month you canget nice perks for contributing to any participating repository"
- Same with event: Probably best to market it to "our people" rather than adding it to "official" events

- Discussion: Time is a bit short and the projects are pretty busy. Decided that Training WG will take part this year. If it's a success then we can have a more organised involvement next year.

### IRIS-HEP/HSF Joint meeting on Software Citation and Recognition

*Reminder*

Planning a possible one-day meeting to discuss topics around how HEP experiments handle citation of software and recognition for software efforts that enable physics publications and other means of disseminating results to the public.

Decided on the date: Wednesday 23 November.

Planning document will be circulated shortly. We will link to relevant discussions, e.g., at Snowmass this summer.

### HSF Calendar

We started filling in the calendar for 2023 - please check and help!

### Next Meeting

Our next coordination meeting is on 13 October.
