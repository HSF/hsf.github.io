---
title: "HSF Coordination Meeting #312, 10 September 2026"
layout: plain_toc
---

## Attending

Present/Contributing: Eduardo Rodrigues, Michel Hernandez Villanueva, Inês Ochoa, Alexander Heidelbach, Liz Sexton-Kennedy, Saptaparna Bhattacharya

Apologies/Contributing: Christian Wessel, Claire Antel, Alexander Moreno, Caterina Doglioni, Maarten van Veghel

## News, general matters, announcements

Welcome back! We hope you all had a relaxing Summer break!

### Steering Group & Advisory Group

Minutes of the last meeting on July 30th are available [here](https://hepsoftwarefoundation.org/organization/2026/07/30/steering.html) and as usual from the HSF homepage.

#### WLCG/HSF workshop

- 2-6 November 2026 in Bologna, [Indico page](https://indico.cern.ch/e/wlcg-hsf-2026).
- Registration is up, abstraction submission remains open. Do consider participating in this nice jount event!

### WLCG Management Board community software liaison

The HSF and Community Software report for the RRB covering the period 16 March – 14 September 2026 is being prepared by Stefan Roiser.

It is currently under review by the SG and AA conveners, and will be submitted shortly.

### HSF Affiliated Projects and Software

Status at <https://hepsoftwarefoundation.org/projects/projects.html> - unchanged, 6 projects affiliated.

Reviews in progress, finalised and in circulation for community approval:
- NoPayloadDB database and client Conditions Database

Other potential projects: we have a rather comprehensive list of projects interested or to be approached, see previous minutes.
- Projects to be approached - we need volunteers to contact them.
- Projects interested - we need volunteers to find reviewers and/or review them.

So kindly let the SG if you are willing to help ... and you may well receive an invitation email otherwise ... ;-)

Do not hesitate to discuss around you to identify relevant projects/libraries that could engage with the affiliation programme. AA conveners are in an excellent position to help us identify which projects to prioritise to join the affiliation programme.

### AI in contributions to HSF repositories

#### "AI Statement" for contributors to HSF repo

*Feedback still welcome:* So far HSF repositories do not provide any statement on AI-powered/-helped contributions, and we are starting to get some. On occasions we can be flooded by not-to-useful contributions.
This year an "AI statement" is strongly suggested in GSoC proposals. We should do something similar.
There is an ongoing discussion at <https://github.com/HSF/hsf.github.io/issues/1919>.
Suggestion to update the [website how-to](https://hepsoftwarefoundation.org/howto-website.html) with a statement on AI and how we will be dealing with "spam".

#### Regarding statement for **HSF hsf.github.io repo**, specifically - input from Claire:

- Did review of rejected PRs this year, and reasons why. See [comment on issue #1919](https://github.com/HSF/hsf.github.io/issues/1919#issuecomment-5140599786).
- Suggest would be helpful to start with a CONTRIBUTING.md file - created [new issue #1951](https://github.com/HSF/hsf.github.io/issues/1951).
- Relevant PRs now in the works - thanks to a proactive external contributor:
    - CONTRIBUTING.md file: <https://github.com/HSF/hsf.github.io/pull/1953>.
    - PR template: <https://github.com/HSF/hsf.github.io/pull/1949>.

#### Forum discussion: Towards common responsible AI-assisted coding guidelines 

Reminder: Kick-off meeting took place on Wed. July 29th with excellent attendance reaching about 200 participants: <https://indico.cern.ch/event/1705480/>.

Next forum discussion is planned for Wed. Sep. 23rd, 15h30-17h30 CEST:
<https://indico.cern.ch/event/1726818/>
- 1st half:
    - Recap of previous meeting.
    - Focus on inputs from labs/institutes other than CERN: Their strategy/plans around providing access to AI-assisted coding tools.
    - Confirmed labs/institutes: BNL, Nikhef, IHEP.
        - DESY contribution planned for Oct edition (discussed with other DESY folks in HSF).
    - Have also had discussion on inviting the French-based IN2P3 institute, given they're mandated to use Mistral AI. Would be an interesting contribution. However, not following up on a particular lead right now. Do we want to - or keep for October edition?
    - Plan to invite other labs/institutes to upload material in a shared folder if they want - with no guarantee we'll have time to discuss them.
- 2nd half:
    - Update from HSF training.
    - Advertise Actionable Items: Early draft of guidelines, creation of repos to collect templates - Dockerfiles, AGENT.md etc - WIP.

### HSF Seminar Series and Compute Accelerator Forum

Planned HSF seminars:
- [30th Sept](https://indico.cern.ch/event/1689368/): Seminar on "assessing sustainability of AI" by Sophia Wilson ([SAINTS Lab](https://saintslab.github.io/), University of Copenhagen).
- 14th Oct? HSF-IML joint seminar on "[WhAM: Whale Acoustic Model](https://arxiv.org/abs/2512.02206)" (part of [CETI project](https://www.projectceti.org/) that has the longterm goal of translating whale speech).
    - Really exciting direct application of transformer-type ML for Science.
    - Have found a young speaker, was hoping to have confirmed date with speaker by now...
    - Hoping to host speaker in person.
    - Also, hoping that there'll be so much interest in this seminar, CERN will consider an Academic Training Lecture series ;).

(Thanks to the activity groups for coming to us with seminar ideas and speakers!)
HSF seminar conveners are reachable at <mailto:hsf-seminar-conveners@googlegroups.com>.
Please send your suggestions for next seminars.

### Proposal to archive the HSF Gitter channels

Read below and shout quickly as otherwise agreement will be concluded!

> We have had the following Gitter channels for some time:

> HSF/PyHEP
HSF/PyHEP-histogramming
HSF/PyHEP-newcomers
HSF/PyHEP-fitting
HSF/ADL
HSF/mpl-hep

> But these channels have very largely been dormant for quite some time, and several of us feel that these aren't worth keeping anymore; better use the HSF Forum or some of the other lists we have.

> Hence the suggestion for each channel to rename the room (e.g. "Deprecated" or "Archived"), update the topic, remove it from the public directory, and leave it as an archive (it is not possible to delete, and probably not the best thing anyway).

## Activities Updates

### General Standing Reminders

### Software Training

- Past Events
    - [HSF/IRIS-HEP Machine Learning Training - Intermediate Level (Virtual)](https://indico.cern.ch/event/1706524/) - 3-4 August.
        - 171 participants registered (~50% experimentalists, ~50% theoreticians).
        - ~70 participants connected to each session on Monday and Tuesday.

- Next Events
    - HSF/IRIS-HEP Profiling in Python - Oct 7 (To be advertised).
    - [15th HEP C++ Course and Hands-on Training - Advanced C++](https://indico.cern.ch/event/1689553/), 12-16 October. Registration is open.
    - WLCG/HSF Workshop, 2-6 November - HSF Training parallel session. We are working on the agenda. Alex (TBC) will convene the session.

### PyHEP

- [PyHEP.dev 2026](https://indico.nikhef.nl/event/7873/) held this week (September 7-9) at Nikhef Amsterdam.
    - Excellent attendance around 30 people.
    - Lots of discussion and many PRs/Issues (>40) created following those - great.
    - Discussions on agentic AI for the first time (including MCP use).
    - Talks and discussions on general HEP package updates, workflow management systems, HEP packaging, and statistical tools.

### JuliaHEP

- [JuliaHEP 2026](https://indico.cern.ch/event/1660753/) will be held at MPI Munich, October 19-23. [Abstract submission](https://indico.cern.ch/event/1660753/abstracts/) and [registration](https://indico.cern.ch/event/1660753/registrations/126987/) are still open!
- JuliaCon 2026 - JuliaHEP Mini-Symposium - Julia for Nuclear and Elementary Particle Physics: From Precision Science to High-Performance Tools. It was scheduled for the Wednesday Morning (Aug 12).
    - [JuliaCon 2026 - Schedule](https://pretalx.com/juliacon-2026/schedule/) - Go to Wednesday, August 12.
        - 15-min talks: 4
        - 30-min talks: 2

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

The next coordination meeting will take place September 24th.

### Chair This Meeting 👇

Please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing a future coordination meeting. (There is even a [HOWTO guide](https://hepsoftwarefoundation.org/organization/running-meetings.html)).
