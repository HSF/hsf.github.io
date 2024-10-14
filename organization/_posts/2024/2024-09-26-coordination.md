---
title: "HSF Coordination Meeting #275, 26 September 2024"
layout: plain_toc
---

## Attending

Present/Contributing: Graeme Stewart, Claire Antel, Patrick Gartung, Eduardo Rodrigues, Stefan Roiser, Joseph Osborn, Nick Smith, Liz Sexton-Kennedy, Krzysztof Genser, Pere Mato, Jamie Gooding, Tamás Gál

Apologies/Contributing: Alexander Moreno

## News, general matters, announcements

### *Reminder* SPECTRUM/JENA Survey on Software, Computing, Training - deadline extended until September 30th.

> Dear Colleagues from Research / Infrastructures,
> 
> The SPECTRUM project [1] and the JENA Computing Initiative [2] are conducting a survey to gather insights on current best practice and expected future evolutions in the domain of large scale / data intensive scientific computing.
> 
> The survey is directed at researchers, managers of scientific initiatives and infrastructure managers, either on individual or institutional bases.
> 
> Our goal is to collect from the community insights on current best practice and expected future evolutions in the domain of large scale / data intensive scientific computing. This is important also for you, if you want to inform policy makers and funders about the needs from science and infrastructures and push in the direction of future interoperability.

[Full announcement](https://www.spectrumproject.eu/article/spectrumjena-survey-on-the-future-of-scientific-computing)

[Link to Survey](https://ec.europa.eu/eusurvey/runner/SPECTRUM-JENA_Survey1)

Please consider filling this in and also helping to disseminate it to your colleagues.

The survey is *differentiated* - filling in the Software and Training part (of most interest to the HSF) should only take 10-15 minutes.

### European Strategy Update

The [European Particle Physics Strategy Update](https://home.cern/news/news/knowledge-sharing/updating-european-strategy-particle-physics) will be next year:

- Inputs from the community by 31 March 2025
- Open Symposium 23-27 June 2025

We think it is a very good idea to have an input from the HSF on the software that we need for the future and how we achieve it. This would be a mini-update of the CWP from 2017.

We believe that input coordinated by our **activity areas** will be critical to doing this, especially from the critical areas of event generation, simulation, reconstruction and analysis; however, we should not at all forget the *people* dimension, so training and careers are vital to cover.

Feedback from working groups...

- Simulation have discussed their possible inputs - how to proceed with them now?
    - Possibly discuss week before CHEP
- Evaluation of new programming languages should be mentioned

Michel and Graeme agreed to help coordinating this work but other volunteers are most welcome (required!) to help.

- M&G to organise a dedicated discussion on this topic in October

### LHCC



### HSF Seminar Series

Seminar coordinators: Benedikt, Michel, Andrea

First HSF Seminar will be organised as part of JuliaHEP:

- Uwe Hernandez Acosta, *Julia in high-energy physics: a paradigm shift or just another tool?* 1 October at 16h30 CEST, <https://indico.cern.ch/event/1452314/>

We would like to organise further seminars on 

- 30 October
- 27 November
- 29 January
- 26 February (CERN local school holidays)

Current topic suggestions:

- Software Triggers & Reco proposed something around 4-D reconstruction
- Event generators on GPUs for the November seminar (after CHEP)

---

## Steering Group News

There was a Steering Group meeting on 23 September and the [minutes](https://hepsoftwarefoundation.org/organization/2024/09/23/steering.html) are available on the website.

- HSF Affiliated Projects proposal was circulated:
    - [document](https://docs.google.com/document/d/1Un1V21LdehQNwkNGeUZOl_GBQ8IdjUpDp5bi9g2YvLg/edit?usp=sharing)
    - [guidelines on best practices and badges](https://docs.google.com/document/d/1AiLcqyLA4c1y2Iq-YZyKP7DwN8m2AJb_J44cDuGGAXI/edit)
    - After feedback, put this onto the website and start to approach projects
- The HSF Advisory Group [document](https://docs.google.com/document/d/1L62pleuuME6K9WLl5T4KQaImPP_Qpc8HSym-XBNTKv8/edit?usp=sharing) is finalised
    - Will put this on the website and contact the experiments concerning constituting the AG

---

## Activity Updates

Our working groups and activities have been merged into a single "Activities" area on the website ([PR](https://github.com/HSF/hsf.github.io/pull/1582)).

"Reviews" sits a bit awkwardly here (and it's not even complete) so needs a revamp.

Areas which were actually not active at all were moved to a [*archived* area](https://hepsoftwarefoundation.org/what_are_activities.html#archive) (Analysis Facilities Forum, Conditions Databases, Differentiable Computing, Frameworks, Visualisation).

### Data Analysis

- Next meeting on Oct 28: https://indico.cern.ch/event/1461088/, focused on Scipp (https://scipp.github.io/) and ragged data. Room also booked at CERN, email to DAWG sent yesterday (feel free to advertise to interested communities!).


### Software Training

#### Next Events

- [HSF Training Pre-CHEP Workshop](https://indico.cern.ch/event/1410343/) - October 19-20. 
    - We will have talks from HSF-India, LHCb, EVERSE, ATLAS, ErUM-Data-Hub, LPC HATS, CoDaS-HEP, and ICFA. 
    - We will have two dedicated working sessions!
    - 45 registrations (before registration closed) 
- The [HSF/IRIS-HEP Software Basics Training](https://indico.cern.ch/event/1451866/) (7-8 Oct) and the [HSF/IRIS-HEP Python for Analysis Training](https://indico.cern.ch/event/1451868/) (15 Oct) will be postponed due to a low number of registrations.


#### C++ Course and Hands-on Training

- [11th HEP C++ Course and Hands-on Training, Advanced C++](https://indico.cern.ch/event/1430163/) 30 September - 4 October (Mo, We, Fr). 
    
### Software Tools and Packaging

- Nothing to report. Will have a chat with SG soon. Work on stacks has advanced and we should try to understand where things are.

### Detector Simulation

- Geant4 collaboration meeting upcoming.


### Reconstruction and Software Trigger

Follow ups on HSF seminar proposals:
- Potential speakers for 4-D tracking not available this year: Proposed Jan/Feb next year.
- The [SMARTHEP Edge ML school](https://indico.cern.ch/event/1405026/timetable/?view=standard) had a variety of interesting topics (heterogeneous compute clusters, real-time earth monitoring satellites, real-time grav wave processing, ultralow power AI processors): Can ask organisers for recommendations and invite speakers for an HSF seminar?
    - Recordings from school will not be made public.
- (I think organisers have already been in contact with CAF about rehosting one of the speakers)


### PyHEP

#### PyHEP.dev 2024
The workshop report is under final scrutiny and will be published to the ArXiv at the end of this week.


### Physics Generators



### JuliaHEP

- [JuliaHEP 2024 Workshop](https://indico.cern.ch/event/1410341/) - Sept. 30 - Oct. 4.
    - It's next week!
    - 155 registrations
        - 84 online
        - 71 in-person (with 50 at the tutorial/hackathon)
    - We have two key Julia developers coming
        - Jeff Bezanson, Julia compiler developer
        - Tim Besard, GPU expert in Julia
    - Jeff will give an extra talk on Thursday at 14h, in 222/R-001 (Filtration Plant) - will be broadcast
- [9 Oct](https://indico.cern.ch/event/1329694/), RISC-V variable precision acceleration(https://indico.cern.ch/e/juliahep2024) last week.


### Next Meeting

Next meeting will be [10 October](https://indico.cern.ch/event/1355758/).
* The 24 October meeting will be cancelled as this is the week of CHEP.

Reminder: please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing this or one of the future coordination meetings - we need volunteers from now until the end of the year!
