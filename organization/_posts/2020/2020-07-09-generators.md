---
title: "HSF Generator Meeting #9, 9 July 2020"
layout: meetings
# {{page.title}}
---
# HSF Generator Meeting #9, 09 July 2020

*This notebook is used to record the minutes of the HSF Generator WG meetings. These are archived after each meeting onto the [HSF Website](https://hepsoftwarefoundation.org/organization/minutes.html). To edit this page, please login with your GitHub account!*

*Agenda: <https://indico.cern.ch/event/936481>*

Present: 
- Remote: A. Valassi, E. Yazgan, O. Mattelaer, J. McFayden, H. Schulz, G. Singh Chahal, A. Grohsjean, L. Sexton-Kennedy, K. Ostrolenk, R. Frederix, S. Frixione, A. Buckley, W. Hopkins, J. Butterworth, T. Childers, J. E. P. Cortezon, M. Schulz, T. Martin, M. Grazzini, J. Cuevas, W. Kilian, M. Schoenherr, Q. Li

Apologies: -

## Introduction 
Speakers: A. Valassi, E. Yazgan, J. McFayden.

- Stefano F.: What's the fraction of weighted events in CMS and ATLAS? Need to fairly compare cost of unweighted events and cost of weighted events. Negative weights is not in the same category as weighted events.
    - Matching/merging can be considered as weighted and those ones weighted from the start 
        - Josh(ATLAS)/Efe-Alexander(CMS): but experiments don't have weighted ones from the start. 
        - Alexander: Bias weights may not be considered as the weights we're discussing here. 
- Stefano F.: typo in slide 10 (now fixed in a new version of the slides): (1-2r^2) -> (1/1-2r)^2
- For the points discussed in the intro, it would be useful to have feedback via email as well.  

## ECHEP (Efficient Computing for HEP)
Speaker: A. Buckley.

- "Aim to complement HSF"
- "low scale physics can also be _expensive_ when scaled up: heavy quarks, exclusive hadron production & decay channels, colour reconnection algorithms".
- Evgen duplication between experiments: Any current HSF effort?
    - Efe: Follow up on the top samples of ATLAS and CMS.
    - Stefano: Experiments may have different needs and requests because of different physics. Physics considerations should have the priority, physics groups should be involved.
        - Efe: it should still be possible to have some common generation (e.g. large SM samples) if experiments agree on physics. 
- PDFs
    - "LHAPDF 6.3 introduced caching"
        - Dima Konstantinov's code was the starting point
    - Andrea: Somebody needs to look at PDFs on GPUs.
        - Olivier: NNPDF started some work on this
        - Marek: Need uniform code throughout differen t PDFs (??)


## CPU performance improvements in MadGraph 
Speakers: K. Ostrolenk, O. Mattelaer.

- Express MEs in terms of spinors instead of Lorentz vectors --> Computation propto N instead of N^2. 

- Slide 7: matrix element speedup is only part of the calculation. The more complex the process, the more of the matrix speedup appears as overall speedup.

- Eventually (~1 month timescale), it may be possible to have speed increase by x2 for ttgg. 

- R. Frederix: Memory increase?
    - Kiran: negligible

- Liz: What is presented is for LO processes. Is it applicable to all orders? 
    - Kiran: should be possible at higher orders
    - Olivier: not possible for processes with loops but OK for all others. 

## Status of NNLO ttbar calculations
Speaker: M. Grazzini.

- Current major bottleneck: two-loop amplitudes ("charting new territory")
- MATRIX MC generates parton level weighted events
    - will include EW corrections and top quark decays in the future. 
- NNLO matching
    - NNLOPS (gg->H, DY, VH, WW)
        - Requires reweighting, more complex for more complicated processes
    - MINNLOPS 
        - no reweighting. 
        - can be extended to ttbar and work is ongoing. 
    - UN2LOPS
    - GENEVA
        - DY, WH
    - Parton Shower in all these cases is still LL but still better due to improvements from having full NNLO.  
- Andrea: is matching to parton showers the missing piece for this to be used in experiments?
    - Massimiliano: Yes. For simple processes there are several methods. But none of these methods are extended to colorful final states. But ttbar shouldn't be very difficult provided that shower is still LL. 
- Andrea: compared number to Top++, but this is a very different program?
    - Massimiliano: yes, Top++ is just a total cross section calculator, it gives you a cross section in 10 seconds. MATRIX is a MC that can give you weighted (and unweighted) events.
- Alexander: What are the plans for decay? Which calculation will be NNLO accurate?
    - Massimiliano: Czakon et al. have some results. What is planned to be achieved in MATRIX is to have decay at NNLO. 
- Olivier: did you try to optimize the speed and how much gain you expect in the future?
    - Massimiliano: The main problem is that our method is non-locality. Subtraction is delicate. 

## AOB

Next meeting will normally be in two weeks, on July 23.
