---
title: "HSF Coordination Meeting #303, 26 February 2026"
layout: plain_toc
---

## Attending

Present/Contributing: Liz Sexton-Kennedy, Eduardo Rodrigues, Claire Antel, Christian Wessel, Uwe Hernandez Acosta, Alexander Heidelbach, Stefan Roiser, Pere Mato, Dmitry Kalinkin, Michel Hernandez Villanueva, Joshua Isaacson, Andres Rios-Tascon, Maarten van Veghel, Juan Miguel Carceller, Saptaparna Bhattacharya, Alexander Moreno, Juraj Smiesko, Steven Gardiner, Da Yu Tou, Pablo Apausa Chamorro

Apologies/Contributing: Graeme Stewart, Philippe Gras, Inês Ochoa, Steve Mrenna

## News, general matters, announcements

### 2026 conveners

*Please [make PRs](https://hepsoftwarefoundation.org/howto-website.html) to update the names of the conveners on the website.*

### HSF Seminar Series and Compute Accelerator Forum

Planned HSF seminars:

- Seminar from creator of mp-units (supports units and constants in C++, see AOB): [25th Feb](https://indico.cern.ch/event/1642384/).  
    - Very clear and interesting presentation.
    - Around 45 people (at peak) attended.
    - Some constructive discussions afterwards.
    - [Recording](https://youtu.be/ROUiCy7rorU) uploaded to agenda.
    - There will be a followup meeting to discuss constants imporatant to HEP on the 27th, see AOB for details.
- Seminar on HS3: [25th March](https://indico.cern.ch/event/1622602/)
- Seminar by Kati Lassila-Perini (chair) on ICFA Data Lifecycle panel [best practice recommendations](https://icfa-data-best-practices.app.cern.ch/): [29th April]
    - Format: recommendations first, then discussion on mapping to HSF Project Guidelines. 
        - Question for us / SG: what would we like out of this mapping? Support / mention of HSF guidelines and supported projects? (ICFA represents a different audience wrt our current circles)
        - The steering group meeting is scheduled for tomorrow
        - Thinking about this until a month's time, then discuss again in Coord meeting

- 2nd in series on AI-assisted SW tools organised by software tools & packaging - possibly separate seminar organised with sustainability group.

(Thanks to the activity groups for coming to us with seminar ideas and speakers!)

HSF seminar conveners are reachable at <mailto:hsf-seminar-conveners@googlegroups.com>.

Please send your suggestions for next seminars.

### Steering Group & Advisory Group

Confirmed date for the **next WLCG/HSF Workshop is 2-6 November 2026, Bologna**.

- Let the SG know asap if you would be interested in helping organising the workshop from the HSF side - identification/discussion of topics is paramount.

### HSF Affiliated Projects and Software

List of current reviews underway:

- DIRAC / DIRAC X - done, sent an email to DIRAC reps, being cross-checked
- NoPayloadDB Conditions Database - ongoing
- Pepper - ongoing (mostly done)
- MadGraph5_aMC@NLO - done, will be sent to SG for review
- Pythia - ongoing (mostly done)

Do not hesitate to discuss around you to identify relevant projects/libraries that could engage with the affiliation programme.

Thank you very much to those who accepted to act as a "reviewer" or spontaneously put themselves forward. This is super appreciated; it makes all the difference.

Very positive feedback from the Pythia developers about the process!

## Activities Updates

### GSoC 2026

There are 31 proposals for this year's GSoC, 1 more in the pipeline.

- Mentoring organisations applied on 3 February
- Approval will come on 19 February
- Full timeline is available [here](https://hepsoftwarefoundation.org/activities/gsoc.html)

### Software Training

Next Training Events

- Analysis Reproducibility Training (Virtual) - April 27-30
    -   Modules: CI/CD GitHub Actions, Docker/Podman, Apptainer, CI/CD GitLab, and REANA
    -   It will be announced next week
-  14th HEP C++ Course and hands-on training, 9 - 13 March (hybrid)
    -  <https://indico.cern.ch/event/1617123/> 
    -  Registration is still open
- Software Basics at Labs - TBD (June) Would like to avoid conflicting events, please check the [HSF Calendar](https://hepsoftwarefoundation.org/future-events.html).
    - BNL
    - Fermilab 
- ML/DL Training (Virtual) - TBD (Probably July)

Papers
- Training on Data Analysis Reproducibility via Containerization with Apptainer. It will be submitted to The Journal of Open Source Education, JOSE, and also to the arXiv. 


### Event generators

- Would like to meet with new conveners for a plan for the rest of the year.
- Sapta and Steve noted a lot of synergistic activities with the data analysis group (SBI, unfolding)
- Received 3 GSoC requests for negative weight mitigation in ATLAS workflows and 1 for MCFM
- There will be a LHCC focus session on Generators with a longer talk by Leif Lönnblad covering the generator author status and talks by the experiments to discuss adoption of these developments for run 4.

### PyHEP

- Conveners meeting on Feb. 19
- PyHEP.dev 2026 workshop in planning stage:
    - Will be in Amsterdam (Nikhef) (95% confirmed)
    - Possible weeks: Sep 7-9,
    - Workshop length 3 days
- Preliminary planning for PyHEP 2026 workshop:
    - Will be mostly online, possible hybrid format (at CERN?)
    - Possible weeks: 9th-12th November, 16th-19th November
- Preliminary planning of PyHEP talks


### JuliaHEP

- JuliaHEP 2026 will be in Munich, October 19-23. We will start advertising the event soon!

- JuliaCon 2026 - JuliaHEP Mini-Symposium
    - JuliaHEP Mini 2026 - Julia for Nuclear and Elementary Particle Physics: From Precision Science to High-Performance Tools
    - Call for contributions to JuliaCon is now out:

JuliaCon Global 2026 in Mainz, August 10-15, 2026 (<https://juliacon.org/2026>). JuliaCon has traditionally featured talks that ranged from introductory to advanced, on topics related to various fields, delivered by developers and researchers from industry and academia. If you have worked with or on Julia in the past, JuliaCon is the best venue to share your work with the Julia community.
The Call for Proposals (<https://juliacon.org/2026/cfp/>) will close February 28, 2026.

## AOB
   
Do not hesitate to get in touch with the SG if you have/know of events useful to add to the HSF calendar.
The calendar is used by very many to check for available dates, constraints, and plan events. Thank you in advance.

### Physical Constants / HEPdata Library

Reminder that we proposed a C++ header-only library that defines physical constants and some salient HEPdata in a lightweight, easy-to-use manner. Also taking into account versioning.

There is a [meeting Friday 27 Feb at 13h30](https://indico.cern.ch/event/1655375/) for those interested. Attached to the agenda is a summary document with the main important points (open for any comments).

### Next Meeting

The next coordination meeting will be on March 12th.

### Chair This Meeting 👇

Please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing a future coordination meeting. (There is even a [HOWTO guide](https://hepsoftwarefoundation.org/organization/running-meetings.html)).
