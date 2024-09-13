---
title: "HSF Coordination Meeting #274, 12 September 2024"
layout: plain_toc
---

## Attending

Present/Contributing: Eduardo Rodrigues, Patrick Gartung, Tommaso Lari, Pere Mato, Stefan Roiser, Anushka Saxena, Claire Antel, Michel Jouvin, Joe Osborn, Jim Pivarski, Saptaparna Bhattacharya, Alexander Moreno, Liz Sexton-Kennedy, Stephen Mrenna

Apologies/Contributing: Torre Wenaus, Graeme Stewart, Alexander Held

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

### Next HSF/WLCG Workshop

The next WLCG/HSF meeting will be hosted by IJCLab in Orsay next May 5-9 (thank you Michel!).

We will need people for the organising team - please say if you are interested.

Topics of mutual interest with WLCG are favoured, but there will also be HSF dedicated sessions.

### European Strategy Update

The [European Particle Physics Strategy Update](https://home.cern/news/news/knowledge-sharing/updating-european-strategy-particle-physics) will be next year:

- Inputs from the community by 31 March 2025
- Open Symposium 23-27 June 2025

We think it is a very good idea to have an input from the HSF on the software that we need for the future and how we achieve it. This would be a mini-update of the CWP from 2017.

We believe that input coordinated by our **activity areas** will be critical to doing this, especially from the critical areas of event generation, simulation, reconstruction and analysis; however, we should not at all forget the *people* dimension, so training and careers are vital to cover.

Michel and Graeme agreed to help coordinating this work but other volunteers are most welcome (required!) to help.

### LHCC

Eduardo circulated the link to the LHCC presentation via the [Architects' Forum meeting](https://indico.cern.ch/event/1354965/).
The [slides](https://docs.google.com/presentation/d/1361TObGpuKHpOLXwaubsBNdJBYPG5aV_32eYblKjpvI/edit?usp=sharing) were presented on Sep. 10th. They were very well received.

Very positive feedback received from the LHCC about the clarifications of the respective roles/responsibilities of the HSF and CERN SFT and the coordination/collaboration between them.

### HSF Seminar Series

First HSF Seminar will be organised as part of JuliaHEP:

- Uwe Hernandez Acosta, *Julia in high-energy physics: a paradigm shift or just another tool?* 1 October at 16h30 CEST, <https://indico.cern.ch/event/1452314/>

We would like to organise further seminars on

- 30 October
- 27 November

The regular slot should be the last Wedenesday of each month, at 16h30 CEST.

Steering Group members who offered to coordinate the organisation: Benedikt, Michel, Andrea.

Suggestions for topics are really needed!

- Software Triggers & Reco proposed something around 4-D reconstruction
- Event generators on GPUs for the November seminar (after CHEP)
---

## Steering Group News

There was a Steering Group meeting on 9 September and the [minutes](https://hepsoftwarefoundation.org/organization/2024/09/09/steering.html) are available on the website.

- HSF Affiliated Projects proposal has now been circulated:
    - [document](https://docs.google.com/document/d/1Un1V21LdehQNwkNGeUZOl_GBQ8IdjUpDp5bi9g2YvLg/edit?usp=sharing)
    - [guidelines on best practices and badges](https://docs.google.com/document/d/1AiLcqyLA4c1y2Iq-YZyKP7DwN8m2AJb_J44cDuGGAXI/edit)
    - Early adopters interest from software projects very welcome!
- The HSF Advisory Group [document](https://docs.google.com/document/d/1L62pleuuME6K9WLl5T4KQaImPP_Qpc8HSym-XBNTKv8/edit?usp=sharing) is finalised
    - Will now discuss with the experiments constituting the AG

---

## Activity Updates

Our working groups and activities have been merged into a single "Activities" area on the website ([PR](https://github.com/HSF/hsf.github.io/pull/1582)).

"Reviews" sits a bit awkwardly here (and it's not even complete) so needs a revamp.

Areas which were actually not active at all were moved to a [*archived* area](https://hepsoftwarefoundation.org/what_are_activities.html#archive) (Analysis Facilities Forum, Conditions Databases, Differentiable Computing, Frameworks, Visualisation).

### Data Analysis

Currently in the process of scheduling a talk on [Scipp](https://scipp.github.io/), likely in Oct. or early Nov.

### Software Training

#### Last Events

- HSF Training Hackathon: [Introduction to Databases for HEP](https://hsf-training.github.io/hsf-training-databases-basics/) - Sep. 9. This was the third session for new training material on Databases.

#### Next Events

- [HSF/IRIS-HEP Software Basics Training](https://indico.cern.ch/event/1451866/) - October 7-8. We will cover the fundamentals of Unix (shell and bash), Git and Github, and Python. Registration is now open! We need Instructors!
- [HSF/IRIS-HEP Python for Analysis Training](https://indico.cern.ch/event/1451868/) - October 15. We will cover the fundamentals of ROOT and Scikit-HEP. Registration is now open! We need Instructors!
- [HSF Training Pre-CHEP Workshop](https://indico.cern.ch/event/1410343/) - October 19-20. We are still working on the agenda. We will have talks from HSF-India, LHCb, EVERSE, DUNE, ErUM-Data-Hub. Registration is still open.

#### C++ Course and Hands-on Training

- [11th HEP C++ Course and Hands-on Training, Advanced C++](https://indico.cern.ch/event/1430163/) 30 September - 4 October (Mo, We, Fr), registration open now.

### Software Tools and Packaging

### Detector Simulation

We briefly discussed on Monday 9th the contribution to the European Strategy. The White Paper (https://arxiv.org/pdf/1712.06982) and the HSF software tools document for the HL-LHC LHCC review (https://zenodo.org/records/4009114) both include a 6-page section on simulation, emphasizing the importance of simulation for HEP and describing the direction of R&D effort to improve the accuracy and computing efficiency of simulation. There is also a simulation document submitted for Snowmass (https://arxiv.org/pdf/2203.07614) which is relevant. We propose to prepare something along similar lines in terms of scope and length. Details still needs to be worked out.

### Reconstruction and Software Trigger
Have gotten in touch with 2 speakers for an HSF Seminar on 4D track reco.

### PyHEP

#### PyHEP.dev 2024

[PyHEP.dev](https://indico.cern.ch/e/PyHEP2024.dev) took place in Aachen, 26 Aug - 30 Aug.
A workshop report is being prepared, to be published on the ArXiv. It's truly a community-driven document, as nearly all participants contributed to the paper.

### Physics Generators

- Event generators on GPUs for the November seminar (after CHEP)?
    - We could either organize one seminar or organize a one day workshop? or two half days?
    - Invite speakers from the Madgraph4GPU group, CMS implementation of Madgraph4GPU and updates from the Sherpa and/or PEPPER team as well as the PYTHIA team?
- What was the outcome of the LHCC kickoff meeting on the cross experiment forum on event generators?
    - Initial pre-kickoff meeting held on 8 Aug with representatives from the LHC experiments and several generator packages.
    - Round table by the participants stating the needs for future developments.
    - A public kickoff meeting (3-4 hours) date will be announced.

### JuliaHEP

- [JuliaHEP 2024 Workshop](https://indico.cern.ch/event/1410341/) - Sept. 30 - Oct. 4. It will be held at CERN. Two days of contributed talks and three days of training, hackathons and birds of a feather sessions. Deadline for registrations and abstract submissions ended last Friday.
    - 137 people registered (~65 in person)
    - 25 abstracts received, they are being reviewed now

### Compute and Accelerator Forum

- [9 Oct](https://indico.cern.ch/event/1329694/), RISC-V variable precision acceleration.

---

## AOB

### Website

There is an [issue in GitHub](https://github.com/HSF/hsf.github.io/issues/1411) to gather ideas about reorganising and revamping the website to better reflect our areas of actual activity. Please contact Mark and Graeme if you would like to help.


### Next Meeting

Next meeting will be [26 September](https://indico.cern.ch/event/1355757/).

Reminder: please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing this or one of the future coordination meetings - we need volunteers from now until the end of the year!
