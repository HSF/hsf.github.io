---
title: "HSF Weekly Meeting #184, 9 April, 2020"
layout: meetings
---

# {{page.title}}

Present/Contributors: Graeme Stewart, Andrea Valassi, Pere Mato, Teng Jian Khoo, Caterina Doglioni, Ben Morgan, Kyle Knoepfel, Josh McFayden, Serhan Mete, Chris Jones, Efe Yazgan, Agnieszka Dziurda, Witek Pokorski, Eduardo Rodrigues, Paul Laycock, Michel Jouvin, Liz Sexton-Kennedy, Stefan Roiser, Andrea Rizzi, David Lange, Davide Costanzo, Horst Severini, Kilian Lieret, Maek Neubauer, Philippe Canal, Predrag Buncic, Antoine Pérus, Gloria Corti, Daniel Elvira

Apologies: Attila Krasznahorkay

## News, general matters

### COVID-19

There are a number of places where HEP is coordinating to help in the current situation:

* CERN Against COVID-19: <https://against-covid-19.web.cern.ch/>
* Science Responds <https://science-responds.org/>

We absolutely encourage HSF members to find useful ways to apply their talents!


## Google Summer of Code 2020

We need to reboot the GSoC Advisory Committee (last year it was Pere Mato, Pete Elmer, Michel Jouvin). See the [mandate](https://docs.google.com/document/d/17ifO0i4O5JsBVKkcx3j75Z_iW2bXFnCbqFB2YirlJQw/edit?usp=sharing). They should be able to rank the projects assuming we get less slots than projects we could run.
- Pere and Michel are available to reprise their role. Liz would be available, if Pete isn't.

News from GSoC Admins:

- We are working these days to gather the student proposal rankings from mentors, who were asked to provide feedback by April 16 the latest.
- As they answer, we go through their selected candidates proposals and make a quite detailed summary in a Google sheet, giving already recommendations based on the info we extract.
    - We tag already project proposals as qualified, reserve or disqualified, which can be used by the committee to make an educated guest of the number of slots we need
- As last year, we expect maybe few clashes or unclear cases that will need to be treated with more attention, but for the vast majority of projects there will be no additional investigation needed by the advisory committee compared to what we do already: Google gave us in the past all the slots we could fill...

- **We need the committee to be ready for the period of few days before April 21** (the deadline for slots requests), but not expecting major work needed on their side.
    - In case Google gives us too few slots compared to what we ask for (which we doubt) there will be more work after. Already now we know that there will be maximum 40 slots needed, but probably more like 35, and last year Google offered 34.

Q. Can projects with many good proposals be split in two? No, they can't.


## LHCC Review of HL-LHC Software and Computing

*Reminder*: LHCC will review software and computing plans for the HL-LHC, Amber Boehnlein (JLab) will chair. Five 20 page documents provided as input to the committee, from ATLAS, CMS, WLCG, DOMA and from *Common Tools and Community Software* (the HSF takes care of the later)

There will be a relatively short virtual meeting in the week of 18 May, with follow-up reviews later.

[HSF Draft Document](https://docs.google.com/document/d/1ai7m7kFyiGgl2tKralJKyPX6rlD9tffU7B6wPj_vpZU/edit?usp=sharing)

- This was released publicly on April 1st
- Now gathering feedback and comments
    - This was extremely active in the last week and (mostly) helpful comments were received, so thanks to commenters and to the WGs for responding and adapting to them
- In general, be pro-active at resolving discussions (they can be re-opened if needed)

[HSF review meeting](https://indico.cern.ch/event/904412/) will be Thursday 16 April, where points needing further discussion will be tabled

- Ask all WGs to gather issues that should be discussed (preferred mechanism? CodiMD or Google Doc? One document or many?)
    - Single Google Doc is the preferred option
    - This is a *one shot* document used only for next week's discussion

**Current list of open points for each section:**

### General

- Contributing authors list?
    - No
- Reference policy, it's very uneven right now
    - Yes, we should have these in the final version, please collect
    - BibTeX probably best for this (see LaTeX discussion below), it's a royal pain in Google Docs
- Document should be written in third person
    - Avoid "we"; ask a native speaker for advice if your passive voice constructions become unclear
- Please refer to the CWP as a starting point (that allows us to keep the document succinct)
- Final conversion to LaTeX (last week, but editing would need to be largely over by then)
    - Some suggestion this is a lot of work (Generator WG), but the CWP experience was ok...?
    - Graeme will have a first go at this

### Introduction

- Should we prepare an executive summary?
    - TBD, will ask for clarification
- Reminder that we align expected hardware gains with WLCG/ATLAS/CMS

### Event Generators
- Most comments now resolved (or at least have replies posted).
- We are also working on longer version of our section that we plan to publish as a separate document.


### Detector Simulation
- Did the first pass through all the comments, resolved a number of them
- Split the chapter into sections as suggested, will add one more section on experiments efforts to tune/speed up the simulation applications
- How to handled references? We would be happy to add a number of them
    - Yes, they should be added - see above
- Shall we discuss the (missing) funding or this will be handled at the global level of the report?
    - It's fine to identify missing effort


### Reconstruction and Software Triggers

- General question: should we focus on ATLAS/CMS? 
    - Probably, given HL-LHC focus; we will ask the reviewers for clarification
- Many comments (still expecting some more from LHCb / ALICE)
- We listed in the text a number of projects that were community-oriented (= had a public GitHub repo, were welcoming cross-collaborations + most of them have presented at HSF meetings)
    - some of them are collaboration specific / coming from a collaboration for the time being
    - these are not HSF-branded / sponsored projects
    - this made us think that we could also list them on our webpage (a previous wishlist from workshops / talking to collaborations), and others can ask to be represented
    - TODO: mention non-ATLAS/CMS projects exist as well (e.g. tracking for HI, neutrino projects that may have an impact on HL-LHC)
        - These should only be covered insofar as they could impact on HL-LHC
 
### Data Analysis

- Addressed a number of comments, mainly on the intro (which we had redrafted, but hadn't yet transferred into the common doc as there were details still being debated)
- Started adding some references, the lack of which prompted a number of comments
- A bit ATLAS/CMS-centric, hope ALICE/LHCb feedback helps us balance out
    - However, the focus is on HL-LHC, so this is ok (see above reco discussion)
- Getting on the long side, but we can aim to cut down later in the editing
- A few comments were on the role of this document in terms of guiding reviewers towards funding priorities, which might require some restructuring
    - One set in particular trying to push for consensus on specific solutions over the current broad exploration -- we don't think this is in our remit
        - Meeting agreed that we can't comment on this and should not have such in the document

### Conclusions

- There are a few suggestions of topics to cover already
    - Feeling that Quantum Computing is being pushed too hard and it's too early to make much of this
        - Agreed
    - OpenLab is important - encourage more links to industry? (They happen in different contexts in other FAs)
        - Yes, we will expand on this point
- We should focus on 12-24 month goals, in general

---

## Working Group Updates

### Detector Simulation
- need to prepare the next topical meeting

### Reconstruction and Software Triggers

- We had a meeting last week: 
  - <https://indico.cern.ch/event/903510/> 
  - this was 2nd meeting on multithreading and code optimization
  - ~20 people connected 
- Our next meeting(s) target: 
  - Heterogeneous architectures
  - Reconstruction for Long Lived Particles (LLP) 

### PyHEP
- We are reorganising the workshop, which is likely to be spread over 5 days, with shorter (than standard) daily sessions.
    - For info SciPy 2020 will happen as a virtual meeting.
- Other activities mostly paused at this moment.


### Software Training

- **Meeting** last week: <https://indico.cern.ch/event/904686/>
- Started to popuplate **github organization** <https://github.com/hsf-training/> with training modules (CI/CD from G. Stark, Awesome Analysis by S. Wunsch)
- **Webpage**: Drafted additional pages for overview over the modules/curriculum 
- **Virtual workshop** on analysis preservation/CI/CD scheduled for April 28th 

### Event generators

- Starting to prepare for our next meeting. Topics may include:
    - Exercising the EOS space we now have to share samples across ATLAS & CMS with new LHC Top WG sample production.
    - Recent plan to shower big HPC Sherpa sample on the grid within ATLAS
    - Docker image for using generators for benchmarking
    - Follow-up on GPU-porting activities
    - Status and Outlook on NNLO calculations

### Frameworks

We will continue/complete our survey of experiment frameworks next week with a presentation from Belle II. We also will discuss what could be targeted for the HSF/WLCG virtual workshop in May.

---

## Workshops

### HSF/WLCG 2020 workshop

21-25 September has been booked in Lund, but this is evidently still subject to later confirmation

### New Architectures, Portability, and Sustainability

[HSF WLCG Virtual Workshop on New Architectures, Portability, and Sustainability](https://indico.cern.ch/event/908146/)

> The HSF and WLCG have organised this virtual event to focus on the challenges and opportunities of new computing architectures. This is a critical and highly relevant topic for HEP where much progress is being made, but there remain many open questions to discuss.
> Adapting to the needs of the communty to host more virtual participation events we will hold this meeting over 3 days, from 16-18h each day, to maximise the opportunity to participate.
> Three themes will be addressed across the three days:
>     - Application Software
>     - Processing Frameworks
>     - Validation and Accounting (including Benchmarking)
>
> We will be exploring new ways to interact effectively during events like these, with more emphasis on having material available early and the opportunity to raise discussion points in advance.

Main speakers identified, inviting them now. The goal is to have public announcement of the virtual workshop and the preliminary agenda next Wednesday, after Easter and the next preparation meeting on Tuesday evening.

**We ask that people [register](https://indico.cern.ch/event/908146/registrations/)** so that we can gague the level of interest.

Prepared a [virtual meeting guide](https://indico.cern.ch/event/908146/page/20187-virtual-meeting-guide) to try to make the event work as well as possible, *more suggestions and feedback very welcome here* (we are treading new ground).

## AOB

### Next Meeting

- Next regular meeeting slot is 25 April
- Don't forget the LHCC Document review meeting next week!

*Happy Easter!*
