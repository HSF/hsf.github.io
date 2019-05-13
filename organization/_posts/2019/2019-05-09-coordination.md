---
title: "HSF Weekly Meeting #165, 9 May, 2019"
layout: meetings
---

# {{page.title}}

*Present/Contributors*: Graeme Stewart, Tommaso Boccali, Marco Clemencic, Davide
Costanzo, Serhan Mete, Andrea Valassi, Guilherme Amadio, Michel Jouvin, Heather
Gray, Daniel Elvira, Ben Morgan, Agnieszka Dziurda

## News, general matters
  - European Strategy Update [<span class="underline">meeting in
    Granda next week</span>](https://indico.cern.ch/event/808335):
      - There is a general introduction to computing on Monday
        (Simone).
      - Software and Computing Parallel session Wednesday AM, covering
        current status and R&D topics for the future.
      - Graeme’s Software R&D has much HSF inspiration in it,
        [<span class="underline">draft
        available</span>](https://docs.google.com/presentation/d/1wVi0jjanzNeNad-DFprcIkmdo1oGHwdkYgo6D-BnVz0/edit?usp=sharing)
        and comments welcome (N.B. it is driven a lot by the set of
        submissions to the process).
  - Future Collider Software Workshop is being organised in Bologna,
    12-13 June:
      - [<span class="underline">https://agenda.infn.it/event/19047/</span>](https://agenda.infn.it/event/19047/).
      - This is aiming at reviewing and finding harmony between
        different software packages and stacks for future experiments.
  - AIDA++:
      - A follow-up project to
        [<span class="underline">AIDA2020</span>](http://aida2020.web.cern.ch)
        is planned, with an EoI call expected soon.
      - The software group of AIDA2020 is planning a f2f meeting at
        CERN 17-18 June to discuss tasks that might form part of the
        project.
          - Contact Witek Pokorski and Frank Gaede for more details.
  - UK STFC Opportunities Call:
      - [<span class="underline">https://stfc.ukri.org/funding/research-grants/funding-opportunities/2019-opportunities-call/</span>](https://stfc.ukri.org/funding/research-grants/funding-opportunities/2019-opportunities-call/).
      - For STFC PPAN only, but encompasses wide area and mentions
        computing, so of potential interest to UK HSF people.

## Google Summer of Code 2019
  - 34 slots granted, +5 slots cf. 2018. 33 used.
  - There is a [mentors meeting](https://indico.cern.ch/event/816889/) at 17h today.
  - Accessing CERN gitlab for external people is a problem.
      - It’s a pain to register people so they can comment, submit MRs, etc.
        (N.B. public projects can be viewed in all cases, for our open source code).
      - CERN IT had recommended using GitHub in this case; to use CERN
        resources the policy is users have to register properly.

## Activity and Working Group Updates

### Data Analysis
  - Meeting last week, JLab summary:
      - [<span class="underline">https://indico.cern.ch/event/813207/</span>](https://indico.cern.ch/event/813207/)
  - Meeting right now, analysis level metadata:
      - [<span class="underline">https://indico.cern.ch/event/813208/</span>](https://indico.cern.ch/event/813208/)

### Detector Simulation
  - Meeting yesterday on simulation on accelerators:
      - [<span class="underline">https://indico.cern.ch/event/816484/</span>](https://indico.cern.ch/event/816484/)
      - Two very interesting talks and lots of discussions:
          - Philippe Canal on the Geant Exascale Pilot Project.
          - Zhihua Dong on the ATLAS FastCaloSim on GPUs Project.
      - Perhaps we should consider a follow up session on the same
        topic in the future as we missed ALICE and LHCb this time.
  - Meeting in June:
      - [<span class="underline">https://indico.cern.ch/event/816485/</span>](https://indico.cern.ch/event/816485/)
      - Please send us suggestions for talks and speakers\!

### Reconstruction and Software Triggers
  - ATLAS/CMS cross-talks:
      - 22nd May, 4pm.
      - [<span class="underline">https://indico.cern.ch/event/815233/</span>](https://indico.cern.ch/event/815233/)
      - Speakers confirmed: Jiri Masik (ATLAS), Silvio Donato (CMS)
  - Plan to have meeting on 5th June:
      - Topic: Algorithms and data structures to efficiently exploit
        many-core architectures - one of the topics described in CWP.
      - Two contributions from LHCb are confirmed.

### Event Generators
  - Next meeting today,
    [<span class="underline">https://indico.cern.ch/event/813620/</span>](https://indico.cern.ch/event/813620/).
  - Following up on ATLAS/CMS comparison as discussed at the workshop.
  - CHEP abstract planned.
  - Will follow up on GPUs in a later meeting.

### Packaging
  - Next meeting 29 May:
      - [<span class="underline">https://indico.cern.ch/event/819329/</span>](https://indico.cern.ch/event/819329/)
      - Let Graeme and Ben know of topics (FNAL Spack MVP and
        Fireworks on Conda planned).
      - CHEP abstract planned.

### Frameworks
  - [<span class="underline">Mandate for this
    group</span>](https://docs.google.com/document/d/157TQqQsLsTns-p_GTSZGReyNsl3-kKw2mQ9ZCwm3Hyk/edit?usp=sharing)
    has been drafted.
      - We now invite comments on that.
      - And we would like to receive nominations for convenors.
          - Send to HSF Coordination or to Graeme and Liz directly.

## Workshops

### Pre-CHEP (2-3 November)
  - Short meeting this week. Everyone seems to be happy with the idea
    of an analysis focused workshop.
      - Covering facilities to code and analysis interfaces.
  - Next meeting this month, include the DAWG and DOMA convenors and
    get a draft agenda together.

## AOB
  - Simulation developers asked for an HSF convened meeting to present
    the results of the GeantV prototype and to discuss plans for the
    future.
      - Date now settled, 15th October, 14-18h (avoid ATLAS Week\!).
  - CERN have added some Nvidia GPUs to lxbatch. If you want to use
    them the add “request\_GPUs = 1” to your Condor submit script.
  - RSE 2018 Conference,
    [<span class="underline">https://rse.ac.uk/conf2019/</span>](https://rse.ac.uk/conf2019/).
    - We did not resubmit the abstracts from last year (deadline was May 7), it would
    still be good if someone attends, also to understand why our previous
    submissions had been rejected. We know that Stefan Roiser did
    submit an abstract on a software institute.
