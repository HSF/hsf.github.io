---
title: "HSF Weekly Meeting #204, 18 March 2021"
layout: plain_toc
---

Present: Graeme Stewart, Benedikt Hegner, Serhan Mete, Eduardo Rodrigues, Nicola Skidmore, Mason Proffitt, Chris Jones, Andi Salzburger, Andrei Gheata, Serhan Mete, Paul Laycock, Stefan Roiser, Allie Hall, Dorothea vom Bruch, Pere Mato, Efe Yazgan, Kevin Pedro, Ben Morgan, Liz Sexton-Kennedy, Michel Jouvin, Teng Jian Khoo, Meirin Oan Evans, Daniel Elvira, Marc Paterno, David Lange, Andrew Norman, Philippe Canal

Apologies: Krzysztof Genser
  
## News, general matters, announcements

### LHCC

The software WLCG report for 2021H1 was prepared - see Indico agenda.

Thanks to all who made comments and suggestions.

### HL-LHC Review Phase 2

We have had some meetings with key people for each section of the document. Now making progress in contacting other projects and arranging mini-workshops, as needed.

### Google Summer of Code, Season of Docs

The GSoC mentors are quite busy at the moment with candidate evaluation and there are few exchanges on the mentors list.

For GSoD so far we have **no applications**. *Do no projects need documentation help?* If there are no proposals we won't apply. Deadline is 25 March.

- Will send another reminder
- Can we also consider facility areas that need documentation?
    - Yes

### November Workshop Survey and Outcomes

See slides attached to the agenda, which give highlights of the survey from the workshop.

- Feedback: no need for a single virtual workshop to be packed with disparate topics, so indeed perhaps better to split into smaller events.

### Proposal for DUNE Framework Requirements Review

Paul: DUNE is trying to work out how to deal with its data, including massive "events" from supernovae (100TB!). DUNE task force has defined the requirements (43 of them) in a document, which is aimed at DUNE people. If the HSF is to give feedback on this, how can it be expanded/annotated to non-DUNE people? Once that's done can we get together a group of experts who could review and bring input from the expertise of the wider community?

- Makes a lot of sense to have the HSF do this, crosscheck requirements and make sure that nothing is forgotten
- Could we ask people from astro-particle to be involved as well, especially to look at the SN event issues

Andrew: wanted to define a timescale on which feedback was given - early enough to be able to take requirements and statements back to FAs, viz. 4-6 weeks... (timescale is driven by US funding and a computing CDR that is due in June).

- To crosscheck the requirements or to check how much existing software matches those (fixed) requirements? Would not be able to do both on a short timescale.

Andrew: check on requirements should be a quick part; real question is how do those requirements fit into the HEP ecosystem?

- We would try to leverage the broadest expertise possible, of people willing to help
- Are the facility boundary conditions clear? GPUs or not? Dedicated or shared resources? Special facilities like analysis facilities?

Andrew: there is a description of some of this and we do anticipate being quite free to decide how to use these resources; data sizes and form of a neutrino analysis are well known. Some feedback on this aspect would also be useful, when people come with different experience.

- That would require some different skills (don't want to have an unmanageable group)

Andrew: HSF is an avenue to different expertise that we would like to take advantage of.

- Have a kick-off talk in a frameworks group meeting?
    - Yes, this is a good idea
    - Chris: agree, but we do want the HSF to assemble a panel of suitable experts

Benedikt, Chris, Kyle and Attila will discuss then how to proceed.

## Working Group Updates

### Data Analysis

- Work has started on the metadata document. After the skeleton document has been created will ask metadata meeting contributors to help populate it
- Organisation of next meeting series on Analysis frameworks has begun (approx. timeline mid-April). Want to focus on the non-LHC experiments, which will be split into developing and established experiment categories. Contacting/investigating potential speakers, please let us know if you have names in mind.
- Current (tentative) list:
    - (proto)DUNE
    - MicroBooNE
    - BNL (RHIC/EIC)
    - JLab
    - FAIR
    - LZ
    - ISOLDE?

### Detector Simulation

- Next two meetings scheduled: <https://indico.cern.ch/category/10916/>
    - 12th April: [Using GPUs in detector simulations](https://indico.cern.ch/event/1019940/). Have updates on AdePT, Celeritas and Opticks/Geant4 examples. See this as opportunity for these projects to report on computing model/progress/plans, _and_ to solicit initial feedback from simulation _users_ on progress on these topics. We will advertise through the usual lists, but wider advertisement very welcome, especially outside of LHC experiments!
    - 10th May: [Simulating solid-state microphysics with Geant4 and G4CMP](https://indico.cern.ch/event/1016632/)

### Reconstruction and Software Triggers

- Kick-off meeting evaluating the outcome of the survey held on Wednesday: https://indico.cern.ch/event/1011873/
- Plan to organize the following events this year:
    - Mini-workshop on heterogeneous computing / algorithms for reconstruction & triggers
        - tentative two half-days, virtual
        - covering both presentations and training
        - together with frameworks & training groups?
        - time slot and exact format to be decided
        - make sure not to overlap with compute accelerator forum
    - Series of 1-hour slot meetings on ML-based / assisted algorithms
        - broader forum than conferences, allowing for in-depth discussions
    - Other 1-hour meetings on some of the following topics:
        - 4D reconstruction
        - Classical reconstruction algorithms
        - Common software

### PyHEP

- **Topical meetings "Module of the month":**
    - Next one on April 7th, on the `pyhf` package.
    - Agenda: <https://indico.cern.ch/event/985425/>.
- **PyHEP 2021 workshop:**
    - First organisation meeting held last week.
    - Indico agenda (WIP): <https://indico.cern.ch/e/PyHEP2021>.
    - Date: July 5-9.
    - Format largely the same as last year's workshop.
      - Aside plan to stream directly to YouTube
      - We would then release the 1000 attendees limit (interesting "problem" to have!)
    - Targeting a community-wide announcement in early April.
      - Registrations will open
      - Abstract submission as well


### Software Tools and Packaging

Our next meeting is on March 31st, 2021 @ 5pm CERN time:
- **Agenda:** https://indico.cern.ch/event/1003975/
- **Topic:** Compiler optimization reverse engineering using [Cutter](https://cutter.re/)
- **Presenter:** Hadrien Benjamin Grasland

**Graeme:** there was a very interesting discussion about Spack in the SFT LIM meeting on Monday. It would be really useful to hear from the Fermilab Spack people in the WG soon.
- **Agenda:** <https://indico.cern.ch/event/1016908/>

### Software Training

Please contact us or drop into the weekly meeting Monday 16h CET so we can help you organise a training.
C++ courses merged onto curriculum https://hepsoftwarefoundation.org/training/curriculum.html
Distributed computing module being planned.

### Event Generators

- First 2021 GEN meeting next Thursday at 16:00: <https://indico.cern.ch/event/1019213/>
    - LHCC review
    - Event accounting

### Frameworks

Had an open discussion a few weeks ago that went well. Current schedule is open for handing the anticipated DNUE review.

---

## AOB

### Next Meeting(s)

- Next meeting will be 1 April - no joke!
