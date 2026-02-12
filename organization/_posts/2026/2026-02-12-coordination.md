---
title: "HSF Coordination Meeting #302, 12 February 2026"
layout: plain_toc
---

## Attending

Present/Contributing: Graeme Stewart, Eduardo Rodrigues, Claire Antel, Ruslan Mashinistov, Peter Fackeldey, Inês Ochoa, Philippe Gras, Menglin Xu, Da Yu Tou, Juan Miguel Carceller, Stephen Mrenna, Saptaparna Bhattacharya, Juraj Smiesko, Stephen Mrenna, Liz Sexton-Kennedy, Caterina Doglioni, Dmitry Kalinkin, Joshua Isaacson, Michel Villanueva 

Apologies/Contributing: Alexander Moreno, Maarten van Veghel, Stefan Roiser

## News, general matters, announcements

### 2026 conveners

The process is now finalised and the new teams of AA conveners for 2026 are set up.

We thank the newcomers for accepting to join us as a new AA convener for this year, and warmly welcome them!

Thank you also to the several of you that continue as a convener this year, and those who stepped down at this point!

Homework: *Please [make PRs](https://hepsoftwarefoundation.org/howto-website.html) to update the names of the conveners on the website.*

### HSF Seminar Series and Compute Accelerator Forum

Planned HSF seminars:

- Seminar from creator of mp-units (supports units and constants in C++, see AOB): [25th Feb](https://indico.cern.ch/event/1642384/).
- Seminar on HS3: [25th March](https://indico.cern.ch/event/1622602/)
- Seminar by Kati Lassila-Perini (chair) on ICFA Data Lifecycle panel [best practice recommendations](https://icfa-data-best-practices.app.cern.ch/): [29th April]
    - Format: recommendations first, then discussion on mapping to HSF Project Guidelines. 
        - Question for us / SG: what would we like out of this mapping? Support / mention of HSF guidelines and supported projects? (ICFA represents a different audience wrt our current circles)
        - Thinking about this until a months time, then discuss again in Coord meeting

- 2nd in series on AI-assisted SW tools organised by software tools & packaging - possibly separate seminar organised with sustainability group.

(Thanks to the activity groups for coming to us with seminar ideas and speakers!)

HSF seminar conveners are reachable at <mailto:hsf-seminar-conveners@googlegroups.com>.

Please send your suggestions for next seminars.

### Steering Group & Advisory Group

The 2026 Advisory Group meeting happened on February 11th. The feedback will be discussed at a near-future SG meeting and actions will follow.

Confirmed date for the **next WLCG/HSF Workshop is 2-6 November 2026, Bologna**.

### HSF Affiliated Projects and Software

List of current reviews underway:

- DIRAC / DIRAC X - done, sent an email to Eduardo + DIRAC reps, being cross-checked
- NoPayloadDB Conditions Database - ongoing
- Pepper - ongoing
- MadGraph5_aMC@NLO - done, will be sent to SG for review
- Pythia - ongoing (mostly done)

Do not hesitate to discuss around you to identify relevant projects/libraries that could engage with the affiliation programme.

Thank you very much to those who accepted to act as a "reviewer" or spontaneously put themselves forward. This is super appreciated; it makes all the difference.

Very positive feedback from the Pythia developers about the process!

## Activities Updates

### GSoC 2026

There are 31 proposals for this year's GSoC, 1 more in the pipeline.

- Mentoring organisations applied on 3 February
- Approval will come on 19 February

### Software Training

Next Training Events

- Analysis Reproducibility Training
    - Week of April 27 or May 4.TBD
    - Modules: CI/CD GitHub Actions, Docker/Podman, Apptainer, CI/CD GitLab, and REANA 
- 14th HEP C++ Course and hands-on training, 9 - 13 March (hybrid)
    - <https://indico.cern.ch/event/1617123/> 
    - Registration is still open

### Event generators

- Submitted two GSoC projects on negative weight mitigation using the cell resampling technique. Envision one project to be more theory based (running cell resampling at NNLO with MCFM), the other one is more ATLAS specific.
- Would like to meet with new conveners for a plan for the rest of the year.
- Steve noted a lot of activities (many in US context) that the group can help to raise awareness of.

### Detector Simulation

- Next [WLCG environmental sustainability forum](https://indico.cern.ch/event/1644632/) (Feb 18th) is on speeding up detector simulation

### Data Analysis

- Had a discussion of possible topics for 2026
- Considering a seminar series on "ML in analysis" covering topics such as SBI, unfolding, etc. (would aim for spring)
    - Would be nice to collate the discussions into a review paper
        - Could be a "5 years on" to [arXiv:2010.06439](https://arxiv.org/abs/2010.06439), but quite some overlap with [Simulation Based Inference Blueprint](https://indico.cern.ch/event/1600677/overview)
    - Could have a workshop at end of summer/early autumn (need to consider who would support this)
    - There is a nice *synergy* with *event generators* (Sapta will reach out to them); and *Julia* based analysis (Philippe will reach out)
- Would like to push again on reproducibility/reinterpretation topics (workflow managers, REANA, HS3, etc.)

### PyHEP

- PyHEP.dev 2026 workshop in planning stage:
    - Will be in Amsterdam (Nikhef) (95% confirmed)
    - Possible weeks: Sep 7-11, Oct 19-23, Nov 9-13 
    - Workshop length ~3-3.5 days
- 2 new convenors: Alexander & Dmitry -> First meeting next week Feb. 19

### JuliaHEP

- JuliaHEP 2026 will be in Munich, October 19-23. We will start advertising the event soon!

- JuliaCon 2026 - JuliaHEP Mini-Symposium
    - JuliaHEP Mini 2026 - Julia for Nuclear and Elementary Particle Physics: From Precision Science to High-Performance Tools
    - Call for contribtions to JuliaCon is now out:

> Dear colleagues,
We invite you to submit proposals to give a presentation (talk or poster) at JuliaCon Global 2026 in Mainz, August 10-15, 2026 (https://juliacon.org/2026). JuliaCon has traditionally featured talks that ranged from introductory to advanced, on topics related to various fields, delivered by developers and researchers from industry and academia. If you have worked with or on Julia in the past, JuliaCon is the best venue to share your work with the Julia community.
The Call for Proposals (<https://juliacon.org/2026/cfp/>) will close February 28, 2026.
We look forward to hearing from you.
The JuliaCon 2026 Organizing Committee

- [Julia in ErUM: Get Started with Julia](https://indico.desy.de/event/51336/) - happened last week, Feb 6. Alex and Oliver led the tutorial sessions and there were excellent short keynotes.
    - About 70 attendees at peak (good retention!)
    - This Friday there be an *office hours* session as a follow-up to the event

### Software Tools and Packaging

- Evaluating the "Multi-platform builds of HEP software on conda-forge for distribution" project <https://github.com/hep-packaging-coordination>
    - This should be the open source version of conda-forge 
- Can HSF help with the project promotion?
    - It could become an affiliated project
- Ruslan is working on it. They wish it to be done before CHEP. Let's see if we can make it.

Liz: what is the status of conda-forge and open source projects?

- There are open source versions of conda repositories (specifically [*conda-forge*](https://conda-forge.org)) as well the Anaconda commercial one, *defaults* (pay per view, watch out!).

Philippe: Julia packaging is also interesting in this space.

Eduardo: SHiP and LHCb have recently been looking at this space again. Could organise an HSF event (mini workshop?) around this topic. Could be a topic at the next WLCG/HSF workshop as well (that will take place in Nov.), although not to leave everything until then.

## AOB

### Physical Constants / HEPdata Library

Reminder that we proposed a C++ header-only library that defines physical constants and some salient HEPdata in a lightweight, easy-to-use manner. Also taking into account versioning.

We have reactivated this!

- Christian Wessel has expressed interest to help
- Proposed MVP is a *versioned* set of constants derived from CODATA releases
    - Not using types with attached units (see mp-units seminar above)
- We will start a Google Doc with some desiderata and design questions
- Poll for meeting w/b 23 February

Contact Graeme if you want to be in the loop.

### Next Meeting

The next coordination meeting will be on February 26th.

### Chair This Meeting 👇

Please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing a future coordination meeting. (There is even a [HOWTO guide](https://hepsoftwarefoundation.org/organization/running-meetings.html)).
