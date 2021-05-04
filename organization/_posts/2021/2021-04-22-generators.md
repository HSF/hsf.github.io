---
title: "HSF Generator Meeting #11, 22 April 2021"
layout: meetings
# {{page.title}}
---
# HSF Generator Meeting #11, 22 April 2021

*This notebook is used to record the minutes of the HSF Generator WG meetings. These are archived after each meeting onto the [HSF Website](https://hepsoftwarefoundation.org/organization/minutes.html). To edit this page, please login with your GitHub account!*

*Agenda: <https://indico.cern.ch/event/1030889>*

Present: 
- Remote: Efe Yazgan, Josh McFayden (ATLAS & HSF), Andrea Valassi, Junquan Tao, Stephan Hoeche, Steve Mrenna, Liz Sexton-Kennedy, Michal Kreps, Graeme Stewart, Andris Potrebko, Alexander Grohsjean, Markus Schulz, Philip Ilten, Emilien Chapon, Matteo Cacciari, Taylor Childers, Zach Marshall, Walter Hopkins, Andy Buckley, Gurpreet Singh Chahal, Doug Benjamin 

Apologies: -

## Introduction

Josh: as discussed last time, we'll have several meetings to prepare for the LHCC review. We start today with Sherpa. 

## Sherpa report for LHCC review 
Speaker: S. Hoeche

Stefan presents the slides describing the answers from the Sherpa team to the question received for the second phase of the LHCC review of HL-LHC computing.
- One issue being addressed is that the framework is somewhat monolithic. For instance will separate ME part (a bit like Madgraph) and the PS part.
- Help from HSF/experiments
    - Restructing framework
    - Porting of code to GPUs
- We have a big CPU bottleneck. 
    - Partly due to the fact that it's often run with several variations (eg three pdfs). One inefficiency is that these variations were done before the unweighting procedure, so for events that would be thrown away anyway.
    - For NLO we are doing a complex handling of spin and color correlations. Discussed this with Frixione in the past. Now we accept that we do not always need to do this (you might not see the difference), so there is an option to disable this.
    - Some inefficiency in clustering algorithm is also being addressed.
    - However, if you expect higher physics precision, we cannot speed up by disabling some of these features.
    - Investigating better phase space sampling, for instance with ML.
    - Some work on negative weights by Danziger, published in her thesis.
- Performance analysis of the code (slide 5)
    - As mentioned, a large part of the time is weight variation. If you remove that, for a typical multijet process the "ME" is 96% (actually this includes also phase space, and matching).
    - Without variations, 2s per event, versus 50+s per event with variations. With variations, actually 86% of CPU time goes in LHAPDF!
- Therefore rearranged the code (slide 6) and got several savings. Running with variations is now almost 30x faster.
- After these optimizations, left with three bottlenecks:
    - One loop ME
        - Generic interface to MCFM done
        - Speed up of at least a factor of 10 w.r.t. openloops2
    - PS clustering 
    - Math library
- Two distinct efforts to use ML to speed up phase space sampling
    - Technique similar to Vegas. No risk to do things wrong, in the worst case you get an inefficient algorithm.
    - Algorithm iflow tested, but unlikely that we use it in production in its present form. Tested for processes which however are fast already. Technologically (TensorFlow?) it does not scale to the processes which instead are slow and that we need to speed up.
- ME on GPU, efforts ongoing
    - Some differences in functionality between Amegic and Comix (helicity sampling/summation, color summation)
    - Most generators on the market do helicity sums, not helicity sampling

Comments/discussion:
- Josh: very interesting and very encouraging!
- Steve: impressive! Technically, how do you do the performance analysis? SH: with vtune, then we get flamegraphs.
- Graeme: impressive, many nice speedups! Note about the charge for HL-LHC, we should also answer the  questions about how the project is managed, this is one area where the outcome of the review may be helful, e.g. if there is shortage in some areas. SH: if you want a more detailed statement, we should get also Frank's input and discuss more in detail about how we can benefit from each other's expertise. Many of our resources are tied to IPPP. Graeme: please feel free to discuss with Liz and myself about these issues.
- Graeme: mentioned negative weights, but did not give details. Overall assessment? Is there any potential improvement coming up? SH: still playing... there will be a writeup from Katarina, but unfortunately she left physics. Many ideas still to investigate.
- Josh: two bigger picture questions. One about your point "these improvements are good for NLO merged, but not for NNLO"? SH: personal perspective (others may disagree!), in some cases there is very little difference between NNLO and NLO+corrections, so you could push to detector simulation only NLO and apply some corrections for NNLO a posteriori. 
    - Efe: for things like ttbar spin correlations how do you do that, we need NNLO most probably there? SH: do not completely agree with this. It may be due to something we don't do right going from LO to NLO. Should discuss more in detail, eg invite Peter Richardson who worked on this for Herwig.
- Josh: very interesting work on MCFM, also the direction, being a bit more modular about software. Do you think a more generic interface/framework for many different generator tools would be productive or counter productive? SH: interesting, discussed this with colleague and it would be very beneficial. One reason more to include MCFM in the review, expect that it will become more and more important. SH: a plug and play framework has been tried and has not worked very well (The PEG), but we should try a second attempt. Not only useful for speed, but also to ease comparisons of different calculations. Allows to focus on specific areas of expertise and also allow easier uncertainty extraction (e.g. swapping showers). JM: Could also help with code porting to different architectures.
- Andrea: Apart from tne number of calls to LHEPDF what is the main bottleneck? SH: MG5_aMC does part of the simulation. MG typically uses one scale only, then you need to do some variation for matching and merging. For instance the yellow box is not part of MG, it is part of Pythia, and you do not see it. For a fair comparison you should take into account this yellow box. However yes the ME yes also for Sherpa does take a significant part of the time.
- Andrea: Is this weight variation something that both ATLAS and CMS (and both Sherpa and Madgraph) do systematically? We did not even particularly describe it in the 2020 paper. SH: not completely sure, also depends on the use case. Josh: probably in the same ballpark between ATLAS and CMS, if not exactly the same. Note that for LO some of the reweighting you can do a posteriori, but this is not possible at NLO for some generators (including Sherpa). Phil: for LHCb there is some analysis where we need a propagation of weights but we do outside the MC framework.
- Alexander: what systematic variations can you provide in Sherpa with these weight variations? SH: hinting specifically at PS systematics? One thing we have is PS renormalization and factorization scale variation. But it's hard to know how to use them as they are a rather rough estimate. NLO Parton Shower is the main focus for HL-LHC. SH: there are also some corrections to propagators that (unlike Madgraph) we cannot handle in our UFO interface.

## AOB

There is no AOB to discuss.