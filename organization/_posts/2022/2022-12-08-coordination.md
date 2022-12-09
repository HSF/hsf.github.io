---
title: "HSF Coordination Meeting #241, 8 December 2022"
layout: plain_toc
---

## Attending

Present/Contributing: Graeme Stewart, Benedikt Hegner, Stefan Roiser, Andrea Valassi, Eduardo Rodrigues, Stephan Hageböck, Allison Hall, Jin Huang, Kyle Knoepfel, Krzysztof Genser, Matti Kortelainen, Liz Sexton-Kennedy, Pere Mato, Josh McFayden, Juraj Smiesko

Apologies/Contributing: Michel Villanueva, Paul Laycock, Dorothea von Bruch

## News, general matters, announcements

### Analysis Ecosystems II Workshop Report

This is now ready in its beautiful LaTeX version and ready to be uploaded to arXiv with the full list of authors.

### ESCAPE OSSR Workshop

Our colleagues in the ESCAPE project invited Graeme to give a talk about aligned HSF activities at their [workshop last week](https://indico.in2p3.fr/event/27630/). The [presentation](https://indico.in2p3.fr/event/27630/contributions/117174/) focused on:

- HSF efforts in cataloguing and the knowledge base
- Outcomes and discussion from the Software Citation workshop

ESCAPE is in the process of transitioning from a project to a consortium and we do foresee future cooperation with our colleagues there.

### Pre-CHEP Workshop

Discussing with WLCG colleagues and LHC computing coordinators we have identified topics for a [pre-CHEP workshop](https://indico.cern.ch/e/wlcg-hsf23) on 6-7 May 2023 in Norfolk, VA. Two areas where software and facilities are close are:

- Analysis Facilities
  - Based on the findings of the AFF group (which we asked to draw conclusions after 12-18 months of work).
  - How do workloads evolve? How do sites adapt their offerings? What are the benchmarks of success?
- Non-x86 Computing
  - Increasingly diverse computing architectures at sites, both in CPU flavours (ARM, PowerPC) and accelerators (GPUs, mainly, from different stables).
  - Readiness of experiments to adapt to this new environment, covering development, building, validation, workflow management, etc.

Will communicate this back to local organizers. We don't know how much remote participation will be supported (the CHEP venue contract was signed pre-COVID).

Scientific organising committee needs to be setup soon.

### Letter of Cooperation Request

We have been approached by Mike Sokoloff to provide a [letter of cooperation](https://hepsoftwarefoundation.org/organization/hsf-letters.html) for an NSF proposal to develop massively parallel and high-dimensional fitters.

Unfortunately no public text has been made available.

We are minded to support this, but from the *HSF Coordination Group* instead of the whole HSF? (The coordination group has seen a draft, which we can share on request.) Generally we discourage this, however. A community organisation like the HSF is not well suited to providing support to private proposals.

Liz - if this was a request that can be delivered by the Coordination Group, e.g., a workshop, it might be possible to give limited support. But for the whole of the HSF it's difficult if there is no public document.

Benedikt - coordination team are volunteers, not an executive, not really empowered to take unilateral decisions. Could he make something public just a few days before the deadline.

**Outcome:** we ask Mike to either prepare a public summary or to agree to upload a few days before the submission deadline the proposal. Graeme will communicate this decision back to Mike.

## Working Group Updates

### General

We have concluded on the first round of invitations to new WG conveners. Many people have accepted already and we have quite a few pending responses. Overall we are making good progress and hope to have most of the WGs settled before the break.

We are short of candidates in Tools and Packaging, so if you have names please let us know.

*Reminder:* In January we will have a review of the year gone, as well as looking forward to 2023 - so please think about it.

#### Meetings

*Reminder:* Please try and book meetings in Indico at least 2 weeks in advance!

That way they go into the calendar early and they will be included in the weekly email announcement that goes to HSF Forum.

### Data Analysis

- Work on writing down experiment training efforts will start ~ mid of January since experiment contacts are quite busy. Collaboration with Training WG.
- Abstract submitted to CHEP Track 8: "Training and on-boarding initiatives in HEP"

### Detector Simulation

- Last meeting of the year on 12th December covering Geant4 Hadronic Physics Model Parameter variation
  - <https://indico.cern.ch/event/1216295/>
- Anticipate Geant4 Technical Forum soon covering latest 11.1 release

### Reconstruction and Software Trigger

- Completed two of the three planned topical meetings in the fall series (GNN tracking and RICH PID reco.). Given holiday approaching, the topical meeting on resonance reconstruction may have to start in 2023. Possible talks in this meeting include `DecayTreeFitter` in LHCb, `KFParticle` in CBM/ALICE/STAR/sPHENIX.

### PyHEP

- [Topical meeting](https://indico.cern.ch/event/1222913/) yesterday. The tool *RootInteractive*, from ALICE colleagues, was presented.
- We plan to organise in 2023 some of the meetings jointly with IRIS-HEP, given the regular overlap in terms of topics presented and meeting attendees.

### Software Training

- Couple of abstracts submitted to CHEP (in addition to the one in collaboration with Analysis WG)
  - "Train to sustain", about the effort for training people on writing sustainable software.
  - "Building a Global HEP Software Training Community", about coordination between different training initiatives while building a training center.
- Analysis preservation training hackathon held on Dec 7.
  - Preparation for a training event early next year (Jan 16-21, 2023): <https://indico.cern.ch/event/1219810/>
  - Material for Docker, Singularity/Apptainer, CI/CD almost ready.
  - Invited talk for the training event: preservation on CMS (Clemens Lange).
  - Inviting other speakers. If you are interested in contribute, please let us know.

#### C++ Course and Hands-on Training

Two new courses planned:

- CERN based "Essentials" course for 3 days in the week of 6 - 10 March.
- JLab based course. Tentatively 3 days course in the week after CHEP/Norfolk. Exact content, dates, etc. to be confirmed end of Jan.

## Other Interest and Activity Areas

### Compute Accelerator Forum

- 2022 Calendar
  - Next meeting will be on [ACTS track reconstruction on GPUs](https://indico.cern.ch/event/1160623/), 14 December
- 2023 Calendar
  - [Madgraph5_aMC@NLO](https://indico.cern.ch/event/1207838/), 8 February
  - [Hepix Benchmarking](https://indico.cern.ch/event/1207839/), 8 March

- Do get in touch with Graeme, Ben, Stefan if you have an idea or a topic to present

### Software and Computing Roundtable

- The Software and Computing Roundtable restarts on Dec. 13 with an update on EIC Software. There will be presentations on the [EIC Software: Statement of Principles](https://eic.github.io/activities/principles.html) and the software stack.
- The "Year in Review" event with contributions from the HEP Software Foundation, Brookhaven National Laboratory, and Jefferson Lab will be on Jan. 17.
  - We need to have an HSF speaker - in past years Graeme, Benedikt, Sudhir and Eduardo have given presentations; a "new face" volunteer would be welcome

### HSF-India

January visit to India from key people is going ahead, to gather support for the project. Proper kick off meeting to follow in the Spring. There will also be a talk at the ASGC meeting next year.

---

## AOB

### Linux Future

News hot off the press is that CERN will be recommending and supporting AlmaLinux 8/9 and Red Hat Enterprise Linux 8/9 (moving away from CentOS Stream).

### HSF Calendar

This should be complete - LHCC weeks for 2023 are now added.

### Next Meeting

The first meeting next year is January 19, where we will start by reviewing 2022 and planning for 2023. It would be great to identify a highlight point from each WG, which can be used as a way to communicate the role and effectiveness of the HSF.
