---
title: "HSF Weekly Meeting #189, 2 July 2020"
layout: meetings
---

# {{page.title}}

Present/Contributors: Graeme Stewart, Liz Sexton-Kennedy, Andrea Valassi, Efe Yazgan, Kyle Knoepfel, Witek Pokorski, Eduardo Rodrigues, Michel Jouvin, Andrea Rizzi, Horst Severini, Teng Jian Khoo, Stefan Roiser, Caterina Doglioni (for a bit), Serhan Mete, Benedikt Hegner, David Lange, Gloria Corti, Kilian Lieret, Pere Mato, Sam Meehan, Sudhir Malik, Daniel Elvira

Apologies: Agnieszka Dziurda 

## News, general matters

### Technical Note on Best Practices for HSF Projects

Current Draft:

- <https://github.com/HSF/documents/blob/master/HSF-TN/draft-2016-PROJ/draft-HSF-TN-2016-PROJ.md>

No additional comments, so this is approved.

### IRIS-HEP Blueprint Meeting on *Sustainable Software in HEP*

This meeting is now set for July 22: <https://indico.cern.ch/event/930127/>.

### ESCAPE Workshop on Open Source Software Lifecycles (July 23, 24 + 27, 28)

<https://indico.in2p3.fr/event/21698/overview> - we were invited to give a 20' talk on Friday 24 (CERN/HSF approach to software/code or workflow optimisation), any volunteers? Contact Graeme for details.

### LHCC Review of HL-LHC Software and Computing

We received a first draft of the report from the panel. Largely it was very positive (which is great for the HSF as this is the first time that we have really been reviewed). There was a feeling that some important points have been missed, which were communicated back to Amber.

### New Convenor for Data Analysis WG

Andrea Rizzi has been nominated CMS deputy physics coordinator. *Congratulations!* It means Andrea will not be able to stay as an Analysis WG convenor. Need to start the process for his replacement, to start Sept. 1st. Proposal to have the appointment run until end of 2021.


### Alpaka Training

- Ongoing this week as a [virtual event](https://indico.cern.ch/event/912156/)
- 25 - 30 people attending so far every day
- Sessions are recorded and will be made available either directly on indico or linked from there.
- No GPUs made available, all the examples also run on CPU (OpenMP backend)

Discuss with them the format of the training material and possible conversion to Carpentry style (Stefan)

## Website

### Review process on PRs

Policy changed: `Web_Site_Managers` can no longer push directly to master; need at least 1 approval on a PR.

BUT: Few people comment on PRs (even when asked), which is slowing things down a lot.

There is a `Web_Site_Managers` group but it seems a bit random...

Possible solutions:
- Volunteers to help with reviews?
- Allow active competent developers to self-merge if needed?
- Technical: Add Jekyll page build to Travis CI; make build outcome independent of unreliable link checker; make successful Travis build a sufficient condition to allow merge

Agreed that we want to keep things running smoothly for people making useful contributions
* If PRs have been checked by the submitter then self-merge should be allowed
* We insist that the `master` branch remains protected
* We try to improve the CI and get the tested website available for inspection

Benedikt volunteered to take a look at these issues and implement some solutions

### Profiles - 'floating heads'

* Training group has now a [community page](https://hepsoftwarefoundation.org/training/community) that acknowledges contributions from the community; [additional page](https://hepsoftwarefoundation.org/training/educators.html) to thank volunteers for training events
* The code can be easily generalized to allow for profiles and community pages for other working groups
* Adding profiles of the convenors to the WGs makes us look more active and approachable (probably important for all groups)
* Community pages can help to foster and encourage community contributions (indispensable for training, but perhaps also important for other groups)

The meeting was positive about this for WG pages, so we try to implement that for all WGs


## Working Group Updates

### Data Analysis

Announced the next meeting for [July 15th](https://indico.cern.ch/event/932570/). The topic is chiefly B-physics, with some input also on "10%" analyses (i.e. those not fitting the central processing model because of special reconstruction and data handling).

Some topics we'd like to arrange events on:
* Analysis languages/declarative analysis -- had ambitions of face-to-face workshop, but not realistic now -- decide if want an online meeting to avoid waiting too long
* Metadata -- key concern without clear stakeholders. Need to clarify exactly what the biggest issues are and prioritise
* More on "10%" analyses and HL-LHC analysis model


### Detector Simulation

Held the 3rd topical meeting devoted to use of GPUs on the 24th of June. Included the presentation by the GATE project and 3 lightning talks. Overall, a very interesting set of talks. The general picture one can see is that in order to gain reasonable speedups we need to move substantial (almost all) parts of the computations to the GPU (otherwise the overheads kill the speedup). On the other hand, moving general transport code seems to be very difficult, so one needs to focus on specific problems like optical photos, low energy neutrons, EM shower, etc, complex enough to gain from the use of GPUs but in the same time simple enough to be 'portable' to the device.


### Reconstruction and Software Triggers

Organized the Allen meeting + attended a number of seminars and workshops about GPU in trigger and reconstruction.
Not many news apart from that for the time being, no meetings in July but will resume in August/September. 

### PyHEP
[PyHEP 2020 workshop](https://indico.cern.ch/e/PyHEP2020) agenda finalised and online - a very interesting set of presentations!
- Two keynote presentations scheduled, i.e. one for each of the 2 time zones of the workshop.
- Registration has been extended to the end of this week. We have 870 participants!
- We still aim to release a pre-workshop questionaire as usually done.

- Good advertising on much more specific lists has been successful.
- Will make FNAL a publicised co-sponsor (for specific Zoom videoconferencing set-up).

### Software Tools and Packaging

As advertised before, a new tag of [HSF/prmon](https://github.com/HSF/prmon) is imminent. Among many other improvements, it'll be the first version that supports NVidia GPU monitoring.


### Software Training

* Expanding our webpage, for example [how to host a training workshop](https://hepsoftwarefoundation.org/training/howto-event.html), trying to make the process of creating new workshops and new training material look less "magical" in order to encourage new people joining in
* **[July 27-30]** Preparations for Docker training underway [indico](https://indico.cern.ch/event/934651/) (follow up of very successful virtual pipelines training [recently](https://indico.cern.ch/event/904759/))
* **[August]** Emery Nigibira (no engagement before, but young postdoc in France) wants to be the lead of next Virtual Pipelines training.  Will reuse the same material (low time investment).
* **[August]** Plan to develop REANA training with Tibor Simko and company.
* **[September]** GPU+ML development underway for Manchester/Lancaster folks
    * Comments on ML training? - [Link to Doc (Please comment!)](https://docs.google.com/document/d/1BZEKnj1D8QVIByr0enHE6fxSBkkd8bGDvUQHukVIz1w/edit)

### Event generators

Will probably have a meeting next Thursday.

### Frameworks

At yesterday's WG meeting, Ben Wynne from ATLAS presented details on the Athena multithreading scheduler.  The meeting was attended by ~20 individuals; there was good discussion.

Still planning on a presentation from LHCb's Allen framework, possibly as early as next week.

## Other Interest and Activity Areas

### Differentiable Computing

There's a PR to setup the activity from Nathan, to be reviewed.

### Licensing

Graeme was contacted by FASER to ask about licensing and passed on the HSF's advice. (CERN experiment, so relatively east case, following the LHC Experiment models,)

*Very positive that we get these spontaneous contacts.*

---

## Workshops

Reminder that the proposed September workshop in Lund is again postponed. Next possible event is another *virtual* workshop in November.

## AOB


### Indico -> HSF Calendar Sync

Stefan has deployed some scripts that manage the synchronisation of the HSF Indico category with the HSF Community Calendar (thank you!). This is now working and deployed.
 
So any (public) events created in Indico will generate an entry then created in the HSF Calendar within 15 minutes (cron job time!).
 
The script is smart: if you update or cancel a meeting it will change or disappear accordingly.
 
This removes an extremely annoying manual step to get things into the HSF calendar. However, do be aware that anything created in Indico it will appear in the calendar more publicly than if it was just lurking. (You can set the visibility of events in Indico on calendar feeds though.)

- Scripts at <https://github.com/HSF/merge2gcal> 

### Next Meeting

- Next regular meeeting slot is 16 July
