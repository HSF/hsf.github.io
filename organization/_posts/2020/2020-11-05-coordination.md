---
title: "HSF Weekly Meeting #196, 5 November 2020"
layout: plain
---

## The [Gunpowder, Treason and Plot](https://en.wikipedia.org/wiki/Gunpowder_Plot) meeting

Present/Contributors: Graeme Stewart, Serhan Mete, Eduardo Rodrigues, Kyle Knoepfel, Attila Krasznahorkay, Andrea Valassi, Teng Jian Khoo, Kilian Lieret, Witek Pokorski, Efe Yazgan, Allie Hall, Michel Jouvin, Caterina Doglioni, Stefan Roiser, Josh McFayden, Pere Mato, Benedikt Hegner, Chris Jones, David Lange, Gloria Corti, Philippe Canal, Stefano Piano, Daniel Elvira, Witek Pokorski, Sam Meehan

Apologies: Paul Laycock, Ben Morgan

## News, general matters, announcements

### Letter of support for CSSI

Last week we approved a letter of collaboration for the CSSI call for *Elements: Machine Learning Quark Hadronization* (Jure Zupan, Phil Ilten). Project description and the letter are attached for reference. The project is very well aligned with our Physics Generator Working Group, so we were happy to propose collaboration should it be funded by the NSF.

### Working Group Convenors for 2021

Liz, Michel and Graeme have been polling our current convenors and we're close to knowing which positions will be open for next year. Hope to be able to make a call next week.

### HEP C++ Course and Hands-on Training

Was held [12 - 16 October](https://indico.cern.ch/event/946584/) with 50 participants. Lecture recordings are available on the Indico page. Very lively discussions and very good feedback from students. Many thanks again to Sebastien Ponce as lecturer and [all mentors](https://e-groups.cern.ch/e-groups/Egroup.do?egroupId=10387430).

Another 180 people on a waiting list. In a post-mortem meeting we decided to go for another iteration with 75 participants max. Tentatively in the week of

**18 - 22 January 2021** --> *Please check if there are any clashes!!*

(We will open registration anew, but let people on the waiting list know.)

If you want to help us promote training please consider using the info from this [propaganda slide](https://cernbox.cern.ch/index.php/s/s7V9FOVDejElBaD).

Attrition rate was very low!

Can improve the afternoon organisation for the students. Some of the rooms were rather quiet.

Attila - should we also discuss higher level concepts (singletons, factory pattern)? Liz - singletons are very concurrency unfriendly though.

- There will be a meeting to discuss the curriculum later.

### Compute Accelerator Forum

Next meeting, [Wed 11 Nov, 17:00 CET](https://indico.cern.ch/event/962110/) with talks given by David Rohr (ALICE) and Daniel Campora (LHCb) on their experiments' approaches to abstraction of GPU hardware.

Currently discussing with Nvidia the possibility to have a seminar style presentation on either the NSight profiling suite or libcu++ for the [Wed 9 Dec, 16:30 CET](https://indico.cern.ch/event/962112/) meeting.

Tentative dates and times for 2021 -- 2nd Wednesday of the month at 16:30 -- have been entered in the [indico category](https://indico.cern.ch/category/12741/).

Please subscribe to [compute-accelerator-forum-announce@cern.ch](https://e-groups.cern.ch/e-groups/EgroupsSubscription.do?egroupName=compute-accelerator-forum-announce) to receive notifications.

## LHCC

### WLCG Software Liaisons

The WLCG has appointed Graeme Stewart and Liz Sexton-Kennedy as their software liaison contacts. Graeme and Liz will take care of reporting for software groups and for communicating WLCG needs back to developers.

- No intention for the current lines of communication between experiments and projects to be cut, but WLCG is an all-experiment forum that can be useful for setting priorities as seen by the WLCG
- Generally we want to improve communications between computing and software, e.g., organise a one-shot workshop on I/O matters

### Referees Meeting

There is an LHCC Referees Meeting with WLCG on Tuesday 17 November. Graeme will give a (general) software update (20' slot). Please send any input that you have.

### HL-LHC Software and Computing Review

We also expect to get news about the charge from the LHCC about the next phase of the review of software and computing for HL-LHC, this time focussing on common software projects, that should take place in Autumn 2021.

## Website

### Profiles/`floating heads'

- [Github issue](<https://github.com/HSF/hsf.github.io/issues/835>) was resolved with [this merge](https://github.com/HSF/hsf.github.io/pull/843)
- Floating heads can be used to either:
  - show a community of people (based on a selection tag in the profiles): [example for hsf training community](https://hepsoftwarefoundation.org/training/community.html)
  - or show selected people, e.g. conveners: [example for training](https://hepsoftwarefoundation.org/workinggroups/training.html#convenors)
- You can add social media or a quick text to your profile
- [This page](https://hepsoftwarefoundation.org/howto-profile.html) shows how to add a new profile. Basically each profile corresponds to a small markdown file.
- To add a selection of people (e.g. conveners) to a page, see [this file](https://github.com/HSF/hsf.github.io/blob/master/_workinggroups/training.md) as an example
- If you want to add more information like phone number, you can just add it in the  profile text (or is there a nice way to turn the phone number into an "icon" with a link?)

## Working Group Updates

### Data Analysis

- First chat with new conveners last week
- Should reconvene to plan 2021 activities
- [IRIS-HEP workshop](https://indico.cern.ch/event/960587/) last week on Future Analysis Systems and Facilities

### Detector Simulation

- LPCC workshop took place Monday, Tuesday this week. Experiments presented their physics results as far as Geant4 simulation was concerned. Overall agreement is very nice. Still a few remaining issues concerning the shower shapes (both EM and hadronic), recent improvements in Geant4 could potentially help there. Test-beam data is extremely useful for any Geant4 development. More effort should be certainly invested in making standalone Geant4 testbeam simulation that could be included in the Geant4 validation suite.
- Agenda for the HSF workshop ready and speakers confirmed.
- Planning to have the next topical meeting on 16th of December devoted to the definition of validation strategies for Deep Learning-based fast simulation models as well as the challenges related to the integration of those tools into the full-simulation frameworks.

### Reconstruction and Software Triggers

#### Meetings

- Next meeting (18 Nov 2020, 16:45): joint with Long-Lived Particles Community for reco & trigger issues of experiments targeting LLP and dark sectors (1h15'). Builds on contacts we had during the LHCC common software document writing.
- Agenda is here: <https://indico.cern.ch/event/972296/overview>
- Abstract submission not yet open, but we need to open it by the end of this week.
- Question: do we want to make it more HSF-wide?

- December meeting (TBC): summary of FastML workshop

#### Other

- Recently "connected" a student looking for fellowship projects to a project (that the conveners knew about) --> something we want to think about more?

### PyHEP

- PyHEP 2020 workshop “proceedings”:
  - Eduardo minted DOIs on Zenodo for all talks and notebook repositories, see <https://zenodo.org/communities/pyhep2020>.
    - Semi-related Q from Caterina: is there common code for doing this? It would be useful for ESCAPE/DM initiatives & other conferences
    - Reply: not that I'm aware of. You need to go and add the info by hand. Some bits can probably be automated, but not all. See on the link above the kind of info each entry has (metadata).
    - Thanks! So I continue with v2 of a Bachelor's project to automate this for future conferences :)
  - Eduardo to prepare a report for the Python Software Foundation.
  - Final email with various bits of info (presentations and "proceedings", videos links, WG communication channels, workshop "photos", survey results summary) will soon be sent to participants.
- Topical WG meetings:
  - Meeting on “HEP Statistics Serialization Standard” with ROOT, zfit and pyhf people postponed to early 2021.
  - Other topics such as automatic differentiation, Numba and JAX are under discussion.

### Software Tools and Packaging

- We will have a group coordination meeting next Monday morning to discuss future activities, meetings, and strategies.

### Software Training

- Alessandra, Meirin et al: GPU + ML Training ongoing this week
- Thinking of organizing a "Training hackathon" last week before the holidays, e.g. Dec 15 - ?
  - Idea:
  - Spread over a couple days
  - First day: Discuss about the most needed training modules
  - Next few days: Hacking
  - Final day: Presenting results
  - Financial support from IRIS HEP? "pay for training content" - [link to document](https://docs.google.com/document/d/1BcI0jS_SWsQdeYZAt02ciIDtW-ATT4WapOhuIPx2B7M/edit#heading=h.957y35c35e4m) (please feel free to comment)
  - Will advertise this hackathon at the HSF meeting in November
- Might use <https://allcontributors.org/> to credit everyone who contributes to specific training module
  - This is a github bot, so you can just write `@all-contributors please add @name for code` and the rest happens automatically
  - Great possibility for any project where you want an easy way to credit contributors
  - can credit different contributions: e.g. issues, PRs,  all the way to design
- Training modules under development:
  - Emery Nibigira: CICD with Github actions (currently factoring out some intersection with CICD gitlab; thinking of technical solutions to keep them in sync)

### Event generators

- Preparing the generator session at the HSF workshop. Four talks so far: two on GPUs (MadGraph and VegasFlow/PDFFlow) and two on negative weights (MC@NLO-Delta and neural resampler). Discussing whether we want to invite 1-2 more talks and which one, and also whether we should have a slightly longer session.
- Generator paper has been sent to CSBS and uploaded on <https://arxiv.org/abs/2004.13687v3>.

### Frameworks

- Still looking at continuing our metadata discussions -- will likely hear from _art_ and/or DUNE next.

---

## Workshops

### HSF-WLCG Virtual November Workshop

Workshop dates fixed 19, 20, 23, 24 November (pm CET). Agenda is pretty much finalised now.

- For the open session we had many more abstracts than we could fit in (even making a few of them lightning talks). We forwarded information about the ones we didn't have time for to the WG convenors as possible subjects for topical meetings.

Indico: <https://indico.cern.ch/event/941278/>.

Registration open 170 people signed up so far - **please sign up yourself**.

- Reminder beginning of next week?

Good advertising so far: HSF, Belle II, ATLAS, CMS, LHCb, ALICE (asked), DUNE (asked), Geant4

**But please help broadcast to other communities as well.**

## AOB

Intel Developer Summit 2020, <https://webinar.intel.com/oneAPIDeveloperSummit2020>

### Next Meeting

- Please check the [HSF Calendar](https://hepsoftwarefoundation.org/future-events.html) to make sure that events for 2021 are listed correctly
- Next meeting scheduled for 19 November, but this is the workshop
  - We agreed to have a "virtual" meeting where people post updates to the live notes, but we don't have a call
