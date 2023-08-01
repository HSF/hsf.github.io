---
title: "HSF Coordination Meeting #254, 20 July 2023"
layout: plain_toc
---

## Attending

Present/Contributing: Graeme Stewart, Benedikt Hegner, Caterina Doglioni, Nicole Skidmore, Patrick Gartung, Torre Wenaus, Liz Sexton-Kennedy, Tamas Gal, Nick Smith, Eduardo Rodrigues, Claire Antel, Samuel Skipsey, Wouter Deconinck, Krzysztof Genser, John Chapman, Sudhir Malik, Daniel Elvira

Apologies/Contributing: Stefan Roiser, Efe Yazgan

## News, general matters, announcements

### Google Summer of Code, 2023

- Mid-term evaluations starting, going well so far in terms of responses (only two reminders needed).
 
- Representative for the mentors summit on behalf of the HSF organizers was decided, and it will be Valentin Volkl. 

- The time and date for the summary session where students present their project will have to be decided after the summer break, we will have it before most students end their project. 
 
### LHCC

#### Software Liaisons

WLCG has decided to change the setup for its software liaisons, who will now be *WLCG Software Representatives*. Some of the most central projects are largely driven through EP-SFT at CERN (ROOT, Geant4, CVMFS) and so the natural representaive there is the chair of the *Architects' Forum* group in SFT, *ex officio* (currently Predrag Buncic).

There are many other important common software projects (e.g., generators, native Python ecosystem) that should also have a voice and representation and so the Management Board will consider nominations for a second software representative with good links to those projects. The HSF can propose a name for this role - *volunteers would be excellent*. This should be by 15 August(?) - Graeme will follow-up with Simone. *It would be strongly favoured to have a non-CERN person take this second position.*

Practically, Liz moves to CMS Offline Computing Coordinator role for the September LHCC and Predrag will join as Architect Forum Chair then. For the second representative, Graeme will stay on until a new person is appointed, so will also cover the September LHCC.

#### September LHCC

Liz and Graeme are discussing with training colleagues to find a presenter for the discussion on training (to take place in the normal 20’ software slot).

### EVERSE

The EU has funded the EVERSE project, ~8M€ over 3 years. 

"The EVERSE project aims to create a framework for research software and code excellence, collaboratively designed and championed by the research communities across five EOSC Science Clusters and national Research Software Expertise Centres, in pursuit of building a European network of Research Software Quality and setting the foundations of a future Virtual Institute for Research Software Excellence."

Strong HSF involvement, with Graeme, Caterina and Stefan all taking part.

N.B. The [5 science clusters](https://science-clusters.eu) are ESCAPE (NHEP, astronomy and astroparticle), ENVRI (envronmental science), Life Science RI, PANOSC (photon and neutron), SSHOC (social science).

Project will cover code quality for application code and for workflow and distributed computing software. Other communities also using a mixture of Python ("user facing") and C++ ("performance") (with interest in Julia?).

## Working Group Updates

### Data Analysis

- [Training and Onboarding initiatives in High Energy Physics experiments](https://www.overleaf.com/5191486352xprmvcmppckg) paper in first circulation  until 7th August
- [Monday's training meeting](https://indico.cern.ch/event/1303066/) will have a slot to discuss the paper outcomes and direction
- Early discussion on hosting [HS3](https://github.com/hep-statistics-serialization-standard/hep-statistics-serialization-standard) (HEP Statistics Serialization Standard) development, though LPCC may be a better home. Perhaps both?
    - How much would the LPCC do in practice? Needs 2-3 people to push this through, so if these people are in HSF maybe that is the better home.
    - Important to consider players beyond the LHC, e.g. Belle II and BES III.
    - There was some belief in CMS that LPCC might be able to draw in more effort, but it's not completely if that's true.
    - For now, focus on hosting _discussion_. How the project evolves can be discussed later perhaps
    - Those belonging to an experiment in the coordination group can help by sending names of members of the statistics committees (after the summer break). 
        


### Software Training

- [HSF/IRIS-HEP Python for Analysis Training (Virtual)](https://indico.cern.ch/event/1300865/) on Wednesday July 12
    - Well attended: ~65 participants, fairly constant over the day
    - Successfully used GitHub Codespaces to avoid variety of platforms (feedback welcome)
- [HSF/IRIS-HEP/Carpentries Software Basics Training (Virtual)](https://indico.cern.ch/event/1295954/) on Thursday-Friday July 13-14
    - Reasonable attendance: ~35 down to ~15 over the two days
    - Successfully used new Carpentries materials:
        - New training format based on R-markdown
        - New Python basics training based on [Gapminder](https://gapminder.org) dataset
- Next up and under development: MCEG training [outline](https://hsf-training.github.io/hsf-training-generators-webpage/) (basic concepts, MadGraph, Pythia8); next software basics in September/October

#### C++ Course and Hands-on Training

- [Training in Manchester](https://indico.cern.ch/event/1266661/) is finalised, registration is open
    - More online registrants than in-person --> consider a hybrid course for hands-on as well? It's historically been difficult to engage remotely if course was hybrid. 
    - Idea for the upcoming course: pair up learners to do some common tasks and bounce tasks off each other.
- [Advanced C++ course](https://indico.cern.ch/event/1266628/) at CERN will run in October
    
### Software Tools and Packaging

- Presentation "Spack in Key4hep" by Juan Miguel Carceller at July 11 meeting. Discussions after presentation were lively. 

### Detector Simulation

- Planning to have a session on "Geant4 cut/process/threshold tuning" tentatively on September 11th or 18th.

### Reconstruction and Software Trigger

- Planning talk on "zero waste computing" in Sept (date to be confirmed)
- Following up with possible talk on timing in tracking in Belle II in October (coincides with Connecting the Dots)

### PyHEP

- PyHEP.dev 2023 developers (in-person) workshop starting next Monday!
    - See <https://indico.cern.ch/e/PyHEP2023.dev>
- PyHEP 2023 users (online) workshop (Oct. 9-12) got announced about a week ago.
    - Registration and abstract submission open!
    - See <https://indico.cern.ch/e/PyHEP2023>

### Frameworks

- Will organize a presentation in September about HPX experience in ATLAS.

## Other Interest and Activity Areas

### JuliaHEP

- Nothing to report for the time being.

- If there is any interest from the community in studying energy consumption of Julia (looks really promising from initial studies, see [link to A. Gupta's University of Manchester final internship talk](https://indico.cern.ch/event/1307021/contributions/5497627/attachments/2692888/4673320/Week%206%20-%20Final%20Presentation.pdf)), get in touch with Caterina and Graeme for code and instructions. 

### Compute Accelerator Forum

- Meeting last week on ALICE's new O2 Facility, well attended and useful discussions. Unfortunately, it wasn't recorded!

- Next meeting will be 13 September with a presentation on [RISC-V architecture](https://indico.cern.ch/event/1264300/).

### Software and Computing Roundtable

- Reboot ongoing, restarting in the Fall. Want to re-discuss HSF input.

---

## AOB

### Website

Benedikt started an [issue in GitHub](https://github.com/HSF/hsf.github.io/issues/1411) to gather ideas about reorganising and revamping the website to better reflect our areas of actual activity.

### Next Meeting

We now take our summer break, with the next meeting scheduled for [August 31st](https://indico.cern.ch/event/1225023/).

Reminder: please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing this or one of the future coordination meetings.
