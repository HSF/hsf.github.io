---
title: "HSF Coordination Meeting #269, 23 May 2024"
layout: plain_toc
---

## Attending

Present/Contributing: Graeme Stewart, Stefan Roiser, Andrea Valassi, Patrick Gartung, Uwe Hernandez Acosta, Eduardo Rodrigues, Joe Osborn, Benedikt Hegner, Pere Mato, Matthew Feickert, Jamie Gooding, Holly Szumila-Vance, Kolja Kauder, Mark Neubauer, Claire Antel, Krzysztof Genser, Tommaso Lari, Steve Mrenna, Benedikt Hegner, Joe Osborn, Juraj Smiesko

Apologies/Contributing: Liz Sexton-Kennedy, Paul Laycock

## News, general matters, announcements

### HSF Joint Workshop with WLCG and HSF Evolution

(Impressions from Graeme - please feel free to add your own)

Overall we felt this was a successful workshop - ~40 people in the room for the software sessions, plus 10-20 on Zoom. A lot of interesting talks and good discussions.

The opening plenary talk on [HSF retrospective and future](https://indico.cern.ch/event/1369601/contributions/5908531/) seemed well received.

The session on [HSF Evolution](https://indico.cern.ch/event/1369601/sessions/536732/#20240514) went pretty well - generally comments were constructive (even when partially critical). See [live notes](https://docs.google.com/document/d/1pJVWsZfTmV-JcmOSrwtstt2jZpIw1L_CjXjU8NTngDI/edit?usp=sharing) for a summary of the discussion.

[Training session](https://indico.cern.ch/event/1369601/sessions/536735/#20240515) had lots of great talks and a good spirit of collaboration. *One of our most appreciated activities!*

For discussion of follow-ups see the [closing slides](https://indico.cern.ch/event/1369601/contributions/5908515/) that Eduardo presented.

Main points:

- Should we have a more formalised time for comments on the proposals?
    - Practically Google Doc comments or by email?
- ~~Coordination Team~~ Steering Group
    - General happiness with the plan...?
    - Rename the Coordination Team to the Steering Group
        - Concretely we can rename hsf-core-coordination to hsf-steering
        - Elect an SG chair
    - Let's repeat here the call for new coordinators!
- Setup the Advisory Group
    - We need to act on who to invite here (experiments plus WLCG at least?)
- Reorganising "Working Groups" and "Activities"
    - Setting up the seminar series seems to get broad support
        - Would help a lot to focus community interest on highlight topics
        - 1x month?
            - How does this play with C&AF and Roundtable?
            - Not clear yet, does need to be re-discussed in the broader context
        - Do not want to "disband" the WGs, we need their expertise
    - In which areas do we really have "working" and which are more like "forums"
        - e.g., the Training WG really work!
            - But what's the best nomenclature?
        - We need input from the WG experts to help organise the seminars
- HSF Affiliated Projects
    - Some interest
    - Would need to **define the criteria** (and do some practical things to generate badges)
    - We need to make some approaches to projects that we think are key to have in this process
    - Project awards (maybe move on this later...?)

## Working Group Updates

### Data Analysis

- DAWG Meeting at 16:00 CET on 10th June '24 dedicated to CMS Combine with talk and discussion from Nick Wardle: https://indico.cern.ch/event/1412073/

### PyHEP

- [PyHEP 2024](https://indico.cern.ch/event/1384010/) (online) (1–4 July, 2024) registration and call for abstracts is open now
    - Call for Abstracts has been extended to **May 31st**.
    - Reviews of abstracts will happen rapidly after to accepted abstracts will have enough time to prepare.
- [PyHEP.dev 2024](https://indico.cern.ch/e/PyHEP2024.dev) (26–30 August, 2024) organisation continues
    - Workshop in-person in Aachen, Germany 

### Detector Simulation

- We held a quite well attended session on “Machine Learning for Detector Simulation”: <https://indico.cern.ch/event/1408850/> on May 6th and the speaker was Kevin Pedro
- A session on "Machine Learning for end-to-end Fast Detector Simulation" to be held on June 3rd: <https://indico.cern.ch/event/1413344/>. It will feature a talk on Lamarr (LHCb oriented application) and FlashSim (CMS oriented application)

### Software Training

- Training Events:
    - May 20-21, [Software Carpentry](https://indico.cern.ch/event/1395323/) (happened this week!). 81 participants registered.
    - Jun 5, [Scikit-hep/ROOT](https://indico.cern.ch/event/1408846/)
    - Sept 25-27, Julia (in person at CERN)
- The pre-CHEP workshop will be an [HSF Training Community Event](https://indico.cern.ch/e/hsftraining2024)

#### C++ Course and Hands-on Training

- An advanced C++ course will be held in fall, exact dates TBD

### Reconstruction and Software Trigger

- First meeting of the year on 4D tracking @ Belle II. Very interesting meeting. Participants numbers on the low side however: 11 total, dominated by ATLAS/ACTS (might have been due to public holiday next day).
- Meeting was recorded - Claire just realised forgot to upload recording. 

### JuliaHEP

- [JuliaHEP WG Meeting](https://indico.cern.ch/event/1388681/) - Thursday May 23, at 17:00 GVA time

- [JuliaHEP 2024 Workshop at CERN](https://indico.cern.ch/e/juliahep2024) (September 30 - October 3):
    - JuliaHEP Training before the workshop (September 25-27)

## Other Interest and Activity Areas

### Analysis Facilities

[Session at the WLCG-HSF workshop](https://indico.cern.ch/event/1369601/timetable/#20240516)

- See the nice [summary](https://indico.cern.ch/event/1369601/contributions/5908516/) by Jamie Gooding

### Compute and Accelerator Forum

[Indico agenda](https://indico.cern.ch/category/12741/)

- 29 May: NVidia Update
- 12 June: AMD GPU roadmap

### Event generators

Graeme and Leif will have a chat with Michelangelo to try and understand the evolving efforts here, supported by the LPCC.

Steve: trying to resurrect "apprentice" as a successor to "professor"; good to see that HDF5 version of LHE files is more prominent (LHEH5, see [talk by Chris](https://indico.cern.ch/event/1369601/contributions/5883607/) at the workshop).

---

## AOB

### ICFA Panel

There was a meeting this week of the new ICFA Panel on Data Lifecycles

- Two [presentations](https://indico.cern.ch/event/1411166/) on training, for HSF/IRIS-HEP (Graeme) and EVERSE (Stefan)

### Website

Graeme had a play with converting the website to run with Hugo or to update the Jekyll theme (currently the very basic `minima`)

- Automatic conversion was not a great success - it really just moves the "posts" into the Hugo `content` folder
- Yes, it's completely possible to do this, but I think it's a week's work to get everything looking good
    - Volunteers...? Anyone have a student who is good with websites?

### Next Meetings

The next meeting will be on [6 June](https://indico.cern.ch/event/1355749/).

Reminder: please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing one of the 2024 meetings.

**We now have a [guide](https://hepsoftwarefoundation.org/organization/running-meetings.html) for running the meeting!**
