---
title: "HSF Weekly Meeting #191, 30 July 2020"
layout: plain
---

Present/Contributors: Graeme Stewart, Stefan Roiser, Serhan Mete, Caterina Doglioni, Agnieszka Dziurda, Witek Pokorski, Efe Yazgan, Andrea Valassi, Kyle Knoepfel, Sebasiten Ponce, Sam Meehan, Liz Sexton-Kennedy, Witek Pokorski, Ben Morgan, Benedikt Hegner, Attila Krasznahorkay

Apologies: Eduardo Rodrigues, Teng Jian Khoo

## News, general matters, announcements

### Technical Notes

The best practices proposal note has been released as HSF-TN-2020-01 (<https://zenodo.org/record/3965581#.XyK7DS-w0gt>).

### IRIS-HEP Blueprint Meeting on *Sustainable Software in HEP*

<https://indico.cern.ch/event/930127/>

Well attended (up to 70) with a series of talks from HEP (ATLAS, CMS, HSFx2 (General + Training)) and other communities, like Software Sustainability Institute, AstroPy, The Carpentries.

In the breakout sessions there was a lot of interest in policy decisions in training and careers (important, but hard to turn into actionable items).

Summary and outcomes in preparation.

### ESCAPE Workshop on Open Source Software Lifecycles (July 23, 24 + 27, 28)

<https://indico.in2p3.fr/event/21698/>

Week-long (half-day/full-day) workshop organized by ESCAPE Project.

*Focus of the workshop:* expert/community (mostly astrophysics) talks, aiming to understand best practices on open source software in terms of development/licensing/...

HSF contributions:

* HSF Talk given by Lukas Heinrich (with Graeme's input)
* Benchmarking talk given by Andrea Valassi
* Also DM Test Science Project 5' talk

*Ultimate goal:* apply best practices to ESCAPE Software Catalogue
Best practices notes: <https://gitlab.in2p3.fr/jutta.schnabel/wossl/-/wikis/Best-Practices-for-software-development>

Some intersting topics: [CodeMeta](https://github.com/codemeta/codemeta) as a way to add metadata to software - hold this close to the code/developers, but then use it to power the catalogue; software archive project: <https://archive.softwareheritage.org/>.

Outstanding question: which facilities / "middleware" will be used to run pipelines? Could use the occasion for a joint session at the November workshop?

Licensing discussion: broadly in line with HSF conclusions (favour liberal licenses; labs holding copyright for telescopes). Overview of legal aspects was useful (Carina Haupt).

Q&A: try to increase involvement of theory and generator community.

### LHCC Review of HL-LHC Software and Computing

Report is attached to the agenda.

#### Highlight points

* HSF is generally praised for providing a discussion and coordination forum
  * Which is recognised by the experiments and the community
* Common software noted to be important and likely to be more important in the future
  * R&D for non-CPU devices noted
* Funding situation for computational improvements to generators does not fit into current scheme
* Improvements in generators and detector simulation are part of the CMS and ATLAS strategy and effort is needed here
* Lack of career opportunity is a risk
* Training and education are important

#### Common activity and projects examples

* Reconstruction algorithms
* Analysis preservation
* Common approaches and best practice for accelerators
  * *Have been discussing this in the SIDIS context and that could fit well as a joint activity*
* (Conditions) databases?
  * *That is verbatim what is in the report*
  * *DUNE actively working on that kind of infrastructure*
  * *CREST project was started in HSF, but was unclear how much the experiments bought-in*

#### Comments

* Formalise the role by which WLCG priorities can be transmitted to the HSF
  * *Have discussed with Simone doing this via the WLCG MB*
* Continue efforts on common software (ROOT, Geant4), in consulation with WLCG and LHC experiments
* Consider structures that would allow FAs to make formal commitments to software
  * *We agitate here generally, but actions?*
* Participate in intentaional standards bodies
  * *Community has representation on C++ committee; anything else?*
  * *Python is our other major language (they use PEPs); Python Software Foundation membership?*
* HSF could be involved in analysis preservation activities

Second review anticipated in 9-12 months on detailed R&D roadmaps.

**Encourage people to read the report and think about practical outcomes for the HSF.**

#### Authorship Progress

We agreed (16 July meeting #160) to broaden the author list of the HSF input document.

* Generators:
  * Agreed to use longer paper author list
* Simulation:
  * To be discussed
* Reconstruction:
  * we sent emails around, already several people replied and asked to be added, 
  * request from the LHCb for slightly changing the text about Allen. Proposed change: 
      > "Allen is a data processing framework for GPUs, as well as a specific implementation of a first-level trigger for LHCb. It will go into production for Run-3 data-taking at LHCb paired with a second trigger stage running on CPUs using highly vectorized code. Allen is optimised for sustaining the rate..."
    * Approved for the updated Snowmass version
  * Different contacts interpret "authorlist" differently (from 'everyone who worked in the project cited' to 'only those who gave input to the HSF document')
* Analysis:
  * Follow-up offline

Generally we favour an inclusive approach, so anyone reasonably connected to projects and development in the field can be an author.

Agreed to send a general email to hsf-forum, calling for people to contact the editors to add their names.

### New Convenor for Data Analysis WG

Reminder that nominations (including self-nominations) are open until 31 July for someone to join Paul and TJ (the appointment is to run from 1 September through 2021).

Please send nomintions to <mailto:hsf-search-committee@cern.ch> (which maps to Graeme, Liz and Michel).

*We have quite a lot of nominations now - many thanks to those who made them.*

### Snowmass

Reminder that announcements about the Snowmass process was sent to the email list, with an [initial workshop on 10-11 August](https://indico.fnal.gov/event/43829/).

We will submit the LHCC input document to the review (which we agreed did not need to go via an LoI).

### C++ Course

Following up e.g. on dicussions in the IRIS-HEP SW Sustainability workshop we want to propose a C++ course. Sebastien Ponce has created [a lot of material](http://sponce.web.cern.ch/sponce/C++Course/) and given the course in several occasions already (LHCb, ESIPAP). Some concrete ideas 

* Sebastien is willing to teach this courses
* Format (all virtual)
  * 2 hours of lecture sessions with moderated questions and answers in the morning
  * Afternoons free for exercises, students can join breakout rooms in case of problems
  * The morning after quick recap of the exercises before continuing with next training session
* Proposed weeks for first iteration are either 
  * 12 - 16 October (clashes: CSC (?), CMS S&C, ATLAS collab)
  * 19 - 23 October (clashes: ALICE mini week, ML workshop, Snowmass planning, FR + CH school holidays)
  * In this first iteration we plan to do the training in the morning CEST; in case of more iterations go for CEST afternoon trainings for the next one.
* Aiming for ~2 training weeks / year
* Limit for the first iteration to max 50 people to allow interaction (especially with virtual training). If successfull go higher for next iteration
  * Introduce "waiting list" if needed to also gauge the level of interest
* Tentative morning schedule:

| Monday | Tuesday | Wednesday | Thursday | Friday | 
| --     | --      | --        | --       | --     | 
| **Basics** (pointers, operators, references, compound types, ...) | **OO** (classes, inheritance, ...) & **C++ features** (auto, move sem., ...)| **Tools** (git, compile chain, gdb, valgrind suite)| **Advanced C++** (templates, lambdas, functors, STL, RAII, ..) | **Poll for extra session** (one of: Concurrency, Python/C++ interaction, Expert C++) 

**Afternoons (Mo - Thu):** Exercises with help by mentors in breakout rooms

***IMPORTANT*** We would need more mentors for the afternoon exercises !!!

Sam was contacted by someone from Orsay (?) also wanting to help with this kind of event. Can we recast the material into the HSF/Software Carpentry format? Example: <http://swcarpentry.github.io/shell-novice/>.

* There is now a repo, <https://gitlab.cern.ch/sponce/cpluspluscourse>, and can do a PR there (this is beamer format)
* Would want help to do this from other people

Limiting to 50 could be a "problem" - we think we would go way beyond that in interest we expect (200-300?).

* Organiser's idea was to restrict the numbers to allow interactivity during the lecture (otherwise we can scale up a lot)
* Sam noted it's hard to get honest input about what people's level actually is
* Experience is that only 50% of people actually turn up for tutorials, even with a emailed pledge

There are other formats that have been tried, with pre-recorded material (flipped classroom).

FNAL C++ course is also going ahead (already quite popular). All online this year. There is material available as well.

**In general this is received very positively. Continue to iterate on organisational details.**

## Working Group Updates

### Reconstruction and Software Triggers

* Together with the call for names of the HSF document, we asked for updates to text of the various open source / cross-collaboration efforts that we can put on your website (our summer project)

### PyHEP

* The [PyHEP 2020 (virtual) workshop](https://indico.cern.ch/e/PyHEP2020) was a success according to the general feedback that we got from the post-workshop survey and direct messages from attendees.
  * We will have a "debriefing meeting" on August 13th at 15h CET and will be happy to subsequently report at a future HSF coordination meeting.
* Eduardo got an invitation to present highlights of the PyHEP 2020 workshop to the EIC community at JLab, "to show there is a large and vibrant Python community in HEP with many developments for efficient and modern data analysis in Python".

### Software Tools and Packaging

* Released _prmon_ [v2.0.2](https://github.com/HSF/prmon/releases/tag/v2.0.2) last week:
  * Minor bug fixes and improvements on top of v2

### Event generators

* Received CSBS referee reports for the LHCC review paper. Positive feedback, quite a few comments to go through.
* Some of us participated in the Sheffield GPU hackathon this week. Extremely useful, we made quite some progress on Madgraph and got many ideas for further work that we need to digest.
* Still planning another meeting during the summer, maybe in one or two weeks, to report on the GPU work.
* It's confirmed that we should give a presentation to the LHCC in September.

## Other Interest and Activity Areas

### Differentiable Computing

* First "campfire" meeting Friday 31 July

---

## Workshops


### Future HSF-WLCG Workshops

Reminder:

* No face to face HSF/WLCG workshop in 2020
* Remote workshop in November (proposal is 19+20 (Thu, Fri) plus 22+23 (Mon, Tue) November)
  * Themes welcome now so that we can call for contributions after the summer
  * We should add this to Indico as a placeholder event...
* CHEP 2021 (17-21 May) still uncertain whether in-person or remotely
* attempt at face to face HSF/WLCG workshop in September 2021, potentially in Lund 

#### Mini-poll (put an X near one or more options, plus first X for attendance):

* I participated in this poll: XXXXXXX
* I would attend a pre/post CHEP (17-21 May) weekend event in person if CHEP takes place in person XXXXXX
* I would not attend a pre/post CHEP weekend event in person
* I would attend a pre/post CHEP weekend event remotely XXXXXX
* I would not attend a pre/post CHEP weekend event remotely 

**We would like to have additional input for organising the next events, so if you would like to help organise please contact HSF Coordnation or Graeme**

**We agreed to send an email out to hsf-forum with an update (inc. call for topics and organisers) as not everyone reads the minutes.**

## AOB

### Next Meeting

* We take a summer break during August
* Next meeeting slot is *3 September* (10 September is Jeune Genevois)
  * Followed by 24 September to go back to the usual every-odd-week Thursday schedule
