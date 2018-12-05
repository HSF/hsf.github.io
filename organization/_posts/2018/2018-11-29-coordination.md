---
title: "HSF Weekly Meeting #152, 29 November, 2018"
layout: meetings
---

# {{page.title}}

*Present/Contributors*: Graeme Stewart, Pere Mato, Serhan Mate, Witek
Pokorski, Andrea Valassi, David Lange, Jim Amundson, Torre Wenaus, Ian
Collier, Danilo Piparo, Daniel Elvira, Dario Menasce, Tommaso Boccali,
Gloria Corti, Paul Laycock, Frank, Caterina Doglioni, Agnieszka Dziurda,
Ed Moyse

News, general matters
=====================
-   IRIS-HEP would like to have HSF representation on their steering
    committee.
    -   Pete Elmer (PI) has proposed that Graeme takes this on.
    -   Fine with Graeme and got support from others.
    -   *Agreed.*
-   Gerri Ganis gave the [*software report to the LHCC
    referees*](https://indico.cern.ch/event/685794/) this week.
    -   Questions on licenses and CWP review comments.
-   Graeme will give a short report on the new working groups and the
    generators workshop tomorrow at the [*WLCG Overview
    Board*](https://indico.cern.ch/event/734889/).

HSF/WLCG/OSG Workshop
=====================
-   Meeting took place on Monday 26th to discuss the workshop
    timetabling.
-   Very constructive and we were able to arrive at good range of
    substantially shared topics, while also earmarking necessary
    separate sessions for WLCG/HSF/OSG matters respectively.
    -   Draft block timetable being populated here:
        -   [*https://indico.cern.ch/event/759388/timetable/\#all*](https://indico.cern.ch/event/759388/timetable/#all)
    -   Broad division is 2 days for plenaries with WLCG/OSG, 2 days for
        HSF parallel sessions.
-   Meeting on Thursday 29th to discuss local organisation matters
    (immediately after this one).
    -   Aim today is to fix logistical matters so we can open up
        registration well before the holidays.

New Working Groups
==================
-   Convenors have been appointed - congratulations to them and thanks
    to all who took part.
    -   Detector Simulation: Heather Gray, Witek Pokorski, Gloria Corti
    -   Reconstruction and Software Trigger: David Lange, Caterina
        Doglioni, Agnieszka Dziurda
    -   Data Analysis: Andrea Rizzi, Danilo Piparo, Paul Laycock
-   Starting the work of the groups
    -   Update website ([*please see
        instructions*](https://hepsoftwarefoundation.org/howto-website.html))
        -   Groups have a stub webpage
            ([*Analysis*](https://hepsoftwarefoundation.org/workinggroups/dataanalysis.html),
            [*Reco*](https://hepsoftwarefoundation.org/workinggroups/recotrigger.html),
            [*Sim*](https://hepsoftwarefoundation.org/workinggroups/detsim.html))
    -   Planning for an activity start next year
        -   HSF “owns” a slot every 2 weeks in 32-1-A24, 17h ([*odd
            weeks*](https://www.epochconverter.com/weeks/2019)):
            -   16, 30 January; 13, 27 February
        -   Sometimes we give over the coordination slot to a topical
            meeting, but this room (32-S-C22) is not very good (too
            small, no vidyo).
            -   Pere - equip this room better? Yes please!
        -   At least one workshop pre-meeting?
    -   Start to organise a parallel session at the workshop:
        -   The main theme could be the survey of the existing
            activities and planned ones in the community.
        -   Short plenary from each group?
    -   Contact experiments.
    -   Mailing lists:
        -   Probably should have dedicated ones
            -   Could seed these from the CWP WG lists?
        -   Reminder that we have the
            [*hsf-forum@googlegroups.com*](mailto:hsf-forum@googlegroups.com)
            (general, everyone) and the
            [*hsf-tech-forum@googlegroups.com*](mailto:hsf-tech-forum@googlegroups.com)
            (technical topics).
    -   Convenors should meet together soon.
    -   Graeme will circulate other names and inputs that we got during
        the process.
    -   Short report on plans from each working group in 2 weeks time
        (December 13).

Generators Software Computing Workshop
======================================
-   Andrea: Physics Event Generator Computing Workshop took place at
    CERN this week
    ([*https://indico.cern.ch/event/751693/timetable/*](https://indico.cern.ch/event/751693/timetable/)).
    Successful workshop, useful discussion and nice atmosphere with a
    mix of theorists/experimentalists and a few engineers.
    -   Many thanks to all the organisers! And to speakers and
        participants!
    -   Talks and discussion Mon-Tue and hackathon on Wed.
    -   Good attendance Mon-Tue (56 people registered), around 30-40
        people in person plus 15-20 via vidyo. Smaller attendance
        (less than 10) at the hackathon, but was also useful.
    -   [*Live
        notes*](https://docs.google.com/document/d/1_EoyKI6-VhPbmTxaDqVtetlVq7zpRXMWTVIiB_un8Ys/edit#heading=h.5i66lr3sffp)
        have been taken (by tasked usual suspects, but not only). Some
        take home messages are at the end.
    -   We will have a post-mortem probably next week to discuss next
        steps. A few people (Andrea, Steve) have already agreed to
        push on work in this area. We might have a dedicated 5-day
        practical workshop in 2019?
    -   Graeme will also give a [*WLCG Overview
        Board*](https://indico.cern.ch/event/734889/) report tomorrow.
        We forwarded Federico’s invitation to ACAT to generators
        people. We might also give a summary there (Andy Buckley will
        be there).
    -   Some of the take home messages and further work planned:
        -   Need to continue investigating ATLAS vs CMS differences.
            Includes Madgraph vs Sherpa but not only. Some comparison
            numbers were presented by Josh in the ATLAS talk. (Note:
            LHCb generators mainly concerned with decays rather than
            production. ALICE were contacted but did not take part in
            the workshop).
        -   Need to better understand Run4 projected needs and possible
            model. Clear that LO can do unweighted events ok, NLO can
            do unweighted events now but only with negative weights
            (large penalty as many more events must be generated).
            NNLO for the moment is only for differential cross
            sections, no unweighted events, but 1-2 orders of
            magnitude slower for LO-&gt;NLO-&gt;NNLO is to be
            expected.
            -   Need some metric to evaluate impact of negative weights,
                in order to best compare generators.
        -   The need to coordinate work and reward system between
            experiments and theorists was pointed out. Example in the
            Herwig talk “improving code performance would be a lot of
            work for no recognition”. Also, how to integrate
            engineers/experimentalists work in theorists’ work?
            ATLAS/CMS started investigation on recognition for work in
            generators area.
        -   Experiment computing infrastructure may help theorists.
            Example: regression tests for timing and physics
            performance across code versions. Example: large scale
            resources for specific NNLO resources.
        -   Some reports on HPC and GPU work, but not that much work
            there.
            -   David: in the 1.5h HPC session GPUs were not even
                mentioned.
            -   In general the HPC work did not show a real need for
                HPC, this work could have been done also on HTCs.
            -   GPUs only presented by Madgraph and it was mentioned
                that at the time they thought the experiments were not
                interested (or not able to use GPUs). The work was
                done around 5 years ago by authors that maybe moved
                elsewhere, but the port should still be functional in
                principle.
        -   Some more technical points, e.g. push for common interfaces
            to apply generator level cuts, review of Les Houches
            format etc.
        -   Licensing was mentioned in David’s talk but we kept it
            intentionally as a side subject. It may be useful to bring
            this up again in the future though.

Activity updates
================

Licensing
---------
-   Matteo Cacciari was not able to come to CERN, so we are exploring
    dates early next year to follow up on this. Licensing was
    raised at the generators workshop and so we may broaden the
    discussion to the whole theory community.

Packaging
---------
-   [*Meeting*](https://indico.cern.ch/event/772263/) 21 November,
    focusing on Portage tool.
    [*Minutes*](https://hepsoftwarefoundation.org/organization/2018/11/21/packaging.html)
    available.
-   Next meeting planned for 5 December

Software Development
--------------------
-   [*Meeting on 6 December*](https://indico.cern.ch/event/776177/) on
    monitoring tools - Servesh will discuss his new Trident tool.
    **N.B. this will replace the usual coordination meeting next
    week.**

Software Forum
---------------
-   Discussion with the [*Electron Ion Collider Software
    Consortium*](https://indico.cern.ch/event/746526/), 21 November.
    -   Some interesting topics to follow up on (data formats, analysis
        workflow) - we could foresee further interactions at the JLab
        workshop.
-   Next [*meeting on Spark*](https://indico.cern.ch/event/754811/) has
    been expanded to also include a talk from ROOT on Spark - should
    prove to be fruitful, and we’ll try not to run on too long!

CWP
===
### General Matters and Roadmap
-   CWP Roadmap was resubmitted to CSBS.
    -   Waiting for news from Springer.
### Publication status for Individual WG Papers
-   **Data Organisation, Management and Access**
    -   Ready to resubmit to arXiv.
-   **Visualization**
    -   [*https://arxiv.org/abs/1811.10309*](https://arxiv.org/abs/1811.10309)
-   **Event/Data Processing Frameworks**
    -   To go to final circulation.
-   **Facilities and Distributed Computing**
    -   No news.
-   **Conditions Access**
    -   Paul did a significant revision of the document, hopes to
        circulate it this weekend.

AOB
===
-   Update: Should we submit a HSF related paper to the European
    Strategy Update?
    -   Pere’s proposal : write a couple of pages around importance of
        taking software & computing into consideration early in the
        process of designing new machines/detectors and refer to the
        CWP for details.
    -   Pere discussed with Fabiola at the EP faculty meeting and she
        did think this was a good idea.
        -   Graeme, Pere to work on a draft for next week.
