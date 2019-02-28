---
title: "HSF Weekly Meeting #160, 28 February, 2019"
layout: meetings
---

# {{page.title}}

*Present/Contributors*: Graeme Stewart, André Sailer, Marko Petric,
Tommaso Boccali, Danilo Piparo, Pere Mato, Stefan Roiser, Andrea
Valassi, Eduardo Rodrigues, David Lange, Agnieszka Dziurda, Serhan Mete,
Andrea Rizzi, Caterina Doglioni, Ed Moyse, Jim Amundson, Liz
Sexton-Kennedy, Mark Hodgkinson, Daniel Elvira, Heather Grey, Markus
Klute

## News, general matters
  - [<span class="underline">LHCC WLCG
    Meeting</span>](https://indico.cern.ch/event/754731/):
      - Graeme presented slides from software projects and HSF.
      - Question asked about Geant vectorisation R&D:
          - Emphasised again the intent to deliver improvements into
            production Geant4.
      - Discussion about accelerator integration and framework from
        CMS presentation:
          - Pointed to JLab workshop as a place to discuss this.
      - Support from referees for common software work.
  - AccelNet:FRESCO support letter
      - See
        [<span class="underline">agenda</span>](https://indico.cern.ch/event/785568/)
        for project description and draft letter.
      - To clarify, the HSF in the project application is described
        as:
          - *HSF: The HEP Software Foundation (HSF) encourages
            cooperation and common development of software in HEP. The
            HSF hosts a number of software-focused working groups and
            projects where developers are collaborating. These include
            groups on physics generator models, detector simulation
            techniques, event reconstruction techniques and approaches
            to software packaging.*
      - i.e. HSF as a forum to build networks and locate community
        experts.
      - André can you mention CLIC?
          - Yes, now it’s there.
      - Meeting approved the letter of support.

## Google Summer of Code 2019
  - We are accepted as an organisation again.
  - There is a [<span class="underline">meeting for all mentors
    tomorrow at 14h CERN
    time</span>](https://indico.cern.ch/event/802397/).
      - Will cover how to interact with students and the timeline.
  - Proposal for Advisory Committee:
      - [<span class="underline">https://docs.google.com
        /document/d/17ifO0i4O5JsBVKkcx3j75Z\_iW2bXFnCbqFB2YirlJQw/edit?usp=sharing</span>](https://docs.google.com/document/d/17ifO0i4O5JsBVKkcx3j75Z_iW2bXFnCbqFB2YirlJQw/edit?usp=sharing)
      - Need help to select projects against slots (assuming slots \<
        projects).
          - Should also assess given the potential students.
          - 3 people proposed - better if these are not mentors.
          - Criteria: novelty, student rank, impact, etc.
  - *Please review and comment on the proposal in the next week*, aim
    to approve in next week’s meeting.
      - If you would be willing to serve as on the AC please let HSF
        Coordination know.

## HSF/WLCG/OSG Workshop News and Planning
  - [<span class="underline">Indico</span>](https://indico.cern.ch/event/759388/) registration is still open.
      - 221 people registered.
  - There is a Google Sheet linked from the
    [<span class="underline">main
    page</span>](https://indico.cern.ch/event/759388/) to help
    coordinate car sharing from Dulles (you take your own
    responsibility for this\!).

### Session Planning (see [<span class="underline">block timetable</span>](https://indico.cern.ch/event/759388/timetable/#all))
  - Reminder: David Lange, Michel Jouvin and Graeme Stewart organising
    for HSF.
  - General Sessions:
      - Plenary sessions all fixed now.
  - HSF Sessions:
      - Rooms:
          - Will do a sound check with Amber and LOC next week to
            verify Vidyo connection is acceptable.
      - For planning other HSF Parallel Sessions, see WG activity
        reports below.
  - We will contact Amber about JLab entry requirements (some worries
    that people may need CVs due to changes in DOE rules).

## Activity and Working Group Updates

### Data Analysis
  - Draft agenda for JLAB discussed, here a draft (speakers being
    contacted).
      - 1st session: Where are we now, where are we going ?
          - 20' talk on analysis needs and how they are served today
            (Paul)
          - 20' talk on what's missing today (Andrea)
          - 20’ talk on evolution of HEP computing implications for
            analysis (data distribution, access to resources, hardware
            platforms, ...) (TBD)
          - 30' discussion
      - 2nd session: Technology
          - 20' talk on the future techs (Danilo)
          - 20' talk on Python and frameworks for declarative
            analyses(Jim/Nick)
              - *Check for overlaps with PyHEP session talk on Coffea!*
          - 20' talk on ROOT Declarative framework: RDF (Stefan)
          - 30' discussion
  - Timetable should go into Indico, even if not 100% settled.

### Detector Simulation
  - Agenda for the HSF meeting is finalised -- both talks and
    speakers.
      - Overall philosophy: tried to assign a balance of speakers from
        experiments. Expect each speaker to summarise one topic
        focusing both on their own work and also the perspective from
        other experiments
  - Next topical meeting on 6 March:
    [<span class="underline">https://indico.cern.ch/event/782508/</span>](https://indico.cern.ch/event/782508/)
      - Need to add agenda entries for that meeting.

### Reconstruction and Software Triggers
  - Agenda for HSF meeting finalised (talks and speakers).
      - Session 1: real-time analysis, talks from LHCb, ATLAS, CMS,
        ALICE.
      - Session 2: ML/accelerators for reconstruction, talks on LHCb
        tracking, GPU for IceCube, ML in FPGA, JLab reconstruction
        challenges.
      - Plan to have a chat/meeting with all speakers to prepare the
        discussion session.
          - We (WG coords) will look at the talks and prepare 2-3
            questions in advance so that we can have a discussion at
            the workshop.
              - General direction of questions:
                  - Is there room for collaboration and where?
                  - Are upgrades & detectors real-time-analysis ready?
  - Topical meetings: would like to have a shared calendar with other
    groups (e.g., IRIS-HEP) to pick dates for our own without
    conflicts.
      - It’s already hard enough for us to find time where we’re all
        available :).
      - Should we have an HSF + others google calendar?
          - This is possible with the current HSF calendar.
          - Graeme will send [instructions](https://hepsoftwarefoundation.org/calendar.html) on how to edit and add
            entries.

### Software Tools
  - JLab session well defined.

### PyHEP
  - JLab 1.5h session is finalised. Outside speaker from Anaconda.

### Training
  - [PR in progress](https://github.com/HSF/hsf.github.io/pull/477) for listing training events on the HSF website.

### Event Generators
  - Will have regular open meetings every two-weeks, first is this
    afternoon at 16h00 after this meeting (but on a different Vidyo
    room). [<span class="underline">28th Feb
    16h00</span>](https://indico.cern.ch/event/799316/).

### Licensing
  - Discussion on Gaudi Plugin Service / Gaudi License with CERN KT.
      - Re. code ©CERN, responsibility for re-licensing open source
        code is given to the CERN group that develops the code. In
        this case EP-LBC.
          - Thus is should be fine to relicense from GPLv3 -\>
            Apache2.
      - With that change the intention is to ©Gaudi to CERN, for the
        benefit of the ATLAS and LHCb collaborations; and to apply an
        Apache2 licence.
  - CERN have a webpage that recommends
        GPLv3:
      - [<span class="underline">https://legal.web.cern.ch/licensing/software-terms-use</span>](https://legal.web.cern.ch/licensing/software-terms-use)
      - We think this is anachronistic - Graeme will follow up with
        KT.
  - Still no response from FastJet authors.

### Packaging
  - Held a meeting on 27
        February.
      - [<span class="underline">NixCon</span>](https://nixcon2018.org/)
        (Chris Burr attended).
      - Spack update (HEP people now have merge rights for our
        packages; we also have our own Slack channel).

## CWP

#### Roadmap
  - We got final proofs from CSBS.
      - Eduardo and Michel noticed quite a few errors, which have been
        pointed out to Springer and will be corrected.
