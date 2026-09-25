---
title: "HSF Coordination Meeting #313, 24 September 2026"
layout: plain_toc
---


## Attending

Present/Contributing: Eduardo Rodrigues, Claire Antel, Ruslan Mashinistov, Juan Miguel Carceller, Michel Hernandez Villanueva, Richa Sharma, Nick Smith, Andres Rios-Tascon, Saptaparna Bhattacharya, Liz Sexton-Kennedy, Steve Mrenna

Apologies/Contributing: Alexander Moreno, Graeme A. Stewart

## News, general matters, announcements

### Steering Group & Advisory Group

#### WLCG/HSF workshop

- 2-6 November 2026 in Bologna, [Indico page](https://indico.cern.ch/e/wlcg-hsf-2026).
- Registration is still up, and abstraction submissions remain open. Do consider participating in this nice jount event!

### WLCG Management Board community software liaison

The HSF and Community Software report for the RRB covering the period 16 March – 14 September 2026, prepared by Stefan Roiser, has been submitted.

### HSF Affiliated Projects and Software

Status at <https://hepsoftwarefoundation.org/projects/projects.html> - unchanged, 6 projects affiliated.

Review of the NoPayloadDB Conditions Database is being finalised this week.

Other potential projects: we have a rather comprehensive list of projects interested, or to be approached, see previous minutes. The list has been sent to the Advisory Group to receive feedback from the Engaged Communities (experiments and other relevant collaborations/projects).
- Projects being approached - we need volunteers to contact them.
- Projects interested - we need volunteers to find reviewers and/or review them.

So kindly let the SG if you are willing to help ... and you may well receive an invitation email otherwise ;-) ...

Do not hesitate to discuss around you to identify relevant projects/libraries that could engage with the affiliation programme. AA conveners are in an excellent position to help us identify which projects to prioritise to join the affiliation programme.

### AI in contributions to HSF repositories

#### "AI Statement" for contributors to HSF repo
*Feedback still welcome:* So far HSF repositories do not provide any statement on AI-powered/-helped contributions, and we are starting to get some. On occasions we can be flooded by not-to-useful contributions.
This year an "AI statement" is strongly suggested in GSoC proposals. We should do something similar.
There is an ongoing discussion at <https://github.com/HSF/hsf.github.io/issues/1919>.
Suggestion to update the [website how-to](https://hepsoftwarefoundation.org/howto-website.html) with a statement on AI and how we will be dealing with "spam".

#### Regarding statement for **HSF hsf.github.io repo**, specifically - input from Claire:
- Did review of rejected PRs this year, and reasons why. See [comment on issue #1919](https://github.com/HSF/hsf.github.io/issues/1919#issuecomment-5140599786)
- Suggest would be helpful to start with a CONTRIBUTING.md file - created [new issue #1951](https://github.com/HSF/hsf.github.io/issues/1951).
- Relevant PRs now in the works - thanks to a proactive external contributor:
    - CONTRIBUTING.md file: <https://github.com/HSF/hsf.github.io/pull/1953>
    - PR template: <https://github.com/HSF/hsf.github.io/pull/1949>

#### Forum discussion: Towards common responsible AI-assisted coding guidelines 

Held "Responsible AI + training" forum discussion yesterday, Wed 23rd Sept:
<https://indico.cern.ch/event/1726818/>.

- First part was input from labs on providing access to AI-assisted coding tools for research. _Tried_ to be diverse: BNL (USA), IHEP (China), Euro-based (Nikhef, IFIC, RAL). Was interesting, and each presented a different aspect.
- ~70 attendees - dropped down to ~20-30 by the (late-ish) end of the day.

**"Guidelines docathon" follow-up:**

During last part of yesterday's forum discussion, Caterina introduced some ideas/discussion points on guidelines (intentions, format), to introduce the idea and hear community opinions.
- General good support.
- Advertised plan for "guidelines docathon" (should we change name?) to brainstorm further: Wed 30th Sept at 15h30, <https://indico.cern.ch/event/1733243/>

### HSF Seminar Series and Compute Accelerator Forum

Planned HSF seminars:
- [30th Sept](https://indico.cern.ch/event/1689368/): Seminar on "assessing sustainability of AI" by Sophia Wilson ([SAINTS Lab](https://saintslab.github.io/), University of Copenhagen).
- 14th Oct: HSF-IML joint seminar on "[WhAM: Whale Acoustic Model](https://arxiv.org/abs/2512.02206)" (part of [CETI project](https://www.projectceti.org/) that has the longterm goal of translating whale speech).
    - Will exceptionally start at 16h00.
    - Speaker will attend in person.

Thanks to the activity groups for coming to us with seminar ideas and speakers!
HSF seminar conveners are reachable at <mailto:hsf-seminar-conveners@googlegroups.com>. Please send your suggestions for next seminars.


## Activities Updates

### GSoC 2026

A full report at the end of this year's programme will be given at the joint WLCG/HSF workshop in Bologna.

### Software Training

- Past Events
    - [Responsible AI-assisted coding and common training aspects](https://indico.cern.ch/event/1726818/) - 23 September. Update on the survey on Training on Effective AI-Assisted Coding in HEP and NP.

- Next Events
    - [HSF/IRIS-HEP Training Hackathon: Training on Effective AI-Assisted Coding in HEP and NP](https://indico.cern.ch/event/1729528/) - Sept 28, 17:00 CERN time.
    - [HSF/IRIS-HEP Profiling in Python (Virtual)](https://indico.cern.ch/event/1723179/)  - Oct 7.
        - Registration is open
        - As of today, 43 participants registered
    - [15th HEP C++ Course and Hands-on Training - Advanced C++](https://indico.cern.ch/event/1689553/), 12-16 October. Registration is open
        - As of today:
            - In person: 10 participants registered
            - Virtually: 42 participants registered
    - [WLCG/HSF Workshop](https://indico.cern.ch/event/1655190/), 2-6 November - HSF Training parallel session on Software Training in the AI-Assisted Coding Era. We are working on the agenda. Alex will convene the session.

### Physics Generators

- [Sapta] Continuing work on negative weight mitigation with a potential GSoC student (project was not funded this year but we still wanted to get a paper out).

### PyHEP

- [PyHEP.dev 2026](https://indico.nikhef.nl/event/7873/) held this week (September 7-9) at Nikhef Amsterdam.
    - Excellent attendance around 30 people.
    - Lots of discussion and many PRs/Issues (>40) created following those - great.
    - Discussions on agentic AI for the first time (including MCP use).
    - Talks and Discussions on general HEP package updates, Workflow Management Systems, HEP Packaging, and Statistical Tools.
    - We had a industry talk from Ruben Arts (prefix.dev) about pixi: <https://indico.nikhef.nl/event/7873/contributions/31401/>.
    - We gave a seminar talk about our PyHEP work and activites at Nikhef in addition/parallel to the workshop.
    - You can find notes and links to issues & PRs here: <https://codimd.web.cern.ch/ttbNPMWETCq7VRnaaxUB8w?both>, concrete achievements / PRs for: 
        - integrating LLMs into existing libraries better.
        - ROOT RDataframe client for histogramming-as-a-service (histserv).
        - many updates to UHI (universal histogram interface) serialization.
        - integration of histserv into coffea framework (pepper).
        - more than 15(!) PRs to iminuit.
    - Very good individual feedback from participants: Nikhef is a great location for such a workshop with an amazing local organization team (strong recommendation!).

- PyHEP seminar talk about the JAX ecosystem by Johanna Haffner (<https://indico.cern.ch/event/1729324/>) last Monday.
    - Participation: ~10 in person + ~20 via Zoom.
    - Patrick Kidger joined for further discussions in person as well.

### JuliaHEP

- [JuliaHEP 2026](https://indico.cern.ch/event/1660753/) has been postponed until 2027.


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

The next coordination meeting will take place October 8th.

### Chair This Meeting 👇

Please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing a future coordination meeting. (There is even a [HOWTO guide](https://hepsoftwarefoundation.org/organization/running-meetings.html)).
