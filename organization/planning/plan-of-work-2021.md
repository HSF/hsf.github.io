---
title: HSF Plans for 2021
author: Graeme Stewart
layout: plain_toc
---

## Preamble

* In the first few meetings of 2021 the HSF established some high-level
plans and goals for 2021. While none of these are cast in stone, we
remain agile to adapt to new opportunities and circumstances throughout
the year, they are a useful guide to our activities.*

* We encourage experiments and projects to take a look at these and
we welcome any suggestions about how to make the HSF more effective
and useful for HEP.*

## Overall Activity and Coordination

* Reference: 7 January 2021 [slides](https://indico.cern.ch/event/981562/contributions/4134317/attachments/2167697/3693851/HSF%202020-2021%20Review%20and%20Planning.pdf) 
and [meeting minutes](/organization/2021/01/07/coordination.html).*

### Meeting Series

* Continue with regular [coordination meetings](/meetings/coordination.html) every 2 weeks (on the odd-numbered weeks of the year by default).
* Monthly [*Software and Computing Roundtable*](/meetings/roundtable.html) is an ideal place to speak to the Nuclear Physics community (BNL and JLab co-organise), but we should make sure the more widely known and undeline that it is not just for Nuclear Physics colleagues.
* Also monthly, the [Compute Accelerator Forum](/meetings/compute-accelerator-forum.html) made a very good start last year and attracts a lot of interest - good that it's co-organised with SIDIS and openlab.

### Workshops

* Although we had two successful workshops in 2020, there is a real sense of zoom-fatigue in the community.
  * Therefore we will not organise any large workshops in the first half of 2021.
  * There is a slot for a possible workshop at the end of September (w/b 27 Sept), but we don't yet take a firm decision on that.

* We will consider more 'one-shot' mini-workshops that cover topics which bridge between working groups, e.g., I/O matters that touch analysis, frameworks and facilities.

### Organisational Engagement

* We already have quite a long list of organisations with which we have a link or some engagement (see slide 11 of the presentation above).
  * Keep this up and be alert for additional opportunities.
  * In particular in the next ~year the Snowmass process will be important (this has been delayed by a year).

### Software Projects

* It can be useful for projects to be associated with the HSF (e.g., listed as a project or
  making use of our GitHub organisation).
  * We should be alert to these opportunities, particularly when the working groups
    can identify areas of common interest or tools that can expand their user base.

### Post-CWP and LHCC

* As we prepare activity for the year we should not forget to look back to the
  [Community White Paper](/organization/cwp.html) and see which plans there were
  put into place, by the HSF directly or in other contexts.

* We already did some of that in preparing last year's [LHCC review document](https://zenodo.org/record/4009114).
  * This year Graeme and Liz have a role for the HSF/WLCG again in this process, so we remind people this can still be useful.

## Working Groups

*Reference: 21 January 2021 [meeting minutes](/organization/2021/01/21/coordination.html).*

### Data Analysis

Ongoing series of metadata discussions seems like a workable format to repeat on other topics. So this and other themes for 2021 could be:

* Metadata in analysis
  * Lots is needed and it's often time consuming for analysts to find and verify all the data they need
  * There's usually no standard way of doing this - lack of uniformity
  * Series of three meetings looking at different aspects of the metadata needed for analyses:
    * Calibrations and scale factors and cross-sections & other similar non-event data needed for analysis
    * Event processing & book-keeping
    * How this is all combined for an analysis
* Declarative analysis & analysis frameworks
  * Want to avoid this becoming a competition —> focus on interfaces & usability?
  * Incorporate workflow management as well as event processing
  * Identify the most essential functions of an analysis framework & how these should be provided to the user
  * Could have follow-up meeting or even mini-workshop to expand benchmarks (c.f. <https://github.com/iris-hep/adl-benchmarks-index>)
  * To-do: review what IRIS-HEP is up to, so we don’t duplicate
* Overviews from non-LHC experiments
  * We as conveners still lack some awareness of the major issues in some other communities
  * Thinking to invite reps from e.g. neutrinos, nuclear physics to describe what issues they are grappling with
* Reduced data formats (NanoAOD/DAOD_PHYSLITE)
  * Attempted conversations with the non-mainstream analyses
  * Should we revisit questions of policy (i.e. how to engage user base), consequences (framework design, sites)
  * Also haven’t spoken to WLCG/DOMA in a year (<https://indico.cern.ch/event/890991/manage/timetable/#20200323>), try to reconnect? But needed more concreteness on what studies should be done.

Besides these, we discussed commonalities with Training WG. One question: how much should HSF branch into (experiment-agnostic) analysis tutorials?

* Curriculum has a basic CMS example — without going heavily in on teaching physics, could this be expanded to cover statistical tools, demonstrate analysis ecosystem e.g. PyHEP? But don’t want to be prescriptive.
* (Probably) have had discussions comparing e.g. CMS DA school and ATLAS SW tutorial? Can HSF material usefully be integrated into these?

### Detector Simulation

* Topics and cross-group areas:
  * Simulation for liquid noble gas detectors (covering both neutrino and dark matter experiments)
  * Use of FLUKA/MARS by experiments
  * Geometry: e.g. developments/experiences with DD4hep, VecGeom
  * Dealing with pile-up (possible cross-link with Frameworks, Reconstruction?)
  * Computational challenges in future detectors (e.g. muon colliders)
  * Use of GPUs and similar accelerators
  * Developments in ML for simulation
* Will keep in touch with Geant4 Task Force for R&D to avoid duplication and identify possible joint meetings
* Further ideas and input very welcome, especially for cross-WG items, e.g.
  * Use of Python with/for Simulation?
  * Training: link up with Geant4 material/courses?

### Reconstruction and Software Triggers

* Areas of common interest (in general these are topics related to HL-LHC and off-LHC experiments, LHC Run 3 R&D is basically closed):
  * ML for and its integration into production code
    * Machine learning frameworks for performant inference engines in real-time supporting various hardware backends (possible links to fastML, clariphy, ...)
    * make the step from conceptual studies to production code integration
  * Alignment / calibration 
    * points of collaboration on "sharp knife" tools
  * Particle flow
    * was initially planned in last term but did not materialize
  * Event data formats and geometry (overlaps with other groups)
    * great possibility to have an overlap session with simulation
  * Use of heterogeneous architectures
    * establish small scale demonstrators outside the experiments' structure
    * investigate inclusion of common HEP reconstruction & trigger packages into such systems

* Establish closer link to training group, expanding from pure technical training
  *  e.g.: general introduction to HEP triggers and reconstruction and introduction to the methods used; can training be done on little demonstrators:
    *  ALLEN demonstrator of multi-event scheduling framework for GPUs, allowing to interleave host(CPU) and device(CPU / AMD GPU / Nvidia GPU) algorithms, where the device type is chosen at compile time (same source code for all device types)
    *  Patatrack, ACTS etc. on OpenDataDetector
* Help integrating common packages into turn-key demonstrator projects
  * natural connection: CERN EP-R&D turn-key  (Key4hep)
* Short, one-day workshops on specific topic, with possible overlap between HSF working groups:
  * trigger/reconstruction & simulation (fast MC initiatives, EDM/Geometry)
  * trigger/reconstruction & analysis (no clear boundaries)
* **Next Steps**
  * Talk to trigger & reco conveners of experiments
    * last survey is ~1.5 years old
  * Talk to computing projects of experiments
  * Make sure to include non-LHC experiments

### PyHEP

* **PyHEP 2021 workshop:**
  * Date to be decided. Likely just after SciPy 2021, which takes place as a virtual event on July 12-18.
* **Topical meetings:**
  * We are running this year a kind of "Python module of the month" meeting, by default the first Wednesday of each month at 16h CET.
  * Topics so far confirmed are, see [Indico](https://indico.cern.ch/category/11412/):
    * Feb 3rd: Numba, by Jim Pivarski.
    * March 3rd: JAX, by Hans Dembinski.
    * April 7th: pyhf, by Giordon, Lukas and Matthew.
  * We welcome suggestions of topics very much.

### Software Tools and Packaging

* Packaging Topics
  * Follow-ups on Spack
    * With the Key4hep group
    * Efforts at Fermilab for LArsoft
  * See how other support projects are doing things
    * EESSI - European Environment for Scientific Software Installations
    * Compute Canada
* Tools
  * Static analysers
  * Profiling
    * Already started to discuss `perf` and plan a follow-up
  * IDEs

### Software Training

* Plans for 2021:
  * Beef out the HSF curriculum <https://hepsoftwarefoundation.org/training/curriculum.html>
  * Nail down how to measure success (surveys?)
  * Encourage more people to integrate into the HSF Training community
  * Strengthen friendship with Software Carpentries
  * Collaborate with other HSF working groups to hold trainings
  * Emphasise the interplay between training and careers
* Hackathon is being actively followed up, to continue to develop material.

### Event generators

* Complete the paper at last! (should be ready in ~few weeks)
* Arrange meetings to discuss work done by others as in the plans laid out in detail in the paper, many areas of work:
  1. Understanding of the current CPU costs by accounting and profiling. 
    * There has been separate work on e.g. profiling MG5_aMC and Sherpa which actually show some common conclusions
        * Time to bring this together and compare more apples-to-apples
    * Look ahead to NNLO codes?
  2. Moving to GPUs/accelerators. 
    * Continue effort on the MG5_aMC GPU port
    * Try to follow-up better on similar activities for other generators (e.g. Sherpa and Pythia8)
  3. Optimisation of phase space sampling and integration algorithms, including the use of ML 
    * This is somewhere we have not yet made large inroads - it will become a larger focus.
        * Topical meeting for the WG.
  4. Reducing the cost associated with negative weight events 
    * Quite some discussions on this already in the WG
      * In particular at the November WS
    * Next steps…?
      * Trying to get existing tools more integrated into generator/experiment/ workflows
  5. Promote collaboration, training, funding and career opportunities in the generator area:
    *Collaboration*
    * Build contacts with relevant projects:
        * E.g. Excalibur/SWIFT-HEP (UK) and HEP-CCE (US)
        * Offer a forum for communication between the two groups and help avoid overlaps?
    * Engage more with the Experiments?
        * There is work that has already been done but doesn’t always make it into the experiment workflows
    * Engage more with Nuclear people? Use contacts established via S&C Roundtable
    * Neutrino community - Liz has some contacts

* Career opportunities and funding
  * Not sure exactly what the WG can do here currently other than raise the visibility of the work through e.g. the paper and presentation at LHCC...

* Training
  * So far we have not been active in providing training
    * Should discuss this with HSF Training folks!
  * Need to think what that would look like…
    * E.g. would generator-specific code training be possible/make sense?
    * If not, do we need more “generic” training on e.g. programming for GPUs, profiling etc.?
      * This might be more the right emphasis from HSF.

### Frameworks

* Have free-form-discussion meetings between the experiments once a month
  * First Wednesday of every month, starting on March 3rd
* Multi-meeting discussion about heterogeneous computing usage in experiment frameworks
  * Joint meeting with Packaging WG about build system / packaging aspects of heterogeneous software releases?
* Invite “DOE parallel I/O developers” to show what they are working on
* Discuss work to remove use of TBB deprecated APIs from frameworks
* Investigate whether guidance (e.g. webpages) can and should be assembled regarding framework aspects such as multithreading, metadata, offloading, etc.
