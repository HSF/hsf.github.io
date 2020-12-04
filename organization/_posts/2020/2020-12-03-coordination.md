---
title: "HSF Weekly Meeting #197-198, 19 November 2020 and 3 December 2020"
layout: plain
---

*Note:* Due to the [HSF Workshop](https://indico.cern.ch/event/941278/) some notes were taken on 19 November, with no meeting held. These were carried over for discussion on 3 December.

Present: Graeme Stewart, Teng Jian Khoo, Witek Pokorski, Kyle Knoepfel, Stefan Roiser, Serhan Mete, Efe Yazgan, Paul Laycock, Ben Morgan, Michel Jouvin, Allie Hall, David Lange, Pere Mato, Attila Krasznahorkay, Andrea Valassi, Gloria Corti, Torre Wenaus, Benedikt Hegner, Kilian Lieret, Liz Sexton-Kennedy, Markusw (?), Stefano Piano, Sudhir Malik, Daniel Elvira

Apologies: Eduardo Rodrigues

## News, general matters, announcements

### LHCC Presentation

Graeme presented the Software Update talk to the LHCC referees on Tuesday 17 November - the final version of the slides is attached [to this agenda](https://indico.cern.ch/event/964169/). *Thanks to those who provided input.*

Discussion focused on human resources for key projects and helping to broaden their developer base to other institutes to manage HR ups and downs. There was a discussion of GPU projects, what can be learned when they are focused on one experiment only (we still think quite a lot). The C++ course and the Compute Accelerator Forum were mentioned a few times and are well received. The LHCC also gave positive feedback on the new Software Liaison role.

The referees official remarks will come soon in the LHCC minutes.

### HL-LHC Software and Computing Review

We have a draft charge for the next review, focusing on common software. The review will take place 8-11 November 2021, hopefully in person at CERN. *Projects to be reviewed need to be finalised in discussion with the LHC experiments* (the review is of what they need). Project documents to be delivered by 1 October 2021.

### Working Group Convenors for 2021

Reminder, we have made a call for WG Convenor nominations open until **4 December** (so you still have a day to nominate):

> Dear HSF
> As we approach the end of 2020 we’d like to extend our thanks to all of the convenors of our HSF working groups who drive so much of the activity that we do. Some of our working group convenors will step down at the end of this year, so particular thanks to them for the work they did, often over several years.
>
> We would now like to call for your nominations for those groups where vacancies are foreseen, which are:
>
> - Detector Simulation
> - Reconstruction and Software Triggers
> - Software Developer Tools and Packaging
> - Training
>
> We are looking for motivated individuals from the community to lead HSF activities in these areas. Self-nominations are very welcome.
> Please send nominations to hsf-wg-search-committee@cern.ch. The search committee consists of Michel Jouvin (IJCLab), Liz Sexton-Kennedy (Fermlab) and Graeme Stewart (CERN).
>
> We would like to receive your nominations by Friday 4 December.
>
> Many thanks in advance
>
> Graeme, Liz and Michel, for HSF Coordination

### 2nd HEP C++ Course and Hands-on Training

As discussed during the last meeting we aim for the 2nd iteration of the C++ course in the week 18 - 22 January 2021. No info on clashes for this week was received. Indico agenda to be put up soon.

Update 2 Dec: The [announcement](https://groups.cern.ch/group/hep-cpp-course-organizers/Lists/Archive/Flat.aspx?RootFolder=%2Fgroup%2Fhep%2Dcpp%2Dcourse%2Dorganizers%2FLists%2FArchive%2F2nd%20HEP%20C%2B%2B%20Course%20and%20Hands%2Don%20tutorial&FolderCTID=0x01200200B8DC60AB96D9D04F95EF586B849E8167) has been sent out to LHC experiment computing coordinators, DUNE/Manchester, CERN EP/SFT + IT, Openlab. Please forward to more HEP communities which may be interested.

Indico agenda page: <https://indico.cern.ch/event/979067/>

**Registration** for 75 places will open on **14 Dec, 9:00 am CET**. Please note for the last event available places ran out quickly. As last time a waiting list will be provided (move to event in case of withdrawal, announcement of future trainings)

We continue to **look for mentors** of the afternoon sessions. Please subscribe at <https://doodle.com/poll/4idhpavi7vepvsqg>. Please also forward to possible candidates.

### Compute Accelerator Forum

[Next meeting (9 Dec, 16:30)](https://indico.cern.ch/event/962112/) will have a seminary from NVidia on their NSight profiling suite.

Meetings for next year are being planned so please contact the organisers with any topics you have: <mailto:compute-accelerator-forum-organizers@cern.ch> (it’s Graeme Stewart, Stefan Roiser, Maria Girone, Ben Morgan and Michael Bussman (from CASUS)).

Note we have settled on a regular slot for the meetings, 16h30 every second Wednesday of the month.

### HSF-WLCG Workshop

Took place 19, 20 + 23, 24 November. General impression was very positive. Rough turnout for HSF software sessions was:

| Session | Attendance |
| :--- | ---: |
| HSF Plenary, Thursday 19 | 100 |
| Event Generators, Friday 20 | 80 |
| Simulation, Monday 23 | 100 |
| Software R&D, Tuesday 24 | 80 |

265 people registered for the event interested in software - the actual turnout is consistent, with a more buffet-style approach to sessions.

Videos from the HSF sessions are uploaded to [Indico](https://indico.cern.ch/event/941278/) and to [YouTube](https://www.youtube.com/playlist?list=PLKZ9c4ONm-Vk-u6aUxJndHKT9qwN6VM1-).

We have a survey open to get feedback on the sessions and the best way to organise future events:

<https://forms.gle/iAAVVetrupRKw27T7>

From the HSF side we should prepare a very short summary of outcomes and points to follow-up on (say 1/2 page per day?).

*This should fall to the session organisers to do, working off the workshop notebook.*

### Invitation for HSF to join Software Round Table Organisation

As a concrete proposal from our discussions with Nuclear Physics colleagues the HSF has been invited to join the organisation of the [Software and Computing Round Table](https://www.jlab.org/software-and-computing-round-table) with JLab and BNL.

*It would seem like a good way to collaborate on an interesting set of meeting topics and build stronger relationships with our colleagues in nuclear physics.*

Meeting was supportive of this initiative.

Graeme (preemptively) attended a planning meeting yesterday and the discussion on topics was very interesting, with a lot of overlap with HSF and HEP. *Also welcome anyone else from HSF who would like to volunteer to be the contact person.*

There is a concrete proposal that if we approve this that there would be an HSF focused meeting in January that could comprise a general HSF introduction and a few working group focus talks.

## Working Group Updates

### Data Analysis

Planning to kick off 2021 with a series of discussions on analysis metadata (LHCC Review hot topic), aiming for 3 fortnightly meetings:

  1. Calibrations, cross-sections and auxiliary info
  2. Bookkeeping processed events
  3. Intersections of the above and/or analysis experience

So far have some candidate speakers from ATLAS/CMS, Paul will tell us about Belle II global tags (probably in 1st theme). Suggestions for speakers from other communities very welcome.

ATLAS has a new group on databases & metadata -- will try to get the coordinators involved. Does (some fraction of) the Frameworks WG want to come along?

- Yes we agreed this was a very good point to explore, given the different views of metadata from these two communities, but that in the then they are very related.

For later in the year, want to follow up on declarative analysis -- flesh out benchmark challenges into more complete analysis situations. HSF to provide a "conventional" implementation for performance comparison?

- We should make sure that ease of use and clarity are prioritised in the solutions. People developing new tools (IRIS-HEP, for example) are definitely interested in this.

### Detector Simulation

Next HSF Detector Simulation working group topical meeting on Wednesday 16th of December at 4pm (CERN time) devoted to the definition of validation strategies for Deep Learning-based fast simulation models as well as the challenges related to the integration of those tools into detailed-simulation frameworks. (Indico entry to come soon!)

We had a short debriefing of the workshop session and it was very positive to have it as Geant4 co-hosted event. One thing we would like to do is to continue fostering including the Geant4 collaboration in HSF.

### Reconstruction and Software Triggers

Would like to have a summary of the on-going Fast-ML Workshop <https://indico.cern.ch/event/924283/>.

### PyHEP

We will be starting topical meetings as of January 2021.

They will be somewhat in the theme of [Python 3 Module of the Week](https://pymotw.com/3/), but with a spirit adapted to our needs, hence rather a "Python Module of the Month", presentations with a focus on libraries relevant to data analysis in Particle Physics.

- First tutorial-like presentation will be on [Numba](https://numba.pydata.org/). Details to follow in due time.

### Software Tools and Packaging

Catch-up on Spack planned.

Talk on `perf` based monitoring 20 Jan. (5pm CERN time):

- Agenda: <https://indico.cern.ch/event/974382/>
- Title: Profiling Tools: `perf`, `strace`, and more
- Speaker: Dr Guilherme Amadio (CERN)

### Software Training

- Training hackathon end of this month (16th-18th)!
  - Currently ~15 registrants
  - Formally in European time zone, but mostly working in parallel groups anyway, so join whenever you're ready (use the google doc or mattermost to express yourself if you miss the kickoff session perhaps -- but we can also discuss in the afternoon session)
  - [indico](https://indico.cern.ch/event/975487/)
  - [google doc with suggestions of topic and async communication](https://docs.google.com/document/d/1M0knOEK0HGHwYuaFCMj3lyKtD9wVgc3ODF0u3MGcGfY/edit?usp=sharing), please edit
  - Will also start a mattermost channel soon

### Event generators

- Paper accepted but still need to make a few changes before publication.

### Frameworks

We will meet next Wednesday, Dec. 9 **at 15:00** for a presentation on _art_'s handling of metadata, including relevant multi-threading considerations.

---

## AOB

### YouTube

We now have a descriptive URL for the HSF YouTube channel as we fulfilled the criteria of 1 month old and 100+ subscribers:

<https://www.youtube.com/c/HEPSoftwareFoundation>

### Next Meeting(s)

- Please check the HSF Calendar to make sure that events for 2021 are listed correctly
  - Mostly this was done - thank you!
  - Only DUNE was missing - Liz was following up
- We have a meeting scheduled for 17 December
- Meetings for next year are booked in Indico, Thursdays 15h CERN time on *odd* weeks
  - First meeting is scheduled for 7 January
- Agreed that we would skip the 17 December meeting and reconvene in January

**We hope that everyone in the HSF has a really great end of year break!**
