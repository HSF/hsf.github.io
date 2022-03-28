---
title: "HSF Generator WG Meeting #18, 24 March 2022"
layout: plain_toc
---

Agenda: <https://indico.cern.ch/event/1141896/>

* Discussion of ATLAS V+jets Modelling paper ([PMGR-2021-01](https://arxiv.org/abs/2112.09588))
    * V+Jets billions per final state produced in ATLAS. Dominant CPU sink is V+jets.
    * Sherpa2.2.11 0-2j@NLO+3-5jets@LO using MEPS@NLO + EW(virt) corrections, HTprime scale, no gluon colour/spin exact matching and analytic enhancement. --> ~375 HS06/event.
        * 200 million events --> 238 HS06 years (compared to 444 HS06 years for Sherpa2.2.1 with different settings). ==> Reduction of a factor of 2 in CPU resources with higher accuracy and better features: NLO QCD + NLO EW corr., on-the-fly weights...
    * When settings similar FxFx and Sherpa has similar CPU times. However in Sherpa using event scale = scalar sum of outgoing particles reduces the accuracy.
    * Slicing: max(HT, PT^V) in six slices.
        * Samples are heavy flavor filtered --> x3 additional samples for each slice.
    * Phase-space enhancement for high pT and high HT for Z+njets (n=1,2,3,4,5): differential or analytic in sherpa.
        * Analytic enhancement behaves better.
        * Differential enhancement causes large spread of weights at high pT^V --> inflation of relative uncertainty.
        * Fraction of negative weights reduced. 
    * Phase-space enhancement  for low pT scales.
        * High mV sample (>120 GeV) and enhance in mV and combine with the max(HT,PV) sample. --> Weight spread is controlled by doing this.
    * Questions/comments:
        * Andrea V: Slide 4: Why the large variations of seconds/event?
            * Matthew G: Merging different final state multiplicities (e.g. 5j means 0-5j). So, we are sampling different events, i.e. different number of jets in the final state.
            * Andrea V: May be one can check the spread generating exactly 5 jets.
        * Efe Y.: How does Sherpa compare to FxFx:
            * M.G.: No benchmarking yet for FxFx but it is definitely faster than sherpa. 
        * Efe Y.: Do you have the HS06 info from the production system as well:
            * Benchmarking only by local machines at CERN but work is going on to have the numbers from actual machines probably with larger spreads in the central values.
            * Efe Y.: In CMS, we tried to this with condor directly using the information using the production machines for each job but even then spreads were unreasonably larger than the ones compared to the local calculations. 
        * Marek S.: Unweighting is a statistical process. The smaller the efficiency the larger variations you will see. With higher number of partons you will see larger spread. Various effects are folded in one distribution. There is the improvement from unordered histories which has huge impact on tails of distributions.
        * Markus D.: EIC will have similar problems in a few years. What would you recommend for an experiment starting to work on these things?
            * Matthew G.: Why FxFx is much faster with similar accuracy needs to be understood. 
        * Alexander G.: Slide 2 plot: Sherpa prediction for 2.2.11 spot on with data, FxFx around 600 GeV there is some deviation? Where is it coming from?
            * Matthew G.: We should not read into this too much. In the paper (updated) version FxFx gives a perfect description (with improving details)_ FxFx and Sherpa have comparable performance sometimes FxFx is even better.
* Lively discussion. Talk on "further Sherpa efficiency improvements" postponed to April, 7th, due to running late.

