---
title: "HSF Coordination Meeting #215, 30 September 2021"
layout: plain_toc
---

Present/Contributing: Graeme Stewart, Serhan Mete, Nicole Skidmore, Attila Krasznahorkay, Eduardo Rodrigues, Krzysztof Genser, Efe Yazgan, Caterina Doglioni, Ben Morgan, Andrea Valassi, Josh McFayden, Michel Jouvin, Liz Sexton-Kennedy, Alexander Moreno, Andi Salzburger, Benedikt Hegner, Michael Hernandez Villanueva, Philippe Canal, Sudhir Malik, Teng Jay Khoo, Daniel Elvira

Apologies: Kyle Knoepfel

## News, general matters, announcements

### HL-LHC Review Phase 2

Editors are now putting the finishing touches to their input documents. They need to be finished *today* for delivery to the reviewers *tomorrow*.

The finished versions are being put into [CERNBox](https://cernbox.cern.ch/index.php/s/QGfcgPkvVsC2p31).

Graeme and Liz wrote a short introduction that summarises the process.

N.B. The review itself will take place 1-5 November, hybrid at CERN + Zoomlandia. Attendance is being clarified with the LHCC.

### CHEP2022 -> CHEP2023

As people will have seen, CHEP has been delayed for a year, to May 2023. This means that we would not have a CHEP-attached WLCG/HSF workshop in May next year.

This gives more scope for smaller (still hybrid) workshops next year; probably even more important to give the community an opportunity for presentations and discussions.

We should gather some ideas of what suitable topics could be and start to discuss sounding things out / organising.

Some ideas:

- Mini-workshop on heterogeneous computing (suggested by Reco + Trigger WG)
- Analysis WS (covering also analysis facilities and HL-LHC analysis needs)

### HSF Letters

Graeme's thoughts:

Had not really considered the HSF letters that would go to an individual before (this issue came up a few weeks ago, we decided not to give a letter of 'support' as this would imply endorsement of an individual, which is not something the HSF is well set up to do).

However, individual applications are an important career step and, in the end, *software is written by individuals, often by ECRs*. We want to foster work on software and improve its recognition.

Proposal for a clarification on letters from the HSF:

- For individual proposals we can write a letter stating if the goals of the proposal are aligned with software needs in HEP (citing CWP and similar)
- If so, we will make this a *letter of collaboration*, i.e., if the proposal is funded we will work with the recipients of the award in the relevant WGs

Such a letter requires a *public project summary* and *clear statement of their intent to work within the HSF*.

Also propose that we make the link to 'letters from the HSF' a bit more prominent - most people don't know that it's there (which may also be why requests invariably come late).

- Discussion on support if people are contributing to HSF projects
  - Not clear what constitutes an 'HSF project' here
  - We did try to develop the project model early in the HSF, but it never really worked as we hoped (how to reinvigorate it is an ongoing topic)
  - There are many projects that pre-date HSF and have their own ownership and lifecycle, which address really important topics for the community
  - Do not bind these things together too tightly (though we continue to encourage projects to identify with the HSF)

- Graeme will prepare a PR with changes that can be approved next meeting

### Geant4

- News from Geant4
  - Proposal to have a more open development model (with approved contributors, not fully open) has been put forward
  - Ben, Graeme and Liz spoke supportively of the proposal

## Working Group Updates

### Data Analysis

[Meeting scheduled](https://indico.cern.ch/event/1081616/) on Wednesday 6th October at 17:00 (CET) - email reminder sent out

We will discuss

- Finalisation of ["HSF Metadata System Requirements" document](https://docs.google.com/document/d/1zT5tPCtiNfuRm8ywKNbaNGvXGtCZYaO-GOj77pV2BEY)
- Developing and expanding [analysis benchmarks](https://github.com/iris-hep/adl-benchmarks-index), also summarising a discussion that took place with IRIS-HEP. Already received emails of interest in respect of fitting benchmarks

### Detector Simulation

Closely allied meeting at 17h CET today:

- *Transport methods for simulation-based inference*, Youssef Marzouk (MIT)
- <https://indico.cern.ch/event/1073290/>
- Part of the MLSim meeting series

WG still looking for available speakers; Trying not to overlap (in topics and time) with other events (e.g., Geant4 Collaboration Meeting ended on 24th of September, which included an open R&D Session)

### Reconstruction and Software Triggers

Not much news from Reconstruction & SW trigger

- large part of community is really tied up in Run-3 preparation
- should try for a higher level of engagement with the community outside LHC

### PyHEP

- *Python Module of the Month* meetings to restart in October. Announcement to go out shortly.
- First [Julia in HEP mini-workshop](https://indico.cern.ch/event/1074269/) took place last Monday.
  - Very well attended - we expected ~20 participants but over 80 subscribed.
  - Minutes are available on the Indico page.
  - There will be a report written in the next 2-3 months. Open to contributions. Register to the workshop if you want to receive information on how to contribute.

- Feedback
  - There was not enough time for discussion, and many interesting points were raised, but not explored properly
  - Too much of a focus on *could we do `X` in Julia?*, to which the answer is invariably *yes* as it's a Turing complete language
    - Have to answer the question *do we want to?*
    - Would like to explore the possibilities of Julia's features like composability, double dispatch, higher development productivity, ... **Are these compelling?**

### Software Tools and Packaging

We have the next WG meeting scheduled:

- Date: 20 Oct 2021, 18:00 (CEST)
- Topic: The Future of Spack
- Speaker: Dr. Todd Gamblin (Lawrence Livermore National Laboratory)
- Agenda: <https://indico.cern.ch/event/1078600/>

### Software Training

- CSBS paper accepted after a second version was submitted, with the suggestions from the referees implemented.
  - [arXiv:2103.00659 [hep-ex]](https://arxiv.org/abs/2103.00659)
- Next Software Carpentries workshop in preparation (Dec 13-15, 2021).
  - First workshop gave us experience to improve the pre and post surveys, and the prerequisites for the attendees.
- Invitation to participate in the IRIS-HEP Analysis Grand Challenge (AGC) Tools 2021 Workshop, circulated with different experiments.
  - <https://indico.cern.ch/event/1076231/>
  - Aiming to cover tools in development for the future of distributed computing technologies.

### Event Generators

- Not much to update. Very busy finishing implementing comments received on the LHCC Review document. Now finished and uploaded to CERNBox, and to arXiv!

### Frameworks

- We will have a meeting next week (agenda to be set up very soon), looking at ATLAS's monitoring framework/code. Will continue in the following weeks with meetings about "event batching" in Gaudi, and a discussion about event overlay in ATLAS.

## Other Interest and Activity Areas

### Licensing

Continuing discussion with the HepMC3 authors.

---

## AOB

### SIDIS COST Proposal

The SIDIS COST proposal draft has been circulated and is attracting comments and being improved. Contact Graeme, Stefan or Caterina if you would like to be involved.

### HSF Calendar

As dates start to be fixed for 2022, please add things to the HSF Community Calendar.

### Next Meeting

Next meeting is on 14 October.
