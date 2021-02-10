---
title: "HSF Weekly Meeting #187, 4 June 2020"
layout: meetings
---

# {{page.title}}

Present/Contributors: Graeme Stewart, Andrea Rizzi, Caterina Doglioni, Attila Krasznahorkay, Agnieszka Dziurda, Efe Yazgan, Kyle Knoepfel, Paul Laycock, Stefan Roiser, Mark Neubauer, Michel Jouvin, Witek Pokorski, Pere Mato, Serhan Mete, Ed Moyse, Benedikt Hegner, Philippe Canal, Serhan Mete, Teng Jian Khoo, Guy Barrand, Danilo Piparo

## News, general matters

### LHCC Referees Meeting

[LHCC referees meeting](https://indico.cern.ch/event/877841/) yesterday, Graeme presented the software report (thanks for feedback and input)

- Comment on workshop
    - Possible tension between live presentations and ensuring we stick to time (pre-recorded talks don't run over!)
        - Need discipline (chairs and speakers) for the presentation 'core' not to be over time; questions during the talk are fine, indeed part of the perceived advantage of live talks
- Questions on PyHEP
    - How to manage so many participants
        - If CERN Zoom trial is made official >500 people may be possible
    - The participant communities
        - LHC, non-LHC, sites, Belle II, DUNE, dark matter
        - Short discussion use of Python in core of DM experiments (XENON1T)

### Alpaka Training

- Alpaka (heterogeneous API) training will take place as a [virtual event](https://indico.cern.ch/event/912156/)
- Reminder mail to be sent soon on the HSF mailing list (fixing last technical details)
    - Co-organised with SIDIS, openlab, CASUS
- Date settled: June 29 - July 3
    - Monday - Friday, 9.00 - 10.30 CEST

## LHCC Review of HL-LHC Software and Computing

- Review took place 19 May, based on the [HSF input document](https://zenodo.org/record/3779250) and a short presentation
- Still waiting for the written feedback from the referees (general impression was quite positive, but we were asked to wait for the written report before discussing and responding)


## Working Group Updates

### Data Analysis
 - Meeting on non-mainstream analysis patterns postponed due to unavailability of speakers from many of the contacted experiments
 - Probably splitting in two sessions (one before summer, one after)
     - Attempted splitting based on topic (e.g. B-physics vs exotics), but does not fit different experiments' timelines

### Detector Simulation
- Topical meeting on 27th May devoted to GPU usage in simulation
    - Three very interesting presentations on successful application of that technology in specific domains (medical, optical photons, neutron transport)
- Next two meetings scheduled for 10th and 24th of June where we invite everybody to contribute with 'lightning talks' on ideas how we could use GPUs in HEP simulation


### Reconstruction and Software Triggers
 - Trying to converge on the next meeting (GPU related)
     - Right now planned for the 10th, but will possibly be moved to get speakers
     - The 10th would be a detector simulation conflict as we type, so one more reason to move :)
 - In the pipeline:
     - GitHub repo for graph networks for tracking
     - Update of webpages with info about projects coming from LHCC report


### PyHEP
- More than 550 registered for the [workshop](https://indico.cern.ch/e/PyHEP2020), which is proceeding as a virtual workshop on the extended dates July 13-17

### Software Tools and Packaging

 - Quite a lot of recent development in the HSF job monitoring tool, [prmon](https://github.com/HSF/prmon)
     - Adds monitoring of NVIDIA GPUs (percentage SM, GPU memory, number of GPUs)
     - Revisited the code and made many nice architectural improvements and enhancements
- Planning to hold a WG meeting "soon" (time TBD):
    - There are a number of topics to be discussed on the packaging side (Spack etc.)
    - We can also discuss the developments on the prmon side.


### Software Training

- There is [Virtual Pipelines Training](https://indico.cern.ch/event/904759/) this week

### Frameworks

- Nothing to report since the HSF/WLCG virtual meeting
    - Conveners will work to schedule next topical meetings, still likely related to multi-threaded scheduling.
- Was informally asked for input to the upcoming LHCb workshop on heterogeneous computing. Should work that into our schedule...

## Other Interest and Activity Areas

### Visualisation

Presentation on [Phoenix](https://github.com/HSF/phoenix) event display, see [Indico](https://indico.cern.ch/event/916410/) for slides

- What is the support model?
    - No one funds this beyond GSoC and open source volunteers
- Neutrino experiments mostly make their own displays, could be very useful for the LAr experiments
    - Good contribution model and cheaper than people rewriting again and again from scratch
- Implements many things we wanted to do from the CWP, +1!
    - Geometries are plugins; so could the data stream in (with suitable metadata?), and could then support time dependent geometry
    - Development work, but definately supported by underlying toolkit (in ATLAS case need to convert from custom geometry to something that can be understood by three.js)

---

## Workshops

### New Architectures, Portability, and Sustainability

[Indico](https://indico.cern.ch/event/908146/).

Some survey highlights:
- Slides in advance and notebook were liked
- Live talks strongly supported over pre-recorded talks
- Format was about what people wanted (duration, timeslot)
- We should be much more disciplined with time keeping
    - More important for virtual meetings
- Topics covered were supported as is posting videos of the event
    - Maybe we should also post to YouTube?
    - N.B. Indico access stats seem broken (woeful under-reporting)
- People want to see conclusions and outcomes
    - We are in the process of identifying these now
- Large support for continuing with virtual meetings in the future
    - But people want face-to-face meetings as well

Full feedback meeting will be *Wednesday 17 June, 17h CERN time*: <https://indico.cern.ch/event/925974/>

Planning next virtual event, **21-25 September** (so *save the date*).

## AOB

### Next Meeting

- Next regular meeting slot is 18 June
    - We plan to discuss a proposal for a new activity on *differentiable computing* (details will be circulated later)
