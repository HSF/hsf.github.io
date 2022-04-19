---
title: HSF Plans for 2022
author: Graeme Stewart
layout: plain_toc
---

## Preamble

At the beginning of 2022 the HSF established some high-level
plans and goals for the year ahead. While none of these are cast in stone, we
remain agile to adapt to new opportunities and circumstances throughout
the year. This planning is a useful guide to our activities.

We encourage experiments and projects to take a look at these and
we welcome any suggestions about how to make the HSF more effective
and useful for HEP.

### Reference Presentations

* See the [slides](https://indico.cern.ch/event/1096580/) that were presented at
the HSF coordination meeting on 20 January 2022.

### Previous Plans

* [Plan of work 2021](./plan-of-work-2021.html)

## Overall HSF Activities

### General Meeting Series

* Continue with regular [coordination meetings]({{ site.baseurl
  }}/meetings/coordination.html) every 2 weeks (on the odd-numbered weeks of the
  year by default).
* Monthly [*Software and Computing Roundtable*]({{ site.baseurl
  }}/meetings/roundtable.html) meetings, co-organised with JLab and BNL, cover general topics of interest and the engagement
  of the HSF increased through 2021. We should continue to advertise the meeting
  and use this as an engagement opportunity for speaking to Nuclear Physics
  colleagues.
* The [Compute Accelerator Forum]({{ site.baseurl
  }}/meetings/compute-accelerator-forum.html), co-organised with SIDIS and
  openlab, established itself as a strong series of meetings with good turnout
  last year, focusing on new compute architectures. We shall continue to find interesting topics to present.
    * As there is a significant cross-over with the WG activities in many places, we should
    consider joint organised meetings when appropriate.

### Workshops

* The COVID situation continues to complicate the planning of any in-peron events, however we plan at least two events for this year:
  * Analysis Ecosystems Workshop, which we strongly wish to be in-person; hopefully at IJCLab at the end of May
    * It is five years since the Amsterdam meeting, time for an update!
  * Community meeting on simulation on GPUs, which will be virtual at the beginning of May
    * Sufficient progress has been made on the R&Ds here to merit wider discussion and input

* In additional a possible follow-up meeting on generators is being considered

## Working Groups

### Data Analysis

* Would like to better generate interest among analysis people
  * Find the relevant fora in different experiments
* Possibly another meeting on workflow management tools, given good past attendance
* Implementing systematic uncertainties in an analysis:
  * What are experiments doing? Can core software frameworks help?
* HSF analysis ecosystems workshop: synergies?
* Ideas to develop
  * Expand on benchmarks discussions
  * Efficiency/green analysis. Does anybody work on this already? Survey?
  * Find out what are the biggest problems that analysis people face? Survey?

### Detector Simulation

* Non-Geant4 detector simulation packages, e.g., MARS, FLUKA
* DD4hep (+ other geometry topics)
* Progress in ML and other fast simulation techniques
* Progress of AdePT/Celeritas and related projects
* Progress in optical photon simulations
* Detector simulations for future colliders
* Aspects of varying Geant4 parameters
* Topics potentially overlapping with other working groups:
  * Interfacing Geant4 with simulation frameworks (including the role of Geant4 Tasking)
  * Detector/event visualisation techniques
  * Python/Julia bindings in simulation packages

### Reconstruction and Software Triggers

* 2nd part of 4D reconstruction topical meeting
  * focus on algorithms
* Machine learning
  * Graph neural networks for reconstruction (topical meeting)
  * Learning to discover workshop summary wrap-up (topical meeting)
  * Coordinate with reco session at AI4EIC workshop (2022 workshop TBD)
* Open data sample
  * Showcase usages of existing samples in topical meeting
  * Tracking Open Data Detector released (ACAT) & decoupled from ACTS
  * Create calorimeter data sample (discussion started)
* Particle flow (topical meeting)
  * LHC experiments experience
  * Current status and plans of other experiments (e.g. sPhenix, EIC experiments)
* Flavor tagging (topical meeting, possibly joint with analysis WG)
  * HF resonance reconstruction and HF jet tagging
* Calibration / alignment & conditions handling in reconstruction
  * Topical meeting (together with framework group?)
* Training material on heterogeneous computing for reconstruction & triggers
  * Together with training group?
  * Needs some discussions and planning
* Heterogeneous computing in reco & triggers - together with compute accelerator forum
  * “Classical” approach: Patatrack + additional project
  * “Exotic” approaches: quantum computing, IPUs, TPUs etc.
* Software trigger and reconstruction for streaming readout experiments
  * Coordinate HSF joint session at Streaming Readout Workshop X and XI (last two at MIT and ORNL, expect two workshops in 2022, TBD)

### PyHEP

#### 2022 Workshop

* Since we’re no longer planning to co-locate with SciPy in Austin, TX, choosing a date within a week of SciPy is no longer a benefit
* We’re considering end of August/beginning of September instead of July.
* We’re thinking of adding new features (still brainstorming)
  * Maybe adding hackathon / community building specific contributions
* Would mean a call for “short tasks” across the ecosystem packages aside the usual call for presentations
  * Possibly, hackathon in person at CERN’s Ideasquare

#### Topical Meetings

* “Python module of the month” → more general “topical meetings”?
  * We are looking to more structurised topical meetings covering a wider set of Python modules (starting from fundamentals and including more HEP specific)
  * Topical meetings are expected to have clearer division between tutorials, short talks and discussions
* Some of topical meetings could include larger time slot for following discussions and questions in a form of “office hours”
* We welcome joint endeavours with other WGs where relevant
  * Data Analysis & Training WGs have obvious overlaps

### Software Tools and Packaging

* Spack will continue to be a focal point from the packaging perspective
  * Planning to get more feedback from the users to promote collaboration
  * Possibly a good idea to keep tracking alternatives, e.g. EESSI, as done previously
* Continue discussions on various profiling tools, static analyzers, IDEs etc.
  * Again, as a cross-WG effort, can host a dedicated discussion on GPU profiliers
  * Battle proven tools, such as perf, VTune, etc. will continue to be discussed
* Promote some discussion on the “new features” of C++
  * Similar to PyHEP’s module of the month
  * Discuss new libraries and/or language features that are useful in the context of HEP

### Event generators

#### High-level plans for 2022

* Snowmass input document
* Expand into NP community (with Markus’ help!)
* Also try to reach out more to the neutrino community.
* Go back to more “topical” meetings
  * Need to follow up on various things highlighted in CSBS paper and HL-LHC review
  * Also need to catch up a bit with more recently developments
  * Could also be useful to have a workshop?

#### Possible Topical Meetings

* MC for EIC:
  * Report from previous MC4EIC WS, Contributions for Spring WS?
* Latest calculations and their CPU/negative weight performance
  * MiNNLO, ttbar NNLO calculations, Recent ATLAS V+jets paper [PMGR-2021-01]
* ATLAS/CMS/LHCb
  * CPU/Event accounting for central production, Sample sharing, Filtering inefficiencies for B-physics
* GPU/CPU vectorisation porting
  * Status from MG4GPU, Sherpa, other groups?
* Unweighting/resampling developments
  * Review of tools, integration into experiments and usage/viability for experiments
* ML tools
  * Get better overview of current usage of ML and work out what is genuinely useful for experiments
    * Phase-space Sampling improvements, Use in systematic uncertainties, GAN for event generation
* Benchmarking and validation
  * Docker image for using generators for benchmarking? Spack and CI for validation?
* Modular generator software framework
  * Is it feasible? How to initiate?
* Reports from other groups
  * SWIFTHEP/EXCALIBUR (UK), HEP-CCE (USA), Others?
* Training
  * Discuss with Training WG
  * Replacement for MCnet schools?
* More long-term/speculative topics to follow more closely
  * Julia
  * Quantum Computing for event generation

### Frameworks

* Reaching out to small experiments
* More involvement from the nuclear physics community
* Collaborate with other WGs
  * Perhaps a common conditions database API
  * Accelerator usage
* Potential topics
  * Effect of C++ evolution on frameworks/accelerators
  * Scalable I/O (using ROOT, HDF5, etc.)
* More reliable schedule
  * Better advance notification of meetings
  * Predictable meeting time/date

### Software Training

* Sustainability of the training model.
  * Software Carpentries training 3-4 times per year
  * Future training events depend on keeping a pool of instructors.
  * Ensure the reward of participating as mentor. Exposure outside experiments.
  * Contact participants from previous workshops and invite them to contribute to coming events.
  * Advertise the opportunities to grow professionally.
* Scale up efforts to collect feedback before and after training events
  * After basic courses, collect more information on what people are interested in. Use it for prioritize
development of training modules.
  * Take the results of surveys and prepare a publication with the outcome.
* Strength the communication with other WGs for training topics
  * HSF Simulation group & reconstruction group?
* Conference and Publications
  * Look for conference to advertise training efforts
  * Publish papers on data collected during surveys