---
title: "HSF Generator Workshop, 26-28 November 2018"
layout: meetings
---
# {{page.title}}

This live notes document is available to any participant in the workshop
to write down important points or conclusions from the workshop and to
identify areas where we will want to follow up or need to resolve open
questions.

Please use it - it’s an essential tool for the workshop’s memory\!

The Organisers

## Monday AM

#### CWP Challenges and Workshop Aims (Liz Sexton-Kennedy)
  - Generators critical part of what experiments do. Aware that
    “reward system” has limitations, need to improve on this. HSF
    CWP suggests reviewing software credits. HSF CWP has a section on
    generators and one on training and careers.
  - Estimated CPU computing resources needed for HL-LHC exceed those
    that are affordable on a “flat budget”. Pileup dramatically
    increases complexity. Need major reengineering of the software in
    all areas to be able to fully exploit HL-LHC potential. Especially
    need to exploit parallelism and vectorization of modern
    architectures, and GPUs are even more challenging.
  - Physics of interest at HL-LHC is at smaller cross sections and
    higher multiplicity.
  - Generators CAN be computationally intensive. Larger consumption in
    ATLAS than CMS. ATLAS US wall clock budget in 2016 had around 20%
    spent on generators.
  - NLO and beyond NLO pose large challenges. Theorist community
    continues to push development a higher orders. HL-LHC will drive
    need to ~~generate events~~ make predictions accurate at higher
    order.
  - Recap from Run1 to Run4.
      - Run1 mainly LO, O(100ms).
      - Run2 moved to NLO with O(10-100s) execution time.
      - Total grid times in an experiment depends on mixture of LO and
        NLO required by analysts.
      - ATLAS/CMS create O(10B) events per year, rule of thumb is MC =
        1-2x data events.
      - Run4 will collect 10x events as in Run2. Will need more
        precision hence higher orders. Will have more particles, with
        more phase space.
      - All within a flat budget…
  - Modernization means: many core, SIMD vectorization, NUMA memory
    hierarchy, offload to GPU/FPGA/TPU accelerators.
      - Need to inject engineering help. Move towards Open Source
        development is a way to achieve this.
  - Agenda of the workshop explained:
      - Introduction to generators for this mixed audience
      - Experiment needs
      - Technical requirements on modern codes
      - Status of main generators. *<span class="underline">Can we
        agree on a way to benchmark them?</span>*
      - Ongoing work on HPCs
      - Event reweighting? Share samples between ATLAS and CMS?
      - Status of generators used as “decayers”
      - NNLO status
      - Follow-up planning
      - Hackathon
  - C/ZachMarshall: reference list in CMS is a twiki, but also in
    ATLAS. There is also a common twiki between the experiments and
    the theorists can contribute
  - C/Zach about HL-LHC: collect 10x events, do we need 10x MC events?
    It depends on balance between statistical and systematic errors.
    In many cases we are limited by statistics and we do not need
    that.
  - C/StefanRoiser: for LHCb please get in touch with Patrick
    Koppenburg for reference lists
  - C/StefanoFrixione: not sure how many people read references, e.g.
    name of madgraph generator
  - C/StefanoFrixione: not sure what the needed precision at HL-LHC
    will be. A/Liz: hope that we get an answer to this question from
    the workshop.
  - C/AndyBuckley: generator codes are already “open” — but these are
    not things that can just be dipped into and have significant
    improvements made, as many have discovered. Impossible to do
    without close collaboration & discussion with authors… who will
    approve a huge & invasive pull request that hasn’t been previously
    discussed? Code hosting systems have also moved toward modern
    web-driven interfaces, but I don’t think that’s been a real
    limiting factor.

#### Introduction to Generator Codes (Simon Platzer)
  - Introduction to generators for a mixed audience.
  - Factorization at different energy scales: hard process
    calculation, parton shower algorithms, multiple interaction
    models, hadronization models. Event weight comes from hard cross
    section.
      - Hard process is exact calculation in QCD/QED perturbation
        theory.
      - *Most developments and computing power requirements sit in
        hard process calculation and parton shower algorithms.*
  - Hard process calculation and parton showers.
      - Jacobian factor to map unit hypercube of phase space to
        physical momenta.
      - At high momentum transfer, expand QCD in LO, NLO, NNLO and so
        on. *<span class="underline">Real and virtual contributions
        are separately divergent and cancel out. This introduces
        subtraction terms which lead to negative weights, this is
        unavoidable.</span>*
      - Landscape of infrared sensitive observables. At every fixed
        order of expansion, need more and more logarithm terms.
      - Factorization of emissions. Resummation and parton showers.
        NLO matching.
      - This is all state of the art for all major generators. In
        order to produce infrared safe predictions, negative weights
        are unavoidable.
  - Event generator structure is based on the factorization discussed
    at the beginning
  - Challenges
      - Negative weights spoil probabilistic interpretation
  - Q/AndreaValassi: has the issue of negative weights hit us already
    or not and how much? A/Liz and Simone Amoroso: it has hit us
    already, but this is only where NLO is needed. For instance some
    SUSY analysis went back from NLO to LO because of this. Simone:
    note that *<span class="underline">where NLO is needed and there
    are 40% of events with negative weights, we need 25x more events
    to generate\! If you can stay at LO, you have no negative
    weights.</span>*
      - C/Zbiszek: note that at LEP times the problem of negative
        weights was already there for QED but was eventually solved.
      - C/StefanoFrixione: disagree, IR is only one part of the
        problem leading to negative weights, and it is very difficult
        to design a catch-all solution.

#### ATLAS Needs and Concerns (Josh McFayden)
  - Generation is 20% in projected 2028 needs for ATLAS. But the slice
    will become more important as improvements come in fast detector
    simulation and elsewhere.
  - Majority of CPU comes from sherpa v2.2 v+jets setup, by far the
    largest and most precise samples.
  - Average CPU/event: 80s evgen, 240s fullsim, 45s fastsim, 60ds
    reco.
  - Thanks for all recent improvements to the theory community\!
  - Problems\!
      - Negative weights. If the fraction is \>25%, using full
        detector simulation becomes impractical.
      - Precision vs CPU. More precision needs more CPU.
      - Efficiently populating extreme regions of phase space.
  - Possible routes out
      - Can experiments help in generator development? Investigating
        funding of positions by the experiments.
      - Sacrifice speed for modelling/precision? Choose faster
        generator? Reweight lower precision to higher precision?
  - PRELIMINARY benchmarking
      - W+jets (2jets NLO and 4jets LO). Sherpa vs MG5\_aMC+Py8.
        Larger CPU and memory consumption for sherpa, marginally
        larger fraction of negative weights for MG/aMC.
      - Note that fraction of negative weights is not a relevant
        metric. You also need to know the spread of the values of the
        negative weights to understand their impact.
        *<span class="underline">Need to design a better metric for
        negative weights.</span>*
      - ttbar comparison, also including Herwig and powheg
  - Infrastructure
      - Common computing infrastructure for ATLAS/CMS?
      - Will generators run on CPUs or GPUs in 2028?
      - ATLAS and CMS sharing samples?
  - Summary
      - Many improvements in recent years
      - Certainly low hanging fruits. Event generation has not been
        highly scrutinised until now.
      - Optimisation can help, has to discuss how
  - Q: on slide 4, how much of generation is on the grid? A: do use
    the external sherpa pre-integration

#### CMS Needs and Concerns (Efe Yazgan)
  - Most LHC events are accompanied by hard jets, which are required
    or vetoed in many analyses, hence need MC predictions for them.
  - Most commonly used in CMS: MG5\_aMC@NLO+Py8
  - CMS software is C++ driven by python. MC production submitted to
    grid resources, software available via cvmfs. External generators
    called from CMSSW through an externalLHEProducer module.
      - Gridpacks: tarballs with precompiled code and initial phase
        space integration results. They are placed in cvmfs and
        accessed by remote jobs. In production, significant time spent
        in untarring the tarballs.
  - In Run2, generators were 1-10% of total CPU (per MC event,
    depending on type of MC event - not a % relative to full grid
    budget). Multi-leg NLO has negative weights up to 40%, larger
    samples needed.
  - Beyond Run2: much larger samples, larger alternative samples for
    systematic studies, precise tails of distributions need more
    precise predictions (NLO, hence negative weights)
  - Table with use of event weights for systematic studies
  - MG5\_aMV bias weights to reweight LO to NLO (see O. Mattelaer’s
    arxiv)
  - Needed developments
      - Timing comparison and understanding in ATLAS and CMS
      - Reduction of negative weights at NLO
      - Multi threading, vectorization, GPUs, reduce memory
        consumption
      - Faster phase space integration (neural networks, GPUs:
        10-5000x faster possible?)
      - Collaboration ATLAS-CMS, support positions
  - C/Servesh: estimates 10-5000 faster depend on how you compute
    this. C/Peter: in that paper, faster was for things that are
    already fast\!
  - Q/slide 7: why the difference in gridpacks between MG and sherpa?
    A: not sure
  - Q/AndreaValassi slide 12: do you actually see problems fitting
    jobs in 2GB per core for generation? A/Liz: in CMS we do share
    geometry in multi threaded framework
  - C/StefanoFrixione: not sure it’s a good idea to use the same
    generator evel events between experiments. Good that experiments
    cross check each other. A/Graeme: this will be discussed more in
    detail in tomorrow’s discussion.

#### LHCb Needs and Concerns (Phil Ilten)
  - *<span class="underline">LHCb designed as B experiment. Decays are
    the most delicate part and go through EvtGen.</span>* Handle
    \~5000 signal decays. Then LHCb expanded physics program and uses
    multiple purpose generators. 90% goes through multi-parton
    interaction (NOT message passing interface MPI\!).
  - All MC production is done centrally. Every job selects a model and
    an event type (i.e. a decay description).
  - GAUSS internals description. Includes pileup typically in pythia8
    and decay typically in EvtGen, plus ME and shower for specific
    generator. Pileup tool generally included at fixed luminosity due
    to luminosity levelling in LHCb running. Large number of
    generators for general purpose, soft and hard processes.
  - Recent developments to cope with Run3: filtered events, multiple
    trigger conditions, redecay, particle gun events. Gaussino in
    progress to be experiment-agnostic, for other experiments and also
    theorists. Also looking at options for faster detector
    simulations, including GAN and DELPHES.
  - Q/Liz on thread safety: did you discuss this for EvtGen?
    A/MichalKreps: will discuss this tomorrow
  - Q/StefanoFrixione: are you using Pythia6? A: no, working on
    eliminating it
  - Q/AndreaValassi: no problem with negative weights? A: not now but
    we will have a problem eventually
  - Q/Servesh: how do you load C++ libraries? A: typically compile
    time rather than dynamic. C/Servesh: good, compile time is much
    faster.
  - Q/SimoneAmoroso: so basically mostly run Pythia8 standalone? What
    is your event generation budget? A/MichalKreps: for many cases it
    is not a limiting factor as Geant4 is much more intense. But if
    the user imposes cuts to save time on Geant4, this puts more
    pressure on generation. A/GloriaCorti: yes in these cases
    generation is the dominant budget. And
    *<span class="underline">event generation budget fraction will get
    worse as we go to a faster detector simulation</span>*. We don’t
    run Pythia8 standalone but together with detector simulation.
  - N.B. MPI in this talk means *multi-parton interactions*\!

#### Practical Computing Considerations (David Lange)
  - MC production (generators plus detector simulation) is the major
    consumer of CPU on the grid. Requests come in bursts, driven by
    analysis deadlines like conferences. Gridpacks are a major
    enterprise for non experts.
  - Two approaches between experiments:
      - CMS like: gen+simulation, pileup+digi+trigger, reco. Good:
        generator is small part of gen+sim. Bad: generators change
        frequently, Geant4 you want stable instead across years.
      - ATLAS like: also separate gen from simulation. Allows more
        flexibility in generator software.
  - Grid runs 500k+ cores across 100 sites. Job slots 1-8 cores and
    1-2 days maximum wall clock time. HPC resources are spiky.
  - Aggressive code optimization of reco led to very large
    improvements in time/event.
  - Code should be robust to run B events. Startup time should be
    minutes not hours. Code should be runnable as a library in the
    experiment specific framework.
  - Common wisdom “generators small compared to the rest”, this is
    incorrect. Examples: gridpack untarring, move from LO to NLO and
    NNLO, filters with low efficiency for selecting events.
  - Examples of coding practices that enabled reco software
    improvements.
  - Examples of recent generator improvements in CMS. Had one NLO
    generation workflow where 99%+ was the initialization of NLO
    generator. Got a 3X improvement by improving specific functions
    and by doing initialization exactly once.
  - Software licenses
      - HEP converged on open source, but there are many such licenses
      - Experiment software becomes GPL by inheritance if it uses GPL
        components (although “derivative work” interpretation is a
        very open discussion). And GPL2 and GPL3 are not even
        compatible with each other.
      - Coming up now because experiments are trying to solidify their
        situations. CERN recently chose Apache2 to ease collaboration
        with industry.
      - We have to improve on software citation.
      - C/StefanRoiser: for LHCb licensing was a long and complex
        business. Chose GPL3 in the end.
  - C/StefanRoiser on workflows: LHCb is spending 70 to 80% of
    resources only in Geant4, will keep generators together because
    this makes it easier to run on unpledged resources without input
    data.

#### Discussion
  - Q/PhilIlten: how efficient are ATLAS/CMS in setting generator
    level cuts for specific users? A/JoshMF: depends on the sample,
    various approaches.
      - A/Zach: the closer to the ME you can put the cuts the faster
        you manage to get. *<span class="underline">Can some hooks be
        added to generators in a common standard way to set generator
        level cuts?</span>*
  - C/VitalianoCiulli: CMS some time ago was doing something like
    redecays, it was more reshowering. We had to do something inside
    Pythia to achieve that, but maybe it was not documented even if it
    is in principle reusable. A/PhilIlten: working with PeterSkands to
    do this in a more reusable way.
  - C/StephenMrenna about inheritance.
  - Q/JoshMF: *<span class="underline">did not really manage to
    understand yet why the ATLAS and CMS budget for generation is so
    different</span>*. A/Graeme: very difficult to answer this
    question here, but we should identify at the workshop ways of
    working on this, by putting the relevant people
together.

## Monday PM

#### Performance Optimisation Introduction - Why should we care? (Servesh Muraidham, IT-DI-WLCG, UP Team, CERN)
  - Technical optimization is the focus, it can not be an after coding
    activity
  - Moore’s Law still working after 42 years but Denard scaling was
    stopped by power consumption.
  - GPU FP performance for non-terminated lines is ether flat or
    dropping
  - Post free lunch - Agricultural performance is improving danger in
    lock in to a specific architecture, note the Xeon Phi cautionary
    tale
  - Roofline Performance Comparison - represents how well an algorithm
    for a specific architecture - defines the concept of operational
    intensity
      - DGEMM is the Linpack benchmark
      - Recommend finding the flops/ byte for your algorithms
      - Cautionary tale of the chinese supercomputer - a top entry at
        SC but not useful for science - on the other hand some SC
        sites take input on kernel benchmarks to use
  - Vector Operation discussion
  - 60% of the compiler implementation is devoted to loop optimization
    so it is wise to allow the compiler to understand your loops
  - Algorithms can be classified into 4 types, figure out which one
    yours is suited to
  - Ideal programs have computational kernels - HEP codes don’t have
    them, why? Maybe too many years of optimizing hot spots?
  - Discussion of the topic of the cost of virtual functions and
    templates

#### Optimising Memory Use (Sebastien Ponce, CERN)
  - The memory problem - relative to CPU speeds memory access is
    extremely slow (100x), mitigated by hierarchical cache structure
  - Make sure stack variables are \<1kbyte, within current scope but
    allocation is almost free
  - Big objects go on the heap but they are very costly to allocate
  - Pro-Con struct of array vs. array of pointers, the latter scatters
    the memory and creates many small allocations - the latter will
    thrash the cache
  - Contiguous memory blocks must be used to limit the thrashing
  - When using a vector of structs make sure you use “reserve”
  - Array of Structures vs. Structure of Arrays which is best depends
    on the algorithm applied to the data SofA would be bad for a sort.
    SofA is best for vectorizable algorithms
  - If the consumer of your data has different algorithms there is no
    best answer (no magic)
  - Profiler tools, 2 types:
      - Vtune from Intel - uses internal processor counters, gprof is
        in the same category
      - Callgrind - open source and simulation a processor, downs side
        is this is slow

Don’t share data across cores, spread them across threads, another
reason to use stack variables

#### Performance Discussion
  - Is deep inheritance expensive? - yes if it virtual , avoid
    multiple inheritance , do use the initializer list with empty
    constructor bodies, this removes initialization ordering fragility
  - Branch predictions and look ahead should be automatic with good
    code , why don’t we have good code? Servesh says we are
    overwhelming the front end with lots of instructions. If we moved
    the code to be SIMD efficient it would alleviate this problem
    automatically.
  - How do you strike a balance between reliability and optimization?
    A: With the tools available today, there is no longer a conflict.
    You can have fast and readable code.
  - Don’t be afraid of specializing templates
  - Don’t be afraid to rewrite your prototype code
  - Understand the limitations of the abstraction and concept
    programming you do
  - Shouldn’t you code for the common case first not the corner one?
    Yes but remember the memory wall and think about how your
    algorithms use the data first.
  - Do code reviews help in readability? Experts think yes.

#### Sherpa Status and Plans - Marek Schonherr, CERN
  - The framework:
      - Two ME generators...
  - Available physics simulations
  - Changing scales and PDFs / alphaS(massZ)
  - Code structure diagram - modular component structure loaded
    dynamically - same technology used for user definable functions
  - Run Strategy 1. Initialization, 2. Integration, 3. Event
    generation
      - The first two steps can be done once and results are platform
        independent
      - Step three is done on the grid
      - The second step is MPI parallizable
  - Code performance tables
      - Confident that x10 size performance improvements are possible
        for the worst case NLO sample
      - There are places where small compromises in physics
        performance can lead to major technical performance
        improvements
  - Walk through callgrind plots - at LO unweighting procedure
    dominates time - at NLO also dominated by unweighting and matching
  - Weight distributions and how they relate to performance - need a
    better approximation of integrand
  - If we have to fall back to LO because of performance it is better
    to use the HT prime approximation
  - Can there be a way to use static linking when in production and
    don’t need the flexibility? A: it can be done but Taylor found
    that he only gained 20% (doesn’t sound bad to Markus)

#### aMC\_@NLO Status and Plans - Olivier Mattelaer
  - The uncertainty @NLO - it is possible to trade speed for disk
    space, allow reweighting with future pdf
  - Limitations of the re-weighting
  - Re-weighting for mass scan
  - NLO re-weighting
  - MadGraph is compiled with (-01) but not much better at higher
    level (tested at O3)
      - \-Ofast makes it 30% faster at LO/NLO -\> however it requires
        validation since messes with the math functions
  - MPI strategies
  - Timing results and resulting mpi scaling as a function of the
    number of ranks - there is a point where you lose by adding ranks
  - LO doesn’t scale to higher then 500-200 rank however it doesn’t
    need high bandwidth communication so can run on a tier2
  - HTC vs HPC chart - argues that HTC is better for constant cost -\>
    started discussion of owned vs. borrowed resources
  - GPUs - plots comparing CPU to GPU performance as a function of the
    number of jets, also as a function of number of gluons in the
    final state
  - CPU vs. GPU - no clear winner but likely winner is GPU
  - Q: Is the MG5 port to CUDA in 2011 still working? A: yes, could be
    improved
      - C: very good, we need any code running on GPUs to exploit
        latest HPCs
  - Q: Is MPI only for integration? Generation? Or both? A: it is only
    for the integration

#### PYTHIA 8 Status and Plans - Philip Ilten
  - History - lasted release will appear in March, another planned
  - Documentation - lots of references
  - Decided to be user-friendly
  - Focuses on everything but ME generation
  - Phythia is thread-safe except for adaptive maximum
  - Special constructors for multiple instances that save time
  - External pointers in the interface allowing lots of customization,
    even hooks for Heavy Ion generation
  - User defined hooks can interrupt and customize different parts of
    the internal work flow of Pythia
  - Supports both HepMC2 and HepMC3 and can read in LHEF, SLHA
  - News -
      - HI support with collective effects and alternate models for
        string fragmentation
          - Developed by Leif Lonnblad and Christian Bierlich JHEP
            1810 (2018) 134
          - Can use gridpacks
      - Full integration of DIRE and VINCIA parton showers
      - Lots more see slide 11
  - DIRE from Stefan\*\*2
  - VINCIA by Peter Skands and Nadine Fischer
  - Shower Variations by Stephen Mrenna and Peter Skands
  - Dark Matter Models by Nishita Desai
  - Deuteron Production by Phil Ilten
  - Merging algorithms are slow and they are working to improve them
    almost a bug fix
  - Phythia CPU consumption may be small but it is used everywhere so
    the integral can be significant - can you work on the MPI? A: Yes
  - LHC specificity happened in the transition from P6 -\> P8

#### Herwig Status and Plans - Peter Richardson, CERN
  - Designed for hadronic physics
  - Strong emphasis on accurate simulation of QCD
  - Became unmaintainable so moved to C++ with Herwig7 - understanding
    the code was of high value
  - Tried to balance performance vs physics and maintainability
  - They rely on externals much less because it turned out that the
    interfaces to externals were more prone to error
  - Structure chart
  - Done with fortran conversion
  - Improved NLO matching
  - Work on uncertainties and reweighting
  - Improvements in soft physics
  - Recent work on Baryonic Colour Reconnection
  - Future
  - All of these are physics improvements - that’s what gets noticed
    in the theory community and gets funding and jobs
  - In Herwig the biggest speed/memory improvement would be to improve
    NLO

#### POWHEG Status and Plans - Emanuele Re, CERN & LAPTh
  - Status of the repository
      - A legacy version in svn
      - V2 also in svn but more modular components
      - RES with just a few processes
  - Powheg needs external parton shower
  - Recent physics Applications
      - W+W- very computationally expensive for decays at NNLO+PS
      - More examples on slide 3
  - Default output is unweighted events - at times weighted events are
    needed
  - Negative weights can appear despite the acronym in the name
      - Can be limited through “folding” -\> runs become longer as
        number of calls to real matrix elements increases
      - Folding costs time but for complicated processes it is a
        balancing act
  - Different steps can be parallelized but there is a synchronization
    point between steps
  - Can detect “bad” (unstable points) grids to avoid including them
    in the next step
  - … more facilities on 5
  - Some facilities come from interaction with experiments and this
    will likely continue
  - No effort to support new architectures or increased
    parallelization
  - NNLOPS reweighting works but it’s CPU intensive
  - MiNLO merging for processes with light partons in the final state
    - there is a proposal that suggests a possible avenue for further
    progress

#### Discussion
  - Josh: is benchmarking exercise redone for each release? (a general
    audience questions) - it’s useful, we hope that support for this
    will continue
  - Can there be unit tests for physics validation?
      - Yes, this is done for Herwig made difficult by multiple
        changes occurring per release which is benchmarked
  - Validation discussion
      - As complex for the generators to evaluate expected changes as
        for the experiments
      - High statistics are often needed - implying a large resource
        pool

## Tuesday AM

#### High-multiplicity multi-jet merging with HPC technology
  - Traditional approaches to generating high-multiplicity jets does
    not scale.
  - HDF5 is used as it’s optimal for parallel access on HPCs.
  - Processing compressed HDF5 files is x2 faster than the
    uncompressed files.
  - Each jet multiplicity is done explicitly and separately, but they
    do need to be added together (merging with CKKW-L).
  - Scaling is good, but not perfect - still being investigated.
  - Q. HSF is working on “ferries” to transform between data types -
    **HDF5 seems very useful for LHE data, can this be made available
    as a library?**
      - Conversion of 65M event files from LHE XML to HDF5 took 17
        hours (single thread). (Note: that’s 1kHz, \~1MB/s.)
      - Added direct HDF5 output as a plugin for Sherpa, will be in
        future releases.
      - SciDAC projects have to produce “open source” products.
  - Q. What inter-rank communications is there? A. For particle level
    more or less none. For the ME this is done using existing Sherpa
    MPI implementation.
  - Q. Is it time to update the LHE format?
  - SP. Pythia has added direct support for reading these HDF5 files,
    will be in a future release (once stabilized).
  - FS. Can move the expensive parts (ME) to HPC, then just do the
    particle level within the experiment software. Good also for
    sharing ME between experiments and with the theory community. How
    reusable are the MEs? A. Could tighten cuts, but would become a
    bit less efficient. However, quite some variations in what can be
    done at the particle level (blue), so expensive ME generation
    (red) can be reused, saving a lot of
time.

#### A novel workflow of generator tunings in HPC for LHC new physics searches
  - Q. HPC specific part is generating MC events, which is trivially
    parallel? A. Yes, no parallel communication, so HTC would also be
    fine for this.
  - Q. Do you need load balancing between the ranks? A. This is
    handled by the DIY toolkit (also used in previous example). Phil
    noted that imbalances between per-event times are a real issue, so
    this kind of dynamic balancing is very useful.
  - Advantage of load balancing on a cluster is that far less
    bookkeeping is needed in the end (cf. really independent jobs +
    merging on the grid).
  - Q. Did you consider Bayesian optimisation method, which offers
    advantages of priors, etc.? A. Yes, it’s been considered, but not
    yet really explored.

#### Adaptive multi-channel integration with MPI
  - Implementing MPI is not just a technical task - one needs to
    understand the program’s purpose, so needs physics input.
  - Use MPI features - they work very well and are written and
    supported by experts (don’t reinvent this wheel, you will fail\!)
  - Shared cluster made benchmarking difficult.
  - Hybrid parallelisation provides an extra speed-up (OpenMP + MPI).
  - Q. Does the integration do adaptive scheduling? A. No. Would be a
    future improvement.
  - Q. How difficult is it to collect the grids? Minor grouping or
    just one big reduction? A. It’s just done on the master, so that
    is a slow part (serial) at the end.
  - OpenMP/MPI is also useful for NUMA architectures.

#### Optimising Generator Usage
  - 1 - Reduce CPU requirements by running large scale event
    generation at LO
      - FS. Q. If things are flat in phase space it’s easy, but if not
        flat then each analysis needs to apply their own corrections
        (per *analysis*). So wouldn’t you need N(N)LO at the detector
        level anyway? So what is the gain?
          - Can save a factor x10 in CPU. (FS was sceptical)
          - No negative weights at LO.
          - Generation itself is also faster.
      - NLO merged you can do at the truth level.
      - Stefano. Q Generating 8 jets is technically impressive, but is
        it needed - problems in the merging? A. Yes, the merging needs
        to logarithmically be as exact as the ME.
          - FS - there was some work that showed this is under
            control.
          - Can use Holger’s work to do cross checks.
      - StefanH - NNLO is coming, but will not be as efficient as LO
        simulations.
          - Stefano - not saying anything about NNLO. NNLO will be
            doing a small number of processes only. LO can do
            everything.
          - NLO matched calculations do exist for inclusive processes.
            MC limited, not ME limited.
  - 2 - Reduce computing costs by sharing unweighted matrix-element
    event samples between experiments
      - Few input parameters.
      - Q. Josh - what are technical hurdles for sharing files between
        CMS and ATLAS? A. Liz, did not work in the past. Now can share
        this in the same way that we do for OpenData, so technical
        limitations not there anymore.
          - Just the computational part - not the
            showering/hadronisation, so storage requirements are
            minimal.
      - Q. Does it affect how experiments run jobs? A. Not much -
        changes the “splitting” line a bit.
      - Q. Don’t different generators do this already? A. In some
        areas. Would want this to be completely open, feed back to
        theorists.
      - Want to share more widely, but LHCb are in a different region
        of phase space, not clear real savings would happen.
          - Can also share intermediate pieces of computation.
      - Q. Who would actually do this? How to get credit for it. A.
        Give DOIs to the data (CERN product - gives attribution).
        Figure out how to actually fund people.
      - Q. What about **cross-checks**? Experiments do this today
        because they are independent. Past experience shows that these
        checks are important. A. Yes, cross-checks are important. SH -
        can do this with different pieces of samples. Q. But what
        about different physics? A. Would have these differently for
        each generator anyway, so that allows for checking across
        different generators. This also alleviates the technical
        difficulties. Josh - we don’t cross check at all at the
        generator level today, so we’re not really losing much.
      - Q. Generating event weights is fast for LO, not much saved
        (detector simulation is the expensive bit). Different for
        N(N)LO though. A. Parton level calculation only - can, e.g.,
        combine samples.
      - Q. Intermediate suggestion - common configuration of cards.
        Share these as they are difficult to get right. A. Marek - for
        Sherpa this is no-brainer. But traditionally ATLAS and CMS
        could not agree on a common tuning for Pythia.
      - Josh - scrutiny should actually go up\! We would have two sets
        of eyes on the setup. Simone - without this we may be
        *limited* in N(N)LO computations and would lose physics. Frank
        - having more theory input helps here too. Peter - beware of
        diminished responsibility.
      - Q. Andrea - does this help with correlation of systematics?
        Yes. But the shower tunings also important.
      - Economics of doing this? People are not being “paid” to do
        this - just part of their physics analysis. What’s the
        motivation to help the other experiment? Don’t want to lose
        the analyst support. Josh - not sure this distinction is true.
        MC convenors are analysts. Davide - everyone needs the common
        samples (W+jets). Common samples will be managed “centrally”.
        Zach - V+Jets, Single Top, and done - not so many samples.
      - Simone - sociologically it would seem to work better to do a
        common sample rather than share existing things. Get buy-in
        from people who will use this.
  - 3 - Other topics
      - Technical RAs making “deep” contributions into MC teams.
          - Zach - experiments are not dripping with software experts.
            What person would do this job? Need a career path.
          - Liz - another way to help would be to modernise software
            practice, open up code to allow pull requests. A. Code has
            always been open. Current version of HEPForge should
            support direct pull requests. Andy - communication is
            important, needs to be a conversation between main
            developers and submitter. Pull requests out of the blue
            are not desirable, given complexity of the systems and
            potential side-effects.
          - Servesh - need a dialog between engineers and physicists.
              - Andy (on Vidyo): “Since time & question bandwidth is
                limited, I may as well write here that I don't think
                pull-request GUIs are a silver bullet for getting
                experiment RA/sw engineering contributions to MC
                tools\! They're nice, but a minor effect IMHO.
              - The sw/performance issues are \*big\*, and require
                significant time investments. If this work isn't
                valued and rewarded, most will not bother... the
                social & career incentive obstacles are much bigger
                than the mechanism for providing patches.
              - Plus, understanding these codes in sufficient detail
                to make significant changes is not something that
                comes without a detailed & lengthy conversation with
                the authors.
      - Better alignments to needs of experiments
          - Ease of use is a big point to improve on.
          - Andy - ATLAS are generating a lot of samples with heavy
            filters - not very efficient. Generator side improvements
            (biasing) would help a lot.
          - Marek - had a student to work on common API, but problem
            is that it’s only applicable to simplest processes.
          - Josh B - analysis groups will do as little work as
            possible (even if it’s wasteful). Need to push groups to
            do this and also teach people how to use the generator
            functionality properly. Zach - examples of issues from
            ATLAS could be given back to theory people and used to
            improve the documentation. Marek - need the documentation
            there, but people also need to read it (\!) to avoid
            inefficient setups.
          - Zach - would be great to have a “production mode” switch
            for generators (like Madgraph), turn off all the bells and
            whistles.

#### Photos and Tauola Status and Plans
  - Q. Is there any plan for being thread-safe? A. Initialisation is
    done in one place - common block. Can pass that to different
    “workers”. Not too worried about speed, it’s fast.
  - Liz - experiments can deal with pattern of initialisation serial,
    but event loop needs to share data read-only. A. There is one
    place where data would be shared (histogram); different random
    number generators can be plugged in already.

#### EvtGen Status and Plans
  - EvtGen written and maintained by experimentalists.
  - Modernisation from Gerhard has now overwhelmed GitLab web
    interface (\!) - many improvements\!
  - Multi-threading is next, will require new interface to the random
    number generator
  - HepMC 3 transition will take a few more months and help with
    threading issues.
  - Pythia8 could be used to replace Tauola; but Photos functionality
    is really needed, no current alternative.
  - Profiling shows lots of low hanging fruit for investigation
  - Dealing with HepMC files (used in Photos interaction) takes a lot
    of time.
  - Q. Z - which version of photos and tauola are used? A. Think it is
    the latest one.
      - Changing interface to “shared” object would be very hostile
        for threading.
  - Two postdocs will contribute to multi-threading conversion effort,
    as well as some help from Michel.
  - Q. Zach - How do you get the decay table?
      - PDG tables cannot be used directly in a computer problem
        (\~disputed).
          - Problem with branching fractions.
      - Is this something HSF can help with?

## Tuesday PM

#### NNLO / N^3LO calculations with NNLOJet
  - NNLOJet is framework for NNLO calculations using Antenna
    subtraction - fortran + openmp + python, depends on LHAPDF.
  - Three processing phases, but dominated by random-number seed
    driven “production” phase -
  - Jumps to N3LO from NNLO increases CPU by 2-3 orders of magnitude.
  - How does this get then used by experiments (eg, to put 100k hours
    in perspective) - experiments answer that they don’t this in
    production - may be via analyst driven work. Sounds like this
    might evolve towards HL-LHC - eg, precision needed in MC event
    generation. \[reweighting + final theory comparisons as opposed to
    MC events\]
      - Q/Andrea: This is not unweighted. How will experiments use
        this? My mental model now is we will do LO unweighted (ok),
        some NLO unweighted (problem with -ve weights, but okish),
        plus complementary info from NNLO, eg some distributions with
        very fine binning for some specific analyses. Is this a
        correct model? A/Simone: yes now this is what we can do, but
        in 10 years we will probably have this NNLO unweighted and
        this will be the bottleneck. C/Andrea: yes but the question is
        whether the NNLO unweighted will be money affordable at that
        time...
  - Scales “badly” with \# of particles. Something to follow
  - HPC discussion suggests that this sort of calculation is a good
    use case.
      - CERN’s collaboration with PRACE may be useful here

#### NNLO calculations with Matrix
  - Matrix requirement sare LHAPDF and numpy (plus more dependencies
    inside)
  - Parallelizm is across processes, batch support built in
  - Nice comparison of CPU vs uncertainty - bottom line - days @ NNLO
    vs minutes @ NLO vs seconds @ LO

#### NNLO calculations with MCFM
  - Linear scaling via MPI - 1% precision on NNLO cross section O(1
    hour) on desktop. CPU for processes with jet O(1000 hours)

#### Beyond Current Paradigms
  - Fixed order calculations - cross sections, not really events
    anymore. Or are we just doing "more of the same"?
  - Large production runs will probably become inaccessible to
    theorists.
  - Andrea - will probably always need unweighted events with detector
    simulation. Driven by physics.
  - Lattice get specific grants to do specific calculations -
    something like this probably becomes the norm. Would be infrequent
    and require some community agreement.
  - Accuracy of the calculations - if something takes 6 months to run
    then this is probably not debuggable - then not trustable. If
    parallalisable then it could easily foresee 10k cores for some
    hours.
  - HSF/LPCC group proposal - identify interested people to build on
    the sort of discussions during this workshop.
      - Andrea volunteered with computing resources point of view
      - 
  - Unfolding - experiments have very different needs in this area.
    Not clear if increasing order helps - often harder to match to
    data. Recent ATLAS paper (Hbb?) just used Pythia8, but with
    sophisticated unfolding.
      - Key point is to describe the data well - if LO does that then
        could be enough.
      - Should be testing unfolding in a number of different
        scenarios.
  - Should be careful about what we mean by “right” - uncertainties
    always exist and we have to balance them. Recent changes towards
    investment in understanding theory systematics
  - Inclusive cross sections and unweighted events have both proved to
    be useful in LHC analysis.
  - Landscape changing - era of ‘fast’ searches are maybe coming to an
    end.
  - Back to negative weights - can we judge if we are happy with 20%
    negative weights? Introduces the discussion of reweighting schemes
    and their use for systematics. When are they robust enough to
    avoid sending events through G4 simulation.
  - Lots of theory advances - this workshop should focus on areas
    where improving the codes’ engineering will help.
      - Need people to work together on this problem.
      - Testing important.
  - If there’s a need there should be a reward\!
  - Codes are evolving all the time - not clear that the languages
    used are optimal, but that’s the code we have. Be simple.

Take Home Messages / Actions / Planning
  - Generator performance comparisons work
      - Broaden this activity
      - Understand differences between ATLAS and CMS - e.g. two things
        to understand
          - Comparison of sherpa and MG for the same process
          - Are the two experiments producing very different types of
            samples or configurations? Is ATLAS producing more or more
            expensive events?
  - LHCb is different from ATLAS/CMS as generation focuses on decays
  - Regression tests (for physics results AND timing performance) and
    best code practice
      - The HSF can help with this (a lot of technical experts)
      - Can the experiments help with their infrastructure for timing
        regression?
  - Projection of CPU needs for Run4
      - The fractional budget of event generation will increase as
        experiments move to fast simulation and faster reconstruction
      - Model for use of LO, NLO and NNLO?
  - Best ways to support technical work in generator field
      - Experiments
      - Engineers (how to fund this - grant applications?)
      - Prospects for ‘permanent’ jobs (i.e. not just two year grants)
  - Generators critical part of what experiments do. Aware that
    “reward system” has limitations, need to improve on this.
      - Physics improvements are what gets noticed in the theory
        community and therefore gets funding and jobs. Example
        speed/memory improvement in Herwig (matrix elements and NLO
        integration) would be “many years of work for little
        recognition”. (see Peter’s presentation)
  - GPU ports / code portability? Are experiments interested in
    using/validating, particularly Madgraph.
      - Supercomputers/HPCs are going more and more towards GPUs.
  - A dedicated performance workshop in the future (Spring?)
      - Say 5 days of real hands-on work
  - Negative weights are a problem (but only in NLO, there are none in
    LO). These come from cancellations of real and virtual
    contributions and are unavoidable. “Unweighted” events with
    negative weights means that events have weight +1 or -1
    essentially.
      - Need better metrics to understand the impact of negative
        weights. Example: scalar metrics integrating the knowledge of
        the weight distribution and also the relative cost (in CPU
        budget) of detector simulation vs generation.
  - Can a common hook be added to generators so that we can set
    generator level cuts in a standard way?
  - HSF has Working Groups in important areas of work for HEP. This
    area could benefit from the same.
      - Some convenors willing to carry this forward and organise?
      - Collaboration with LPCC has been very fruitful - should be
        joint activity
