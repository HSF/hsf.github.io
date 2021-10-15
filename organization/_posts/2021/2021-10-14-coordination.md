---
title: "HSF Coordination Meeting #216, 14 October 2021"
layout: plain_toc
---

Present/Contributing: Graeme Stewart, Benedikt Hegner, Marc Paterno, Andi Salzburger, Josh McFayden, Krzysztof Genser, Stefan Roiser, Ben Morgan, Alexander Moreno, Mark Neubauer, Michael Hernandez Villanueva, Liz Sexton-Kennedy, Allison Hall, Caterina Doglioni, Michel Jouvin

Apologies: Serhan Mete, Eduardo Rodrigues,

## News, general matters, announcements

### Letter of Collaboration

After discussion in the coordination group we approved a [letter of collaboration](https://docs.google.com/document/d/1D-IyZs1OkZDZ1MVWILj6g2wfCpCqfW7judTSQ5RfxJE/edit?usp=sharing) with *AccelNet-Implementation: HSF-India - Research Software Networks in Physics* ([description](https://drive.google.com/file/d/1l8akzDcbcSnkRA-AcHaMw296xWUYRWtI/view?usp=sharing)).

The project aims at establishing better collaboration in software with India. We have very good contact with Indian students via GSoC, so there is clearly talent around. Pete noted that few people outside of North America and Europe [signed the CWP](https://drive.google.com/file/d/19vvCEawUg9LBKDOh1nmVa_3oY0lwFpfP/view?usp=sharing), so there is scope to expand in many areas of the world.

### HL-LHC Review Phase 2

Documents were delivered to the LHCC reviewers on time (1 October).

**Many, thanks to the projects and individuals involved.**

The finished versions have been put into [CERNBox](https://cernbox.cern.ch/index.php/s/QGfcgPkvVsC2p31).

Graeme and Liz wrote a short introduction, that summarises the process.

N.B. The review itself will take place 1-5 November, hybrid at CERN + Zoomlandia. Attendance is being clarified with the LHCC, but it should be possible for some participation beyond document editors.

### HSF Letters

After discussion last week, there is a PR to propose a clarification of the HSF policy on letters.

<https://github.com/HSF/hsf.github.io/pull/1023>

Please comment - plan to merge by end of the week if no blockers.

### HSF Upcoming Talks

We have a few HSF talks upcoming:

- [ILCX workshop](https://agenda.linearcollider.org/event/9211/) 26-29 Oct, Graeme invited to speak on *HEP computing challenges and the HSF*
- [Swift-HEP workshop](https://indico.cern.ch/event/1033028/) 2-3 Nov, Caterina invited to speak on *The HSF landscape*

Draft slides will appear!

## Working Group Updates

### Mandates for 2022

We should start to think about WG convenerships for 2022

- Normally WG conveners serve for 2 years, by mutual agreement (but this is not set in stone)

### Data Analysis

Productive meeting last week (“kick-off meeting” after summer) <https://indico.cern.ch/event/1081616/>.

- Discussed expanding the analysis benchmarks. Main topics were fitting benchmarks (particularly for the b-physics experiments but also ATLAS and CMS) and workflow benchmarks that go beyond the simple analysis benchmarks that IRIS-HEP has done so much with
  - For data, interest in using the Snowmass datasets, which should be large enough to be useful
- If you have more comments or suggestions for useful analysis tasks that could be turned into a benchmark, please add to the meeting minutes: <https://docs.google.com/document/d/10XVZm859rjRudImRGtcyKKWFhPLzPVGdr0T4w3Eriqg/edit#heading=h.hcubs8cy4y7c> 
- Other topic was the metadata document, which we are finalizing (everything up to the actual technical specifications is mostly final)
  - <https://docs.google.com/document/d/1zT5tPCtiNfuRm8ywKNbaNGvXGtCZYaO-GOj77pV2BEY/edit>

Next meeting will be announced soon.

### Detector Simulation

- Planning following meetings, speakers to be contacted/dates confirmed:
  - Status/Update on DD4Hep (following on from previous, related topic on PyG4ometry)
  - FPGAs for Simulation (some overlap with previous CAF meeting, but recent updates/progress)
  - New techniques in ML for simulation
- Also idea for Python/Julia use with/in/for simulation.
  - Python maybe joint with HSF Working Group?
  - Julia maybe after HSF report comes out and "why Julia" clarified.

### Reconstruction and Software Triggers

No update on 2nd part of the 4D timing reconstruction meeting, will be probably being followed up only next year (LHC community seems very busy with Run-3 preparation). 

Further on list for potential topical meetings (following the survey):

- Machine Learning in Reconstruction (eventually as a follow-up of the Institute Pascal in January 2022)
- Reconstruction on heterogeneous hardware (mini-workshop in discussion for Q1 2022)

### PyHEP

- Not much to report, there was a [Module of the Month meeting](https://indico.cern.ch/event/1053342/) last week (Qibo). Some discussion of next topics.

### Software Tools and Packaging

- We'll have our next WG meeting on Wednesday, Oct. 20th at 6pm (CEST). Todd (Gamblin) will tell us about the future of Spack. You can find the agenda [here](https://indico.cern.ch/event/1078600/). Please let us know if there are any specific topics you'd like us to cover in the next meetings.

### Software Training

- Software Training in HEP paper accepted for publication in Springer CSBS: [Comput Softw Big Sci 5, 22 (2021)](https://doi.org/10.1007/s41781-021-00069-9).
- Announcement of the next HSF IRIS-HEP Training Challenge in the coming days. 
  - Discussion focused on the sustainability and scalability of the training in the HEP community.
  - Define possible engagement with experiments and their existing training organization. 
- Next Software Carprentries training event being organized (Dec 13-15, 2021). 
  - We are preparing videos to cover prerequisites in Mac, Linux, and Windows. 
- A task force organized to develop the Matplotlib training module. Aiming to organize an event by November. 

### Event Generators

Not much to report, taking a short break after the rush of the LHCC Review document preparation.

Starting to think about topics for future WG meetings. For example, several recent papers of interest:

- "Unbiased Elimination of Negative Weights in Monte Carlo Samples" - <https://arxiv.org/abs/2109.07851>
- "Accelerating Monte Carlo event generation -- rejection sampling using neural network event-weight estimates" - <https://arxiv.org/abs/2109.11964>

### Licensing

Continuing discussion with the HepMC3 authors.

---

## AOB

### SIDIS COST Proposal

The SIDIS COST proposal is advancing well. Contact Graeme and Stefan if you would like to be involved (last chance!).

### Anaconda Terms of Service and Licensing

This has changed recently and they are trying to sell it more as a paid for product, not really suitable for our community.

Can we ask Chris Burr about this - he was keen on this as a solution and presented in the HSF Packaging Group. Miniconda provides a lot of addons, but still refers back to the (to be paid for) Anaconda packages.

Still free for individuals, but unclear situation for non-commercial institutions and labs.

`conda` as a command line tool is still free. ["mini-forge"](https://github.com/conda-forge/miniforge) would avoid connecting to the problematic anaconda default channel.

### HSF Calendar

As dates start to be fixed for 2022, please add things to the HSF Community Calendar.

- Graeme added ATLAS Weeks and ATLAS S&C Weeks for 2022

### ESCAPE + European Open Science Cloud

Setting up the "Test Science Projects", funded by EOSC-Future grant. 

Aim to go from  (more or less processed) data to plots, using reproducible workflows that run on common computing resources, using standards/steering tools provided by ESCAPE. 

Dark matter TSP, coordinated by Caterina: 4 postdocs started working in different EU institutes in October (CERN / tools, LAPP+Lund+Manchester / ATLAS, LAPTh / Indirect detection & theory, FAU / Indirect detection & neutrinos), 1 to come (INFN Rome 1 / direct detection).

Link: <https://projectescape.eu/dark-matter-test-science-project>

Also: Extreme Universe TSP.

Would be nice to sync up with what the Analysis WG is doing (e.g. metadata document) --> will contact the conveners after November 2nd when we have the next meeting.

Anyone is welcome to join the meetings if they'd like on the 1st Tuesday of the month at 10 am CERN time, agendas are here: <https://indico.in2p3.fr/category/976/>.

### Next Meeting

Next meeting 28 October.
