---
title: "HSF Weekly Meeting #146, 4 October, 2018"
layout: meetings
---

# {{page.title}}

*Present/Contributors*: Graeme Stewart, Michel Jouvin, Liz
Sexton-Kennedy, Eduardo Rodrigues, Catarina Doglioni, Pere Mato, Jim
Amundson, Giulio Eulisse, Daniel Elvira, Helge Meinhard, Concezio Bozzi
(Lots of apologies this week from Michel, Andrea, Tommaso, David, Witek -
it’s a CMS Week and an ATLAS S&C Week!)

News, general matters
=====================
-   European Committee for Future Accelerators
    ([ECFA](https://ecfa.web.cern.ch/)) have launched a survey on
    “Recognition of individuals in large collaborations”. Aimed at
    younger researchers; very relevant that people working on software
    share their experience and participate in the survey.
-   IRIS-HEP [*announcement
    list*](https://groups.google.com/a/iris-hep.org/forum/#!forum/announcements)
    was publicised, people are encouraged to sign-up.
-   The hepix-techwatch-wg was launched and had its [*first
    meeting*](https://indico.cern.ch/event/759721/) last week. The aim
    is to organise and formalise technology tracking in a wider group.
    Sub-groups to be setup.
    -   Michel, Graeme and Torre are cross-over members with HSF hats.
    -   Helge: lots of people joined the list, but many are known to be
        very busy already. So people who actually have sufficient time to do
        real work should join.
    -   Software area does not to be covered as this is an existing HSF
        activity; likewise costs are already covered by the Costs and
        Performance WG.

HSF/WLCG workshop
=================
-   Reminder, proposal is a workshop at JLab, 18-22 March 2019.
-   Met Friday 28 September with Amber, OSG and WLCG reps.
-   Logistics look good for JLab - main auditorium can take 280, 4 other
    rooms available for parallel sessions (80, 60, 35, 25 people).
    -   Amber is investigating catering and event logistics.
-   Now confirmed as the location for WLCG and HSF.
    -   Still awaiting final confirmation from OSG, although feeling is
        positive.
-   Then we need to start planning an agenda outline soon.

New Working Groups
==================
-   [*Draft mandate
    document*](https://docs.google.com/document/d/1lvgBqCk1kWgY90iAkjl84eLbO3b1qllEDRvG8FVfemI/edit?usp=sharing)
    -   Quite a bit of activity and clarifications in the last couple of
        days (thanks!).
-   Due to absences this week we were asked to delay approval until next
    week.
-   Should we call for further nominations now or wait until next week?
    -   Wait till next week.

Generators Software Computing Workshop
======================================
-   Reminder: [*Indico agenda*](https://indico.cern.ch/event/751693/),
    with registration.
-   Timetable is being firmed up and speakers from experiments and
    generator teams invited. (Will go into Indico when a critical mass
    has been reached.)
-   Looks like a small hackathon on Wednesday is viable.
-   Next organisers’ meeting, [*Thursday 11 October
    16h*](https://indico.cern.ch/event/763170/).

Activity updates
================

Licensing
---------
-   Matteo Cacciari replied for the FastJet team about another meeting.
    Not sold on non-GPL license and would like some more concrete
    information/requests from CERN and experiments.
    -   Discussing with ATLAS and CMS Computing Coordination how to move
        forward.
    -   Why do they want GPL?
        -   In our opinion some confusion with acknowledgements.
        -   Want code to be contributed back (but LGPL would do that too).
    -   CERN’s position has evolved now to favour MIT (old recommendation was
        more strongly GPL).
        -   It’s the combinations of licenses that are problematic, GPL is
            difficult in that regard for non-GPL components,
    -   Giulio - but GPL is a well established license and ecosystem,
        it’s still a viable solution.
    -   Industrial collaboration for new architectures is a big
        motivational point (Nvidia in particular are very GPL
        hostile).

Training
--------
-   Sudhir suggested an item on this next week.

Packaging
---------
-   [*Meeting yesterday*](https://indico.cern.ch/event/758817/) covered
    developments at FNAL to provide a prototype development
    environment for experiments (SpackDev).
    -   Interesting discussion - learning how to add extra things to
        Spack. In general our interactions with the LLNL developers
        are very positive.
    -   Minutes are
        [*here*](https://github.com/HSF/hsf.github.io/pull/385).
-   Next meeting in [*2 weeks
    time*](https://indico.cern.ch/event/762971/), 17 October.

Software Development
--------------------
-   Giulio - would like to have a meeting on profiling tools. To be
    followed up, perhaps in 2 weeks time?

Software Forum
---------------
-   HEP.TrkX [*meeting last
    week*](https://indico.cern.ch/event/745416/).
    -   From David: “the discussion went well - in total, they lasted
        about one hour, and it seemed to me that this project made
        some interesting progress since CHEP, so that helps keep the
        discussion going. We only had a handful of people in the CERN
        room, but quite a large number outside (I know there were
        clashes in CMS with an ML meeting and in ATLAS with your
        review (presumably a smaller group than any sort of ML
        meeting...), but that’s to be expected. I realize that we
        should consider recording these discussions if the speaker is
        willing. Its apparently not hard to put recordings on youtube
        (as one example) and then would be linkable to indico and the
        HSF.”
    -   Liz - concurred that hearing the project progress was
        interesting and showing the flexibility to change tack, as needed.
-   Discussion of potential gains on modern hardware [*next
    week*](https://indico.cern.ch/event/745286/).

PyHEP
-----
-   Interesting discussions being held on our Gitter channel
    [*https://gitter.im/HSF/PyHEP*](https://gitter.im/HSF/PyHEP).
-   A new room
    [*https://gitter.im/HSF/PyHEP-histogramming*](https://gitter.im/HSF/PyHEP-histogramming)
    has been created for technical discussions around histogramming
    tools following the DIANA-HEP meeting of this Monday, see
    [*https://indico.cern.ch/event/759556/*](https://indico.cern.ch/event/759556/).
    Feel free to join as the future of those tools will be discussed
    there.

CWP
===
-   ### General Matters and Roadmap
    -   [*CSBS review
        comments*](https://docs.google.com/document/d/16T2RRu1LmAyXTgtKjyWgOwZR8zsVOw2Y1SCntot3_NU/edit?usp=sharing)
    -   Michel was too occupied to make progress on these yet (seems
        everyone else was too).
-   ### Publication status for Individual WG Papers
    -   **Software Trigger and Event Reconstruction**
        -   PR to the documents repo was
            [*accepted*](https://github.com/HSF/documents/pull/102). **Done**
    -   **Data Organisation, Management and Access**
        -   Bo was having a biber/bbl issue uploading to arXiv - Graeme
            suggested using either TeXLive 2016 (as used by arXiv) or
            2017 (known to work).
    -   **Data and Software Preservation**
        -   **Done**
            [*https://arxiv.org/abs/1810.01191*](https://arxiv.org/abs/1810.01191)
    -   **Visualization**
        -   Ric said a few last issues were addressed in the final
            review by the community. Should be able to now submit to
            arXiv.
    -   **Event/Data Processing Frameworks**
        -   Graeme discussed with Liz, Jim and Benedikt. Plan is to make
            progress in the next week, it may be that only an abstract
            is missing.
    -   **Conditions Access**
        -   Paul will review what’s there right now and Graeme will
            proof it.

AOB
===
-   HSF Logo in vector format - reminder of action on Benedikt.
-   Calendar was moved from “Activities” to “Communication” on the web
    site.
-   There was a small forum discussion thread on
    [*codemeta*](https://codemeta.github.io/) - this looks like a very
    nice way to integrate important information about software
    repositories into the repo itself. Used by CalTech (with Invenio)
    and Zenodo.
    -   Dan Katz has been a driver behind this and it looks like it
        would be well worth investigating and helping to promote.
    -   A future evolution of
        [*http://hepsoftware.org/*](http://hepsoftware.org/) could go
        this way?
