---
title: "HSF Weekly Meeting #201, 4 February 2021"
layout: plain_toc
---

Present: Graeme Stewart, Serhan Mete, Attila Krasznahorkay, Michel Jouvin, Ben Morgan, Eduardo Rodrigues, Dorothea Vom Bruch, Chris Jones, Kevin Pedro, Efe Yazgan, Mason Proffitt, Andrei Gheata, Paul Laycock, Daniel Elvira, TJ Khoo, Sudhir Malik, Krzysztof Genser, Stefan Roiser, Kyle Knoepfel, Antoine Pérus, Benedikt Hegner, Liz Sexton-Kennedy, Mircho Rozodov, Philippe Canal, Daniel Elvira, Andrea Valassi (late), Meirin Oan Evans (late)

Apologies: Josh McFayden, Marc Paterno

## News, general matters, announcements

### WG Plans and Last Meeting's Minutes

At the [last meeting](/organization/2021/01/21/coordination.html) we reviewed WG plans for the early part of 2021 in particular. (Note that a TOC was added, so that direct links to individual WG notes are easier.)

We want to now more widely announce these to the community, to different experiments. This is both to raise the profile of HSF activities and to solicit feedback, particularly from non-LHC experiments.

Should we just refer to these minutes or prepare another page as a 2021 *Plan of Work*?

- Graeme will prepare a separate page and send the PR for people to comment on. This allows us to refer to topics from multiple meetings. Make it clear that this was a plan in early 2021, not set in stone!

### Google Summer of Code

Remember to [submit your project ideas](https://hepsoftwarefoundation.org/activities/gsoc.html) by 15 February. Avoid submitting the last minute, there is a review process for the PRs! Also check the instructions for changes to the projects this year. Few points to keep in mind:

- The program [timeline](https://developers.google.com/open-source/gsoc/timeline) has changed. Student projects have halved in length (175 hours), so project proposals need to be more concise. The coding period is Jun 7 - Aug 16, but the project hours can be spread within as convenient for the mentor and student.
- Shorter projects makes it possible to have more proposals splitting larger developments. This is encouraged as long as sub-projects do not depend on each other. There will also be potentially more candidates than last year.
- There is a detailed internal [timeline](https://hepsoftwarefoundation.org/activities/gsoc.html#timeline) for the project submission and candidate selection period.
- Prepare a test for candidates, relevant for your proposal, by Mar 9, when mentors will start being contacted. It is very important to do an initial filtering to have an extended exchange only with a limited number of students this year!
- We will need help, as every year, for the final proposal evaluation for the slots request (selection committee) (Apr 28 - May 2)

### November Workshop Survey and Outcomes

The [outcomes and follow-up document](https://indico.cern.ch/event/941278/attachments/2141065/3690191/HSF%20Workshop%20Follow-Ups.pdf) was finalised - please have a look for items to not forget about in 2021. (There is still the [commentable version](https://docs.google.com/document/d/137j-4mAtGupGC2iR4_EKn0Z4FuSSFdxY9Qo2BNwzE6Y/edit?usp=sharing) if anything was omitted.)

The [post-workshop survey was digested](https://cernbox.cern.ch/index.php/s/66nXbudet4keYXn). 55 people responded for the HSF sessions (about 20%?). Overall the results seem quite positive (e.g., we improved the number of students attending). Proposal is to look more in depth in a future coordination meeting.

## Working Group Updates

### Data Analysis

(Repeated post-meeting addendum to previous minutes)

Ongoing series of metadata discussions seems like a workable format to repeat on other topics. Some themes that could follow:

* Declarative analysis & analysis frameworks
    * Want to avoid this becoming a competition -> focus on interfaces & usability?
    * Incorporate workflow management as well as event processing
    * Identify the most essential functions of an analysis framework & how these should be provided to the user
    * Could have follow-up meeting or even mini-workshop to expand benchmarks (c.f. <https://github.com/iris-hep/adl-benchmarks-index>)
    * To-do: review what IRIS-HEP is up to, so we don’t duplicate
* Overviews from non-LHC experiments
    * We as conveners still lack some awareness of the major issues in some other communities
    * Thinking to invite reps from e.g. neutrinos, nuclear physics to describe what issues they are grappling with
        * Graeme - Caterina would be a good contact with dark matter experiments
* Reduced data formats (NanoAOD/DAOD_PHYSLITE)
    * Attempted conversations with the non-mainstream analyses
    * Should we revisit questions of policy (i.e. how to engage user base), consequences (framework design, sites)
    * Also haven’t spoken to WLCG/DOMA in a year (<https://indico.cern.ch/event/890991/manage/timetable/#20200323>), try to reconnect? But needed more concreteness on what studies should be done.

Besides these, we discussed commonalities with Training WG. One Q: how much should HSF branch into (experiment-agnostic) analysis tutorials?

* Curriculum has a basic CMS example - without focusing heavily on the physics aspects, could this be expanded to cover statistical tools, demonstrate analysis ecosystem e.g. PyHEP? But don’t want to be prescriptive.
* (Probably) have had discussions comparing, e.g. CMS DA school and ATLAS SW tutorial? Can HSF material usefully be integrated into these?
    * Feeling that apart from experiment-specific SW, things like stats, generators etc. could be made more common between experiments
    * No mention of HSF material now - probably because it is rather new compared to the established experimental tutorials?
        * There is surely enough material on useful topics for beginners now that we should start to campaign for this as a useful core training resource

### Detector Simulation

- First new conveners' meeting last week
- Initial set of topics to cover discussed
    - Simulation challenges for future experiments (provisionally last week of Feb)
    - NEST package for liquid noble gases/dark matter
    - AdePT/Celeritas/Excalibur/GPU update
    - Geometry: experiences of migrating to/using DD4HEP (advertise CAF meeting on lower level VecGeom, etc. topics)
    - Machine Learning implementations in experiments (inc. LHC and Low Background)
- Avoid duplicating meetings like Geant4 R&D, CAF, etc (like the VecGeom topic in CAF).
- No ideal slot, provisionally Mondays 5pm CET, but realise this has issues.
- Attended (Ben) this week's Training WG meeting. Useful discussion on possibilities for Geant4 training. Following up with Geant4 on potential here.

### Reconstruction and Software Triggers

- First meeting of the new conveners next Monday
- Possible synergies with simulation group on the topic of geometry, especially a format suitable for accelerators such as GPUs
    - Supported by sim conveners

### PyHEP

The **topical meetings** ([Indico](https://indico.cern.ch/category/11412/)) of the kind *“Python Module of the Month”* started yesterday with a tutorial on Numba.

- Agenda with link to GitHub repository at <https://indico.cern.ch/event/985350/>.
- Excellent participation - 94 people!
- Tutorials being recorded in [dedicated HSF playlist](https://www.youtube.com/playlist?list=PLKZ9c4ONm-VnFUD0XX2DmfP1JA8VIRhXP).

Next topical meeting on March 3rd (every first Wednesday of the month).

- Happy to engage more strongly with the training WG for these tutorial sessions, which are rather training oriented.

Not clear how many people followed-along live, launching and using the notebook at the same time as the speaker?

- Graeme and Eduardo felt it was hard to listen to Jim, follow Slido and work with one's own notebook at the same time
- However, having the tutorial in a notebook is still extremely useful; people can (re)run at their leisure, even while following the YouTube video

### Software Tools and Packaging

We have two interesting talks lined up:
- Continuation of the "Linux Systems Performance: Tracing, Profiling, and Visualization" talk by Guilherme Amadio
  - Agenda : <https://indico.cern.ch/event/999543/>
  - Time : **February 17, 2021 @ 5pm CET**
- "Compiler optimization reverse engineering using Cutter" by Hadrien Benjamin Grasland
  - This'll be a demo on [Cutter](https://cutter.re/), in Hadrien's words _"[...] a binary reverse engineering tool, which is normally meant to be used by people like security researchers who try to figure out how random stripped binaries from the Internet work. However, I recently found out that it is also useful when one is trying to figure out what compilers are doing during the code optimization process, in order to investigate puzzling behaviors like auto-vectorization not vectorizing when it seems it could, or similar implementations of a given algorithm performing very differently at high optimization levels."_
  - Agenda : <https://indico.cern.ch/event/1003975/>
  - Time : **March 31, 2021 @ 5pm CET**  

We're planning to have a packaging oriented meeting soon. We'll get in touch w/ Bob Dröge, who gave a nice talk ([link](https://indico.cern.ch/event/885212/contributions/4120576/)) on EESSI (European Environment for Scientific Software Installations) at the CVMFS workshop, to present. The date/time TBD.

Homework : Follow-up on the Eigen discussion we had prior to the Christmas break ([agenda](https://indico.cern.ch/event/949460/) for the original meeting).

### Software Training

1. GitHub Actions CI/CD training 16-19th Feb. Mentors and participants still welcome! <https://indico.cern.ch/event/1001128>
2. Please drop into our weekly training meeting 16h CET Mondays to kick-start a training activity.


### Event Generators

- Have started a discussion with Markus Dienfenthaler on possible needs of NP community.
- We understood that we can't get reliable HS06 values from CMS monitoring - after testing for the first time a single big GEN campaign that has the full info (i.e. not affected by the 18 month limit) - an issue that has been rolling on since Nov 2018 WS....
    - Instead, CMS is now going through a campaign with local runs where CPU->HS06 conversion is known and everything is under control. After some checks, we will discuss in an HSF GEN meeting.
- Did not make it to the Training WG meeting this week. Ideally we need to find time to discuss amongst ourselves first, but hope to discuss Generators needs in that meeting soon.
- In response to paper referee comment, we have been significantly expanding the discussion on the MP/MT usage in experiments for generators.
- Les Houches 2021 (<https://phystev.cnrs.fr>) will include some projects on generator software, including benchmarking, ML applications and migration to alternative architectures (largely GPU).

Q. When will the next WG meetings be? A. Not yet decided, but this year...

### Frameworks

First meeting of 2021 next week, discussing CMS's experience with upgrading to the latest UI of TBB. <https://indico.cern.ch/event/1005030/>.

* Make sure we schedule this meeting to avoid a clash with the CAF (Wed 16h30 start)

We plan to start "free-form-discussion" meetings once a month, to allow for an easier exchange of information. We will see how that goes...

## Other Interest and Activity Areas

### Differentiable Computing

Group is planning a second "campfire" meeting, Friday 12 Feb at 17h: <https://indico.cern.ch/event/1005490/>.

### Licensing

Graeme was in discussion with the Faser collaboration and advised them how to copyright and license their code. The usual formula of (C) CERN and license Apache 2 was advised and will be proposed to their CB.

---

## AOB

### Meetings next week:

- Software and Computing Roundtable, 17h Tuesday 9 Feb, <https://indico.jlab.org/event/420/>
    - I/O is the topic
- Compute Accelerator Forum, 16h30 Wednesday 10 Feb, <https://indico.cern.ch/event/975007/>
    - NVidia intro/tutorial on libcu++ & CERN IT/CM update on GPU infrastructure

### IRIS-HEP Feedback

We have been asked to give another round of feedback to IRIS-HEP at their next steering board meeting on 16 February. Can you think about feedback (the good, the bad, the ugly) to send via Graeme?

For reference, the feedback given last year is here: <https://indico.cern.ch/event/809181/>.

### Website

A few recent updates:

- A new link checker is in place, which checks all changed markdown files' links for validity
    - As this is a diff-check it is much more reliable than the old checker, which died under the weight of false positives
    - Still need to implement a more general checker that runs now and again to spot deceased links

### vCHEP2021

Registration has [opened](https://indico.cern.ch/event/948465/).

### Next Meeting(s)

- Next meeting will be 18 February
