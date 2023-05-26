---
title: "HSF Coordination Meeting #250, 25 May 2023"
layout: plain_toc
---

## Attending

Present/Contributing: Graeme Stewart, Pere Mato, Claire Antel, Eduardo Rodrigues, Krzysztof Genser, Efe Yazgan, Caterina Doglioni, Torre Wenaus, Patrick Gartung, Nicole Skidmore, Kyle Knoepfel, Nick Smith, Nicole Skidmore, Killian Lieret, Liz Sexton-Kennedy, David Lange, Valentin Volkl

Apologies/Contributing: Markus Diefenthaler, Benedikt Hegner

## News, general matters, announcements

### LHCP Presentation

Vangelis Kourlitis presented a [talk](https://indico.cern.ch/event/1198609/contributions/5370078/) on *HL-LHC and Beyond Computing Challenges*. Thanks to him and to everyone who commented on the slides.

### Pre-CHEP Workshop

The [pre-CHEP workshop](https://indico.cern.ch/event/1230126/) had 150 people attening (not bad for a weekend!).

*Analysis Facilities:** presentation of what we have learned about AFs from the Analysis Facilities Forum. Key topics, such as AAI, DOMA, site "toolkit" (or "substrate") as well as analyst needs were discussed. The AFF conveners released the first draft of their [Analysis Facilities White Paper](https://docs.google.com/document/d/1Pn9KWG-tGQ20OaNFUVlXLQddC7vFsQnu2EHR4DBfTjo/edit?usp=sharing), which is still very much open for comments. See below for LHCC slides. Still a lot of open questions - very nice work by the forum conveners to bring all of this into the open for discussion. The White Paper will be informed by the workshop itself and the draft comments are being discussed and incorporated.

*Non-x86 Architectures:** presentations on power advantages of ARM (36% power savings on HEPScore workloads), along with the experiments' experience of porting to ARM (ATLAS) and POWER9 (CMS), which is relatively strightforward. Progress in porting some middleware components and in running multi-arch jobs in the production systems - helped by increased availability at CERN and in the cloud. Some process is needed by which these resources can be pledged to be defined - this is something that will be discussed within WLCG (HSF can help). For GPU, 3/4 experiments using these at HLT in Run3, which improved efficiency, cost savings, etc (good talks from ALICE and CMS). Workloads do require significant tuning. No real experience of running mixed CPU/GPU workloads on WLCG - sites that have GPUs can help here, and we (HSF) can facilitate the process with the training. More discussion expected at the [JENA computing workshop](https://agenda.infn.it/event/34738/). There is a [summary document](https://docs.google.com/document/d/1U8GDHhUrkhvJT6qTYl221QVsfaK8amiNSI5ktm5Aekk/edit?usp=sharing) is available (which can be commented on!). 

### LHCC

The next LHCC week is 5-9 June. For software, the referees asked us to report on the future role of *Analysis Facilities*. There will be a special 1 hour session on Monday 5 June as this is a big topic.

Alessandra Forti, one of the Analysis Facilities Forum co-conveners, will present: [draft slides](https://docs.google.com/presentation/d/1lEjP4l2DZmT80BfADbd7CSSn7ryw9OmnnEyVLngWrDI/edit?usp=sharing). Please comment on them by Monday 29 June, as they need to be posted for the referees by this date.

There will be some further dedicated discussion on the presentation at the [Architects Forum meeting](https://indico.cern.ch/event/1251045/), Thursday 1 June at 14h CEST.

### Google Summer of Code, 2023

Only 17/22 projects with good students accepted - feedback from Google was that we had too many long projects. In previous years we had a 100% acceptance rate (there was also no difference in project size). For next year, we should balance long/short projects more.

Could have an HSF kick-off for all of the students? This would help foster a sense of community. Discuss with Benedikt / GSoC Coordinators / coordination list.

### JENA Computing Meeting

As mentioned above, there is a [joint ECFA/AaPEC/NuPEC meeting](https://agenda.infn.it/event/34738/) to discuss software and computing strategies for European science in Bologna, 12-14 June. JENA

- This was an outcome of discussions with the funding agencies at the last JENA Symposium in Madrid
  - Registration now seems to be generally open
- Workshop should lead to the formation of WGs that work on different aspects of the needs of the science areas
  - For HEP, these should form inputs to the next European Strategy Update

## Working Group Updates

### Data Analysis

- Due to CHEP some progress was made on the onboarding paper
  - Hopefully ATLAS and DUNE contributions coming
- Would like to have a meeting series dedicated to open data end of June
  - Recent developments in LHCb
  - Common issues amongst experiments
- Considering moving the meeting time to Monday 1500 - does this clash with anything?
  - We don't think so

### Software Training

- Software Basics Training:
  - Bash + Python + Git (taught by Carpentry instructors)
  - 150 registrants (hit our maximum, perhaps there would've been more)
  - O(70) joined the first session; O(50) remained in last session (very good retention rate for us)
    - Good pace in the delivery helped keep peoples' attention (don't spend too much time in the shallow waters of `cd`)
      - We learned that going too slow at the start loses the more advanced students
    - Carpentries membership not renewed this year

#### C++ Course and Hands-on Training

- JLab course
  - No attrition at all (in-person classes)
  - OOP methodology takes the spotlight in a 3-day course? Maybe think about the ordering of the course and move OOP later and smart pointers/STL earlier? 
    - Discuss this in the next monthly call
- Manchester course dates: 29/08-01/09, taught by Sebastian Ponce
  - Anyone from this meeting wants to come and help as demonstrator for hands-on exercises? We have good curry :) 
    - we will send the call to the appropriate mailing list
  - Announcement imminent, lots of bureaucracy needed for the fee payment (to pay for coffee breaks and said curry)
    - Full scholarships by Swift-HEP (including accommodation) for UK students who can't otherwise afford this

### Software Tools and Packaging

- Met at CHEP and coordinated for next steps, see last coordination meeting for plans.

### Detector Simulation

- Talk on Geant4 physics models and event generators scheduled for June 5th: <https://indico.cern.ch/event/1276128/> announcements/invites sent out
- Still following up on possible contributions on Geant4 cuts/optimizations implemented by experiments (Two identified)
- Still following up on possible contributions on Geant4 Physics extensions that experiments have developed (One identified)

### Reconstruction and Software Trigger

- Haven't managed to meet for chat since last meeting (CHEP, holidays), so no new news
- Already reported last meeting:
  - Following kick-off meeting last month, planning first topical meeting, most likely 4-D tracking in Belle II. Could become more general with some contributions from the LHC timing upgrades. Need to confirm target date & speaker.

### PyHEP

- PyHEP.dev 2023 in-person workshop: preparations well under way. Most registrations confirmed and sorted.

### Event Generators

- Draft tuning workshop agenda: <https://indico.cern.ch/event/1283969/> (online event only)
  - Started contacting speakers; some already accepted. But the dates may still change...

### Frameworks

- We will hold a meeting next week (Wed. 31 May):
  - [Using Alpaka with the CMSSW framework](https://indico.cern.ch/event/1281987/)
  - Matti Kortelainen (FNAL) will be presenting.

## Other Interest and Activity Areas

### JuliaHEP

Nice papers at CHEP showing good progress in using Julia and a lot of potential. We'd like to organise more activities here, so there is a [planning meeting next week](https://indico.cern.ch/event/1290359/), Tuesday 30 May, 16h CEST. Open to all!

The paper on *Potential of the Julia programming language for high energy physics computing* is now basically complete and ready for CSBS submission. The paper can be endorsed (there was a call on the `hsf-julia-for-hep-report@cern.ch` list), but the deadline is today.

### Compute Accelerator Forum

Change of topic for the next meeting - we will hear from the DOE funded HEP CCE project, which is now reaching the end of its first funding phase.

- Charles Leggett will present results on portable paralellisation layers
- Peter Van Gemmeren will present results on high-performance I/O

[Meeting will be held jointly with ATLAS Core Software in Salle Curie](https://indico.cern.ch/event/1264297/), Wenesday 14 June at 16h30.

---

## AOB

### Website

Benedikt started an [issue in GitHub](https://github.com/HSF/hsf.github.io/issues/1411) to gather ideas about reorganising and revamping the website to better reflect our areas of actual activity.

### Next Meeting

The next meeting will be, on [8 June](https://indico.cern.ch/event/1225017/)

Please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing this or one of the future coordination meetings.
