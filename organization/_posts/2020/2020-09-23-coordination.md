---
title: "HSF Weekly Meeting #193, 24 September 2020"
layout: plain
---

Present/Contributors: Graeme Stewart, Serhan Mete, Teng Jian Khoo, Paul Laycock, Kyle Knoepfel, Attila Krasznahorkay, Agnieszka Dziurda, Benedikt Hegner, Caterina Doglioni, Chris Jones, David Lange, Eduardo Rodrigues, Gloria Corti, Horst Severini, Liz Sexton-Kennedy

Apologies: Ben Morgan, Witek Porkorski, Andrea Valassi, Stefan Roiser, Michel Jouvin, Josh McFayden

## News, general matters, announcements

### WLCG News

Responding to the LHCC HL-LHC review request to improve coordination and "formalize a role by which the priorities of WLCG can be transmitted to HSF" a new role of "WLCG (Common) Software Liaison" was agreed by the WLCG MB, with this mandate:

> Within the WLCG organisation the (Common) Software Liaisons have the role of ensuring that the development priorities for common software used by the LHC experiments are properly communicated to the appropriate development teams. The projects concerned are those where the LHC experiments rely on software that is developed and maintained outside of the experiment specific domain (e.g. ROOT, Geant4, event generators, CVMFS). The liaisons will specifically communicate with: groups at CERN and in other institutes responsible for the development of this software; the HEP Software Foundation. They will also regularly liaise with the development teams to feedback reports on status and plans.  The liaisons will also ensure that, through the HSF, needs are communicated to the wider HEP software development community. They are also charged with general reporting on common software matters to the WLCG MB and to the LHCC.

> The proposal is to appoint two people to the role of WLCG (Common) Software Liaison for a 1 year term, renewable.

The MB is proposing people for this position now, to appoint people next month.

Q. Is input to this appointment being also given by HSF? There is not so much software expertise in the MB. A. No, although HSF people are on the MB and giving some input with that hat on. We don't anticipate any issues. However, Graeme will pass that feedback to Simone.

### Snowmass

We are collecting a list of HSF Snowmass submissions and LoIs:

- <https://docs.google.com/document/d/1h4uELoWs3Uf0MKDBNW6MnrwS_Uiettui2nlTt8KAtaU/edit?usp=sharing>

Our main HSF submission is now listed on the Snowmass pages:

- <https://snowmass21.org/submissions/compf>

In fact both submissions at the moment are from the HSF.

### New Convenor for Data Analysis WG

Some delay here, but should conclude soon.

### Future Trends in Nuclear Physics Computing, September 29 - October 1, 2020 (Reminder)

Good opportunity to strengthen links to NP community. The first day is focused on common software and would be a great opportunity for members of HSF to contribute.

<https://indico.bnl.gov/event/9023/>

3rd in series of workshops. EIC is a theme this time, which is a well focused community.

### C++ Course (Reminder)

12-16 October, <https://indico.cern.ch/event/946584/>.

50 available places have been taken (within 20 minutes). Another 170 people currently on the waiting list.

Many thanks to all **Volunteers** who offered help for mentoring afternoon hands on sessions. Very nice to receive help throughout the HEP community!! More mentors still welcome (then not every mentor needs to spend the whole week). Please sign up [on this google spreadsheet](https://docs.google.com/spreadsheets/d/14vdf4YC6JvXIF47iTHg7dkNJ3N01PzrnQ8SrsE2wirc/edit?usp=sharing). There is a Doodle for a tutors meeting, linked from the spreadsheet.

Videos will go to YouTube.

### Compute Accelerator Forum (Reminder)

New meeting format to **discuss the fundamental aspects of programming compute accelerators and heterogeneous systems** which apply across application domains. The meeting shall serve as a body to introduce basic concepts, infrastructure and tools and to discuss advanced topics of compute accelerators.

**First meeting next week at 1 October 15:00 CEST**, <https://indico.cern.ch/event/950196/> with presentations on available GPU infrastructure at CERN/IT and WLCG for software engineering and workflow execution.

The first meeting will be recorded for people who cannot attend. During the meeting we will also discuss the least harmful slot for future meetings.

## Website

### Profiles/"floating heads"

Tracked here: <https://github.com/HSF/hsf.github.io/issues/835>

## Working Group Updates

### Data Analysis

Waiting for new convenor before making concrete plans.

### Detector Simulation

Will get started organising for November workshop and for LPCC simulation workshop. Due to the density of events in the near future we are not planning WG meeting: we will send a message to the group outlining the plan.

### Reconstruction and Software Triggers

We followed up on organizing a reco/trigger area in github as discussed in the last coordination meeting. It is here: <https://github.com/HSF-reco-and-software-triggers>.

### Software Tools and Packaging

- **Next WG meeting on September 30th, 2020 5pm CERN time:**
  - Agenda at: <https://indico.cern.ch/event/956862/>
  - Topic: An Introduction to Modern CMake
  - Speaker: Henry Fredrick Schreiner
- Possible topics for upcoming meetings:
  - Spack: Update from Key4HEP and FNAL, others?
  - Tutorial: Packaging software with Conda
  - To be followed up with the relevant people...
  - **Other ideas are most welcome!**

- Follow up after meeting with Acts colleagues and Eigen

### Event generators

Will start organising November workshop.

### Frameworks

We will be [meeting next week](https://indico.cern.ch/event/958266/) to discuss ATLAS's recent metadata considerations in the context of multi-threading.  We are lining up other talks related CMS' handling of non-event data, and the LHCb Allen framework's GPU processing.

## Other Interest and Activity Areas

### Quantum Computing

Author of Qibo toolkit contacted us (<https://github.com/Quantum-TII/qibo>). Followup discussions with openlab.

---

## Workshops

### HSF-WLCG Virtual November Workshop

We have a [draft Indico site](https://indico.cern.ch/event/941278/) up with more details of the event we're planning.

Dates remain the same: 19, 20, 23, 24 November (Thursday, Friday, Monday, Tuesday). Times are rather asymmetric (3, 2, 3, 2.5 hours proposed).

#### Main points

- Organisation team remains much the same as before (Caterina, David, Graeme, Michel)
- We foresee two tracks, software and computing, this time, rather than fully plenary sessions.

#### Sessions

- General Software Plenary
  - Updates from specific working groups and activity areas, e.g., PyHEP, Training, Differentiable Computing, Packaging, ...
  - Please make suggestions to the organisers (or just add them to the meeting notes..)
- Event Generation
  - Organised by Physics Generators WG (Efe, Andrea, Josh)
- Detector Simulation
  - Co-organised with Geant4 R&D (Witek, Gloria, Philippe + Jonathan Madsen (LBNL))
- Open Session

For the Open Session we decided to make a *call for abstracts*. The intention is to increase the participation of younger colleagues and reach out to projects that we have little contact with, or just don't know at all. Try to position the HSF as a good forum in which to present and discuss work.

- We never did this before, but we think it's worth a try
- Time is very short, so we need to get this call out ~now, and have a deadline 4 weeks before the event (23 October)
  - Need to balance time to prepare input against time to accept and then write contributions
  - We hope this works with experiment Speakers' Committees (it's only an abstract, initially)

To try and give at least some guidance, the following themes were suggested:

- Use of accelerated computing devices to help with HEP data processing
- Novel techniques to handle massive event datasets
- Making analysis easier for physicists
- Innovative algorithms for scaling and parallelism

Anything to add? Remove?

### PRACE-CERN-GÉANT-SKAO kick-off workshop on High Performance Computing

"The workshop will identify the challenges in facing HPC integration. After a general introduction on overall goals we will have detailed discussions on the areas of work and related technical demonstrators.  The event will focus on discussions and team-forming around four areas of work: training and center of expertise, authorisation and authentication, benchmarking and data access."

<https://indico.cern.ch/event/952623/>

This is an open meeting. Stefan and Graeme will present the CERN/HSF training needs.

## AOB

### Coordination Group

We welcome Andreas Morsch (ALICE) to the group.

### Next Meeting

- We're back to the normal schedule now, so the next meeting will be 8 October.
