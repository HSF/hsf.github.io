---
title: "HSF Coordination Meeting #294, 25 September 2025"
layout: plain_toc
---

## Attending

Present/Contributing: Eduardo Rodrigues, Claire Antel, Joe Osborn, Ines Ochoa, Torre Wenaus, Alexander Moreno, Maarten van Veghel, Michel Hernandez Villanueva, Nick Smith, Sapta Battacharya, Juan Miguel Carceller

Apologies/Contributing: Stefan Roiser, Graeme Stewart (moving house!)


## News, general matters, announcements

### European Strategy Update (EPPSU) 

Our EPPSU submission has been submitted EPJ-C.

There were some comments about the use of acronyms, which we should define more clearly (or add a glossary).
* Michel is looking into it, see [this PR](https://github.com/HSF/EPPSU-2025-Paper/pull/21).

### HSF Seminar Series and Compute Accelerator Forum

Recent HSF seminars:
- Yesterday: [_dCache (as a software project)_](https://indico.cern.ch/event/1575146/)
    - Very good presentation on how dCache runs.
    - ~30+ people connected.
    - Recording uploaded to YouTube.

Planned HSF seminars:
- Oct. 29th: _European Strategy Report: Inputs, Impressions, Venice Open Symposium Highlights_.
- Dec. 3rd: _HS3_.

Others in the works:
- Seminar on OpenData organised by trig & reco software.
- 2nd in series on AI-assisted sw tools organised by software tools & packaging.

(Thanks to the activity groups for coming to us with seminar ideas and speakers!)

HSF seminar conveners are reachable at <mailto:hsf-seminar-conveners@googlegroups.com>.

Compute & Accelerator forums:
- Oct. 8th: [Error estimation for floating point operations via automatic differentiation](https://indico.cern.ch/event/1472686/).
- Nov. 12th: [A Formal but Pragmatic Foundation for General-Purpose Operating Systems](https://indico.cern.ch/event/1472688/).


- Please send your suggestions for next seminars.

### Steering Group

The first meeting post Summer will be held very soon. News will follow appropriately.

Stefan Roiser took over from Eduardo Rodrigues on September 1st as community software on the WLCG Management Board.

### HSF Affiliated Projects and Software

A new version of the project affiliation was prepared early Summer - thank you Graeme Stewart! The system of badges has been simplified as per community feedback. Details at:
- <https://hepsoftwarefoundation.org/projects/affiliated.html>
- <https://hepsoftwarefoundation.org/projects/guidelines.html>

Several projects are being contacted after the Summer.

Recently the evaluation of the [nnpdf](https://github.com/NNPDF/nnpdf) package got concluded - of course positively. Check out [here](https://hepsoftwarefoundation.org/projects/projects.html) for the list of affiliated projects.

## Activities Updates

### Software Training

- #### Past Events:

    - [HEP/IRIS-HEP Software Basics Training (Virtual)](https://indico.cern.ch/event/1569915/), 3-4 Sept
        - Registration:
            - 53 participants registered - ~16 attended the first session, then it went down to ~6 by the end of the day.
            - Pre-Survey:
                - Position/Academic Level:
                    - Junior Ph.D. Students: 30.8%
                    - Undergrads: 25%
                    - Masters Students/Senior Ph.D. Students: 13.5%
                    - Postdocs: 9.6%
                    - Faculty/Staff/Scientists: 7.7%
                - HEP Experiment (or area):
                    - CMS: 21.2%
                    - Belle-II: 19.2%
                    - DUNE: 17.3%
                    - Theory: 7.7%
                    - ALICE: 5.8%
                    - ATLAS/Neutrinos Experiments: 3.8%
                - Timezones:
                    - Americas: 34.6%
                    - Europe/Africa/Central Asia: 26.9%
                    - East Asia/Australia: 11.5%

    - [HEP/IRIS-HEP Python for Analysis Training](https://indico.cern.ch/event/1575769/), Sep. 11. Due to the low number of registrations (17) the event was postponed! Typically, fewer than 50% of those who register actually attend the sessions.

     - [Deep Learning Train-the-Trainer Workshop](https://indico.desy.de/event/47263/), Sep. 15-19. 
         - Organized by the HSF and [ErUM-Data-Hub](https://erumdatahub.de/en/). Thanks to ErUM-Data-Hub, all the organization was amazing!
         - In-person in Potsdam, Germany
         - ~25 people from different fields
         - Talks and hands-on sessions:
             - [Developing a Curriculum](https://indico.desy.de/event/47263/sessions/19805/#20250916): Introduction & Hands-On (Michel Hernandez Villanueva)
             - [Organizing a Training Event](https://indico.desy.de/event/47263/sessions/19804/#20250916): HSF Experience (Alexander Moreno Briceño)
             - A Mini-Intro to Julia (Alexander Moreno Briceño)
             - [Teaching Methodology](https://indico.desy.de/event/47263/sessions/19808/#20250918): Hands-On (Michel Hernandez Villanueva)
             - Outcome of the workshop: training modules written by the participants ([repositories](https://github.com/orgs/erum-data-hsf/repositories))

- #### Ideas for upcoming trainings:
    - Organize the basic training twice a year: once online and once in-person, charging a small fee. The one in-person could be scheduled alongside other in-person events (for instance, summer schools).
    - Move to intermediate and advanced trainings, and keeping the basic material available in the Training Center for self-study.
    
- #### Future Events:
    - [13th HEP C++ Course and hands-on training - Advanced C++](https://indico.cern.ch/event/1549051/overview), Oct 27-31, registration open, places for in person attendance available
    - SSH shell - Hackathon, Oct. 6th
    - Blueprint Meeting on AI - TBD 
        - Survey to collect comments, and then organize a dedicated session with different collaborations to define a roadmap

### Event generators

There is a meeting of the LHC MC Working Group on Oct. 2nd on data sharing and new workflows: <https://indico.cern.ch/event/1568443/>.

### Reconstruction and Software Triggers
- Ongoing work to organize an HSF seminar on open data sets for AI/ML training purposes. We have one on LHC Open data, foundation models for NPP dataset, and potentially one on foundation models from CMS (and maybe trackML?).

### JuliaHEP

- [JuliaHEP 2025 Workshop](https://indico.cern.ch/event/1488852/) was held at Princeton from July 28 to 31.
    - 40 people registered
    - 3.5 days
    - ~20 Talks
    - ~4 Tutorials
    - Keynote Talk by Stefan Karpinski
- We will start soon organising the JuliaHEP 2026 Workshop!

## AOB

### Physical Constants / HEPdata Library

Reminder: we are proposing a C++ header-only library that defines physical constants and some salient HEPdata in a lightweight, easy-to-use manner. Also taking into account versioning.

Status reminder:
- Thanks to Maciej, we became aware that there is a very promising project which has been proposed for C++ 29 standardisation, https://github.com/mpusz/mp-units, so support units and constants in C++. We think it’s the right approach to investigate this library and see if it would be suitable for our needs. If it is on the road to an stdlib inclusion then that makes it much more future proof that anything we would write ourselves.
- The units support looks very well written and robust, and there are already some HEP relevant constants in the library: https://github.com/mpusz/mp-units/blob/master/src/systems/include/mp-units/systems/hep.h. There is a also a lot of documentation about the motivations and a review of existing solutions and their limitations (e.g., Boost::Units).
- So we’d like to proceed to try and both use this library, extend it to the kind of PDG quantities that we would want.

Please let Graeme know if you'd like to be kept in the loop.

### Next Meeting

The next coordination meeting will be October 9th, <https://indico.cern.ch/event/1477088/>, Stefan will chair.

### Chair This Meeting 👇

Please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing a future coordination meeting. (There is even a [HOWTO guide](https://hepsoftwarefoundation.org/organization/running-meetings.html)).
