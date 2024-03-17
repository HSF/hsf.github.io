---
title: "HSF Coordination Meeting #265, 29 February 2024"
layout: plain_toc
---

## Attending

Present/Contributing: Caterina Doglioni, Pere Mato, Jim Pivarski, Reiner Hauser, Joe Osborn, Alexander Moreno, Andrea Valenzuela, Liz Sexton-Kennedy, Paul Laycock, Patrick Gartung, Jamie Gooding, Benedikt Hegner, Matthew Feickert, Torre Wenaus, Michel Jouvin, Stefan Roiser, Tommaso Lari, Krzysztof Genser, Steven Mrenna, Daniel Elvira

Apologies/Contributing: Graeme Stewart, Eduardo Rodrigues

## News, general matters, announcements

### HSF Joint Workshop with WLCG

Registration is now open for the WCLG-HSF workshop at DESY (13-17 May) is now available: <https://indico.cern.ch/e/wlcg-hsf-2024> (register at the DESY linked Indico)

Graeme, Eduardo and Caterina are helping with the overall organisation for HSF.

We would like to have a few dedicated sessions/talks:

- Analysis Facilities (N.B. the whitepaper is now finalised), discussing with the experiments
- Software Citation and Recognition Follow-up
    - Caterina and Stefan follow up with EVERSE recognition at the Kick-off meeting
- HSF Evolution Plans
- HSF Training Activities

Our main HSF activity will, however, refocus on community software. We have opened a [call for abstracts](https://indico.cern.ch/event/1369601/abstracts/):

> The HSF will have several sessions on Community Software at the workshop.
We invite you to submit abstracts for talks of 20' where you can describe a tool, package or other contribution that you are making to software for multiple HEP experiments.
Submissions describing projects or other ideas, such as training initiatives or community support structures are also warmly welcomed.
This is your chance to show off how good your project is and to meet and talk to current and future users!

**Please broadcast this call widely and encourage contributors.** Deadline is 18 March.

### LHCC

Generators presented at the last LHCC meeting, with a number of comments/findings from the HSF discussions. Echoed from the generator workshop from last November: 
- need better pipelines for generator software development
- LHCC would like experiments to get involved in JENA activities and HSF could be the catalyser

### JENAA

[announcement](https://www.appec.org/news/joint-ecfa-nupecc-appec-activities-jenaa), [website](https://nupecc.org/jenaa/index.php?display=computing), [2023 workshop](https://agenda.infn.it/event/34738/), 

Keep thinking about how to involve the experimental / theory communities in the broader picture of nuclear and astrophysics. 

Related: SFT has a new machine learning group: how to integrate models better into frameworks (and analysis facilities)? 

### Google Summer of Code 2024

HSF accepted as organization. 
Number of slots only known after student rankings.

Some communication (from the candidates) is lost in CERN email security-related issues / filters. Maybe a solution could be to use Google / GitHub classroom to recruit and select candidates. 

Q&A from later on in the meeting:

  - all-remote program
  - Comment from JimP: the all-remote format works well, the students are ready for that kind of interaction, and we do have some continuity: usually GSoC the first year, then re-hire them as IRIS-HEP Fellows, then other mechanisms, up to 3 years or so
  - Caterina/Benedikt: you get very good computer scientists that can solve standalone problems. 
  - Saptaparna: connection to experiments? A: does not need to be too tight. 
  - Not too late for students to join project proposals, broad advertising. 

### HSF Evolution

Work in progress: next meeting of the core coordination team next week, producing some text for everyone to look at. 

## Working Group Updates

### Data Analysis

Nothing to report. 

### PyHEP

See [slides](https://indico.cern.ch/event/1355741/contributions/5708297/attachments/2801733/4888044/PyHEP%20status%20report%20Feb%2015,%202024.pdf) on the agenda.

Workshop planning, started planning for PyHEP.dev early as it's an in-person workshop that complements the (users, general) PyHEP online for July 1-4 2024. 

Prep meetings in Princeton and Aachen. Planning for a PyHEP.dev conclusion document. 

Monthly topical meetings in the past lack speakers now - how to keep them useful / the audience engaged? 
  * advertise IRIS-HEP topical meetings connected
  * create communication channel for people to ask questions replacing gitter (shared across HSF working groups?)
      * IRIS-HEP Slack exists for developer communication
      * Users of the software don't have places to ask questions apart from GitHub repo (isolated from each other)
          * Could have a common index for these discussions
          * LLMs for semantic search are an option?
          * HSF training also has similar needs
          * More hackathons/help-a-thons with lower organisational bar?

Plan: have a topical chat about this in the future. 

### Detector Simulation

- Had a conveners/coordinators meeting last Monday.
- Will be ready to present 2023 summary and 2024 plans at the next coordination meeting

### Software Training

This week's event: 
- [HSF/IRIS-HEP Training on Analysis Pipelines](https://indico.cern.ch/event/1375507/): 
    - Podman, Apptainer and CI/CD
    - 186 participants registered

Expressed our interest in:
- having a plenary talk and a parallel session at the WLCG-HSF Workshop 

- possibly holding a pre-CHEP event this year


#### C++ Course and Hands-on Training

- 10th HEP C++ Course and Hands-on Training - The Essentials, Mar 25 -29 <https://indico.cern.ch/event/1370681/>
    - Registration still open
    - Mentors (local at CERN) welcome, please sign up [here](https://docs.google.com/spreadsheets/d/1es_UiXuzOcaV1JZ-SmRUDaM_mlKz7K7nS3MZDe3t-C8/edit#gid=0)
    
### Software Tools and Packaging

- Meeting Feb 21 to discuss future plans for meetings/talks.
    - Talk on Fermilab's roll out of Spack later in year

### Reconstruction and Software Trigger

Presenting plans at next meeting.

### Physics Generators

Incoming/outgoing conveners meeting soon, organise training sessions in the spirit of what was done last year. 

Training the next generation of people who are doing generators is hard (especially at labs). 

Points to think about:
   * Some IRIS-HEP projects are generator-related but can we tighten the connections so that they actually get enough help and manage to advance the generator project? 

### JuliaHEP

- Had a WG [meeting](https://indico.cern.ch/event/1352938/) last week: doing EDM4hep data analysis with Julia
- Outcome of JuliaHEP workshop last year: HSF YouTube channel video, outcome document. 
- Plans for 2024 are on Indico, see slides. 
    - Monthly topical meetings
    - Workshop in Sept/Oct 2024
    - Training event in person prior to the workshop
- GSoC and project proposals

## Other Interest and Activity Areas

### Analysis Facilities

The Analysis Facilities Forum [Whitepaper](https://docs.google.com/document/d/1Pn9KWG-tGQ20OaNFUVlXLQddC7vFsQnu2EHR4DBfTjo/edit?usp=sharing) is now revised and finalised. 

*In the best HSF tradition, you are invited to read and endorse the paper (please [email the AFF conveners](mailto:hsf-af-forum-convenors@googlegroups.com) to do this)*

### Compute and Accelerator Forum

Indico agenda for March/Apr/May: https://indico.cern.ch/category/12741/ 

March: joint meeting with OpenLab (Nvidia)
April: high-performance I/O for HEP
May: GPU infrastructure and tools being developed

Planned to have AMD later this year (June?), have CPU/GPU. 

### Software and Computing Roundtable

Restart pushed back to April.

---

## AOB

### CERN Mail filtering

We had issues again this week with HSF mail being quarantined by the CERN mail filters (xorlabs). This was due to Google Group's propensity to spoof sender addresses (see [this article](https://material.security/blog/identify-google-groups-vulnerable-to-spam-and-spoofing). HSF Forum, WG Convener and Coordination lists are now whitelisted. We are discussing if we can fix this also on the group settings, changing the `Default sender` to `Group Address`.

If you have other Google Groups you use, please watch out for this!

### Next Meetings

The next meeting will be on [14 March](https://indico.cern.ch/event/1355742/).

Reminder: please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing one of the 2024 meetings.

