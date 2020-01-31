---
title: "HSF Weekly Meeting #178, 23 January, 2019"
layout: meetings
---

# {{page.title}} - Lund Workshop Planning Meeting
Present: Graeme Stewart, Pere Mato, Agnieszka Dziurda, Philippe Canal,
Sam Meehan, Stefan Roiser, TJ Khoo, Andrea Valassi, Serhan Mete, Witek
Pokorski, Paul Laycock, Mason Proffitt, Ben Morgan, Markus Schulz, Liz
Sexton-Kennedy, David Lange, Josh McFayden, Kyle Knoepfel, Mark
Neubauer, Efe Yazgan, Daniel Elvira, Caterina Doglioni, Chris Jones

Organising team for HSF are: Graeme, Heather, David and Michel - please
get in touch with any suggestions you have.

# Plenary
  - Opening session on Monday afternoon and closing session on Friday
    will be in plenary
  - For Monday we foresee some overview talks to set the scene
      - We have specifically reached out to some non-HEP communities,
        e.g. ESS, Dark Matter, Astroparticle, ESCAPE
      - Good time to give an HSF review talk, for new people to the
        software and computing area
      - Would it be useful to have some cross-cutting technology
        items, e.g. compute accelerators or networking…?
  - Our WLCG colleagues have mooted a plenary session on “portability
    and sustainability of workflows”. Maybe 0.5 days. Proposed to
    cover aspects around 1) software/infrastructure sustainability;
    and 2) the process for supporting “new” architectures (be it HPC
    or otherwise) on the grid. Both potentially broad areas. Could eat
    0.5 days from the parallel session blocks.
      - Ben - could overlap with software and tools area (packaging)?
      - Liz - maybe less overlap? Is Geant4 suffering from “the
        tragedy of the commons”? Everyone wants it, but wants others
        to pay for it… HSF was created to address this
          - Geant is a priority, but we lack a coherent voice
          - Storage technologies are evolving
      - Andrea - suggest more plenary? That’s the point of the joint
        workshop
          - Plenary talk from *each WG* to increase awareness
              - Concern this would be too much like a general
                round-table of status reports without much discussion?
              - Fold a little piece from each WG into an HSF overview?
          - HL-LHC review “summary” (this was foreseen)
      - Paul - likes the idea of crossover talks, following the themes
        above
      - Stefan - cross cutting topics could be things like
        vectorisation on the grid
          - Heterogeneous resources… (and HPCs) - roadmap to GPU
            workloads?
              - How do you manage them? What software do you run in
                them?
      - Andrea: definitely HPCs could be an interesting topic for a
        cross-over session, with both computing and software people.
        As an example, we had HPC meetings with computing people
        mainly discussing computing integration issues (storage,
        workload, network, O/S…), while those specific issues like
        Summit have mainly GPU computing, and we essentially have no
        GPU workloads ready to run in production at that scale. It
        would be useful for instance from the reconstruction/trigger
        WG to know how much of their GPU work is online farm specific,
        and how much can be exploited on HPCs.

# Parallel
  - Tuesday, Wednesday and Thursday will probably (all) be parallel
    HSF
      - We could have 2 items ongoing (there are 3 rooms in total),
        but will need negotiations with our computing colleagues
  - The DOMA/Analysis workshop pre-CHEP was a success, with the
    interactive sessions appreciated
  - Should we try to do something along the same lines here?
  - e.g. Reconstruction and Simulation are the other major resource
    impacting areas
      - This would mean dedicating a day to each of these
      - How best to get everyone involved in discussions and have
        useful outcomes?
          - New ideas
          - R&D
          - Shared projects
      - The large room is amenable to splitting into smaller groups
  - If we do this then only one more (or just 0.5) day left (unless
    not using Monday morning is reconsidered)
      - That means we cannot cover all topics\!
  - Ideas and thoughts for other WGs:
      - Generators is a centre of expertise in Lund, can we take
        advantage of that and organise something significant, building
        on the Nov 2018 workshop
      - Software Tools and Packaging is an active group, with
        widespread impact, so a session makes sense
      - Frameworks is a new group, so a first session in the workshop
        will help bootstrap and define directions
      - Training - could have a session, but what would need discussed
        in this forum that would drive outcomes?
      - Analysis had a session in Adelaide and we felt the next event
        needed to be at CERN to get the coal-face analysts
      - PyHEP organised the UK workshop and are busy with the SciPy
        2020 event
      - \[Caterina\] Pro domo mea, literally: I have started a “local”
        group called REALTIME, including people from other faculties
        (psychology/law/astronomy/engineering), who are interested in
        real-time data acquisition / analysis. Info in English here:
        [<span class="underline">https://realtime.blogg.lu.se/hej-varlden/</span>](https://realtime.blogg.lu.se/hej-varlden/)
        I talked to them on Monday and they were keen for a mingle,
        but we could also do something totally out there and have a
        trigger&reco discussion session that includes them (not sure
        it’d be of program-wide interest though).
  - If a WG does not have a dedicated session, we could have WG
    reports that cover the main activities and directions (as full
    plenary or an HSF “summary” session)

### Working Group Thoughts and Feedback
  - Assume that we’re looking at 4 sessions in a whole day, each
    session being \~90 minutes long.
  - Let us know how many sessions your group would use.
      - Or if you’d like an overview talk instead
  - Do you want to have some group interaction during your session
    (which was really a success in Adelaide); this helps a lot getting
    everyone discussing and can be very fruitful.
      - Bear in mind this needs to have enough time dedicated to it.

#### Reconstruction and Software Triggers
See above for an interdisciplinary thought from Caterina. *copied
from above*:
  - \[Caterina\] Pro domo mea, literally: I have started a “local”
    group called REALTIME, including people from other faculties
    (psychology/law/astronomy/engineering), who are interested in
    real-time data acquisition / analysis. Info in English here:
    [<span class="underline">https://realtime.blogg.lu.se/hej-varlden/</span>](https://realtime.blogg.lu.se/hej-varlden/)
    I talked to them on Monday and they were keen for a mingle, but we
    could also do something totally out there and have a trigger\&reco
    discussion session that includes them (not sure it’d be of
    program-wide interest though).
  - Graeme - Better not to have this as lunch, which would limit
    participation, but really get input from them in \~1-2 session
    slot (tools, licensing are topics in which we have expertise)
  - Need to have a chat among ourselves before deciding, but it could be a
    good idea to have a longer topical discussion on accelerators for
    trigger and reconstruction (shared with frameworks?) since we keep
    getting interest from people wanting to give talks and here we could
    have a longer session.
  - One interesting thing would be to have a talk for non-standard
    reconstruction techniques for long lived particles. The issue here is
    that tracking is generally CPU-expensive, and one risks missing those
    signatures at the trigger level because one can’t reconstruct the
    features fast enough. Various grapevines tell me (Caterina) that this is
    a hot topic in both ATLAS and CMS, but I haven’t talked to LHCb/ALICE
    yet.
  - Focus on this for the HEP Reco session, also brings in physics
    analysis people
  - Interesting CMS work (we think) on LLPs

*Accelerator crossover with simulation, generators and frameworks...
identify generic work where possible.*

#### Detector Simulation
We think that one full day of parallel session on simulation is a very
good idea, taking into account how critical simulation CPU performance
and physics precision is becoming. We would probably like to have 4
different sessions along the general axis of improvements/modernization
of Geant4, fast simulation and new hardware technologies (accelerators,
HPC, etc). Physics precision is also a very important topic that should
not be ignored, but this should in principle be covered by the LPCC
workshop that we are planning to have in the second half of 2020.
We would be very pleased to have more Geant4 community involved. We
would also be interested to hear about successful attempts of porting
simulation software to accelerators from other communities (outside
HEP).

#### Data Analysis
Topics for the start of year are Analysis languages and Analysis meets
DOMA, our first WG meeting is tomorrow :)
Cross-over topics in other WG parallels might be of interest, seeing as
we needn’t have a dedicated session:
  - Analysis languages crossover with frameworks?
  - Another crossover with frameworks that came out of the Adelaide
    workshop was how to integrate industry standard ML toolkits with
    frameworks
  - Analysis meets DOMA would make use of WLCG but we hogged the
    Adelaide agenda.
  - Real-time analysis and the other Reco topics esp if physics reps
    will come
  - Training would also be natural.
  - ML/GPU +1

#### Frameworks
Not certain who will be at Lund yet from FNAL.
Cross cutting topics would be really interesting - scheduling
accelerator jobs, portability issues. How to make use of an HPC as an
application.
Exploring different frameworks and examining complications... once
finished

#### PyHEP
  - We do not request a parallel session.
  - We kindly request a plenary report on WG activities, if possible
    within the time budget.

#### Tools and Packaging
Serhan : Will probably be able to discuss tomorrow. Last two HOW
workshops, we had 1h30min parallel sessions with approximately 50% talk
- 50% discussions. Overall, I think this is a balanced approach. We
might have three or so talks (15’ + 15’). The usual suspects:
  - Build systems + packaging + software distribution
  - Profiling/monitoring tools (maybe focus a bit on accelerators)
  - Static analyzers (linters etc.)
  - IDEs (and perhaps integrating some of the above tools therein) -
    cross over with training\!

#### Training
Sam M. : I’m sorry that I could not attend the meeting \[ref.
Coordination meeting 16 Jan\]. I do think that having a session would be
good and I think that if we want to consider outcomes, then having the
critical mass of people to brainstorm what types of bootcamps we need
would be helpful. We can then discuss this with the experience of the
last year in mind \[specifically how we held the workshops\] and that
would provide the concrete list of events that we need to plan in the
coming year - spanning \~July 2020 - July 2021.
Caterina: another “crazy host” idea: would you be willing (and would
there be interest) to organize a mini-bootcamp before/after the
workshop? Students may be encouraged to fly on Sunday night and in the
morning we have the rooms. In Lund we have huge interest from all
faculties on our Jupyter course and if we do something generic we can
“expand our horizons”. → Caterina will follow up with Sam towards the
end of next week.

#### Generators

We have a generator meeting at 4pm after this one, where we will also discuss the LUnd workshop more in detail.
Lund is sort of the ‘home’ of MC generators and there are people there
working in Pythia, MadGraph, Herwig, possibly more. It would certainly
be nice to organise one parallel session to meet and engage with some of
those experts, who are not normally involved in our WG activities. We
have not yet made contacts but will do soon. So in principle we request
one parallel slot (90 minutes?).
We could have a plenary talk if people find this useful \[Andrea more
generally suggested that each WG gives one, but some people feel
otherwise\]

### AOB
We are asked for a letter of collaboration for an AI Institute proposal
going to the HSF, “AI Institute: Community Laboratory for AI Research at
the Intersection with Physics (CLARIPHY)” (from Pete Elmer). The HSF’s
collaboration would be in training and workshops:
[<span class="underline">https://docs.google.com/document/d/13YHqtL3UI0QV5KQ8fUQ0ab0jiDzs7Nw089lbzjW-rS4/edit?usp=sharing</span>](https://docs.google.com/document/d/13YHqtL3UI0QV5KQ8fUQ0ab0jiDzs7Nw089lbzjW-rS4/edit?usp=sharing)
Can we approve this? Comments until tomorrow morning CERN time as the
[<span class="underline">proposal</span>](https://www.nsf.gov/pubs/2020/nsf20503/nsf20503.htm)
deadline is very close.
*We would like a \~1 page summary so that we can check we approve the
idea.*
Mark: there will likely be other asks for this call. Graeme: we can sign
off without a meeting as long as the letter and project description are
circulated.
