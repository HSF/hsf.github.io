---
title: "HSF Generator WG Meeting #21, 2 June 2022"
layout: plain_toc
---

Agenda: <https://indico.cern.ch/event/1155046/>

present: Zenny Wettersten, Andrea Valassi, Graeme Stewart, Olivier Mattelaer, Andrew Lifson, Juergen Reuter, Robert Schoefbeck, Walter Hopkins, Liz Sexton-Kennedy, Uwe Hernandez Acosta, Markus Diefenthaler, Efe Yazgan


* Source of speed gain: Simplified Lorentz structures and Gauge based diagram removal. 
* Only works for massless QED
* Not generalizable - every structure is implemented explicitly. 
* e+e- --> ngamma for n  [2,7]
    * For n >= 6 a factor of > ~10 faster than standard MG5_aMC

Discussion:
* Andrea: Slide 12: factor 2^n. How much you gain from Simplified Lorentz structures and how much from Gauge based diagram removal. 
    * ZW: 2^n is for Gauge based diagram removal. 
    * Olivier: Relative gains from diagram removal do not seem to line up with 2^n, is this because of some prefactor?
    * ZW: Partially because of the prefactor on the scaling, but this estimate should only hold as n -> infinity.
* Andrea: This is limited for LHC but next week there is a workshop for FCC for theorists and calculations. This formalism may be relevant there for such calculations. There will be a talk on ISR from S. Frixione. Agenda: https://indico.cern.ch/event/1140580/timetable/  
* Andrea: The code developed for massless particles. What would be the speed gain if not massless.
    * ZW: That depends on the situation. For internal particles massive (massive fermions), every fermion propagator adds a factor 2 to number of evaluations.
        * Andrew Lifson: Massive bosons not much difference. Fermion propagator (slide 9) will be more complicated. 
* Olivier: If you do ttbar, if you add gluons it is massless. Is it possible to combine the two, not-chirality for the top and then mix it with the chirality flow sector for the rest? 
    * ZW: Should be possible. Mixing should not be an issue, as long as the different methods are kept track of properly.  
* Andrea Valassi: helicity recycling that Olivier is working on. How much overlap is there with chirality flow for speed-ups?
    * ZW: The speed gains are independent. However, we may not see the same gains in helicity recycling because we will be evaluating fewer diagrams, so same structure appears fewer times. 
* Andrea Valassi: Helicity filtering something we are debugging these days. In the helicity formalism for each external particle there is some allowed helicity. Some of the helicity combinations give zero contributions that are excluded. By construction are you only using helicity combinations that give non-zero contribution?
    * ZW: Intuitively yes. 
    * Andrew Lifson: MG5_aMC is evaluating too much helicity, at least in standalone output. 
    * Olivier: This issue does not appear in MadEvent, where there is a threshold comparison instead of an exact zero.
    * Olivier: A lot of stuff from chirality flow get from filtering. 
    * ZW: For the plot on slide 22, the stuff removed from filtering is removed.  
    * Juergen Reuter: Helicity filtering gives you something that you get for free when you use chirality flow automatically.  
* MD: This could be used in QCD in the outlook. Spin-dependent measurements in deep inelastic scatering - could this approach be used there? 
    * ZW: I think so. Chirality flow has developed for full LO SM.
    * Andrew Lifson: The full SM paper EPJC 81.4 (Apr. 2021): https://arxiv.org/pdf/2011.10075.pdf  
* AV: Are there plans for somebody to continue doing this?
    * ZW: There are plans to continue this in Lund University. 
