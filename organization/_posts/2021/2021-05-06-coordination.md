---
title: "HSF Coordination Meeting #207, 6 May 2021"
layout: plain_toc
---

Present:
Allison Hall,
Andreas Salzburger,
Ben Morgan,
Caterina Doglioni,
David Lange,
Eduardo Rodrigues,
Graeme Stewart,
Josh McFayden,
Kilian Lieret,
Krzysztof Genser,
Kyle Knoepfel,
Liz Sexton-Kennedy,
Mason Proffitt,
Meirin Oan Evans,
Michel Jouvin,
Michel Villanueva,
Paul Laycock,
Serhan Mete,
Stefan Roiser,
Sudhir Malik,
Teng Jian Khoo

Apologies: Andrea Valassi, Dorothea vom Bruch
  
## News, general matters, announcements

### HL-LHC Review Phase 2

We have had two mini-workshops that presented plans and ideas for the HL-LHC era from both experiments and projects (a *conversation*):

* Detector Simulation, Thursday 29 April <https://indico.cern.ch/event/1028379/>
* Analysis, Tuesday 4 May <https://indico.cern.ch/event/1028381/>

These were well attended and extremely useful.

The inputs and discussions will inform the documents that are being written. First drafts to be ready **30 June**, so that they can be discussed and get feedback over the summer.

### Google Summer of Code

GSoC administrators have requested slots for all proposals where they received a good proposal (~27).

### Proposal for DUNE Framework Requirements Review

Framework requirements review kick-off to be held next week (probably Mon. or Tues., time to be settled by the end of the week).  Review mini-workshop will be during the week of May 24th or May 31st.

## Working Group Updates

### Data Analysis

Second instance of "Wider HEP/NP analysis community" meetings yesterday. Agenda with recording & live notes [here](https://indico.cern.ch/event/1033484/).

* Excellent, interesting talks from FAIR/GSI, LZ, Xenon
* Highlights:
    * Sharing of basic SW framework and dynamic computing resource allocation at GSI
    * Effective Gitlab CI, common analysis SW in LZ
    * 100% python framework at Xenon
* Put together our own "talking points"
    * DUNE framework review -- generalisable?
    * How have (some, smaller?) experiments managed to converge on one analysis framework
    * Keen to revisit discussion on recognition (always a popular topic!)

Need to define an agenda for the next instance, currently scheduled for 19 May but perhaps we should postpone it to a week later to avoid vCHEP...

[Analysis metadata "constraints" rough draft](https://docs.google.com/document/d/1zT5tPCtiNfuRm8ywKNbaNGvXGtCZYaO-GOj77pV2BEY/edit#) written, to share with community for comments soon:

* Already solicited comments from Paul (thanks!)
* Feel free to add yours

### Detector Simulation

- Next meeting 10th May on simulation for solid state microphysics:
    - <https://indico.cern.ch/event/1016632/>
- Provisional next meeting 7th June on [pyg4ometry](http://www.pp.rhul.ac.uk/bdsim/pyg4ometry/) (see also <https://arxiv.org/abs/2010.01109>) package for geometry construction
    - Likely of interest to Reconstruction/Triggers and Python WGs? (literally set it up a couple of days ago, so not advertised yet!).
    - May also have an update on GDML parsers/support in Geant4/ROOT/VecGeom
- Preliminary topics for fall: MARS, varying Geant4 parameters

### Reconstruction and Software Triggers

* First topical meeting on timing reconstruction (LHC + Future Expt) has a lot of interest. Trying now to find a date.
* Open data detector + timing files are almost ready for release.


### PyHEP

- **Topical “meeting of the month” on the Dask package** held yesterday Wednesday, see <https://indico.cern.ch/event/1027094/> for the tutorial materials (recording soon to be uploaded to YouTube).
- **PyHEP 2021 workshop**:
  - Details on the [Indico agenda](https://indico.cern.ch/e/PyHEP2021).
  - Reminder - registration and abstracts submission are both open.
      - Seeing again a very high level of interest :-).


### Software Tools and Packaging

We had a WG meeting last Wednesday (Wednesday 28 April 2021, 5pm CERN time):
* **Agenda:** <https://indico.cern.ch/event/1026182/>
* **Topic:** Experience with Spack at Fermilab
* **Speaker:** Stephen White (Fermilab)
* Pretty good turn out with almost 80 people from various experiments/labs. Would be good to do a "post-mortem", converge on a few action items based on the discussions and follow-up from there.

### Software Training

- Modification in the web design of the [Training Curriculum](https://hepsoftwarefoundation.org/training/curriculum.html).
    - A more intuitive interface. Modules are shown in boxes instead of lists. 
    - Instead of "beginner, intermediate, advanced", the modules are now organized in collections such as "Basic", "Software dev", "Machine learning".
    - Easily maintained with YAML.
- A Hackathon follow-up was held on Apr 30 to discuss the status of the training modules towards the main Hackathon in June.
    - For the next time, meetings dedicated to each module can work better than a general call for a follow-up. 
    - We need to define a list of the high-priority modules to develop/improve. Based on the list, we will organize the meetings.
    - Some of the modules require input from experts in other WGs. We will ping the contact person when required.
        - As an example, for Singularity we are working in a [chapter](https://hsf-training.github.io/hsf-training-singularity-webpage/03-building-containers/index.html) that aims to deploy Pythia8 in a container.
- Discussing when the next round of HSF training events must be held.
    - Candidates: 
      + Summer, when people are usually with more time available.
      + Sep-Oct, when new PhD students take place.
- Improve contact between training WG and other WGs
    - Nominate a training contact for each WG - *WGs please follow-up on this*

### Event Generators

- Started series of meetings to gather feedback for LHCC Review 2:
    - Had a very productive meeting with Sherpa authors on 22nd April
        - They showed a number of CPU improvements recently implemented and/or in the pipeline
        - We discussed some very interesting "bigger picture" ideas such as creating a "global" modular plug-and-play generator interface 
    - We have an HSF Generators WG meeting this afternoon:
        - LHCC Review 2 input from EvtGen (Photos also invited to contribute).
        - Update on MadGraph5_aMC@NLO migration to GPUs
    - The next meeting will probably be on May 20th (Pythia)
    - Then one on May 27th and others from early June (Powheg, Madgraph, Herwig to be scheduled precisely).
        - Has been a bit hard in places to pin people down!


### Frameworks

Monthly informal "coffee" delayed one week until May 12.

---

## AOB

### CAF and Roundtable

* Roundtable meeting was this week on User-centred Design: <https://indico.jlab.org/event/420/#day-2021-05-04>
* Compute accelerator forum meeting next week (Wed 12) on Alpaka: <https://indico.cern.ch/event/975010/>

### Webpage

- Cannot properly deploy to github pages from a fork of the repository (links won't properly resolve)?
    - This seems to be related to the usage of absolute links (e.g. `/css/hsf.css`) without using `{{site.baseurl}}` (which only works if everything is directly relative to the domain, as with the official deployment to `hepsoftwarefoundation.org`, as `/` resolves to that)
- Some PR with design tweaks:
    * Slightly increase overall font size:
        * <https://github.com/HSF/hsf.github.io/pull/964>
    * Add some icons to Nav bar
        * <https://github.com/HSF/hsf.github.io/pull/965>
    * Boxes with "big" links to make the important things stick out
        * <https://github.com/HSF/hsf.github.io/pull/968>

### Next Meeting(s)

- Next meeting will be 27 May (after Ascension and vCHEP)
