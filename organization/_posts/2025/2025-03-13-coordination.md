---
title: "HSF Coordination Meeting #283, 13 March 2025"
layout: plain_toc
---

## Attending

Present/Contributing: Liz Sexton-Kennedy, Graeme Stewart, Peter Fackeldey, Christian Wessel, Tommaso Lari, Claire Antel, Juan Gonzalez, Paul Laycock, Mark Neubauer, Juan Miguel Carceller, Marcel Rieger, Alexander Moreno Briceño, Michel Hernandez Villanueva, Michel Jouvin, Luke Kreczko, Maarten van Veghel, Sapta Bhattacharya, Stefan Roiser, Torre Wenaus, Ruslan Mashinistov

Apologies/Contributing: Eduardo Rodrigues


## News, general matters, announcements

### European Strategy Update (EPPSU) final stages

The up-to-date version of the document is at this [CERNbox URL](https://cernbox.cern.ch/s/XQ3wEp3L8UOVjjb) (we always keep this link).

After some feedback, we made a set of small changes to the text: grammar/spelling mistakes, minor factual corrections, rephrasing some sentences for clarity. The set of changes from the original draft are captured [in this PR](https://github.com/HSF/EPPSU-2025-Paper/pull/14/files#diff-ca1a9fbc25dc75daae9680150d6e7e28444a27eaeb06f3432b7c78f3fa0e3652).

We have also decided on the cover page format:

> The Critical Importance of Software for HEP
>
> Prepared by the HEP Software Foundation, with inputs from the HEP community.
>
> Edited by: LIST OF ALL EDITORS
> 
> This document has been endorsed by the following experiments and communities:
> 
> LIST OF ALL EXPERIMENTS AND COMMUNITIES

Action:

- Editors, please fill in your name, institute, ORCID in this [spreadsheet](https://docs.google.com/spreadsheets/d/1SFcJkI0bBoGs5av1o80apeMCXYWd8P-8PEbEJ-odlpI/edit?usp=sharing)

Discussions with the experiments have so far been positive - certainly no blockers have been raised. We also decided to reach out to ePIC/EIC and FCC and have invited them to endorse the document.

CMS Discussion: want to have the same endorsment from all of the experiments, at the experiment level (not just individuals or sub-groups, like S&C). Graeme and Michel will follow-up as needed.

### HSF/WLCG Workshop announced

Taking place on 5-9 May at IJClab, Orsay, Paris. The workshop was announced to the WLCG and HSF communities on Feb 20. Registration is now open, see the [indico site](https://indico.cern.ch/e/wlcg-hsf-2025).

Local organisation is basically all settled. Some concerns about US participation due to possible funding issues, but this may not be the case.

Abstract deadline is now 23 March. More abstracts are definetely needed - please submit something!

Plenary programme is in good shape, firming up.

People are invited to register ASAP so that the local organizers can better prepare for the event. Please note that the early-bird registration deadline is Thursday April 3. Registration closes on April 22.

The timetable has been filled with the different sessions. While the agenda of each session is work in progress, the coarse timetable will not significantly change. This should allow people to start planning for their participation. The event will be an in-person event with (limited) possibility for remote participation. Given the nature of the event (an interactive workshop) we encourage in-person participation.

The HSF organisation team is Michel, Nicole, Eduardo, Paul.

### HSF Seminar Series and Compute Accelerator Forum

[Seminar Indico Category](https://indico.cern.ch/category/18810/).
[Compute & Accelerator Forum Category](https://indico.cern.ch/category/12741/)

There is an HSF seminar on technical debt in software at the end of this month, agenda already prepared:
https://indico.cern.ch/event/1520114/

Trying to organise a C&AF on *Julia and GPUs* with Valentin Chauray - joint event with the [EVERSE Network](https://everse.software/network/).

HSF seminar conveners are reachable at hsf-seminar-conveners@gmail.com
* Please send your suggestions for this Spring seminars

### Steering Group

No SG meeting since our last CG.

### HSF Affiliated Projects and Software

*We need to find people to help do these reviews.* They are fairly lightweight and should not take a lot of time - we are checking usefulness and impact in the community, as well as software development and project best practices.

As suggested last time a [google spreadsheet](https://docs.google.com/spreadsheets/d/1GCy9Me2mroTdZLtWOdblHyrfkap9BOZp06XkXEd_XYM/edit?gid=0#gid=0) has been set up where people can indicate their willingness to participate as a reviewer in their areas of expertise. Please sign up! And thank you to those who already have. There is also a tab 'Projects' to gather planned and suggested projects for reviews.


**[Link to the review template](https://docs.google.com/document/d/1l8Tkruo0EEHwgRBQPmiHq-i4BuwwiR1choRRMUIv6qY/edit?usp=sharing)**

The Steering Group agreed to approach Dirac, Rucio, ACTS, HLS4ML and XrootD to discuss engaging. A few positive conversations have been had; more discussions planned.

Many aspects of the affiliation are independent of new versions - don't need a big re-review.

Conditions database software developers were positive and are taking steps to improve documentation. Torre will follow-up with them on the best timescale for them.

The Training Group will offer to help projects who want to improve their tutorials (this is required for a Silver badge).

## Activities Updates

Planning chats between activity conveners and SG liaisons are underway.

| Group                                | SG Liaison        | Status
| ------------------------------------ | ----------------- | ----------|
| Data Analysis                        | Mark and Eduardo  |
| Detector Simulation                  | Torre             | Done |
| Physics Generators                   | Stefan            | Scheduled |
| JuliaHEP                             | Pere              | Scheduled |
| PyHEP                                | Eduardo           |
| Reconstruction and Software Triggers | Claire and Paul   | Done      |
| Tools and Packaging                  | Liz               | Done      |
| Training                             | Nicole and Graeme | Done      |

The AA conveners should also feel free to reach out to their liaison to speed the planning!

Please remember to update your activity page on the HSF website with the names of the current conveners.

### Mailing List

The activities list has been renamed to <hsf-activities-conveners@googlegroups.com>.

### General Standing Reminders

#### Website banners

We have the ability to put event banners on the HSF website. All it requires is a markdown file with the event data. See, e.g., files [here](https://github.com/HSF/hsf.github.io/tree/main/announcements/_posts/2023).

#### Meetings

Please try and book meetings in Indico at least 2 weeks in advance!

That way they go into the calendar early and they will be included in the weekly email announcement that goes to HSF Forum.

#### Videos

When meetings are recorded (recommended), please try to put them onto:

- [HSF YouTube channel](https://www.youtube.com/c/HEPSoftwareFoundation) (ask for permission to do this)
- <videos.cern.ch> (recommended over posting directly)

Then post links to these locations. See [C&AF](https://indico.cern.ch/category/12741/) for examples.

## Activity Updates

### Data Analysis

No report today.

### Software Training

Ongoing events:

-  [12th HEP C++ Course and Hands-on Training - The Essentials](https://indico.cern.ch/event/1477096/) - Mar 10-14.
    - Participation:
        - In-person: 22/25
        - Remotely: 115

- [HSF/IRIS-HEP Analysis Reproducibility (Virtual)](https://indico.cern.ch/event/1508102/) - March 24-28. 48 people registered so far. Registration open until March 21.

- [HSF/WLCG Workshop](https://indico.cern.ch/event/1484669/) - May 5-9
    - We will have a dedicated training session


Future events:

- [HSF/IRIS-HEP Software Basics Training (Hybrid)](https://indico.cern.ch/event/1516608/) - Jun 18-20. Hybrid at CERN
- [Deep Learning Train-the-Trainer Workshop](https://indico.desy.de/event/47263/) - Sept 15-19. Organized by HSF and ErUM-Data-Hub. In-person in Potsdam

HSF activities: What is your interest in Training?

- Event Generators?
    - We could consider a training for FCC-ee: there is a tutorial planned for the FCC-ee meeting at Fermilab/Argonne (https://indico.fnal.gov/event/67484/). Remote participation is (probably) possible because that was an option at the time of registration 
- Python - Essentials and Advanced?
- Data Analysis?


### Software Tools and Packaging

- Chat between activity conveners and SG liaison
    - Discussed some ideas the activity conveners came up with in a previous meeting


### Detector Simulation

[Slides](https://docs.google.com/presentation/d/1UpIv9E04xQQhNL1MkDt7eicZwTKFWVVIM7ECxeHebL4/edit?usp=sharing) with a summary of the activity in 2024 and the plans for 2025.

Discussion:

- Clarifying the license for MRADSIM would be needed - is it long-term trustable?
- Could "promote" GPU sim presentations to HSF Seminar? It would be of wide interest, beyond simulation experts. Tommaso to liaise with seminar organisers.

### Reconstruction and Software Triggers

No report today.

### PyHEP

PyHEP.dev (July 14-18, Seattle): Waiting for feedback from local organisation to estimate our budget. 

PyHEP (Oct 27-30, Zoom): Reviewing documents and the agenda from the previous event to create a poll for participant interests before planning topics.

### Physics Generators


### JuliaHEP

Planning well underway for [JuliaHEP in Princeton](https://indico.cern.ch/e/juliahep2025), 28-31 July - we have sponsorship from HSF/CERN-SFT, IRIS-HEP and JuliaHub!

Registration and abstract submission are open. Abstract submission deadline is 31 March.

New papers:
- [Fast Jet Finding in Julia](https://arxiv.org/abs/2503.08146)
- [Julia in HEP](https://arxiv.org/abs/2503.08184)

Interst in discussing how to use the Julia package in the experiments - [`JetReconstruction.jl`](https://github.com/JuliaHEP/JetReconstruction.jl) developers are working on a statically compiled library with the `juliac` compiler. (FYI, license is MIT, in common with most of the Julia ecosystem.)

### GSoC program 2025


## AOB

### 2025 High Performance Software Foundation Conference 

Schedule <https://events.linuxfoundation.org/hpsf-conference/program/schedule/> is now live. 5-8 May in Boston.

Many topics of interest for software and computing!

### Next Meeting

Next meeting will be [27 March](https://indico.cern.ch/event/1477074/)

### Chair This Meeting 👇

Please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing a future coordination meeting. (There is even a [HOWTO guide](https://hepsoftwarefoundation.org/organization/running-meetings.html)).
