---
title: "HSF Weekly Meeting #169, 11 July, 2019"
layout: meetings
---

# {{page.title}}

*Present/Contributors*: Graeme Stewart, Andre Sailer, Marco Clememcic,
Pere Mato, Agnieszka Dziurda, Daniel Elvira, Andrei Gheata, Serhan Mete,
David Lange, Ed Moyse, Paul Laycock, Torre Wenaus, Ben Morgan, Dario
Menasce, Eduardo Rodrigues, Gloria Corti, Liz-Sexton Kennedy, Heather
Gray, Sudhir Malik, Caterina Doglioni, Mark Neubauer

*Apologies*: Andrea Valassi

## News, general matters
  - HPCs and GPUs - cost model and benchmarking WG
      - WLCG Management Board has set up a group to work on benchmarking of GPUs in
        particular. 
      - This is to anticipate that some funding agencies might offer GPU resources
        as part of their WLCG pledge.
      - Some notes and the charge in this
        [<span class="underline">Google
        Doc</span>](https://docs.google.com/document/d/1rAr9RN_CcvmiA8aC0thh5aINeUgNl44mOiHcx2RweZI/edit).
      - Note that at the moment we don’t have many (any?) workloads
        that we could run at any scale.
      - We are asked to have at least 1 HSF representative in the
        group.
      - Would anyone be keen to participate?
          - David; Graeme; Andrea V; Hadrien G (all can contribute a
            bit).
  - EDM4HEP
      - As an outcome of the Bologna Future Collider Software Workshop
        we had the [<span class="underline">first
        meeting</span>](https://indico.cern.ch/event/832559/) of the
        EDM4HEP group this week.
      - HSF is acting as an umbrella.
      - ILC, CLIC, CEPC, FCC all present, we reviewed LCIO and
        FCC-EDM.
      - Had to change some of our normal practices to collaborate with
        Chinese colleagues (Google blocked).
          - CERN e-group instead of Google Group
            ([<span class="underline">hsf-edm4hep-wg@cern.ch</span>](mailto:hsf-edm4hep-wg@cern.ch)).
          - Overleaf instead of Google Docs.
  - ECFA Presentation
      - Graeme will give a talk on Computing and Software Challenges
        at the ECFA session of EPS-HEP.
      - [<span class="underline">Draft
        talk</span>](https://docs.google.com/presentation/d/1dGJHa2v1CbXuiYCQ3c9XxFKcEBfsxQS4ptSb34cZDFY/edit?usp=sharing) - comments welcome.

## Google Summer of Code 2019
  - Second coding period.
  - All students passed, but a few ‘alerts’ to watch out for.
  - Mostly going well.

### Google Season of Docs
  - Application period ended.
      - 5 applications for 3 proposals (DIRAC, Rucio, ROOT).
      - Mentors are looking at these.
  - Our choices by 23 July.
  - Seems Google will only finance one project.
  - August for community bonding, three months work.
  - How to select?
      - Filter and use the same committee as GSoC - Peter, Pere and
        Michel.

## Activity and Working Group Updates

### Data Analysis
  - Next meeting will be on the 22nd July on “Computing infrastructure
    for future data analysis”, as a precursor to this year’s pre-CHEP
    workshop on \~the same topic.
      - Agenda (and indico) still in preparation.

### Detector Simulation
  - No news to report.

### Reconstruction and Software Triggers
Update slides [<span class="underline">attached to agenda</span>](https://indico.cern.ch/event/785587/contributions/3266731/attachments/1776030/3097450/20190711_-_HSF_Reconstruction_and_Software_Triggers_Report.pdf)

1)  Acting on topics of interest from Reconstruction and Software
    Trigger CWP roadmap
    ([<span class="underline">link</span>](https://arxiv.org/pdf/1802.08638.pdf))

**P** - Past meeting - **J** JLab workshop talks - **F** Future planned meetings

- P: Enhanced vectorization programming techniques
- P: Algorithms and data structures to efficiently exploit many-core architectures
- J: Algorithms and data structures for non-x86 computing
  architectures (e.g., GPUs, FPGAs)
- F: Enhanced quality assurance (QA) and quality control (QC) for
  reconstruction techniques
- PJF: Real-time analysis
- JF: Precision physics-object reconstruction, identification and
  measurement techniques
- F: Fast software trigger and reconstruction algorithms for
  high-density environments

2) Seeking enhanced collaboration / discussion with other communities:
  - F: Neutrino and astroparticle
  - JF: Nuclear physics

#### Past meetings
  - Summary of ATLAS / CMS trigger April/May cross-talks
      - Indico:
        [<span class="underline">https://indico.cern.ch/event/815233/</span>](https://indico.cern.ch/event/815233/)
      - Live notes:
        [<span class="underline">https://docs.google.com/document/d/1sjPazZzVTy6aPyznCokC2gcYmS1kigorPdW8DIqGOoE/edit</span>](https://docs.google.com/document/d/1sjPazZzVTy6aPyznCokC2gcYmS1kigorPdW8DIqGOoE/edit)
  - Algorithms and data structures to efficiently exploit many-core
    architectures
      - Indico:
        [<span class="underline">https://indico.cern.ch/event/823263/</span>](https://indico.cern.ch/event/823263/)
      - (Some) live notes:
        [<span class="underline">https://docs.google.com/document/d/1IcvpsgOPpVfaBeZpSCcKD6i1y4HesA-VJopOYV4S\_7c/edit</span>](https://docs.google.com/document/d/1IcvpsgOPpVfaBeZpSCcKD6i1y4HesA-VJopOYV4S_7c/edit#)

#### Planned meetings
  - Next week (July 17th): joint discussion on partial event building
    for real-time analysis within Institut Pascal
    [<span class="underline">“Learning To Discover”
    workshop</span>](https://www.universite-paris-saclay.fr/fr/real-time-workshop)
    (agenda tba today)
  - July 31st: [<span class="underline">joint ACTS
    meeting</span>](https://indico.cern.ch/event/830160/)
  - August 28th (tbc after contacting speakers): second part of
    trigger and real-time analysis meeting with LHCb & ALICE
  - September 10-13: IRIS-HEP Blueprint Meeting on
    [<span class="underline">Fast Machine Learning and
    Inference</span>](https://indico.cern.ch/event/822126/) + and
    FastML tutorials
  - October 2nd (tbc after contacting speakers): second part of
    software optimization meeting, with ATLAS, CMS and ALICE
  - October 16th (tbc after discussion with organizers): joint
    discussion with neutrino and astroparticle community,
    [<span class="underline">after JENAS
    workshop</span>](https://jenas-2019.lal.in2p3.fr)
  - November/December:
      - Meeting focused on reconstruction techniques
      - Hands-on tutorial on FPGAs

### Software Tools
  - Topic for meetings after the summer break:
      - A follow-up discussion on Trident
      - A presentation/demonstration from
        [<span class="underline">Tuning and Analysis Utilities
        (TAU)</span>](https://www.cs.uoregon.edu/research/tau/home.php)
        people
          - Trying to pin down someone from the team
      - A discussion GPU profiling
          - Need to see if we can contact someone from NVIDIA (via
            OpenLab)
      - A discussion on Hadrien’s valgrind plugin for numerical
        stability
      - A discussion on IDEs, i.e. see if we can invite someone from
        Microsoft on VSCode
          - There is some recent development on the
            [<span class="underline">remote
            development</span>](https://code.visualstudio.com/docs/remote/remote-overview)
          - (Gordon) I’ve been using this tool for a while now, and it
            was pretty amazing. At a local group I saw a guy present
            who was partly responsible in MS for the remote
            development code. Shall I see if I can get in touch with
            him?
              - Serhan : That’d be fantastic Gordon, thank you very
                much.
      - A talk on Mutation Testing
        ([<span class="underline">mull-project</span>](https://github.com/mull-project/mull))
      - A talk on test-suites he added to Phoenix (GSOC student,
        timescale?)
      - A talk on
        [<span class="underline">Nexus</span>](https://codimd.web.cern.ch/p/ByKnsM5xH#/)
        (a web app to store and organize binaries, libraries, RPMs
        etc.)
          - That would also be interesting for the packaging group.

### PyHEP
  - Preparations for the 2nd workshop, PyHEP 2019, have started. An
    announcement email will be sent next Monday or Tuesday at the
    latest.  
    \- Workshop taking place in the UK, at
    [<span class="underline">The Cosener’s
    House</span>](https://www.thecosenershouse.co.uk/), Abingdon.  
    \- Will run 2.5 days, October 16-18.  
    \- We welcome input and suggestions from the HSF already at this
    stage.  
    \- Facilities can accommodate 80 people.  
    \- Organisation together with Ben Krikler, a CMS colleague and
    [<span class="underline">UK Software Sustainability
    Institute</span>](https://www.software.ac.uk/) 2019 fellow.
  - The WG is organising topical meetings for after the Summer
    break.  
    \- The first one is penciled down for September 11th at 17h (same
    time as the Software Forum). It will be on fitting tools and their
    design, hopefully engaging with non-HEP communities.  
    \- Agenda is being put in place and an advertisement will come out
    soon.

### Training
  - See
    [<span class="underline">slides</span>](https://indico.cern.ch/event/785587/contributions/3266731/attachments/1776030/3097240/HSF_TEO_WG_update_11July_2019-2.pdf)
    attached to the agenda...
  - Software Carpentry @ CERN, 16-18 October.
      - (Unfortunately now clashes with PyHEP, but constraints are
        quite binding and we should go ahead.)
      - Order maybe better as Shell / Git / Python / C++?
      - Is 1 day enough to do much that’s useful in C++
          - ROOT focus may help, but teach modern programming (not
            ‘98), use ROOT7 interfaces
          - Is ROOT7 stable enough?
              - A lot still experimental though
              - To discuss with ROOT team

### Event Generators
  - Subjective report from Andrea (apologies, in another meeting)
      - Last [<span class="underline">meeting on June
        27</span>](https://hepsoftwarefoundation.org/organization/2019/06/27/generators.html).
        Many thanks for all the work and contributions\!
          - Further progress in accounting analysis, close to
            completion. Over the 2017 MC the fraction of time spent on
            generation (with respect to the MC production chain) is
            17% for ATLAS and 9.3% for CMS. Taking into account MC is
            around 70% of ATLAS and 50% of CMS of overall WLCG
            computing, this means generation is around \~12% for ATLAS
            and \~5% for CMS of overall WLCG computing. Still larger
            for ATLAS than CMS, but only by a factor \~2, not 10.
          - Report from Les Houches workshop in June: a lot of
            discussion about negative event weights and how their
            impact could be reduced to decrease CPU budget.
          - Top physics WG considering ttbar sample sharing between
            ATLAS and CMS.
          - Somewhat outside our usual scope, but welcome in the HSF
            WG: discussion of a proposal for Particle Data Group
            particle ID’s extensions.
      - Would like to define a few standard configurations for similar
        physics productions using different generators (to use for
        profiling and also as standard candles for hardware
        benchmarking and software comparisons. No progress on this.
      - Event generators are often discussed as a candidate workflow
        to exploit GPU based resources (e.g. HPC supercomputers). But
        we have not discussed this yet in detail in any meeting and I
        am not aware of any significant progress in this area. One WG
        member recently informed us that he is starting some work on
        this.

### Event Delivery Forum
  - Doodling for first meeting at the end of this month:
      - [<span class="underline">https://doodle.com/poll/n3ykm6knp6tv5uif</span>](https://doodle.com/poll/n3ykm6knp6tv5uif).

### Packaging
  - Met yesterday, minutes available
    [<span class="underline">here</span>](https://hepsoftwarefoundation.org/organization/2019/07/10/packaging.html).
    We discussed the Key4HEP stack project.
  - Next meeting 11 September.

### Frameworks
  - We have 9 nominees for the working group.
  - Names have been circulated and we requested comments by 25 August.
      - This is very long, but it’s summer and it would be hard to
        converge and organise anything before this time.
      - Comments to
        [<span class="underline">hsf-wg-search-committee@cern.ch</span>](mailto:hsf-wg-search-committee@cern.ch)
        (maps to Graeme, Liz and Michel)

### Visualisation
  - Phoenix GSoC project is going very well.
      - Github:
        [<span class="underline">https://github.com/HSF/phoenix</span>](https://github.com/HSF/phoenix)
      - Live demo:
        [<span class="underline">http://hepsoftwarefoundation.org/phoenix/</span>](http://hepsoftwarefoundation.org/phoenix/)
  - Experiment independent in browser toolkit, easy to use.
  - Would be good to present this.

## Workshops

### Pre-CHEP (2-3 November)
  - Wait for next Analysis WG meeting for progress.

### Next HSF/WLCG Workshop
  - Call for hosting institutes is out.
      - 3 interested so far.
  - Considering the constraints in May and June
      - June now looks very difficult (LHCC, LHCb Week, ATLAS S\&C
        Week, ATLAS Week)
      - In May 4-8 or 11-15 look possible (18-22 is Ascension Week,
        25-29 DIRAC Users Workshop)
  - Are there any more known clashes for **May 4-8** or **May 11-15**?
  - It would be very good to pin down a favoured date *now*.
      - We agreed that 11-15 May would be favoured.
  - Can we extend the deadline for institutes?
      - Early September should be ok - Graeme will discuss with the
        other organisers.

## AOB
  - Git repository for Harvester.
      - Harvester is PanDA’s new workload submission engine (deals
        with HPCs, dynamic cloud resources, other non-standard
        resources)
      - But it’s actually backend agnostic, so a request to host the
        code as an HSF project.
          - Part of Intelligent Data Delivery System (iDDS).
      - N.B. similar to things we currently do host, like CREST and
        Phoenix.
      - Agreed.
  - Summer break now, when to resume meetings?
      - Resume 29 August [as discussed after the meeting, on realising that
        5 September is Jeûne Genevois CERN holiday].
