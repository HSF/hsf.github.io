---
title: "HSF Weekly Meeting #177, 16 January, 2020"
layout: meetings
---

# {{page.title}}

Present/Contributors: Graeme Stewart, Eduardo Rodrigues, Benedikt Hegner, Efe Yazgan, Serhan Mete, Pere Mato, Daniel Elvira, Liz Sexton-Kennedy, Andrei Gheata, Witek Pokorski, Agnieszka Dziurda, Caterina Doglioni, Attila Krasznahorkay, Andrea Valassi, Torre Wenaus, Paul Laycock, Ben Morgan, Danilo Piparo, Gloria Corti, Stefan Roiser, Teng Jian Khoo, Andrea Rizzi, Akanksha, Concezio Bozzi, David Lange, Jim Pivarski, Philippe Canal, Chris Jones, Martin Ritter

Apologies: Eduardo Rodrigues

## News, general matters

- Pre-Christmas Virtual Meeting
    - Please check the [minutes](https://hepsoftwarefoundation.org/organization/2019/12/19/coordination.html)

- Working Group Convenors
    - Data Analysis Working Group: The final working group convenor for 2020 is TJ Khoo (ATLAS), who will join Paul and Andrea. Welcome to him and many thanks to Danilo Piparo for his work as outgoing convener.

- LHCC Review of HL-LHC Software and Computing
    - LHCC will review software and computing plans for the HL-LHC, Amber Boehnlein (JLab) will chair
    - The first phase will be 18-20 May 2020
    - There will be five 20 page documents provided as input to the committee, from ATLAS, CMS, WLCG, DOMA and from Common Tools and Community Software
        - These have to be ready by 1 May (*before* Lund workshop)
        - This is extremely close!
    - HSF is in charge of the *Common Tools and Community Software* document
    - Should cover software directly impacting on resources, viz.
        - Event Generation
        - Detector Simulation
        - Reconstruction
        - Data Analysis
    - These map nicely to our four working groups in these areas, so the suggestion is that each group takes charge of ~4 pages of text
        - Starting point should be the CWP
        - R&D plans should be outlined
        - Important question is how to get community input and reasonable consensus
        - Outline plan was discussed:
            - 4 pages by March
            - March for feedback and meetings
            - April to finalise
        - Graeme can do a skeleton...
            - Start in Google Doc, convert to LaTeX for the final version
        - We can speak about useful things not yet being done, i.e. gaps (LHCC could then flag this up and that might help)
    - Follow-up review, with more focus on community software anticipated for Autumn 2021
        - By that time plans should be better defined...

## Google Summer of Code 2020

The 2020 season of GSoC has started, and a [call for HSF mentors and project proposals](https://groups.google.com/d/msg/hsf-forum/Mhcog0Kogrw/LnQTizz3DQAJ) has been made recently. The deadline for submitting proposals is **Feb 4**!

- The HSF GSoC [page](https://hepsoftwarefoundation.org/activities/gsoc.html) has been updated, detailed [instructions](https://hepsoftwarefoundation.org/gsoc/guideline.html) for how to contribute are available, including the HSF GSoC 2020 mentor [guidelines](https://docs.google.com/document/d/110NS7iRonBUKa05pny-YaOS8mXpBYjs6DG302SeWbOI/edit)
- Some more info about GSoC 2020 is available in this [presentation](https://docs.google.com/presentation/d/1_FIzNoAKLlNMuRsLIMoHhN7EW6_QoUfYaVylwE9pcSQ/edit#slide=id.p)
- In 2019 we had 34 slots assigned by Google, out of which we managed to fill in 33, so almost all proposals having a good student candidate got a slot. Out of those, 29 successfully completed the program.
- We have distributed the call to the HSF channels, but spreading the word with contacts would help getting more proposals and eventually approved slots.

## Working Group Updates

### Data Analysis
- Welcome to TJ !!
- Kick-off [meeting planned for the 24th January](https://indico.cern.ch/event/880410/)
    - Summary of the preCHEP workshop on "Analysis Systems"
    - Organization of future activities
        - Analysis languages
        - DOMA and Analysis
    - Roundtable for other ideas

### Detector Simulation
- Welcome to Philippe
- Organising meeting soon
- Will prepare for LHCC inputs


### Reconstruction and Software Triggers
- convenors meeting late in December 
- our 2020 target: one meeting per month 
- 22nd January: follow up CPU data structures and algorithms 
    - ATLAS speaker confirmed 
    - Still didn't converge on CMS speaker
    - Meeting not announced yet (might be short notice)
- 12th February: tracking improvements for Run4(-5) 
    - talk based on ATL-PHYS-PUB-2019-041 (confirmed)
    - possible one more contribution from CMS or LHCb or heavy ions (to be seen)
- March goal: GPU with focus on algorithms discussion
- April: Conneting the dots (not sure we can be competitive with it)
- May: Lund 


### Software Tools and Packaging
- TAU follow-up meeting this Monday:
    - Details : On 20/01 at 2pm-4pm CERN time in room 304/1-007 
    - Agenda : <https://indico.cern.ch/event/876921/>
    - Plan : Sameer Shende (U. of Oregon) will be at CERN in person. Planning to have a talk followed by an interactive session. Please join if possible.
    - Can people prepare some examples in advance?
        - Contact conveners if you do
- Planning to have a conveners meeting on 24/01 to discuss the plans for this year.
- Categories merged on Indico and renamed as *Software Tools and Packaging WG*: <https://indico.cern.ch/category/7975/>


### PyHEP

- The 3rd workshop, PyHEP 2020, will be held on July 11-13 in Austin, Texas, U.S.A.
    - An announcement will be sent out soon via the usual channels.
    - Do mark the date down already!
- PyHEP 2020 will "tag along" with [SciPy 2020](https://www.scipy2020.scipy.org/) held on July 6-12, also in Austin.
    - Great opportunity to engage with the SciPy community!
    - We encourage HEP colleagues to submit abstracts to SciPy and let us WG conveners know about it, so that we curate a list of submissions. Note that the submission deadline is Feb. 11.

### Training

- Training meetings happening regularly (Mondays 15h30)
- Upcoming events
    - [Analysis Preservation](https://indico.cern.ch/event/854880/) 17-19 February
    - Software Carpentry (v2.0) 24-27 March

### Event generators

- Welcome to Efe, many thanks to Stefan, Steve and Taylor!
- Convenors met this morning to plan the restart of activities
- We will have a meeting next week, to be announced later today or tomorrow. Tentative agenda on <https://indico.cern.ch/event/880274>:
    - information about Lund workshop and HL-LHC review
    - update on ATLAS/CMS accounting
    - (TBC) update on Madgraph on GPU
    - discussion of GSoC

### Frameworks

- Last meeting before Christmas was about the status of the FAIR/ALICE framework (<https://indico.cern.ch/event/871485/>)
- Next meeting planned for 29th January
    - No agenda yet, still trying to make it up...
    - Would prefer to get input from Belle II and the JLab experiments, but we'll see...
- After that we will finally really turn to specific topics around the software frameworks

## Interest and Activity Areas

### Event Delivery Forum

 - Torre: intelligent data delivery service (iDDS) prototype has been progressing well, all components implementing the full workflow now in place, expectation is that the first functional prototype with full workflow + Rucio plugins for operation as part of the data carousel (the first use case target for ATLAS iDDS) will be ready by the end of the month.
 - establishing an iDDS R&D instance of PanDA at CERN with the help of WLCG DOMA folks in CERN IT
 - Very unfortunate news is that Gancho Dimitrov, an outstanding Oracle DBA and developer for many years in ATLAS and a major contributor to iDDS, has just left ATLAS. A big loss to ATLAS and CERN, best of luck in your next endeavours Gancho!

## Workshops

### HSF/WLCG 2020 workshop

#### Logistics

The workshop will start Monday after lunch and end Friday at lunchtime. For now no pre-workshop or splinter meeting is foreseen.

We hope to open registration rather soon now... start of February

<https://indico.cern.ch/event/867789/>

#### Scientific Programme

Organising team for HSF are: Graeme, Heather, David and Michel

##### Plenary
- Opening session on Monday afternoon and closing session on Friday will be in plenary
- For Monday we foresee some overview talks to set the scene
    - We have specifically reached out to some non-HEP communities, e.g. ESS, Dark Matter, Astroparticle, ESCAPE
    - Would it be a good time to give an HSF review talk, for new people to the software and computing area?
    - Would it be useful to have some cross-cutting technology items, e.g. compute accelerators or networking...

##### Parallel
- Tuesday, Wednesday and Thursday will probably (all) be parallel HSF
    - We could have 2 items ongoing (there are 3 rooms in total), but will need negotiations with our computing colleagues
- The DOMA/Analysis workshop pre-CHEP was a success, with the interactive sessions appreciated
- Should we try to do something along the same lines here?
- e.g. Reconstruction and Simulation are the other major resource impacting areas
    - This would mean dedicating a day to each of these
    - How best to get everyone involved in discussions and have useful outcomes?
        - New ideas
        - R&D
        - Shared projects
    - The large room is amenable to splitting into smaller groups
- If we do this then only one more day left
    - That means we cannot cover all topics!
- Ideas and thoughts for other WGs:
    - Generators is a centre of experise in Lund, can we take advantage of that and organise something significant, building on the Nov 2018 workshop
    - Software Tools and Packaging is an active group, with widespread impact, so a session makes sense
    - Frameworks is a new group, so a first session in the workshop will help bootstrap and define directions
    - Training - could have a session, but what would need discussed in this forum that would drive outcomes?
        - Sam M. : I'm sorry that I could not attend the meeting.  I *do* think that having a session would be good and I think that if we want to consider outcomes, then having the critical mass of people to brainstorm what types of bootcamps we need would be helpful. We can then discuss this with the experience of the last year in mind [specifically *how* we held the workshops] and that would provide the concrete list of events that we need to plan in the coming year - spanning ~July 2020 - July 2021.  
    - Analysis had a session in Adelaide and we felt the next event needed to be at CERN to get the coal-face analysts
    - PyHEP organised the UK workshop and are busy with the SciPy 2020 event
- If a WG does not have a dedicated session, we could have WG reports that cover the main activities and directions (as full plenary or an HSF "summary" session)

**As it is fairly urgent to make progress on this we will exceptionally have a meeting next week, dedicated to the Lund scientific agenda**

### PyHEP 2020 workshop

See first announcement in section on PyHEP WG.

## AOB

### Coordination Team

- After discussion about expanding the Coordination Team, we are very happy to welcome:
    - Caterina Doglioni, stressing her excellent links to non-HEP communities (Dark Matter, Astroparticle)
    - Simone Campana, as the representative of WLCG

### CodiMD

- Still need to test if CERN's CodiMD instance is writable to people who use eduGAIN authentication.
    - [Test that here](https://codimd.web.cern.ch/H0QkodL5Ro2st9hp1AHlng?both#)
       - Just tested it and got an internal server error on https://codimd.web.cern.ch/auth/saml/callback ... (Martin)

### Next Meeting

- We will have an [exceptional meeting next week](https://indico.cern.ch/event/880725/) to discuss the Lund workshop agenda
