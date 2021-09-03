---
title: "HSF Coordination Meeting #213, 2 September 2021"
layout: plain_toc
---

Present: Graeme Stewart, Josh McFayden, Attila Krasznahorkay, Kyle Knoepfel, Michel Jouvin, Pere Mato, Ben Morgan, Dorothea vom Bruch, Krzysztof Genser, Mark Neubauer, Caterina Doglioni, Eduardo Rodrigues, Allison Hall, Philippe Gras, Liz Sexton-Kennedy, Alexander Moreno, Andrei Gheata, Gordon Watts, Jerry Ling, Michael Hernandez, Nicola Skidmore, Sudhir Malik, Torre Wenaus, Daniel Elvira, Benedikt Hegner, Aman Goel

## News, general matters, announcements

### Julia Discussion

See slides on [the agenda](https://indico.cern.ch/event/1043626).

- Workshop planned on **September 20** to discuss with more details how to move forward in the
  Julia evaluation planned in PyHEP WG

- Don't use developer preferences to guide choices ("small enthusiastic communities bias" of minor languages)
  - We need to concentrate on the language's features and potential
- Any roadmap for integration should be clearer than Python (we now have experience of going beyond a single language)
  - Building bridges is important, don't rebuild everything - we need to use legacy code
  - Julia and Python can interoperate

### LHCC

#### HL-LHC Review Phase 2

We now have the first version of most documents:

- [Generators](https://drive.google.com/file/d/18_ID_XLw4K1AjaYXuQC2pdNjZEWWbhk4/view?usp=sharing) (PDF copy)
- [Simulation](https://docs.google.com/document/d/1Rl9PH43gEWSzYtELT12-77zi-uW1avz8uClL44wcDvE/edit?usp=sharing) (Google Doc)
- [Foundation](https://docs.google.com/document/d/160o1LtpjL0Zgb4Suey1vyD_l03Ggh4frrADXMlOUcC4/edit?usp=sharing) (Google Doc)
- Analysis
  - [Data Science Tools](https://docs.google.com/document/d/13b1icyAsr99gPqgTQo5-Lso5x6aotdvVXe8lXjD5YvY/edit?usp=sharing) (Google Doc)
  - [ROOT](https://docs.google.com/document/d/15dlmSbOUCXXC35tOX5axNlK96MqnOqw_93RnSgCpDjI/edit?usp=sharing)
- [DOMA](https://www.overleaf.com/read/gkbppxdvcvvf)

Time for comments has basically passed, so if you want to give further feedback please do that ASAP.

#### LHCC Referees Meeting and Closed Session

LHCC Referees meeting was this week. Slides are [attached to the agenda](https://indico.cern.ch/event/1043626/). *Many thanks to everyone who gave input.*

Feedback:

- CernVM effort levels were discussed, stressing the need for projects like this to do *support* and *R&D*
- Some clarification on the ROOT/HighLO project, praised for attracting external funding
- Discussion of the sustainability of the current C++ course, where - stressed that others (beyond Sebastien P) were contributing and the course material was open source
- Long discussion on the effort available for software and computing, particularly for computing operations, the fact that this is declining and not well recognised
  - Institute commitment was seen to be key to solving this
  - Recognised as part of a wider problem, covering almost all areas
  - Software is not in quite such a parlous state as operations, but it was stresses that software needs *long term support* and *viable career paths* - just funding cool R&D isn't enough
- Many thanks from the referees for the efforts put into preparing the HL-LHC review documents

### HSF Letters

#### KISS - German Machine Learning Project

[Simulation ML project](https://drive.google.com/file/d/1x5cZDP-7R40X9NvCY2pODfcoNgO9MSD8/view?usp=sharing) applying for funding in Germany. The project is broad, interdisciplinary, and aligned well with what we laid out for simulation in the CWP.

We distributed the following information and a [letter of support](https://docs.google.com/document/d/1qyTPWRKyu9sDmLba0RjEkx6L4fV2ApaLG4b67ko1wfQ/edit?usp=sharing) was given last week.

#### Fellowship Proposal

We were approached by a colleague asking for support for their fellowship application in the UK. This is to work on computational improvements to event generators and is aligned with the challenges that we identified.

There was general concern expressed in discussions that the HSF should not support *individual* applications in a competitive setting, where the HSF is not structured to be able to judge particular individuals. Our role should be to support *community* efforts, thus should be at the level of support for projects and consortia working on common software topics.

Our support for certain *work topics* is already made clear via the CWP and other HSF documents, such as the Generators paper, which can be freely cited and we encourage applicants to do that. Anyone can be approached to write a reference letter for candidates and is also free to mention HSF papers in respect of the proposed work, but should not do that in an HSF role.

### NorCC Meeting

Graeme was invited to give a talk on the international software development landscape in HEP to the NorCC meeting (new umbrella organisation of all Norwegian CERN activities), Friday 3 September.

[Draft slides](https://docs.google.com/presentation/d/1w0Kk8OPNEdQe7G5PNbgRO6G9bOEfYq0nH7j9TgwO_Kc/edit?usp=sharing) - comments welcome.

## Google Summer of Code

We had 27 students this year, of whom 25 completed successfully (93%).

- Big thanks to everyone who took part
- Particular thanks to our coordinators: Andrei, Xavier and Antoine

- Discussion about the success rate noted that:
  - Our success rate has steadily improved over the years
  - It's usually higher than the program average

An EP newsletter article has been prepared by Graeme and Andrei.

## Working Group Updates

### Data Analysis

- Starting to plan next topical meetings; more details to follow.

### Detector Simulation

- Starting to prepare Autumn meetings, contacting speakers.
- As always, contact the convenors if you have anything you'd like to present or see covered.

### Reconstruction and Software Triggers

- Planning second topical meeting on 4D timing on September 22nd or 29th (tbc)
- Possibly plan a mini-workshop on heterogeneous architectures in November
- Getting in touch with people in the field to get a feeling for need / interest of specific topics for discussions at such a workshop

### PyHEP

- Re-start of topical meetings on October 6th.

### Software Training

- Organised the first [virtual Software Carpentry workshop](https://indico.cern.ch/event/1058873/) 25-27 Aug 2021 (75 participants registered)
  - Software Carpentry workshops (SCW) will be organized every ~3 months.

- First publication on Software training (based on vCHEP 2021 contribution) submitted (1 Aug 2021) to CSBS  - Springer (Computing and Software for Big Science) [arXiv version](https://arxiv.org/abs/2103.00659))

#### 3rd HEP C++ Course and Hands-on Training

- [Event](https://indico.cern.ch/event/1019089/) is running this week. 75 students attending. Another 90 on the waiting list. With this course we will have trained 200 students since October 2020.
- Many thanks to all lecturers and mentors!!!
- Meeting notes that we should improve the connection between the C++ teaching and the WG.

### Event Generators

- Not much to report. Very little action in August.
  - Main focus now is on implementing comments received on the LHCC document and recirculating to the WG.
  - "Taming the accuracy of event generators" workshop last week, will be interesting for us to look at discussions: <https://indico.cern.ch/event/999271/>

### Frameworks

- Will (hopefully) have a meeting next week after a longer hiatus. (<https://indico.cern.ch/event/1072798/>) With the intention of going back to regular meetings in the autumn once again.

---

## AOB

### HSF Domain Name

Ticket still open, no recent movement.

### SIDIS COST Proposal

We are currently working on a funding proposal (EU COST) in the context of the "Software Institute for Data Intensive Sciences", aiming to bridge the gap between computer scientists and natural science software engineers. The "grand theme" of the proposal will be around the topic of "software sustainability".

For a success proposal it is useful to include participants also from "inclusive target" countries (mostly eastern European countries). In case you have contacts in this direction please get in contact with Graeme or Stefan.

### Next Meeting

We restart our regular 2 week cadence, next meeting 16 September.
