---
title: "HSF Generator Meeting #12, 06 May 2021"
layout: meetings
# {{page.title}}
---
# HSF Generator Meeting #12, 06 May 2021

*Agenda: <https://indico.cern.ch/event/1032036>*

Present (remote): Andrea Valassi, Josh McFayden, Efe Yazgan, Stefan Roiser, Zbigniew Was, Holger Schulz, Michal Kreps, Graeme Stewart, Liz Sexton-Kennedy, Olivier Mattelaer, Gurpreet Singh Chahal, Fernando Abudinen, Stephan Hageboeck, John Back, David Lange, Thomas Edward Latham, Simone Amoroso, Alexander Grohsjean, Saptaparna Battacharya, Taylor Childers, Juan Cruz Martinez, Zach Marshall

Apologies: Phil Ilten

## EvtGen report for LHCC review 
Speaker: M. Kreps

Michal presents the slides describing the answers from the EvtGen team to the question received for the second phase of the LHCC review of HL-LHC computing.
- Code very stable over 10 years
    - Mostly just adding decay models and updating Pythia versions
- Future plans
    - Code consolidation (not urgent)
        - Address code duplication (coming from uncontrolled addition of decay modes over time)
    - Allowing event-level multithreading
        - Currently not possible
        - Minimal plan is to have thread safety and full reproducibility when decaying different events in different threads
        - Some funding for software engineer (from SWIFT-HEP) to work on this.
- Multi threading in LHCb (Gaussino)
    - There was single instance of EvtGen, locked to be used by different threads. Pythia8 is actually multi threaded, it is only EvtGen that needs to be locked.
    - There is some performance overhead from this locking of EvtGen, but once you include detector simulation this overhead is completely negligible for LHCb.
    - Liz: are you running Geant4 simulation in MT mode? Michal: not doing it currently, but we are doing it in this exercise. Liz: probably then, if you are not hit by Amdahl's law, it means that GEN is a very small fraction of SIM (while in CMS it is larger, at least in some processes). Alexander: should also take into account Pythia8. 
- Issues with multithreading in EvtGen
    - One issue is Tauola and Photos. We have no resources to work on making those thread safe. 
    - Around 40% of the time in EvtGen is Photos radiative corrections. A lot of this time is spent in HepMC conversions, we will try to bypass HepMC and just feed data directly from EvtGen into Photos.
    - Also trying to do tau decays in Pythia8 directly rather than using Tauola. One challenge is passing the spin states from EvtGen to the tau decayer.
- Also working on updating the decay tables. Unrelated to code issues, but an important aspect of EvtGen.
    - One point that we should mention in the review is that it would be useful to agree with other generators about particle properties (else we may get inconsistencies)

Comments/discussion on Tauola and Photos:
- Zbigniew about Tauola and Photos. Bypassing HepMC would indeed speed up significantly the interface to Photos, we should discuss this more in detail (complex now, cannot come to CERN from Krakow). Multithreading was not a priority so far. Tauola should now be ready for C++, with simple functions that can be more easily parallelized. One priority was so far to work on Tauola for Belle2, they can also provide a lot of physics feedback on tau decays to improve the software.
    - Michal: do you use Evt internally? Zbigniew: it is something equivalent to HepEvt. Michal and Zbigniew agree that EvtGen should try to write data directly in the structure used by Photos. Zbigniew: we should really sit together to avoid trivial mistakes.
- Zbigniew: Photos and Tauola have random number wrappers, so it should be easy to replace them.
    - Michal: one issue is that if these random wrappers are global then this complicates multi threading. Zbigniew: will follow up offline after the meeting.
- Zbigniew: summary for Photos, two things, more flexibility on random numbers and also multi threading. If you could come to Krakow for one or two weeks we could easily fix it!

Other comments/discussion:
- Josh: surprised about the inconsistencies mentioned. Many sources like PDG and HFLAV. And different choices in different generators. Can we define a generic way/tool to do this? Michal: PDG is only published data, HFLAV is also preliminary data. Zbigniew: in our experience you often have to work with multi dimensional distributions directly from the experiments. Simone: there is a PDG API and we are currently using that.
- Simone: some feedback from other ATLAS colleagues that some EvtGen settings  are mainly fitting LHCb needs. Michal: not correct, we are also taking into account ATLAS needs, but we can only include what they feed back to us.
- Andrea: can ATLAS/CMS confirm that they use EvtGen? Josh: ATLAS use it for everything except Sherpa - this is important because having different heavy flavour decay properties leads to different b/c-tagging calibrations/scale factors. Alexander: in CMS we are using EvtGen but only for some specific processes.

## MadGraph5_aMC@NLO brief report/plans about GPUs and vectorization 
Speaker: Stefan Roiser

Stefan presents the slides describing a brief report on the status and plans for porting the matrix element calculation in MadGraph5_aMC@NLO to GPUs and vectorised CPUs.
- Overview, we started in Spring2020 with Olivier Mattelaer. Focusing on CUDA and C++ but also looking at abstraction layers. 
- Focus on matrix element calculation because this is the main consumer of CPU (eg 80% for one typical CMS process).
- Got good numbers so far for matrix elements. We are at a crossroads to understand where we want to go now and would like some feedback from the experiments.

Comments/discussion:
- Simone: very nice work. A few questions. 
    - Vectorization could be even more interesting for GPUs. Do you need to do many optimizations? Stefan: no, all done for you. Andrea: essentially the code uses compiler vector extensions (the auto generated code will use those), so you spoon feed that to the compiler and it auto vectorizes.
    - Vectorize the rest? Stefan: could do but it is in Fortran. Andrea: yes could be done but much more complex in Fortran. Olivier: in any case the ME is the part that should take the largest time.
    - Simone: we would definitely be interested to try this out as soon as possible if we get a factor 2 in CPU...
- Josh: is this flamegraph for creating or running the gridpack? Olivier: this plot is probably for running the gridpack, but in any case both ways will use the ME. Josh: we are especially interested in the running the gridpack, which is the biggest consumer.
- Josh: in principle running a mixture of Fortran and C++ is not a problem. You tar up the executable and run it, even if it is a whole bunch of stuff together. You do not even care to run it in an ATLAS or CMS environment.
- Stefan: physics validation can be quite a long process. So one question is whether you want to spend the effort. Also the Grid is heterogeneous, depends if you can choose a nehalem or haswell node. Josh: you can taylor a production for a specific site: eg in the past in ATLAS we did a large production at NERSC, we could imagine doing something similar here. Simone: also remember even a site is heterogeneous. Andrea: solving the distributed computing should not be a problem (and most sites are or soon will be at least AVX2).
- Efe: most important part is to be able to run in the Grid. Stefan: can also produce fat binaries, all this is solved.
- Gurpreet: it will not be a big problem for us in CMS to test this workflow. We also already have GPU resources where we are running some other workflows. In terms of validation, initially we would not run large scale validations, there should not be many technical difficulties. As soon as you give 
- Simone: will this be released in standard MadGraph_aMC@NLO? Andrea: Olivier is already maintaining some code upstream in launchpad, where there is the code-generating python code. We have not discussed the details, but probably initially this will be one of the "output" backends (like now we have default Fortran, plus standalone_cpp). This code is actually an evolution of the standalone_cpp version: it is a single source C++/CUDA (same code, with #ifdef's choosing either branch). We are doing an iterative development (changing C++/CUDA, porting upstream to Python, regenerating C++/CUDA), and it may take a few more iterations e.g. for QCD color algebra and processes with more than one subprocess. Then we also need to develop the Fortran/C++ linking to complete the prototype.

## AOB

- Next meeting is probably on May 20 (during vCHEP), discussing Pythia.
