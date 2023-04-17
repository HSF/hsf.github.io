---
title: "HSF Coordination Meeting #248, 13 April 2023"
layout: plain_toc
---

## Attending

Present/Contributing: Graeme Stewart, Giulia Casarosa, Phil Ilten, Liz Sexton-Kennedy, Claire Antel, Torre Wenaus, Pere Mato, Valentin Volkl, Efe Yazgan, Kyle Knoepfel, Nick Smith, Kilian Lieret, Ale Di Girolamo, Alex Held, Juraj Smiesko, Nick Styles, Wouter Deconinck, Zach Marshall

Apologies/Contributing: Krzysztof Genser, Eduardo Rodrigues, Bendikt Hegner, Caterina Doglioni

## News, general matters, announcements

### LHC Experiment Feedback

We got some LHC experiment feedback - see [presentation](https://indico.cern.ch/event/1251043/) from the last Architects Forum, slide 13:

> - A useful list of activities foreseen to be discussed during in 2023
>   - No committed effort to the various activities (by construction!)
> - Nice to have events to spread new and technical insights (Computer Accelerator Forum, Frameworks WG, SW Tools and Packaging WG)
>   - Perhaps to be held more regularly?
> - HSF: Foundation or useful Forum?
>   - E.g. it gathers together people from various communities to share ideas and discuss possible synergies, for example in the areas of trainings (e.g. C++).

- Nick Styles: HSF is useful, but ATLAS concerns that WG interests not well aligned with experiments
  - Valid concern, though HSF is wider than LHC experiments (feedback on important topics **always** welcomed)
- Pere Mato: feedback was via SFT and we wanted to know if the SFT effort that goes to the HSF is thought to be well used
- Nick Styles - is the HSF really a foundation? No assignable resources and activities are best-effort
  - True that we had more foundation-like ideas in the early days (modeled on the Apache Software Foundation)
  - While effort is 'best-effort', people contribute to HSF to enhance things they would be hoping to do anyway
    - So little risk that activites go away
    - Albeit that there is limited capacity to ask the HSF for things
  - At the moment not really keen to change the name, even if 'forum' is more what we do
    - We have an identity well established
    - We don't want to preclude different feature activities
    - We should explain better what we do (see website revamp ideas below)

### Pre-CHEP Workshop

This is pretty much all ready to go now. See [indico](https://indico.cern.ch/e/wlcg-hsf23) for final agenda. The Zoom link will be created soon, should be ok for presentations, but still it's YMMV for dicussions.

We plan to circulate the AFF report and a list of topical questions in advance to that we know what we are trying to achieve.

### Google Summer of Code, 2023

- Preparing proposal evaluation overview
- 66 proposals for ~39 projects received, for ranking by April 27

### Google Season of Docs, 2023

- CVMFS proposal submitted, but it was not accepted by Google (and no feedback given)

## Working Group Updates

### General

The PR for the planning summary of 2023 is here: <https://github.com/HSF/hsf.github.io/pull/1410>.

Please comment on the PR to add clarifications or additional information. (Thanks to those who already did - also PRs fine.)

A lot of the WGs have had slow starts this year (see also LHC comments above), so it becomes a bit urgent to plan pre-summer activities, so that people know we are still alive.

### Software Training

- Hackathon next week, Monday April 17, 16h-18h, [indico] (todos following last analysis preservation workshop, taking inventory of ML material)
- Possibly two students with ~1 month FTE to work on pytest module to be integrated with analysis preservation workshop and brushing up the [REANA training][reana-training] (still looking for mentor with more REANA experience)
- Lively discussion regarding the format of our training:
  - The Carpentries are switching to a new framework ["Workbench"][workbench] with a new static page generator built in R. This would require some porting effort without clear benefits to us. Example in new format: [shell-novice]
  - At the same time, [Jupyterbook][] is a static page rendering with much more familiar technologies (for a HEP person) and has been used for training in our and the RSE field.

[indico]: https://indico.cern.ch/event/1276398
[workbench]: https://carpentries.github.io/sandpaper-docs/
[shell-novice]: https://fishtree-attempt.github.io/shell-novice/
[reana-training]: https://github.com/hsf-training/hsf-training-reana-webpage/
[Jupyterbook]: https://jupyterbook.org/

Just to note - Peter Elmer gave a very nice talk yesterday on workforce development at a [US HEP planning (P5) meeting](https://indico.bnl.gov/event/18372/timetable/?view=standard) at BNL (with the HSF figuring prominently in his talk of course)

#### C++ Course and Hands-on Training

C++ course in the UK:

- Dates: August 28-September 1st, lunchtime to lunchtime
- Costs: TBC (would have been 500 GBP with accommodation, lunch and breakfast + 1 social dinner but see below)
  - Swift-HEP <https://swift.hep.ac.uk> can cover some scholarships
- Structure
  - 3 days of lectures + 2 days of hands-on / team work (will coordinate with training team)
  - seminar by the Software Sustainability Institute <https://www.software.ac.uk>
- Teachers/demonstrators:
  - Day 1, Day 2: Sebastian Ponce
  - Day 3: Caterina Doglioni (or other volunteers welcome!)
  - Looking for demonstrators (some available locally)
    - Swift-HEP has some budget to cover costs
- Logistics:
  - since the Monday is a holiday we can't have lodging at the university
  - hotel rooms will be pre-booked
  - Next steps: finishing up and sending around "interest" questionnaire via indico

### Detector Simulation

- A talk on Geant4 physics models and event generators tentatively scheduled for June 5th: <https://indico.cern.ch/event/1276128/>

### Reconstruction and Software Trigger

#### Kick-off meeting scheduled for 26/04/2023 @ 2pm CEST

- Created indico agenda: <https://indico.cern.ch/event/1273894/>
  - Introduction of the WG
  - Discussion on SW reco & trigger between different experiments (slides)
    - will present slides with some aspects in common/different among "our" experiments (accelerator/beams, trigger, reconstruction)
  - Plans and topics for 2023, Google doc to collect ideas [here](https://docs.google.com/document/d/1v03aQRlKfTxcXTYb6Stf_cpqklt7e-FznmIUEw5Ec9o/edit?usp=sharing), reduced our proposal to 3 topics:
    - Sustainability in SW development for HEP
    - Lessons learned from recent trigger upgrades and new data-taking campaigns
    - Biased triggering & missed physics 
- Planning to circulate email in the following days - share with HSF coord for x-check beforehand?
- Weekly meet-ups until kick-off meeting.

### PyHEP

- Organisation of PyHEP.dev 2023 in-person workshop progressing well.
  - Set of participants essentially finalised.
  - Now focusing on the preparation of the agenda with short kick-off presentations in the mornings.
  - Grant proposal submitted to the PSF.

### Event Generators

- Tuning tutorial - started contacting potential contributors and trying to fix the date(s).
- Graeme: Updates from Swift-HEP project would be well worth presenting (see Christian Gutschow's [talk](https://indico.cern.ch/event/1215829/contributions/5306554/attachments/2621168/4531821/cg_swiftHepUpdateMar2023.pdf))

## Other Interest and Activity Areas

### Compute Accelerator Forum

Next meeting is 26 April, <https://indico.cern.ch/event/1264290/>:

- CADNA, tool for studying numerical precision (Fabienne Jézéquel, Sorbonne)
- The case for AI-augmented facilities (Michael Bussmann, HZDR)

---

## AOB

### Website

Benedikt started an [issue in GitHub](https://github.com/HSF/hsf.github.io/issues/1411) to gather ideas about reorganising and revamping the website to better reflect our areas of actual activity.

### Next Meeting

The next meeting will be on [27 April](https://indico.cern.ch/event/1225014/).

Please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing this or one of the future coordination meetings.
