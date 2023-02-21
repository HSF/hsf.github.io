---
title: "HSF Generator WG Meeting #19, 7 April 2022"
layout: plain_toc
---

Agenda: <https://indico.cern.ch/event/1142647/>

Further Sherpa efficiency improvements by Enrico Bothmann:

* Further improvements on top of the factor of two that goes into Sherpa 2.2.12.
* Calls to LHAPDF ~60% CPU time when on-the-fly weights / multiweigths are turned on.  
* Switching to LHAPDF6.4.0 makes ATLAS V+jets setup 30% faster.
* Do a pilot run for an event, if event (e.g. without weights) is accepted rewind and calculation using all weights etc.  --> ~x5 improvement in V+jets setup (close to ATLAS setup). On top of this LHAPDF 6.40 improvement is now 6% speedup. 
* Other things can also be done before unweighting: EW one-loop amplitudes --> from 19% to 0.8%. 
* Improvements similar in ttbar. 
* Phase-space and clustering 
* Si Hyun: if open loops does not have EWK corrections. openloops and MCFM gives similar performance. Is there a physics performance difference? 
    * EB: Analytic MEs not available for everything. In ttbar we get only zero-jet from MCFM so it depends on the process. So, we can not use it for everything. 
* Meng: Slide 5: 2nd bullet: What does accepted means? 
    * EB: accepted in unweighting step. The gain depends on the distribution of weights. 
* Andrea: are PDF variations similar in CMS and ATLAS?
    * EY: yes
* Andrea: Why too much time is spent in clustering (without PDF variations)? is this parton shower? 
    * EB: It starts from ME and interpret as in PS including emissions etc. It is a factorial problem. 
    * AV: is the clustering large because it is a merged setup? 
        * EB: yes the problem will be much smaller without merged setups.  And there may be other ways to cluster which may have linear scaling.
    * OlivierM: also surprised that clustering takes so long. Especially because that part of the code in Madgraph was written by a Sherpa author, so it would be strange that it is faster in Madgraph than in Sherpa. 
* Andrea: why too much time in phase space sampling (without PDF variations)?
    * EB: this is mainly because large multiplicity of jets
    * Olivier M.: also surprised by much time in phase space sampling, it is almost none in Madgraph. 
* Olivier M: about the NLO loops ME. Use one loop for each phase-space point or? In MG_aMC we have a trick so that most of the cases we do not evaluate it. 
    * EB: In sherpa it is always calculated but there are some tricks as well (e.g. see Danziger et al.) that prevents a lot of loop evaluations. 
* Andrea: Is there a work ongoing to reduce the speed even more from the LHAPDF side?
    * EB: There is an effort using GPUs but not usable yet. 
* Josh: we have the flame graphs for MG5_aMC
    * OM: It was dominated by the ME AFAIK but which variations were there or not. May not be directly comparable to the sherpa one presented here. 
* Gurpreet: Will there be a benchmarking for MG5_aMC  and the new Sherpa?
    * Josh: Plan is to include more processes like VV etc. They may not be public very quickly. But something to definitely follow up. 


