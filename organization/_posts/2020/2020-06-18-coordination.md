---
title: "HSF Weekly Meeting #188, 18 June 2020"
layout: meetings
---

# {{page.title}}

Present/Contributors: Graeme Stewart, Michel Jouvin, Lukas Heinrich, Benedikt Hegner, Stefan Roiser, Agnieszka Dziurda, Kyle Knoepfel, Caterina Doglioni, Pere Mato, Witek Pokorski, Paul Laycock, Eduardo Rodrigues, Sam Meehan, Antoine Pérus, Chris Jones, Giles Strong, Liz Sexton-Kennedy, Philippe Canal, Sudhir Malik, Daniel Elvira, Vassil Vassilev, Kilian Lieret

## News, general matters

### Proposal on Differentiable Analysis / Computing

> Over the last decade “Deep Learning” has been one of the driving paradigms in Machine Learning and its application in High Energy Physics data preparation and analysis. Neural network architectures have evolved significantly into a growing collection of re-usable building blocks such as recurrent, stateful, or attention units, which can then be freely composed into larger networks that can then be jointly optimized. Optimization often occurs through gradient-based methods, such as backward propagation; the differentiability of such modules is an important characteristic. Based on that, a new paradigm of “differentiable programming” is emerging that utilizes automatic differentiation techniques to formulate optimizable algorithms, with common elements such as control structures and loops. In high-energy physics, activity in this area is gaining increasing consideration based on techniques such as INFERNO, neos, MadMiner, and others. This activity area seeks to provide a forum for research and discussion on techniques and software to implement HEP-specific differentiable building analysis blocks.

Application of these techniques is wider than just analysis, e.g., error propagation in reconstruction.

Mattermost (everyone welcome) to discuss projects:

- <https://mattermost.web.cern.ch/signup_user_complete/?id=zf7w5rb1miy85xsfjqm68q9hwr>

(this does work for non-CERN people, but you might need to create an lightweight account).

Meeting approved this a new Activity for the HSF, **Differentiable Computing**. Use the HSF platform to look for cross-cutting topics with, e.g., Analysis and PyHEP WGs.

### Technical Note on Best Practices for HSF Projects

Current Draft:

- <https://github.com/HSF/documents/blob/master/HSF-TN/draft-2016-PROJ/draft-HSF-TN-2016-PROJ.md>

This has had a revamp and update and we would very much like to finish it now.

Comments and suggestions (and PRs!) before the next meeting please!

#### Project Template Tool

Reminder that we have an [HSF project template tool](https://github.com/HSF/tools) that helps setup some of these best practice points. 

If you think of a good way to improve this, please implement it and make a *pull request*.

### Computing and Software for Big Science

One of the editors of the [journal](https://www.springer.com/journal/41781) contacted us to ask if we would make a call for papers to the journal, which would help them reach their threshold for 2020 (important for the journal being indexed). Papers need to be accepted by November 2020.
- Development of CHEP papers might be a good candidate

### IRIS-HEP Blueprint Meeting on *Sustainable Software in HEP*

July 22: <https://indico.cern.ch/event/930127/>

Crucial issue for HSF and HEP. Nice set of talks being arranged from other communities, e.g., AstroPy and Carpentries, as well as people inside our community.

## LHCC Review of HL-LHC Software and Computing

There are some preliminary conclusions from the review as part of the LHCC minutes. More statements about event generators than any other aspect. They are generally positive about the role the HSF has played.

We do expect more details later from the panel.

## Alpaka Training

- Alpaka (heterogeneous API) training will take place as a [virtual event](https://indico.cern.ch/event/912156/).
- Reminder mail to be sent soon on the HSF mailing list (fixing last technical details):
    - Co-organised with SIDIS, openlab, CASUS
- Date settled: June 29 - July 3
    - Monday - Friday, 9.00 - 10.30 CEST

## Dark Matter Test Science Project (ESCAPE) updates

Caterina, Graeme, Xavier, Pere, Tommaso (and others, including Lukas Heinrich and Sam Meehan on the ATLAS side) involved in discussions to make the "ESCAPE Dark Matter Test Science Project" (=review and implementation of software pipelines for different dark matter experiments) part of a proposal for the European Open Science Cloud [INFRAEOSC-03-2020](https://www.eosc-portal.eu/infraeosc-03-2020-integration-and-consolidation-existing-pan-european-access-mechanism-public). 
   * If successful, some postdocs from CERN and other institutes will join up to work on this, with a link to HSF. 
   * Work plan outlined very roughly so far, but there is a lot of room for feedback to make this project actually useful (and how to use this platform to make work on tools & pipelines more recognized career-wise).
   * Slides if you want to know more in broad terms: [link](https://cernbox.cern.ch/index.php/s/6iFibyWVHReeBk1).

## Working Group Updates

### Data Analysis
- Some problems trying to converge on a date for the next meeting (follow up from the DOMA-Analysis meeting), we will resort to doodle now that we have (nearly!) finalised speakers.
  - Theme is a B-physics focus (LHCb and Belle II) with contributions from CMS and ATLAS that also include exotics / not-mainstream analysis.

### Detector Simulation
- Next to topical meeting next week on Wednesday 24th June at 4pm. Third (and last) of the series of meetings devoted to GPU usage in particle transport. 
  - The slides for the lightning talks will be available before the meeting and a document with live notes will be attached to the agenda for people to ask questions before and/or during the meeting. 

### Reconstruction and Software Triggers
- Today's meeting (17h, CERN time):
    - [“Allen: the LHCb HLT1 trigger on GPU” by Dorothea Vom Bruch](https://indico.cern.ch/event/929836/)
- In the pipeline: website reorganization with projects, following up on Graph networks for tracking, meetings after the summer


### PyHEP
- [PyHEP 2020 virtual workshop](https://indico.cern.ch/e/pyhep2020):
  - So far about 15 abstracts submitted and we are aware of more in the pipeline. Very healthy situation.
  - Deadline for abstract submission extended to June 22nd.
  - We are approaching 740 registrants!
  - Agenda actively being prepared.

### Software Training

- [See slides](https://indico.cern.ch/event/916411/contributions/3852668/attachments/2060079/3455432/hsf_training_1.pdf) for the update of WG activity.
- Captioning - sent mp4 files of the event to the company (takes ~1 week to turnaround)
- FNAL will offer a C++ class (last year has 60 people; attendance dropped from 50->30 through the week). This time will change a nominal fee to try and increase commitment. Virtual event, spread over a few weeks, to give more time for exercises. Discuss in training meetings the format. Not clear if the tutor would be able/willing to put the material into the proposed HSF lessons template.

### Frameworks

- We are still trying to identify someone to discuss the Gaudi multi-threading scheduling mechanisms.
- We are also working to schedule a talk regarding LHCb's Allen framework. Thanks to Agnieszka for putting us in touch with the Allen team.

---

## Workshops

### New Architectures, Portability, and Sustainability

Feedback meeting was yesterday (<https://indico.cern.ch/event/925974/>), but was not very well attended (~20 people)
- General agreement that the virtual workshop was a success: allowed useful discussions that will be followed up in topical meetings organised by the WGs
- Summary and outcomes [document](https://docs.google.com/document/d/1ujwMhFTwxy3TAe8jKpvHvT1TB-ZXv1s7BolcfNKgqJA/edit?usp=sharing) has been prepared 

Good participation in the survey: 34% of the registered people (75 out of 221)
* People attended sessions out of their main area of interest
* Having presentations a few days in advance was important: 2/3 reviewed them
* Strong preference for live presentations over recorded ones
* Having a notebook where people can ask questions in advance and during the presentation seen as very useful: in fact something to consider even for F2F meetings
* 2 hour session format seen as the best compromise for a virtual event: important, even more than in a F2F meeting, to stick with the scheduled time. 50/50 between presentation and discussion is a good balance.
* Virtual events have a role to play in the future once the COVID crisis is over, as one collaboration tool: lower barrier for participation than a F2F meeting involving travelling.
* Virtual events don't replace F2F meetings: don't allow the informal interactions that are often an important part of the meeting value.
  * Enabling remote participation as a first class one and not as a backup solution during F2F meetings needs to be considered for future F2F events

Next WLCG/HSF event: no possibility for a F2F one this year, date foreseen in September are too early for another virtual workshop
* Current proposal: a virtual workshop in November: 19-20 + 23-25 marked as an option in the calendar
  * The only free days before end of 2020
  * Thursday 26 is Thanksgiving so 25 may be ruled out
  * Starting to discuss possible topics but also the idea to open a call for contributions for part of the workshop
  * Feel free to send your ideas to <wlcg-hsf-workshop-organisation@cern.ch>

Lund is all "unbooked", but they will welcome us if we want to come back in 2021!

## AOB

### Website Update

Significant clean-up of broken and outdated links was done on the website. We are almost back to a clean bill of health, except for some strange issues to do with DESY's Indico.
- Accesses from Travis get `403 no error` errors (ironic!)
- DESY support desk were very responsive and helped verify there are no IP blocks from their side

As part of this cleanup we deprecated the old HSF Knowledge Base
- Had been down for a while
- But it never gained the traction we hoped for anyway
    - Continue to work with ESCAPE team on their software catalogue as an eventual successor

### Indico -> HSF Calendar Sync

Significant progress in automating the synchronisation of HSF Indico Events to the HSF Google Calendar thanks to Stefan's efforts:
- <https://github.com/HSF/hsf.github.io/issues/726>
- script at <https://github.com/HSF/merge2gcal> 

### Next Meeting

- Next regular meeting slot is 2 July
