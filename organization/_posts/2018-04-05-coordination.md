---
title: "HSF Weekly Meeting #132, 5 April, 2018"
layout: default
---

# {{page.title}}

#### *Present/Contributors*: Graeme Stewart, Giulio Eulisse, Marco Clemencic, Marco Petric, Benedikt Hegner, Pere Mato, Enric Tejedor, Michel Jouvin, David Crooks, Torre Wenaus, David Lange, Eduardo Rodrigues, Simone Campana, Helge Meinhard, Andrea Valassi, Daniel Elvira, Liz Sexton-Kennedy, Martin Ritter, Robert (K?), Sudhir Malik, John (H?)

News, general matters
=====================
-   Call for papers to [UK Research Software Engineers 2018](http://rse.ac.uk/conf2018/) was circulated to lists.
    -   A few people are interested in working on an HSF paper, Graeme
        will follow up.
-   2018 CERN School of Computing (CSC 2018) applications open,
    [https://indico.cern.ch/e/CSC-2018](https://indico.cern.ch/e/CSC-2018).
-   CERN OpenLab organising a 2 day workshop on Quantum Computing, w/b 5
    November.

HSF/WLCG Workshop Follow-up
===========================
-   Gather important items that we should be tracking after the workshop
    (see workshop [live
    notes](https://docs.google.com/document/d/1QSkvwRK_2HENuxYXcs9Op1dTUK824KddQ1Tfan-P0WU/edit?usp=sharing))
    -   ### General Points
        -   We need a newsletter!
            -   Graeme to follow up.
        -   Benedikt will give a WS summary in next week's EP-SFT meeting.
    -   ### Common Data Management and Data Lakes
        -   WLCG lead here.
        -   Are there software implications?
            -   Needs a global view and to see how the data will be used
                by applications - production and analysis are quite
                different. Software stacks and ROOT are important.
        -   Identified issues with content delivery, tape carousels,
            etc. Horizontal and vertical dimensions.
        -   Will start a mailing list for this R&D.
            -   Need to relate to other WGs in this area, e.g., WLCG
                Data Management Steering Group.
            -   Will have to organise regular meetings.
            -   Need to add a few more notes.
    -   ### Frameworks and Infrastructure
        -   BOF session pre-CHEP - activity before that?
        -   1 / month meeting to help here. Liz will help look for a
            convenor.
    -   ### Programming for Concurrency and Co-Processors
        -   Tracking community seems quite well organised (CTD, Kaggle
            challenges, etc.).
        -   Michel spoke to David Rousseau, coordination between ACTS
            and HEP.TrkX is taking place.
    -   ### Simulation
        -   Ongoing activity around the GeantV prototype.
        -   Geant4 have proposed R&D activities.
        -   Some concerns from Daniel about 2 weaker R&D area
            -   ML effort seems weak, can this be strengthened?
            -   Use of HPCs remains a concern for us: this is a wider
                problem for HEP workflows.
    -   ### Analysis Facilities and Use Cases
        -   Expanded summary + follow-up asked to be presented at next
            WLCG GDB meeting on April 11th. Eduardo to do it.
        -   We need to keep activities alive, "connected" and,
            hopefully, focused, with an effective communication across
            experiments in particular. Some suggestions will probably
            be written down in the GDB presentation.
            -   Example activity: ALICE tests of Apache Arrow + TDataFrame.
    -   ### Software Development
        -   Documentation of how to use profiles / static analysers
        -   Web based GUI to browse and compare different profilers.
        -   Common plugin based mechanism for clang-tidy so that adding
            checks does not require modifying the upstream sources.
    -   ### Visualization
        -   Ric to follow-up.
    -   ### Workload Management
        -   R&D prospects primarily in WM aspects of WLCG-led DOMA/data
            lakes R&D and how to use WM to manage/optimize
            DOMA-related operations.
        -   Link to frameworks and what the brokered units of work are,
            across the scale spectrum from datasets to events.
        -   DOMA = data organization, management and access
    -   ### Security
        -   WLCG led, some ongoing discussions identified.
        -   Trust groups with grid/campus teams.
    -   ### Performance and Cost Modeling
        -   WLCG led, group is pretty active already.
    -   ### Data Preservation for HEP
        -   Organised community.
        -   Links to analysis.
    -   ### Training and Careers
        -   See below...
    -   ### Others:
        -   Technology watch group should be launched. Relationship to
            other groups (Cost Model, Benchmarking) should be defined,
            but not merging them at the moment.
        -   Andrea - worried about the generators in general. Deserves
            some follow-up, Graeme involved (but unfortunately off
            next week at the time of the next MCnet meeting,
            [https://indico.cern.ch/event/689514/](https://indico.cern.ch/event/689514/)).
            Liz can engage with MCnet people next week. Idea
            starting to be discussed to organise a workshop dedicated
            to computing requirements for generators at HL-LHC.
            Configuration of generators has a big impact on resource
            consumption. Need to do some baseline benchmarking between
            the different experiments and get an understanding of
            costs in each generator and costs of each process.
        -   Links to OpenLab are important - they produced their own
            White Paper end of last year, for the next 3 years of
            activities.
-   ## Practical follow ups at the HSF level
    -   Inventory of community activities.
        -   Should go with general website reorganisation.
    -   More variation in themes in these meetings (more topical)
        -   Would really need a better room to show slides on Vidyo.
        -   Time ok? It's rather early for Pacific Time.
        -   Need also to have organising meetings, but alternating would work.
    -   Collaboration guide for projects
        -   New white paper suggested by Pete (but short!)

CWP
===
-   ### General Matters and Roadmap
    -   Second draft of one of the Symmetry Magazine articles from Sarah
        Charley.
    -   CWP article was published in the CERN Courier April edition
        (cover this in the newsletter too).
    -   Graeme will give a CWP talk at the [GridPP40
        meeting](https://indico.cern.ch/event/684659/)
        next week.
    -   Publication in CSBS - need to follow up with the editors.
        -   Graeme and Michel to follow up.
-   ### Publication strategy for Individual WG Papers
    -   ### Machine Learning
        -   Sergei says it's basically done, "waiting for an updated
            version of a plot and we are good to go to the arxiv".
    -   ### Software Trigger and Event Reconstruction
        -   PR for the documents repo please!
    -   ### Data Organisation, Management and Access
        -   Last call for comments about the LaTeX paper in Overleaf:
            expires end of next week. Will be ready for arXiv
            afterwards.
    -   ### Data Analysis and Interpretation
        -   Still problems uploading to arXiv?
    -   ### Conditions Access
        -   Paul has not followed up yet.
    -   ### Generators
        -   Discussed at Naples. Feeling was that the CWP chapter was
            good enough and that there should be more of a work plan
            oriented follow up with the theory community, an autumn
            workshop? N.B. There is an [MCnet
            workshop](https://indico.cern.ch/event/689514/)
            next week at CERN.

PyHEP Workshop
==============
-   "Advert paragraph" for upcoming 3rd CHEP bulletin in preparation.
-   Agenda itself will be given a push in the next week or so.
-   We have 23 participants registered so far - a healthy number.

Activity updates
================

Licensing
---------
-   Organise meeting with Belle II who are interested in clarifying
    their situation.
-   Follow-up time with FastJet.
-   Indico will move from GPLv3 to MIT license in next version (2.1) to
    make easier adoption outside the academic world. See
    [https://github.com/indico/indico/issues/3255](https://github.com/indico/indico/issues/3255).
    All commit authors contacted.
-   ATLAS: looking at making the code public but stuck in trying to
    "sanitize" the history... Advice/recommendations from HSF and the
    community may help...

Training
--------
-   Create a \"federation\" of existing schools, a \"logical\" place
    (instead of a \"physical\" one) where to plan together school
    calendars, training materials, eventually exchange tutors and
    slides and so on.
    -   Another Google Calendar?
-   Make sure is that all of us representing our different experiments
    have a mandate from our own very experiment to represent it. This
    is important to ensure continuity in representation of an
    experiment/community and make it an individual independent.
-   Let us try to meet virtually post Napoli meeting to discuss the
    future path of Training and Career
-   A good place would be to have a website displaying schedule of
    Training activities of our experiments of the kind that all of us
    showed in our talks so that we are all aware of what is happening.
-   Also we should have an egroup kind of email to communicate with this
    community.
    -   There is a training group email on Google -
        [https://groups.google.com/forum/\#!forum/hsf-training-wg](https://groups.google.com/forum/#!forum/hsf-training-wg)
        ([hsf-training-wg\@googlegroups.com](mailto:hsf-training-wg@googlegroups.com))
-   At the same time we can think of creating common training material
    up to the point where it becomes experiment specific. There was a
    lot of common training topics listed in all the talks and those
    would be a good place to start.
-   A future step should be, if possible to invite, training experts
    from one experiment to the other to get a first hand feeling
    commonality. Such an opportunity can be communicated via the above
    email group.

Packaging
---------
-   Discussion slot last week in Naples - good to communicate with a
    wider group of developers.
    -   Containers are important and simplify things.
    -   Test driving solutions is the next practical step.
-   Meeting
    [yesterday](https://indico.cern.ch/event/716297/)
    ([minutes](http://127.0.0.1:4000/organization/2018/04/04/packaging.html)
    available)
    -   Reviewed Naples.
    -   Feedback from first (naive) test drive of Nix
-   Next meeting [18
    April](https://indico.cern.ch/event/719557/).

GSoC
----
-   Student applications now closed. Have asked mentors to provide
    feedback on the proposals - ranking for the students needs to be
    communicated to the admins. Today is the hard deadline!
-   Tomorrow admins will meet and decide on the min/max slots to give to
    Google. Min = number of projects with very good students; Max =
    add projects with good, but not outstanding, students. No
    decisions on projects yet.

