---
title: "HSF Weekly Meeting #131, 22 March, 2018"
layout: default
---

# {{page.title}}

#### *Present/Contributors*: Graeme Stewart, Michel Jouvin, Ian Bird, Jim Pivarski, Mohammad Al-Turany, Eduardo Rodrigues, Pere Mato, Marco, Benedikt Hegner, David Lange, Giulio Eulisse, Simone Campana, Ben Morgan, Peter Elmer, Ricardo Maria Bianchi, Daniel Elvira, Elizabeth Sexton-Kennedy.

News, general matters
=====================
-   [UK Research Software Engineer Association](http://rse.ac.uk/) has their 2018 conference [call for
    papers](http://rse.ac.uk/conf2018/calls/) out.
    -   Mention this on the forum list, for our UK people.
    -   Ben Morgan might be interested, particularly for our packaging
        efforts.

HSF/WLCG Workshop
=================
-   ### General points
    -   210 people registered.
    -   Local details checked with organisers, all looks good.
    -   Vidyo:
        -   Vidyo setup is tested, we have one stationary mic and one or
            two mobile microphones in each room.
        -   **Session convenors** - please organise some microphone runners.
    -   Live notes
        -   In the finest tradition of HSF meetings, there is a [live
            notebook](https://docs.google.com/document/d/1QSkvwRK_2HENuxYXcs9Op1dTUK824KddQ1Tfan-P0WU/edit?usp=sharing).
        -   **Session convenors** - make sure that someone is taking notes.
    - Other LOC Matters:
        -   Taxis - how to get them from the airport
            outside or book at an inside office. (Answer - [just go outside](https://indico.cern.ch/event/658060/page/12427-travel-info).)
        -   For people arriving in Rome, what to do? (Answer - [get the train](https://indico.cern.ch/event/658060/page/12427-travel-info).)
        -   One of the speakers wants a live demo - 8888 any port blocks
            outbound? (Answer - should be ok and there is a backup plan if it's a problem.) 
        -   Room PC setups - is there HDMI or VGA? (Answer - HDMI, VGA and mini-display port should all be ok.)
-   ### Outcomes
    -   [Single
        slide](https://docs.google.com/presentation/d/1YqcuyEXEHkuC2KchwbkKS0uO1pR4lHSKrhvLyBeadPI/edit?usp=sharing)
        of questions and key points is written.
        -   Given the shortness of time on Thursday, a template is
            probably not ideal - let people pick the important and
            relevant things.
        -   Emphasise *common projects*.
-   ### Monday
    -   Opening Plenary
        -   Graeme and Ian are working on some opening questions for the
            discussion.
    -   HEP Use Cases
        -   Agenda should now be complete. We don't yet have simulation
            use cases. Will present that in the introduction, along
            with analysis.
-   ### Tuesday
    -   DPHEP (Parallel)
        -   All set.
-   ### Wednesday
    -   Visualisation (Parallel)
        -   Agenda finalized on Indico.
        -   Contributions from ATLAS, Belle II, CMS and joint projects
            with GSI/ROOT and Ljubljana.
        -   Discussion on future development of
            test-projects/demonstrators
-   ### Thursday
    -   Closing Plenary
        -   Planned now in Indico. Graeme and Ian will give the final
            talks on the vision for the way forward.
CWP
===
-   ### General Matters and Roadmap
    -   Graeme got a draft of one of the Symmetry Magazine articles to
        check - looks like a nice snappy article emphasising the
        importance of software for the LHC upgrades.
        -   Pete also got it.
    -   Chasing a few obvious missing persons in the author list...
        (currently 300 authors). May be good to review the author list
        of the topical papers to identify missing people for the
        global CWP.
        -   **Working Group convenors** - please check this.
    -   Michel has improved the author tex generating script. Allow the
        reuse of affiliations from the global CWP for improved
        consistency. Can also generate a tex file to build the author
        list in the (JHEP-formatted) title page rather than as a
        separate appendix.
        -   Contact Michel for details...
-   ### Publication strategy for Individual WG Papers
    -   ### Machine Learning
        -   No news.
    -   ### Software Trigger and Event Reconstruction
        -   PR for the documents repo please!
    -   ### Data Organisation, Management and Access
        -   [Current
            version](https://github.com/HSF/documents/tree/master/CWP/papers/HSF-CWP-2017-04_doma)
            put in documents repo. In pretty good shape.
        -   Needs review by the WG and probably some references
            (completely absent currently).
    -   ### Data and Software Preservation
        -   In final proof stage.
    -   ### Data Analysis and Interpretation
        -   [Version](https://github.com/HSF/documents/tree/master/CWP/papers/HSF-CWP-2017-05_analysis/latex)
            (final?) now uploaded to documents repo.
    -   ### Visualization
        -   Use Naples for final comments on content, from the WG.
    -   ### Event/Data Processing Frameworks
        -   Use Naples to draw this together.
    -   ### Careers, Staffing and Training
        -   Want to incorporate thoughts from Naples and revise, given
            the wider community involved there.
    -   ### Facilities and Distributed Computing
        -   Waiting until after the WLCG strategy document is done.
    -   ### Conditions Access
        -   Paul hasn't found cycles yet.
    -   ### Generators
        -   Discuss at Naples.
        
PyHEP Workshop
==============
-   N(major)TR - progress with agenda and set of confirmed speakers.
-   So far, 13 participants, to compare with 56 for CHEP itself.

Activity updates
================

Packaging
---------
-   CHEP paper accepted as oral. Finalised Use Cases document and now
    looking to "test drive" different tools. Looked at the use of
    [Nix](https://nixos.org/nix/) in LHCb in the [21
    March](https://indico.cern.ch/event/712739/) meeting.
    Seems a very attractive and capable tool; philosophically quite
    different from our current practice. Lots of animated discussion
    about use cases for patching older releases in particular.
    [Minutes
    available](http://hepsoftwarefoundation.org/organization/2018/03/21/packaging.html).
-   Will contribute to the Software Development session in Naples.
-   Next meeting [5 April](https://indico.cern.ch/event/716297/).
    
GSoC
----
(Notes added after the meeting)
-   Process of students applying in progress until **March 27th**
-   Mentors need to make sure that students submit to Google:
    -   The final version of their project proposal. It can be first
        submitted as \"Draft\" for mentors to review it, but in the
        end it has to be submitted as \"Final\" on the GSoC website.
    -   Proof of enrollment in an accredited university or college.
-   After March 27th, mentors will need to provide admins with a ranking
    of the students (maximum 3), together with a review of each of
    them (performance in the evaluation tests and in the project
    proposal).
    
AOB
===
-   HSF Rebranded!
    -   Mailing lists were renamed:
        -   hep-sf-startup-team -> hsf-coordination
        -   hep-sf-* -> hsf-*
        -   Mailing lists should be aliased from the old ones - to
            check.
        -   **Update** - mailing lists are not aliased. We have to use the
            new ones.
    -   Website was updated with new links, but please raise an issue if
        you spot any anachronistic references to old names.
