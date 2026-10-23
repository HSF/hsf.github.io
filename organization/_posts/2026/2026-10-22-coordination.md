---
title: "HSF Coordination Meeting #315, 22 October 2026"
layout: plain_toc
---

## Attending

Present/Contributing: Johannes Elmsheuser, Claire Antel, Inês Ochoa, Michel Hernandez Villanueva, Liz Sexton-Kennedy, Dmitry Kalinkin, Menglin Xu

Apologies/Contributing: Alexander Moreno, Christian Wessel, Eduardo Rodrigues

## News, general matters, announcements

### Steering Group & Advisory Group

* Next HSF Steering Group Meeting: TBD
* Next AG meeting will take place in Bologna in Nov. during the joint WLCG/HSF workshop.

#### WLCG/HSF workshop

- 2-6 November 2026 in Bologna, [Indico page](https://indico.cern.ch/e/wlcg-hsf-2026).
- Agenda is final (organiser discussion on Monday Oct 19)
- As previously discussed: 2 parallel sessions now on the agenda on Thursday afternoon about (a) Coding Assistant and (b) AI (operations + coding assistants)
    - Suggestion to update the AI agenda content to make it more clear and advertise it better

### HSF Affiliated Projects and Software

- Beyond the mailing lists some discussions about "HSF review of nopayload DB Server and Client" [review document](https://docs.google.com/document/d/1FqryG-__qtGCQn3aItdtWdklOqHz80UpxjNRMPwNNc0/edit?tab=t.0)
    - There is a DB and client part of the software
    - The initial result of the review was a Tier1 rating by the reviewer
    - After the HSF feedback period the rating was changed to Tier2 and the maturity of the DB vs. client components was mentioned.
    - Suggestion points for improved future reviews (personal comments from Johannes):
        - Tiered rating system perceived as school marks
        - Ideally there are several reviewers
        - Transparency on who provided feedback when assessments/ratings were changed


Status at <https://hepsoftwarefoundation.org/projects/projects.html> -  6 projects affiliated, 1 being finalised, see above.

Other potential projects: we have a rather comprehensive list of projects interested or to be approached. The list has been sent to the Advisory Group to receive feedback from the Engaged Communities (experiments and other relevant collaborations/projects):

-ACTS - being followed up
-Clad
-CVMFS
-DD4hep
-FastJet
-Gaudi - being followed up
-Geant4
-HepData
-HepMC3
-Herwig
-hls4ml - 2 reviewers
-Invenio
-LHCb Conditions DB - 2 reviewers
-LHAPDF
-Omnifold - being followed up
-MCFM
-Phoenix - 1 reviewer - still searching for 2nd
-PODIO - being followed up
-Rivet - 2 reviewers, invitation sent out
-Rucio - being followed up
-Sherpa
-XRootD
-WHIZARD

- Projects being approached - we need volunteers to contact them.
- Projects interested - we need volunteers to find reviewers and/or review them.

So kindly let the SG if you are willing to help ... and you may well receive an invitation email otherwise ... ;-)

Do not hesitate to discuss around you to identify relevant projects/libraries that could engage with the affiliation programme. AA conveners are in an excellent position to help us identify which projects to prioritise to join the affiliation programme.

### AI in contributions to HSF repositories

#### "AI Statement" for contributors to HSF repo
*Feedback still welcome:* So far HSF repositories do not provide any statement on AI-powered/-helped contributions, and we are starting to get some. On occasions we can be flooded by not-to-useful contributions.
This year an "AI statement" is strongly suggested in GSoC proposals. We should do something similar.
There is an ongoing discussion at <https://github.com/HSF/hsf.github.io/issues/1919>.
Suggestion to update the [website how-to](https://hepsoftwarefoundation.org/howto-website.html) with a statement on AI and how we will be dealing with "spam".

We now have a `CONTRIBUTING.md` and `pull-request-template.md`:
- https://github.com/HSF/hsf.github.io/blob/main/CONTRIBUTING.md
- https://github.com/HSF/hsf.github.io/blob/main/.github/pull_request_template.md

Is there anything else we want to do in this area? (e.g. apply to all HSF projects via .github?)


#### Forum discussion: Towards common responsible AI-assisted coding guidelines 

- Another (last?) forum discussion held yesterday (21st Oct): https://indico.cern.ch/event/1739582/
    - MadGraph, Pythia and EpsilonEridani presented on how they're adapting to AI-assisted contributions to collaborative software.
        - A variety of perspectives and themes: From reflections on the role of maintainer in future (less rewarding), to forming AI policies to going full agentic.
    - Caterina presented first "loose guidelines" draft.
        - There was some discussion before the room kicked us all out, which unceremoniously ended the (already running overtime unfortunately) meeting.
        - We're hoping that people will contribute to the [live google doc](https://docs.google.com/document/d/1VvkB9siVFs5ozc7kkjULmhLB_k9xqW_5-mlCAXiTSsM/edit?tab=t.0#heading=h.na9ekmaze8ng), ahead of the WLCG/HSF workshop discussion session.
        - Still nailing down the main purpose these guidelines should serve (given the vastly different perspectives, changing landscape).

### HSF Seminar Series and Compute Accelerator Forum

Past HSF seminars:
- 14th Oct: HSF-IML joint seminar on "[WhAM: Whale Acoustic Model](https://arxiv.org/abs/2512.02206)" (part of [CETI project](https://www.projectceti.org/) that has the longterm goal of translating whale speech).
    -<https://indico.cern.ch/event/1730035/>
    - Around 30 participants on zoom + 10 people in the room (was hoping for more attendance).
    - Talk was great!
    - Some technical difficulties in setting up room (with speaker's laptop), not so great.
    - Did not manage to find recording button until later in talk. Speaker helpfully provided a YouTube link of a similar talk of theirs from April - added to agenda.

Planned HSF seminars:
- Future seminars ? Possibly talk from Pythia on project sustainability?
- No others planned.

Thanks to the activity groups for coming to us with seminar ideas and speakers!
HSF seminar conveners are reachable at <mailto:hsf-seminar-conveners@googlegroups.com>. Please send your suggestions for next seminars.


## Activities Updates

### GSoC 2026

A full report at the end of this year's programme will be given at the joint WLCG/HSF workshop in Bologna.

### Software Training

- Past Events
    - [15th HEP C++ Course and Hands-on Training - Advanced C++](https://indico.cern.ch/event/1689553/), 12-16 October.
        - Participants ?
        - Registration: 14 in person, 50 virtually

- Next Events
    - [WLCG/HSF Workshop](https://indico.cern.ch/event/1655190/), 2-6 November - HSF Training parallel session on Software Training in the AI-Assisted Coding Era. We are working on the agenda:
        - Confirmed (in person):
            - CMS, Belle II, EVERSE, HSF, ATLAS, EIC
        - Still TBC (virtually):
            - CLARIPHY, LHCb, ALICE
        - Agenda will be up by Friday   

- Papers
    - Collection “[Software Training in High Energy Physics for the AI Era](https://www.frontiersin.org/research-topics/82889/software-training-in-high-energy-physics-for-the-ai-era)” - Frontiers in Big Data:
        - HSF/IRIS-HEP Training on Responsible Usage and Best Practices for AI-Assisted Coding - Summary submitted on Sept. 16 
        - Full manuscript - Nov. 29
    - [Training on Data Analysis Reproducibility via Containerization with Apptainer](https://arxiv.org/pdf/2604.06244) - The Journal of Open Source Education - It was submitted ~7 months ago. We are considering submitting it to a different journal.


### JuliaHEP

JuliaHEP 2027 - New date and location to be announced in due time.


## AOB

#### HSF calendar

Do not hesitate to get in touch with the SG if you have/know of events useful to add to the HSF calendar.
The calendar is used by very many to check for available dates, constraints, and plan events. Thank you in advance.

### HSF Promotional Poster

Sapta has a poster to promote the HSF. There is one version [here](https://indico.cern.ch/event/1606598/), but please contact her for the latest version.
- (Claire) A slightly edited version based on Sapta's poster: <https://cernbox.cern.ch/s/cNRZgeuiTKB22Gd>

### Physical Constants / HEPdata Library

There is now an early "proof of concept" version: [hep-constants](https://github.com/HSF/hep-constants). Some generally positive feedback was received, but no further development yet.
We are looking for contributors.

### Next Meeting

The next coordination meeting on November 5 is cancelled due to the WLCG/HSF workshop during that week in Bologna.
The next coordination meeting will take place November 19.

### Chair This Meeting 👇

Please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing a future coordination meeting. (There is even a [HOWTO guide](https://hepsoftwarefoundation.org/organization/running-meetings.html)).
