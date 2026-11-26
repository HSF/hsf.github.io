---
tags: HSF, Minutes
lang: en-gb
description: HSF Meeting Notes
---

# HSF Coordination Meeting #316, 19 November 2026

---

## Attending

Present/Contributing: Claire Antel, Eduardo Rodrigues, Ruslan Mashinistov, Andres Rios-Tascon, Philippe Gras, Saptaparna Battacharya, Stephen Mrenna, 

Apologies/Contributing: Alexander Moreno, Stefan Roiser

## News, general matters, announcements

### Steering Group & Advisory Group

* Next HSF Steering Group Meeting tomorrow.
* 2nd 2026 AG meeting took place in Bologna during the joint WLCG/HSF workshop.

Any actions or decisions will be reported back in due time.

#### WLCG/HSF workshop

- Was 2-6 November 2026 in Bologna, [Indico page](https://indico.cern.ch/e/wlcg-hsf-2026) - a great workshop overall!

Some points:
- Very positive response to <https://heptraining.cern.ch/> (not HSF initiated - but advertises HSF training & HSF seminars).
- It was raised several times that it would be useful to have a place where AGENTS.md and SKILLS.md (also sandbox environment setups?) could be shared in community.
    - Had previously considered just a HSF GitHub repo (of links to other GitHub repos?).
    - A suggestion at workshop was <https://heptraining.cern.ch/> : Would that work?
    - (discussion) from those involved in CLARIPHY: A platform exists for sharing of agent files - but currently access controlled. Are happy to collaborate!

### HSF Affiliated Projects and Software

Status at <https://hepsoftwarefoundation.org/projects/projects.html> -  6 projects affiliated, 1 in progress - Phoenix event display review completed, in circulation.

Other potential projects: we have a rather comprehensive list of projects interested or to be approached. The list has been sent to the Advisory Group to receive feedback from the Engaged Communities (experiments and other relevant collaborations/projects):
-ACTS - being followed up by Caterina
-Clad
-CVMFS
-DD4hep
-EvtGen
-FastJet
-Gaudi - being followed up
-Geant4
-HepData
-HepMC3
-HERWIG
-hls4ml - 2 reviewers, review starting
-Invenio
-LHCb Conditions DB - 2 reviewers
-LHAPDF
-Omnifold - being followed up by Sapta
-MCFM
-Millepede-II
-Needle - 1 reviewer, getting in touch with authors
-Phoenix - review reported, now in the 2-week circulation period for community feedback
-PODIO - being followed up by Michel V.
-Rivet - 2 reviewers, review ongoing
-Rucio - being followed up (exchange with authors)
-Sherpa
-XRootD
-WHIZARD

- Projects being approached - we need volunteers to contact them.
- Projects interested - we need volunteers to find reviewers and/or review them.

So kindly let the SG if you are willing to help ... and you may well receive an invitation email otherwise ... ;-)

Do not hesitate to discuss around you to identify relevant projects/libraries that could engage with the affiliation programme. AA conveners are in an excellent position to help us identify which projects to prioritise to join the affiliation programme.

### AI in contributions to HSF repositories

We now have a `CONTRIBUTING.md` and `pull-request-template.md` for hsf.github.io:
- https://github.com/HSF/hsf.github.io/blob/main/CONTRIBUTING.md
- https://github.com/HSF/hsf.github.io/blob/main/.github/pull_request_template.md

A couple of PRs have gone in, with new pull-request-template - no complaints. 

Is there anything else we want to do in this area? (e.g. apply to all HSF projects via .github?)
- No comments - can remove this item in future meetings.


#### Forum discussion: Towards common responsible AI-assisted coding guidelines 

Hosted an interactive guidelines review at WLCG/HSF joint workshop.
- Were able to form 3 groups of ~3-4 people (1 on zoom).
    - Session room was "buzzing" during interactive discussion.
- Valuable new perspectives on doc, such as:
    - More input on use and benefits of local hosting and RAG.
    - Suggestions on using LLMs to serve as teachers, as solution to supervision over-burden.
    -  To attribute _human_ contributions - not just AI contributions.

Next steps: To incorporate new feedback, make github draft page - with more detailed "how-tos" and links to further relevant material (e.g. security guidelines)
- Caterina working on it.

Do we host more forum discussions in future?
- No comments.
- For now, will not plan any more forum discussions.
- Probably will host related topics as HSF seminars.

### HSF Seminar Series and Compute Accelerator Forum

To plan Pythia + other Generators: Building sustainable software seminar.
- Event Generator AA is still keen.
- Possible dates are Dec or early next year - more likely early next year.
    - To follow up via email.

Thanks to the activity groups for coming to us with seminar ideas and speakers!
HSF seminar conveners are reachable at <mailto:hsf-seminar-conveners@googlegroups.com>. Please send your suggestions for next seminars.

## Activities Updates

### GSoC 2026

A presentation of this year's programme was given at the joint WLCG/HSF workshop in Bologna, providing also a historical perspective over the past 15 years - a great talk to check out!

### Software Training

- Past Events
    - [WLCG/HSF Workshop](https://indico.cern.ch/event/1655190/), 2-6 November - HSF Training parallel session on [Software Training in the AI-Assisted Coding Era](https://indico.cern.ch/event/1655190/timetable/#20261105.detailed).
        - Presentations by:
            - CMS, Belle II, CLARIPHY, LHCb, HSF, ATLAS, EIC
        - General comments:
            - Guidelines and best practices are still at an early stage of development
            - There are still many questions about how software training will evolve as the adoption of LLMs increases
            - AI presents opportunities to expand the reach of software training. For instance, LHCb is using AI to translate its training materials into chinese
            - Funding and responsibility for providing AI resources remain unresolved issues for many communities
            - Concerns about the use of LLMs, particularly regarding grid certificates and other credentials
            - HSF Training infrastructure: The structures already in place. What's missing is the AI-era content inside them
            - Opportunities for collaboration!

- Next Events
    - Next Hackathon - Training on Effective AI-Assisted Coding in HEP and NP
        -  December 7, after the Training Planning meeting. It will be announced this week
        -  Live notes: [HSF Hackathon - LLMs for HEP](https://docs.google.com/document/d/1iiOLJlN9eVGJwy1PN-ti3czcGcCSaOOGo8_3EPLKnAw/edit?usp=sharing)
    - We are already planning the next events for next year. If you have ideas and suggestions please let us know. Some ideas we have discussed so far:
        - Scikit-HEP
        - ROOT
        - Generative AI
        - Software Basics at Labs: BNL, Fermilab, CERN?

- Papers
    - Collection “[Software Training in High Energy Physics for the AI Era](https://www.frontiersin.org/research-topics/82889/software-training-in-high-energy-physics-for-the-ai-era)” - Frontiers in Big Data:
        - HSF/IRIS-HEP Training on Responsible Usage and Best Practices for AI-Assisted Coding - Summary submitted on Sept. 16 
        - ML Training - Based on the recent [Machine Learning Training](https://indico.cern.ch/event/1706524/)
        - Full manuscripts - Nov. 29
    - [Training on Data Analysis Reproducibility via Containerization with Apptainer](https://arxiv.org/pdf/2604.06244) - The Journal of Open Source Education - It was submitted ~7 months ago. We are considering submitting it to a different journal.

### Physics Generators

- Work with potential GSoC student (Deep Dhamanwala) ongoing. Large scale sample production was just completed. Hopefully, we can get something out by spring. 

### JuliaHEP

- JuliaHEP meeting on December 8 at 16:00 CERN time (it will be announced this week):
    - Geant4.jl - Pere Mato
    - Summary of the JuliaHEP Mini 2026 - Julia for Nuclear and Elementary Particle Physics: From Precision Science to High-Performance Tools - Uwe Hernandez Acosta
    - Gauge the interest for a JuliaHEP workshop in 2027

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

The next coordination meeting on the 3rd Dec 2026.

