---
title: "HSF Weekly Meeting #163, 11 April, 2019"
layout: meetings
---

# {{page.title}}

*Present/Contributors*: Graeme Stewart, Eduardo Rodrigues, Serhan Mete,
Pere Mato, Andrei Gheata, Daniel Elvira, Stefan Roiser, Andrea Rizzi,
Antoine Péruz, Liz Sexton-Kennedy, Paul Laycock, Torre Wenaus, Witek
Pokorski, Giulio Eulisse, Marco Clemencic, Heather Gray, Jim Amundson,
Michel Jouvin, Caterina Doglioni, Agnieszka Dziurda, Danilo Piparo,
Martin Ritter, David Lange, Brian Bockelman

## News, general matters
  - Preparations for the [<span class="underline">European Strategy
    Symposium</span>](http://europeanstrategyupdate.web.cern.ch) in
    Granada are underway - there will be a parallel session on
    software and computing, organised by Brigitte Vachon (McGill),
    Xinchou Lou (IHEP).
      - Graeme has been asked to speak on Software R\&D.
      - This will be based on
        [<span class="underline">inputs</span>](https://indico.cern.ch/event/765096/contributions/)
        received during the process (including
        [<span class="underline">our
        own</span>](https://zenodo.org/record/2413005#.XKxWtS-B2L4)
        from the HSF).
      - Do feel free to raise any key points that you think should be
        made there.
  - New *Event Delivery Forum* proposal - comments from Torre:
      - ATLAS has had its "event service" in production for some time,
        which assigns processing to workers with granulary down to
        event level, and returns results in a similarly granular way,
        well suited to using opportunistic resources with full
        efficiency.
      - Event delivery, however, still uses conventional mechanisms.
        The next phase of development has recently begun, the event
        streaming service (ESS), to intelligently deliver event data
        to workers, with latency hiding and with the possibility to
        prepare, filter and marshal data to use storage and network
        efficiently.
      - There need be nothing ATLAS-specific about this event delivery
        service, and Brian Bockelman has expressed interest in it from
        IRIS-HEP, where he's been developing the notion of an
        intelligent data delivery service (iDDS).
      - ATLAS and IRIS-HEP have decided to jointly develop the iDDS as
        a common project; the ATLAS ESS will be a specialization of it
        for ATLAS.
      - HSF seems like an appropriate home for this common project, so
        we propose that HSF host a google group and web presence as an
        'event delivery forum' which would be the communication hub
        for this effort, to which others are of course welcome
        (including lurkers\!).
      - *Meeting supportive and we agree that HSF is a good home -
        people welcome to also just ‘follow-along’ to keep an eye on
        developments.*

## Google Summer of Code 2019
  - Coordinators Report:
      - Students have now made final proposals.
      - 197 proposals in total. About 10 are not eligible.
          - One project (AWAKE) got 43 proposals.
          - Three projects got 10-15 proposals.
          - Most projects 2-9.
          - Thirteen projects got 0 (so they are out).
      - Mentors:
          - Rank the proposals, pick at most 3 that you would like to
            mentor. Precise criteria sent to mentors for the ranking
            by mail.
          - *Do this by Sunday 14 April.*
      - Maximum slots would be 41, but more likely to be similar to
        last year (29).
      - Slot request 22 April: some final adjustments after this date
        still possible up to the publication of accepted proposals.
      - Accepted proposals announced 6 May.
  - The Advisory Committee will be:
      - Pete Elmer (Princeton), Pere Mato (CERN), Michel Jouvin (LAL)
      - Intent and guidelines are described
        [<span class="underline">here</span>](https://docs.google.com/document/d/17ifO0i4O5JsBVKkcx3j75Z_iW2bXFnCbqFB2YirlJQw/edit?usp=sharing).
      - Organisers will provide as much information as possible to
        make it easy to generate the ranking.
      - Needs to be ready end of next week - most important thing is
        to cut the tail, rather than sort the top proposals.

### Google Season of Docs
  - A few projects have declared interest: Rucio, ROOT.
      - Don’t want more than 3 for this first test of this project.
  - Proposal to be written in the same way as for GSoC on the HSF
    website.
      - April 23 is the deadline.
  - Gaudi expressing some interest - what is the expected commitment
    from the project?
      - Not clear - Rucio have proposed 6-7 mentors to spread the
        load.

## HSF/WLCG/OSG Workshop
  - Summary
        newsletter:
      - [<span class="underline">https://hepsoftwarefoundation.org/newsletter/2019/04/03/Jlab-Workshop.html</span>](https://hepsoftwarefoundation.org/newsletter/2019/04/03/Jlab-Workshop.html)
  - Note that the [<span class="underline">newsletter
    section</span>](https://hepsoftwarefoundation.org/newsletter.html)
    of the website has been revived to do this.
      - This is ideal for writing any longer articles you’d like to
        see.
  - General questions were raised about very specific sessions vs. general
    workshop and the amount of parallel sessions in software and with the rest
    of the workshop.
      - Many people appreciated the overview that you could get from a
        wide set of software sessions that didn’t overlap much.
      - However, most groups felt they did not have enough time.
      - More cross-cutting sessions would be useful (WLCG/HSF).
          - But that would reduce per-group sessions even more.
      - Many valid points which are impossible to satisfy in
        parallel\!
      - We may have a better idea of what WGs want for next year, when
        the WGs that are running are much better established and know what
        they want from the workshop.

## Activity and Working Group Updates

### Data Analysis
  - Brief summary: very pleased with the two sessions, interesting
    presentations and lively discussions. Follow up topics for our
    next meetings have been announced for the start of May. Topics:
      - 2nd May:
        [<span class="underline">https://indico.cern.ch/event/813207/</span>](https://indico.cern.ch/event/813207/)
          - Workshop summary
          - Defining benchmarks - allow comparisons of different
            technologies.
          - Analysis description language - quite a lively discussion, a workshop
            organised at FNAL.
      - 9th May:
        [<span class="underline">https://indico.cern.ch/event/813208/</span>](https://indico.cern.ch/event/813208/)
          - Metadata - would like feedback from all experiments here,
            is there something we could provide (unlikely a
            one-size-fits-all metadata solution, but perhaps something
            akin to the TTree for event data).

### Detector Simulation
  - Very high-level quality of presentation; thought that having the
    talks not being experiment-specific was successful -- encouraged
    discussions prior to the workshop between the different
    experiments.
  - Would have liked to have additional time for discussion, but think
    that the workshop will be a good starting point for more in-depth
    discussions in the topical meetings.
  - Advertised two next simulation topical meetings, 8 May
    (accelerators) and 12 June (detector geometry description).
      - Need to create Indico entries.

### Reconstruction and Software Triggers
  - Brief HSF wrap-up: it went well!
      - RTA session:
          - Nice to see all LHC collaborations.
          - ATLAS and CMS have synergies on physics analysis, ALICE is
            mostly interested in detector calibration/reco in
            real-time, LHCb well advanced with a different trigger
            infrastructure but there are plans for ATLAS/CMS to
            attempt continuous readout and topic has been deemed
            interesting by trigger conveners in our preliminary chats,
            so we will continue the discussion.
      - Machine learning / reco session:
          - Talks were more heterogeneous.
          - JLab experiments interested to know more about LHC ones to
            avoid reinventing wheels.
              - Maybe things are too experiment-specific though?
      - Having speakers talk to each other in advance meant that they
        also talked to each other at the workshop without our
        “supervision”.
  - We may have a meeting on April 17th or 24th on summary of
    ATLAS/CMS cross-talk open to non-ATLAS/CMS members (after second
    cross-talk on April 4th).
      - Waiting for ATLAS/CMS conveners to get back to us on exact
        date (pinged).
  - Other ideas for future:
      - Organize taster sessions to coding on non-CPU, since high
        barrier to entry so far / not clear where resources are (maybe
        coordinate with Training group?).
          - HLS for FPGA
          - GPU programming
      - So far emphasis on trigger (possible bias from interest of ⅔
        of conveners), but would like to involve reco community more.
      - Invite LHC, dark matter and Dune communities to talk about
        their reconstruction algorithms.

### Software Tools
  - Highlights from the workshop:
      - **Profiling**
        [<span class="underline">TAU</span>](https://www.cs.uoregon.edu/research/tau/home.php)
        : *TAU Performance System® is a portable profiling and tracing
        toolkit for performance analysis of parallel programs written
        in Fortran, C, C++, UPC, Java, Python.*
          - Looks promising. We can contact the developers and invite
            them to make a presentation/demonstration during a meeting
            in the coming weeks.
      - **Profiling** Trident : This was discussed during one of the
        cost monitoring parallel sessions. We already had a
        demonstration from Servesh a few months ago. We can follow
        this up w/ Part-II.
      - **Static Analyzers** Coverity : Being used a fair bit. Seems
        to have had issues supporting latest C++ standards. However,
        the latest version seems to support C++17. CMS is using
        Clang’s static analyzers.
          - An idea here might be a presentation from one of the
            experiments to demonstrate how these analyzers are
            integrated into their frameworks, how the issues
            reported/followed-up etc.
      - **Packaging** Spack/Conda : Spack looks like the most likely
        candidate (especially for large-scale projects). Conda is used
        extensively by users.
      - **Packaging** `RPATH/LD_PRELOAD/LD_LIBRARY_PATH` conundrum :)
        There were a lot of discussions but no clear agreement on one
        or the other.

### PyHEP
  - JLab session was the 1st WG meeting per se.
  - 1.5 hours is a bit on the short side, to be honest.
  - The mix of “standard” talks and an invited talk from Anaconda was
    a good thing - several participants discussed with the Anaconda
    speaker during the session and workshop dinner.
  - We had lively discussions throughout the session - great.
  - Feedback was mixed, from very positive to “I did not understand
    the flavour of the session”.
  - Need to discuss what next steps are. Our WG is a bit special, as
    Python permeates various WGs/communities. For sure we need to
    coordinate certain activities, e.g., discussions around Python
    analysis tools with the Data Analysis WG (the DAWG convenors
    agree\!).

### Training
  - Sudhir will give an update in the next meeting.

### Packaging
  - We gave a talk and had quite a lot of discussion at JLab in the
    Software Tools session.
      - See the summary that Graeme gave at the last
        [<span class="underline">Packaging
        Meeting</span>](https://indico.cern.ch/event/802100/).
      - Main takeaway is that we need to advance with our prototypes
        and tests to the position where we solve significant pieces of
        the problem (e.g. FCC or LArSoft dependencies).
  - Next meeting 24 April.

### Frameworks
  - Touched on frameworks again during the Software for Accelerators
    session.
      - Which was judged to be a success.
  - Scope for re-starting activities based around use of accelerators
    and good models for heterogeneous programming, which was
    identified as a key missing piece at JLab.
  - FNAL would like to be involved in that - need an active group to
    take CWP work forward.
      - Do we want to have a nomination process for that, a la other
        working groups?
      - DOE are also interested in this because of accelerators -
        would support work in that area so that applications would be
        ready for new machines.
  - Try to come up with a proposal offline and then circulate it more
    widely.

### Software Forum
  - We have had no Software Forum meetings this year.
      - Run-up to JLab workshop.
      - Working groups all active and having meetings.
  - As well as any talks from experiments we’re not strongly engaged
    with or from other science domains.
  - Graeme happy to coordinate suggestions here.

## AOB
  - We should start to think also about the pre-CHEP workshop that we
    can have with WLCG.
      - Two days (Saturday 2 - Sunday 3 November).
      - Multiple rooms are available.
  - Easter holidays are almost on us, so many people away.
      - Agreed to have the next meeting in 2 weeks time, 25 April.
