---
title: "HSF Coordination Meeting #289, 5 June 2025"
layout: plain_toc
---

# Attending

Present/Contributing: Torre Wenaus, Eduardo Rodrigues, Liz Sexton-Kennedy, Michel Jouvin, Tommaso Lari, Luke Kreczko, Michel Villanueva, Pere Mato, Inês Ochoa, Joe Osborn, Sapta Battacharya, Claire Antel

Apologies/Contributing: 

## News, general matters, announcements

- It was decided last time that a common stand-alone library for physical constants would be a good topic for HSF to address, Graeme to organize a follow-up meeting.

### European Strategy Update (EPPSU) final stages

Progress on submission to EPJC? As discussed it will be submitted as an editorial. Will be finished off and submitted ASAP.

### LHCC Meeting

Eduardo  [prepared and presented](https://docs.google.com/presentation/d/1A9iOPT9s54-B3yirfThaELAmQ0iI9guhiD6jeNS02o4/edit?usp=sharing) the report for the LHCC referees meeting that took place on 3 June.

The feedback was very positive. Specific questions/feedback to us:

- Training from the general Scientific Python stack and other relevant groups: how to engage better and bring courses on their libraries to HEP? To be discussed within the training group.
- The news from the Scikit-HEP project, which is part of the first 2 domain stacks to integrate their core projects, are very welcomed and good to hear. In general, how to improve HEP engagement with Scientific Python?
- AI/ML is ever more important and ubiquitous, yet the HSF has no activity area around it. Furthermore, most ML is Python after all, and Python is big in the HSF. Is it purely historical or …? Has the HSF thought of engaging strongly with the IML group or even bring it to the HSF?
- Discussion on SWIFT-HEP raised by LHCC - no Phase-2 funding will affect some people’s funding and community efforts to work together between institutes.

### IRIS-HEP Steering Board

Caterina Doglioni as the new HSF representative at IRIS-HEP is preparing [slides](https://docs.google.com/presentation/d/1zrV0P_kIDxwDS9bZsYYE6S3HXPUsaEXfKkQUYr8EjmA/edit?usp=sharing) from the HSF for the meeting now postponed to June 17th.

### HSF Seminar Series and Compute Accelerator Forum

Recent and planned seminars:

- 28th May, 16h30 CEST: Seminar on AdePT and Celeritas update on detector simulation with GPUs. <https://indico.cern.ch/event/1528440/>
- 4 June, 16h30 CEST: AI-assisted software tools. <https://indico.cern.ch/event/1549643/>
- 11 June, 16h30 CEST: Julia on GPUs for fun and profit. <https://indico.cern.ch/event/1472683/>
    - This event co-organised with the [EVERSE Network](https://everse.software/network/)

Venice workshop report tentatively scheduled for September. dCache project have signalled interest in presenting in a future Seminar.

HSF seminar conveners are reachable at <mailto:hsf-seminar-conveners@googlegroups.com>

* Please send your suggestions for next seminars

Conveners plan to work with CAF conveners for a better co-organisation of these 2 events: hope to see some concrete steps next Fall.

### Steering Group

The SG met on Monday 3 June, <https://indico.cern.ch/event/1550243/>. Minutes will be available later.

Graeme will step down at the end of the month. Election for a new (co-)chair(s) just started.

SG will contact the IML and EUCAIF to see what kind of stronger engagement/collaboration is viable.

Project affiliation - decided after feedback to stop the gold/silver/bronze distinctions, just a basic badge. And possibly add topical badges later.

* Well received by the projects we met since then

### HSF Affiliated Projects and Software

ACTS: Graeme and Michel attended the last ACTS weekly developer meeting.

* Graeme presented HSF Project Affiliation and the recent evolution (suppression of badge levels)
* Very positive feedback from all the persons present: waiting for the formal answer but no real uncertainty!
* Main discussion was about the benefit of affiliaton for large projects
    * We realized that we probably forget to mention that this project affiliation is part of our effort to build a community around software and that the participation of large HEP SW projects is important for us too!
* They mention that one thing that HSF affiliation could bring to large project, if they want, is an "external view" by people from the same community
    * Could for example be done through the participation to a project advisory board: ACTS would be particularly interested in this

## Activities Updates

### Software Training

Future events:

- [HSF/IRIS-HEP Software Basics Training (Hybrid)](https://indico.cern.ch/event/1516608/) - Jun 18-20. Hybrid at CERN. Registration is open!
    - Have a good number of people both local and remote for helping, based in current number of registered participants 
- [Deep Learning Train-the-Trainer Workshop](https://indico.desy.de/event/47263/) - Sept 15-19. Organized by the HSF and ErUM-Data-Hub. In-person in Potsdam. Registration is open! Deadline: August 4
    - For people with experience who want to upskill teach techniques

### Physics Generators

- Negative weights workshop: [indico](https://indico.cern.ch/event/1501347/timetable/#20250505.detailed) (maybe we can invite Jeppe to give us a summary)
- Optimising Floating Point Precision Workshop: [indico](https://indico.cern.ch/event/1538409/overview)

Topic of generators in the neutrino community would be interesting.

Website still needs to be updated with current convener names.

Monte Carlo WG is starting a new subgroup to discuss the following issues: “Data Sharing and New Workflows” in the context of event generation.

- The sharing of *particle-level* event samples (i.e. after shower and
 hadronisation) to reduce duplicated efforts between experiments. This is not
 a new discussion, but it makes sense in my opinion to follow up on it as
 part of this WG (sub)group. What is the status of such efforts? Can we do
 more/better? Are there technical stumbling blocks? Is there something to be
 done on the generators’ side to facilitate this?

- The sharing of *parton-level* event samples (i.e. before the parton shower).
 This would allow for a more factorised event generation workflow, where
 off-the-shelf unweighted parton-level samples can be used as input for
 different shower and hadronisation models. A separate generation of large
 parton-level samples requires (not much) storage and easy deployment to WLCG
 event generation jobs. Some generators already support such a workflow.

- Such a factorised event generation workflow would also enable easy HPC/GPU
 off-loading to reduce the event generation computing footprint on the WLCG.
 Novel HPC/GPU-accelerated parton-level MC generators have recently been
 released (MadGraph4GPU, Sherpa/Pepper, …) Their deployment on large HPC
 resources is now being tested.

- Which computing/storage/deployment tools and infrastructure are most suitable
 for what job (Zenodo, Rucio, WLCG, HPC, LHEF, HDF5, HepMC3 …)?

- Which MC samples can be shared publicly as Open Data? This would be very
 useful for pheno and ML studies that require very large samples. To maximise
 versatility one might need to identify additional event data entries to be
 stored, as well as metadata, configs, cached MC integration results etc.

### PyHEP

[PyHEP.dev 2025 Workshop](https://indico.cern.ch/event/1515852/) will be held at University of Washington from July 14 to 17.

### JuliaHEP

[JuliaHEP 2025 Workshop](https://indico.cern.ch/event/1488852/) will be held at Princeton from July 28 to 31.
- Abstract submission is still open
    - the number of submissions is approaching that of last year
- Final registration deadline: July 7 

### GSoC program 2025

## AOB

### Next Meeting

The next coordination meeting will be 19 June, <https://indico.cern.ch/event/1477079/>, and we still need someone to chair! We will then be covered until October.

### Chair This Meeting 👇

Please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing a future coordination meeting. (There is even a [HOWTO guide](https://hepsoftwarefoundation.org/organization/running-meetings.html)).
