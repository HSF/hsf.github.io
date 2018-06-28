---
title: "HSF Weekly Meeting #140, 21 June, 2018"
layout: default
---

# {{page.title}}
### It's the summer solstice meeting!

#### *Present/Contributors*: Graeme Stewart, Dario Menasce, Andrea Valassi, Benedikt Hegner, Tommaso Boccali, Eduardo Rodrigues, Jim Pivarski, Michel Jouvin, Pete Elmer, Daniel Elvira, Riccardo Maria Bianchi, Pere Mato

News, general matters
=====================
-   WLCG management board meeting decided to remove the moribund
    Applications Area (AA). HSF will take on the role of reporting
    software at the WLCG-MB and the LHCC.
    -   Graeme will by default take on that role for now.
-   Old AA meetings stay, but now focused on SFT hosted software
    projects.

Activity updates
================

Licensing
---------
-   Need to follow-up with Belle II (task force meeting this week during
    their collaboration General Meeting) and Fastjet.

Training
--------
-   Currently busy putting out to arXiv the Training&Careers paper
	(now in [GitHub](https://github.com/HSF/documents/tree/master/CWP/papers/HSF-CWP-2017-02_training/latex)).
    Almost there, will resume WG activity after publication (very soon,
    thanks to Graeme)

Packaging
---------
-   Had a meeting last week
    ([minutes](https://hepsoftwarefoundation.org/organization/2018/06/13/packaging.html)).
    Discussed more R&D proposals based on a deeper investigation of
    various approaches:
    -   Build everything (Chris Burr and Ben Couturier, Nix)
    -   Prefix based environments (Guilherme Amadio and Graeme, Portage)
    -   Developer environment setup (Chris Green, SpackDev)
-   Will have [next
    meeting](https://indico.cern.ch/event/737348/) 4 July
    (sorry USA), to discuss CHEP talk
-   SFT summer student has started, looking at using Spack to build the
    LCG stack.

Frameworks
----------
-   [Agenda](https://indico.cern.ch/event/727646/) for the
    pre-CHEP workshop is in place. Please sign up.
    -   We are investigating vidyo possibilities with CHEP organisers.

Visualization
-------------
-   The code of Ed Moyse's WebGL based browser code in now in [GitHub](https://github.com/HSF/phoenix).
    It has been used as the base for a community-driven web-based
    event display developed for the TrackML challenge. The event display
    will be further developed by the Visualization WG members.
-   CWP paper is moving on: Ric merged post-Naples contributors'
    additions; he also fixed, updated, and expanded the bibliography.
    Tom and Ric are editing the text for submission. Latest version on
    [GitHub](https://github.com/HSF/Visualization/tree/master/documents/CWP).

Software Development
--------------------
-   There was a Software Development Tools meeting last week
    ([minutes](https://hepsoftwarefoundation.org/organization/2018/06/14/software-tools.html)).
    -   Good turnout, \~25 people.
    -   Extensive discussion on performance measurements, tools to do
        this and comparisons.
    -   There is interest in working on a common warehousing and
        visualisation project.
-   Next topics: static analysers, metric gathering tools.
    -   Date not yet decided.

Software Forum
--------------
-   Next [meeting](https://indico.cern.ch/event/736105/)
    after CHEP will look at vectorisation and data layout libraries.
-   Please suggest more topics!

Technical Notes
---------------
-   Technical note on [HSF Platform Naming
    Conventions](https://github.com/HSF/documents/tree/3feb950306b75c93c6eb090fc7d38e86a004aae6/HSF-TN/draft-2015-NAM)
    is finished its consultation stage. To be finalised.
-   Technical note on [HSF Project Best
    Practices](https://github.com/HSF/documents/tree/3feb950306b75c93c6eb090fc7d38e86a004aae6/HSF-TN/draft-2016-PROJ)
    is now circulated more widely, please give feedback.

HSF/WLCG Workshop Follow-up
===========================
-   New activity areas for critical areas:
    -   We will set up working groups in analysis, reconstruction and
        simulation areas soon, follow up on CWP roadmap. Means to
        provide input to LHCC review.
    -   Please think about names of good people to be involved.

PyHEP Workshop
==============
-   Registration closed since June 15th. 71 registrants.
-   Sponsorships: Nikhef grant received in the account. The transfer
    from the Python Software Foundation has been confirmed. Together
    with the registration fees all expenses are covered.
-   Pre-workshop questionnaire had been sent \~10 days ago. Very good
    response (43 participants replied so far).
-   Other bits of admin being finalised. E.g. we now have our workshop
    secretaries assigned.
-   In short, we are largely ready!

Generators Software Re-engineering Workshop
===========================================
-   Graeme and Andrea with a few people from MCnet. Generally positive response to
    call. Now working on a
    [document](https://docs.google.com/document/d/1q0yErmSjYJOepESRs3bqjrF78oo0Y0QfjR3K93naJKU/edit?usp=sharing)
    to outline the workshop's background, discussion areas and
    intended outcomes. (AndreaV: due to the '"too many Andrea's"
    effect, was not aware of Graeme's document so I also started
    drafted [another
    document](https://docs.google.com/document/d/11GkCox5mRRITi5L0Lg5w9l88xoSO7cJj1kZCJoERhOc/edit?ts=5b2b71ff) -
    never mind, should just merge them!)
    -   Hope to define work programmes that can attract support to the
        critical areas of re-engineering and have long term
        attachments with the generator authors.
    -   Want to have this before the LHCC review of HL-LHC plans.
        -   Possible conflict with Madgraph tutorial in November - early
            December.

CWP
===
-   ### General Matters and Roadmap
    -   Accepted final signature on the paper. Need to update the arXiv
        version (hopefully the last time).
    -   Michel is following up on re-submission from the "ed board" HSF
        address.
-   ### Publication status for Individual WG Papers
    -   **Machine Learning**
        -   New content added. Now being reviewed and finalised.
    -   **Data Organisation, Management and Access**
        -   No news from Bo\...
    -   **Data and Software Preservation**
        -   Stuck in Michel (J)'s todo list\...
    -   **Visualization**
        -   See above.
    -   **Event/Data Processing Frameworks**
        -   Not quite final (but close) version now in HSF documents
            repository.
    -   **Careers, Staffing and Training**
        -   See above.
    -   **Conditions Access**
        -   Still a commitment, but no progress.

AOB
===
-   IRIS-HEP proposal (a condensed version of the Strategic Plan that is
    in [arXiv](https://arxiv.org/abs/1712.06592)) has been submitted. They would like a letter of
    intention to collaborate that they can give to the NSF.
    -   Draft of that is
        [here](https://docs.google.com/document/d/1L_RIQQ1kwnVohRDyuGgvIL8swIPPsg8ANuPOIyQwRlU/edit?usp=sharing).
    -   We would like this meeting to agree to that.
    -   There will be a steering board that meets quarterly, HSF will be
        represented.
    -   "Mechanical" question - which live body or bodies actually sign?
        -   OK for Graeme to sign, approved by this meeting.
    -   No dissent on this letter - approved.
-   SFT group had some concerns about the way ROOT maintenance was
    expressed in the submission. SFT believes that challenges *are*
    being addressed successfully over time. There is agreement to collaborate
    in the future.
-   Website reorganisation underway:
    https://github.com/graeme-a-stewart/hsf.github.io/tree/website-reorganise.
    -   Please take a look and add suggestions or updates (Google Doc
        collecting ideas is
        [here](https://docs.google.com/document/d/1t8x8Ua9E__vp_9i3KwLGrgk8QDAIGL4-ZPsqvPOUCQY/edit?usp=sharing)).
