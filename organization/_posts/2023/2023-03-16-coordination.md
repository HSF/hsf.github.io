---
title: "HSF Coordination Meeting #246, 16 March 2023"
layout: plain_toc
---

## Attending

Present/Contributing: Benedikt Hegner, Graeme Stewart, Krzysztof Genser, Christina Agapopoulou, Eduardo Rodrigues, Kyle Knoepfel, Valentin Volkl, Torre Wenaus, Stefan Roiser, Nicole Skidmore, Matthew Feickert, Alessandra Forti, John Chapman, Juraj Smiesko, Nick Smith, Liz Sexton-Kennedy, Killian Lieret, Nicole Skidmore

Apologies/Contributing: Claire Antel, Efe Yazgan

## News, general matters, announcements

### Pre-CHEP Workshop

HSF-WLCG [pre-CHEP workshop](https://indico.cern.ch/e/wlcg-hsf23) planning now well underway.

See slides on the agenda.

Benedikt: how do we gather outcomes and plan next steps?

- AFF will write a whitepaper in advance of the workshop, which is the basis for the first 2 presentations
- AFF gathered a lot of information, but cannot marshall resources, so that's why we need the experiments on-board
- HET we have to do more work, but we should have a skeleton in advance that we can use to draw conclusions

### Google Summer of Code, 2023

Next steps:

- First round of selections finished on March 14
- Some tail of not yet finished evaluations
- Final selection in two weeks

### Google Season of Docs, 2023

[Google Season of Docs](https://developers.google.com/season-of-docs) has been announced. Deadline for the application is March 24. We still need to select which project to put forward this time. Proposals welcome.

Still waiting for input!

Valentin - there are projects that would be interested, but perhaps some confusion because only one proposal can be made

- Conclusion, if you have an idea then please send this ASAP!

### LHCC

#### LHCC Referees Meeting

Graeme presented the Software Project summary to the LHCC (see [slides](https://indico.cern.ch/event/1225011/attachments/2552950/4514912/LHCC%20153%20Software%20Presentation-1.pdf) on the agenda). This consisted of inputs from Geant4, ROOT and the 4 LHC experiments.

- LHCC were very positive about the progress in the projects, making substantial progress in improving the efficiency of our software and reducing resource needs.
  - These are recognised as vital projects for LHC physics.
  - Appreciated very much the close collaboration between the experiments and the projects.
    - Understanding and validating new physics results in Geant4
    - Adding all the required features for a new I/O subsystem
  - They encouraged experiments and funding agencies to make commitments to working with Geant4 to maintain expertise.
  - Encouraged large scale tests of RNTuple in production at a variety of grid sites.
  - Stressed the importance of career progress to foster an up-and-coming generation of experts.

Projects were present at the meeting with the referees. The LHCC Referees meeting agenda is closed as sometimes sensitive topics are on the slides (hence we mirror the slides on this agenda). *Our software slides are public, please use them as needed.*

#### WLCG Half-yearly Report

We have input from the projects and, very soon, from HSF activities which are prepared [here](https://docs.google.com/document/d/1M7ujqYEKoeF3qa9INhM9_Y1Fa9iPByiJkaC2w9Ka_to/edit?usp=sharing).

If you have any comments or observations please make them today or tomorrow (report needs to be submitted on Monday 20).

### LHCP Invitation

We have been invited to give a talk at [LHCP](https://lhcp2023.ac.rs/) (May 22-26), in the Upgrade/Performance & Tools parallel session (20'+4'). Tentative title *Computing Challenges at the HL-LHC and Beyond*. The organisers strongly request in person presence.

We have a volunteer from TMU, Vangelis Kourlitis, who can give this talk (he is an expert on simulation and analysis and we can help with any other aspects of the talk). Thanks to him for volunteering and to Lukas Heinrich for enabling this.

## Working Group Updates

### General

After we finish all the WG presentations we should update the HSF Planning page, and advertise this and the WG mailing lists to the community.

#### Meetings

*Reminder:* Please try and book meetings in Indico at least 2 weeks in advance!

That way they go into the calendar early and they will be included in the weekly email announcement that goes to HSF Forum.

### Data Analysis

- Also involved in CHEP pre-workshop and CHEP track convening
- Analysis survey template discussion: working to find experiment contacts and organize a first meeting (CMS and LHCb identified)
- Abstract on experiment on-boarding accepted for CHEP - to decide speaker. No movement with paper.

### Software Training

- Had [**hackathon** two weeks ago](https://indico.cern.ch/event/1261775/) on analysis preservation training
- Talked to [REANA](https://reana.io/) team: [Cloned old "carpentry-style" training](https://github.com/hsf-training/hsf-training-reana-webpage) and brought it to our organization. Started to brush up the framework.
- Would have **funding to have US based student** working on training material in the coming months (but currently missing qualified candidate). [Possible topics](https://docs.google.com/document/d/e/2PACX-1vTYzpXhUpC6bDcHWeax3-FLjadZYt_SZ18J72FQ_UkpEpky82VstqCqiNI8a3im120fLBm0rhR6t3Q3/pub): pytest (for analysis preservation), brushing up REANA lesson, brushing up "plotting for HEP" lesson, or more for "expert" students
- **GSoC**: O(40) applicants for [training center project](https://hepsoftwarefoundation.org/gsoc/2023/proposal_HSFTraining_central_entry_point.html), O(30) submitted qualification tasks, currently 6 left in phase 2
- **Question**: Could we link to our rendered training webpages relative to hepsoftwarefoundation.org? E.g., `hepsoftwarefoundation.org/t/apptainer`, `hepsoftwarefoundation.org/t/cicd-gitlab`, etc.?
  - This would avoid having links break when we rename training modules (as we need to do for some already)
  - **Yes** - we believe this is possible using simple Jekyll redirects

#### C++ Course and Hands-on Training

The HEP C++ Course, "the Essentials" took place 6 - 10 March <https://indico.cern.ch/event/1229412/> at CERN & zoom. The 20 CHF registration fee helped reducing the no-shows. For next time we will free the slots of not paying students on time.

- Very positive feedback by participants (see [de-briefing slides](https://indico.cern.ch/event/1234519/contributions/5194811/attachments/2612100/4513293/20230315-HepCppCourse-6thCoursePostTraining.pdf)).

- The hybrid approach worked well.
- Students were particularly happy about having an in-person event again
- They liked the idea of leap days allowing them to catch up
- The programme was perceived as challenging

More courses planned in 2023:

- 15-17 May tentative (week after CHEP) @ JLAB (contact: Brad Sawatzky)
- end Aug @ Manchester (contact: Caterina Doglioni)
- 16-20 Oct tentative, Fall "Advanced course" @ CERN

Meetings to define more details next week.

Are these courses local or residential? Need to explore resources and rediscuss this.

If you want to stay informed about upcoming courses please sign up at <https://indico.cern.ch/e/HepCppInfo>. Announcements of new courses will be sent to registrants.

### Software Tools and Packaging

Yesterday, presentation and discussion about [The status of Linux distributions for HEP](https://indico.cern.ch/event/1245212/).

### Detector Simulation

In the process of organizing sessions on:

- Geant4 cut tuning as done by experiments
- Overview of external (not Geant4) physics model developments
- Geant4 hadronic physics models and connections with event generators

### Reconstruction and Software Trigger

Not much to report. Updated webpage with new conveners' info. Planning a kickoff meeting (probably next week) with all 3 conveners.

### PyHEP

[PyHEP.dev 2023](https://indico.cern.ch/e/PyHEP2023.dev) registration is now closed.

- We have so far a very good level of registration (even more so taking into account constraints of this in-person event).
- Details to be provided later once we finalise attendance (it requires approval as we wanted to have the "best and widest" community representation possible).

## Other Interest and Activity Areas

### Compute Accelerator Forum

- 2023 Calendar
  - [CADNA a tool for estimating numerical stability](https://indico.cern.ch/event/1264290/), April 26
  - [Hepix Benchmarking](https://indico.cern.ch/event/1207839/), 14 June

- Do get in touch with Graeme, Ben, Stefan if you have an idea or a topic to present.

### Analysis Facilities

Meeting last week, focussing on EOS storage: <https://indico.cern.ch/event/1260978/>.

Covered tuning that was done to improve performance to the point where it's the application which is the bottleneck. And some discussion on user use and abuse of CERNbox. Video is available.

### Licensing

Question from the community about providing CUDA on cvmfs (runtime is ok, but SDK is the issue).

---

## AOB

### Next Meeting

The next meeting will be on [30 March](https://indico.cern.ch/event/1225012/).

Please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing this or one of the future coordination meetings.
