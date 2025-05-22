---
title: "HSF Coordination Meeting #288, 22 May 2025"
layout: plain_toc
---

## Attending

Present/Contributing: Graeme Stewart, Claire Antel, Pere Mato, Luke Kreczko, Sapta Battacharya, Tommaso Lari, Krzysztof Genser

Apologies/Contributing: Eduardo Rodrigues, Paul Laycock, Michel Villanueva, Alexander Moreno

## News, general matters, announcements

### European Strategy Update (EPPSU) final stages

Journal submission: EPJC is waiting our submission but not done yet due to lack of time...

We have one reference to update, #101 (ATLAS paper, now published).

### HSF/WLCG Workshop

Workshop came off well! HSF overview presentations:

- [HSF Introduction](https://indico.cern.ch/event/1484669/contributions/6463259/attachments/3060782/5412392/HSF%20Introduction_%20WLCG_HSF%202025.pdf)
- [HSF Recap and Next Steps](https://indico.cern.ch/event/1484669/contributions/6480469/attachments/3064177/5419534/WLCG_HSF%202025%20-%20HSF%20summary-2.pdf)

We had HSF sessions on Common software and Software Projects, Sustainable Software and Training. As well as plenaries on AI/ML and heterogeneous computing; and Analysis at scale and analysis challenges.

Outcomes:

- In the HSF BoF we discussed project affiliation. Feedback that bronze, silver and gold were interpreted in a "judgemental" way, i.e., that bronze would be viewed as pejorative and not be good for the project.
    - Some follow-up discussions are forming a proposal that we have core criteria for projects to fulfil that allows them to be affilites, viz. the [*Best-practice Guidelines*](https://hepsoftwarefoundation.org/projects/guidelines.html).
    - There are a set of *bonus* badges when projects are outstanding in particular areas, e.g., documentation, training, user support.
        - These can be developed over time.
    - We will try to come up with a more concrete proposal (will have an SG discussion) - input and feedback welcome!
- Sustainable Software is a very important topic
    - This could be an HSF focus area and we can work in partnership with projects like EVERSE
    - Follow up activity suggestions
        - HSF Training on Software Sustainability
        - HSF Seminar mini-series

### LHCC Meeting

Eduardo has started to [prepare the inputs](https://docs.google.com/presentation/d/1A9iOPT9s54-B3yirfThaELAmQ0iI9guhiD6jeNS02o4/edit?usp=sharing) for the next LHCC referees meeting on 3 June.

Comments and suggestions by *tomorrow*, 23 May, please.

### IRIS-HEP Steering Board

Reminder that Caterina Doglioni is now the HSF representative at IRIS-HEP.

[Draft slides](https://docs.google.com/presentation/d/1zrV0P_kIDxwDS9bZsYYE6S3HXPUsaEXfKkQUYr8EjmA/edit?usp=sharing) from the HSF for the next meeting on 3 June - comments welcome.

### HSF Seminar Series and Compute Accelerator Forum

Planned seminars:

- 28th May, 16h30 CEST: Seminar on AdePT and Celeritas update on detector simulation with GPUs. <https://indico.cern.ch/event/1528440/>
- 4 June, 16h30 CEST: AI-assisted software tools. <https://indico.cern.ch/event/1549643/>
- 11 June, 16h30 CEST: Julia on GPUs for fun and profit. <https://indico.cern.ch/event/1472683/>
    - This event co-organised with the [EVERSE Network](https://everse.software/network/)

Venice workshop report tentatively scheduled for September. dCache project have signalled interest in presenting in a future Seminar.

HSF seminar conveners are reachable at <mailto:hsf-seminar-conveners@googlegroups.com>

- Please send your suggestions for next seminars

### Steering Group

Next SG meeting will be 3 June, <https://indico.cern.ch/event/1550243/>.

### HSF Affiliated Projects and Software

ACTS: Graeme will present a HSF Project Affiliation in their next dev meeting (even if exact iteration on badges not yet decided).

## Activities Updates

### Software Training

Future events:

- [HSF/IRIS-HEP Software Basics Training (Hybrid)](https://indico.cern.ch/event/1516608/) - Jun 18-20. Hybrid at CERN. Registration is open!
- [Deep Learning Train-the-Trainer Workshop](https://indico.desy.de/event/47263/) - Sept 15-19. Organized by the HSF and ErUM-Data-Hub. In-person in Potsdam. Registration is open! Deadline: August 4

### Physics Generators

- Negative weights workshop: https://indico.cern.ch/event/1501347/timetable/#20250505.detailed (maybe we can invite Jeppe to give us summary)
- Optimising Floating Point Precision Workshop: https://indico.cern.ch/event/1538409/overview

Topic of generators in the neutrino community would be interesting.

Website still needs updated with current convener names.

### PyHEP

[PyHEP.dev 2025 Workshop](https://indico.cern.ch/event/1515852/) will be held at University of Washington from July 14 to 17.

### JuliaHEP

[JuliaHEP 2025 Workshop](https://indico.cern.ch/event/1488852/) will be held at Princeton from July 28 to 31.

- Abstract submission is still open until 31 May
    - the number of submissions is approaching that of last year
- Final registration deadline: July 7

## AOB

### Physical Constants

Graeme discussed with ATLAS who are concerned about the number of different places where physical constants get defined in HEP, viz. at least in [CLHEP](https://gitlab.cern.ch/CLHEP/CLHEP/-/blob/develop/Units/Units/PhysicalConstants.h?ref_type=heads), [ROOT](https://github.com/root-project/root/blob/master/geom/geom/inc/TGeoPhysicalConstants.h) and [Geant4](https://gitlab.cern.ch/geant4/geant4/-/blob/master/source/externals/clhep/include/CLHEP/Units/PhysicalConstants.h).

This mainly seems to affect C++, Python is more conststent with [hepunits](https://github.com/scikit-hep/hepunits) and Julia has [PhysicalConstants.jl](https://github.com/JuliaPhysics/PhysicalConstants.jl/).

Defining constants in larger HEP packages binds the physical constants to other software updates, which is not great. None of the packages, except for Julia, offer explicit versioning of the constants (and they **do** change, e.g., Plack's constant was [updated in 2019](https://physics.nist.gov/cgi-bin/cuu/Value?h) and is now *defined*, not measured).

Q. Is there interest in having a common stand-alone library for this? C++ seems to have the greatest need. The Python package might usefully get versioning. For Julia one could imagine at least a cross-check and validation.

- This would be naturally an HSF project
- "Truth" would be from PDG (which for physical constants uses the CODATA recommendations)
    - Values can be programmatically obtained via. an [API](https://pdg.lbl.gov/2024/api/index.html)
    - Then dropped into a generated source file

Generators are also rather messy here, with their own definitions of these values. Or user defined values at the top of data cards!

General feeling this is a good topic to address. Graeme will organise a follow-up meeting.

### Next Meeting

The next coordination meeting will be 5 June, <https://indico.cern.ch/event/1477079/>.

### Chair This Meeting 👇

Please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing a future coordination meeting. (There is even a [HOWTO guide](https://hepsoftwarefoundation.org/organization/running-meetings.html)).
