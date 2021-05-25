---
title: "HSF Generator Meeting #13, 20 May 2021"
layout: meetings
# {{page.title}}
---
# HSF Generator Meeting #13, 20 May 2021

*Agenda: <https://indico.cern.ch/event/1036317>*

Present (remote): Josh McFayden, Efe Yazgan, Andrea Valassi, Steve Mrenna, Andy Buckley, Simone Amoroso, Leif Lonnblad, Aravind Thachayath Sugunan, Zach Marshall, Phil Ilten (partly), Michal Kreps (partly), Gurpreet Singh Chahal (partly)

Apologies: Alexander Grohsjean

## Pythia8 report for LHCC review 
Speaker: S. Mrenna

Steve presents the slides describing the answers from the Pythia8 team to the question received for the second phase of the LHCC review of HL-LHC computing.
- "Larger team than in the past but much more to do!"
- Some ME generation but also reading in LHE events
- Fragmentation is only with the Lund model now
- Dedicated tau package that we believe is as good as TAUOLA
- Good documentation, user support, no external dependencies (ROOT, thepeg), user hooks, do not duplicate efforts of others unless needed (e.g. no built-in ME generator)
- Funding dependent on FA/lab priorities, big challenge is funding/retaining junior colleagues
- Many major physics updates, including EW showers (ie removing dependency on PHOTOS)
- Main bottleneck is finding time (have competent people but they have little time)
- Help from HSF/experiments would be useful in restructuring (if people say it's needed), GPUs (if there are use cases), profiling (the way it's really used by the experiments)
- Rescattering in HI collisions is a source of significant slowdown
- No one complains about software performance. If there is a problem, willing to work on it...
- Vincia/Dire not significantly used. Vincia gives a better physics description (based on antennas). In some cases (not all), like sector showers slide 10, it also has better software performance for high multiplicities.
- Slide 13, Pythia concurrent hadronizer filter (from Chris Jones in CMS): Pythia thread friendly, but decayers are not
- Slide 15 takeway: HSF can help with profiling and with Vincia/Dire adoption

Comments/discussion:
- Andy: Is it fair to say the a priori physics content is better; the physics "description" is probably still to be fully evaluated by the experiments? I.e. some tuning is probably needed before production use. 
    - Steve: yes would agree with this.
- Simone: limited experience with the new showers, but DIRE has a significant negative weight fractions. If you take into account that we use this with NLO ME that already has negative weights, this becomes a problem. 
    - Steve: great question. ATLAS is actually using DIRE more than CMS.
- Andrea: does Vincia also have negative weights?
    - Steve: Vincia also has weights, but not negative weights.
- Zach: dealt a lot with Madgraph and ATLAS generators recently, and matching comes over and over again. While there are many people on the team, Stefan Prestel seems to be the person who is the main expert on this (and he is now busy elsewhere)?
    - Steve: there is also a junior person, but Stefan is indeed the main expert.
- Zach on restructuring slide 6. Comment: difficult to find exactly the repository, it would be nice to have a well defined path to provide pull requests for instance.
    - Phil: https://gitlab.com/Pythia8/releases
    - Phil: be aware however that we have a private development repo which is not this release repo. This is also because some collaborators use the private development repo to publish papers. People may have some criticisms of this, but this is the compromise we came up with.
    - Phil: in terms of restructuring it would be useful to have some feedback at the high level about the structure of the code. It would also be useful to know what people think about the user hooks we provide.
- Zach: HSF organized a review of GeantV, one suggestion would be to organize one of Pythia8 if you want it...
    - Andrea: interesting suggestion! Should be understood better. Best would be if the development team themselves agree to ask for this. Phil: will follow up inside the team. Josh: would also be useful to focus this on specific themes, eg on multithreading or heterogeneous architectures.
    - Steve: it was also interesting when we sat down with Peter Richardson and Servesh after the workshop, though we did not follow up (Andrea: Servesh left some time afterwards).
- Phil: we would like to be proactive. As far as we know, we are fine. But if people have some comments, then we would like to know.
    - Steve: for instance see the comments by Chris Jones on multithreading.
    - Zach: also reading from LHE files is something to be discussed.
- Steve: with Zach and others we are also involved in a project to port Pythia to HPCs.
    - Andrea: if this is also GPUs, you may be interested in yesterday's vCHEP talk about MG5aMC on GPU, though this is mainly about the ME (https://indico.cern.ch/event/948465/contributions/4323568). Josh: would be useful however to also have Pythia (after MG5aMC) on the GPU.
    - Phil: we need to work on the interfaces. Andrea: I would be very interested in this, even for MG5aMC to Pythia interfaces (eg NLO and PS interface), please give suggestions if you have some!
    - Zach: anyway can also have the ME on GPUs and then Pythia on CPUs.
    - Gurpreet: in CMS we want to invest in porting to GPUs, but we could do with some help from HSF.
- Josh: you mentioned NNLO matching, is there a clear path to NNLO matching in Pythia8? 
    - Leif: this is one of the things that in principle can be done in DIRE. We do not collaborate very much with the GENEVA team. It would be useful to adopt DIRE more, if you want this addressed.
    - Josh: rephrasing, maybe there is nothing to worry about for matching to NNLO MEs. But if there is, we should know soon. Steve: will follow up on this.

## AOB

- Next meeting is next week on May 27, discussing MadGraph5_aMC@NLO.
