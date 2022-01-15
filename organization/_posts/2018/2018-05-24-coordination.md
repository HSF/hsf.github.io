---
title: "HSF Weekly Meeting #137, 24 May, 2018"
layout: meetings
---

# {{page.title}}

#### *Present/Contributors*: Graeme Stewart, Dario Menasce, Benedikt Hegner, Michel Jouvin, David Lange, Davide Costanzo, Torre Wenaus, Guilherme Amadio, Daniel Elvira, Andrea Sciaba, Eduardo Rodrigues, Paolo Calafiura, Pere Mato

News, general matters
=====================
-   [EIC Software Consortium
    Talk](https://www.jlab.org/indico/event/264/other-view?view=standard)
    -   Well received. Discussion focused on licenses and R&D in
        simulation.
    -   EIC happy to give us an HSF talk in return on their activities.
-   [IEEE eScience
    conference](https://www.escience2018.com/), Exascale
    Computing in High-Energy Physics track: abstract deadline extended
    to June 18.
-   Presentation by Benedikt at Belle II software week. Feedback about
    where more collaboration is possible and desired. For licensing
    just following what the community decides. Copyright holder unclear. 
    CERN was brought up as potential community-wide code owner.

PyHEP Workshop
==============
-   Tails of distributions are exactly that - agenda 95% done but not
    totally yet.
-   Pleasing that there are still 1-2 people registering per week.
    Almost 70 participants so far.

Activity updates
================

Licensing
---------
-   See [attached documents](https://indico.cern.ch/event/722019/).
-   We need to follow up with FastJet.

Training
--------
-   Discussion with Sudhir. He volunteered to host a web page on the
    Fermilab platform with links to existing training schools and
    material. In the beginning just a web page, but will grow into an
    effective portal for training. Will happen at the end of next
    week, when he will be done with teaching duties.

Packaging
---------
-   Will contribute to the [LIM
    workshop](https://indico.cern.ch/event/720948/) next
    week. Next meeting [13
    June](https://indico.cern.ch/event/730538/).
    -   aliBuild and Portage contributions to the test drive are
        currently PRs.
    -   Ben worked on a
        [guide](https://github.com/HSF/packaging/tree/master/istools)
        to working with different instruction sets.

Frameworks
----------
-   [BOF at CHEP](https://indico.cern.ch/event/727646/)
    -   Talks semi-confirmed from Kyle Knoepfel, Chris Jones, Alex
        Buchanan, Holger Schulz, and Alexander Souza. Speakers
        expected from ALICE and ATLAS.
    -   Indico to be filled in soon; will add a registration page to
        help planning.
    -   Focus on I/O and data models.

Visualization
-------------
-   WebEventDisplay project is being setup so that people can
    collaborate on a common WebGL based event display (this was
    initially developed by Ed Moyse and is used for the TrackML
    challenge).

Software Development
--------------------
-   Martin, Giulio and Graeme met and we will have a Software
    Development meeting on 14th June (taking this 15-16h slot). Aim is
    to make progress and identify people wanting to work on
    performance & optimisation topics. Also proposing a BOF follow up
    at CHEP.

HSF/WLCG Workshop Follow-up
===========================
-   Practical follow ups at the HSF level
    -   Inventory of community activities
        -   http://www.hepsoftware.org/
            is dormant - do we need a new "technology" (for example, a
            graph database may look as an attractive technology)? But
            re-use the information for sure. Link this to Sudhir's
            work with training inventory perhaps?
        - Does not preclude a quick reorganisation of the website with
          more highlighting of the more active areas.
    -   More variation in meeting themes (more topical):
        -   DD4hep meeting confirmed for 6 June.
        -   Do we restart this in the Software Tech Forum?
            -   Torre: that never seemed to work too well - rethink this
                activity.
            -   Links to HSF were weaker than they should be.
    -   Collaboration guide for projects
        -   Draft by Benedikt. Iterating with Graeme.
-   **Important discussion** on the question of are we missing the 
        big picture for "software upgrades"?
    -   How does the HSF become a focus point that helps tackle the
        grand challenge of HL-LHC?
    -   There are some project proposals that will be coming up in the
        next months - checkpoint at CHEP and after.
    -   More urgent for the experiments in HL-LHC planning. A
        "re-engineering" task force? Topical groups, e.g., HPC
        efforts. GPU working group?
    -   Bottom up efforts to be encouraged, but support from
        experiment management is vital as developers are everywhere
        stretched.
    -   We should restart the Software Tech Forum as a start, 
        *continue to discuss this next week*.

CWP
===
-   ### General Matters and Roadmap
    -   Conversion to CSBS format more or less done now, see
        [WIP](https://github.com/HSF/documents/pull/83).
        Need to fix a few remaining formatting issues (because of the
        move to a new LaTeX style) and have a final agreement with
        Springer about using "HEP Software Foundation" as the author
        with the actual list in an appendix like in arXiv.
    -   Michel will continte the mechanics of the submission with this
        updated LaTeX version.
        - "Author" will be HSF generically, but with the usual
          list of signatories as an appendix.
-   ### Publication status for Individual WG Papers
    -   **Data Organisation, Management and Access**
        -   Michel waiting an answer from Bo about the exact status.
            Last update 2 weeks ago was that Bo was doing the arXiv
            submission.
    -   **Data and Software Preservation**
        -   Michel and Graeme to post from Mike's documents.
    -   **Visualization**
        -   Ric and Tom will work on it next week.
    -   **Careers, Staffing and Training**
        -   Dario, Sudhir and Arthur and going to draw this to a close
            now. They would like to send the paper to arXiv by Jun 4th
            (to allow some additional time for voluntaries to read and
            correct the manuscript)
        -   [https://www.sharelatex.com/project/595500273c5204ff35dfdcf9](https://www.sharelatex.com/project/595500273c5204ff35dfdcf9)
    -   **Facilities and Distributed Computing**
        -   Ian wants to publish \~as is as a record. He's doing a last
            review now.
    -   **Conditions Access**
        -   Paul still on leave - Graeme meeting with him next week.

AOB
===
-   Ideas for a Generators workshop need moved forward - this would have
    to be in the late autumn.
