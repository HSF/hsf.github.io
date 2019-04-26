---
title: "HSF Weekly Meeting #164, 25 April, 2019"
layout: meetings
---

# {{page.title}}

*Present/Contributors*: Graeme Stewart, Witek Pokorski, Heather Gray,
Andrei Gheata, Javier Cervantes, Eduardo Rodrigues, Marco Clemencic,
Andrea Rizzi, David Lange, Daniel Elvira, Pete Mato, Mark Neubauer,
Caterina Doglioni, Agnieszka Dziurda, Paul Laycock, Liz Sexton-Kennedy,
Michel Jouvin, Martin Ritter, Sudhir Malik, Davide Costanzo

## News, general matters
  - CernVM Workshop is quite soon, 3-5 June. Please
        register:
      - [<span class="underline">https://indico.cern.ch/event/757415/</span>](https://indico.cern.ch/event/757415/)

## Google Summer of Code 2019
  - Slots requested: min 30 - max 35.
  - Accepted slots: 34 (5 more than last year).
  - We need to start ranking projects and selecting students.
  - 36 projects were eligible, but 1 had no proposals, making 35.
  - So had to cut just one project (done based on advisory committee
    input - thanks to them).
  - Will organise a few meetings one only for mentors and one for
    students + mentors.
  - Students will be confirmed by 6 May.
  - Mentors should not contact students, but can start preparations
    for involving the students from May.
  - Q. Can you sent a summary to the mentor list?
      - Will post a message soon.

### Google Season of Docs
  - We submitted our application to be an umbrella organisation.
  - Three proposals: ROOT, Rucio, DIRAC.
  - Google have said they will only give 1-2 writers, but perhaps
    different for umbrella organisation, we are asking.

## Activity and Working Group Updates

### Data Analysis
  - Preparing the next two meetings. Indico
        links:
      - [<span class="underline">https://indico.cern.ch/event/813207/</span>](https://indico.cern.ch/event/813207/)
      - [<span class="underline">https://indico.cern.ch/event/813208/</span>](https://indico.cern.ch/event/813208/)
  - These are clashes with HSF Coordination meeting on Thursdays, not
    ideal, but was the best option with other constraints.
  - Next week there is also the FNAL workshop on
    [<span class="underline">declarative analysis
    languages</span>](https://indico.cern.ch/event/769263/).

### Detector Simulation
  - Preparing for next two topical meetings. Indico agendas are now
    available. Please don’t hesitate to get in contact with us if
    you’d like to suggest any presentations or future topical
    meetings.
      - [<span class="underline">https://indico.cern.ch/event/816484/</span>](https://indico.cern.ch/event/816484/)
      - [<span class="underline">https://indico.cern.ch/event/816485/</span>](https://indico.cern.ch/event/816485/)

### Reconstruction and Software Triggers
  - We had several convenors’ discussions before Easter break, the
    outcome is following:
  - ATLAS/CMS cross-talks:
      - 22nd May,
        4pm.
      - [<span class="underline">https://indico.cern.ch/event/815233/</span>](https://indico.cern.ch/event/815233/)
      - Speakers confirmed: Jiri Masik (ATLAS), Simone Gennai (CMS)
  - Plan to have meeting on 5th June:
      - Topic: Algorithms and data structures to efficiently exploit
        many-core architectures - one of the topics described in CWP.
      - Invitations to collaborations will be sent shortly.
  - We discussed many several potential subjects for our meetings:
      - DUNE reconstruction,
      - DarkMatter,
      - Benchmarking for different architectures (x64, GPU, FPGA),
      - SOA vs AOS data format design
      - Packages that help go from cuda--\>CPU or c++-\> GPU
      - Organize taster sessions to coding on non-CPU (together with
        Training?)
          - HLS for FPGA
          - GPU programming
  - We decided to go through the list and aim to have 1 meeting in
    every 3-4 weeks.

### PyHEP
  - NTR on organisation of meetings.
  - A lot of discussion on design of histogramming packages at
    [<span class="underline">https://gitter.im/HSF/PyHEP-histogramming</span>](https://gitter.im/HSF/PyHEP-histogramming).
    Do join if you want to participate as user/developer/chatter …
      - IRIS-HEP topical meeting on histogramming just over one week
        ago, see
        [<span class="underline">https://indico.cern.ch/event/803122/</span>](https://indico.cern.ch/event/803122/).

### Training
  - See
    [<span class="underline">slides</span>](https://indico.cern.ch/event/785576/contributions/3266720/attachments/1776008/3004837/HSF_TEO_WG_update_25April2019.pdf)
    attached to today’s agenda.
  - Liz is organising a C++ training event at FNAL next month. Good
    instructor, but we need to see how well this works for an HEP
    audience.
  - Feedback from carpentry people who taught at FNAL? Were the
    students more advanced?
      - They were pre-warned about the level and adapted the material.
      - Students were very happy with the course.
  - Can we think about a future event in Europe?
      - Yes, it’s planned for after the round of current US events.

### Event Generators
  - Next meeting planned for 9 May.

### Event Delivery Forum
  - [<span class="underline">Mailing
    list</span>](https://groups.google.com/forum/#!forum/hsf-event-processing-wg)
    and [<span class="underline">GitHub
    repo</span>](https://github.com/HSF/iDDS) setup.

### Packaging
  - Meeting this week was postponed until May.
      - Probably Wednesday 29:
        [<span class="underline">https://doodle.com/poll/xzpu6zg2nsprghqa</span>](https://doodle.com/poll/xzpu6zg2nsprghqa)

### Frameworks
  - Would still like to work on a mandate for a revitalised frameworks
    group post-JLab - contact Graeme and Liz if you are interested in
    helping.

## Workshops

### Pre-CHEP (2-3 November)
  - First organisation meeting last Tuesday (23 April): only Ian C.,
    Michel and Simone. List created for the organizing committee:
    [<span class="underline">wlcg-hsf-workshop-2019-organisation@cern.ch</span>](mailto:wlcg-hsf-workshop-2019-organisation@cern.ch).
    Let Michel or Ian C. know if you want to be involved.
  - Proposal is to have a 2 x half day meeting from Saturday noon to
    Sunday noon so that people can rest a little bit during the
    weekend before the CHEP week. Idea is to focus on one topic that
    could be of interest for HSF (SW) and WLCG (infrastructure), with
    no parallel session. Suggested topic is analysis from DOMA to SW
    tools.
      - Paul - would have to plan properly, but it’s a good idea.
      - Need to distinguish it from the CHEP talks and presentations.
        More discussions, break across the site/users boundary.
      - TODO: add Andrea and Paul to mailing list.
      - Baseline proposal generally supported during the coordination
        discussion
  - Parallel rooms are available, should people want a BoF or the
    like, but in general we don’t want a lot of parallel sessions.

## AOB
  - Simulation developers have asked for an HSF convened meeting to
    present the results of the GeantV prototype and to discuss plans
    for the future.
      - Proposed datetime is 8 October, 14-18h.
          - Noted a clash with a non-CERN ATLAS week
          - Would be better the following week (w/b 14 Oct) as any
            “clash” with HEPiX should be quite limited.
          - Witek will check with colleagues.
  - Graeme added the next few WG meetings as announcements to the
    website.
      - Note we have to have far too many manual steps right now for
        meetings:
          - Create Indico.
          - Add to community calendar.
          - Do a PR to the website for a banner via an “announcement”.
      - It’s tedious, tricky and error prone - want to improve it.
      - Discussion of improvements on
        [<span class="underline">GitHub</span>](https://github.com/HSF/hsf.github.io/issues/567)
        (happy to have people help\!).
  - Next coordination meeting planned for 2 weeks time, 9 May.
