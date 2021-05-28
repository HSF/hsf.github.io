---
title: "HSF Coordination Meeting #208, 27 May 2021"
layout: plain_toc
---

Present:
Andi Salzburger,
Andrea Valassi,
Ben Morgan,
Benedikt Hegner,
Daniel Elvira,
Dorothea vom Bruch,
Eduardo Rodrigues,
Efe Yazgan,
Graeme Stewart,
Krzysztof Genser,
Kyle Knoepfel,
Liz Sexton-Kennedy,
Marc Paterno,
Mason Proffitt,
Meirin Oan Evans,
Nicola Skidmore,
Paul Laycock,
Pere Mato

Apologies: Caterina Doglioni, Josh McFayden, TJ Khoo, Serhan Mete
  
## News, general matters, announcements

### LHCC Meeting

There is a meeting with the LHCC referees next week. The software report will cover news on common software and some brief statement about the progress towards the review.

[Draft talk](https://docs.google.com/presentation/d/1ecdtWvv_PXoKen7sDI-qrFD6HX_Pn4qgD56rzGKndGA/edit?usp=sharing) - additional comments and suggestions welcome.

### HL-LHC Review Phase 2

After our mini-workshops everything is on track for document drafts to be ready by 30 June. The DOMA chief editors (Oliver Keeble, Mario Lassnig) have scheduled two meetings for feedback:

- 1 June for Rucio, FTS and network
- 8 June for storage

Details went to the wlcg-doma@cern.ch list (Zoom link has now been circulated).

### Google Summer of Code

We received 27 slots, which corresponded to the 27 good proposals that we had from potential students. One slot needed to be reassigned as the student was taken by a different organisation, but we managed to re-use it for a Ganga project.

We are in the community bonding period now, with coding starting 7 June.

### DUNE Framework Requirements Review

Review will take place next week, 2-3 June, <https://indico.cern.ch/event/1038551>. See below for details.

## Working Group Updates

### Data Analysis

- [Survey](https://forms.gle/QL7NzSZJDRtUKgTo8) distributed to gain feedback on next meeting in the series "Analysis software in the wider HEP/nuclear physics community". To be on 2nd June.
- [Metadata document](https://docs.google.com/document/d/1zT5tPCtiNfuRm8ywKNbaNGvXGtCZYaO-GOj77pV2BEY/edit) hoping to be wrapped up by Friday.

### Detector Simulation

- Interesting meeting on the [10th May on simulation of solid state physics](https://indico.cern.ch/event/1016632/)
  - Some challenges in performance very similar to those in EM and Optical Photons
- Next meeting is [7th June on the Pyg4ometry package and a GDML update](https://indico.cern.ch/event/1038196/)
  - Expect this may be of interest to anyone using or working on geometry construction (e.g. Reconstruction?) and may be commonalities with DD4Hep.
  - Feel free to advertise more widely for this reason!
- Probably the last meeting before Summer given calendar in June, but as always let the convenors know if you have anything you'd like to present, or topics you'd like to see covered.

### Reconstruction and Software Triggers

- Upcoming meeting on time information in reconstruction, covering three topics
  - Opportunities for HL-LHC (Phase-2 / Phase-3)
  - Time information for future experiments (Linear Collider, Muon Collider, FCC*)
  - Future algorithms (Timing KF, GNN with Timing)
- Could be split into more than one meeting, dates likely 23.06. / 30.06.

### PyHEP

- [PyHEP 2021 workshop](https://indico.cern.ch/e/PyHEP2021):
  - Continue to see a very high level of interest, with various communities (new ones too!) represented :-).
  - Programme under active discussion with invitations being sent out (especially for 1h tutorials) and several abstracts received.
- Topical meetings: [next one](https://indico.cern.ch/event/1039240/) will be on June 2nd on "Giving a good Jupyter talk", as a helper for PyHEP 2021 as various participants welcome info on presenting with notebooks (feedback from last year and interest from this one).
  - This would be of general interest to anyone wanting to develop training and tutorial information.

### Software Tools and Packaging

- We are in a short lull after the recent burst of meetings. The convenors need to meet to make plans, and welcome suggestions for topics and especially volunteers for speakers.

### Software Training

- Planning workshop for IRIS-HEP "Training Challenge" 28.06 16:00 CERN time
  - Aim to train every new PhD student in our collaborations by ~2023
  - Workshop is to flesh out this idea and how we get there
  - Please join if interested!

### Event Generators

- [CSBS paper now published!](https://link.springer.com/10.1007/s41781-021-00055-1)
- Several WG meetings to gather LHCC Review 2 input.
  - Have slots arranged for all generator groups now.
    - Done: Sherpa, EvtGen, Pythia, MadGraph5_aMC@NLO (today).
    - Scheduled: Herwig, POWHEG.
    - One left to arrange for LHAPDF/Rivet.
  - Scheduling has been hard so these will run until the 24th June.
  - We'll work on writing the document in parallel. We haven't started yet but have lots of information from the meeting slides and minutes.
- One interesting comment from the [Pythia discussion last week](https://hepsoftwarefoundation.org/organization/2021/05/20/generators.html): they might be interested to have a code review (but they still need to discuss this internally).
  - *This is certainly something that the HSF can arrange.*

### Frameworks

Fleshing out DUNE framework requirements [mini-workshop](https://indico.cern.ch/event/1038551) (17 registered participants).  Tentative timeline:

- Day one (2 June)
  - Opening
  - DUNE computing overview
  - HEP framework landscape (~3 talks from the HSF conveners)
  - Clarifying the stated requirements
  - Discussion and panel questions/comments

- Day two (3 June)
  - Discussion and panel questions/comments
  - Final remarks from DUNE
  - Executive session among HSF participants

---

## AOB

### ACAT and vCHEP

- The ACAT [abstract deadline](https://indico.cern.ch/event/855454/abstracts/) has been extended to 29 August.
- The vCHEP [post-conference survey](https://indico.cern.ch/event/948465/surveys/2195) is open now.

### CAF and Roundtable

- Next Software and Computing Roundtable [meeting](https://indico.jlab.org/event/420/#b-2284-analysis-i-tools-analys) is Tuesday 1 June at 17h30 CEST, on Analysis Tools
- Next Compute Accelerator Forum [meeting](https://indico.cern.ch/event/975011/) is on Wednesday 9 June at 16h30 CEST, topics are JEWELS Booster Cluster at Julich (Europe's top supercomputer) and Belle II GPU "real-time" analysis

### Recording Meetings

- We discussed if we should be recording HSF meetings
  - In general we think **recording is appropriate for HSF meetings**, which are there to foster discussion and collaboration
    - There are a lot of meetings and it's a worldwide community, so not everyone who is interested can join the meeting
  - However, make it very clear with the speakers and to participants...
    - That the meeting is being recorded
    - And where the video will be posted (YouTube, CDS, etc.)
      - Note that it is strongly recommended not to add video files directly into Indico, instead post a link
  - In any case, *please also make sure that meetings are minuted in a concise way* (it's not always the case that people have the time to watch the 60 minute video and they need a shorter summary)

### Next Meeting(s)

- Next meeting will be Thursday 10 June
