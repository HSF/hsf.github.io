---
title: "HSF Weekly Meeting #144, 13 September, 2018"
layout: meetings
---

# {{page.title}}

#### *Present/Contributors*: Graeme Stewart, Ian Bird, Michel Jouvin, Liz Sexton-Kennedy, Heather Gray, Daniel Elvira, Serhan Mete, Caterina Doglioni, David Lange, Eduardo Rodrigues, Andrea Valassi, Ed Moyse, Pere Mato, James Catmore, Sudhir Malik

News, general matters
=====================
-   LHCC Presentation:
    -   [https://indico.cern.ch/event/685793/](https://indico.cern.ch/event/685793/)
    -   Comments were directed to:
        -   How much ROOT progress in the I/O layer?
        -   When packaging WG would reach conclusions?
        -   Are other FAs in supporting software (in the wake of the
            IRIS-HEP news)?
            -   New WGs are important in defining concrete work plans.
            -   LHCC has been asked to offer general support for work
                plans, that helps this to happen.
        -   LHCC have not yet set a date for the review of HL-LHC (may
            not be before next summer).
-   COMCHA (Spanish organisation for tackling COMputing CHAllenges) Presentation:
    -   [https://indico.ific.uv.es/event/3438/](https://indico.ific.uv.es/event/3438/)
    -   Presentation was well received - organisers are keen to keep in
        touch with us and work together.
-   IRIS-HEP was funded!
-   ACAT call for abstracts and registration is out
    ([https://indico.cern.ch/event/708041/](https://indico.cern.ch/event/708041/)).
-   Connecting the Dots call for abstracts and registration is out
    ([https://indico.cern.ch/e/ctdwit2019](https://indico.cern.ch/e/ctdwit2019)).

Activity updates
================

Training
--------
-   [Formats discussion](https://groups.google.com/forum/#!topic/hsf-tech-forum/k9V-0buFD0Q)
    (tech list) was very useful.
    -   RISE extension for Juypter notebooks seems ideal for live
        presentations.
-   Dedicate one of our next meetings to training activities?
    -   Yes, to be followed offline with Sudhir.

Packaging
---------
-   [Next meeting](https://indico.cern.ch/event/754985/),
    September 19.
    -   Report from Hadrien Grasland about his experience using Spack to
        build ACTS.

Frameworks
----------
-   Workshop at ANL arranged for discuss I/O for exascale. Recommended
    re-investigating OpenMP. The HPC community have invested a lot into OpenMP
    in recent years and report that it now has much
    better support for tasks (which was the main feature that led HEP
    to choose TBB in the past). Could be a topic for a future
    meeting/workshop (HSF Software Forum).

Visualization
-------------
-   Group released its [final CWP
    draft](https://github.com/HSF/Visualization/tree/master/documents/CWP).
    Please review if you are interested in this topic.

Software Forum
---------------
-   Booked in a meeting on [Spark use in
    LSST](https://indico.cern.ch/event/754811/) for 5
    December.
-   A few slots still available this year
    -   [https://indico.cern.ch/category/10392/](https://indico.cern.ch/category/10392/)
    -   The Framework OpenMP talk would be ideal here.
-   Next meeting is "HEP.TrkX: Deep Learning Tracking" on [26
    September](https://indico.cern.ch/event/745416/).
    -   Graeme may be tied up in the ATLAS IO Review - volunteers to
        chair the meeting? David L should be able to do this.

PyHEP
-----
-   PyHEP 2018 workshop presentations: most of them now on Zenodo, with
    a DOI attributed, see
    [https://zenodo.org/communities/pyhep2018](https://zenodo.org/communities/pyhep2018).
-   Should advertise Gitter and resources more widely (hsf-forum).
-   Still trying to find a neutrino community representative.

New Working Groups
==================
-   Community [nominations now
    received](https://docs.google.com/document/d/19-Etynm2gO07PGVGSDETmGNStWX3oq6TIpXftsbMoAc/edit?usp=sharing)
    (thanks!).
-   Need to write a mandate.
-   Vava wanted to make sure the Reconstruction group covers also
    software triggers and real-time processing.
    -   This was in the CWP (strongly!), so yes.
    -   What about the other group's names? Are they too abbreviated?
-   How to proceed when we have more than 3 people nominated?
    -   How do we make sure we get a good balance, reflecting the whole
        community?
        -   Elections have been skewed in the past.
        -   Collaborations should have significant input.
    -   Do we want to have terms for the conveners so there can be
        rotation?
        -   1 year renewable agreed.
-   We should call again for nominations once the mandates are
    available.

Generators Software ~~Re-engineering~~ Computing Workshop
=========================================================
-   [Indico ready](https://indico.cern.ch/event/751693/).
-   Tweaked the announcement a little.
    -   It was felt that aspects of how we use generators could also
        bring significant gains and should be discussed.
-   Dates of 26-27 November at CERN confirmed.
-   Should be ready now to circulate widely (please look if you can).

CWP
===
-   ### General Matters and Roadmap
    -   Feedback from CSBS review was pretty good. List of comments was
        circulated to the coordination group.
        -   [CSBS review
            comments](https://docs.google.com/document/d/16T2RRu1LmAyXTgtKjyWgOwZR8zsVOw2Y1SCntot3_NU/edit?usp=sharing)
            (commentable by everyone, writable by HSF-coordination).
        -   Try to finish this by the end of next week.
        -   Please take a look and comment as needed.
-   ### Publication status for Individual WG Papers
    -   **Software Trigger and Event Reconstruction**
        -   Still needs to go to HSF repo.
    -   **Data Organisation, Management and Access**
        -   Michel has been chasing Bo.
    -   **Data and Software Preservation**
        -   Mike H gave us some LaTeX sources ages ago, now finally
            being
            [added](https://github.com/HSF/documents/pull/101)
            into github.
    -   **Visualization**
        -   See above.
    -   **Facilities and Distributed Computing**
        -   Ian ways should be done in next month. Some editorial decisions
            to be made regarding contradictory comments.
    -   **Conditions Access**
        -   Paul has changed institute, but this
            is high on his priority list.

AOB
===
-   HSF Logo in vector format - reminder of action on Benedikt.
-   Next HSF/WLCG workshop:
    -   Workshop dates fixed for 18-22 March 2019.
    -   Offer from JLab.
    -   Offer from BNL to host at Stony Brook.
    -   JLab looks cheaper for registration (\$200 vs. \~\$350) and has
        cheaper accommodation options (staying in Stony Brook looks
        expensive).
        -   Pere, Michel supported JLab, easy accommodation.
    -   Nobody with objection to choose JLab at the meeting. Final check
        to be done with I. Collier.
-   We wrote an HSF [letter of intent to
    collaborate](https://docs.google.com/document/d/1PcRv47JGcwUWVM3LcZ64YyewpNcThx-Sw7bcUI0wuRM/edit?usp=sharing)
    with an IREU proposal from David Lange and Pete Elmer (funds US
    students to come to CERN, working with Openlab in Big Data and
    Machine Learning).
