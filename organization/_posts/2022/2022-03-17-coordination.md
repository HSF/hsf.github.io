---
title: "HSF Coordination Meeting #225, 17 March 2022"
layout: plain_toc
---

Present/Contributing:
Alexander Moreno,
Allison Hall,
Ben Morgan,
Benedikt Hegner,
Daniel Elvira,
Dorothea vom Bruch,
Eduardo Rodrigues,
Gordon Watts,
Graeme Stewart,
Jin Huang,
Josh McFayden,
Kevin Pedro,
Krzysztof Genser,
Kyle Knoepfel,
Liz Sexton-Kennedy,
Marc Paterno,
Mason Proffitt,
Matti Kortelainen,
Michael Hernandez,
Michel Jouvin,
Nicole Skidmore,
Oksana Shadura,
Paul Laycock,
Pete Mato,
Philippe Canal,
Stefan Roiser,
Vakho Tsulaia,
Wouter Deconinck

Apologies/Contributing: Serhan Mete, Efe Yazgan

## News, general matters, announcements

### LHCC

#### LHCC Referees Meeting

The LHCC referees meeting was on Tuesday 8 March, feedback session was Thursday 10 March. Overall the talk seemed to be well received (for reference, the [slides](https://indico.cern.ch/event/1096585/attachments/2344258/4122673/Common%20Software%202022-03.pdf) are attached to the agenda).

In the Tuesday meeting there were a few questions:

- Q. GSoC, is it useful or a PR exercise?
  - It's useful (otherwise people would not keep submitting projects), both for work done and as a talent feeder; not just for PR
  - This was supported by ATLAS and CMS
  - We even have some examples of people who came into the field via GSoC
- Q. Single precision geometry in VecGeom, how would this be used?
  - Would be used mainly on GPUs, which have much higher SP throughput; but, with care, as round-off errors can appear (large detectors, precision tracking). But it is now there to be tested.
- Analysis Facilities Forum, Catherine expressed support for the initiative; would this also look at other non-HEP communities?
  - No, we think that would over-complicate things and even defining what an analysis facility is for HEP is challenging
  - Simone: group needs to start with a problem statement, so that it can focus on the right questions

The referees' summary statement was "The LHCC commends the CS bodies for their fundamental role in supporting the LHC experiments and welcome the initiatives of HSF and IRIS-HEP in accompanying the development of forums for the larger community to exchange on areas of mutual interest."

LHCC minuites will be published soon.

#### LHCC Bi-annual Report

The LHCC Bi-annual report was due 15 March. Graeme and Liz got project input and Graeme summarised the main HSF activities in the last 6 months.

The draft report is [here](https://cernbox.cern.ch/index.php/s/hAHMEoC8inQAi4b). There is probably still time to make a change if you spot anything important.

#### LHCC HL-LHC Software and Computing Review, part 2

The review committee's [report](https://cds.cern.ch/record/2803119) has now been published.

The report is complementary of the software projects and the HSF. We should read the report and discuss more fully the conclusions.

### Workshops in 2022

#### Analysis Ecosystems Workshop

23-25 May: <https://indico.cern.ch/e/aew2>

**Registration is open!** (limited this to 80 in-person places).

34 people have registered, 30 in-person, 4 virtual.

Progress is being made by session conveners on the following topics:

- Analysis Facilities: Oksana Shadura, Nicole Skidmore
- ML tools and differentiable computing workflows: Lukas Heinrich, Nathan Simpson
- “Real-time” online/trigger-level analysis: Giulio Eulisse, Mike Sokoloff
- Analysis User Experience and Declarative Languages: Jonas Rembser, Alex Held
- Analysis on reduced formats or specialist inputs: Allie Hall, +others
- Bookkeeping and systematics handling: TJ Khoo, Paul Laycock

Next organising meeting 24 March.

*Please forward news about the workshop to your community and think about key people to invite.*

#### Detector Simulation on GPU Community Meeting

3-6 May: <https://indico.cern.ch/e/simgpu>

There is a sketched agenda now and invitations to be sent out soon.

### Google Summer of Code / Season of Docs

First phase of student selection started. Will last till April 3.
A complete timeline can be found [here](https://hepsoftwarefoundation.org/activities/gsoc.html).

There is interest by various people to participate in the Google Season of Docs. David Lange has one idea, Andy Buckley two more. Who would like to organize things? Deadline is **next week**.

There may be a limit to one proposal per "project" - we think there was in the past.

We nominate David and Vassil to do this for HSF! Benedikt will follow-up.

### Snowmass

Deadline for Snowmass papers considered by WGs has passed (15 March). Submissions to the Computational Frontier are [here](<https://snowmass21.org/submissions/compf>). There is still an opportunity for other inputs (see <https://snowmass21.org/>) and we know other things are also in the queue.

### HSF History Paper

[Document](https://docs.google.com/document/d/1y45VSJeUZQnxgk7UMrLpVX4VhWtwYvp1sqz6Hp3dN1g/edit?usp=sharing). Did anyone have input?

Upload to Zenodo is still TODO, but we will do it ~now.

## Working Group Updates

### General

We published the [plans for 2022](https://hepsoftwarefoundation.org/organization/planning/plan-of-work-2022.html).

### Data Analysis

- Metadata paper (<http://arxiv.org/abs/2203.00463>) was accepted for publication in CSBS. We are working on addressing the comments from reviewers now, and will circulate a new draft in the next week.
- Started inviting speakers for a discussion about systematics. Goal is to overview what is currently done by the experiments, and then focus on future developments at the workshop in May

### Detector Simulation

- Next meeting on [28th March on MARS MC](https://indico.cern.ch/event/1107097/)
- Special meeting, in cooperation with the CERN ML4Sim group, on [April 11 at 17:30 CERN time](https://indico.cern.ch/event/1140563/)
  - The topic will be the new Fast Calorimeter Simulation Challenge for ML in simulation, also called the [CaloChallenge](https://calochallenge.github.io/homepage/).
- Finalizing meeting on DD4Hep (joint with Reco and Software Trigger) for second half of May.

### Reconstruction and Software Trigger

- Had the joint CAF meeting on March 9th on Patatrack & ACTS: <https://indico.cern.ch/event/1073640/>
- Had a meeting on 4D reconstruction yesterday (March 16.) with contributions from sPHENIX and LHCb with interesting discussions: <https://indico.cern.ch/event/1128087/>
- finding a date now for a topical meeting on RICH reconstruction

### PyHEP

- Next meeting on *Awkward Array Updates*, April 6: <https://indico.cern.ch/event/1140031/>

### Software Tools and Packaging

- As discussed before, we got in touch w/ Axel Naumann for a talk on the future of C++ (since he's in the standards committee). He suggested to get in touch with others who have been more active with WG21. We need to follow up on that.

### Event Generators

- Snowmass:
  - Had a presentation from Stefan Hoeche last week in the WG meeting. Some useful discussions.
  - The "semi-final" draft (now including executive summary) circulated today
- Tentative Meeting schedule:
  - ~~10th March: Snowmass Generators Whitepaper~~ ([link](https://indico.cern.ch/event/1135424/))
  - 24th March: Recent ATLAS V+jets paper discussion
  - 7th April: (TBC) Generator usage for neutrino experiments
  - 5th May: EIC/NP Generators usage
- Other foreseen topical meetings still to be scheduled:
  - Negative weights and resampling algorithms
  - Progress in GPU/vector CPU porting
  - AI/ML methods for Event Generation

### Frameworks

- We have secured speakers from "small" experiments for April and May:
  - April 6: [NOvA and its Framework Usage](https://indico.cern.ch/event/1138383/) (Gavin Davies of University of Mississippi)
  - May 4: [Mu2e and its Framework Usage](https://indico.cern.ch/event/1138384/) (Roberto Soleti of LBNL)
- We will coordinate with Software Tools and Packaging re. next C++ talk.
- Noted that regular slots used by Frameworks and PyHEP clash (1st Wednesday of each month, 16h CERN time) - conveners should chat and try to avoid this!

### Software Training

- 4th HEP C++ Course and Hands-on Training held on 15–17 Mar 2022.
  - 75 participants.
  - Two hour interactive lecture session in the morning and hands-on training exercises during the afternoons (CEST).
  - Course was split into two parts (Essentials & Advanced). This was the first time we ran the "Essentials" part. Advanced part will happen most likely after summr. 
  - Hybrid format: meeting room at CERN + Zoom.
- Two training events announced for the coming weeks:
  - Software Carpentry (Virtual):  28–30 March 2022 
    - <https://indico.cern.ch/event/1112526/>
    - Same format as previous SC events: two days covering development essentials (Bash, Python, Git) and the last day focused to HEP (ROOT, Uproot).
    - **Registration opens tomorrow March 18** (tell your students)
  - Matplotlib Training (Virtual): 21–22 April 2022
    - <https://indico.cern.ch/event/1058838/>
    - First-time Matplotlib training. The module was developed recently by enthusiast volunteers from the HSF/IRIS-HEP training working group.
    - **Registration opens tomorrow March 18** (tell your students)

## Other Interest and Activity Areas

### General

Compute Accelerator Forum / HSF Reco and Triggers meeting [last week](https://indico.cern.ch/event/1073640/) saw interesting presentations on Patatrack and ACTS.

### Analysis Facilities

- Kick-off meeting arranged for 25 March: 
  - <https://indico.cern.ch/event/1132360/>
  - Please register!

### Licensing

Benedikt contacted all HepMC3 authors for consent to move to LGPLv2.1-or-later instead of GPLv3. All but one answered and agreed.

---

## AOB

### Swift-HEP

Graeme and Alessandra will attend the [Swift-HEP workshop](https://indico.cern.ch/event/1127798/) next week, with presentations on HSF Activity and the Analysis Facilities Forum

- Draft slides will arrive next week!

### Next Meeting

Next coordination meeting is scheduled for 31 March.
