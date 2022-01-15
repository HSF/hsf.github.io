---
title: "HSF Weekly Meeting #155, 17 January, 2019"
layout: meetings
---

# {{page.title}}

*Present/Contributors*: Graeme Stewart, Dario Menasce, Sudhir Malik,
Andrei Gheata, Danilo Piparo, Giulio Eulisse, Tommaso Boccali, Serhan
Mate, Witek Pokorski, Stefan Roiser, Concezio Bozzi, Andrea Valassi,
Javier Cervantes Villanueva, Marco Clemencic, Torre Wenaus, Eduardo
Rodrigues, Agnieszka Dziurda, Antoine Perus, Caterina Doglioni, Chris
Tunnell, Davide Costanzo, Liz Sexton-Kennedy, Heather Gray, Josh
McFadyen, Martin Ritter, Michael Kirby, Paul Laycock, Daniel Elvira,
David Lange

## Google Summer of Code 2019
  -  See slides attached to the
    [<span class="underline">agenda</span>](https://indico.cern.ch/event/785562/).
  -  Do students come to your institute?
      -  No, they are all remote. Has a very big pool of candidates for
        this reason.
      -  Payment is linked to continued success at checkpoints.
  -  Level of students?
      -  Typically masters.
  -  Proposals are filtered by organisation first, if more proposals
    than awarded slots.
  -  Having a good group of mentors (>2) really helps.
  -  Activity now is important to have a good allocation of slots from
    Google.

## HSF/WLCG/OSG Workshop News and Planning
  -  [<span class="underline">Indico</span>](https://indico.cern.ch/event/759388/)
    - registration is open, please sign up.
      -  N.B. The JLab rate at the Marriott is a good one.
  -  There is a Google Sheet linked from the
    [<span class="underline">main
    page</span>](https://indico.cern.ch/event/759388/) to help
    coordinate car sharing from Dulles (you take your own
    responsibility for this\!).
  -  Please advertise again in your community.
  -  There is a
    [<span class="underline">poster</span>](https://indico.cern.ch/event/759388/attachments/1770924/2877653/HOW2019.pdf)
    that can be printed and put on your local notice boards.

### Session Planning (see [<span class="underline">block timetable</span>](https://indico.cern.ch/event/759388/timetable/#all))
  -  Reminder: David Lange, Michel Jouvin and Graeme Stewart organising
    for HSF.
  -  General Session News:
      -  New Workflows, New Facilities (Tuesday AM).
          -  Benedikt Hegner and Maria Girone are convening.
      -  Closing Session, visionary talk and discussion on the future
        (Friday).
          -  Amber Boehnlein has agreed to do the final talk.
  -  HSF Sessions:
      -  Software on Accelerators (2 slots).
          -  Graeme, Michel, David L will convene; send suggestions
            (generators, tracking, etc. style projects)
              -  Various invitations issued now, but further
                suggestions welcome.
              -  Talks that have generic conclusions evidently
                favoured.
      -  Simulation (2 slots, with one in parallel with other HSF
        sessions; idea is to use first slot for topics of general
        interest, second for items that are more technical or narrow
        in focus).
          - Heather: It would be useful to get feedback about which
        topics should be plenary vs more technical (I suspect that
        most of the topics that we have would be of quite general
        interest).
          -  fast simulation.
          -  physics models.
          -  common geometry tools.
          -  pile-up.
          -  vectorisation (Andrei).
          -  common geometry tools.
          -  simulation code on new architectures (particularly g4).
      -  Reconstruction (2 slots, 1 “parallel”)
          -  Brainstorming on topics, converging on Tuesday.
          -  Question on whether there could be more non-HEP-specific
            talks (we have contacts from recent ITNs on interesting
            topics).
          -  Initial topics (we will trim down/add, this is to see
            overlap with other sessions):
              -  Hybrid architectures and accelerators for triggers.
              -  ML for reconstruction.
              -  ML for trigger.
                  -  Connect to DarkMachines effort (some people from
                    Unsupervised Learning group based in the US).
              -  LHC: Run-3 preparations and expectations.
              -  HL-LHC: Updates on TDRs.
              -  Beyond colliders: what are smaller experiments
                planning / doing (use Physics Beyond Colliders
                platform to advertise a call for talks).
      -  Analysis (2 slots, 1 “parallel”)
          -  Using events at CERN to help plan contribution (see below).
      -  Software Tools (1 slot)
          -  Martin, Giulio and Serhan will discuss next week.
          -  Overlaps with analysis are interesting.
      -  Education and Training (1 slot)
          -  Initial thoughts from Sudhir/Dario:
              -  Highlight ramping of US centric training efforts
            FIRST-HEP/IRIS-HEP.
              -  How can these efforts be expanded to Europe and beyond.
              -  Invite speakers/European counterparts (people who might
            lead efforts there - NOT adhoc basis).
                  -  Now that ITN deadline for European graduate schools
                has passed maybe we can talk about them as a source of
                coordinated effort (and maybe a step towards bigger
                efforts)?
      -  PyHEP (1 slot)
          -  We met this week and converged on a draft agenda for the
            HSF session at JLab.
          -  Basically a 30-minute part with lightning talks and the
            rest for 2 topical presentations, leaving the last 20
            minutes for an open discussion (e.g.: activities in 2019,
            community interests).
      -  One spillover BoF slot.

## Activity and Working Group Updates
General points:
  -  There is now a mailing list for all working group convenors
      -  hsf-wg-convenors (at) googlegroups.com.
          -  This is postable by all (does anyone know how to restrict
            posting to members of other groups, like hsf-forum?).
      -  If you are involved in a WG and did not get an email then
        please let Graeme know.
      -  We will allow this group to be able to edit the
        [<span class="underline">HSF community
        calendar</span>](https://calendar.google.com/calendar/embed?src=e4v33e1a1drbncdle1n03ahpcs%40group.calendar.google.com&ctz=Europe/Amsterdam)
        to add their meetings.
  -  Please set up mailing lists and advertise them on your group page.
      -  HSF website “Mailing Lists and Discussion Forums” links to all
        WGs’ and activities’ pages.
  -  We can help with [<span class="underline">website
    practicalities</span>](https://hepsoftwarefoundation.org/howto-website.html).
  -  For the first announcement of new group’s activities you can send
    an email to the whole HSF using the hsf-forum list (any subscriber
    can post).
  -  Activities can also be added to a banner announcement on the HSF
    frontpage (see, e.g., this
    [<span class="underline">commit</span>](https://github.com/HSF/hsf.github.io/commit/71bdb4e841dbc0e106983732f42756a99c0ee30a)).

### Data Analysis
  -  Preparing 2 events at CERN:
      -  23 Jan - what analysers distill from their experience.
      -  13 Feb - technology used for analysis.

### Detector Simulation
  -  We’ve been working on the agenda for the fast simulation session
    at the workshop (see above).
  -  Planning the discussion on Fast Simulation for 30 January
      -  We plan to have 3 overview talks: ATLAS, CMS and LHCb and each
        talk would be 20+10’.
  -  Potential topic for meeting on 6 March: Applications of machine
    learning for fast simulation.

### Reconstruction and Software Triggers
  -  We aim to have the first meeting: February 6th.
  -  Changed name of the mailing list:
    [<span class="underline">https://groups.google.com/forum/\#\!forum/hsf-recotrigger</span>](https://groups.google.com/forum/#!forum/hsf-recotrigger)
  -  We discussed among ourselves potential topics for the HSF/WCLG
    workshop, will give more specific proposal next week.
  -  We aim to discuss with experiment representatives in the coming
    weeks.

### Event Generators
  -  Getting organized (discussing mailing lists, meetings…).
  -  Follow up of the November workshop.
      -  Contacted the Madgraph team about their GPU code - Stefan
        Roiser interested in doing some concrete work and tests on
        that.
      -  Not much progress on the write up of the workshop.
      -  Andy Buckley will give a theory plenary at ACAT also covering
        the workshop.
  -  No specific plans for the JLAB workshop, some generator speakers
    have been or may be contacted for other sessions
    (GPU/accelerators, HPC).

### Licensing
  -  Discussion about licensing in the AF meeting - how to relicense
    Gaudi code (some parts currently (c) CERN and GPLv3).
      -  HSF will help to carry this discussion with CERN to a
        conclusion.
  -  Still need to discuss FastJet license.

### Training
  -  Got great feedback (\~350 people) in response to training needs in
    terms of software and computing for HEP.

### Packaging
  -  [<span class="underline">Next
    meeting</span>](https://indico.cern.ch/event/790021/) scheduled
    for 30 January.

### PyHEP
  -  Graeme is stepping down since over-committed. But will keep
    contributing when possible - thank you so much, Graeme!
  -  Welcome to Jim Pivarski to the conveners team!

## CWP

#### Publication status for Individual WG Papers
  -  **Conditions Access**
      -  Paul has uploaded the Conditions Paper to arXiv -
        yay\!
      -  [<span class="underline">https://arxiv.org/abs/1901.05429</span>](https://arxiv.org/abs/1901.05429)

## AOB
  -  We will do a clean-up of the HSF Coordinators list.
      -  Active coordinators and ex-officio members stay on the list.
      -  New proposals for active coordinators are always welcome.
  -  Reminder - if anyone gives a talk that is of relevance to HSF
    activities we can add it to our
    [<span class="underline">presentations
    list</span>](https://hepsoftwarefoundation.org/organization/presentations.html).
      -  Eduardo gave a very useful [talk on software citations and
        publications]({{ site.baseurl }}/assets/EduardoRodrigues-LHCb-2019-01-15.pdf)
        to LHCb, that is now available.
