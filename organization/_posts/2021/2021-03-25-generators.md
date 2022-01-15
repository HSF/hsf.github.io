---
title: "HSF Generator Meeting #10, 25 March 2021"
layout: meetings
# {{page.title}}
---
# HSF Generator Meeting #10, 25 March 2021

*Agenda: <https://indico.cern.ch/event/1019213>*

Present: 
- Remote: Efe Yazgan (HSF WG, CMS), Josh McFayden (HSF WG, ATLAS), Andrea Valassi (HSF WG), Stefano Frixione, Michal Kreps (LHCb, EvtGen), Steve Mrenna (Pythia), Taylor Childers, Graeme Stewart (WLCG SWL), Torre Wenaus, Danilo Piparo (CMS CC), James Letts (CMS CC), Zach Marshall (ATLAS CC), Gurpreet Singh Chahal (CMS, Sherpa), Matteo Cacciari, Phil Ilten (LHCb, Pythia), Thomas Latham (EvtGen), Holger Schulz, Liz Sexton-Kennedy (WLCG SWL), Alexander Grohsjean (CMS), Olivier Mattelaer (MadGraph), Aravind Thachayath Sugunan (CMS), Simone Amoroso (ATLAS), David Lange (CMS), Stefan Roiser (CERN)

Apologies: Simon Platzer (Herwig)

## Introduction to Generators document for LHCC review 
Speaker: G. Stewart.

Graeme presents the slides describing the general plans for the second phase of the LHCC review of HL-LHC computing. The new charge for the review is attached to the agenda.

Comments/discussion
- Graeme: the fact that generators are included in the review does not necessarily mean that we think there is a problem with generators! 
- AndreaV: we should cover issues and we will definitely ask the experiments and the generator projects what they think the issues are, but did the LHCC give some hints about what they themselves are concerned about? Graeme: they did not really give us this hint, it should mainly come from the experiments.
    - Danilo: one big uncertainty is how much the cost of generators will increase. Josh: agree, but this depends a lot on what the experiments will require in terms of precision. Danilo: agree, benchmarking and profiling will help. AndreaV: some things cannot yet be profiled because they do not exist yet, eg NNLO/jets. Simone: some of the bottlenecks now may be different from the bottlenecks in the future.
    - Phil: previous document has focused a lot on ME generation which is very relevant for ATLAS/CMS, but LHCb for instance has more needs on hadronization, how do we take those into account? Josh: in the previous document we tried to cover the topics on which we had more interactions, but definitely some of these issues should be covered, especially if the issues are already known. AndreaV: we should start by having a presentation in the near future. Zach: things like EvtGen are definitely in scope, but if it is LHCb specific issues they would not be in scope. Phil: it's about how you extract physics about the hadronization, so not even only EvtGen but also Pythia, Herwig, Sherpa, and this could be useful also for ATLAS/.CMS about some of their systematics.
    - Zach: could people write down from which community they are in the minutes. If we are missing on some ommunities, eg Sherpa or Herwig, we should make sure we reach out to them.

## WG plans for the LHCC review
Speaker: J. McFayden.

Josh presents the slides describing the current WG plans for the second phase of the LHCC review of HL-LHC computing.

Comments/discussion:
- Phil on thread safety: would be very useful if the thread safety are made clear to the generator side.
- Stefano: mentioned NNLO several times, and if this becomes systematic then one should also include higher order electroweak effects, as they are as important if not more important. There is some work (even in Madgraph), though probably people are not yet to do a simultaneous expansion in alphas and alpha. Two different issues on QED and QCD showers; how to start QCD showers from EWK dominated MEs and vice versa. They are different and equally important issues. 
- Stefano about NLO-Delta: unfortunately the team is delayed by covid and personal issues. Now work being resumed (e.g. Stefano and Stefan Pretzel), a number of criticalities have been identified and are being worked on.
- Zach on the general slide: if there are general common projects (eg Matrix or Geneva), they are in scope. This could also include ML projects. 
- Zach on POWHEG: we should ask about their sustainability model, they have all different process, this is not sustainable. 
- Zach: experiments need a final precision, it would be good to know also if they have no effort available for computing.
- Gurpreet on slide 7: in Sherpa we are starting to look at GPU, while the work on negative weights (which was in a thesis) is already in the code.
- Gurpreet: for technical and scientific work, we can work on it, but for dedicated career paths and budgets we need some message from higher management, is there some progress? Josh: this is slowly being acknowledged from funding bodies. Stefano: from the theory community, keep the expectations low. Graeme: made some noise at higher level (e.g. ECFA), but we are still waiting foir this to translate into hiring policies... it's not going worse than it was, and there are some universities keen on recruiting software experts.
- Michal: about EvtGen, currently this is completely impossible! (It requires big changes to make it MT). We have some funding for a software engineer, probably will start in the Autumn, though it's not certain where we will arrive. Michal: did not see Photos discussed, but this has similar issues with MT. Phil: functionality seen in Pythia8 does not extend to the low masses in B decays. Andrea: would be useful to clarify some of these issues for LHCb especially, where is the MT problem (Gaussino, Pythia, EvtGen, Photos?) and also how big of a problem it is for experiments. Michal: Dominik Muller had run some tests and until 16 threads at least it was not a major issue, but beyond it may be a problem. Photos may be a bigger problem, we did try some profiling but a better understanding is needed, some of the problem is related to HepMC. Liz: the problem with some of these decayers is that some workflows, especially filtering in B physics, are really hit hard. David Lange: actually for CMS the issue is mainly in Pythia rather than in EvtGen. Alexander: the problem in CMS is mainly in the filtering, it would be interesting to compare, it seems LHCb has a slightly different approach. Michal: there are also some ideas from Peter Skands (discussing with Michal and Phil) about how to create specific hadrons in Pythia without biasing kinematics.

## CMS generator event accounting 
Speaker: E. Yazgan.

Efe presents the slides, giving an update about the accounting for generator CPU budgets in CMS based on work done with David Lange.

Comments/discussion:
- Efe: today cannot compare these numbers to ATLAS, but next time we should be able to compare them to ATLAS.
- Simone: to understand better, you run up to minutes till you get 5 events? I am concerned that 5 events may be too few and may bias these numbers, I have in mind some slightly different ratios for some of these categories.
- Simone: can we have some more fine grained info for some of these categories, as it is done in the HT binned slide? Josh: yes, and also to know for instance if they are from gridpacks or not. Efe: essentially all from gridpacks except Comphep and Pythia.
- Stefano: just to be sure, this is without detector simulation and unweighted? Efe: yes only GEN and all unweighted. Stefano: For NLO, they are unweighted as being all +1 or -1 weights. Stefano: in Delta paper we have introduced a cost function to evaluate cpu costs.
- Andrea: can you also translate into full budgets for one year, allowing a better comparison to ATLAS? Efe: may be not before the  campaign is complete. Danilo: it depends what you want to do with those numbers. Long discussion. Zach: a lot of this is to how to extrapolate to what we need for HL-LHC, and the takeaway from the exercise in ATLAS over the last few weeks is that it was extremely useful and we understood that previously we were oversimpliying the estimates. 
- Alexander: also important to compare event weights and consider LHAPDF. Stefano: indeed it depends on what exactly you do in LHAPDF. Zach: we found that LHAPDF uses a lot of CPU.
- Stefano for Efe: time per event averaged over different generators (eg FxFx and MGaMC@NLO) is not interesting, for me as generator author I want to know if my own generator has an issue. Efe: I agree. This was the "first approximation" - will do for the next presentation. 
- Josh: I see 27 seconds per event for V+jets and I recall from memory that the full chain was 90 seconds per event, so this would be inconsistent with statements we have seen that GEN is completely negligible overall. Efe: for heavy processes like V+jets in this table, GEN becomes significant. 

## AOB

There is no AOB to discuss.
