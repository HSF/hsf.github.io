---
title: "HSF Coordination Meeting #292, 17 July 2025"
layout: plain_toc
---

## Attending

Present/Contributing: Claire Antel, Eduardo Rodrigues, Stefan Roiser, Michel Jouvin, Joe Osborn, Juan Miguel Carceller, Fanxin Sun, Michel Hernandez Villanueva, Inês Ochoa, Maarten van Veghel, Saptaparna Bhattacharya

Apologies/Contributing: Graeme Stewart


## News, general matters, announcements

### European Strategy Update (EPPSU) 

Our EPPSU submission has been submitted to EPJ-C.

There were some comments about the use of acronyms, which we should define more clearly (or add a glossary)
* Michel has started to look at it, see [this PR](https://github.com/HSF/EPPSU-2025-Paper/pull/21)
* Probably not finalized before end of August due to the holidays...

### IRIS-HEP Steering Board

Caterina Doglioni as the new HSF representative at IRIS-HEP prepared [slides](https://docs.google.com/presentation/d/1zrV0P_kIDxwDS9bZsYYE6S3HXPUsaEXfKkQUYr8EjmA/edit?usp=sharing) from the HSF. The presentation was on July 15.

### HSF Seminar Series and Compute Accelerator Forum

*HSF seminars*
- HSF seminar on ESSPU & Venice Symposium confirmed: Wed 29th Oct ([indico](https://indico.cern.ch/event/1481829/)), given by Tommaso and/or Borut themselves (conveners of the ESSPU Computing WG)
- Following up on HSF Seminar on "dCache", from the perspective of dCache as a large and successful HEP software project: How is it managed? Would be great to get this scheduled for September.


HSF seminar conveners are reachable at <mailto:hsf-seminar-conveners@googlegroups.com>.

- Please send your suggestions for next seminars

### Steering Group

A SG meeting was held on July 10th:
- Discussion of the proposed update for HSF Affiliated Projects and Software, see below.
- Eduardo Rodrigues's term as WLCG Management Board community software liaison ends in August. Stefan Roiser suggested as new liaison for 2 years, with unanimous support from the SG. WLCG is to choose in the next weeks among candidates.

Back in September after the Summer break.

### HSF Affiliated Projects and Software

A new version of the project affiliation has been prepared - thank you Graeme Stewart! The system of badges has been simplified as per community feedback. Details at:
- <https://hepsoftwarefoundation.org/projects/affiliated.html>
- <https://hepsoftwarefoundation.org/projects/guidelines.html>

Note: you are still welcome to submit any feedback to the SG, as the ideas are not set in stone!

Several projects will be contacted after the Summer.

## Activities Updates

### Software Training

- [HSF/IRIS-HEP Software Basics Training (Virtual)](https://indico.cern.ch/event/1569915/) - 3–5 Sept 2025
    - Covering the basics: bash, git, python, ROOT and Scikit-HEP
    - Some experiments (ATLAS, Belle II) already informed us that they will use the HSF/IRIS-HEP training as prerequisite for their own onboardings
- [Deep Learning Train-the-Trainer Workshop](https://indico.desy.de/event/47263/) - Sept 15-19.
    - Organized by the HSF and ErUM-Data-Hub
    - In-person in Potsdam
    - Registration is still open! Deadline: August 4. 17 people registered!
- We are discussing the organization of a blueprint meeting on AI
    - Brainstorming on [foundation models](https://en.wikipedia.org/wiki/Foundation_model), AI engineering
    - Invite training coordinators from the experiments
    - Aiming to answer 
        - Shall we have a training related to most recent developments, at all?
        - What should we cover? 
        - A list of experts to reach
- Planning for the next C++ advanced training under discussion, likely for [October 27-31](https://indico.cern.ch/event/1549051/).


### PyHEP

- The [PyHEP.dev 2025 workshop](https://indico.cern.ch/e/PyHEP2025.dev) is running this week!
- [PyHEP users (virtual) workshop](https://indico.cern.ch/e/PyHEP2025) (October 27-30, 2025):
    - Need an agenda event created
    - Planning the (invited) talks:
        - Already have one: rabbit - TensorFlow based fitting library (similar to CMS Combine)
        - Columnar analysis with Awkward Array and Uproot 

- PyHEP topical meetings:
    - "NanoAOD and RNTuple - Uproot" talk-discussion involving the analysis and xpog people from LHC experiments lead by Andres Rios-Tascon

### JuliaHEP

- [JuliaHEP 2025 Workshop](https://indico.cern.ch/event/1488852/) will be held at Princeton from July 28 to 31.
    - Final registration deadline: July 7
    - 40 people registered so far
    - 3.5 days
        - ~20 Talks
        - ~4 Tutorials
        - Keynote Talk by Stefan Karpinksi

### Event generators

- Event generators for FCC-ee/Higgs factory:

Enrico Bothmann will talk about Sherpa for FCC-ee on July 24th at 17:00 CERN. Indico agenda now available: https://indico.global/event/15218/

### GSoC program 2025

- 26 GSoC projects ongoing
    - 8 related to EP-SFT
    - wide variety of topics: ML, green software, IT, compression...
- Admins don't have much news - good sign?
- Midterm evaluations for shortest projects approaching (Mid-july)
    - mentors should contact admins if they want an extension
    - should also not be afraid to fail students when it doesn't work out
- We'll invite the students to the SFT induction event next week. (Danilo gives a nice overview over computing in HEP).
    - https://indico.cern.ch/event/1564721/
    - will send out mail soon. Mentors: please forward to gsoc students
- If someone is willing to give a brief introduction to the HSF (and maybe the training program) that would be very welcome.
    - Training group have some suitable material

Reminder: time for submitting proposals for the current year usually starts in January

## AOB

### Physical Constants / HEPdata Library

Reminder: we are proposing a C++ header-only library that defines physical constants and some salient HEPdata in a lightweight, easy-to-use manner. Also taking into account versioning.

Status:
- Thanks to Maciej, we became aware that there is a very promising project which has been proposed for C++ 29 standardisation, https://github.com/mpusz/mp-units, so support units and constants in C++. We think it’s the right approach to investigate this library and see if it would be suitable for our needs. If it is on the road to an stdlib inclusion then that makes it much more future proof that anything we would write ourselves.
- The units support looks very well written and robust, and there are already some HEP relevant constants in the library: https://github.com/mpusz/mp-units/blob/master/src/systems/include/mp-units/systems/hep.h. There is a also a lot of documentation about the motivations and a review of existing solutions and their limitations (e.g., Boost::Units).
- So we’d like to proceed to try and both use this library, extend it to the kind of PDG quantities that we would want.

Please let Graeme know if you'd like to be kept in the loop.

### Next Meeting

The next coordination meeting will be 31 July, <https://indico.cern.ch/event/1477083/>, Caterina will chair. Then back in September.

### Chair This Meeting 👇

Please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing a future coordination meeting. (There is even a [HOWTO guide](https://hepsoftwarefoundation.org/organization/running-meetings.html)).

