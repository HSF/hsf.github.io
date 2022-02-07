---
title: "HSF Coordination Meeting #206, 15 April 2021"
layout: plain_toc
---

Present: 
Allison Hall,
Andi Salzburger,
Andrea Valassi,
Andrei Gheata,
Attila Krasznahorkay, 
Ben Morgan,
Benedikt Hegner,
Caterina Doglioni,
Daniel Elvira,
Dorothea vom Bruch,
Eduardo Rodrigues,
Efe Yazgan,
Graeme Stewart,
Josh McFayden,
Krzysztof Genser,
Kyle Knoepfel,
Liz Sexton-Kennedy,
Marc Paterno,
Mason Proffitt,
Michel Jouvin,
Mircho Rodozov,
Nicole Skidmore,
Paul Laycock,
Pere Mato,
Philippe Canal,
Serhan Mete,
Stefan Roiser,
Sudhir Malik

Apologies: Kevin Pedro
  
## News, general matters, announcements

### HL-LHC Review Phase 2
    
We have discussed having mini-workshops to help prepare for the Analysis and Simulation documents. The idea is project and experiment presentations on plans, R&D, boundary conditions, etc. that we then discuss to check that we are aligned.

The dates are now fixed for these meetings:

- Detector Simulation, Thursday 29 April <https://indico.cern.ch/event/1028379/>
- Analysis, Tuesday 4 May <https://indico.cern.ch/event/1028381/>

They run from 15-18h CEST. Note the plan is to have a first draft of these documents by *30 June*.

For the Physics Event Generators the WG conveners are contacting different generator teams and will invite them to discuss the review in forthcoming meetings. There are quite a few to get though, but we think we have time.
### Google Summer of Code, Season of Docs

- now in the proposal evaluation and slots request phase
- 74 proposals (8 of them spam) for our 36 project ideas. This is 1/3 the number of last year. Observed by other orgs as well:
    - *"In our case, we got about 50% less applicants this time"*
    - *"We had 86 proposals last year but were reduced to 39 this year"*
    - *"It is horrible this year. 70% of proposals are empty, nothing beyond “My name is John Doe and I have 50 hours per week to work for you”. I guess it is the pandemic effect."*
- the spam rate we got seems to be quite low compared to other Orgs:
    - *"... about 55 total with ~10 being spam"*
    - *"... received 21 total proposals, out of those 15 actually had a proposal that was more than just a resume, ... This was a sharp decline from last year were we got 62 proposals, with 15 of those being spam."*
- counted 9/36 projects without a proposal
    - [Caterina] I guess we can't "share" good candidates at this point? It was hard to do it before the deadline as it would have been against the Google recommendations (it would have meant ranking before the proposal stage) -> A. no, unfortunately this isn't possible
- we plan asking for slots for **all** projects having a good candidate
- we sent instructions to mentors for evaluating and ranking the proposals in the coming days, the deadline is Apr 20 to send us feedback (with few days extension for any good reasons)
- we have not applied for **Season of Docs** this year since we haven't received any project proposals


### Proposal for DUNE Framework Requirements Review

- We have now heard from everyone that we invited to the panel.
- Will be sending a more formal communication soon.
- 6 out of 7 people said yes to the invite.
- Will have 2 x 1/2 day meetings at the end of May (but some internal panel discussion before that).

### HSF Workshops in 2021

With vCHEP and ACAT this year (and the HL-LHC review) we think there is no need to have a big event this year.

But we would like to have possible mini-workshops focusing on one particular topic. A couple of possible ideas:

- Focus on high-granularity calorimeters, from simulation to reconstruction
- Focus on I/O, driven by technology evolution and how this would affect data processing software and facilities

For next year, we do plan to have a f2f pre-CHEP workshop in Norfolk (has been discussed with Amber).

See PyHEP 2021 workshop below.

## Working Group Updates

### Data Analysis

- Meeting series on "Analysis software in the wider HEP/nuclear community" starts next week on Wednesday, April 21 from 15:30-17:30 CET, featuring speakers from SBN, DUNE, Jefferson Lab, and sPHENIX: <https://indico.cern.ch/event/1027471/>


### Detector Simulation

- Meeting last Monday on GPUs was widely attended and good set of material and questions <https://indico.cern.ch/event/1019940/>
    - Excellent early results on physics between AdePT and Geant4 ~0.1%
    - Opticks work presented showed a huge speedup that should be able to benefit LAr detectors
        - Growing involvement beyond Simon Blyth and using current version of Geant4
- Next meeting on 10th May on "Simulating solid-state microphysics with Geant4 and G4CMP": <https://indico.cern.ch/event/1016632/>
- Starting to think about next set of meetings, as always, suggestions for topics welcome!


### Reconstruction and Software Triggers

- Planning a topical meeting on 4D reconstruction. Date still to be defined (tentatively on May 26th)
### PyHEP

- **Topical "meeting of the month" on the [pyhf](https://github.com/scikit-hep/pyhf) package** held last Wednesday, see <https://indico.cern.ch/event/985425/> for the tutorial materials and the recording uploaded to YouTube.
- **PyHEP 2021 workshop:**
    - Details on the [Indico agenda](https://indico.cern.ch/e/PyHEP2021).
    - First announcement went out yesterday via many community lists and communication channels.
    - Registration and abstracts submission are both open.

### Software Tools and Packaging

Next meeting on *experience with Spack at Fermilab* by Steve White:
- **Date:** Wednesday 28 Apr 2021 at 17:00 CERN
- **Agenda:** <https://indico.cern.ch/event/1026182/>
- The goal is to have 30' presentation followed but a discussion among Spack developers/users (need to invite some people explicitly, e.g. Valentin Volkl for FCC/Key4hep and Ivan Razumov for SPI etc.; FAIR experiments). Please feel free to advertise more widely. An announcement will be made soon, too.

There is a Spack HEP channel that can be used for discussion and help.
 - See <https://spack.io> for details/links.

### Software Training

Not many people signed for training hackathon followup (to pick a date in end of April) - <https://doodle.com/poll/2yuffursq7t7ghhb>
Please advertise (C++ team??), also using Mattermost. This is good for other HSF working groups with interest in training.

### Event Generators
- Had a discussion with Graeme and Liz about the HL-LHC review. We are planning meetings to follow up.
    - Potential next meetings 22 April, and 6 May Thursday 16:00 CERN time
    - We are starting with Sherpa, Madgraph, Powheg, Pythia8, EvtGen and Herwig7 (~2 groups/meeting)
- We received the latest proofs of the CSBS paper, need to give a final cross check but will hopefully be published soon.

### Frameworks

We met last week for our monthly "coffee"--Ben Wynne (ATLAS/Gaudi) discussed efforts to migrate to the encouraged TBB interface. These have been rather fun!

- Other projects, like ROOT and Geant4 have migrated, we think
- Frameworks concerned are art, CMSSW, Gaudi seem to be well on the way
- Experiments who are not memory bound tend to just use multi-processing (Belle II)

Would also like to touch on data quality in later meetings.

Much effort going into DUNE fwk review.

## Other Interest and Activity Areas
### Licensing

Plan to update / reword the HSF document about licenses and copyright.

- More explicit and clear advice about people writing libraries, in particular

---

## AOB

### ESCAPE / European Open Science Cloud EOSC-Future work starting

- Goal: prototype end-to-end analysis workflows for two science project (dark matter / extreme universe & gravitational waves) on frameworks/services that will work on the European Open Science Cloud
    - Using the ESCAPE services as a starting point
- Dark matter science project: have theorists + indirect detection, direct detection (DARKSIDE), collider (ATLAS/CMS) experimentalists on board
    - For now those are only ESCAPE partners (who get funding)
    - Once things are starting, will "extend the invitation" to other experiments
- How to coordinate with analysis / frameworks (?) WGs? 
- There are quite a number of people in CERN-IT also involved (Simone Campana, Riccardo Di Maria, ...)

### Mailing Lists

It seems that changes in Google policy now mean that it is *not* possible to
sign up to Google Groups lists without a Google account. Note that when we
decided the mailing list policy for HSF it was before eduGAIN so we may
consider a different policy later (not urgent).

### Next Meeting(s)

- Next meeting would be 29 April
    - Clashes with Detector Simulation mini-WS
- Meeting after that would be 13 May
    - Clashes with the Ascension Holiday at CERN and in many EU countries
- Propose then an exceptional even-week meeting, *Thursday 6 May*
    - Agreed: next meetings 6 May, then 27 May
