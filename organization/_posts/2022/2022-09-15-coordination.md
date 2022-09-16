---
title: "HSF Coordination Meeting #235, 15 September 2022"
layout: plain_toc
---

Present/Contributing: Graeme Stewart, Serhan Mete, Benedikt Hegner, Liz Sexton-Kennedy, Valentin Volkl, Pere Mato, Jin Huang, Wouter Deconinck, Ben Morgan, Krzysztof Genser, Josh McFayden, Michel Jouvin, Kyle Knoepfel, Matti Kortelainen, Sudhir Malik, Stefan Roiser, Philippe Canal, Stefan Roiser, Michel Jouvin

Apologies/Contributing: Kevin Pedro, Nicole Skidmore, Stephan Hageboeck, Eduardo Rodrigues, Efe Yazgan

## News, general matters, announcements

### LHCC

Slides presented at the LHCC are attached to the [agenda](https://indico.cern.ch/event/1096598/).

LHCC Feedback:

#### News from many fronts (a selection)

- Event Generators: covering theoretical, experimental and computing aspects (possible role of AI/ML)
- Detector simulation: Fast Calorimeter Simulation Challenge; Recent developments and experience with DD4hep
- Simulation: Geant4 11.1-Beta released, new VecGeom release v1.2.0 (enhanced CUDA support, C++17 default std)
- ROOT: 6.26/06 released, current recommended release. All experiments agree to use 6.24 for production, at least for the initial part of Run 3. Simplifies maintenance for ROOT.
- CernVM File System: Version 2.10 feature complete, pre-release available

#### Personnel turn-over

- ROOT: Significant challenges due to departure / time reduction of key people, for instance end of fellowship for inventor of RDataFrame, departure of CernVM LD affecting RNTuple development -> CERN is willing to hire new collaborators
- EU grant SYCLOPS as partner (~ 450 k€ for ROOT) - RDataFrame offloading (GPU and possibly other accelerators)
- CernVM File System: a talented staff left to industry -> position is reopened
- Collaboration with private companies: one fellow funded from Jumptrading

#### Training & attracting young talents

- Training: Mathplotlib, Software carpentry, hackatons, Advanced C++…, Geant4 (beginners, advanced)
- Google Summer of Code:
  - HSF is participating in the program as a GSoC umbrella organization (CERN-HSF)
  - Proposition of projects on common SW (26 participating organisation)
  - 2022: Google granted a quota of 27 students ; all passed mid-term evaluation (projects to be finished in Sept.)

The WLCG Software Report for the RRB (2022-H2) is available [here](https://docs.google.com/document/d/1WbwmWYe1bp_TJMwTfOdMlm3ecAmlpuH51mgRnhqU9nQ/edit?usp=sharing). It will be submitted Friday 16 September, so please check now if there's anything to add or correct.

### Twitter

Twitter goes at speed for the HSF!

We have a new training dedicated twitter: [@hsftraining](https://twitter.com/HsfTraining). We encourage you to follow this and the main HSF twitter, [@hepsoftfound](https://twitter.com/hepsoftfound).

The HSF homepage was updated with a feed from twitter for more visibility.

### .github for HSF

We have created a [.gitub](https://github.com/HSF/.github) repository that allows us to have a *landing page* for the organisation itself on GitHub.

We are adding a first [README](https://github.com/HSF/.github/pull/2). N.B. This doesn't replace the website at all, but it is very useful to provide a good experience for people browsing the organisation.

## Working Group Updates

### General

### Data Analysis

- Coordinators meeting next week to discuss how to follow on from *Data analysis training in HEP experiments* meeting series [1](https://indico.cern.ch/event/1175096/), [2](https://indico.cern.ch/event/1175097/) featuring DUNE, CMS, ATLAS, BelleII, LHCb, EIC

### Detector Simulation

- Contacted possible speakers for differentiable simulation, awaiting proposals of possible dates
- Next meeting on October 31st on FLUKA.CERN: <https://indico.cern.ch/event/1196629/>
- September is busy with other meetings, including Geant4 Collaboration Meeting (in Rennes)
  - Open [Geant4 Technical Forum](https://indico.cern.ch/event/1156193/sessions/440560/#20220927) on Tuesday 27 Sept 2022, 16:00 Paris time

### Reconstruction and Software Trigger

Continue to put together the fall meeting lineup:

- Oct: RICH PID reconstruction. Reaching out to speakers and finalizing dates (Proposing Oct 5 or 19 4-5PM CET)
- Nov: GNN tracking
- Dec: KFParticle + HF tagging

Other topic of interests: particle flow jet reco, reconstruction on AI chips (e.g. [LHCb related work](https://arxiv.org/abs/2008.09210))

### PyHEP

- PyHEP workshop is ongoing, with more than 1000 people registered
  - Peak attendance on Monday was more than 200
  - Now at to a steady 75 per session
  - Two social events held on *Virtually Green*
  - Hackashop running this evening and tomorrow morning

### Software Tools and Packaging

- Finalizing a series of Spack discussions with LCG, CMS, LHCb and Spack developers
  - We discussed Spack training and think this would be a good idea, both for users and developers
  - There is a view/environment tutorial (sort of) here: <https://spack-tutorial.readthedocs.io/en/latest/tutorial_environments.html>
- mail discussion regarding conda with a PUNCH developer, possible meeting
- Meeting on ACTS build time optimizations during the summer was sparsely attended, repeat discussion at a future meeting

### Event Generators

- Very nice talk from Anja Butter (and well attended meeting) on ML for generators at [last meeting](https://indico.cern.ch/event/1180220/)
- Next meeting: Electron Ion Collider and Nuclear Physics Generators by Markus D., Oct, 6th. ([Agenda](https://indico.cern.ch/event/1200496/)).
- Discussing next topics for the meetings until the end of the year. May follow up on ML for generators.
  - Possibly driven in part by key discussion topics from Snowmass
- Co-host MC4EIC (Nov., 16-18)

### Frameworks

- [Planned meeting](https://indico.cern.ch/event/1196608/) for Sep 21 with contribution about Jana2 framework (David Lawrence from JLab is the speaker).
  - Overlaps with CMS Week, but the conflict with framework folks could be smaller than with any option considered for October

### Software Training

- HSF Training Containerization hackathon on September 6
- PyHEP 2022 [Talk "Teaching Python the Sustainable Way: Lessons Learned at HSF Training"](https://indico.cern.ch/event/1150631/timetable/#20220912.detailed) (September 12) and Hackathon on matplotlib and scikit-hep tools
- Please advertise the next training event [HSF/IRIS-HEP Software Basics Training (Virtual)](https://indico.cern.ch/event/1190572/) (September 28-30)
  - Next ones planned ([7 May - 19 May, 2023](https://indico.cern.ch/event/1190821/) and [08 Feb - 10 Feb, 2023](https://indico.cern.ch/event/1190820/))
- HSF Training is now on twitter as well! Please follow [@HSFTraining](https://twitter.com/hsftraining)

#### 5th HEP C++ Course and Hands-on Training

- October 11-13: Advanced C++ Training, 100 students registered
  - More tutors would be really welcome (contact Stefan Roiser), doodle for signup <https://doodle.com/meeting/participate/id/dwm961ma>

## Other Interest and Activity Areas

### Compute Accelerator Forum

- Meeting on [Wednesday 14 September](https://indico.cern.ch/event/1073646/) restarted activities
  - Christian Mayr (TUD) introduced SpiNNaker 2 and neuromorphic computing

---

## AOB

### IPA2022

Common software tools discussion at *Interplay between Particle and Astroparticle Physics*, IPA 2022 <https://indico.cern.ch/event/837621/contributions/5041291/>

### Reminder: Future Trends in Nuclear Physics Computing Workshop

[Future Trends in Nuclear Physics Computing](https://indico.bnl.gov/event/15089/) will be 28-30 September at Stony Brook University.

### IRIS-HEP/HSF Joint meeting on Software Citation and Recognition

Planning a possible one-day meeting to discuss topics around how HEP experiments handle citation of software and recognition for software efforts that enable physics publications and other means of disseminating results to the public.

Decided on the date: Wednesday 23 November.

Planning document will be circulated shortly. We will link to relevant discussions, e.g., at Snowmass this summer.

### HSF Calendar

We started filling in the calendar for 2023 - please check and help!

### Next Meeting

Our next coordination meeting is on 29 September.

N.B. We are back in 32/S-C22 here at CERN.
