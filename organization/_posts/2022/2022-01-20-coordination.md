---
title: "HSF Coordination Meeting #221, 20 January 2022"
layout: plain_toc
---

# Attending

Present/Contributing:
Alaettin Serhan Mete,
Ale Di Girolamo,
Alexander Moreno,
Allison Hall,
Andrea Valassi,
Andreas Salzburger,
Ben Morgan,
Benedikt Hegner,
David DeMuth,
David Lange,
Dorothea vom Bruch,
Eduardo Rodrigues,
Efe Yazgan,
Gordon Watts,
Graeme Stewart,
Jim Pivarski,
Jin Huang,
Josh McFayden,
Kevin Pedro,
Krzysztof Genser,
Kyle Knoepfel,
Liz Sexton-Kennedy,
Marc Paterno,
Mark Neubauer,
Markus Diefenthaler,
Matti Kortelainen,
Michael Wilkinson,
Michel Jouvin,
Michel Villanueva,
Nicole Skidmore,
Oksana Shadura,
Paul Laycock,
Pere Mato,
Serhan Mete,
Stefan Roiser,
Stephan Hageboeck,
Sudhir Malik,
Torre Wenaus,
Valentin Volkl,
Wouter Deconinck

Apologies/Contributing: 


## News, general matters, announcements

**Happy New Year!**

### HSF Talks

#### Lepton-Photon

Graeme gave an overview [plenary talk](https://indico.cern.ch/event/949705/contributions/4575453/) about Software and Computing R&D in Lepton-Photon last week - thanks to all who make suggestions for improvements. Discussion focused on use of accelerators and HPCs (perenial topics of interest!).

## Working Group Updates

### General

A big welcome to all of our incoming conveners for 2022 and many thanks to all of our continuing conveners.

Many thanks to TJ Khoo (Analysis); Chris Jones and Attila Krasznahorkay (Frameworks); Andrea Valassi (Generators); Ben Krikler (PyHEP); David Lange (Reconstruction); Mircho Rozodov (Developer Tools); and Meirin Oan Evans (Training) for their work in 2021 and, in many cases, for quite a number of years before that. It’s very much appreciated!

After this meeting outgoing conveners will be liberated from the mailing list, but we look forward to your continuing involvement in HSF and the WGs.

All WGs uploaded their plans to the [agenda](https://indico.cern.ch/event/1096580/), which gets discussed group by group:

### Data Analysis

Review:
- metadata in analysis
- analysis software in wider community
- analysis benchmarks
- workflow management tools

Preview:
- reach out better to analysis people
- another workflow management meeting
- systematic uncertainties in analysis
- workshop on analysis ecosystems

TODO - Post paper to arXiv! This paper was a really great idea to give a concrete outcome to the WG's activity. When appropriate other WGs should consider the same as the HSF brings a unique pan-experiment perspective.

### Detector Simulation

WG will be involved in organising the GPU R&D community meeting.

Geometry is also important for reconstruction, so this is a cross-over topic between the two WGs.


### Reconstruction and Software Triggers

Are there concrete plans in the training? Should start that discussion soon and try and identify the topics. Training is needed in how to convert reco algorithms, which is rather bold and broad.

There would be a link to the Conditions DB activity here as well.

### PyHEP

Suggestion to gather all of the didactic material presented through PyHEP in one place so that people could browse and pick from them (even without (re)formatting things!).
- Note that we have <https://github.com/hsf-training/PyHEP-resources> linked from the WG webpage and we could either add "tutorials" there and/or have a section in the WG webpage. To be thought about.

What about Julia? Should we organise activities still via PyHEP or separately. Probably keep it under the PyHEP umbrella for now, which is beneficial for gathering interest in this language in HEP.

### Software Tools and Packaging

Good idea to look at new C++ features, a la module of the month.

### Event Generators

Benjamin Morgan: use of julia for generators as in simulation could be a possible topic? 

Josh: for this to work you have to convince all generator authors... To make this work it would require convincing lots of people, the code base it already fragmented in Fortran, C++, Python. Idea is good but in practice it may be difficult. 

Jim Pivarski: Just a note: in some syntactical ways, Julia is a shorter jump from Fortran than C++ is. In other fields (non-HEP), Julia is replacing Fortran, so generators, which still have more affinity for Fortran, is not inconceivable.

Benjamin morgan: At least on the detector sim side, it’s not just use of Python/Julia for implementation, but also “good practices” for binding existing C/C++/Fortran libraries to these. That’s a slightly different scope, but can be a good bridge/intro. 

Liz: Any discussion of neutrino generators? 

Josh: it's on our radar.

Liz: Fermilab put a proposal to do generators for neutrinos. If succeeded, definitely I'd nominate someone to give a talk on that. 

### Frameworks

Similarity with the tools group re. new C++ features - could cover that in common to get a broader audience.


### Software Training

Please see the slides attached to the [agenda](https://indico.cern.ch/event/1096580/contributions/4613188/subcontributions/364054/attachments/2376265/4059425/TrainingWG_HSFcoordinationMeeting_20Jan2022.pdf)

HSF Groups expressed interest in trainig (hope didn't miss any)
* Reconstruction & SW Trigger
* Physics Generators
* Software  Packaging 
* PyHEP (explore overalaps)

PyHEP have also been interested into how to better use survey information, especially when multiple events have been held.


---

## AOB


### Workshops in 2022

#### Analysis Ecosystems

Analysis Ecosystems workshop in May still being sounded out. Unfortunately CPPM in Marseille was only possible week of 9-13 May, which is the ROOT Users Workshop, an impossible clash. 16-17 May is an IRIS-HEP review.

These constraints mean we are very likely restricted to two choices:

- 18-20 May
- 23-25 May

Michel is checking if IJCLab could host us.

*We need to start to plan this in earnest now - propose that we have a first organisers meeting next week (to be Doodled), Analysis WG and PyHEP clearly should be involved.*

#### Simulation on GPU

Would like to have a review/discussion of progress on simulation on GPUs (AdePT, Celeritas), also in May. Weeks beginning 2 May and 16 May are possible (Celeritas checking their diaries). This will be a virtual event, European afternoons.

### Google Summer of Code

HSF call for proposals sent beginning of the week. Deadline for project proposals is Feb 21.


### Proposed Activity Area in Analysis Ecosystems

We have a proposal:

"Dear HSF Coordination Team,
 
We hope that you are all doing well and staying healthy during this challenging time.
 
With the email, we put forward a proposal for a new HSF Activity Area on the topic of analysis facilities called the  “Analysis Facilities (AF) Forum.” Please see the google doc at
 
<https://docs.google.com/document/d/1UHlNmoGIG4nKp41yzZT19UN4Wwu7Nypf7pVdDorMdgc/edit?usp=sharing>
 
for a description of the activity, which would also serve as a draft version of the AF Forum web page to be added to
 
<https://hepsoftwarefoundation.org/what_are_activities.html>
 
if approved by HSF Coordination.
 
Diego Ciangottini (INFN, Perugia U, CMS)
Lukas Heinrich (TUM, ATLAS)
Nicole Skidmore (Manchester, LHCb)
 
(in CC) have kindly agreed to coordinate the AF Forum activity. We hope that this initiative to create a community platform to discuss analysis facilities is well received by the coordination team and we can proceed with next steps in planning as an HSF Activity.
 
best regards,
 Mark, Oksana, Alex, Diego, Lukas and Nicole
"

Notes/Elaboration:

- Given the length of today's agenda, probably best to take up the discussion on this proposal at the next meeting (3 Feb)
- IRIS-HEP plans to help the Forum get started by organizing a Blueprint Meeting with the AF Forum coordinators as a kickoff
- Chats with WLCG/DOMA team recognize that the activity would benefit from a liaison between the HSF AF Forum and the WLCG/DOMA
- Plan a HSF/WLCG community white paper on Analysis Facilities by the end of 2022 as a specific goal for the Forum activities 

### Calendar for 2022

Mostly complete, but as new things come up please add them!

### Next Meeting

Next coordination meeting is scheduled for 3 February.
