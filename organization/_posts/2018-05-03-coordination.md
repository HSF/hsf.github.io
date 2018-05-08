---
title: "HSF Weekly Meeting #135, 4 May, 2018"
layout: default
---

# {{page.title}}

#### *Present/Contributors*: Graeme Stewart, Benedikt Hegner, Pere Mato, Dario Menasce, Scott Snyder, Michel Jouvan, Guilherme Amadio, Ben Morgan, Pete Elmer, Simone Campana, Sudhir Malik

News, general matters
=====================
-   Two abstracts were submitted to the [RSE 2018
    Conference](http://rse.ac.uk/conf2018/)
    -   One general one on HSF as an organisation
    -   One specific one from the Packaging WG
    -   Should hear the outcome quite soon
-   [IEEE Nuclear Science
    Symposium](http://www.nssmic.org/2018/) in Sydney,
    Australia, 10-17 November 2018
    -   Abstract submission open until 9 May
-   [IEEE eScience
    Conference](https://www.escience2018.com/) in
    Amsterdam 29 October - 1 November, 2018
    -   Abstract submission until 25 May
    -   There is a particularly relevant track on *Exascale Computing
        for High Energy Physics*

HSF/WLCG Workshop Follow-up
===========================
-   Practical follow ups at the HSF level
    -   Inventory of community activities
        -   Graeme will work on this real soon now!
    -   More variation in themes in these meetings (more topical)
        -   See news on packaging below
    -   Collaboration guide for projects
        -   Draft by Benedikt. Iterating with Graeme
-   Gordon Watts has proposed UW Seattle for the next workshop
    -   Next general meeting would probably be in \~one year from the
        HSF side
    -   Need to discuss with WLCG colleagues

PyHEP Workshop
==============
-   Attendance still increasing ... and we welcome more attendees, of
    course!
-   Status of **AGENDA**, largely finalised:

Saturday, 7 July
----------------
**09:00 -\    09:10 Welcome and workshop overview**

**09:10 -\    10:30 Historical perspective / overview**
- The slow adoption of Python in HEP
- The Python scientific software ecosystem - past, present and future
- Open discussion, guided by some survey input

**11:00 -\    12:30 HEP python software ecosystem**
- The Python ecosystem in HEP data analysis
- Python packages for Machine Learning (TBC)
- GPU-oriented Python analysis package example (TBC)

**12:30 -\    14:00 Lunch**

**14:00 -\    15:00 HEP python software ecosystem**
- Python and Deep Learning for Neutrino Experiments (TBC)
- The Scikit-HEP project

**15:00 -\    16:00 Analysis & HEP frameworks**
- The NEXT experiment analysis and data flow
- The Belle-II analysis framework

**16:00 -\    16:30 Coffee/tea break**

**16:30 -\    17:30 Distribution and installation**
- LCG releases: a complete, mult-ilanguage analysis ecosystem
- Distributing Python for the HEP environment (TBC)

**17:30 -\    18:30 PyROOT and Python bindings**
- Tools to bind to Python
- ROOT's C++ Python bindings

Sunday, 8 July
--------------
**09:00 -\    10:40 Analysis & HEP frameworks**
- KEYNOTE PRESENTATION on JupyterLab
- Python tools for simulating beam dynamics
- Python for \"core software\" in ATLAS
- Python for "core software" in CMS

**10:40 -\    11:00 Coffee/tea break**

**11:00 -\    12:00 Python 2 versus 3**
- Python 2 versus 3
- Discussion on community plans for the future

**12:00 -\    13:00 Open discussion on education and training**

**13:00 -\    14:00 Lunch**

Activity updates
================

Licensing
---------
-   [Meeting organised for next
    week](https://indico.cern.ch/event/727095/), 9 May at
    17h CERN time
    -   ATLAS and LHCb will give an update on their © and license status
    -   Belle II will report on their deliberations and open questions
-   FastJet told us they will relicense to GPLv2+
    -   This is an improvement over GPLv2 only
    -   But still copy-left, so substantial impact on users' software
-   AIDA2020 WP3 (Software) meeting discussed software licenses, and a
    move from GPLv3 to LGPLv3, summarised in the [closing
    talk](https://indico.cern.ch/event/677272/contributions/2772691/attachments/1641052/2620652/WP3_3nd_annual_summary.pdf)
    from Frank Gaede
    -   "in principle should be able to re-license relevant packages;
        need agreement of all copyright holders..."
-   Doesn't seem we have a licensing list, should we?
    -   Pere and Michel support a more focused list for discussions; we
        will set this up for next week
        
Training
--------
-   We had a kick-off meeting last Monday with the goal of trying to
    create a "*federation*" of Schools of Computing. 12 people
    attended, some of them representing existing schools some other
    just representing users. We introduced ourselves and our roles.
-   URL for minutes of Training and Career Working group 
    meeting [here](https://tinyurl.com/yddyflaq)

    Dario illustrated the goal of this initiative and its potential
    benefits (improved efficiency and cost-effectiveness of having a
    coordination among existing schools). No significant objections were
    made, so we consider the idea worthwhile to pursue and start building
    around it.

    First step consists in putting together a mini DB capturing the
    current situation (existing initiatives, goals, existing material,
    future programs,\...). This is being done on
    [https://docs.google.com/spreadsheets/d/1J5DVs0f1aUpsfp5hewGos43NCr7jr3unWMH8kivkKsc/edit\#gid=0](https://docs.google.com/spreadsheets/d/1J5DVs0f1aUpsfp5hewGos43NCr7jr3unWMH8kivkKsc/edit#gid=0)
    (please anyone, contribute with your piece of additional information
    if you have any).

    This document should later evolve in a dedicated web page (under the
    HSF site tree) to show training schedules, public
    material-presentations/good software related examples/exercises and
    best practices/reference material.

    Identified a three tier structure to work on and later develop:
    -   Lower - examples - Linux/C++/Python
    -   Medium -- ROOT/Geant4
    -   High -- Machine Learning/ GPUs/ Developer level
    
    Foreseen a regular calendar of future meetings (still to setup and
    decide)

-   Pete - many basic things are part of Software Carpentry, so we
    should try to re-use that. Will we need to augment it as well?
    E.g., data analysis for ROOT. Get a consensus around this basic
    material.
-   Dario - this wasn't really discussed, agree with the thrust of
    the idea. Input from Universities is also important.

Packaging
---------
-   Meeting [May 2](https://indico.cern.ch/event/719557/)
    covered micro-architecture builds and progress in Spack from FNAL,
    [minutes
    available](http://hepsoftwarefoundation.org/organization/2018/05/02/packaging.html).
-   Next meeting will be [May
    16](https://indico.cern.ch/event/727088/), should
    review progress on Test Driving.
    -   Updates on the packaging repo in GitHub to help people test
        this.
-   Would be good to update the note on micro-architectures.

Frameworks
----------
-   Frameworks Birds of a Feather session at CHEP
    -   Announcement needed!

GSoC
----
-   Report in the next meeting from organisers.

CWP
===
-   ### General Matters and Roadmap
    -   Agreed with editors that CWP Roadmap can be submitted to CSBS,
        Graeme and Michel will take care of preparing the submission
        in the proper LaTeX format (quite some work may be needed!).
-   ### Publication strategy for Individual WG Papers
    -   ### Machine Learning
        -   Sent ping.
    -   ### Software Trigger and Event Reconstruction
        -   Just needs PR to hsf-documents.
    -   ### Data Organisation, Management and Access
        -   Text finalized, submission about to be done by Bo.
    -   ### Data and Software Preservation
        -   Follow up with Mike.
    -   ### Visualization
        -   No news.
    -   ### Event/Data Processing Frameworks
        -   Still needs one more iteration.
    -   ### Careers, Staffing and Training
        -   Would like to verify with the community whether to include
            in the document the idea of a federation of existing (as
            well as new one) schools of computing.
    -   ### Facilities and Distributed Computing
        -   WLCG strategy document is now released. This captures a lot
            of information. Ian B will need to decide how to proceed.
    -   ### Conditions Access
        -   Sent ping.

AOB
===
-   No meeting next week (Ascension holiday in a lot of Europe).
    Reconvene on 17 May.
