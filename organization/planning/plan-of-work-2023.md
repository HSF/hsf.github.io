---
title: HSF Plans for 2023
author: Graeme Stewart
layout: plain_toc
---

## Preamble

In the first few months of 2023 the HSF again established some high-level
plans and goals for the year ahead. While none of these are cast in stone, we
remain agile to adapt to new opportunities and circumstances throughout
the year. This planning is a useful guide to our activities.

We encourage experiments and projects to take a look at these and
always welcome any suggestions about how to make the HSF more effective
and useful for HEP.

### Reference Presentations

* See the slides that were presented at HSF Coordination meetings on [19 January](https://indico.cern.ch/event/1225007/),
[2 February](https://indico.cern.ch/event/1225008/), [16 February](https://indico.cern.ch/event/1225009/)
and [30 March](https://indico.cern.ch/event/1225012/)

### Previous Plans

* [Plan of work 2022](./plan-of-work-2022.html)
* [Plan of work 2021](./plan-of-work-2021.html)

## Overall HSF Activities

### General Meeting Series

* Continue with regular [coordination meetings]({{ site.baseurl
  }}/meetings/coordination.html) every 2 weeks (on the odd-numbered weeks of the
  year by default).
* The [Compute Accelerator Forum]({{ site.baseurl
  }}/meetings/compute-accelerator-forum.html), co-organised with SIDIS and
  openlab, has established itself as a strong series of meetings with good turnout,
  focusing on new compute architectures. We shall continue to find interesting topics to present.
  * As there is a significant cross-over with the WG activities in many places, we should
    consider joint organised meetings when appropriate
* Monthly [*Software and Computing Roundtable*]({{ site.baseurl
  }}/meetings/roundtable.html) meetings, co-organised with JLab and BNL, cover general topics of interest and the engagement
  of the HSF increased through 2022. We should continue to advertise the meeting
  and use this as an engagement opportunity for speaking to Nuclear Physics
  colleagues.

### Workshops

* As travel restictions have now largely eased, we can organise more workshops
as in-person events, which we know are extremely productive, after last year's
[Analysis Ecosystem II meeting](https://indico.cern.ch/event/1125222/)
* In particular, we plan a [pre-CHEP workshop with WLCG](https://indico.cern.ch/event/1230126/), that should focus on
common topics between software and computing infrastructure
  * Use of non-x86 hardware on at WLCG sites
  * Analysis Facilities

See below for PyHEP and Generators workshop ideas.

## Working Groups

### Physics Event generators

* Priorities:
  * Event generation:
    * Event generation for LHC and HL-LHC
    * Cross-cutting aspects with other experiments in NHEP
  * MCEG R&D:
    * Cutting-edge software technology
    * Standards for shared elements
* Working group discussions:
  * More engagement in the WG?
  * Follow up on LHCC and Snowmass/P5
  * New documents?
* Workshop planning:
  * MC4EIC 2023 (tba)
  * Follow up of the [2018 workshop](https://indico.cern.ch/event/751693/)?
* Training:
  * Tuning tutorial (co-organize with Training WG)

### PyHEP

#### PyHEP 2023

* [The 5th anniversary workshop!](https://indico.cern.ch/event/1252095/)
* Online workshop, we converged on the week of October 9‒13
  * To be advertised soon, but see next slide …
* Targeting as always the broader audience of developers and physicists:
  * Idea of connecting Python users in HEP

#### PyHEP Dev Workshop

* New this year: [In person workshop for Python package developers](https://indico.cern.ch/event/1234156) @ Princeton, USA
  * 25-29 July, at Princeton, aiming for ~50 people
* *Idea to get developers getting their software products to work together as a coherent ecosystem, and plan a coherent roadmap and make priorities for the upcoming year*

#### Topical Meetings for 2023

* Thinking about possibility to do joint meetings with IRIS-HEP / other HSF WGs or other interested parties
  * Agreed already with IRIS-HEP
* We need to define better the goal of the meetings:
  * To introduce users to new packages?
    * Now harder to find packages that are at a stage where there is a package that is on the verge of becoming mature
  * To connect to various working groups, analysis groups, experiments to connect users?
  * Possible to have better overlap with training working group as well

### Detector Simulation

* Following up on developments of or in the area of
  * Opticks
  * FLUKA
  * Simulation on GPUs and co-processors in general
  * ML/AI related to simulation (including training on Geant4 samples)
  * Fast Simulation
  * Differentiable simulation
  * Simulation of future experiments (at EIC, FCC, and others)
* Techniques used to optimize geometry
* Optimization of Geant4 cuts and materials as done by experiments
* Simulation of effects like space charge

* Topics overlapping with other working groups:
  * Integration of Geant4 and Event Generators
    * E.g., in the area physics models, processes, including exotic physics/particles
  * Sharing experiences of extending Geant4 by experiments
  * Integration of processing frameworks, Geant4 as well as Event
Generators
    * Simulation aspects of ACTS (A Common Tracking Software)
  * Integration of Geant4 into Python based frameworks
    * More generally, Python/Julia bindings in simulation packages

### Frameworks

* Improve interactions with other WGs
  * Accelerator usage, Simulation, ...
* Potential topics for meetings/discussions
  * Integration of accelerators into experiment frameworks
    * Allen and Gaudi in LHCb
    * Integration of CUDA and Alpaka (and beyond) in CMSSW
  * Incorporation of ML models into frameworks. Management of ML model files
  * New language features
  * New parallelism libraries as a potential long-term alternative to TBB
    * E.g., HPX
  * Key4Hep

### Software Training

* Switch to intermediate target audience and HEP-specific tools
* Teach more scikit-HEP & IRIS-HEP packages
  * Active community that is interested in growing its user base
  * Use IRIS-HEP fellowships to expand training fellowships
* Coordinate with new initiatives from the Research Software Engineering World
* Be more open to materials of different formats and from different authors
* State of Training Survey: identify blind-spots, start subgroups to work on them
* Improve liaisons to experiments
* Report experiences in Journals like JOSE
* Hybrid training events

* Expand Training Center
  * Vision: One website as entry point for all HEP related training material

* Concrete Events
  * Carpentry workshops (still included in subscription):
    * How can we lower attrition?
    * How do we bundle carpentry intro together with our previous “last day” (if at all) → should probably be
separate indico agenda
  * Analysis preservation
    * Second event in summer for scale?
    * Now that all videos are in place, only need to find mentors for last day, so relatively easy
  * ML + GPU
    * Already have material, so should be somewhat easy to set up

### Software Tools and Packaging

* Continue Spack Discussions with contributions from Spack Developers and Experiments
  * Update on EESSI
  * Python packaging
* Together with other Working Groups:
  * C++ language features
  * Spack training material

### Data Analysis

* Data compression
  * several speakers and novel areas identified
* Open data
  * LHCb now has significant open data set
  * Key for AGC, can serve as common ground for “challenges”
* End user survey of data analysis approaches across experiments
  * Needs careful design & large representative set of responses
  * No recent comprehensive results available -> good to get overview of field
* Set up a “Systematics challenge”
  * Small analysis task to probe handling of systematic uncertainties
  * Needs careful design (scope, effort involved to contribute)
  * Would naturally frame further discussions on this topic following AEWII

### Reconstruction and Software Triggers

* Hot topics?
  * 2021 survey showed 4D reco and heterogeneous computing - still relevant today
* New topics
  * Open data initiatives: Open data for reco studies (open thread by former conveners)
  * Biased triggering and missed physics:
    * Experiment TDAQ design and trigger/reco biases
    * Strategies to “leave no stone unturned”
  * Sustainability: Impact, indicators, better practices
  * Focus on small/medium-sized experiments, e.g. Common DAQ/software frameworks
  * Lessons learned” from new/upgraded experiments after 1-2 years of data-taking

* Have a [kick-off meeting](https://indico.cern.ch/event/1273894/) - confirmed for 26 April
  * Introduction to the group
    * Highlight differences & commonalities among experiments
    * WG as place where to discuss issues that someone else may have already solved
  * List of plans - old survey & new ideas
  * Open the floor to proposals from participants
    * Make a google-doc available in advance
