---
title: "HSF Weekly Meeting #153, 13 December, 2018"
layout: meetings
---

# {{page.title}}

*Present/Contributors*: Graeme Stewart, Andrea Valassi, Serhan Mete,
Gordon Watts, Pere Mato, Danilo Piparo, Tommaso Boccali, Paul Laycock,
Heather Gray, Giulio Eulisse, Witek Pokorski, Charles Leggett, David
Lange, Agnieszka Dziurda, Daniel Elvira, Andrea Rizzi, Marilena
Bandieramonte, Caterina Doglioni, Gloria Corti, Eduardo Rodrigues, Steve
Mrenna, Jim Amundson, Josh McFayden, Martin Ritter, Liz Sexton-Kennedy

New Working Groups Reports
==========================

Data Analysis
-------------
-   The conveners met twice since the start of their mandate.
-   Good agreement about the high level objectives for 2019.
-   Scheduled a pre-Workshop meeting with experiments’ representatives
    of the analysis community on 23rd January.
    -   Will be open.
    -   Comment: Try to reach out to whole analysis community (not just the main
        convenors).
-   Plan to rename the CWP analysis mailing list to the Analysis WG one.
-   Wrote a mandate for the group, which will appear as a PR to the HSF
    main website:

    > The Data Analysis Working Group aims to eliminate time spent by
    > physicists working on monotonous and laborious tasks while performing
    > physics analysis, and make the publication of physics results
    > efficient both in terms of human and computing resources. To this end,
    > the group will prioritise capturing the requirements of physics
    > analysis across the HEP domain, aiming to gain a detailed
    > understanding of the needs of physicists by direct consultation.
    > Engagement of those people experienced in working at the coalface of
    > physics analysis will be critical to the group’s success. As a close
    > second priority, the group will work with pioneers of technology, both
    > inside and outside of the HEP community. The goal is to build bridges
    > between physics analysis experts and technical innovators, fostering
    > collaboration between these two communities to produce optimal
    > solutions to a well-defined set of problems.

- Please feedback on this (noted that "coalface" was not well understood by North
    American colleagues).

Detector Simulation
-------------------
-   The conveners met for a first discussion on 5 December.
-   We discussed the overall scope of our group.
    -   Clarified that generators will be outside the scope of the
        simulation group.
-   We brainstormed on topics for the workshop in March.
    -   We’d like to request grouping the HSF topics such that a three
        day attendance to the workshop would be possible.
    -   At least 2 slots.
-   We also made a list of ideas for upcoming topical meetings.
    -   Would like to start scheduling these.
    -   First topic would likely be fast simulation.
-   Our next discussion will be on 17 December at 2 pm.
-   Fast simulation meeting early February.

Reconstruction and Software Triggers
------------------------------------
-   30/11: first discussion among convenors.
-   Request to rebrand ourselves from “conveners” to “organizers” (can
    be discussed at HSF meeting).
    -   Not clear what the best replacement would be, but open to
        suggestions.
-   Plan:
    -   Use Christmas break to familiarize ourselves with the various
        efforts in different experiments (will start a google doc of
        our own with interesting reading material).
    -   After Christmas, reconvene and write a short advertisement talk
        for the existence of this new group.
        -   Talk to trigger / reco conveners from the different
            experiments
            -   Caterina: ATLAS/ALICE
            -   Agnieszka: LHCb/Belle2
            -   David: CMS
            -   Neutrino community (DUNE) - contact Kirby and Heidi
                Schellman to get a good name if you don’t already have
                one.
            -   \[would like to have input from other future experiments
                as well, how to be inclusive && selective at the same
                time? Possibly speak to Physics Beyond Colliders
                effort.\]
        -   Understand individual challenges (used as input to workshop
            organization).
            -   Point we can already think about:
                -   Integration between trigger and reconstruction.
                -   Common tracking effort (ACTS).
                -   FastChain (reco+simulation) - coordinate with
                    simulation WG.
        -   Present short talk at their meetings and gather feedback.
-   General agreement about using Christmas to think about detailed
    structure and work of the WG, then write short specific mandate
    and open mailing list.

General Point
-------------
- It's a good idea to revive the HSF newsletter now.
  - Can start with a general New Year newsletter.
  - Groups can then use this as a way to publicise their activities.

HSF/WLCG/OSG Workshop News and Planning
=======================================
-   [*Indico*](https://indico.cern.ch/event/759388/)
-   Registration is open.
    -   13 people registered so far (but a lot of people planning to come, we
      believe)
-   Block timetable in place.
-   Plenary sessions (Graeme’s thoughts):
    -   Monday looks strong - experiment talks, WLCG evolution.
    -   Tuesday less so - tech watch is good, but then a lot of
        facilities oriented sessions, unclear relevance for software.
        -   Idea 1 - we take some afternoon slots as HSF parallel
            sessions.
        -   Idea 2 - make a session on “new workloads, new facilities”
            -   Pose the questions: what work do we need to do in the
                future that at the moment is not well provisioned
                (e.g. ML training on GPUs); what hardware/facilities
                are available from resource providers that we are ill
                placed to exploit (large GPU resources at HPCs)?
        -   Idea 3 - shift that Tuesday to Thursday.
    -   Wednesday, Thursday parallel slots:
        -   Session is organised to have 4 x 90’ slots each day.
        -   So we have 8 slots available:
            -   Maybe not be enough? (2 sim, 2 analysis, 1 reco, 1 PyHEP,
                1 tools, 1 frameworks, 1 Training…).
            -   Can add 1 or 2 on Tuesday.
            -   In any case, need to decide ASAP what we actually want.
            -   If groups organise in a single HSF "track" need to make
                sure material is relevant to all (could have HSF parallel
                  sessions for more technical topics).
        -   Should we organise a session on “Accelerated Workloads”?
            -   Discuss community ideas and experience around using
                accelerators (ideas: event generators on GPUs, LHCb
                port of HLT1 to GPU, CMS Patatrack, ML training
                workloads, …) - one easily reaches a 2 slot session.
            -   This could also be a nice focus to fold in the framework
                integration (instead of separate slot)
            - Generally this suggestion well received.
-   Practical matters:
    -   Block booking the Marriott looks to be good value.
    -   Car sharing from IAD recommended.
    -   Flights from GVA are (for now) quite cheap.

EPSS Strategy Document
======================
-   Got really useful feedback and the document got a bit longer, but
    definitely improved.
    -   Still short, but gives some more details on why the problems are
        so difficult and makes more definite suggestions for what investments
        are needed in the future.
-   “Live” copy on [*Google
    Docs*](https://docs.google.com/document/d/1emvkqUz6sq3P6JeYIeEZozJdNkA6A6otP8XezPBgOxs/edit?usp=sharing),
    a snapshot is attached to the agenda.
-   Please finish commenting by end of tomorrow. After that Graeme will
    prepare the final version and upload it next week.

Activity updates
================

Event Generators
----------------
-   Andrea: we had a debriefing meeting this week
    ([*https://indico.cern.ch/event/778521/*](https://indico.cern.ch/event/778521/))
    to prepare the follow up of the generators workshop.
    -   Need to carry on activities as a Working Group. A subset of
        people agreed to coordinate these efforts (Andrea Valassi,
        Josh McFayden, Stefan Hoeche, Steve Mrenna, Taylor Childers).
    -   Agreed to write up the main outcomes of the workshop in a brief
        report/proceedings. Aim for an outline before Christmas and a
        full text by the end of January. Peer review from workshop
        participants and put it on arXiv. Some details still to be
        sorted out (authors, possible submission to conferences like
        ACAT or CHEP). Note that CWP generator chapter is not
        published as a standalone paper and probably will not be.
    -   Some of the main priorities for future activities:
        -   Understanding of ATLAS/CMS differences. Benchmarking of
            sherpa/madgraph. Document generator configurations to
            allow rerunning of standard setups.
        -   Iterate between ATLAS/CMS and generator groups on ways to
            support technical work, and also on reward system and
            citations.
        -   As a background activity for the longer term, define an
            evolving model of what generation we will need for Run4
            (LO, NLO, NNLO, weighted and unweighted events… what will
            be the CPU budget?).
        -   Get madgraph team to minimally validate the GPU code, then
            try it out.
        -   Could eventually organize a 5-day workshop with more
            hands-on work.
-   Expect some (but not huge) overlap with simulation WG, definitely
    need to keep in touch.
-   Campaign of benchmarks on the CPU codes?
    -   Yes - it’s part of the first activity listed.
-   Should not forget about the GENSER project - they can help with
    benchmarking tests.
-   Sharing events?
    -   CMS have them in CVMFS already.
    -   Discussion on sharing was had at the workshop. Many issues to
        consider (CPU cost, cross-check of each other’s results,
        combination). AndreaR: not clear if sharing events would make
        combinations better or worse.
-   Caterina: was anyone from the Dark Machines project there? Would
    like to share samples, but lack of a standard format hampers this.
-   Do you plan to evolve to a WG like the others, with 3 convenors?
    Andrea: no clear plan or timescales yet, this activity is just
    starting and we are 5 people who volunteered or were volunteered
    to keep some momentum - anyway I agree, eventually we should
    become a more formal WG and go through the same procedure as the
    other WGs.

Software Forum
--------------
-   Had a meeting on 5 December on [*Spark R&D for LSST and in
    ROOT*](https://indico.cern.ch/event/754811/) (but without CMS Big
    Data project participation due to various conflicts). One possible
    outcome, after talking to Oli, may be a workshop on Spark for
    physics at Fermilab next Spring. Decision/date expected before the
    HSF workshop in JLab.

Software Tools
---------------
-   Serhan Mete has joined Martin and Giulio as a
    convenor/organiser/coordinator/facilitator of the group.
-   [*Meeting*](https://indico.cern.ch/event/776177/) on CERN IT’s
    Trident tool last week, 6 December.
    -   Follow-up with Servesh, because people are interested.
    -   Links between performance counters and lines of code is not so
        clear - point that could be improved.

CWP
===
### General Matters and Roadmap
-   CWP Roadmap has been accepted by Springer.
    -   Need to confirm that we want an open-access publication and who
        will pay it: from discussion with Springer, it seems that CERN
        could do it as part of its open-access policy and that we need
        to contact the CERN librarian (J. Vigen).
    -   We will upload the final revised version to arXiv.

### Publication status for Individual WG Papers
-   **Data Organisation, Management and Access**
    -   Done:
        [*https://arxiv.org/abs/1812.00761*](https://arxiv.org/abs/1812.00761)
-   **Event/Data Processing Frameworks**
    -   Now in final circulation, arXiv next week.
-   **Conditions Access**
    -   Broken promises to be repaired this week

AOB
===
-   Reminder: HSF Logo in vector format - action on Benedikt.
    -   PDFs uploaded here:
        [*https://github.com/HSF/documents/tree/master/logos*](https://github.com/HSF/documents/tree/master/logos)
        (thanks!)
-   Meeting next week? 20 December is quite close to Christmas.
    -   No, we cancel it and reconvene next year.
    -   Happy Holidays to Everyone!
