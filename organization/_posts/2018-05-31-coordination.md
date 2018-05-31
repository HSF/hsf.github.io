---
title: "HSF Weekly Meeting #138, 31 May, 2018"
layout: default
---

# {{page.title}}

#### *Present/Contributors*: Graeme Stewart, Benedikt Hegner, Dario Menasce, Eduardo Rodrigues, Michel Jouvin, Laurent Duflot, Torre Wenaus, Davide Costanzo, Tommaso Boccali, Daniel Elvira, Pere Mato, Ian Bird, Ed Moyse, Guilherme Amadio, Sudhir Malik, Markus Schulz, Guy Barrand

News, general matters
=====================
-   WLCG DOMA (Data Organisation Management and Access) has a [kick-off
    meeting](https://indico.cern.ch/event/729930/) 4-5
    June.
    -   There is a [CERN mailing
        list](https://e-groups.cern.ch/e-groups/EgroupsSubscription.do?egroupName=wlcg-doma)
        for this work.
-   LHCC Meeting
    -   Presented status of HSF. Mentioned active areas at and after
        Naples workshop
    -   Referees' impression is that we now have an active community
    -   Re-emphasized the need for recognition of technical tasks and
        careers
    -   Ian B presented idea of 2 foci of activity around WLCG and HSF
    -   Have agreed with LHCC that experiment TDRs should be delayed.
    -   Want to have a review of the strategy document - early next year
        of computing strategy for HL-LHC. Comprehensive, all of
        computing needed for Run 4. Should also cover software and how
        we make it sufficiently performant and flexible for HL. To
        include Geant, ROOT. We will need to address this at the HSF
        level - projects for software re-engineering should be done.
    -   From the LHCC and the WLCG OB is clear they want to see this structure in
        order to allow FAs to contribute.
-   [RSE 2018 Conference](http://rse.ac.uk/conf2018/)
    -   Neither the packaging talk or the general HSF talk were accepted
        for this conference. This was pretty surprising to us. Ben
        Morgan is going anyway and might try to enquire a bit more.

PyHEP Workshop
==============
-   We are preparing a short questionnaire to send to all participants
    *before* the start of the workshop. Almost ready. The
    questionnaire will help us steer the discussions and the session
    on training at the end of the workshop.
-   68 participants is great; 70 would be fantastic. In short, do not be
    shy and register!

Activity updates
================

Training
--------
-   The coming week we should begin (thanks to Sudhir) the creation of
    the WEB portal devoted to link all the existing training
    initiatives under a single place. This should be a cornerstone of
    the concept of "federation" of schools. Next step, after this,
    will be to organize a Skype-meeting with the stakeholders (schools
    directors) to see how we can begin the process of "federating"
    activities in a concrete and effective way.
    
Packaging
---------
-   HSF Group contributed to the [LIM
    workshop](https://indico.cern.ch/event/720948/)
    yesterday. Next meeting on [13
    June](https://indico.cern.ch/event/730538/).
    -   Good that the participation in the workshop was very wide. Still
        a lot of disagreement on some fundamental points.
    -   Not very clear what the next steps should be - progress made 
        on smaller issues, but not really an emerging
        strategy.
    
Frameworks
----------
-   Chase up the agenda.

Visualization
-------------
-   New github project setup for WebGL based event display, experiment independent
    -   [https://github.com/HSF/phoenix](https://github.com/HSF/phoenix)
    
Software Development
--------------------
-   Meeting planned for 13 June.
-   There will be a Geant4 developer position opened up in Pittsburgh -
    US ATLAS funded (more details as they are known).

HSF/WLCG Workshop Follow-up
===========================
-   Practical follow ups at the HSF level
    -   Inventory of community activities
        -   Ideas for restructuring the website are advancing
            -   Graeme set up a [Google
                Document](https://docs.google.com/document/d/1t8x8Ua9E__vp_9i3KwLGrgk8QDAIGL4-ZPsqvPOUCQY/edit?usp=sharing)
                to collect suggestions
                -   Need to translate these into a git branch that
                    people can preview.
            -   Discussed the future of
                [http://www.hepsoftware.org/](http://www.hepsoftware.org/) -
                at the moment we should keep using it, even if we
                foresee its frontend being migrated (when effort is
                identified).
    -   More variation in meeting themes (more topical)
        -   DD4hep meeting confirmed for 6 June.
        -   This needs to be advertised and announced.
        -   Other ideas:
            -   Vectorisation (VecCore) and data layout work
            -   ACTS/HEP-Trk.X (Other reco?)
            -   Simulation R&D
    -   Collaboration guide for projects
        -   Draft by Benedikt has been iterated with Graeme. Should be
            turned into a TN fairly soon.
-   Are we missing the big picture for "software upgrades"? How do we make the HSF more central?
    -   Listings of community activities.
    -   Benedict - do this from the bottom up - see what emerges
        from the software forum
    -   Packages need to adhere to some guidelines for projects -
        "price of admission" and minimal guarantee of good structure.
    -   Ian - FAs and national projects want something that is more
        structured, with the expected outcomes. So this needs to
        be somewhat more formal.
    -   Torre - don't want to break the bottom-up-ness. Have some
        way to point to activities. Meeting with DOE/HPC people
        soon, can write this up and see it as a way to generate
        real projects.
    -   Dario - bottom-up is great, but delivery needs funding.
    -   Torre - Funding via SFT; also Google; US contributions
        hopefully coming; Projects need to be structured;
    -   Daniel - FNAL also summoned to talk to exascale people, use
        of accelerators. Will turn into projects with milestones
        and deliverables. Partnerships with other organisations
        can also become more formal, with clearer plans.
    -   Tommaso - how does this interact with the LCG AA Architects
        Forum?
        -   AF transformed from original AA projects coordination
            (for LCG experiments) into more of a meeting of users
            of Geant and ROOT.
        -   Pere - want to keep that meeting, but recognising its
            more limited scope.
    -   HSF can offer reviews of projects as well - to see if they
        makes sense.

CWP
===
-   ### General Matters and Roadmap
    -   Contact with Springer - trying to break out of the infinite loop
        re. authors next week at the CSBS EB meeting.
-   ### Publication status for Individual WG Papers
    -   **Machine Learning**
        -   Got new input for the chapter, but now the door has closed.
    -   **Data Organisation, Management and Access**
        -   Ready to go - some small technical issues with the
            submission re. references.
    -   **Data and Software Preservation**
        -   Michel needs to tweak the style.
    -   **Event/Data Processing Frameworks**
        -   Waiting for FNAL feedback.
    -   **Careers, Staffing and Training**
        -   Dario - Made a last-call to everyone to read, comment and correct
            mistakes and missing points. Albert and Sudhir revised the
            document. I guess we are ready to submit. Will do on
            Wednesday (I'll be at a Workshop Monday and Tuesday)
            unless Sudhir can take care of it on Monday.
    -   **Facilities and Distributed Computing**
        -   Still need to continue to clean up the comments.

AOB
===
-   The [HSF website](https://hepsoftwarefoundation.org/)
    has been updated to [support
    https](https://github.com/HSF/hsf.github.io/issues/351).
    -   We can now enable the option to force http access to redirect to
        https.
-   [Technical note on platform naming
    conventions](https://github.com/HSF/documents/tree/master/HSF-TN/draft-2015-NAM)
    -   Some feedback from Graeme to Benedikt, reminder for others to
        comment on that soon...
    -   Needs to be broadcast a bit more widely.
-   Suggestions for best practices for new software projects is in
    draft, will be a proposed TB soon as well.
