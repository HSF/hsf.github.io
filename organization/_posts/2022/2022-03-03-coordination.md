---
title: "HSF Coordination Meeting #224, 3 March 2022"
layout: plain_toc
---

Present/Contributing: Graeme Stewart, Serhan Mete, Stefan Roiser, Dorothea vom Bruch, Markus Diefenthaler, Efe Yazgan, Pere Mato, Ben Morgan, Nicole Skidmore, Kyle Knoepfel, Krzysztof Genser, Wouter Deconinck, Matti Kortelainen, Allie Hall, Josh McFayden, Mark Neubauer, Valentin Volkl, Alexander Moreno

Apologies/Contributing: Eduardo Rodrigues, Benedikt Hegner

## News, general matters, announcements

### LHCC

There is another meeting with the LHCC referees next week (Tuesday 8). Can WGs please send a short summary of activity and plans to Graeme and Liz by tomorrow?

Draft presentation will be ready on Monday 7.

### Workshops in 2022

#### Analysis Ecosystems Workshop

23-25 May: <https://indico.cern.ch/e/aew2>

**Registration is opened!** At the moment we have limited this to 80 in-person places.

Thanks to the support of IRIS-HEP, CERN/HSF and IJCLab we do not require a registration fee - coffee/tea and lunches will be covered.

Investigating support for dinner (IRIS-HEP, CERN/HSF, possibly external sponsors), but maximum cost of around €50 per person.

We have a better overview description of the workshop now. Announcement has been sent out to LHC experiments, Belle II, DUNE, EIC, GDB, CERN IT, etc.

Content planning is progressing well, we have session convenors for most of the headline topics:

- Analysis Facilities: Oksana Shadura, Nicole Skidmore
- ML tools and differentiable computing workflows: Lukas Heinrich, Nathan Simpson
- “Real-time” trigger-level analysis: Giulio Eulisse, LHCb mystery guest
- Analysis User Experience and Declarative Languages: Jonas Rembser, Alex Held
- Analysis on reduced formats or specialist inputs: Allie Hall, +others
- Bookkeeping and systematics handling: TJ Khoo, Paul Laycock

Next organising meeting 10 March, identifying key questions on the topics - focus on outcomes.

#### Detector Simulation on GPU Community Meeting

3-6 May: <https://indico.cern.ch/e/simgpu>

Stub agenda for now (N.B., this meeting is virtual).

### Google Summer of Code

HSF call for proposals was sent a few weeks ago. Deadline for project proposals was Feb 25.

We have 39 proposals from 18 projects, covering 25 organisations.

### Snowmass

A small team (inc. Graeme and Paul) have helped draft a document with WLCG for submission to Snowmass. The draft should be ready for circulation soon.

### HSF History Paper

As reported a few weeks ago, we gave input to Dan Katz re. developing scientific software communities. This summarised the origins and history of the HSF.

The text we wrote is [here](https://docs.google.com/document/d/1y45VSJeUZQnxgk7UMrLpVX4VhWtwYvp1sqz6Hp3dN1g/edit?usp=sharing). It has ended up a very nice summary of our origins, so we would like to publish it. Can people take a look and we shall upload a version of this to Zenodo?

## Working Group Updates

### General

- There is a summary of our [2022 planning as a PR](https://github.com/HSF/hsf.github.io/pull/1057)
- Please comment by tomorrow, when it will be merged!

### Data Analysis

- Metadata paper has been [submitted to ArXiv](https://arxiv.org/abs/2203.00463)
  - Email sent to authors with instructions on how to claim paper ownership

### Detector Simulation

- Confirming previously scheduled meeting on MARS
- Looking at other meeting ideas
  - Contacting DD4Hep developers on possibility of topical status/use meeting
    - Also interesting for reconstruction geometry and links between these use cases
  - Discussing ML-related topics

### Reconstruction and Software Trigger

- Next topical meetings:
  - 9 March: Jointly with CAF: Parallelised reconstruction on GPUs <https://indico.cern.ch/event/1073640/>
  - 16 March: 4D reconstruction @ sPHENIX and LHCb: <https://indico.cern.ch/event/1128087/>
  - Plan for April: RICH reconstruction
  - Plan for May: AI in reconstruction (Summary of learning to discover workshop)

### PyHEP

- We had yesterday the first topical meeting of 2022!
  - Topic was histogramming (`boost-histogram` and `Hist` packages).
  - See [Indico agenda](https://indico.cern.ch/event/1133099/).

### Software Tools and Packaging

- We had a constructive meeting with the conveners of the Frameworks WG last week
  - The idea is to host a series of meetings in the upcoming weeks/months on Modern C++
  - First invitation was sent today to Axel for a talk on the latest news from the ISO C++ standards and/or reflection
  - We also identified a number of additional topics/speakers and will be following up on those soon.

### Event Generators

- Snowmass doc for event generators will be circulated within the WG soon.
- [WG Meeting next week Thursday at 16:00](https://indico.cern.ch/event/1135424/) with a contribution from Stefan Hoeche on the "Discussion of the Snowmass white paper on event generators".
- TBA - (invited for 24th March) Recent [ATLAS V+jets paper](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/PMGR-2021-01) (possibly including related recent Sherpa efficiency improvements).
- TBA - MC4EIC and MCEGs for the EIC
- TBA - MCEGs for neutrino experiments

### Frameworks

- We met with Software Tools and Packaging to discuss modern C++ (see above)
- Yesterday we discussed some features of C++20---there were about 45 participants including attendees of multiple WGs
- Excellent discussion with invitation from Software Training to see what type of framework training can be developed

- Our next WG meeting is tentatively Wednesday, April 6---we hope to secure a talk from a smaller experiment.

### Software Training

- SW Carpentry + ROOT/uproot training workshop March 28-30, <https://indico.cern.ch/event/1112526/>, locking in instructors now
- Planning for Matplotlib tutorial in ~April
- Starting to plan an update to HSF Training Survey
- Ongoing weekly meetings on Monday 16 CET
- C++ Fundamentals training 15-17 March, <https://indico.cern.ch/event/1119339/>
  - Anybody interested in upcoming courses please register on the "Waiting List" of this course, we shall send info to the members

## Other Interest and Activity Areas

### Analysis Facilities

- Activity page live!
  - <https://hepsoftwarefoundation.org/activities/analysisfacilitiesforum.html>
  - See details for Google groups, Mattermost, ..
- Kick-off meeting arranged for 25 March:
  - <https://indico.cern.ch/event/1132360/>

---

## AOB

### Calendar

Q. How do we setup the HSF calendar?

- There is a normal Google Calendar, in which any events can be added directly; there is also an Indico sync script that added events from the HSF Indico area, see <https://github.com/HSF/merge2gcal> (this is far superior to adding things by hand...)

### Next Meeting

Next coordination meeting is scheduled for 17 March.
