---
title: "HSF Weekly Meeting #200, 21 January 2021"
layout: plain
---

Present: Graeme Stewart, Josh McFayden, Serhan Mete, Ben Morgan, Kyle Knoepfel, Paul Laycock, Efe Yazgan, Attila Krasznahorkay, Meirin Oan Evans, Michel Jouvin, Andreas Salzburger, Benedikt Hegner, David Lange, Eduardo Rodrigues, Peter Elmer, Stefan Roiser, Gloria Corti, Kevin Pedro, Krzysztof Genser, Liz Sexton-Kennedy, Marc Paterno, Mason Proffitt, Michel Jouvin, Philippe Canal, Stefano Piano, Sudhir Malik, Daniel Elvira, Torre Weanus

Apologies: Dorothea vom Bruch, Caterina Doglioni, Michel Villanueva

## News, general matters, announcements

### CLARIPHY Letter of Collaboration

We are asked for a letter of collaboration from the CLARIPHY project for their NSF funding application. See the [agenda links](https://indico.cern.ch/event/981563/) for background documents.

> Graeme Stewart has agreed to coordinate the collaboration between the HEP Software Foundation (HSF) and CLARIPHY. This collaboration will include co-hosting training and community events of mutual interest

The meeting approved the letter, Graeme will send the signed copy to Pete.

### Linux4Science

We in CERN and Fermilab IT wanted to leverage the HSF community to discuss what to do 
about the policy changes at RedHat/IBM regarding CentOS. While GitHub "Discussions" are 
still in beta, we thought it was worth a try to start one there in order to hear from as many people as possible who wish to contribute.

<https://github.com/HSF/Linux4Science/discussions>

Waiting to add content to the site before advertising it more widely.

### Google Summer of Code

Remember to [submit your project ideas](https://hepsoftwarefoundation.org/activities/gsoc.html) by 15 February! Also check the instructions for changes to the projects this year.

### HEP C++ Course and Hands-on Training

- [Second iteration](https://indico.cern.ch/event/979067/overview) being held this week. Good participation, good level of interaction
- 75 offered places were taken within 2 minutes after opening the registration (+120 on waiting list)
- New, trying to help students to get the course acknowledged at universities for their curriculum
- Many many thanks to Sebastien Ponce for lecturing and all mentors for helping and teaching in the afternoon trainings
    - David Chamont, Stewart Martin-Haugh, Graeme Stewart, Walter Lampl, Attila Krasznahrkay, Benedikt Hegner, David Smith, Ben Couturier, Riccardo Maria Bianchi, Stephan Hageboeck, Andrea Valassi, Bernhard Gruber, Martin Ritter

## Working Group Updates

### Data Analysis

#### Plan for 2021

* Have well defined agenda for metadata discussions (into mid-Feb)
* Had plans to follow up on declarative analysis benchmarking, with goal of a concrete discussion later in the year
* Ideas about more cooperation with Training WG to improve analysis code robustness — should arrange a cross-WG discussion (open?)
* Still room for more concrete planning…

**DAWG Metadata Discussion 1 — Takeaways:**

* Priority features:
    * Good user interface — analysers prefer POSIX over web access to DB (etc). Authentication is considered an obstacle. Does a cvmfs cache suffice? How can we incentivise using existing metadata structures vs inventing own (e.g. dataset name parsing)?
    * Local caching for situations w/o full connectivity, e.g. HPC, HLT. Relocatable paths addressed at least in a couple of ways (Belle II, ATLAS)
    * In some cases, need user input & extension (e.g. higher order cross-section). Also need override functionality, e.g. Belle II mergeable Global Tag.
* Unifying calibration data
    * ATLAS/CMS seem to be partially converging on cvmfs-based write-once storage with versioning (directory structure). CMS further hoping to standardise file format on json — does this serve all purposes?
    * Code for access & application may need to serve wider range of analysis codes (row vs columnar)
* Analysis/metadata association
    * Important for analysis preservation. Generally solved for central production: datasets have identifiable tags.
    * ATLAS is putting more of this into Glance

### Detector Simulation

- Convenors' meeting earlier this week, a few topics and cross-group areas discussed
    - Simulation for liquid noble gas detectors (covering both neutrino and dark matter experiments)
    - Use of FLUKA/MARS by experiments
    - Geometry: e.g. developments/experiences with DD4hep, VecGeom
    - Dealing with pile-up (possible cross-link with Frameworks, Reconstruction?)
    - Computational challenges in future detectors (e.g. muon colliders)
    - Use of GPUs and similar accelerators
    - Developments in ML for simulation
- Will keep in touch with Geant4 Task Force for R&D to avoid duplication and identify possible joint meetings
- Further ideas and input very welcome, especially for cross-WG items, e.g.
    - Use of Python with/for Simulation?
    - Training: link up with Geant4 material/courses?

### Reconstruction and Software Triggers

#### Summary of Hand-off meeting
- Hand-off meeting organized this week. Thanks to all that attended and contributed. That discussion identified a number of areas of common interest:
    - ML for and its integration into production code
    - Alignment / calibration - points of collaboration on "sharp knife" tools
    - Particle flow
    - Event data formats and geometry (overlaps with other groups)
    - Use of heterogeneous architectures
    - Closer link to training to establish training on trigger/reco methods/demonstrators
    - Integration into turn-key demonstrator projects 
- Next steps: Organize discussions/survey with experiment trigger/reco/computing project leads on plans/synergies (includes beyond LHC)


#### More details... Brainstorming on Topical Meetings

- Particle flow
    - was initially planned in last term but did not materialize
- Event Data formats & Geometry
    - great possibility to have an overlap session with simulation
- Machine learning frameworks for performant inference engines in real-time supporting various hardware backends (possible links to fastML, clariphy, ...)
- Machine learning algorithms for reconstruction and its integration
    - make the step from conceptual studies to production code integration
- Alignment and calibration? 
    - check whether collaboration is possible on "sharp knife" tools
- In general rather topics related to HL-LHC and off-LHC experiments
    - Run 3 R&D is basically closed
- Reconstruction on heterogeneous architectures
    - establish small scale demonstrators outside the experiments' structure
    - investigate inclusion of common HEP reconstruction & trigger packages into such systems

#### Possible formats:
- Establish closer link to training group, expanding from pure technical training
    -  e.g.: general introduction to HEP triggers and reconstruction and introduction to the methods used
    -  can training be done on little demonstrators:
        -  ALLEN demonstrator of mixing CPU/GPU algorithm
        -  Patatrack, ACTS etc. on OpenDataDetector
- Help integrating common packages into turn-key demonstrator projects
    - natural connection: CERN EP-R&D turn-key project
- Short, one-day workshops on specific topic, with possible overlap between HSF working groups:
    - trigger/reconstruction & simulation (fast MC initiatives, EDM/Geometry)
    - trigger/reconstruction & analysis (no clear boundaries)

#### Next steps:
- Talk to trigger & reco conveners of experiments
    - last survey is ~1.5 years old 
- Talk to computing projects of experiments
- Make sure to include non-LHC experiments 


### PyHEP
- **PyHEP 2021 workshop:**
    - Date to be decided. Likely just after SciPy 2021, which takes place as a virtual event on July 12-18.
- **Topical meetings:**
    - Reminder that we will do a kind of "Python module of the month", by default the first Wednesday of each month at 16h CET.
    - Topics so far confirmed are, see [Indico](https://indico.cern.ch/category/11412/):
        - Feb 3rd: Numba, by Jim Pivarski.
        - March 3rd: JAX, by Hans Dembinski.
        - April 7th: pyhf, by Giordon, Lukas and Matthew.
    - We welcome suggestions of topics very much. Advance thanks.


### Software Tools and Packaging

We kicked off this year's meetings w/ a fruitful discussion on `perf` yesterday:
* Presenter: Dr Guilherme Amadio (CERN)
* Agenda: <https://indico.cern.ch/event/974382/>

We agreed to continue the discussion in an upcoming meeting:
* Tentative time: February 17th (Wednesday) 5pm CERN time
* Agenda: <https://indico.cern.ch/event/999543/>
  * This time with an Indico integrated Zoom room :smile: 
* Please let us know if this clashes w/ an important meeting etc.

We're going to have a conveners' meeting, most likely first week of February, to iron out plans for this year. Please let us know if you have any topics/subjects you'd like to see us cover...
  * Already had an initial chat w/ the incoming conveners and the outgoing ones where we discussed the direction we want to take in 2021
  * There are a few topics to focus on/be discussed:
      * Spack on the packaging side
      * Static analyzers, profilers, IDEs on the tools side


### Software Training
Plans for 2021:
* Beef out the HSF curriculum <https://hepsoftwarefoundation.org/training/curriculum.html>
* Nail down how to measure success (surveys?)
* Encourage more people to integrate into the HSF Training community
* Strengthen friendship with Software Carpentries
* Collaborate with other HSF working groups to hold trainings
* Emphasise the interplay between training and careers

Hackathon follow up Friday 22nd January 17:00 CERN time <https://indico.cern.ch/event/997485/>


### Event generators

__Thoughts from 2020:__

- We only held 2 WG meetings in 2020 - will try for more this year.
- But…
   - We also had a dedicated generators session at the HSF/WLCG WS which was well attended and well received.
   - We submitted the paper on HL-LHC challenges for Event Generation.

__Plans for 2021:__

Complete the paper at last! (should be ready in ~few weeks)

Arrange meetings to discuss work done by others as in the plans laid out in detail in the paper, many areas of work:

1. Understanding of the current CPU costs by accounting and profiling. 
   - There has been separate work on e.g. profiling MG5_aMC and Sherpa which actually show some common conclusions
      - Time to bring this together and compare more apples-to-apples
   - Look ahead to NNLO codes?

2. Moving to GPUs/accelerators. 
   - Continue effort on the MG5_aMC GPU port
   - Try to follow-up better on similar activities for other generators (e.g. Sherpa and Pythia8)

3. Optimisation of phase space sampling and integration algorithms, including the use of ML 
   - This is somewhere we have not yet made large inroads - it will become a larger focus.
      - Topical meeting for the WG.

4. Reducing the cost associated with negative weight events 
   - Quite some discussions on this already in the WG
     - In particular at the November WS
   - Next steps…?
     - Trying to get existing tools more integrated into generator/experiment/ workflows

5. Promote collaboration, training, funding and career opportunities in the generator area:

   *Collaboration*
   - Build contacts with relevant projects:
      - E.g. Excalibur/SWIFT-HEP (UK) and HEP-CCE (US)
      - Offer a forum for communication between the two groups and help avoid overlaps?
   - Engage more with the Experiments?
       - There is work that has already been done but doesn’t always make it into the experiment workflows
   - Engage more with Nuclear people? Use contacts established via S&C Roundtable
   - Neutrino community - Liz has some contacts

   *Career opportunities and funding*
   - Not sure exactly what the WG can do here currently other than raise the visibility of the work through e.g. the paper and presentation at LHCC...

   *Training*
   - So far we have not been active in providing training
       - Should discuss this with HSF Training folks!
    - Need to think what that would look like…
      - E.g. would generator-specific code training be possible/make sense?
      - If not, do we need more “generic” training on e.g. programming for GPUs, profiling etc.?
         - This might be more the right emphasis from HSF.


### Frameworks

- We have not yet met in the new year.  We will likely be focusing on accelerator-offloading.  We are expecting a request from DUNE to present their framework needs.

---

## AOB

### IRIS-HEP Feedback

We have been asked to give another round of feedback to IRIS-HEP at their next steering board meeting on 16 February. Can you think about feedback (the good, the bad, the ugly) to send via Graeme?

For reference, the feedback given last year is here: <https://indico.cern.ch/event/809181/>.

### Website

A few recent updates:

- Disabled the very unreliable link checker
    - So many false positives that it was practically useless
    - Will fully disable Travis CI and move to Github Actions
- [New link checker](https://github.com/gaurav-nelson/github-action-markdown-link-check) under consideration
    - Javascript based
    - Much more flexible JSON configuration
    - Can be set to only check changed pages in the PR
- Added an HSF Documents page
    - <https://hepsoftwarefoundation.org/organization/documents.html>
    - Please check that nothing has been missed
    - Separate from Technical Notes (which are just cross linked)

### Next Meeting(s)

- Next meeting will be 4 February
