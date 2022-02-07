---
title: "HSF Coordination Meeting #205, 1 April 2021"
layout: plain_toc
---

Present:
Graeme Stewart,
Teng Jian Khoo,
Andrea Valassi,
Paul Laycock,
Serhan Mete,
Eduardo Rodrigues,
Meirin Oan Evans,
Kyle Knoepfel,
Michel Jouvin,
Benedikt Hegner,
Ben Morgan,
Attila Krasznahorkay,
Allison Hall,
Krzysztof Genser,
Sudhir Malik,
Liz Sexton-Kennedy,
Chris Jones,
David Lange,
Dorothea Vom Bruch,
Host Severini,
Josh McFayden,
Kevin Pedro,
Michael Villanueva,
Mike Kirby,
Philippe Canal,
Daniel Elvira

Apologies: Andi Salzburger, Pere Mato, Efe Yazgan
  
## News, general matters, announcements

### HL-LHC Review Phase 2

The Generators WG meeting last week discussed the review - see below for a report from the WG convenors.

Key people in Simulation met yesterday (expts., projects, HSF) and are planning a mini-workshop where experiments will present some plans (from CTDRs), boundary conditions and thoughts about R&D impacts. Should be w/b 26 April, afternoon meeting CERN time (to be doodled).

Key people in Analysis met yesterday (expts., projects, HSF) and are planning a mini-workshop where experiments will present some plans (from CTDRs), boundary conditions and thoughts about R&D impacts. Should be w/b 26 April or 3 May, afternoon meeting CERN time (to be doodled).

DOMA project has appointed two chief editors for that document, Oliver Keeble (CERN IT) and Mario Lassnig (CERN EP, Rucio).

We have asked for first document drafts by 30 June.

### Google Summer of Code, Season of Docs

Students who did good assessments are now working on their proposals, have to be done by 13 April.

Season of Docs? Waiting for news.

### Proposal for DUNE Framework Requirements Review

The basic idea, following on from the discussion at the last coordination meeting, is to bring together a panel of experts with broad experience (e.g. including experts from outside HEP) to review the annotated[1] DUNE requirements and make recommendations.  The panel will be chaired by the HSF Framework WG convenors who would start contacting potential panel members ASAP.  Review of the requirements by the panel could start as early as possible, with a "panel meets DUNE" workshop consisting of two 1/2 days after vCHEP (late May / early June) that could then focus on the recommendations.  The workshop outcome would be a public document (it is the HSF!), DUNE could then take those recommendations and make a development plan.

[1] Annotated, as the DUNE requirements are written for a DUNE audience.  These annotated requirements would need to be public, intend to use googledoc for this and freeze at the time of the workshop.

## Working Group Updates

### Data Analysis

Started contacting individuals from various experiments for our upcoming meeting series, attempting to survey the wider HEP & NP communities for analysis computing needs. So far the response has been encouraging, and we are trying to get specific names. Contacted so far:

- Neutrinos:
    - SBN, DUNE (looking for speakers), FASERnu (apparently heavier requirements than FASER)
- Nuclear:
    - JLab, sPHENIX (speakers confirmed), FAIR (interested, looking for speakers), EIC (contacted)
- Dark Matter:
    - Xenon1T, LZ (contacted, looking for speakers)
- Rare decays/precision:
    - Muon g-2 (contacted), further suggestions from Ben to be followed up

We hope to start the week of April 19.

Have also been working on metadata summary document. To flesh out tech specs then invite wider community input.

### Detector Simulation

- Next meeting confirmed for 12th April on Using GPUs for Detector Simulation (Updates on EM/Workflow from AdePT, Celeritas projects, Opticks/G4 integration) , announcement sent, further advertisement welcome!
  - <https://indico.cern.ch/event/1019940/>
- After that, next meeting is 10th May on simulation of solid state microphysics
  - <https://indico.cern.ch/event/1016632/> 


### Reconstruction and Software Triggers

- Will be planning more activities post-Easter based on survey feedback

### PyHEP

- Monthy topical meetings "Module of the month":
    - Next one coming up next Wednesday at 16h CET
    - Tutorial on the [pyhf](https://github.com/scikit-hep/pyhf/) package for "fitting/limit-setting/interval estimation HistFactory-style"
- PyHEP 2021 workshop:
    - Preparations under way. Still planning on first announcement by early April
    - Basic information at <https://indico.cern.ch/e/PyHEP2021>

### Software Tools and Packaging

We had a nice meeting yesterday:
- Agenda: https://indico.cern.ch/event/1003975/
- Topic: Compiler optimization reverse engineering using [Cutter](https://cutter.re/)
- Speaker: Hadrien Benjamin Grasland
- Executive summary:
    - A nice turn-out, great discussions. Cutter is an open-source project that can be used to guide optimization studies. Hadrien gave a nice demo where he walked through an example, going from binary to assembly via decompiling and doing a static analysis on why two different libraries (std vs thrust) were giving different results for a specific problem dealing with complex numbers. All these were accomplished without run-time testing. The tool itself is a work-in-progress. Therefore, it has a number of rough edges. 

*We recommend that meetings like this be recorded, when there is lasting value in the presentation and demo.*

Meeting on Spack is being planned, but date not yet settled.

### Software Training

- Reinforce the synergy with other working groups is one of our main goals. We would like to propose a training liaison from each WG, acting as a contact person.
    - Eduardo - is it necessary to have a named liaison? Will end up being the same, well known, people.
    - Michel - it's not the same as an experiment role; it's lightweight and overcomes diffusion of responsibility
    - WGs should feedback...
        - *Main aim is to establish a point of contact and not have a dead channel*
- Next Hackathon will be organized next June, still a few months ahead. To keep momentum, we will send an invitation for a follow-up of the last Hackathon to be held in April. 
- IRIS-HEP will resubscribe to The Carpentries. We will take advantage using the resources available, like a training of trainers for HSF.

### Event Generators

Had LHCC Review 2 kickoff [meeting](https://indico.cern.ch/event/1019213/)

- Attendance from most generators/tools groups, will follow up with those missing.
- Starting to plan next meetings with a view to the HL-LHC review: we will invite each generator/tool group to give contributions over the next ~2 months.
- Also discussed an update about CMS accounting for generator CPU costs.

### Frameworks

- Working to form panel for reviewing DUNE's framework requirements.  Will be sending out invitations to potential panel members soon.
- "General discussion" meeting next Wednesday. (With short report from ATLAS's / Gaudi's TBB migration.)

## Other Interest and Activity Areas

### Visualisation

Phoenix people want to start holding meetings as their user base grows - created a category for that in Indico.

### Licensing

ATLAS had reason to use an EvtGen header in Athena, for which it turns out the licence is GPLv3, which would have its usual viral impact on the rest of the code, which is baseline Apache2.

We contacted the EvtGen authors who were not in principle averse to changing to a more liberal licence, however they are dependent on Pythia8, Photos++ and Tauola++, all of which are GPL, tying their hands.

In the course of this discussion we realised that HepMC3 is also GPL. As the main interface between the generators and the experiment codes we would like to ask that the authors change this to (at least) LGPL. This is to be followed up.

Archeology showed that HepMC2 should have been under BSD license.

FastJet authors were not very willing to change their license when we discussed with them. There has been some recent development here to add thread-safety.

Propose dual licensing to generator authors? If they want to keep GPL for everyone and allow HEP to use it non-virally nonetheless, maybe this can be formalised?

*Follow-up in a Generator WG meeting.*

---

## AOB

AIDAinnova kick-off meeting, 13-15 April: <https://indico.cern.ch/event/1003419/overview>.

* There is a software work package with tasks in Turnkey Software, ML Simulation, Tracking, Particle Flow. People very welcome to join the discussion and hear about plans.
* Frank Gaede (DESY) and Graeme Stewart (CERN) are WP coordinators.

### Next Meeting(s)

- Next meeting will be 15 April
