---
title: "HSF Generator Meeting #16, 24 June 2021"
layout: meetings
# {{page.title}}
---
# HSF Generator Meeting #16, 24 June 2021

*Agenda: <https://indico.cern.ch/event/1042657>*

Present (remote): Josh McFayden, Andrea Valassi, Efe Yazgan, Emanuele Re, Paolo Nason, Alexander Grohsjean, Liz Sexton Kennedy, Michelangelo Mangano, Simone Amoroso, Taylor Childers, Gurpreet Singh Chahal, Michal Kreps, Gloria Corti, Phil Ilten (partly)

Apologies: Graeme Stewart, Phil Ilten

## News

- Andrea: the vCHEP proceedings on the work on MG5aMC on GPU and vector CPUs will be on arxiv tomorrow.
- Please feel encouraged to give updates at these meetings about new papers relevant to software and computing for event generators! (Noticed today an interesting new paper about GPUs from the Sherpa team, https://arxiv.org/abs/2106.06507.)

## Powheg report for LHCC review 
Speaker: E. Re

Emanuele presents the slides describing the answers from the Powheg team to the question received for the second phase of the LHCC review of HL-LHC computing.
- Main focus: matching of fixed order to PS, mainly for SM processes
- Development will continue, but there are no funds specifically dedicated to the maintenance of the framework!
- Main physics update is NNLO QCD+PS in MiNNLO, but also NLO EW+PS and interpay with modern PS. These may require major recoding.
- Core of the software is Fortran based. Growing interest in GPUs.
- So far we have interacted (in a useful/efficient way) with users in the experiments. If there are other opportunities from HSF, opportunities would be welcome!
- CPU bottlenecks have been dealt with through reweighting (eg multiple pdfs, 1 or 2 loop amplitudes, scale variations) or parallelization (multicore). Some initial attempts at using MPI. No memory issues. 
- Negative weights does not seem to be a major issue with respect to other generators.
- Growing interest in GPU/ML, example efficient PS sampling and generation of underlying Born events
- Many processes available in NNLO QCD, negative weight fractions around 15% to 30% depending on the process
- Please let us know if there is anything that may be a bottleneck!

Comments/discussion:
- Andrea: nice to see many NNLO results, I thought the experiments were mainly using it for NLO. Paolo: not a general purpose MEG like MG5, but we are thinking of this and for instance we have interfaces to MG5 for that. We do not have a MEG inside the BOX, and using MG5 inside the box would even cause issues to publish (what would be the new thing to publish?). Using MG5_aMC tools to automatically generate MEs in conjuction with Powheg could be possible. Doing some interfaces to MG5 or others is needed, we could do that to improve usability even if its not new physics. 
    - Josh: In general NNLO is used when available, it's just that most processes were only recently implemented in Powheg and they can be hard to setup in the experiments... Also the negative weight fraction can be problematic, 15% is much larger than we are used to for Powheg - problematic when L
- Paolo: Modern Parton Showers means state-of-the-art new tools/approaches, e.g. PanScales (G. Salam et al.)
- Alexander: we are also exploring the interface of Powheg and MG5, this is very appreciated. We also do produce NNLO samples eg for DY. Negative weights do become a problem if they are the level of 30% as mentioned in the slides for Zgamma. 
    - Alexander: can you confirm the 15% for DY, I heard from colleagues it was 8%. When you go above 10% the number of events that you need to generate starts to increase substantially (would need to calculate this exactly). Emanuele: will check, should be possible to stay below 10%. Paolo: Larger negative weight fraction due to difference in scales with MiNNLO and complications with photon emissions.
    - Simone: at least for DY with MiNNLOPS the number of negative weights can be substantially reduced (to a few percent) through folding
- Simone: Reweighting more geared towards use in TH papers than for production in experiments. Layer of scripting/conversion of LHEF formats to be useable in experiments. Emanuele: We can fix it.
- Simone: Having automated framework, even just for NLO, could still be useful in several places. E.g. Powheg ttH came much later than in aMC@NLO. Other examples W+c exists in MG5_aMC but has large negative weights, it does not exist in Powheg. Interface with MG5_aMC could be expanded by something Marco Zaro already has. MG has full access to the amplitudes so can weight phase-spaces accordingly - this could be embodied into interface to Powheg.
    - Andrea: we are discussing with Olivier how to make more info available from the ME calculation (specifically, single diagram amplitude contributions rather than just the ME from the sum of all amplitudes), would this be useful? Paolo: yes something in this direction would be useful and was not conceived in the interface (would need amplitude squared). Andrea: will tell Olivier that you are interested in extending the interface. Paolo: would be interested in common interface coming from MG5_aMC.
- Gurpreet: Are you interested in implementing [positive resampler](https://arxiv.org/pdf/2005.09375.pdf)? Emanuele: we'll consider it. 
- Phil: LHCb Powheg Interface (https://gitlab.com/Pythia8/releases/-/blob/master/include/Pythia8Plugins/PowhegProcs.h) has two issues:
    - 1. Setting up compilation of all Powheg processes - could some work go into this to make it more user-friendly?
        - Josh: we do something in ATLAS which is probably similar, and it is painful to maintain.
    - 2. There have been security changes in glibc (https://patchwork.ozlabs.org/project/glibc/patch/20190312130235.8E82C89CE49C@oldenburg2.str.redhat.com) - need powheg as executables or libraries, not executable that can be loaded as libraries. Phil: 1st point could be fixed when fixing this one.
- Josh on funding: if no funding for software, are there permanent people who plan to work on this? Emanuele: yes this is a fair description. Paolo: as long as there is interest in the LHC community, we will support it (if it is used, people want to work on it). Emanuele: gratifying to see that what we work on is being used and is useful!
- Josh on help from HSF: if there is refactoring and reworking that can be useful as a common work, we can try to coordinate that.
- Josh on GPUs: Andrea with Olivier and others in CERN IT have been working on GPUs for MG5, this is a nice example of a collaboration. Emanuele: probably need a specific example and then attract some work?
- Andrea: is GPU only for ML in your plans? Paolo: for us the ME calculation belongs to different people, s we will not work on porting the ME to GPUs. Instead we have an efficiency of 1% in upper bounding of one hit-or-miss algorithm, if you can improve a lot on this with ML you make a big gain.
 
## LHAPDF/HepMC/Rivet/... report for LHCC review 
Speaker: A. Buckley

Andy presents the slides describing the answers from the team supporting LHAPDF/HepMC/Rivet (and other tools) to the question received for the second phase of the LHCC review of HL-LHC computing.
- MC tools are essential. They ar edifferent from typical generators, the teams working on them are more from the experiments than from the theory community.
- Sustainability is clearly an issue, most of this work is not funded. MCNet is ending, we need to replace that with another source.
- LHAPDF. Profiling Sherpa for NLO V+jets shows that pdf is a clear CPU sink, sums up to 40-50% for event generation. Some work on caching has helped (for Sherpa, not sure about MG).
- HEPMC. Completely rewritten in v3. CERN EP helped with that, now this support has gone. 
    - HDF5 support was added by Sherpa/Pythia teams, but is not standardised
    - Not just the library, also tools to manipulate events. Another example of stuff that is needed and requires work, but you do not get rewarded on, you cannot write a paper about it.
- RIVET. Development essentially stopped during the pandemic. Much of the development is needed in areas involding complex statistical tools, e.g. to handle event weights: what looks like a histogram is something much more complicated.
    - The issue with RIVET is not so much about speed. It is more about the experiments buying into the whole idea of analysis preservation... Reference data incompatible with HepData submission!
- Other tools. YODA is the statistics library below RIVET, it contains a lot of neat statistics stuff. Professor (now rewritten as Apprentice) is used for MC tuning, essentially unsupported. Other small tools (mcutils/heputils, HepData...).
- General issue with funding, no incentive to work on tools.

Comments/discussion:
- Josh about MCNET: can you quantify the impact of this? At face value it seems even more worrying than what we heard from other generator groups. 
    - Andy: very concerned! Personal example, travel money from MCNet will completely disappear. In the past we have made a lot of progress with small residential meetings, this will disappear. More generally, it becomes very difficult to attract new people into this area.
- Josh: how much support was coming from CERN EP and what will change? Andy: this gave a continuity, to have people paid in the GENSER area. We have now a core library used by all experiments which is essentially unsupported.
    - Andrea: have you tried to follow this up with CERN EP? Andy: no not really.
- People who are active for HepMC include Andy Verbitzky, AB, there is no project leader.
- Alexander: there is some use of Apprentice in CMS. Josh: also in ATLAS.
- Alexander: some analyses are difficult to preserve in RIVET. Efe: often this comes at the end and is found to cost too much effort. Gurpreet: we are trying to improve the process now to make sure Rivet is included in the analysis process in CMS.
    - Michal: we do try in LHCb to include Rivet, but we have little manpower to assist the analysts to give them the help they need. Gloria: there are many papers for which people can see the Rivet preservation (eg they see it for cross sections, not for decays).
- Gurpreet: can you elaborate on Apprentice/Professor? Andy: Holger is not in HEP any more, so he will not support it.
- Andrea: would you have a model how to support these? Andy: there is a lot of stuff that is purely technical and has no physics, builds etc, so a pool of RSEs would help. In the UK this seems to work, the point is you cannot hire 0.1 FTE of a person, but you can buy 0.1 FTE in a pool of people.
- Andrea about LHAPDF: are you in contact (or collaborating) with the PDFFlow team? Andy: aware of their work, but they did not contact us; not completely clear how useful this would be to the generators used in the experiments.

## AOB

- We now need to work on the document for the LHCC review (first draft needed by end of June in principle...). We will certainly come back to ask for your feedback and help!
- We will probably take a break from meetings during the summer.  Your suggestions for topics for future meetings would be extremely welcome!
