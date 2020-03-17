---
title: "HSF Weekly Meeting #182, 12 March, 2020"
layout: meetings
---

# {{page.title}}

Present/Contributors: Graeme Stewart, Pere Mato, Eduardo Rodrigues, Ben Morgan, Paul Laycock, Attila Krasznahorkay, Mason Proffitt, Efe Yazgan, Daniel Elvira, Michel Jouvin, Kyle Knoepfel, Teng Jian Khoo, Liz Sexton-Kennedy, Maria Girone, Philippe Canal, Stefan Roiser, Witek Pokorski, Andrea Rizzi, Chris Jones, David Lange, Gloria Corti, Horst Severi


ni, 

Apologies: Caterina Doglioni, Agnieszka Dziurda

## News, general matters

### HEP-CCE Kick Off Meeting
There was an [organizing meeting](<https://indico.fnal.gov/event/23262/other-view?view=standard>) for a new project organization of the CCE which is a collaboration of ANL, BNL, Fermilab,and LBNL participants funded to work on HEP's most pressing and uncovered topics.

We've agreed that going forward all technical meetings should be fully public in the same way that IRIS-HEP meetings are. It seems that this could be coordinated through the HSF sub-group conveners.

Main topics interesing to HSF:

-  Portable Parallelization Strategies: meaningful systematic comparison of a few pieces of HEP code (FastCalosim, Patatrack, Wirecell)
    - Overlap with interests of Framework WG and Reco WG
- Fine-Grained I/O and Storage: new storage technologies, Philippe is involved, evolution of ROOT I/O - RNTuple is in development, so apposite time for this activity
- Event Generators, recognised as ever more important and will ramp up over time

### HSF/WLCG 2020 workshop

Sadly, due to the uncertainty regarding COVID-19, and the advice and restrictions being put in place (CERN, DOE), we thought that it was prudent to cancel the workshop. For people who paid registration, refunds are being arranged.

Hope is to move to the Autumn - **21-25 September is the proposal being discussed**
- This is the only week from September to mid-November when there is not an LHC/LHCC experiment event of some kind
- There is a clash with the European HTCondor event (at LAL/IJCLab), we are discussing how best to manage that (thanks to our HTCondor colleagues for their understanding)
- There is also a clash with the Geant4 collaboration meeting in Rennes, which will impact detector simulation people
- We hope to confirm these new, tentative, dates very soon
    - Evidently actually holding the workshop, even in the Autumn, is contingent on a positive evolution of the COVID-19 situation

*For most of the topics we were intending to cover in Lund, these should now move to "regular" style Working Group meetings*

#### Virtual Event Proposal

The Scientific Organising Team discussed what we could do as a virtual event in the May slot

- Video conferencing technology is good enough now to make virtual events feasible
- Timeslot has to be US/EU friendly (sorry to Asian colleagues, at least for this time)
    - Could start 15h CERN time at the earliest
        - 6h for Pacific coast, which is still a bit hard
    - Could end at 19h CERN time
        - Quite late for Europe, but not awful
    - We understand that this can be difficult, especially re. family committments, *but these are exceptional events, not regular meetings, and they replace a week of travel*
    - Concentrating on remote meetings can be hard, so this also makes a 4h slot more practical
- We believe that encouraging less physical travel overall in our community is a positive thing (money, time, CO2 - see <https://remotely.green>, <http://hiltner.english.ucsb.edu/index.php/ncnc-guide/> aka <http://greenphysicsconference.com>)

We would like to try and organise a 2 session event, focused on **New Architectures, Portability, and Sustainability** (i.e. the Tuesday Lund plenary session)
- Monday 11 and Tuesday 12 May, 15-19h CERN time
- *or* Tuesday 12 and Wednesday 13 May, 15-19h CERN time

We should think creatively about how to make remote-only meetings more effective as well, e.g., more active use of chat and live notes
- We can record these using Vidyo, at least, and post them

- Q (Caterina): can we try and use Zoom? Many of the "wishes" for more effective videoconferences that Vidyo doesn't have are there already (e.g. someone raising their hand, asking to slow down/speed up for a presentation, expressing agreement/disagreement). If we want to test things out, I can host one of the future coordination meetings because my university provides a full account.
    - Noted that CERN IT are investigating future solutions for video conferencing, not necessarily Vidyo
- Liz:  I second Caterina's suggestion.  Fermilab is using zoom so I have the opportunity to compare both solutions and find zoom superior.
    - Could investigate using FNAL's infrastructure to help us host this event? (Not sure exactly what the requirements would be at the moment, but FNAL has first class connectivity worldwide)
- Horst: Also supportive (and it works better).
- Eduardo: just for completeness, let me say that there is also [SpeakApp](https://speakapp.link), which is used by Belle II. I believe our colleagues are very happy with it. It's all in the browser.

### Alpaka training event

On **Monday 27 April** a training session for Alpaka will be held in the CERN/IT auditorium (modulo COVID-19). Event info and registration at <https://indico.cern.ch/event/883212/>. In case we need to postpone the event all registered participants will be contacted. *Please sign-up, but do not make any travel arrangements.*

### CUDA Training at CERN

Maria attended a dedicated meeting with Nvidia for organising training through hackathons and bootcamps. Want to host at CERN a CUDA dedicated bootcamp, 2-3 days (pre-requisites are to be a decent CPU coder). Then a hackathon as a follow-up, when people have real projects to work on.

Can have it in the technical training centre at CERN. Was arranged for April, but that has had to be cancelled. Will try to make another definite arrangement once COVID-19 has calmed down a bit.

Machine Learning WS - 2-3 day event, more open than the CUDA event (less expertise required from participants); hope to have it end of June.

## WLCG Report

A draft of the 2020-H1 report is attached to the agenda. This covers SFT projects and the HSF. If you have feedback, please send it to Graeme by this Friday (2020-03-13).

## Google Summer of Code 2020

Currently *Student Interaction Period*, until 16 March

## LHCC Review of HL-LHC Software and Computing

*Reminder*: LHCC will review software and computing plans for the HL-LHC, Amber Boehnlein (JLab) will chair, first phase will be 18-20 May 2020. Five 20 page documents provided as input to the committee, from ATLAS, CMS, WLCG, DOMA and from *Common Tools and Community Software* (the HSF takes care of the later)

[Document outline](https://docs.google.com/document/d/1ai7m7kFyiGgl2tKralJKyPX6rlD9tffU7B6wPj_vpZU/edit?usp=sharing) has been created and is being filled in.

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

*Please take a look and decide if we need to expand on any points (but remember the target audience!)*

#### Discussion with CMS and ATLAS

- CMS invited us (Graeme) to report on the document and discuss with them at their next S&C week (24-27 March)
- Graeme contacted ATLAS with a view to having a similar discussion in early April

#### HSF Feedback Sessions

- Maybe organise one longer meeting, but also decide in advance what topics need discussion time

Proposal: HSF review and feedback week of 6 April, one afternoon 15-17h (is that enough time?).
- Launch a doodle ASAP, avoid using the Coordination slot

## Working Group Updates

### Data Analysis
* Joint meeting with DOMA on March 17th (<https://indico.cern.ch/event/890991/>), announcement made in the proper lists.
    * First meeting will feature ATLAS+CMS, but more instances envisioned, and have suggestions of collaborations to invite (more ideas welcome!)
* Dumped a fair bit of text into the LHCC draft (4 pages, but can use refinement -- will evolve based on upcoming meetings)


### Detector Simulation
- Next topical meeting planned on 25th March; proposed topic: Needs and experience of non-LHC HEP community; currently contacting potential speakers
- Following meeting planned for 15 or 22 April
- Two pages of LHCC draft document on simulation written, more coming
- R&D Forum for Simulation on Accelrators? 
    - Can foresee this to be one of the topical meetings, end of April (announce this well in advance)


### Reconstruction and Software Triggers

- Next meeting: March 18th at either 16 or 17:00, *CPU software improvements in ATLAS and CMS* (CMS TBC)
- Working through the LHCC document, on track to have a draft by the end of the month
- We will start planning next meetings with the topics we wanted to cover in HSF workshop
    - tracking alternatives (CPU/GPU/maybe even FPGA if in mandates) for triggers, possibly wait until LHCb makes a decision
    - non-standard reconstruction
    - particle flow


### Software Tools and Packaging
- Will review upcoming meetings/topics in light of HSF Workshop postponement.
    - Packaging/Deployment (maybe overlap with BoF session)
    - Profiling tools, especially for GPUs
    - IDEs
- Discussion (related to generators + gitlab.cern.ch) that tools for CI would be a useful topic for a meeting (Jenkins, GitlabCI, Travis, etc.)


### Event generators
- LHCC Document
    - Received (positive) feedback from generator experts etc. on first draft for the LHCC document. Now implementing small sets of comments before circulating to the WG. On schedule to have a draft ready by the end of the month.
- GPU tutorial
    - Hard to arrange anything concrete given the COVID-19 situation, but we would still like to try to get something provisional or that works purely remotely in place (see training discussion above).
- gitlab.cern.ch for generators
    - Several MC generators/tools have recently migrated their code to git; e.g. Pythia, Sherpa and Rivet made the move to gitlab.com. 
    - They would have preferred to use the CERN based service, but they are not all CERN users and the CERN light-weight account does not have sufficient functionality to allow gitlab usage.
        - Rivet gets mainly contributions from LHC
        - Pythia/Sherpa have many authors who have CERN accounts, but not all; it would be easier to have things at CERN
        - Easier to do heavier CI tests covering some non standard HW when things are at CERN
    - We are going to follow up with CERN IT to see what can be done to improve the situation.
        - eduGAIN would be much more discriminating of bona fide HEP colleagues

### Frameworks

- After some time off, started with organising meetings once more.
    - Had a private meeting amongst the conveners about this yesterday...
- Will still have to hear from Belle II in a meeting, we are trying to find the "right time" for them.
- The main topic of discussion for the few following meetings will be on MT scheduling.
    - First meeting to be scheduled (hopefully) soon.


## Other Workshop News

### [PyHEP 2020 Workshop](http://indico.cern.ch/e/PyHEP2020)
  - The Python Software Foundation confirmed sponsorship, with a generous $1000 grant. Many thanks to the PSF!
  - We are moving forward with the preparation of the agenda. We expect - and hope! - the COVID-19 saga to be over by the time the workshop takes place in mid-ish July.

### LAWSCHEP2019 Workshop

The document with the summary and conclusions of the First Latin American Workshop on S&C challenges in HEP has been finished and posted in the workshop web page at:
<https://indico.cern.ch/event/813325/>
The document includes action items and a list of projects. The list was put together using a google document where participants added their proposed activities and names with the purpose of either initiating new partnerships or joining existing ones. A "live document" with only the project list will be added to the web page soon so that the list continues to evolve. Unfortunatelly the LAS4RI workshop in Sao Paulo planned for March 22-27 was postponed due to the virus crisis. We can think of LAS4RI is a Latin American "Snowmass process" or "European Strategy process". In any case, the LAWSCHEP scientific committee will send the LAS4RI organizers the LAWSCHEP document so that they are aware of the LAWSCHEP workshop and action items.

## AOB

- [Update](https://github.com/HSF/hsf.github.io/pull/744) to the calendar information on the website
    - Prefer the inlined calendar on an HSF webpage
    - Clearer links to HSF Indico
    - Link to the [calendar of religious holidays](https://hepsoftwarefoundation.org/holiday-calendar.html) (maintained by CHEP IAC Diversity Group)

- A proposal describing how HSF delivers letters of cooperation and support:
    - <https://github.com/HSF/hsf.github.io/pull/732>
    - *This is now considered approved*

### Next Meeting

- Next regular meeeting slot is 26 March
