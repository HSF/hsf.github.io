---
title: "HSF Weekly Meeting #157, 31 January, 2019"
layout: meetings
---

# {{page.title}}

*Present/Contributors*: Graeme Stewart, Danilo Piparo, Jim Amundson,
Agnieszka Dziurda, Jim Pivarski, David Lange, Witek Pokorski, Serhan
Mete, Pere Mato, Liz Sexton-Kennedy, Stefan Roiser, Caterina Doglioni,
Michel J, Guilherme Amadio, Daniel Elvira, Gloria Corti, Davide
Costanzo

*Apologies:* Heather Gray

## Google Summer of Code 2019
  - Lots of PRs coming in now.
  - Remember the HSF deadline: *February 4.*
      - But better if you can submit this week.
  - This
    [<span class="underline">presentation</span>](https://indico.cern.ch/event/785562/)
    has all the
    details.

## HSF/WLCG/OSG Workshop News and Planning
  - [<span class="underline">Indico</span>](https://indico.cern.ch/event/759388/) - registration is open.
      - Early registration ends on 1 February; 1 week extension
        probable - please register *right now*.
  - There is a Google Sheet linked from the
    [<span class="underline">main
    page</span>](https://indico.cern.ch/event/759388/) to help
    coordinate car sharing from Dulles (you take your own
    responsibility for this\!).
      - If you are arriving/travelling from another airport you can
        also use that spreadsheet (just make it clear which airport
        you will be at).

### Session Planning (see [<span class="underline">block timetable</span>](https://indico.cern.ch/event/759388/timetable/#all))
  - Reminder: David Lange, Michel Jouvin and Graeme Stewart organising
    for HSF.
  - General Sessions:
      - Opening plenary session from HEP experiments and other
        communities (Monday)
          - Confirmed talks from LHC Experiments, DUNE, Belle II, Dark
            Matter, Electron-Ion Consortium, LIGO, IceCube,
            Lightsources; yet to confirm LSST (speaker invited).
          - Plus discussion on WLCG future evolution.
      - Technology watch and networking (Tuesday AM).
      - New Workflows, New Facilities (Tuesday AM).
          - Benedikt Hegner and Maria Girone are convening.
      - Closing Session, visionary talk and discussion on the future
        (Friday).
          - Funding updates:
              - DE (Thomas Kuhr)
              - UK, IRIS (Pete Clarke)
              - US, IRIS-HEP (Pete Elmer)
              - If you are aware of any other projects that have
                secured funding for software efforts can you let us
                know?
          - Amber Boehnlein will do the final talk.
  - HSF Sessions:
      - *Please fill in a first version of your detailed timetable in
        the coming week, even if not all slots are confirmed*
          - All session convenors have management rights, let us know
            if you have any problems.
          - And do remember it’s a workshop - schedule generous
            discussion time\!
      - Software on Accelerators (2 slots).
          - Graeme, Michel, David L are convening.
              - Confirmed talks on Accelerator Technologies, Framework
                Integration, Patatrack, ALICE GPU Algorithms, MadGraph
                on GPUs
              - One last speaker to confirm, will leave plenty of time
                for discussion.
      - For other HSF Parallel Sessions, see WG activity reports
        below.
      - Due to the logistics of rooms at JLab we propose that:
          - We only have one session on Wednesday 16h-17h30
          - We move the other two WG’s second sessions to Thursday
            9h-10h30
          - We move Software Tools to Thursday 16h-17h30
              - N.B. Still likely that small rooms would be available
                for any BoFs

## Activity and Working Group Updates
General points:
  - Reminder to make sure your WG page has
      - Brief description of the interests of the group
      - Information on how to join the group’s mailing list
      - Information on how to contact the convenors (convenor list or
        individual emails)
      - A link to the group’s Indico category

### Data Analysis
  - Second meeting (afternoon of Feb 13th) of the WG in preparation:
    [<span class="underline">https://indico.cern.ch/event/789007/</span>](https://indico.cern.ch/event/789007/)
  - Refined focus of the meeting to survey innovation and best
    practice from the community
  - Meeting will be workshop in style, shorter talks, focus on the
    ideas, “what is the ground-breaking, earth-shattering idea(s) /
    functionality that make your framework/tool so useful?”

### Detector Simulation
  - First topical meeting [<span class="underline">yesterday on
    FastSim</span>](https://indico.cern.ch/event/782507/).
      - Nice overview from LHC experiments.
      - In future address non-LHC experiments as well.
      - Daniel can help with contact to IF (division between fast/full
        sim for IF less clear, but simulation very relevant for them
        too).
  - [<span class="underline">Next
    meeting</span>](https://indico.cern.ch/event/782508/) on ML, 6
    March.
  - Invitations being sent for the workshop, some speakers might have
    to be remote.

### Reconstruction and Software Triggers
  - Indico updated (15+5) min with 10 min discussion.
  - Talks accepted:
      - Machine Learning for the Primary Vertex reconstruction.
      - Using FPGAs to accelerate machine learning inference.
      - A comprehensive real-time analysis model at the LHCb
        experiment.
      - \[still waiting for speaker, but Speakers Committees have said
        yes\]: real-time analysis in CMS/ATLAS/ALICE.
  - We are waiting still to get feedback from:
      - DUNE/Belle II/LSST (machine learning).
  - We planned to have a first meeting next week, but due to people’s
    unavailability we decided to postpone - more news next week.

### Software Tools
  - Invitations for JLab session to be sent tomorrow.

### PyHEP
  - Plan to divide 1.5 hours (14:00‒15:30 on Thursday) into
      - two 15+5 minute long talks
          - considering LPC Coffea group’s Numpy-based CMS analyses
          - invited Stan Seibert to present Numba (Python
            JIT-compiler)
      - three 5+5 minute lightning talks
          - confirmed talk on
            [<span class="underline">zfit</span>](https://github.com/zfit/zfit)
            by Albert Puig, Jonas Eschle, Rafael Silva Coutinho
          - invited ROOT Team to present ROOT packaging in Conda
          - looking for a final talk on Python in neutrinos, dark
            matter, or BELLE...
      - 20 minutes of free-form discussion

### Licensing
  - Still chasing up CERN KT and FastJet authors.

### Packaging
  - Meeting yesterday. Group plans to track work on various projects.
    Main topic was an [<span class="underline">update on
    Conda</span>](https://indico.cern.ch/event/790021/contributions/3301108/attachments/1787718/2911364/2019-01-30_HSF-Packaging-Conda.pdf) -
    very interesting to see how this tool has hugely progressed
    since the first meetings of the WG. New ROOT recipe seems to be
    very nicely integrated now.
  - Next meeting in 1 month, 27 February.

## AOB
  - URL checks on website are unreliable; another URL check code could
    be tried to see if that improves things.
  - Working on an update to the instructions for converting Google Doc
    -\> Word -\> Markdown.
