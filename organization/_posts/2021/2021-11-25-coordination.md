---
title: "HSF Coordination Meeting #219, 25 November 2021"
layout: plain_toc
---

Present/Contributing: Graeme Stewart, Nicola Skidmore, Paul Laycock, Ben Morgan, Andrea Valassi, Aniket Raj, Dorothea Vom Bruch, Efe Yazgan, Michel Hernandez Villanueva, Teng Jian Khoo, Gordon Watts, Michel Jouvin, Eduardo Rodrigues, Alexander Moreno, Josh McFayden, Stefan Roiser, Andi Salzburger, Liz Sexton-Kennedy, Sudhir Malik

Apologies/Contributing: It's Thanksgiving, so US colleagues excused! Pere Mato, Serhan Mete,

## News, general matters, announcements

### LHCC

- The talk (on Tuesday 16 Nov; see [today's agenda](https://indico.cern.ch/event/1043632/) for slides) was well received, just two questions: one on continued work on benchmarking generators between ATLAS and CMS (there are new CMS figures CPU/event and Josh is working on ATLAS numbers, but still no agreement about having total sample numbers); a second discussion of work on Spack as a build orchestrator (running over the main features, as a reminder to the referees)
- In the closed session Catherine highlighted a few of the topics we had raised in the slides and her conclusions were positive:
  - “The LHCC commends the CS bodies for their fundamental role in supporting the LHC experiments towards the success of their physics program.”
- Amber then gave some feedback about the HL-LHC review, which were preliminary and not a close out. From my notes the relevant things are:
  - Impressed by quality of documentation and presentations
  - From a technical perspective all activities showing excellent progress
  - CMS and ATLAS understand the performance/budget needs and have made progress in heterogeneous computing
    - Investments in R&D are important
  - G4 and the experiments have strong relationship - more coordination on fast simulation desired
  - ROOT makes excellent progress on RNTuple; RNTuple-lite viewed positively
    - Encourage more Pythonic/ROOT analysis interactions, which will strengthen efforts in both areas
  - HSF forums are useful in fostering positive collaboration
    - Particularly for generators and Pythonic analysis
    - Generators making progress, despite incentive mismatch
  - Rucio praised – espcially for CMS adoption, there is a need for a wider developer base
  - DOMA group has played a key role in coordination in that area
    - Detailed requirements still not established, working assumptions of x10 need to be pinned down
    - Exercises that increase in scope and complexity will help understand the challenge
- As we already understood there will be a draft report in December with a final, public, report expected in January (expect more observations than recommendations)
- Next steps not decided at the moment

### HSF Talks

#### Snowmass Small Experiments Workshop

There was a Snowmass Small Experiments Workshop [last week](https://indico.physics.lbl.gov/event/1756/overview). Liz gave the HSF talk.

- Small experiments does not mean small computing problems
  - They have with less human resources to tackle the issues
- Data management is often at the PB scale, which is well beyond management by hand
- Great reliance on common software, like ROOT and Geant4
- Small cosmic experiments are often west coast US based, which is a hard TZ for collaboration with CERN and Europe

One practical follow-up would be in the context of the ESCAPE workflows activity (Caterina is our contact there). We want to follow-up on that next year.

There is a follow-up report document to which we can contribute (join the "computingforsmallexps" channel in the Snowmass Slack).

### ASCR Workshop on the Science of Scientific-Software Development and Use

There is a DOE supported [ASCR workshop](https://web.cvent.com/event/1b7d7c3a-e9b4-409d-ae2b-284779cfe72f/summary) 13-15 December on scientific software. There is a call for [position papers](https://web.cvent.com/event/1b7d7c3a-e9b4-409d-ae2b-284779cfe72f/websitePage:5c30ffe5-b577-491f-8d8d-1f745b03e9ec): *We invite community input in the form of **two-page position** papers that identify and discuss key challenges and opportunities in the science of the scientific-software development process and the study of the use of scientific software.*

It was felt to useful to submit a paper to this, so Graeme, Liz and Eduardo wrote/contributed to [what we submitted](https://docs.google.com/document/d/1f3wcOgE8tqh-Q88A3wzQrZaWhLazPl196g1lLkv0XZo/edit?usp=sharing).

- We seem to be more of an "interesting problem" than a solution in this space, but no bad idea to throw our hat into the ring.*

## Working Group Updates

### Mandates for 2022

We have started to think about WG convenerships for 2022. For WG convenors, please let Benedikt know your plans.

- Normally WG conveners serve for 2 years, by mutual agreement (but this is not set in stone).
- Most conveners want to continue; some would make space for younger replacements if there are any.

Outcome: we anticipate a call for WG conveners in 7 of the 8 groups (the exception is Simulation where everyone stays on). The search committee would by default be Graeme, Liz, Michel and Benedikt.

Email will be sent on Monday with a call for nominations and a 2 week window.

### Data Analysis

- Metadata document now in [overleaf](https://www.overleaf.com/read/cxkkdqdrrfcf), to be submitted to CSBS. Need ORCIDs and institute info from people still (probably searchable)
- Will have meeting before Xmas on workflow management tools - potential benchmarks here
  - Have spoken to 'Luigi' developers, planning to find (LHCb?) speaker on SnakeMake and possibly also CWL
- Start of 2022, may arrange a meeting on representing/book-keeping systematic uncertainty variations
- Will there be a HSF workshop in the Spring?
  - IRIS-HEP is also thinking about this, and due to the CHEP cancellation, the corresponding dates (May) may be an appropriate time
  - People in HSF seem generally keen as well
  - Analysis ecosystem is the preferred topic, practical to keep it constrained (hybrid, ~60-70 attendees)
    - Aim to put together organising team by end of the year
    - Gordon can look into option to host in Marseille

### Detector Simulation

- Presentation on December 13th on FPGAs for simulation:
  - <https://indico.cern.ch/event/1096432/>
- Now thinking about/planning meetings for 2022
- Talk on simulation at Snowmass small experiment workshop
  - <https://indico.physics.lbl.gov/event/1756/contributions/6251/>
  - Noted that all small experiments rely heavily on Geant4 and need it to be sustained by the FAs

### Reconstruction and Software Triggers

- One outcome of 2021 survey for Reconstruction was the need/request for R&D detector dataset:
  - Open Data Detector - Tracking System (follow-up of TrackML detector) to be ACTS-free (MR + ACAT poster)
  - Calorimeter system will be added as part of a bigger initiative of CERN EP-R&D allows full Geant4 simulation of realistic tracking (including timing) + calorimeter
- Also a [HSF PHOENIX](https://acts-project.github.io/odd-phoenix/docs/) version available.

### PyHEP

- The last topical "Python Module of the Month" meeting of the year will take place on December 8th and will be devoted to PyTorch. Agenda at <https://indico.cern.ch/event/1098618/>.
  - Training frameworks were quite disucssed at the LPCC Fast Sim workshop this week

### Software Tools and Packaging

- Nothing new to report.

### Software Training

- Next Sotware Carpentries workshop in preparation. Link to [Indico page](https://indico.cern.ch/event/1097111/)
  - Instructors from Software Carpentries have been asigned. They will cover the basic part the first two days (Bash, Python, Git).
  - ROOT team confirmed for teaching on last day.
  - Registration will open soon.
- Matplotlib module development in progress ([link to GitHub](https://github.com/hsf-training/hsf-training-matplotlib)).
  - Organized for a tentatively 2-day workshop.
  - Chapter of data vs MC comparisons being prepared with open data from ATLAS.
  - Comments are very welcome. Take a look at the PRs on the repository.
- HSF/IRIS-HEP Training contribution at ACAT 2021
  - Link to the contribution: <https://indico.cern.ch/event/855454/contributions/4604988/>.
- C++ Course Organisers are splitting the course into two parts: *essentials* and *advanced*
  - Hope to run the first edition of the *essentials* version w/b 17 Jan

### Event Generators

- Interesting discussions on generators at the first ECFA meeting on generators for future colliders, <https://indico.cern.ch/event/1078675>.
  - Andrea gave a talk on the HSF generator WG and on the work on MG5aMC for GPUs and vector CPUs.
  - Andrea: Michelangelo gave a talk on a new "Future Colliders" Unit at CERN. It would be useful to get in touch and discuss possible collaborations/interactions with HSF for software and computing.

- There seem to be quite a few interesting generator-related talks at the upcoming ACAT next week, <https://indico.cern.ch/event/855454/timetable/#all.detailed>.
  - Gordon: ACAT has a dedicated track (track 3) specifically about joining theorists, phenomenologists and computing. Looking for new people to contribute to this track.

### Frameworks

- We are scheduling a meeting with CMS developers regarding their efforts in making thread-unsafe generators work with a multi-threaded framework. Exact meeting date is TBD (perhaps as early as Dec. 1).
  - Andrea: please keep the event generator WG conveners in the loop.

---

## AOB

### Snowmass Slack

Noted that this was funded through Snowmass and funding will last for at least the duration of the process. Can it be continued beyond? Could the HSF help argue for that?

- Better to be funded by an academic institute (large discount cf. normal price)
- CERN has Mattermost (open source, but it has to be hosted)
  - But could one import the existing data, which is important?

### Conditions Databases

A new HSF Activity for Conditions Databases?  BNL are adapting the Belle II conditions database design, which largely follows HSF CWP best practice, for the sPHENIX experiment.  In so doing they are taking this as an opportunity to design something that incorporates as much of the experience and expertise from other experiments as possible.  Paul Laycock, Andrea Formica and Giacomo Govi are interested in attempting to define "the" API for a conditions database (independent of technology choices).  Other interesting discussion topics would be technology choices for the server, payload serialisation, calibration workflows, etc.  This also relates to the relevant parts of the Data Analysis working group's "Metadata" summary paper, paeticularly analysis global tags.  The interested community is small but that makes knowledge exchange all the more important.  Would it make sense to make this an HSF activity?  It already covers experts from ATLAS, CMS, Belle II, DUNE and sPHENIX!

**We shall discuss this proposal in more depth at the next meeting on 9 December.**

### GPU Hackathon

- Advert for a GPU hackathon in the UK under the UKRI umbrella:
  - <https://www.gpuhackathons.org/event/uk-national-gpu-hackathon-2022>
  - UK focussed (and GMT timezone...), but can have international groups.
  - Andrea: there are many more such events elsewhere too, <https://www.gpuhackathons.org/events>. They all seem digital for the moment, except a physical one in Berlin in March 2022.

### Next Meeting

Next meeting 9 December.

Meeting slots in [Indico](https://indico.cern.ch/category/7970/) for next year are now booked. We follow the usual pattern, odd numbered weeks, giving us first meetings on 6 and 20 of January.
