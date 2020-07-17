---
title: "HSF Weekly Meeting #190, 16 July 2020"
layout: plain
---

Present/Contributors: Graeme Stewart, Benedikt Hegner, Liz Sexton-Kennedy, Teng Jian Khoo, David Lange, Horst Severini, Agnieszka Dziurda, Kyle Knoepfel, Paul Laycock, Efe Yazgan, Pere Mato, Caterina Doglioni, Gloria Corti, Daniel Elvira, Ben Morgan, Michel Jouvin, Pere Mato

Apologies: Eduardo Rodrigues

## News, general matters, announcements

### Letter of Support for SWIFT-HEP

Our colleagues in the UK are submitting a bid for funding to STFC as a follow-on to ExCALIBER HEP (PI Davide Costanzo). It will cover:

* Event Generators
* Detector Simulation
* Intelligent Data Management
* Analysis
* Reconstruction Algorithms

The draft letter of support is [attached to this meeting](https://indico.cern.ch/event/916413/).

Approved by the meeting, but also need to circulate a bit wider so more people can see. (We discussed that in general WG convenors should also see this during the internal discussion phase.)

### IRIS-HEP Blueprint Meeting on *Sustainable Software in HEP*

This meeting is now set for July 22: <https://indico.cern.ch/event/930127/>.

Graeme was asked to give a contribution on the HSF's role -- draft slides next week.

### ESCAPE Workshop on Open Source Software Lifecycles (July 23, 24 + 27, 28)

<https://indico.in2p3.fr/event/21698/overview>

Lukas Heinrich kindly agreed to give the HSF talk.

There will be a short contribution, plus discussion session about the sustainability of test science projects.

### LHCC Review of HL-LHC Software and Computing

Still awaiting the report from the referees.

We were contacted by someone who contributed to the Detector Simulation chapter and was surprised not to have an acknowledgement or have been added as an author to the document. *This is not a good situation and the contributions from beyond the WG convenors are valuable and valued.*

Proposal: WG Convenors can *nominate* people who should be added to the document as authors and *poll* their communities for self-nominations. We then list these people in a revised version as authors, and mark the WG convenors and Graeme as editors.

We agree to proceed in this way.

### New Convenor for Data Analysis WG

Reminder that nominations (including self-nominations) are open until 31 July for someone to join Paul and TJ (the appointment is to run from 1 September through 2021).

Please send nomintions to <mailto:hsf-search-committee@cern.ch> (which maps to Graeme, Liz and Michel).

### YouTube Channel

An [HSF YouTube Channel](https://www.youtube.com/channel/UCv4hukXGkCYvBClQMKzypnQ) has been created. This is really useful for hosting training material, workshop recordings, etc. A description of the purpose and mechanics was added to the website: <https://hepsoftwarefoundation.org/organization/youtube.html>.

We have almost 100 subscribers (please sign up!) and many of the videos have been viewed 20+ times in just a few days:

First playlists:

* PyHEP 2020
* Training : Continuous Integration/Development
* Training : CMSOpenData HTauTau Payload
* HSF-WLCG May 2020 Workshop

### Snowmass

Reminder that announcements about the Snowmass process was sent to the email list, with an [initial workshop on 10-11 August](https://indico.fnal.gov/event/43829/).

We will submit the LHCC input document to the review (which we agreed with the convenors did not need to go via an LoI).

## Website

### Review process on PRs

Reviews have been happening more promptly in the last few weeks - thanks to the reviewers!

## Working Group Updates

### Data Analysis

[Meeting yesterday](https://indico.cern.ch/event/932570/) on B-Physics/Light states/exclusive analyses:

* LHCb, Belle II, CMS, ATLAS contributions
* Trying to understand workflows, disk/CPU requirements for analyses requiring special reconstruction
* Already some cross-experiment interest in some workflow features
  * Grid-based CI checks and automated central submission of jobs on successful MRs
  * Scouting jobs for grid processing
  * conda for analysis distribution
  * Enforced resource caps on user-developed skimming operations
* Plan to follow up by summarising known resource needs for B-physics/Exotics analyses to understand where more quantitative metrics are needed

Thinking about next meeting -- tentatively end of Sept. Possible topics:

* (Analysis) metadata survey across experiments
* Joint programme with training subgroup on improving analysis code quality? CI, documentation, developer tools, ...

### Detector Simulation

Having a summer break on meetings. Will resume in September.

### Reconstruction and Software Triggers

Having a summer break on meetings. Will resume in September.

Short contribution at Snowmass TDAQ meeting about real-time analysis (slide taken from Institut Pascal). Agenda here: <https://indico.fnal.gov/event/44402/>.

### Software Tools and Packaging

Lots of fixes for Spack packages (from CERN+DESY). Would like to get a talk from Spack
developers after the summer break.

### Software Training

* Preparations for Virtual Docker Training well underway
  * 100 participants selected out of 154 registrations
  * will record videos soon
* Moved recordings of past workshop to HSF youtube channel
* New content:
  * Emery to prepare second version of CI/CD module using github + travis (for CMS)
  * Started blank repository for ALPAKA module
  * Started pages [how to create new hsf training module](https://hepsoftwarefoundation.org/training/howto-new-module) and similar
* Discussions on minimum requirements to call a training event an “HSF training” event (probably very loose, because it's usually a win-win situation)

### Event generators

* Minutes of last meeting: <https://hepsoftwarefoundation.org/organization/2020/07/09/generators.html>
* May have another meeting next week.
* Paper:
  * Received referee comments - deadline, Aug, 23rd.
  * Included as a "contributed paper" in SnowMass in Computational Frontier as well as in Theory Frontier

### Frameworks

* We continue our efforts to line up talks on framework scheduling as it relates to accelerator offloading.  We have a tentative commitment from the Allen framework to speak in late August; we are seeking a talk from CMS (and anyone else) as well.

* We are also planning to schedule talks related to metadata handling in the context of multi-threading.

## Other Interest and Activity Areas

### Differentiable Computing

* Two relevant contributions in the PyHEP 2020 workshop from Lukas and Nathan.

---

## Workshops

### PyHEP 2020

The [PyHEP 2020](https://indico.cern.ch/e/PyHEP2020) virtual workshop in running this week, with keynotes, talks and tutorials.

* Things have been smooth after a hiccup at the very beginning, as Zoom was not allowing more than 300 people to join. Issue sorted out within 30 minutes (we then had 430 participants in that first session in the end).
* We are experimenting different ways of running a virtual event:
  * No live notes, no GoogleDoc. Participants rather post questions to the speakers via the [slido](https://www.sli.do/) platform, the preferred ones get upvoted by anyone, and at the end of the presentation the chair brings the most popular questions up for discussion with the speaker.
  * All presentations are been recorded, captioned and uploaded the the [YouTube HSF PyHEP 2020 workshop playlist](https://www.youtube.com/playlist?list=PLKZ9c4ONm-VkZXgXlA8bGsOXcukp8hh9N) (captioning is ongoing).
  * Inter-participant communication goes via several [Slack channels](https://join.slack.com/t/pyhep2020/shared_invite/zt-fnzdj0pv-AEdBBkEohHaj8Gf3mazDPA ) - general announcements, topical, etc.
  * We pushed for "notebook presentations" and many speakers are playing the game, having their presentations in notebooks in GitHub repositories.
  * We have been in touch with the Binder team so that they allocate the speaker's repositories extra resources at the time of the presentation, to enhance the experience from potentially many participants spawning the same notebooks at the same time.
  * There is a continuous flow of tweets in our [Twitter channel](https://twitter.com/PyHEPConf).

### Future HSF-WLCG Workshops

* No face to face HSF/WLCG workshop in 2020
* Remote workshop in November (proposal is 19+20 (Thu, Fri) plus 22+23 (Mon, Tue) November)
  * Themes welcome now so that we can call for contributions after the summer
  * We should add this to Indico as a placeholder event...
* CHEP 2021 (17-21 May) still uncertain whether in-person or remotely
* attempt at face to face HSF/WLCG workshop in September 2021, potentially in Lund

#### Mini-poll 

Put an X near one or more options, plus first X for attendance...

* I participated in this poll: XXXXXXX
* I would attend a pre/post CHEP (17-21 May) weekend event in person if CHEP takes place in person XXXXXX
* I would not attend a pre/post CHEP weekend event in person
* I would attend a pre/post CHEP weekend event remotely XXXXXX
* I would not attend a pre/post CHEP weekend event remotely

We would like to have additional people helping to organise the next events, **so if you would like to help organise please contact HSF Coordnation or Graeme**

## AOB

### Next Meeting

* Next regular meeeting slot is 30 July
  * Propose to make this a short meeting
* Propose to then skip the scheduled meetings for August, viz. 13 and 27
* First post holiday season meeting would normally be 10 September
  * *This is the CERN Jeune Genevois holiday, which we usually skip*
  * Therefore propose 3 September (exceptional), then 24 September to go back to the usual every-odd-week Thursday schedule
* Agreed to this schedule
