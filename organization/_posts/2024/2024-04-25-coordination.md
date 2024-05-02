---
tags: HSF, Minutes
lang: en-gb
description: HSF Meeting Notes
---

# HSF Coordination Meeting #268, 25 April 2024

---

*This notebook is used to record the minutes of the HSF Coordination meetings. These are archived after each meeting onto the [HSF Website](https://hepsoftwarefoundation.org).*

## Tips

- If you find you cannot edit these notes please login with your GitHub account!

- If you are adding a URL, please use `<` and `>` to make it an active link, as in `<https://daringfireball.net/projects/markdown/syntax#autolink>`
    - Without the <>s the link is not active in Jekyll, even if it is in CodiMD
- Please use `-` to indicate lists in this file (we try to avoid mixing `-` and `*` in the same file - it's markdown lint!)
- Please use the Zoom "raise hand" if you'd like to make a comment in the meeting

## Attending

Present/Contributing: Stefan Roiser, Graeme Stewart, Michel Jouvin, Jamie Gooding, Tommaso Lari, Krzysztof Genser, Reiner Hauser, Claire Antel, Liz Sexton-Kennedy, Eduardo Rodrigues, Joe Osborn, Alexander Moreno, Mark Neubauer

Apologies/Contributing: Benedikt Hegner, Pere Mato

## News, general matters, announcements

### ePIC Software & Computing Meeting at CERN

This week has been [ePIC Software & Computing](https://indico.cern.ch/event/1343984/) at CERN.

Tomorrow (Friday 26 April) there is a [joint HSF/ePIC session](https://indico.cern.ch/event/1343984/timetable/#20240426.detailed) with talks on HSF and Common Software Projects (Benedikt Hegner) and on Key4hep (André Sailer). All welcome to join!

### HSF Joint Workshop with WLCG

[Workshop timetable](https://indico.cern.ch/event/1369601/timetable/#all.detailed) is now finalised.

Registration closes tomorrow (26 April), so if you want to attend in person, last chance!

We have a great selection of software talks and a dedicated session on training activities.

In plenary we shall cover:

- HSF Retrospective and Future (Graeme)
- HSF Organisation and Activities (Paul)
- HSF Software Projects (TBD)

Then there will be a 10' wrap-up on the last day.

There will also be a dedicated session on Analysis Facilities.

### Google Summer of Code 2024

Deadline for evaluation input was last week.

News on slots?

### HSF Evolution

The Core Coordination Team have been meeting fairly regularly to discuss how we evolve the HSF to be most effective.

We have discussed a number of points:

- Updated [HSF Motivation](https://docs.google.com/document/d/1wRrMAOzF2hchgHrRjvWyMTET8tbGwSHYquQNyVw7h9k/edit?usp=sharing)
    - Evolving from the era of the CWP
    - Keeping the same general principles of working together for common solutions to problems
- A newly defined [Core Coordination Team Mandate](https://docs.google.com/document/d/1SxLPq1gUHBCnCcIhrVy7QuqysGshyFAxeUrZlh80NX4/edit?usp=sharing)
    - Give this group a more formal structure (regular meetings and an elected chair)
    - Define better the roles played by the members, with specific responsibilities
- A new [Advisory Group](https://docs.google.com/document/d/1L62pleuuME6K9WLl5T4KQaImPP_Qpc8HSym-XBNTKv8/edit?usp=sharing), with HSF *Engaged Communities* (experiments, service providers like WLCG), that provide their input and advice on HSF strategy
    - This group only give *advice*
    - It should have an elected chair from the ECs
    - Meets ~1/year
- The relationship with software projects; final document still in preparation, but a number of promising lines identified
    - HSF endorsment/recognision for community software projects
        - This is a "badge" system, with different levels
        - Projects need to be evaluated
        - No control is ceded to the HSF - the project is owned and contolled by its developers
        - This is just as relevant for small projects and tools as large ones (maybe even more so!)
    - HSF Projects
        - Where a project has been developed in closer association with the HSF and had direct input
        - e.g., [prmon](https://github.com/HSF/prmon), [Phoenix](https://github.com/HSF/phoenix), [Harvester](https://github.com/HSF/harvester)
    - HSF reference implementations
        - Where a common problem exists the HSF can setup a group of experts to study it
        - Should result in a whitepaper on solutions
        - Then followed by a reference implementation
    - HSF "Reviews"
        - For projects wishing to have a group of experts from the community review their implementation or requirements
        - e.g., Detector simulation on GPUs, DUNE framework requirements
    - Effort/resources from the HSF
        - Still considering this and how it could work, modelling on, e.g., [NumFOCUS](https://numfocus.org), which gets foundation funding and industry support
        - Limited to auxilliary support, e.g., for workshops or travel
            - Paying people a salary is extremely complicvated
        - Would we stand a chance of getting foundation type funding?
            - This will require leg-work, but there is some chance that it would be successful if spun in the right way

## Working Group Updates

### General Standing Reminders

#### Website banners

We have the ability to put event banners on the HSF website. All it requires is a markdown file with the event data. See, e.g., files [here](https://github.com/HSF/hsf.github.io/tree/main/announcements/_posts/2023).

#### Meetings

Please try and book meetings in Indico at least 2 weeks in advance!

That way they go into the calendar early and they will be included in the weekly email announcement that goes to HSF Forum.

### Data Analysis

- Planning a DAWG meeting for talk on CMS Combine (in touch with Nick Wardle) + update on HS3 (in touch with Carsten Burgard), nominally 10th June

### PyHEP

- [PyHEP 2024](https://indico.cern.ch/event/1384010/) (1–4 July, 2024) registration and call for abstracts is open now
- [PyHEP.dev 2024](https://indico.cern.ch/e/PyHEP2024.dev) (26–30 August, 2024) organisation continues 

### Detector Simulation

- We shall hold a session on "Machine Learning for Detector Simulation" <https://indico.cern.ch/event/1408850/> on May 6th and the speaker will be Kevin Pedro

### Software Training

- Next Training Events:
    - May 20-21, Software Carpentry
    - Jun 3, Scikit-hep/ROOT
    - Sept 27-29, Julia (in person at CERN)
- Don't forget the training session at the WLCG-HSF workshop
- The pre-CHEP workshop will be an [HSF Training Community Event](https://indico.cern.ch/e/hsftraining2024)

#### C++ Course and Hands-on Training

- An advanced C++ course will be held in fall, exact dates TBD

### Reconstruction and Software Trigger

Organising a topical meeting on "4D tracking @ Belle II": 
- Confirmed date: 8th May
- Agenda: <https://indico.cern.ch/event/1399441/>
- Not announced in mailing list yet.
- Two talks: "Hit Timing Determination in Belle2 SVD" (Luigi Corona) & "SVD Timing in Tracking at Belle2" (Thomas Lueck)
- Thanks to Giulia for providing the speakers and Joe for following up.
- Discussion with some others about an additional 4D tracking meeting to follow the Belle2 focused discussion 

To get WG google-group white listed by CERN IT (_before_ sending a first email), it helped to cc Graeme in ticket who linked past tickets and attached [screenshots](https://cernbox.cern.ch/s/qaPY2M9rWlfXrWm) 

>It's the xorlabs filter that does this, see tickets [INC3759294 ](https://cern.service-now.com/service-portal?id=ticket&table=incident&n=INC3759294)and [INC3761021](https://cern.service-now.com/service-portal?id=ticket&table=incident&n=INC3761021). I pasted a few screenshots of how this happened for other HSF lists that are now unblocked.
 

### JuliaHEP

- Topical group meetings:
    - May and June
- JuliaHEP 2024 Workshop at CERN (end of September - beginning of October):
    - JuliaHEP Training before the workshop
    - <https://indico.cern.ch/e/juliahep2024>

### Tools and Packaging

- We plan to have a topical meeting on experience with using SPACK in existing experiments
    - CMS, LHCb, FNAL(Patrick, TBC)
    - No date set yet, we would prefer to have a single meeting rather than spread it out over multiple ones

## Other Interest and Activity Areas

### Analysis Facilities

[Session at the WLCG-HSF workshop](https://indico.cern.ch/event/1369601/timetable/#20240516) to look forward to

### Compute and Accelerator Forum

[Indico agenda](https://indico.cern.ch/category/12741/)

- 8 May: GPU infrastructure and tools being developed; CERN infrastructure update
- 29 May: NVidia Update
- 12 June: AMD GPU roadmap

### Software and Computing Roundtable


### Event generators

We should have a BoF for the generator people at the workshop, because quite a few are coming.

---

## AOB

### OSCARS Open Call

The [OSCARS](https://oscars-project.eu) call is open until 14 May (<https://oscars-project.eu/open-calls>).

### Other workshops

### Next Meetings

The next meeting will be on [9 May](https://indico.cern.ch/event/1355747/).

Reminder: please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing one of the 2024 meetings.

**We now have a [guide](https://hepsoftwarefoundation.org/organization/running-meetings.html) for running the meeting!**

