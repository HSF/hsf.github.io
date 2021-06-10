---
title: "HSF Coordination Meeting #209, 10 June 2021"
layout: plain_toc
---

Present:
Ben Morgan,
Benedikt Hegner,
Caterina Doglioni,
Daniel Elvira,
Dorothea vom Bruch,
Eduardo Rodrigues,
Elizabeth Sexton-Kennedy,
Graeme Stewart,
Guilherme Amadio,
Josh McFayden,
Krzyszof Genser,
Kyle Knoepfel,
Mark Neubauer,
Meirin Oan Evans,
Michel Jouvin,
Paul Laycock,
Pere Mato,
Serhan Mete,
Stefan Roiser,
Sudhir Malik,
Teng Jian Khoo

Apologies: Andrea Valassi
  
## News, general matters, announcements

### LHCC Meeting

Meeting with the LHCC referees was last week. Liz presented the software report, which is [attached](https://indico.cern.ch/event/1043620/attachments/2253400/3829547/Software%20Update%20and%20Review%20Preparation%202021-06.pdf) to this week's agenda. Thanks to everyone for inputs.

Notable points raised in the meeting and in the referees' feedback:

- General delays in procurement (global shortages) are causing a little concern for Run 3 provisioning
- ROOT team were praised for their work in helping [STEM students with disabilities](https://home.cern/news/news/cern/cern-opportunities-stem-students-disabilities)
- There was a discussion about porting to Power (which CMS have done, to run on the Marconi 100 at CINECA). This has also been discussed in the Librarians and Integration Meeting (LIM) for the LCG stack. No technical issues foreseen (definitely no ROOT problems when little-endian), but will need access to machines at CERN and some effort to setup and monitor the builds.
    - News from openlab, they will upgrade their Power cluster from Power8 to Power9
- Referees asked about how AdePT was integrated into the rest of the simulation stack, so we explained the "plugin" approach being adopted, with Geant4 running the main CPU simulation and calling out to AdePT when a particle enters the calorimeter and then AdePT passing back the hits from the shower
- [Added post-facto for completeness:] *The referees encouraged us to check against the plans of work we laid out at the beginning of the year*

### HL-LHC Review Phase 2

We also discussed the review with the referees. They are pleased with progress towards draft documents by 30 June.

*Reminder - draft documents due at the end of June!*

### DUNE Framework Requirements Review

We had the [mini-workshop](https://indico.cern.ch/event/1038551/) last week (2-3 June).  There were roughly 20 participants who discussed:

- Charge of the review
- Technology available from current frameworks
- Many aspects related to their stated requirements

The aim is for the review panel to provide a document (by the end of the month) that DUNE can use to guide its framework selection/development.

Many thanks to the panelists for their hard work and to DUNE for their willingness to ask for input from HSF.

Very open and useful discussion, that also give a good overview of the frameworks in other experiments on Day 1 - summary of the 'state of the art'.

### HSF Domain Name

Currently the HSF's domain name (`hepsoftwarefoundation.org`) is managed via Torre's AWS account (and special thanks to him for saving the name over the Labour Day Weekend!). This isn't ideal (small cost, bus factor). We have asked CERN IT how they can take this over, although in fact any of the major labs could take this on, assuming the small costs can be covered.

Liz: Fermilab could help if this proves to be difficult to do at CERN.

## Working Group Updates

### Data Analysis

- "Constraints on future (analysis!) metadata systems" [document](https://docs.google.com/document/d/1zT5tPCtiNfuRm8ywKNbaNGvXGtCZYaO-GOj77pV2BEY/edit#) circulated for comments
    - Received a ton (many confirmed useful, not all reviewed yet)! Accepting comments until next week (Jun 15), will then follow up with anybody who has commented.
    - Plan to publish on Zenodo subsequently, then arrange some input on possible solutions
- Took a bit longer to finalise [next meeting agenda](https://indico.cern.ch/event/1037201/), hence pushed back to 16 June.
    - Training overview
    - SuperNEMO
    - Belle II
    - EIC
- Subsequent meetings -- BES III in the pipeline
    - Polled attendees on whether they are interested in LHC overviews now that we've heard from the much wider community -- LHCb was top pick (admittedly small sample size due to poll needing fix+recirculation)

### Detector Simulation

- Meeting earlier this week on [PyG4ometry and GDML](https://indico.cern.ch/event/1038196/)
    - Interesting topics and good discussion
- Now planning future meetings for September, so suggestions welcome especially cross-WG 

### Reconstruction and Software Triggers

- The next topical meeting will take place on Wednesday June 30th at 5 pm. This will be the first of two events covering 4D reconstruction with timing, covering future detectors and colliders. 
    - <https://indico.cern.ch/event/1048211/>
- The second meeting will be scheduled from September on, covering more the algorithmic side.

### PyHEP

- **PyHEP topical meeting** on "Giving a good Jupyter talk" took place last Wednesday June 2nd ([Indico agenda](https://indico.cern.ch/event/1044648/))
    - Next topical meeting not before September since next month is PyHEP 2021 and we want to have a proper Summer break.
- **PyHEP 2021 workshop** preparations well under way
    - Grand plan on session contents to be discussed tomorrow in our organisation meeting.
        - All personal invitations done by now.
    - Deadline for abstract submission was yesterday.
        - We got more abstracts than last year!


### Software Tools and Packaging

- We're going to have a conveners meeting on Wednesday Jun 23rd to discuss future plans.

### Software Training

Advertise two workshops and C++ training:

####  HEP Software Training Challenge

- Date: Monday 28 June 2021
- Time: 4:00 PM-6:30 PM CERN time
- Indico: <https://indico.cern.ch/event/1044523/>
- Goal: In this workshop we propose to build on and expand the software training effort in the coming 3 years by defining a clear target in the form of the “Training Challenge”.

#### HSF Training Hackathon on C++

- Date: Monday 5 July 2021 
- Time: 4:00PM -6:30 PM CERN time
- Indico: <https://indico.cern.ch/event/1044512/>
- Goal: This would focus on revisiting highly successful and sought after  C++ training, lessons learnt, progress made, modifications needed and feedback to constantly improve it.

Q. Where is this advertised? Via the Google Group. We suggest a mail to the `hsf-forum` for these two special meetings, as well as reaching out to people who participated before, as trainers or students.

#### HEP C++ Course

- Preparing for 3rd iteration of the event. Plan to hold the course **30 Aug - 3 Sept** <https://indico.cern.ch/event/1019089/>
- Registration for 75 places will open **Monday 28 June, 9 am CEST**. (if you are interested please be there on time, last course was "sold out" in a bit more than 2 minutes)
- Currently we are working on adapting content and new exercises.
- **IMPORTANT**: We are **looking for mentors** for the hands-on tutorials. A mentor would usually attend 2 hands-on trainings (2 hours each) during the week and guide 5 - 10 students through already prepared exercises. Please contact the [organizers](mailto:hep-cpp-course-organizers@cern.ch). 

### Event Generators

- Many HSF generator WG meetings in the pipeline, <https://indico.cern.ch/category/8460>. Had three in May (EvtGen, Pythia, Madgraph). Planning two more in June (Herwig, Powheg, Lhapdf). 
- Will then be busy preparing the document for the LHCC review of HL-LHC.
    - Graeme: document on 30 June can still be 'living', and get a few last pieces added post-facto.
    - We need to make sure that the document (all of them) are preserved - use the HSF Zenodo community

### Frameworks

- Focus has been on the DUNE framework requirements review.  Will get back to the "regularly scheduled program" after review activities complete.

---

## AOB

### CAF and Roundtable

#### CA Forum

9 June, 2 very good talks on "JUWELS Booster, Europe's fastest HPC" and "Event interpretation in Belle2". Attendance lower than usual - several other meetings apparently clashed this time. 

Indico category at <https://indico.cern.ch/category/12741/>

Next CA Fora (always Wed 16:30 CEST):

- 7 July, Usage of FPGAs for pixel detector readout and processing (PSI + IBM)
- 8 Sept, Kokkos abstraction layer

More topics in the pipeline but please do contact any of the [CA Forum organisers](mailto:compute-accelerator-forum-organizers@cern.ch) if you have proposals. 

Q. Who has been looking at Kokkos? A. At least for the Madgraph GPU port, Taylor Childers has been looking at using Kokkos. ATLAS, CMS, and DUNE have also been exploring Kokkos through the HEP-CCE program (specifically the portability activities) funded by the DOE. There was also work on WireCell, reported at vCHEP.

### Recording Meetings

After our discussion on if HSF meetings should be recorded, the summary recommendation has been [added to the website](https://hepsoftwarefoundation.org/what_are_WGs.html) [(PR)](https://github.com/HSF/hsf.github.io/commit/839cc3e32292663ca0e34e48ede3d4ef55e66e41).

Who has the copyright on recordings like this? We are not sure, something to think about.

### vCHEP

If there was anything at vCHEP that you think the HSF should be tracking, please let us know (email to coordination, or WG, or raise it in a meeting).

### Next Meeting(s)

Our next meeting will be 24 June.
