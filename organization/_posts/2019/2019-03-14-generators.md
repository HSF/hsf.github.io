---
title: "HSF Generator Meeting #3, 14 March 2019"
layout: meetings
---
# {{page.title}}

*Agenda:
[<span class="underline">https://indico.cern.ch/event/802643</span>](https://indico.cern.ch/event/802643)*

*Present/Contributors: Simone Amoroso, Andrea Valassi, Efe Yazgan, Lesya
Shchutska, Qiang Li, Taylor Childers, Zach Marshall, Olivier Mattelaer,
Josh McFayden*

## Discussion on sharing SUSY samples across experiments
  - ATLAS-CMS comparison recently started for process definitions in
    SUSY searches
  - Detailed comparison of MadGraph setups (both ATLAS and CMS use
    MadGraph for SUSY)
  - Run cards: matching configuration is very different in the two
    experiments, cuts instead differ only in minor ways. Difference in
    systematics setup partly depends on different MadGraph versions.
  - Param cards, i.e. SUSY models: there are some differences. For
    sbottoms, the physics that is tested is essentially the same. But
    for electroweakinos, there may be quite some differences.
      - Olivier: is b mass different? Josh: there is an agreed set for
        the experiments, there may still be something to harmonise.
        But it may be different from the MadGraph default. Olivier:
        please send me the values you use, so we can put it in
        MadGraph.
  - Decays: ATLAS rely on MadSpin (both on-shell and off-shell), CMS
    do not.
      - Lesya: in CMS we reweight one sample to test different
        physics, e.g. for details of CMS look at
        [<span class="underline">Figure 8 in
        SUS-16-051</span>](http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-051/index.html#Figure-aux_008).
  - Pythia showering/merging: each experiment uses its own recommended
    settings, this would be difficult to harmonise
      - Josh: could this make a difference? Zach: probably not a big
        difference through the acceptance, but will try and run both
        schemes and compare.
      - Qiang: which tuning is ATLAS using? CMS is using its own tune.
        Zach: working on new tunes at the moment, now using an ATLAS
        specific tune (A14). Zach: can also try the CMS tune to see if
        it makes a difference, is it available? Efe: not available in
        the pythia software, but parameters are public, will send them
        to you. *\[Info circulated by Efe after the meeting: CMS
        default tune parameters are in
        [<span class="underline">github</span>](https://github.com/cms-sw/cmssw/tree/master/Configuration/Generator/python/MCTunes2017)
        (in most cases, for NNLO PDF CMS uses CP5 and for LO PDF they
        use CP2) - and there is a corresponding public note for this
        in
        [<span class="underline">cds</span>](https://cds.cern.ch/record/2636284?ln=en),
        paper version is coming soon\].*
  - Zach’s opinion on sharing
      - Harmonizing does not mandate sharing, but sharing prevents
        later divergence
      - If sharing: need to choose a format (LHE?) and mechanism, with
        authorizations (rucio?)
      - Opinion: focus on harmonization for now, but then it would be
        nice to have the technical issues solved for sharing, can the
        HSF WG help?
      - Early this can hit analysis is Moriond 2020 timescale, no
        pressure
  - Long lived particles (LLPs): a bonus
  - Discussion
      - Josh on slide 9 (sharing): how advanced is rucio adoption?
        Efe: must ask computing guys. Josh: before we can do something
        technical, it would be nice to know how much rucio is actually
        used.
      - Efe: for SUSY, what is the purpose of comparing/sharing? Zach:
        mainly physics, i.e. we want to ensure that when we talk of
        gluinos we talk of the same thing. If we do harmonise
        settings, then we also have the option of sharing.
      - Zach: signal production is a very tiny fraction of CPU
        consumption, so CPU saving is certainly not the driving force.
        Simone: agree, CPU not relevant here, but this is a good first
        example for sharing also in other cases.
      - Simone: one argument against sharing is that we reduce risk
        for instance of a bug in one generator used by one experiment.
        Having two independent samples reduces risks.
      - Olivier: actually sharing does not require harmonisation, we
        can have two samples used by both experiments and use
        technique like re-weighting to morfe the other samples
        generated to be equivalent to the dedicated one.
      - Andrea: very useful discussion both for physics and CPU
        consumption.
      - Efe: so what is the long run model, a database of samples that
        anyone can use? Simone: yes something like this. Zach: one can
        even think of doing these LHE publicly available for theorists
        and phenomenologists. Simone: same way, theorists can put LHE
        files somewhere and then experiments can analyse them.
      - Andrea: what’s the more general feeling in ATLAS and CMS,
        apart from the people here? Zach: actually we have generator
        and SUSY convenors from both ATLAS and CMS here today, so
        there seems to be quite some agreement that this is
        interesting\!

## ATLAS and CMS event generator accounting update 
  - Some slides are the same as last week
  - Slide 3: more accurate info from one generation, generation is
    about 10% of GENSIM combined, so for a total of 30% GENSIM in Grid
    resources, generation is 3% of all resources, accurate to within a
    factor two
  - Slide 6: new tests from Qiang, GEN is 1% to 4% of chain (including
    miniAOD) for some samples
      - Note that miniAOD is negligible
  - Slide 7: filled in the table
      - Still some clarifications needed on CMS and ATLAS definitions
      - Josh: propose to have an approximate version only for the
        moment, to get a gross estimate, no need for details, but
        split at least LO and NLO. Andrea: agree. So you split 6600M
        into LO and NLO? Josh: yes, already done.
      - Josh: agree however to have a textual description too, so we
        understand better similarities and differences.
      - Josh: propose to split inclusive and merged samples.
      - Andrea: is this for one year of data taking? Josh: yes, will
        update the numbers to more closely match what CMS has filled
        in.
      - Josh: will fill in the values for ATLAS for the specific cases
        suggested.
  - Andrea: are there public presentations showing the lists of big
    productions public? Josh/Efe: there are no presentations about
    this really, maybe the CRSG?
  - Efe: can we find some infrastructure to run benchmarking tests?
    Zach: Openlab are great for that, we can get dedicated machines,
    even bare metal, for one day or longer, with exclusive access.
    Andrea: I can definitely help with getting these machines, but we
    would need possibly a plan first, how many machines we need for
    how long and to do what. If we (especially ATLAS/CMS) prepare this
    plan, then we can easily get some openlab machines from CERN IT.

## AOB
  - Next meeting will normally be in two weeks on March 28.
