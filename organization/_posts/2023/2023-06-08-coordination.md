---
title: "HSF Coordination Meeting #251, 8 June 2023"
layout: plain_toc
---

## Attending

Present/Contributing: Graeme Stewart, Kyle Knoepfel, Benedikt Hegner, Pere Mato, Alex Held, Mason Proffitt, Nicole Skidmore, Claire Antel, Patrick Gartung, Uwe Hernandez, Vangelis Kourlitis, Krzysztof Genser, Nick Smith, Michel Jouvin, Wouter Deconick, Stefan Roiser

Apologies/Contributing: Eduardo Rodrigues, Efe Yazgan

## News, general matters, announcements

### LHCP Presentation

Vangelis Kourlitis presented a [talk](https://indico.cern.ch/event/1198609/contributions/5370078/) on *HL-LHC and Beyond Computing Challenges*.

Questions raised regarding:

- ATLAS - Google Cloud Platform project and future
- Common fast-simulation software à la ACTS
- CO2 emissions of our disks usage

- *Discussion:* disk energy consumption is much less than CPU. See [A holistic study of the WLCG energy needs for the LHC scientific program](https://indico.jlab.org/event/459/contributions/11499/attachments/9236/14205/WLCGEnergyNeedsCHEP2023.pdf) talk at CHEP2023 (slide 9).

### LHCC

Alessandra Forti, one of the Analysis Facilities Forum co-conveners, presented the status of Analysis Facilities in the community ([slides](https://indico.cern.ch/event/1225017/attachments/2552956/4612708/20230605_LHCC_AF_progress_report-8.pdf) attached).

There was a very productive discussion between the referees, the experiments, WLCG and HSF at the special session.

LHCC thanked the Analysis Facilities Forum for their work bringing the R&D around analysis facilities into the light.

In the whole community, we should take care to balance the R&D with production activities at the sites. Modernising infrastructure, helped by this type of R&D, is already a valuable outcome.

To demonstrate the new analysis facility concepts work, they need to be tested on representative used cases *at scale*. LHCC asks the experiments to provide a document on analysis use cases, which can be matched to AFs, then using this to develop benchmarks.

- The exact parameters of this document will come later, in consultation with the LHCC's HL-LHC review committee.

*Long discussion on this point, we conclude that the LHCC are positive about the R&D and would like to get more formal engagement from the experiments, folding these studies into HL-LHC planning. We think the "concerns" are not new, but this actually means that we are investigating the right topics and sending the right messages.*

### Google Summer of Code, 2023

The projects have started and students are working. Would like to find a person to attend the mentors' summit meeting and discuss the procedure for that.

If people need access to CERN resources contact Yasemin, the EP-SFT secretary.

Want to have an early meeting with the students, not just at the end of the coding period.

## Working Group Updates

### Data Analysis

- Planning for a meeting focused on Open Data from LHC experiments on July 3rd, 15:00 CET (now drafting emails to identify speakers).
- Considering possibility of a talk on Julia following the Julia white paper, does that sound of interest?
  - Yes, we think that is a good idea
    - Could have some generic Julia info + dedicated HEP libraries + pointer to new HSF Julia group

### Software Training

- Most recent software basics carpentry training: 18-19 May
  - 150 registrations -> 65 participants through the end
  - Lessons learned: slack for online discussions work well; ssh keys for github interaction, learners on WSL need more attention
    - Little things go wrong for them and it's enough to trip up beginners
- HSF Training materials now instrumented with Plausible web analysis
  - Initial look at first week of data: many deep link arrivals into modern cmake training, not many visitors from curriculum landing page
  - Will work with DAWG to integrate links to HSF training resource links better into experiment-specific training materials
- Two training fellows actively working on:
  - REANA training evaluation and improvement
  - pytest training development
- Next software basics carpentry training: 12-14 July
- Further into the future:
  - Analysis Preservation training workshop: mid-September
  - Matplotlib training workshop: mid-October


### Software Tools and Packaging

- Hope to have Adam Stewart, the person who maintains Python package packaging in Spack, come to CERN in September and give a talk. He is starting a postdoc at Techical Univerity of Munich.

### Detector Simulation

- Held a meeting dedicated to Geant4 physics models and event generators on June 5th: <https://indico.cern.ch/event/1276128/>
   - Quite good attendance, 19 people in total; Both from the detector simulation and generator community. (Several other meetings prevented more people from attending.)
- Still following up on possible contributions on Geant4 cuts/optimizations implemented by experiments (Two identified)
- Still following up on possible contributions on Geant4 Physics extensions that experiments have developed (One identified)

### Frameworks

- CMSSW talk on incorporating Alpaka into framework jobs  has been rescheduled for [28 June](https://indico.cern.ch/event/1281987/).

## Other Interest and Activity Areas

### JuliaHEP

- The paper *Potential of the Julia programming language for high energy physics computing* was submitted Tuesday to the Computing and Software for Big Science journal. You can find the preprint on arXiv: <http://arxiv.org/abs/2306.03675>.
  - Feedback is very positive so far.
- Some of us met last week to discuss the **creation of a new JuliaHEP working group** in HSF. Decided on the following:

  - The following people volunteer to be the conveners of the new working group:
    - Tamás Gál (Erlangen Centre for Astroparticle Physics, Erlangen-Nurenberg, Germany)
    - Alexander Moreno (Universidad Antonio Nariño, Ibagué, Colombia)
    - Uwe Hernandez Acosta (Center for Advanced Systems Understanding, Görlitz, Germany)
    - Pere Mato (CERN, Switzerland)
  - Start organizing the first JuliaHEP workshop
    - 6-9 November 2023 at ECAP (Erlangen Centre for Astroparticle Physics)
  - Start entry point documentation for JuliaHEP at <https://www.juliahep.org>
  - Fill in [Google Doc](https://docs.google.com/document/d/19Q3bWnumKLkfG4FyhLidv3IGhQq01azFQzvInL-Ty8o/edit#) with projects we are interested to do
  - Sign up to [Discourse](https://discourse.julialang.org) and Slack if you aren't already!
  - Move to the JuliaHEP mailing list: <julia-hep@googlegroups.com>

- Created a [page](https://hepsoftwarefoundation.org/workinggroups/juliahep.html) in the HSF web side with the information on JuliaHEP

### Compute Accelerator Forum

Next week we will hear from the DOE funded HEP CCE project, which is now reaching the end of its first funding phase.

- Charles Leggett will present results on portable paralellisation layers
- Peter Van Gemmeren will present results on high-performance I/O

[Meeting will be held jointly with ATLAS Core Software in Salle Curie](https://indico.cern.ch/event/1264297/), Wenesday 14 June at 16h30.

### Visualisation

The [Phoenix Event Display](https://github.com/HSF/phoenix) will be featured in the next CERN Courier.

---

## AOB

### Website

Benedikt started an [issue in GitHub](https://github.com/HSF/hsf.github.io/issues/1411) to gather ideas about reorganising and revamping the website to better reflect our areas of actual activity.

### Next Meeting

The next meeting will be, on [22 June](https://indico.cern.ch/event/1225018/).

Please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing this or one of the future coordination meetings.
