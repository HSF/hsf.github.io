---
title: "HSF Coordination Meeting #256, 14 September 2023"
layout: plain_toc
---

Present/Contributing: Claire Antel, Benedikt Hegner, Liz Sexton-Kennedy, Sandro Wenzel, Kilian Lieret, Eduardo Rodrigues, Michel Jouvin, Caterina Doglioni (joined late)

Apologies/Contributing: Graeme Stewart

## News, general matters, announcements
 
### LHCC

#### Software Representatives

At the last WLCG MB Eduardo Rodrigues, who we nominated from the HSF, was appointed as the second WLCG software representative, along with Predrag Buncic from EP-SFT. 
Congratulations to Eduardo!

#### September LHCC

Kilian Lieret presented the status of training in HEP to the LHCC for the September meeting. See slides attached to the agenda.

#### RRB Reports

The text for the RRB report (covering 20 March - 21 September) is due 22 September. Graeme and Predrag are organising inputs from the projects and the HSF. 
Graeme will write the HSF report, so if you have anything you want to highlight please let him know.

## Working Group Updates

### General

#### Website banners

Remember we have the ability to put event banners on the HSF website. All it requires is a markdown file with the event data. 
See, e.g., files [here](https://github.com/HSF/hsf.github.io/tree/main/announcements/_posts/2023).

#### Meetings

*Reminder:* Please try and book meetings in Indico at least 2 weeks in advance!

That way they go into the calendar early and they will be included in the weekly email announcement that goes to HSF Forum.

### Software Training

- [Software Basics](https://indico.cern.ch/event/1316853/), 13-14 November

#### C++ Course and Hands-on Training

- [Advanced C++ course](https://indico.cern.ch/event/1266628/) at CERN will run in October
    
### Detector Simulation

- [Next working group meeting](https://indico.cern.ch/event/1321071/) scheduled 18.09.2023 - 17:30 (CERN time)
    - topic is discussing approaches / sharing knowledge about Geant4 client-side tuning (step-count reduction) 
    - 2 speakers: Walter Hopkins (ATLAS), Benedikt Volkel (ALICE)

### Reconstruction and Software Trigger

Yesterday's topical meeting 
- Yesterday, had topical meeting on ["zero-waste computing"](https://indico.cern.ch/event/1320368/) by Ana-Lucia Varbanescu (performance engineer) and Stephen Swatman (PhD student on HP computing & HEP applications) 
   - Interesting, very general overview presentations with good attendance: 38 people connected. 
   - Recording available: uploaded to `CDS Videos`and linked to agenda

Future talks
- Thinking of having a follow up session on "zero-wast computing" where we invite experiments (so far have LHCb candidate) to show case projects involving algorithm performance optimisations & assessments. 
  - Will nicely compliment yesterday's overview talks. 
  - Date, details to be defined. 
  - (Let us know if know of "algorithm optimisation" projects in other experiments, that we can invite presentations on.)
- Got confirmation that 2 speakers from Belle II available to give talk on timing in tracking (from (1) detector and (2) algorithm perspective).
   - To define exact date next, aiming for October. 

### PyHEP
- Abstract submission deadline for PyHEP 2023 ended yesterday. We got a healthy number of submissions, now under review.
- PyHEP.dev 2024: this second iteration of these new in-person developers workshops will be hosted by RWTH Aachen University (ErUM-Data-Hub team, a "central networking and transfer office for the digital transformation in the exploration of universe and matter").
    - Many thanks to them for the spontaneous proposal!

### Frameworks

Regrouping after the summer, will get more updates next meeting. 

## Other Interest and Activity Areas

### JuliaHEP

Conference organization going on at the [Erlangen Centre for Astroparticle Physics (ECAP) in Erlangen](https://indico.cern.ch/e/juliahep2023). More room for local/in-person participants. 

### Compute Accelerator Forum

- Yesterday, a presentation on [RISC-V architecture](https://indico.cern.ch/event/1264300/).
- Next meeting will be 11 October, with an [Introduction to the D programming language](https://indico.cern.ch/event/1264301/)

### Software and Computing Roundtable

Plan to restart these meetings in September.

---

## AOB

### Technical Note on Project Best Practices

We added a [new section](https://github.com/HSF/documents/pull/148) to the project TN on [CITATION.cff files](https://citation-file-format.github.io).

It would be good if people took 5 minutes to [review the advice](https://github.com/HSF/documents/blob/master/HSF-TN/2020-01/HSF-TN-2020-01.md) there and suggest any additions before we publish the update.

### Call for US panel of computing

See e-mail to the coordination list, excerpt:

> Dear colleagues,
>  
> The DPF Executive Committee is following up on the request from the Snowmass Computing Frontier (CompF) to establish a Coordinating Panel for Software and Computing (CPSC). The DPF will do this by assembling a Formation Task Force (FTF) to write a report that will serve as the governance document for the CPSC.  The charge to the FTF is attached.  The charge also explains briefly how the DPF will move forward with the submission from the FTF to establish the actual CPSC. 
>  
> The FTF is an ad hoc body that will work for approximately three months to produce its report. The expected contents of the report, which should be no longer than 50 pages, is given in the charge.  It will require significant effort during this period to gather input from the community and produce a high-quality result. The mandate of the FTF will conclude when the DPF Executive Committee accepts its report.  
>  
> We are now requesting nominations for 12-15 people to serve on the FTF. People are encouraged to read the charge and to nominate colleagues, including themselves, who can carry out this challenging task.  

Panel charged with writing a report on how to set up this Coordinating Panel for Software and Computing (basically: mandate, how panel gets selected, what is the distribution of people across labs/universities...). This is a sub-panel of Division of Particles and Fields (DPF). 

This is answering a request from the Snowmass computing group (Daniel Elvira was in the list of proponents) to form something similar to the detector R&D panel (CPAP). 

DOE/NSF and other government agencies look at this for advice, people on this panel set up workshops to develop Basic Research Needs (which have funding calls attached). 

ECFA (ICFA?), APPEC, NuPECC are establishing similar panels after  [the Bologna JENA workshop](https://agenda.infn.it/event/34738/), there will be a meeting end of November/beginning of December in Edinburgh to present a preliminary plan. Graeme is involved in one of these working groups. 

It would be good to have someone accustomed / participating in HSF to be writing this document, so that things can go hand in hand - but it's a lot of work. 

### Website

Benedikt started an [issue in GitHub](https://github.com/HSF/hsf.github.io/issues/1411) to gather ideas about reorganising and revamping the website to better reflect our areas of actual activity.


### Next Meeting

The next meeting will be on [September 28](https://indico.cern.ch/event/1225025/).

Reminder: please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing this or one of the future coordination meetings - we need volunteers from now until the end of the year!
