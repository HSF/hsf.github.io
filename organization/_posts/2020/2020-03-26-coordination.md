---
title: "HSF Weekly Meeting #183, 26 March, 2020"
layout: meetings
---

# {{page.title}}

Present/Contributors: Graeme Stewart, Caterina Doglioni, Stefan Roiser, Kyle Knoepfel, Attila Krasznahorkay, Eduardo Rodrigues, Serhan Mete, Michel Jouvin, TJ Khoo, Efe Yazgan, Andrea Valassi, Pere Mato, Andrea Rizzi, Horst Severini, Paul Laycock, David Lange, Gloria Corti, Ken Herner, Liz Sexton-Kennedy, Martin Ritter, Serhan Mete, Witek Pokorski, Aman Goel

Apologies: Ben Morgan

## News, general matters

### Discussion with CMS

We were invited by Danilo and Markus to give a talk to CMS in a [session on external projects](https://indico.cern.ch/event/902343/) (along with IRIS-HEP and HEP-CCE)
- Outline of the HSF, motivation and history
- Current structure and activities
- Prospects for future collaboration and impact

### Proto-SIDIS

The "[Software Institute for Data Intensive Sciences (SIDIS)](https://sidis.web.cern.ch/)" is an initiative to establish connections and promote common R&D between software engineers in natural sciences and computer science departments at universities, currently focusing on European partners. SIDIS currently is in a conceptualisation phase. 

The activities of SIDIS are regularly discussed on the **third Wednesday of the month, 10.00 - 11.00 CE(S)T**, in the [SIDIS Coordination meeting](https://indico.cern.ch/category/11734/). The meeting usually contains topics to discuss and is public. If you are interested in a specific topic or SIDIS in general please join. 

Current activities of SIDIS are:
- the "Alpaka training and hackathon (see below)" in collaboration with HSF, Openlab and [CASUS](https://www.hzdr.de/db/Cms?pNid=1227&pLang=en)
- a "Topical Workshop on accelerator programming" tentatively to be held in early December with the goals to
    - Draw a landscape of current national initiatives similar to SIDIS and connecting those
    - Exercise the core idea of SIDIS to connect computer scientists and natural scientists, aiming at interactivity as much as possible
    - Establish common R&D activities amongst computer science and natural science

If you are interested in SIDIS please [subscribe to proto-sidis-concept@cern.ch](https://e-groups.cern.ch/e-groups/EgroupsSubscription.do?egroupName=proto-sidis-concept). In case you don't have a CERN account you need to follow some [special instructions to subscribe](https://sidis.web.cern.ch/node/44). Meetings will be also announced on this list.

### Alpaka training event

This has had to be postponed for now. If you are interested please sign up at <https://indico.cern.ch/event/883212/>. We will inform participants when the new date (tentatively end of June) and format have been decided.


## Google Summer of Code 2020

The GSoC timeline has been updated: <https://summerofcode.withgoogle.com/how-it-works/#timeline>

The student application deadline is still March 31, but the student proposal review period is now March 31-April 20. So the new *deadline for finishing the student evaluations is April 16* (instead of April 10), giving us few days to evaluate the number of slots we need to ask.


## LHCC Review of HL-LHC Software and Computing

*Reminder*: LHCC will review software and computing plans for the HL-LHC, Amber Boehnlein (JLab) will chair. Five 20 page documents provided as input to the committee, from ATLAS, CMS, WLCG, DOMA and from *Common Tools and Community Software* (the HSF takes care of the later)

*Latest News*:
- There will be no face to face meeting, there will be a one day virtual meeting instead
- Present each of the 5 documents (20') + discussion (20')
- Participation: review panel, LHCC chair (Frank Simon), 1-2 people per document (about 25)
- 1 May deadline for the documents is maintained
- Foresee one more virtual meeting in the Autumn, a f2f meeting next year in Q2 2021
    - No news yet on how this affects a common software in-depth review in Autumn 2021

[Document outline](https://docs.google.com/document/d/1ai7m7kFyiGgl2tKralJKyPX6rlD9tffU7B6wPj_vpZU/edit?usp=sharing) has been created and now has a fair amount of material.

*Aim is now to have a reasonable draft by the end of this month, with all sections populated.* This allows for our own review and an alignment with the other documents.

### Introduction

- Some introductory text has been written covering a few topics at high level:
    - Technology Evolution
        - Compute devices and APIs
        - Storage systems
    - Software Tools and Packaging
    - Training
    - Software Distribution (CVMFS)
    - Software Preservation

*Please take a look and decide if we need to expand on any points (but remember the target audience)*

### Event Generators

The draft contribution of the WG has been merged into the full HSF document, although it still needs to receive feedback from all of the WG. Presently 5 pages plus one of references (do others foresee references, too?). This is a shorter version of the draft that was prepared last month, which we plan to complete on the same timescale and upload to arXiv (or submit to a journal).

### Detector Simulation
Draft of the simulation chapter for LHCC review completed and merged into the full HSF document.

### Reconstruction and Software Triggers

Were drafting text in a different document - can now move this into the main document. Contacted more trigger & reco common efforts, most of them have replied / have promised to reply. 


### Data Analysis

Draft added before last meeting, not substantially changed, but a few spots will require further input, notably:
* Discussion of new analysis tools (including PyHep, ROOT developments) to be expanded
* Prospects/R&D section will be updated with information gathered from meetings this Spring including DAWG-DOMA discussions (see below)
* Fact-checking, references, numbers...

### HSF Feedback Process

**Discussion [with CMS](https://indico.cern.ch/event/902139/)** happened on Tuesday 24, points that came up were:

- Is there an overall plan and priority?
    - No and we did not expect to have one at this stage
    - Prioritisation can happen on a profiled basis (invest more in the more expensive areas); *however every experiment is at a different working point, so no one-size-fits-all recommendation*
- HSF should comment on the performance of generators, not on the decisions of the experiments
    - Indeed, but comparison of ATLAS and CMS led to significant insights in this area; it is not a competitive or pejorative comparison - this was the spirit of the study, which was led by ATLAS and CMS generator experts
- WLCG does not foresee 'analysis facilities' being distinguished at the resource accounting level (they stick to the Tier 0/1/2 model)
    - ALICE plans are more for a reduction facility
    - (Graeme personal comment) true analysis facilities are very much at the R&D stage

**Further Feedback**

- Make public release of document at the *beginning of next week* (probably needs some tidying)
    - Commentable in Google Docs
    - WGs can update and resolve comments as they come in; flag up controversial points
- Organise one longer feedback meeting, but also decide in advance what topics need discussion time
- **Proposal:** HSF review and feedback Thursday 16 April, 15-17h
    - In the coordination slot, but out of phase (we know this time is reasonably free from clashes)


## Working Group Updates

### Data Analysis

- Very interesting discussions in the joint meeting with WLCG-DOMA: <https://indico.cern.ch/event/890991/>
    - Would be useful to define benchmarks and inject realism into tests -> will followup (homework for the convenors)
    - Emphasis (rightly) on the streamlined reduction model (nanoAOD, PHYS_LITE), but we need to consider the "10%" that can't fit into that model
    - How will exclusive analysis (e.g. LHCb, Belle II) work, similar?  Or would ServiceX be an even better fit there?
- Analysis language workshop is postponed, hope is still to have a face to face meeting but in "wait and see" mode

### Detector Simulation
Topical [meeting 25th of March 2020](https://indico.cern.ch/event/899153/) focused on non-LHC experiments. One talk from neutrino experiments (NOvA, SBN and DUNE) and one from Belle II. Neutrino community would appreciate a lot having a GPU-based module for optical photons transport that could be integrated into Geant4, as this currently is a very CPU-consuming part of the simulation.

Next topical meeting to be decided, but target is end April, beginning May.


### Reconstruction and Software Triggers

Next meeting confirmed for April 1st 17-18h, ATLAS/CMS CPU optimization experiences in reconstruction code. In calendar, will be announced today. 

General HSF question: we had a researcher contacting us to do some hands-on work in the WG. We think this is great! We could go two ways:
- give him the set of projects and putting him in touch with the one that matches his interest
- ask him to help out with making one of the projects more cross-collaboration
- other opinions... 

Opinions on what's best for HSF? 
- In general this is very positive; we are very keen on work that *generalises software to a larger community*, but do need to check that the projects themselves are amenable is important

### Software Tools and Packaging

- In case people have missed it, you can access the agenda for the OpenLAB/Intel remote session on oneAPI [here](https://indico.cern.ch/event/878418/timetable/?view=standard):
    - Material is available for future reference.
    - In particular, _Offload Advisor_ (What should I offload to a GPU?) looks like an interesting tool that we can discuss in one of the upcoming meetings. If you have any experience w/ it (especially in a real-life example) please get in touch w/ us.
    - Majority of the session was dedicated to DPC++.

- From Ben: "[...] collect a list of packages we need in Spack, but not currently there. I've got a feeling there are several efforts out there writing their own recipes, but in either case it could be good to get this in place."
    - To be followed up possibly via e-mail and/or a meeting.
    - LCG release contents would be a good starting point

### Event generators

- Development on GPU port of MG5aMC is progressing. Planning a meeting on Monday including CERN, Louvain and Argonne contributors.

### Frameworks

We have scheduled a meeting for next week (April 1) to discuss the JANA framework's multi-threaded scheduling mechanisms.  This inaugurates a series of meetings devoted toward exploring how different experiments handle the scheduling of steps to be performed in a multi-threaded environments.

## Workshops

### HSF/WLCG 2020 workshop

For a re-scheduled full workshop **21-25 September is the proposal being discussed**

- We have pre-booked the same venue in Lund (social dinner moved to Tuesday as there are more takers for Fall conferences)
- No one knows how the situation will evolve, so more news will come before the summer

#### Virtual Event Proposal

The Scientific Organising Team continued discussing what we could do as a virtual event in the May slot

Current proposal to organise a *3* session event, focused on **New Architectures, Portability, and Sustainability** (i.e. the Tuesday Lund plenary session), but to have these three sessions spread over 3 days and *only for 2 hours* (roughly the time we feel that people can concentrate on remote hosted events)
- Monday 11, Tuesday 12 and Wednesday 13; 16-18h CERN time (fairly friendly from Europe to the N American Pacific coast)
    - Day 1 - Code portability, Common software
    - Day 2 - Workflows (Framework, WMS)
    - Day 3 - Validation, Pledges, Benchmarking
- We would like speakers to upload their material *well* in advance.
- Have a notes document where people can post questions, also in advance.
- Almost certainly we would use Zoom which has some nice features for larger meetings.
- Setup a semi-permanent chat channel (not just VC chat), like Slack or Mattermost.
- [discussion needed] material can be indexed on Zenodo, including recordings
    - Practically, use Indico to get recording permission
    - Not planning to pre-record talks, but to have material still presented during the event

*This would be a learning experience for the community, that could lead the way towards less travel and f2f meetings as well as keeping activities running in times of COVID-19.*

- **Is this worthwhile doing?** Please *do* give feedback on whether you believe this event is good to organise and if you would attend it (in particular, if your feelings are *negative*)
    - Liz - virtual meetings need to have a specific focus, but experience of virtual CMS S&C week is positive
    - David - *Connecting the Dots* will be pre-recording material (otherwise not practical to do 20hrs of material from many timezones), so this will provide some experience of an alternative format

### [PyHEP 2020 Workshop](http://indico.cern.ch/e/PyHEP2020)
- We will decide on the format of PyHEP 2020 next week.
- In touch with SciPy 2020 conference chairs for what happens there.

## AOB

We changed to Zoom this week, a regular meeting has been booked until the end of the year
- Please give [feedback on your Zoom experience](https://escape.cern.ch/AVC-workspace/videoconference/Lists/Zoom%20Pilot%20Feedback/overview.aspx) to CERN IT

### Next Meeting

- Next regular meeting slot is 9 April
