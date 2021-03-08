--- 
title: "HSF Weekly Meeting #202, 18 February 2021"
layout: plain_toc
--- 

Present: Benedikt Hegner, Alaettin Serhan Mete, Ben Morgan, Mason Proffitt, Teng Jian Khoo, Krzystof Genser, Allison Hall, David Lange, Kevin Pedro, Dorothea vom Bruch, Liz Sexton-Kennedy, Caterina Doglioni, Eduardo Rodrigues, Kyle Knoepfel, Marc Paterno, Efe Yazgan, Sudhir Malik, Michel Villanueva, Josh McFayden

Apologies: Graeme Stewart

  
## News, general matters, announcements

### WG Plans and Last Meeting's Minutes

At the [2nd but last meeting](/organization/2021/01/21/coordination.html) we reviewed WG plans for the early part of 2021 in particular.

Graeme sent a PR request for people to comment on.

### Google Summer of Code

[Submission of project ideas](https://hepsoftwarefoundation.org/activities/gsoc.html) was open till 15 February. Avoid submitting the last minute, there is a review process for the PRs! Also check the instructions for changes to the projects this year. Few points to keep in mind:

 - The program [timeline](https://developers.google.com/open-source/gsoc/timeline) has changed. Student projects have halved in length (175 hours), so project proposals need to be more concise. The coding period is Jun 7 - Aug 16, but the project hours can be spread within as convenient for the mentor and student.
 - Shorter projects make it possible to have more proposals splitting larger developments. This is encouraged as long as sub-projects do not depend on each other. There will be also potentially more candidates than last year.
 - There is a detailed internal [timeline](https://hepsoftwarefoundation.org/activities/gsoc.html#timeline) for the project submission and candidate selection period.
 - Prepare a test for candidates, relevant for your proposal, by Mar 9, when mentors will start being contacted. It is very important to do an initial filtering to have an extended exchange only with a limited number of students this year!
 - We will need help as every year for the final proposal evaluation for the slots request (selection committee) (Apr 28 - May 2)

### November Workshop Survey and Outcomes

The [outcomes and follow-up document](https://indico.cern.ch/event/941278/attachments/2141065/3690191/HSF%20Workshop%20Follow-Ups.pdf) was finalised - please have a look for items to not forget about in 2021. (There is still the [commentable version](https://docs.google.com/document/d/137j-4mAtGupGC2iR4_EKn0Z4FuSSFdxY9Qo2BNwzE6Y/edit?usp=sharing) if anything was omitted.)


## Working Group Updates

### Data Analysis

Metadata discussion series had good discussion -- last meeting on Tues with "analysis experience". Some overall impressions (see [live notes](https://docs.google.com/document/d/12PptTc851lthSmptzax6OqkbIoB2zCOag5WNi1WXYNc/edit#heading=h.x90p8rq02qnj) for more):
- Analysers seem "happy" -- but are they just used to working suboptimally?
    - Tendency to prefer easy over robust -- rather parse filename (and self-impose file/dir naming conventions) than read in-file MD
    - Yet also rationalising "wait for email to copy from Twiki" as an important "validation strategy"
    - Liberation from collaboration code is valued
- Bearing in mind mostly ATLAS/CMS input, steps towards consolidation of analysis-specific sources
    - ATLAS Calibration Area, CMS common JSON on CVMFS for heavier calibration files
    - Associated cross-section info in dataset/production management DBs
        - Concerns over curation & source-checking
    - ATLAS keener to centralise than CMS -- this did take some time
    - Needs to be relocatable for sites/users w/o connectivity
    - Preloading to reduce overheads/facilitate preservation?
- Concern over 100% processing requirement is not so great?
    - Given for final publication, but only a limitation for reproducibility of intermediate studies in case of low MC stat
    - Have book-keeping tools at least for jobs that don't split files

Follow-up:
- Invited participants to start drafting a rough set of requirements for future metadata schemes, circulate result as basis for feedback (survey?)
- Organise a meeting/workshop later on to refine

Other plans:
- Find a date to speak to Training WG
- Pick next topic between (non-LHC) expt overviews and declarative analysis, set dates & contact speakers
- Prefer to involve 3rd convener

### Detector Simulation

- First two meetings scheduled:
    - [Simulation challenges for muon colliders](https://indico.cern.ch/event/1009175/) 22nd Feb. 17:30 CERN time.
    - [NEST package for liquid nobel gases/dark matter](https://indico.cern.ch/event/1009384/) 8th March 17:30 CERN time.
- To avoid duplicating meetings like Geant4 R&D, CAF, etc (like the VecGeom topic in CAF), input/ideas from other WGs on common/cross topics of interest very welcome!

### Reconstruction and Software Triggers

- New conveners had their first meeting last week.
- Any news on possible synergies with simulation group on the topic of geometry, especially a format suitable for accelerators such as GPUs
    - Useful starting point at next [Compute Accelerate Forum on 10th March](https://indico.cern.ch/event/975008/) which will cover geometry on accelerators.

### PyHEP

Next topical meeting on March 3rd (every first Wednesday of the month).
- Happy to engage more strongly with the training and/or DA WGs for these tutorial sessions, which are rather training oriented.

PyHEP 2021 workshop preparations due to start in the next few days.


### Software Tools and Packaging

- We had the follow-up meeting on Guilherme's perf discussion:
  - Thanks to all who joined and contributed
  - Very useful discussions and positive feedback
  - [Agenda](https://indico.cern.ch/event/999543/)

- Next week, Bob Dröge will tell us about European Environment for Scientific Software Installations (EESSI):
  - Time: Wednesday, February 24 @ 5pm CET 
  - [Agenda](https://indico.cern.ch/event/1005954/)

### Software Training

- GitHub CI/CD training event started on Feb 16 with a kickoff gathering.
    - [Agenda](https://indico.cern.ch/event/1001128/overview)
    - 189 participants registered.
    - Videos are available on the Indico and participants are following them during the week.
    - Hands-on session on Friday.

- Please drop into our weekly training meeting 16h CET Mondays to kick-start a training.
    - Live notes are available in [this document](https://docs.google.com/document/d/12ePA3CLkBks89YcMXA7qulCDs0D_7RLfMpQe-k1du3g/edit?usp=sharing).
    - A potential training event related to Simulation is on the radar. We will keep the communication with the Detector Simulation WG.

- Nice to see people (~12) from Nuclear Physics community participate

### Event Generators

- The only news is that we are uploading the new version of the generator paper (v4) to arxiv today and then submitting the latest version to the journal along with the responses to the referee comments. 

### Frameworks

Yesterday discussed CMS's experience with upgrading to the latest UI of TBB. [https://indico.cern.ch/event/1005030/](https://indico.cern.ch/event/1005030/)

We plan to start "free-form-discussion" meetings once a month, to allow for an easier exchange of information. We will see how that goes...


## Other Interest and Activity Areas

### Differentiable Computing

"Campfire" meeting, last week Friday 12 Feb at 17h: <https://indico.cern.ch/event/1005490/>.

---

## AOB

### vCHEP2021

Registration has [opened](https://indico.cern.ch/event/948465/).

### Next Meeting(s)

- Next meeting will be 4 March

