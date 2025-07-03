---
title: "HSF Coordination Meeting #291, 3 July 2025"
layout: plain_toc
---

## Attending

Present/Contributing: Graeme Stewart, Peter Fackeldey, Eduardo Rodrigues, Ines Ochoa, Ianna Osborne, Joe Osborn, Torre Wenaus, Valentin Volkl, Saptaparna Battacharya, Liz Sexton-Kennedy, Michel Hernandez Villanueva, Pere Mato, Michel Jouvin, Luke Kreczko, Juan Miguel Carceller, Alexander Moreno, Mark Neubauer, Claire Antel, Maciej Pawel Szymanski

Apologies/Contributing:

## News, general matters, announcements

### Letter of Cooperation for CAREER

Eduardo has circulated a [draft letter](https://docs.google.com/document/d/1vs3TSsqPIqkJ_iqxRiqKXc4wyMpO889aTR7a4q8qpfM/edit?usp=sharing) of cooperation for the NSF proposal *CAREER: Exploring Exotic and Rare Processes with New Hardware Trigger Tools at ATLAS* from Ben Carlson.

*The meeting approved the letter.*

### European Strategy Update (EPPSU) 

Computing session at Venice went very well:

- Presentation on various aspects during the 3 hour parallel session
- 2 talks during the plenary session, one about HL-LHC, one about future beyond it
  - Parallel session slides: <https://agenda.infn.it/event/44943/sessions/33815/#20250623> and <https://agenda.infn.it/event/44943/sessions/33818/#20250623>
  - Plenary session slides: <https://agenda.infn.it/event/44943/sessions/32614/#20250626>
  - Plenary also has video save to YouTube here: <https://www.youtube.com/live/7MtB0CXIr_Y?feature=shared>

WLCG noted that current projections for computing needs will not fit into "flat budget" - so more software R&D is needed. Tommaso also noted that little concrete progress had been made with careers.

Our EPPSU submission has been submitted EPJ-C.

### IRIS-HEP Steering Board

Caterina Doglioni is the new HSF representative at IRIS-HEP is preparing [slides](https://docs.google.com/presentation/d/1zrV0P_kIDxwDS9bZsYYE6S3HXPUsaEXfKkQUYr8EjmA/edit?usp=sharing) from the HSF. The presentation is scheduled on July 15.

### HSF Seminar Series and Compute Accelerator Forum

Venice workshop report tentatively scheduled for September. dCache project have signalled interest in presenting in a future Seminar. A seminar on HS3 will be organised also in the future.

How to format "seminar" on Venice symposium?

- Engaging discussion, or..
- (unbiased) report of highlights and key statements?
- Suggest inviting Borut and/or Tommaso for this to give a summary of the outcomes and main messages (and they may prefer October, after the briefing book?)

HSF seminar conveners are reachable at <mailto:hsf-seminar-conveners@googlegroups.com>

- Please send your suggestions for next seminars, **particularly from the activity areas**.

### Steering Group

Eduardo Rodrigues has been elected the new HSF Steering Group chair, effective 1 July. Congratulations to Eduardo and thanks for taking on this important role!

A HUGE thanks again to Graeme for being SG chair for the past year and for all his (long-standing) impactful commitment!

- There will be a SG meeting soon in July. Then back in September.

### HSF Affiliated Projects and Software

We will work on a new version of the project affiliation (streamlined, no bronze, silver, gold) - will be circulated for discussion when it's ready.

## Activities Updates

### Software Training

- [Hackathon](https://indico.cern.ch/event/1565267/) on [Databases for HEP](https://hsf-training.github.io/hsf-training-databases-basics/index.html) on July 7.
    - Finishing the chapters, giving some consistency between examples and exercises
    - We will try to develop a bonus chapter on Grafana dashboards
    - Switching from "old" Carpentries style to JupyterBook

- [Deep Learning Train-the-Trainer Workshop](https://indico.desy.de/event/47263/) - Sept 15-19.
    - Organized by the HSF and ErUM-Data-Hub
    - In-person in Potsdam
    - Registration is still open! Deadline: August 4. 17 people registered!

### PyHEP

- [PyHEP.dev 2025 workshop](https://indico.cern.ch/e/PyHEP2025.dev) organisation being finalised:
    - More than 30 participants confirmed
    - 12 abstracts accepted
    - Talks in the mornings, discussions & hacking sessions in the afternoons
    - Registration & abstract submission closes tomorrow, timetable will be finalized right after

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
        - Keynote Talk: Stefan Karpinksi

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
    - Training group have some suitable material, will arrange details offline

### Event generators

- Event generators for FCC-ee/Higgs factory:

Enrico Bothmann will talk about Sherpa for FCC-ee on July 24th at 17:00 CERN. Indico agenda will be available soon. 

## AOB

### Physical Constants / HEPdata Library

Reminder: we are proposing a C++ header-only library that defines physical constants and some salient HEPdata in a lightweight, eaasy-to-use manner. Also taking into account versioning.

We are discussing a next meeting for this, probably next week. Please let Graeme know if you'd like to be kept in the loop.

### NGT/openlab Optimising Floating Point Computation

Very interesting workshop - a particular highlight was work on emulating FP32, FP64 with lower precision types (like bFloat16).

Enrico Bothmann also gave an excellent talk explaining how the mathematics of event generation give rise to stringent requirements on numerical precision.

<https://indico.cern.ch/event/1538409/>

### Next Meeting

The next coordination meeting will be 17 July, <https://indico.cern.ch/event/1477081/>, Stefan will chair.

### Chair This Meeting 👇

Please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing a future coordination meeting. (There is even a [HOWTO guide](https://hepsoftwarefoundation.org/organization/running-meetings.html)).
