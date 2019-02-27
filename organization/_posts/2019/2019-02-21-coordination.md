---
title: "HSF Weekly Meeting #159, 21 February, 2019"
layout: meetings
---

# {{page.title}}

*Present/Contributors*: Liz Sexton-Kennedy, Pere Mato, Daniel Elvira,
Josh McFayden, Jim Amundson, Michel Jouvin, David Lange, Dario Menasce

## News, general matters

-   Many people absent this week from CERN due to school holidays.

## Google Summer of Code 2019

-   The answer from Google about HSF being validated as an umbrella this
    year will be known next week.
    -   HSF has ~50 project proposals: more than last year. But the
        total number of proposals is similar (proposals are grouped by
        projects).
    -   Total number of mentors ~100: lots of interest in the community
        means big success.

## HSF/WLCG/OSG Workshop News and Planning

-   [<span
    class="underline">Indico</span>](https://indico.cern.ch/event/759388/) -
    registration is still open.
    -   210 people registered.

-   There is a Google Sheet linked from the [<span
    class="underline">main
    page</span>](https://indico.cern.ch/event/759388/) to help
    coordinate car sharing from Dulles (you take your own
    responsibility for this!).
    -   If you are arriving/travelling from another airport you can also
        use that spreadsheet (just make it clear which airport you
        will be at).

### Session Planning (see [<span class="underline">block timetable</span>](https://indico.cern.ch/event/759388/timetable/#all))

-   Reminder: David Lange, Michel Jouvin and Graeme Stewart organising
    for HSF.

-   General Sessions:
    -   Plenary sessions all fixed now.

-   HSF Sessions:
    -   Distributed analysis and Simulation still have to fill the
        detailed timetable for their sessions (Wednesday/Thursday)
    -   Software on Accelerators (2 slots).
        -   Graeme, Michel, David L are convening
            -   Confirmed all talks and discussion tome.
    -   Reconstruction and real-time anlysis: one talk proposed from
        Icecube not yet added
    -   Training: session almost filled in
    -   One spillover session still available but no request for it yet
    -   Rooms:
        -   Thursday we will need to make some use of the auditorium,
            which has not so great Vidyo.
            -   Amber says that they are working on setting this up and
                we’ll do a ‘sound check’ soon, so hopefully ok.
    -   For planning other HSF Parallel Sessions, see WG activity
        reports below.

## Activity and Working Group Updates

General points:

-   Reminder to make sure your WG page has
    -   Brief description of the interests of the group
    -   Information on how to join the group’s mailing list
    -   Information on how to contact the convenors (convenor list or
        individual emails)
    -   A link to the group’s Indico category

### Event Generators

-   Had first closed [<span
    class="underline">meeting</span>](https://indico.cern.ch/event/799280/)
    ([<span
    class="underline">minutes</span>](https://docs.google.com/document/d/1a5cQKQm9O_SFtOpmjbLlOLT4xxotVLf67HocnpQImtw/edit))
    between the conveners
    -   Essentially a roundtable on how best to follow up from the
        November WS and what needs to be done to finish the
        proceedings.

-   Now will have regular open meetings every two-weeks, first is [<span
    class="underline">28th Feb
    16h00</span>](https://indico.cern.ch/event/799316/). Will announce
    to the mailing list as soon as contributions are confirmed.

-   The TBC agenda items:
    -   Understanding ATLAS & CMS resources computing - i.e. getting to
        the bottom of inconsistencies discussed at the workshop,
        mostly in CMS’s reported numbers.
    -   Discussion on ATLAS-CMS sample sharing - starting with SUSY
        signal samples where some steps are already in place to move
        in this direction. We will see how we can best support this
        effort.

-   Updates to the proceedings:
    -   Clarifications on resources accounting (as mentioned above).
    -   New work from Stefan getting Sherpa to run on Haswell and KNL,
        comparing their performance.
        -   Could be useful to get this kind of ported code into the
            benchmarking suite.
        -   Andrea will champion this, he sees this as an interesting
            contribution to the WLCG performance/ cost model and
            metric’s group (they will meet at HOW on Wed. morning).

### Licensing

-   Marco and Graeme to meet with CERN KT next week.

-   No news from FastJet authors.

-   CMS CB approved moving to Apache 2 in the same way as ATLAS (we, the
    field may need the LLVM exception since we like LLVM at the binary
    level depend on GNU licensed software, the foundation claims that
    GNU is not incompatible with Apache2)

-   Both the CERN and FNAL KT people signed off on licensing Apache2 for
    their contributions to LLVM

-   Pere was asked if FCC code should be made closed but this is being
    proposed for high level software, the concern could be revealing
    detector designs to competitors

### Packaging

-   Next meeting on 27 February.

## AOB

-   Graeme should be back next week to convene the meeting
