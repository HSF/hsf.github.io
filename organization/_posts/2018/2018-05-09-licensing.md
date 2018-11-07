---
title: "HSF Licensing Meeting, 9 May, 2018"
layout: meetings
---

# {{page.title}}

Participants: Carl Rosenfeld, Thomas Kuhr, Graeme Stewart, Stefan
Roiser, Ed Moyse, Benedikt Hegner, Dave Dykstra, Marco Clemencic, Scott
Snyder, Pere Mato, Martin Ritter, Andrea Valassi, Michel Jouvin, Liz
Sexton-Kennedy, Davide Costanzo

Introduction
============
-   See
    [slides](https://indico.cern.ch/event/727095/contributions/2992610/attachments/1647248/2633145/HSF_Licensing_Intro_2018-05-09.pdf)
    attached to [Indico](https://indico.cern.ch/event/727095).
-   Reminder on meeting goals and the license problem: license
    compatibility makes it mandatory to have a licensing scheme
    compatible with the license of all the dependencies we use. But also
    constraints by funding bodies that are not compatible with the
    restrictive approach chosen by some dependencies.
-   Summary of experiments' approach -
    -   Apache 2 is what CMS would like to apply
-   Various projects moved from GPL to LGPL or other more permissive
    licenses.
-   FastJet staying with copyleft, but now GPLv2 or later rather than
    GPLv2, clearing the incompatibility with anything else the GPLv2
    and LGPLv2. Still obliges clients to go for GPL too.
-   Please [join](mailto:hsf-licensing-wg+subscribe@googlegroups.com)
    Working Group mailing list!
-   LCG AA - there are a lot of GPLv2 packages still - to be checked
    again (ACTION on SFT colleagues).
-   Default copyright varies country to country - copyright is an issue
    especially for changing license (something more likely to happen
    with a copyleft license than with a permissive one).
    
LHCb
====
-   Copyright to CERN as experiments are not legal entities.
-   License GPLv3 targeted, CERN copyright makes possible to relicense
    if necessary.
-   Adjusted statues and procedures in experiment.
-   Plan to be finally endorsed in collaboration board in June.
-   Some initial reservations from 2 countries, but now addressed.
-   Keeping independent record of contributions as to make them
    visible/help authors.
    
ATLAS
=====
-   Committed to open source its SW by summer 2018 and would like to
    move to Apache2 preferably, GPLv3 as a fallback solution:
    copyright ownership by CERN will allow further evolutions. Still
    trying to understand what is left preventing Apache 2.
-   Open sourcing the SW, license/copyright is only part of the work:
    also need to clean the repositories from swearwords and other
    inappropriate words/sentences: tools can help but all involve
    rewriting the history with impact on many tools...
-   Situation for Gaudi affects both LHCb and ATLAS - problem to track
    down all of the (c) holders.
    -   Some dependencies on GSL (but isolated); Gaudi plugin service is
        GPLv3, (c) CERN - could relicense this (should be easy as it is
        quite in line with the recent move supported by CERN of
        Invenio/Indico licenses).
    -   Gaudi (c) could naturally go to CERN, as most of the primary
        authors are CERN and the main experiment users are also
        CERN based.
   
Belle II
========
-   A TF created in 2017: still at the beginning of the work, no target
    license selected yet, welcoming collaboration with HSF on this
    topic.
-   The solution of ATLAS and CMS is split licensing more than dual
    licensing (each file has only one license, but mixed in the overall
    repo).
-   Started to work on assigning the copyright to one holder: KEK would
    be the natural candidate, but not a role it is prepared to have
    yet. Discussions with KEK in progress.
-   What would the fallback solution be for the copyright holder? This
    is not clear.
    -   Would CERN be in a position to hold Belle II copyright? KEK
        answer really is not known. DESY could be a fallback.
    -   Carl thinks CERN (c) could be ok for the collaboration, but very
        unclear if CERN would take this role on.
-   CERN are developing Contributor License Agreements (CLAs) that could be 
    useful models (probably not needed for experiments that have
    their collaboration boards).
-   External dependencies - there are a few GPL dependencies like GSL.
    Pythia is more of an issue.
-   We do have some traction with the theory community and want to keep
    discussing with them.
    -   They should feel part of the community and participate in this
        decision.
-   Citations are really important for the theorists.
-   We should keep a list of citations that should be used.

Discussion
==========
-   ATLAS and LHCb assigned (c) through the collaboration board.
-   We should be a bit pragmatic about contacting authors and copyright 
    holders, but make reasonable efforts to do so.
-   Action: Update LCG stack for licenses.
-   Next meeting pre-summer.
