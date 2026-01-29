---
title: "HSF Coordination Meeting #301, 29 January 2026"
layout: plain_toc
---

## Attending

Present/Contributing: Caterina Doglioni, Peter Fackeldey, Christian Wessel, Graeme Stewart, Ruslan Mashinistov, Joe Osborn, Inês Ochoa, Stefan Roiser, Luke Kreczko, Michel Villanueva, Uwe Hernandez Acosta, Claire Antel

Apologies/Contributing: Eduardo Rodrigues, Alexander Moreno, Maarten van Veghel

## News, general matters, announcements

### 2026 conveners

We are finalising the teams of 2026 AA conveners. Most invitations have been sent out and we already received many acceptations - thank you! We hope to have the full 2026 team by the end of the month.

### HSF Seminar Series and Compute Accelerator Forum

- HSF Open Data seminar joint with IML yesterday (<https://indico.cern.ch/event/1604475/>): ~45 people in attendance.
    - See trigger & reco report
    - Recording will be on the agenda

Planned HSF seminars:
- Seminar from creator of mp-units (supports units and constants in C++, see AOB): [25th Feb](https://indico.cern.ch/event/1642384/).
- Seminar on HS3: [25th March](https://indico.cern.ch/event/1622602/)
- Seminar by Kati Lassila-Perini (chair) on ICFA Data Lifecycle panel [best practice recommendations](https://icfa-data-best-practices.app.cern.ch/): [29th April]
    - Format: recommendations first, then discussion on mapping to HSF Project Guidelines. 
        - Question for us / SG: what would we like out of this mapping? Support / mention of HSF guidelines and supported projects? (ICFA represents a different audience wrt our current circles)
        - Thinking about this until a months time, then discuss again in Coord meeting

- 2nd in series on AI-assisted SW tools organised by software tools & packaging - possibly separate seminar organised with sustainability group.

(Thanks to the activity groups for coming to us with seminar ideas and speakers!)

HSF seminar conveners are reachable at <mailto:hsf-seminar-conveners@googlegroups.com>.

Please send your suggestions for next seminars.

### Steering Group & Advisory Group & WLCG/LHCC/IRIS-HEP liaisons

SG meeting date not yet confirmed. 

Advisory Group meeting expected for February 11th - will report back. 

Proposed date for WLCG/HSF workshop: 2-6 November, Bologna. 

IRIS-HEP meeting with HSF feedback postponed, date not yet confirmed. 


### HSF Affiliated Projects and Software

The list of affiliations is so far rather short but there is momentum, with several "reviews" ongoing or on the horizon:
  - DIRAC / DIRAC X - done, sent an email to Eduardo + DIRAC reps, being cross-checked
  - NoPayloadDB Conditions Database - ongoing
  - Pepper - ongoing
  - MadGraph5_aMC@NLO - done, will be sent to SG for review
  - Pythia - ongoing (mostly done)

Discussion points:
  - Language-specific code reviews
      - Python: HSF gives a tool to check, can be used for cross-checking what the project uses for themselves
      - C++ a bit more tricky (also projects using mixed languages)
  - After the technical review: 
      - Do we circulate to SG and to authors? 
      - Does the report become public? (Once the badge has been achieved && if the authors agree)
          - Consensus is that it should be public, so different people can read it and evaluate the different categories we're reviewing as well 

Do not hesitate to discuss around you to identify relevant projects/libraries that could engage with the affiliation programme.

Thank you very much to those who accepted to act as a "reviewer" or spontaneously put themselves forward. This is super appreciated; it makes all the difference.

## Activities Updates

### GSoC 2026

Call for mentors 2026 is open - Deadline Feb 1st (Saturday!) Email hsf-gsoc-admin@googlegroups.com if you are interested in mentoring a project or add it to the website directly (see https://github.com/HSF/hsf.github.io/pull/1804)

Note that it is probably a good idea (and recommended by Google) to add an AI usage policy to the project idea, for example

> ## AI usage policy
> AI assistance is allowed for this contribution. The applicant takes full responsibility for all code and results, disclosing AI use for non-routine tasks (algorithm design, architecture, complex problem-solving). Routine tasks (grammar, formatting, style) do not require disclosure.


### Software Training

Next Training Events

- Analysis Reproducibility Training
    -   Week of April 27 or May 4.TBD
    -   Modules: CI/CD GitHub Actions, Docker/Podman, Apptainer, CI/CD GitLab, and REANA 
-  14th HEP C++ Course and hands-on training, 9 - 13 March (hybrid)
    -  https://indico.cern.ch/event/1617123/ 
    -  Registration has opened


### Event generators

- Ready to submit two GSoC projects on negative weight mitigation using the cell resampling technique. Envision one project to be more theory based (running cell resampling at NNLO with MCFM, the other one would be more ATLAS specific.
- Would like to meet with new conveners for a plan for the rest of the year


### Detector Simulation

- [related] Next WLCG environmental sustainability forum (Feb 17th, to be announced) on speeding up detector simulation

### Data Analysis

- Had a discussion of possible topics for 2026
- Considering a seminar series on "ML in analysis" covering topics such as SBI, unfolding, etc. (would aim for spring)
    - Would be nice to collate the discussions into a review paper
        - Could be a "5 years on" to [arXiv:2010.06439](https://arxiv.org/abs/2010.06439), but quite some overlap with [Simulation Based Inference Blueprint](https://indico.cern.ch/event/1600677/overview)
    - Could have a workshop at end of summer/early autumn (need to consider who would support this)
- Would like to push again on reproducibility/reinterpretation topics (workflow managers, REANA, HS3, etc.)

### Reconstruction and Software Triggers

- Open data seminar went well, good discussion and well attended
    - Overall useful discussion that consolidated material available to the community in one place
    - Ran out of time for discussion, good sign

### PyHEP

- PyHEP.dev 2026 workshop in planning stage -> Starting reaching out to a potential host in Nikhef.
- 2 new convenors: Alexander & Dmitry -> Plan to meet soon

### JuliaHEP

[notes from last meeting still apply]

- JuliaHEP 2026 will be in Munich. End of September or beginning of October - TBD
    - [Planning meeting](https://indico.cern.ch/event/1639187/), 30th Jan at 15:00 CERN time

- JuliaCon 2026 - Mini-symposium proposal was accepted:
    - JuliaHEP Mini 2026 - Julia for Nuclear and Elementary Particle Physics: From Precision Science to High-Performance Tools
    - Call for contribtions to JuliaCon is now out:

> Dear colleagues,
We invite you to submit proposals to give a presentation (talk or poster) at JuliaCon Global 2026 in Mainz, August 10-15, 2026 (https://juliacon.org/2026). JuliaCon has traditionally featured talks that ranged from introductory to advanced, on topics related to various fields, delivered by developers and researchers from industry and academia. If you have worked with or on Julia in the past, JuliaCon is the best venue to share your work with the Julia community.
The Call for Proposals (https://juliacon.org/2026/cfp/) will close February 28, 2026.
We look forward to hearing from you.
The JuliaCon 2026 Organizing Committee

- [Julia in ErUM: Get Started with Julia](https://indico.desy.de/event/51336/) - Feb 6
    - Targets DE community, but open to all

### Software Tools and Packaging

   - Evaluating the "Multi-platform builds of HEP software on conda-forge for distribution" project https://github.com/hep-packaging-coordination
       - This should be the open source version of conda-forge 
   - Can HSF help with the project promotion?
       - It could become an affiliated project

## AOB

Do not hesitate to get in touch with the SG if you have/know of events useful to add to the HSF calendar.
The calendar is used by very many to check for available dates, constraints, and plan events. Thank you in advance.

### EVERSE community event next week

[EVERSE Community Event at CERN on February 5th](https://indico.cern.ch/event/1606722/), see announcement on mailing list

### Physical Constants / HEPdata Library

Reminder that we proposed a C++ header-only library that defines physical constants and some salient HEPdata in a lightweight, easy-to-use manner. Also taking into account versioning.

This has rather stalled - but please get in touch with Graeme Stewart if you would like to discuss involvement in this.

### Next Meeting

The next coordination meeting will be on February 12th.

### Chair This Meeting 👇

Please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing a future coordination meeting. (There is even a [HOWTO guide](https://hepsoftwarefoundation.org/organization/running-meetings.html)).
