---
title: "HSF Coordination Meeting #258, 12 October 2023"
layout: plain_toc
---

Present/Contributing: Graeme Stewart, Benedikt Hegner, Patrick Gartung, Liz Sexton Kennedy, Nick Smith, Efe Yazgan, Claire Antel, Pere Mato, Krzysztof Genser, Tamas Gal, Alexander Held

Apologies/Contributing: Eduardo Rodrigues (and others still at PyHEP), Nicole Skidmore (added to notes already about paper)

## Working Group Updates

### Conveners for 2024

We need to start the process to decide on conveners for the working groups for 2024

Proposed timeline:-

- Now, ask WG conveners their plans for next year and if they plan to stay on
- 31 October, know which slots will open for the different WGs
- 1 November, broadcast openings to HSF channels, projects and experiments, asking for nominations by 20 November
- HSF Search Team (last year was Michel, Liz, Graeme and Benedikt) discuss candidates, check balance across WGs and experiments, then invite people to take on the role, hopefully concluding by the end of the year
  - N.B. Any of the HSF Coordinators can serve on the search team! We do encourage this very much as the current people have served for quiet a long time.

Alex - do we have an engagement issue? We should do more reaching out to *help people engage* and to get more HSF input / update presentations; at least we would like that new collaboration members are told about the HSF. Ensure that this goes beyond the LHC experiments to Belle II, DUNE, FAIR, etc.

### Data Analysis

- Training paper on arxiv <https://arxiv.org/abs/2310.07342>
- For publishing "Frontiers in Physics editors are aware of our intentions, so we should be able to progress with that soon."
  - We hope this process will start in earnest soon, now that the CHEP proceedings are submitted - Graeme and Liz are editors for the special edition and will help track things
- Recent LHCb FunTuple publication <https://arxiv.org/abs/2310.02433> as possible target for dedicated discussion
- Discussing possible dates for dedicated meeting for HS3: important to get the right people from CMS & LHCb (plus beyond, flavour physics, etc.?) involved in the discussion, so timing is important

### Software Training

Python courses are running as part of the [Software Basics](https://indico.cern.ch/event/1316853/), which should run this November.

#### C++ Course and Hands-on Training

[Advanced C++ course](https://indico.cern.ch/event/1266628/) runs next week, at CERN and remote lectures (still some slots available).

### Software Tools and Packaging

Want to have Adam Stewart, Spack developer, come to CERN.

Graeme and Marco reported on the use of / plans for Spack across some significant sub-section of the NHEP community and experiments. We reported in last week's [Architects Forum](https://indico.cern.ch/event/1251048/) meeting.

Main points:

- Real strengths in Spack for deploying production software stacks; large community of contributors to 1000s of package recipes
- Some features need improvements: relocation, binary caches
- Principle lack seems to be poor support for developer story - e.g., for reconstruction developer in an experiment software stack
  - It may well be best to just keep Spack out of this area as it lacks sufficient granularity to understand the internals of experiment software
  - The current experiments have working examples of how to do this

Discussion:

- Patrick/Liz: SpackDev (from Fermilab), is not working so well at the moment
- EP-DT provide DAQ software with Spack (for, e.g., Faser) - we were not aware of this
- Do Belle II use Spack in production? Was SCONS in the past, but there were efforts to migrate, we are not sure where this got to

### Detector Simulation

- Geant4 Collaboration Meeting took place at the end of September (25-29)
- Still hoping to have a session on external (not Geant4) physics model developments and on a couple of other topics; No specific dates yet.
- Geant4 will review GPU related R&D in December (13,14)

### Reconstruction and Software Trigger

- Invite to LHCb potential speakers on topic related to efficient computing

### PyHEP

- [PyHEP2023](https://indico.cern.ch/e/PyHEP2023) is still ongoing! Full event report later.

### Physics Generators

Not yet progress on the topics we would like to cover, viz.,

- shared elements between MCEGs or
- forum or even collaborative projects between experiments on tuning.

### JuliaHEP

- [JuliaHEP workshop](https://indico.cern.ch/e/juliahep2023)
  - 126 registrations (~20 local participation).
  - Agenda has just been finalised and is now published on [Indico](https://indico.cern.ch/event/1292759/timetable).

## Other Interest and Activity Areas

### Compute Accelerator Forum

- Yesterday had a [meeting](https://indico.cern.ch/event/1264301/) on the D language: *Why D? An opinionated talk on why you should pick D for your next project* from Atila Neves (video uploaded)
- 8 November meeting will be a presentation on [HEPiX benchmarking](https://indico.cern.ch/event/1264302/)

---

## AOB

### Website

There is an [issue in GitHub](https://github.com/HSF/hsf.github.io/issues/1411) to gather ideas about reorganising and revamping the website to better reflect our areas of actual activity.

*We aim to try and have a new website ready for next year.*

### Community Calendar

As the autumn is now firmly entrenched, we should make sure the calendar is up to date with events for next year.

- [ ] ALICE
- [x] ATLAS
- [ ] CMS
- [ ] LHCb
- [ ] EIC
- [ ] Belle II
- [ ] DUNE
- [x] Conferences (ACAT and CHEP - others?)
- [x] LHCC Weeks

And anything else relevant for the software and computing communities in NHEP?

Please take your favourite experiment and add the dates!

### Next Meeting

The next meeting will be on [26 October](https://indico.cern.ch/event/1225027/).

Reminder: please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing this or one of the future coordination meetings - we need volunteers from now until the end of the year!
