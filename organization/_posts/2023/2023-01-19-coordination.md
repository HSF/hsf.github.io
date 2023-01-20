---
title: "HSF Coordination Meeting #242, 19 January 2023"
layout: plain_toc
---

## Attending

Present/Contributing: Graeme Stewart, Krzysztof Genser, Oksana Shadura, Marc Paterno, Torre Wenaus, Nicole Skidmore, Liz Sexton-Kennedy, Dorothea vom Bruch, Kyle Knoepfel, Markus Diefenthaler, Efe Yazgan, Valentin Volkl, Stefan Roiser, Matti Kortelainen , Patrick Gartung, John Chapman, Juraj Smiesko, Matthew Feikert, Nathan Brei, Nick Smith, Paul Laycock, Philippe Canal, Vakho Tsulaia, Allie Hall, Ben Morgan, Caterina Doglioni, Jim Pivarski

Apologies/Contributing: Benedikt Hegner, Eduardo Rodrigues

## News, general matters, announcements

**Happy New Year!**

### Analysis Ecosystems II Workshop Report

Is now available on [arXiv:2212.04889](https://arxiv.org/abs/2212.04889).

N.B. We should continue to occasionally review progress on the outcomes and follow-up points.

### Pre-CHEP Workshop

We have confirmed with WLCG colleagues and LHC computing coordinators the two topics for a [pre-CHEP workshop](https://indico.cern.ch/e/wlcg-hsf23) on 6-7 May 2023 in Norfolk, VA.

- Analysis Facilities
  - Based on the findings of the AFF group (which we asked to draw conclusions after 12-18 months of work).
  - How do workloads evolve? How do sites adapt their offerings? What are the benchmarks of success?
- Non-x86 Computing
  - Increasingly diverse computing architectures at sites, both in CPU flavours (ARM, PowerPC) and accelartors (GPUs, mainly, from different stables).
  - Readiness of experiments to adapt to this new environment, covering development, building, validation, workflow management, etc.

Still to follow-up on remote participation options (the CHEP venue contract was signed pre-COVID), but we do hope people come in-person.

Scientific organising committee will meet next Monday (HSF AFF coordinators + WLCG people).

### Letter of Cooperation Request

Graeme and Mike Sokoloff discussed after our December 8 meeting and Mike prepared an [abbreviated public text](https://drive.google.com/file/d/1plY9AkUIg1IKX1N5UPcDfWMVFb3ifi7L/view?usp=share_link) of the NSF proposal to develop massively parallel and high-dimensional fitters.

With that in place we signed the [letter of cooperation](https://docs.google.com/document/d/1wnrbIw4Dv_VgWOleBRkbRddaFAtQ2wRnmqUMrftfnBg/edit?usp=share_link) (in the very standardised NSF format!).

### Google Summer of Code, 2023

Google Summer of Code for 2023 is starting!

This year Benedikt will head up the organising team. After many years Andrei and Antoine step down. *Huge thanks to them for their work!*

**We therefore urgently need two people to join Benedikt at the helm of GSoC for the HSF.** This is a very valuable service for the community and it much appreciated by all of us, so please consider volunteering.

**For projects** we need to have proposals available by *7 February* - it's not long. Please start thinking about this now!

Programme allows for long/short contributions. GSoC people do not have to be students any more. However, note we had our highest failure rate last year (5/27), so we probably need to put extra effort into the pre-selection process.

## Working Group Updates

### General

We are proceeding well with WG convenerships for 2023. A few WGs are not quite concluded yet (Data Analysis and Software Trigger and Reco), but should converge soon.

We are very grateful to all the conveners, continuing, joining or stepping down, for their contribution to the community through the HSF. **Thank you!** We hope that outgoing conveners remain active in the groups, even if relieved of specific responsibilities.

Today we shall review 2022 and discuss plans for 2023 with 4 of the groups. The other WGs we shall cover next meeting.

#### General HSF Activities

See slides attached to the [agenda](https://indico.cern.ch/event/1225007/).

#### Meetings

*Reminder:* Please try and book meetings in Indico at least 2 weeks in advance!

That way they go into the calendar early and they will be included in the weekly email announcement that goes to HSF Forum.

### Data Analysis

- Nicole Skidmore, LHCb (Continues)
- Nick Smith, CMS (Joins)
- Stephan Hegebroek, ATLAS (Steps down)
- Allison Hall, CMS (Steps down)

(1 convener position still under discussion)

- News:
  - Paper on experiment on-boarding is under development
  - CHEP talk accepted

### Detector Simulation

- Krzysztof Genser, Mu2e (Continues)
- Sandro Wenzel, ALICE (Joins)
- John Chapman, ATLAS (Joins)
- Kevin Pedro, CMS (Steps down)
- Ben Morgan, ATLAS (Steps down)

See slides attached to the [agenda](https://indico.cern.ch/event/1225007/).

### Reconstruction and Software Trigger

- Christina Agapopoulou, LHCb (Joins)
- Andi Salzburger, ATLAS (Steps down)
- Jin Huang, sPHENIX (Steps down)
- Dorothea vom Bruch, LHCb (Steps down)

(2 convener positions still under discussion)

### PyHEP

- Oksana Shadura, CMS/IRIS-HEP (Continues)
- Eduardo Rodrigues, LHCb (Continues)
- Jim Pivarski, IRIS-HEP (Continues)
- Matthew Feickart, ATLAS (Joins)

See slides attached to the [agenda](https://indico.cern.ch/event/1225007/).

PyHEPdev looks like a great initiative.

### Software Tools and Packaging

- Valentin Volkl, FCC (Continues)
- Patrick Gartung, CMS (Joins)
- Henry Schreiner, IRIS-HEP (Joins)
- Serhan Mete, ATLAS (Steps down)
- Marc Paterno, DUNE (Steps down)

### Event Generators

- Markus Diefenthaler, EIC (Continues)
- Efe Yazgan, CMS (Continues)
- Phil Ilten, LHCb (Joins)
- Josh McFayden, ATLAS (Steps down)

See slides attached to the [agenda](https://indico.cern.ch/event/1225007/).

Standards would be very interesting. No detailed discussions yet on APIs or specific needs. This came out of an MC4EIC discussion, where specific nuclear generators are used, but they lack many important features found in generators like Sherpa and MG5 (matching, merging, ...).

Workshop on computational efficiency in generators would be welcome again. CMS meeting that discussed this, so there is interest. But how can we engage them better.

Our mailing lists might well be a bit tired now, given their origins in the CWP process.

### Frameworks

- Kyle Knoepfel, Neutrino Platform (Continues)
- Vakho Tsulaia, ATLAS (Continues)
- Benedikt Hegner, FCC/Key4hep (Continues)
- Nathan Brei, EIC/JANA2 (Joins)
- Matti Kortelainen, CMS (Steps down)

See slides attached to the [agenda](https://indico.cern.ch/event/1225007/).

New language feature presentations were very popular last year - they are certainly cross-cutting and of general interest.

### Software Training

- Wouter Deconinck, EIC (Continues)
- Kilian Lieret, IRIS-HEP (Continues)
- Alexander Moreno, Theory (Joins)
- Jason Veatch, ATLAS (Joins)
- Michel Hernandez Villanueva, Belle II (Steps down)
- Sudhir Malik, CMS (Steps down)

## Other Interest and Activity Areas

### Compute Accelerator Forum

- 2023 Calendar
  - [Madgraph5_aMC@NLO](https://indico.cern.ch/event/1207838/), 8 February
  - [Hepix Benchmarking](https://indico.cern.ch/event/1207839/), 8 March

- Do get in touch with Graeme, Ben, Stefan if you have an idea or a topic to present

### Software and Computing Roundtable

- The ["Year in Review" event](https://indico.jlab.org/event/675/#b-3493-year-in-review-and-2023) with contributions from the HEP Software Foundation, Brookhaven National Laboratory, and Jefferson Lab was on Tuesday,
  - Graeme gave the HSF talk, summarising events and workshops that we had last year, GSoC, Training, etc.

---

## AOB

### Next Meeting

The next meeting will be on [2 February](https://indico.cern.ch/event/1225008/). We shall complete our overview of 2022 and planning for 2023.
