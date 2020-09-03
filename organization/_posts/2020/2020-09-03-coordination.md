---
title: "HSF Weekly Meeting #192, 3 September 2020"
layout: plain
---

Present/Contributors: Graeme Stewart, Stefan Roiser, Serhan Mete, Ben Morgan, Torre Wenaus, Eduardo Rodrigues, Kyle Knoepfel, Witek Pokorski, Attila Krasznahorkay, Caterina Doglioni, Efe Yazgan, Michel Jouvin, Teng Jian Khoo, Josh McFayden, Pere Mato, Benedikt Hegner, Chris Jones, David Lange, Liz Sexton-Kennedy, Philippe Canal, Daniel Elvira, Witek Porkoski

Apologies: Agnieszka Dziurda, Gloria Corti

## News, general matters, announcements

### LHCC News

LHCC referees meeting with WLCG was Tuesday 1 September.

- The agenda pages seem to now be private - we will follow up on that

Andrea Valassi presented a report on the status and plans for generators from the HSF WG. *Feedback from the referees was positive and encouraged the group to continue with their work and for the experiments to engage more.*

Discussion during the meeting centred on the topic of negative weights being the most important one for the experiments; and that optimisation can focus on the processes which are consume most resources for the LHC: V+jets, ttbar, di-bosons.

#### LHCC Review of HL-LHC Software and Computing

Official link for the report: <https://cds.cern.ch/record/2725487/files/LHCC-G-177.pdf>.

Frank Simon has proposed that the next phase of the review looks at common software in much more detail. Three day review anticipated sometime in the window September 27 - October 8, 2021.

More news on the exact charge later, but driven by the idea of a special emphasis on enabling the individual software projects to present plans and status.

This will certainly involve the important generators, Geant4 and ROOT. *Other pieces of software could be included too, so we should suggest any that we think are important.*

### Snowmass

LHCC document was uploaded as a paper to Snowmass. DOI: `10.5281/zenodo.4009114`.

- Zenodo: <https://zenodo.org/record/4009114>
- arXiv: <https://arxiv.org/abs/2008.13636>

Full list of 108 authors was identified (thanks to the WGs for helping a lot with that).

#### LoIs

Believe that a number of LoIs were also uploaded where HSF WGs were involved. It would be a good idea to know which ones.

- Follow this up in the next week gathering these papers.

### Future Trends in Nuclear Physics Computing, September 29 - October 1, 2020

Good opportunity to strengthen links to NP community.

<https://indico.bnl.gov/event/9023/>

3rd in series of workshops. EIC is a theme this time, which is a well focused community.

### New Convenor for Data Analysis WG

We are making good progress with this, hope to conclude soon.

### C++ Course

Dates for the C++ course have been set: 12-16 October, <https://indico.cern.ch/event/946584/>.

**Registration opens next Monday 7 Sept 9.00 am CEST**. N.B. this iteration is **limited to 50 places**. If you can't get a place please still register on the waiting list for eventually grab a free slot and to be informed about new iterations.

**Need more volunteers** for people to be tutors for afternoon hands-on sessions. (It's fine if you can only volunteer for a few, or even just one session.)

### Compute Accelerator Forum

New meeting format to **discuss the fundamental aspects of programming compute accelerators and heterogeneous systems** that apply across application domains. The meeting shall serve as a body to introduce basic concepts, infrastructure and tools and to discuss advanced topics of compute accelerators.

**First meeting at 1 October 15:00 CEST**, <https://indico.cern.ch/event/950196/> with presentations on available GPU infrastructure at CERN/IT and WLCG for software engineering and workflow execution.

The first meeting will be recorded for people who cannot attend. During the meeting we will also discuss the least harmful slot for future meetings.

### GSoC

End of GSoC for 2020, there is a meeting today with lightning talks from all of the successful students: <https://indico.cern.ch/event/949149/>.

## Working Group Updates

### Data Analysis

TJ [presented](https://indico.fnal.gov/event/43829/contributions/193756/) to Snowmass CF in their end-user analysis kickoff.

- Seems like we are very much concerned with the same topics

### Detector Simulation

Restarting after the break. Not much to report today.

### Reconstruction and Software Triggers

Regrouping after vacation period
A long TODO list (we'll have a meeting among conveners):

- follow up on HSF GitHub for Track with Graph NN (where should we place it?)
  - discussion concluded that we can have a GitHub org per working group (prefix with `hsf`)
    - this avoids having too many repositories under the one organisation
  - we should have a "landing page" somewhere that gives an overview of each group
- planning meetings for the Fall, topics:
  - Tracking algorithms exploiting timing information
  - Continuous readout and calibration: ALICE, glueX
  - ML inference in trigger -> there is a workshop about it so maybe point to that?
  - particle flow commissioning up to Run-3
  - reconstruction algorithms in experiments connected to LHC (e.g. FASER, LDMX, others?)
- webpage updates to be put on git (raw content: <https://docs.google.com/document/d/1wEcy53XLwXHok_TNM7LDY2EVq1Ed36O4XRDSAtSuiE8/edit>)

What will we do for the November HSF workshop? For the Lund workshop we had the idea of a session of reconstruction techniques for long lived particles...

### PyHEP

- Eduardo gave a presentation on the WG and the PyHEP 2020 workshop to the EIC community (invitation from JLab).
  - Quite a bit of a "workshop debriefing" presented there already.
  - It will be great to see EIC join the PyHEP community.
- PyHEP 2020 workshop:
  - We had a debriefing among organisers.
  - But still need to analyse the full content of the post-workshop survey.
- WG conveners still to discuss future (topical) WG meetings.

### Software Tools and Packaging

- Next WG meeting on Wednesday the 9th September at 17:00 CERN time:
  - Indico page: <https://indico.cern.ch/event/949460/>
  - Topical discussion on "Build performance w/ Eigen"
- Serhan will give a presentation on [HSF/prmon](https://github.com/HSF/prmon) at the next Grid Deployment Board meeting on Wednesday the 9th September at 10:30 CERN time:
  - Indico page: <https://indico.cern.ch/event/813751/>

### Software Training

- Has been quite active (2 LoIs to Snowmass)
- Lots of work on Henry S's CMake tutorial

### Event generators

- GEN paper
  - Referee comments to be answered by early October.
  - Included as "contributed paper" in Snowmass computational  (<https://snowmass21.org/submissions/compf>) and theory frontiers (No LOI).
- WG meeting(s) 2nd half of September, covering:
  - Recent relevant ML developments, e.g. VegasFlow.
  - New tools addressing negative weights and associated strategies
- Andrea working with MG5_aMC authors on GPUs.
- To resume ATLAS-CMS comparisons waiting for CMS ultra-legacy campaign to be much more complete.

### Frameworks

Started discussing how to come out of hibernation after the holidays... Will likely start with discussions about metadata handling in multi-threaded frameworks.

## Other Interest and Activity Areas

### Event Delivery Forum

- Intelligent data delivery service (iDDS) in production for data carousel, enables prompt distributed processing of data as soon as it appears from tape, improves campaign completion time (shortens tails)
- DAG support implemented in IDDS for experiment-agnostic workflow definition, permits integration with DAG based systems like HTCondor, Pegasus, LSST workflow
- working on LSST as first non-ATLAS iDDS application
- iDDS and its DAG support also in use for scaling up distributed ML services (hyperparameter optimization the first target)
- iDDS doc: <https://idds.readthedocs.io/en/latest/>
- PanDA/iDDS for LSST: [A BNL NPPS group internal update on it](https://brookhavenlab-my.sharepoint.com/:p:/g/personal/spadolski_bnl_gov/ERIRfrSL__NPl6sAHWxGib4BBPGNH9B3pCmTeudEeWQJGg?rtime=u8t1TA9Q2Eg)

---

## Workshops

### Future HSF-WLCG Workshops

- Remote workshop in November (proposal is 19+20 (Thu, Fri) plus 22+23 (Mon, Tue) November)
  - *We need to start planning this in detail now*
  - Main themes
    - Generators (will be 2 years since the last workshop)
    - Simulation (looking at R&D, particularly accelerators)
    - ...
    - Reco for long lived particles
    - Analysis Facilities
    - Hot topics like differentiable computing
  - Please volunteer to help organise! Contact Graeme if you are interested.

## AOB

### Next Meeting

- Next week (10 September) is Jeune Genevois, CERN holiday
- Meet on 24 September - back to the usual every-odd-week Thursday schedule
