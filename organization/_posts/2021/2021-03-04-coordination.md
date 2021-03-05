---
title: "HSF Weekly Meeting #203, 4 March 2021"
layout: plain_toc
---

Present: Graeme Stewart, Caterina Doglioni, Kyle Knoepfel, Andrei Gheata, Pere Mato, Allie Hall, Krzysztof Genser, Michel Jouvin, Efe Yazgan, Ben Morgan, Serhan Mete, Stefan Roiser, Kevin Pedro, Sudhir Malik, Meirin Evans, Michel Villanueva, Liz Sexton-Kennedy, Andi Salzburger, Dorothea vom Bruch, Eduardo Rodrigues, Josh McFayden, Marc Paterno, Paul Laycock, Daniel Elvira, Benedikt Hegner, Philippe Canal, Antoine Pérus

Apologies: Andrea Valassi
  
## News, general matters, announcements

### LHCC

The [software presentation](https://indico.cern.ch/event/1000087/attachments/2201584/3723818/Software%20Update%20and%20Review%20Preparation%202021-03%281%29.pdf) to the LHCC covered 2 topics:

- Software highlights from SFT and HSF
- Progress on planning for the second phase of the HL-LHC review, focussing on common software projects
  - For the review mandate, [see Indico](https://indico.cern.ch/event/1000087/attachments/2201584/3712348/HL-LHC-CommonSoftware-v4.pdf)
- *Thanks to everyone who gave input*

#### Feedback on general software matters

- Plans of work got very positive feedback
- 5-7% Geant4 speed extremely welcome
- ROOT effort shortages in several areas was presented to the committee and highlighted as a concern
- C++ course highlighted as a big need that we're helping to fill
- Positive note taken of the CAF and Roundtable meeting series

#### HL-LHC Review Phase 2

Plans have been made together with WLCG PL and the experiment computing coordinators. We have settled on presenting 6 documents (each one to be 20-30 pages). Projects have been selected on the basis of the challenges presented by HL-LHC, of event complexity, trigger rates, etc.

*Introduction* - overview of inputs and process, place to highlight experiment differences, mention of important software that was not reviewed (e.g., no worries for scaling, effort, sustainability, etc.)

*Event Generators* - want to cover the more important NLO generators (Sherpa, MadGraph, POWHEG) as well as other important pieces (Pythia, EvtGen). Editors to include HSF WG.

*Detector Simulation* - Lion's share of input from Geant4, so we have them as key editors. Also will cover GPU R&D projects (Celeritas, AdePT) and underlying tools like DD4hep and VecGeom.

*Foundational Tools* - Mostly core pieces of ROOT, such as I/O system, geometry and event display, JSROOT, PyROOT, Maths. ROOT project will edit this.

*Analysis* - To cover the ROOT project (more "analysis facing" components, such as RooFit, Histograms, RDataFrame) - handled by ROOT team. Also cover newer Pythonic Tools, Scikit-HEP project (pyhf, uproot, etc.), Coffea project, zfit fitting package; editors from SciKit HEP, HSF PyHEP and Analysis WG, IRIS-HEP.

*DOMA* - Rucio, File Transfer Service (FTS), Storage interfaces and caching layers (CTA, dCache, Xcache, StoRM, xrootd, http TPC, etc.), Network technologies including monitoring and software defined networks, CVMFS, Token based authentication. Liz and Graeme made a presentation at the last DOMA general meeting (<https://indico.cern.ch/event/1009737/>). We will assemble an editorial team.

Feedback/discussion from LHCC and review chair:

- Generally they are happy with the plan
  - "The LHCC thanks the WLCG PI, WLCG SW liaisons, the experiments and the HSF for their efforts to come up with a sensible list of Common Software Activities. We understand the schedule is tight and we appreciate your help to make this review a success."
  - Amber praised the clear selection of projects and the fact that our documents will be useful beyond the review
- We did discuss some specific projects/issues
  - Accelerators? Yes, but on a per-project basis, rather than generally
  - Build systems? Probably not, as the scaling for HL-LHC is not a big problem (albeit, likely to need optimised builds)
    - Meeting discussed this and we shall raise this again with the WLCG/Experiments; could foresee to have it in the foundation document
  - ACTS? To be reviewed later, in the ATLAS context as other LHC experiments not using it
    - Noted that as this is an LHCC review the non-LHC use of ACTS, while very welcome, is not in scope

### HSF Plans

As mentioned above... the summary of our plans for 2021 are here: <https://hepsoftwarefoundation.org/organization/planning/plan-of-work-2021.html>.

Please help circulate it to other communities.

### Google Summer of Code, Season of Docs

- Applied as CERN-HSF Organization, accepted orgs announced Mar 9
  - 37 project proposals (vs. 47 last year)
  - Students will contact mentors from **Mar 9** (>400 registered in the Gitter chat channel!)
  - First phase evaluation mandatory based on a test, **Mar 25** is the limit date for mentors to announce the results.
  - Extensive interaction mentor-student for the students passing the test
  - *Clarification:* not necessary to put the test on the webpage, it can be communicated directly to students
- Season of Docs 2021 call for mentors and project proposals already issued
  - Proposals accepted until **Mar 25** (on Mar 26 we need to apply as Org)
  - We had 4 projects in 2020 (2 short-term, 2 long-running) on [Rucio](https://www.divya-mohan.com/project-report-gsod), [Allpix Squared](https://github.com/sabitarao/gsod/wiki), ROOT (being evaluated) 
    - Techical writer [blogs](https://hepsoftwarefoundation.org/gsdocs/2020/blogs.html) available
  - The web page 2021 still being prepared. Folders in the repo for 2021 not there yet, but people can [contact us](mailto:hsf-gsdocs-admin@googlegroups.com) in case they plan to make a proposal.

### Data Analysis Working Group Convenors

Chris Burr (LHCb, CERN) has unfortunately had to step down as a convenor of DAWG. We are however delighted to announce that Nicole Skidmore (LHCb, U Manchester) has agreed to take this role.

### C++ Course

Next iteration, tentatively 30 August - 3 Sept. Pivot the material a bit to concentrate more on the on basics and to have more exercises.

## Working Group Updates

### Data Analysis

- Working on metadata writeup to close out that discussion. Let us know if you want to help!
- Now that Nicole has joined, we will start planning our next events.

### Detector Simulation

- Next meeting: Monday, March 8, on NEST (noble liquid simulation for dark matter, neutrino experiments)
  - May 10: Simulating solid-state microphysics with Geant4 and G4CMP (Mike Kelsey)
  - Considering subsequent meetings on other related topics
- GPU usage:
  - advertise next accelerator forum (March 10)
  - possible meeting (April or end March) on Celeritas, Opticks integration w/ Geant4
- ML for simulation: considering a few topical meetings
  - Run 3 deployment plans and experiences (ATLAS, LHCb)
  - Mathematical improvements in NN architectures: reweighting GANs, normalizing flows, ...
  - Usage beyond LHC experiments (if any)

### Reconstruction and Software Triggers

- Feedback form to plan future events sent out (<https://forms.gle/sTM1cyERyKVZPFbE6>), to be filled out by March 12th
- Kick-off meeting will take place on March 17th at 5 pm

### PyHEP

- 2nd topical meeting, on automatic differentiation with JAX, took place yesterday (<https://indico.cern.ch/event/985423/>).
  - Good attendance with almost 40 participants.

### Software Tools and Packaging

- Had a nice meeting last week on European Environment for Scientific Software Installations (EESSI):
  - Speaker: Bob Dröge (University of Groningen) 
  - Agenda: <https://indico.cern.ch/event/1005954/>
  - Graeme: Although they use Easibuild and we use LCGCMake/Spack, there are still many pieces in common (e.g., we could look at using `lmod` to setup releases)
- Material from [GA's talk](https://indico.cern.ch/event/999543/) on performance monitoring should be made more widely available, a great resource:
  - <https://indico.cern.ch/event/974382/contributions/4102981/attachments/2174921/3672328/linux-systems-performance.pdf>

### Software Training

- Quick presentation summarising recent GitHub CI/CD training <https://docs.google.com/presentation/d/12sS7p5E1skOAATztGk5C3NjK0FNCFV9VbWTVxX1UtME/edit?usp=sharing>

### Event Generators

- HL-LHC Review 2: Have been discussing the proposal from Liz and Graeme and have decided it would be good to dedicate some upcoming WG meetings to discuss the important topics - expecting to send announcement to the WG tomorrow.
- ATLAS and CMS GEN accounting: Have updates coming soon.
- CSBS Paper: Now accepted!

### Frameworks

- We had our first free-form meeting yesterday.  It was lightly attended, but we had good discussion regarding TBB UI deprecations, other multithreading issues, and how data-quality monitoring integrates with experiment frameworks.
- Re-brand as 'Frameworks Coffee'?

---

## AOB

### November Workshop Survey and Outcomes

See slides attached to the agenda, which give highlights of the survey from the workshop.

In the interests of time we decided to delay presenting these until a future meeting.

### IRIS-HEP Feedback

Graeme presented feedback to IRIS-HEP in their last steering board meeting (<https://indico.cern.ch/event/894517/>).

- Thanked for this input (so thanks to all HSF people for material)
- We identified a few issues to follow up on:
  - Training matters, such as re-engagement with The Carpentries
  - Willingness to organise join mini-workshops on topics of mutual interest

### Next Meeting(s)

- Next meeting will be 18 March
