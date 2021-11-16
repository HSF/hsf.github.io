---
title: "HSF Coordination Meeting #218, 11 November 2021"
layout: plain_toc
---

Present/Contributing: Eduardo Rodrigues, Josh McFayden, Michel Hernandez Villanueva, Serhan Mete, Efe Yazgan, Nicole Skidmore, Krzysztof Genser, Marc Paterno, Kyle Knoepfel, Alexander Moreno, Philippe Canal, Daniel Elvira

Apologies/Contributing: Graeme Stewart, Pere Mato, Benedikt Hegner, Caterina Doglioni, Ben Morgan, Liz Sexton-Kennedy

## News, general matters, announcements

### LHCC

#### HL-LHC Review Phase 2

The HL-LHC review took place last week. There was good discussion on many points after interesting questions from the reviewers. We expect that there will be an internally circulated first draft report in December, followed by a final report in January.

The reviewers thanked a lot those involved in preparing the documents - as do Graeme and Liz!

#### LHCC Referees Meeting

There is the usual quarterly meeting between the LHCC Referees and WLCG on Tuesday 16 November, next week. We are asked for a *short* (15' + 5') update on software projects and the HSF. There is a focus on any activities relevant for Run3.

Please send any relevant points to Graeme and Liz by tomorrow, 12 November. Expect draft slides on Monday 15.

### HSF Talks

#### SWIFT-HEP

Caterina gave the [HSF talk](https://indico.cern.ch/event/1033028/contributions/4551806/attachments/2337826/3985074/20211102%20-%20SwiftHEP_Excalibur%20-%20HSF-6.pdf) at the SWIFT-HEP meeting last week.

Q&A:

- _Is there any effort on sharing control board software?_ The answer here was that HSF is not covering this topic, but if anyone is interested we can exchange contacts.
- _Can we organize / benefit from joint training activities?_ Davide Costanzo flagged a call (for UK institutes but with virtual participation we can do joint things):  <https://www.ukri.org/opportunity/support-the-development-of-research-software-engineering/>. Caterina is following up in a thread with Ben Morgan and Tim Scanlon; let her know if you'd like to be added in the thread.

#### ILCX

Graeme gave an [HSF talk](https://agenda.linearcollider.org/event/9211/contributions/49168/) to the ILC community two weeks ago. Well received, with some discussion on if linear colliders really can share software with the LHC community (our answer: *yes, albeit that tracking and pattern matching algorithms are at a different working point to hadronic experiments, there is still a huge amount of potentially shareable software*).

#### Snowmass Small Experiments Workshop

There is a Snowmass Small Experiments Workshop [next week](https://indico.physics.lbl.gov/event/1756/overview). Liz will give an HSF talk.

### ASCR Workshop on the Science of Scientific-Software Development and Use

There is a DOE supported [ASCR workshop](https://web.cvent.com/event/1b7d7c3a-e9b4-409d-ae2b-284779cfe72f/summary) 13-15 December on scientific software. There is a call for [position papers](https://web.cvent.com/event/1b7d7c3a-e9b4-409d-ae2b-284779cfe72f/websitePage:5c30ffe5-b577-491f-8d8d-1f745b03e9ec): *We invite community input in the form of **two-page position** papers that identify and discuss key challenges and opportunities in the science of the scientific-software development process and the study of the use of scientific software.*

Should we put in an HSF paper for this? N.B. Deadline is 19 November. (The last similar paper we submitted was to the European Strategy Process, <https://zenodo.org/record/2413005>, could be a template?)

- Seems a good idea but we would need to identify somebody to push that through.

## Working Group Updates

### Mandates for 2022

We have started to think about WG convenerships for 2022. For WG convenors, please let Benedikt know your plans.

- Normally WG conveners serve for 2 years, by mutual agreement (but this is not set in stone).
- So far, all but 8 convenors answered. Most want to continue (even beyond 2 years). Some would make space for younger replacements if there are.

### Data Analysis

[Meeting](https://indico.cern.ch/event/1094888/) yesterday on "Expanding analysis benchmarks" with a talk from LHCb analysts on fitting.

- Will follow up on [live notes](https://docs.google.com/document/d/15z2bO8BFFLarqRiEiKdvxCRPj5nX8H4l-lbnQgR3FFY/edit#) and in a future meeting to discuss if we can establish suitable fitting benchmarks
- Ran out of time to discuss workflow benchmarks - asked people to refer and contribute to [previous live notes](https://docs.google.com/document/d/10XVZm859rjRudImRGtcyKKWFhPLzPVGdr0T4w3Eriqg/edit#heading=h.hcubs8cy4y7c) which will be consolidated and discussed at the next meeting.

Potential future topic - running analysis software on GPUs.

### Detector Simulation

- Held a session on New ML Techniques for Simulation last Monday <https://indico.cern.ch/event/1089895>
- Scheduled a session on using FPGAs for simulation on December 13th.

### Reconstruction and Software Triggers

- NTR

### PyHEP

- LHCC HL-LHC Review: presentation of and discussion around "Data Science Tools for Analysis" seemed very positive to us. Looking forward to the LHCC feedback.

### Software Tools and Packaging

- Serhan and Marc had a meeting last week to discuss what (if anything) can (needs to) be done from our WG side for the Anaconda licensing issue. The current goal is to have a topical WG meeting (TBC) to discuss user experience on porting code from Anaconda to open-source alternatives (at least Marc has some). Apart from that, of course this is overall a complex legal issue that involves money at the end. We think that those aspects are beyond the scope of our WG (possibly even HSF).

### Software Training

- Training Challenge was held on Nov 1st, with participation from several collaborations. Main points discussing:
  - How to get people involved in training activities and get useful feedback from students (surveys, PRs, comments).
  - Recruit people to create training content and ensure maintenance.
  - How to add new technologies in training.
  - Collaboration between experiments and with non-HEP groups (Carpentries, Universities).
- Software Carpentries Workshop to be held on Dec 13 - 15.
  - Instructors from the Carpentries have been appointed for the event.
  - Prerequisites for students being recorded and will be available in advance.
  - Indico page in preparation.
- ACAT abstract related to Training in HSF accepted as poster.

### Event Generators

- LHCC HL-LHC Review: Presentation and discussion last week. Seemed to go well; the efforts of the HSF WG was appreciated and we were thanked for the quality of the review document. We wait to see what will be written in the report :smiley:.
- There was a [meeting](https://indico.cern.ch/event/1078675) "ECFA Higgs Factories: 1st Topical Meeting on Generators" where, amongst other things, there was:
  - A presentation from Andrea on the MG4GPU developments.
  - A presentation from Michelangelo Mangano (MLM) on the “Future Colliders Unit" at CERN. Could overlap somewhat with our WG activities:
    - "development/validation of MC tools & calculations for future ee colliders: develop LesHouches-like accords to streamline sharing of matrix-element (ME) and MC events, ME calculations, facilitate interoperability and comparison of tools?"
    - We're planning to reach out to MLM.

### Frameworks

Still have not scheduled our next meeting, but we will aim for at least one more before 2022.

---

## AOB

### HSF Calendar

HSF calendar now should be complete with LHC experiments, DUNE events, major conferences - thanks to Pete, Eduardo, Graeme, Stefano and Paul for helping. However, please double check and add anything that's missing (e.g. Belle II).

### SIDIS EU COST Funding proposal

SIDIS COST proposal was submitted last month.

### Next Meeting

Next meeting 25 November. (Thanksgiving - will we be quorate?)
