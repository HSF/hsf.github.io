---
title: "HSF Weekly Meeting #145, 20 September, 2018"
layout: meetings
---

# {{page.title}}

#### *Present/Contributors*: Graeme Stewart, Eduardo Rodrigues, Dario Menasce, Pere Mato, Tommaso Boccali, Witek Pokorski, Torre Wenaus, Horst Severini, Ian Collier, Michel Jouvin, Pete Elmer, Daniel Elvira, Liz Sexton-Kennedy, Mark Neubauer, Martin Ritter

Activity updates
================

Licensing
---------
-   Michel sent an email to FastJet developers about re-discussing their
    licensing choice.

Training
--------
-   Graeme wrote his Python intro course slides (technical solution of
    Jupyter + RISE was very successful). Available
    [*here*](https://github.com/graeme-a-stewart/python-introduction)
    and should be forked to HSF-training, once a few other people got
    a chance to check them.
-   [INSIGHTS](https://www.insights-itn.eu/) - this is EU funded.
    We should reach out to them as training contacts.
-   Henry Schreiner is teaching a Data Science course, the URLs are
    available.
-   Mark Neubauer also has a course on this topic.
-   Dario - we need a way to gather this material to curate it (there is
    a meeting with Sudhir Malik, Albert Puig, Dario Berzano soon).
    -   Liz, Pete, Graeme: HSF website would be ideal as everyone can contribute
        there with a known workflow.
    -   Dario - not sure that the GitHub PR is the best way: past and
        future events should be browsable and this is possible only if
        there’s a database under the hood. Managing this kind of
        information can be best accomplished with a Content Management
        System (CMS :) ). This requires some work, somebody willing
        and able to set it up (something like a Joomla web site). Food
        for thought for the Training WG.
-   IRIS-HEP contribution? Want to build the community around this is
    the key point. Having a curator would be really helpful, not to
    take on all the work, of course they can delegate to others as
    well.
-   Conclusion - there is a lot of useful things we can achieve now in
    the training domain.

Packaging
---------
-   [*Group met*](https://indico.cern.ch/event/754985/), September 19
    -   Very useful meeting, focused on 2 interesting Spack talks - one
        covered important recent developments, one on successful
        developments, using containers.
    -   Todd Gamblin (main Spack developer) joined us
        -   He has been very happy with our collaboration and wants to
            prioritise HEP use cases.
        -   Issue of Spack relicensing (from LGPL to MIT/Apache 2) was
            raised - we will chase our HEP contributors.
-   [*Next meeting*](https://indico.cern.ch/event/758817/) October 3

Frameworks
----------
-   Graeme contacted Chris Jones (FNAL) re. the OpenMP investigations we
    discussed last week.

Software Forum
---------------
-   Next meeting is “HEP.TrkX: Deep Learning Tracking” on [*26
    September*](https://indico.cern.ch/event/745416/).

PyHEP
-----
-   PyHEP 2018 workshop presentations: all available on Zenodo, with a
    DOI attributed, see
    [*https://zenodo.org/communities/pyhep2018*](https://zenodo.org/communities/pyhep2018).
-   Can this be automatic from Indico? Could be a feature request,
    especially if there are more presentations to handle.
-   Eduardo gave a talk to LHCb about PyHEP that was well received.
    -   Could repeat that for other communities.
-   Has this been brought up in CMS/ATLAS? Not to our knowledge. Torre -
    could be useful at an ATLAS S&C week (but over to Davide!). Not
    about convincing people to use Python, but propagates information
    about the community and resources available. Analysis community
    are probably under-informed on all that’s available.
-   For the work that has been done, we need to link back better to
    the main HSF website.

Technical Notes
---------------
-   Working on getting DOIs for these.

New Working Groups
==================
-   [*Draft mandate
    document*](https://docs.google.com/document/d/1lvgBqCk1kWgY90iAkjl84eLbO3b1qllEDRvG8FVfemI/edit?usp=sharing)
    being worked on.
-   There will be many common items for each group in terms of planning
    and organisation.
-   Concrete goals can’t be set in a mandate (right?), but each group
    should go through a planning/doing/reporting cycle.
-   Pete - most important thing is to decide what the working groups
    should do. Organising, not driving. We ask for deliverables?
    -   e.g., inventory of active projects, overlaps and gaps.
    -   need to make sure that this is prominent.
-   Daniel - should be more explicit about common solutions and
    identifying areas that need more effort.
-   Pere - can *facilitate* the communication.
-   Eduardo, e.g., could encourage LHCb people to also try the Belle II
    analysis facilities.
-   Advocating new things to try seems a positive thing, not the
    same a *deciding* for people.
-   Liz - in the packaging we had to deliver a document that summarises
    the state of the art in an area, that was helpful to guide an
    informed decision.
-   Don’t want this to be a re-iteration/re-invention of the CWP process
    -   Graeme defended the short summary of areas of interest, as not
        everyone will go back and read a whole CWP chapter.
-   We do want to have a process that leads to concrete outcomes; that
    will require some discussion with potential convenors.
-   Action - work on document and try to converge on the most useful
    description; re-ordering things is fine and look for the most
    important points to stress.

Generators Software Computing Workshop
======================================
-   This was announced at the beginning of the week (hsf-forum).
    -   Yet to go to generator community lists.
-   [*Indico ready*](https://indico.cern.ch/event/751693/) and
    registration open.
-   Next coordinators’ meeting on Monday, firming up the agenda.

CWP
===
-   ### General Matters and Roadmap
    -   [*CSBS review
        comments*](https://docs.google.com/document/d/16T2RRu1LmAyXTgtKjyWgOwZR8zsVOw2Y1SCntot3_NU/edit?usp=sharing)
    -   No progress this week.
-   ### Publication status for Individual WG Papers
    -   **Data and Software Preservation**
        -   Content added to HSF documents repo; good to go into arXiv.

AOB
===
-   HSF Logo in vector format - reminder of action on Benedikt.
-   Next HSF/WLCG workshop:
    -   Amber confirmed JLab availability for 18-22 March 2019.
    -   Last minute clash arose with OSG All Hands meeting (which was
        planned for University of Oklahoma).
        -   Graeme suggested actually making a 3-way workshop.
        -   This went down pretty well with all parties; planning will
            be quite tricky but there are also a lot of potential
            advantages to doing this.
        -   Discussed with Amber and it seems that JLab does have the
            capacity for this (main auditorium seats 286, there are a
            number of smaller rooms for parallel sessions).
        -   Michel will also join the discussions for HSF.
    -   Correction from last week - original BNL/Stony Brook offer was
        for \$300 per person for 239 people, which was scaled up to
        \$350 for 200 based on a misunderstanding of how the costs
        were calculated (fixed vs. per person).
-   The lesson learned:
    -   Please put *tentative dates* into the HSF calendar as soon as is
        reasonable, even if they change later on! OSG people are
        added as calendar editors.
-   Comment from Graeme: should the calendar be in “Communication”
    instead of “Activities”?
    -   Agreed.
-   Next week’s meeting: Graeme will be in the ATLAS I/O Review, can
    someone else chair? Will decide on coordination list, but we
    should try to have a meeting.
