---
title: "HSF Coordination Meeting #295, 9 October 2025"
layout: plain_toc
---

## Attending

Present/Contributing: Eduardo Rodrigues, Tommaso Lari, Ianna Osborne, Graeme Stewart, Claire Antel, Inês Ochoa, Maarten van Veghel, Liz Sexon-Kennedy, Luke Kreczko

Apologies/Contributing: Michel Villanueva

## News, general matters, announcements

### HSF Seminar Series and Compute Accelerator Forum

Planned HSF seminars:
- 29th Oct: _European Strategy Report: Inputs, Impressions, Venice Open Symposium Highlights_
- Dec 3rd: _HS3_, TBC

Others in the works:
- Seminar on OpenData organised by Trig & Reco SW AA
- 2nd in series on AI-assisted SW tools organised by software tools & packaging
- Seminar from creator of mp-units (suports units and constants in C++, see AOB) - still to be arranged

(Thanks to the activity groups for coming to us with seminar ideas and speakers!)

HSF seminar conveners are reachable at <mailto:hsf-seminar-conveners@googlegroups.com>.

Compute & Accelerator forums:
- We had a meeting on [Error estimation for floating point operations via automatic differentiation](https://indico.cern.ch/event/1472686/) just yesterday
- 12 Nov: [A Formal but Pragmatic Foundation for General-Purpose Operating Systems](https://indico.cern.ch/event/1472688/)

Please send your suggestions for next seminars.

### Steering Group

The first meeting post Summer took place last week. See [the minutes](https://hepsoftwarefoundation.org/organization/2025/10/02/steering.html).

We discussed in particular:
- The HSF budget we collect from our participation in the GSoC programme. This can be used for HSF related activites.
- Idea to create a community repository for bibliographic citations. In the works. It will soon be advertised.
- Status of the affiliation programme. See item below for details.

### HSF Affiliated Projects and Software

Several projects have been contacted after the Summer and evaluations are either in discussion or will happen soon.

Check out [here](https://hepsoftwarefoundation.org/projects/projects.html) for the list of affiliated projects.

## Activities Updates

### Software Training

Oct. 6: a Hackathon on the SSH shell course material tool place.

##### Ideas for upcoming trainings: 
- Organize the basic training twice a year: once online and once in-person, charging a small fee. The one in-person could be scheduled alongside other in-person events (for instance, summer schools)
    - Move to intermediate and advanced trainings, and keeping the basic material available in the Training Center for self-study

##### Future Events:
- [13th HEP C++ Course and hands-on training - Advanced C++](https://indico.cern.ch/event/1549051/overview), 27-31 Oct, registration open, places for in person attendance available
- Blueprint Meeting on AI - TBD 
    - Survey to collect comments, and then organize a dedicated session with different collaborations to define a roadmap

### Event generators

- A 2-day workshop from the LHC Monte Carlo WG is taking place as we speak, Oct. 8-9: <https://indico.cern.ch/event/1553687/timetable/>.
    - The HSF was invited to present on "HSF: Vision and Role in MC Toolchain Sustainability" at the session "Sustainability of the MC toolchain". Sapta presented for us.

### Detector Simulation

The next G4 Technical forum will be held on Oct. 23.

### Reconstruction and Software Triggers
- Ongoing work to organize an HSF seminar on open data sets for AI/ML training purposes. We have one on LHC Open data and one on foundation models for NPP dataset. No confirmation yet from one on foundation models (from CMS colleagues); maybe alternatively one related to ML-based tracking.

### PyHEP

- [PyHEP 2025 Users Workshop](https://indico.cern.ch/event/1566263/): hybrid event at CERN on Oct. 27 - 30. Call for abstracts is open up to Oct. 13 23:59.
    - Over 150 people registered
    - 4 half days
    - Over 20 abstracts: ML, AD, analysis tools, etc.
    - Wednesday at 16:30 - a tutorial by Ashwin Srinath from Nvidia "Pythonic GPU Parallelism for HEP with cuda-cccl"
    - Possibly an awkward package hackathon on Thursday (morning session)

### JuliaHEP

- We will start soon organising the JuliaHEP 2026 Workshop! It will probably be in Germany, so that it takes advantage of JuliaCon 2026 in Mainz.


## AOB

### Physical Constants / HEPdata Library

Reminder: we are proposing a C++ header-only library that defines physical constants and some salient HEPdata in a lightweight, easy-to-use manner. Also taking into account versioning.

John Chapman and Graeme Stewart picked this up again last week. We have asked for *mp-units* to be added to the LCG builds. Then we would like to add a simple header with common HEP constants and gradually migrate towards an integrated solution with mp-units.

Finally, we would like to automate the generation of constant files directly from PDG and CODATA (this bit can be language neutral).

*Additional help/contributions welcome!*

### Next Meeting

The next coordination meeting will be October 23rd, <https://indico.cern.ch/event/1477089/>.

### Chair This Meeting 👇

Please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing a future coordination meeting. (There is even a [HOWTO guide](https://hepsoftwarefoundation.org/organization/running-meetings.html)).
