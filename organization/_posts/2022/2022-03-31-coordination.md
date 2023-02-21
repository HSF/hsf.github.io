---
title: "HSF Coordination Meeting #226, 31 March 2022"
layout: plain_toc
---

Present/Contributing: Graeme Stewart, Serhan Mete, Michel Jouvin, Josh McFayden, Pere Mato, Efe Yazgan, Krzysztof Genser, Wouter Deconinck, Kyle Knoepfel, Eduardo Rodrigues, Paul Laycock, Nicole Skidmore, Liz Sexton-Kennedy, Andrea Valassi, Stefan Roiser, Andi Salzburger, Michel Hernandez, Pere Mato, Stephan Hageboeck

## News, general matters, announcements

### LHCC

LHCC [minutes](https://cds.cern.ch/record/2803321/) from March 2022 meeting are available.

### Workshops in 2022

#### Analysis Ecosystems Workshop

23-25 May: <https://indico.cern.ch/e/aew2>

**Registration is open!** (limited this to 80 in-person places).

2022-03-31: 50 people have registered, mostly in person

Progress is being made by session conveners on the following topics:

- Analysis Facilities: Oksana Shadura, Nicole Skidmore
- ML tools and differentiable computing workflows: Lukas Heinrich, Nathan Simpson
  - We need to chase this one up!
- “Real-time” online/trigger-level analysis: Giulio Eulisse, Mike Sokoloff
- Analysis User Experience and Declarative Languages: Jonas Rembser, Alex Held
- Analysis on reduced formats or specialist inputs: Allie Hall, +others
- Bookkeeping and systematics handling: TJ Khoo, Paul Laycock

Next organising meeting 7 April with the goal to have a draft agenda ready

- Requires all sessions to have a precise enough idea to make it possible

*Please forward news about the workshop to your community and think about key people to invite.*

#### Detector Simulation on GPU Community Meeting

- HSF Detector Simulation on GPU Community Meeting to be held 3-6 May
  - <https://indico.cern.ch/e/simgpu>
  - There is a sketched agenda now that the organisers are finalising.

### Google Summer of Code / Season of Docs

GSoC evaluation period finishes this weekend, 3 April.

GSoD, proposal has been made and [advertised](https://hepsoftwarefoundation.org/activities/gsdocs.html), combining documentation sub-projects for Clang-REPL, Rivet and Gambit - thanks to David and Andy for doing this.

### Snowmass

### HSF History Paper

[Document](https://docs.google.com/document/d/1y45VSJeUZQnxgk7UMrLpVX4VhWtwYvp1sqz6Hp3dN1g/edit?usp=sharing). Upload to Zenodo is still TODO! Document should first be converted to LaTeX to make it look nice for posterity.

### Talks

Graeme and Alessandra gave talks at the [SWIFT-HEP workshop](https://indico.cern.ch/event/1127798) last week - thanks for comments and improvements.

## Working Group Updates

### Data Analysis

- Final modifications to [Metadata paper](https://arxiv.org/abs/2203.00463) ongoing - will re-circulate to proponents
- Discussing having a meeting on the 12th April focussing on Systematics

### Detector Simulation

- Held a meeting on MARS: <https://indico.cern.ch/event/1107097/>
- Next meeting will be on Fast Calorimeter Simulation Challenge on April 11th
  - <https://indico.cern.ch/event/1140563/>
  We will work to advertise this to all possibly interested communities
- HSF Detector Simulation on GPU Community Meeting (3-6 May) - see above
- Expecting a session on DD4hep towards the end of May

### Reconstruction and Software Trigger

- Second meeting on 4D reconstruction held on 16/03/2022, agenda at <https://indico.cern.ch/event/1128087/>.
- Preparation ongoing on ML in Reconstruction topical meeting (after IPa Workshop, Orsay, Paris), tentatively end of May.
- Discussion on expanding Open Data Detector for calorimetry ongoing (expert meeting in April planned)

### PyHEP

- Next **topical meeting** on "Awkward Array (and 'relatives') Updates". Agenda at <https://indico.cern.ch/event/1140031/>.
- **PyHEP 2022 workshop** will be taking place on the week of September 12th! Event is on the HSF community calendar. Agenda to be out soon and advertised. Do book that week if interested :-)!

### Software Tools and Packaging

- Nothing to report.

### Event Generators

Recent meetings:

- 10th March:     Snowmass Generators Whitepaper
- 24th March:     ATLAS V+jets - was very interesting, lots of discussion!

Future meetings:

- 7th April:     Further Sherpa efficiency improvements by Enrico Bothmann (confirmed)
- 5th May:     Neutrino event generators (confirmed)
- 2 June: Master thesis on chirality flow formalism (TBC)
- 23 June:     EIC/NP Generators usage (TBC)
- 7th July:     Event generation with Julia (confirmed)
- 1st Sept.:     AI/ML-focussed discussion (TBC)

Interesting presentations at Swift-HEP [workshop](https://indico.cern.ch/event/1127798/#21-wp2-event-generators) relating to generators, one half of this (Sherpa) will also be presented at our 7th April meeting.

### Frameworks

- To avoid colliding with the PyHEP topical meeting on 6 April, we have rescheduled our next meeting for 13 April at 15h30.
- After our 4 May meeting, We will be shifting our regular meetings to the last Wednesday of each month.

### Software Training

- Software Carpentry workshop held on 28-30 of March ([link to Indico](https://indico.cern.ch/event/1112526/)).
  - 58 participants registered. ~30 participants attended live.
  - Carpentries instructors covering the basics (Bash, Git, Python)
  - HEP community instructors for ROOT (E. Saavedra, V. Padulano and J. Rembser) and Uproot (J. Pivarski).
  - We will discuss the pre and post surveys and the aftermath in the next HSF Training meeting on Monday.

- Next event is Matplotlib Training ([link to Indico](https://indico.cern.ch/event/1058838/)).
  - This is the first Matplotlib event organized by the HSF Training community. Material preparation is almost done.
    - Pending: surveys, prerequisites.
  - Registration is open. 14 participants registered so far.

## Other Interest and Activity Areas

### Analysis Facilities

- [Kickoff meeting](https://indico.cern.ch/event/1132360/) took place last week
- Up to 67 attendees at the peak (note this was 1500-2000 CET), lots of very good discussion
- First topical meeting scheduled for the 14th April 1800-1900 CET on the use of Kubernetes. Meetings then bi-weekly. Yet to be widely announced

### Licensing

Benedikt contacted all HepMC3 authors for consent to move to LGPLv2.1-or-later instead of GPLv3. All but one answered and agreed. One objection, but not clear that this person actually contributed any code, so this may be a moot point.

### Conditions Databases

Finally having the first meeting next week, Wednesday April 6th: <https://indico.cern.ch/event/1143958/>.
We could delay the start time to 14:30 to be kinder to our US colleagues, and Graeme seems to have pre-empted this :)

---

## AOB

### Anaconda

After deciding that Fermilab would not be considered as non-commercial, which led to a block on access to the Anaconda repositories being put in place at Fermilab and to a rash of PRs to make sure that there were alternatives, Anaconda seem to have changed their mind on this. Fermilab is still considering how to react.

### HSF Mail in Spam?

Graeme put in a ticket with CERN about HSF email being mischaracterised as spam, which seems to have been a problem in the last few months. (There is little/no actual spam from HSF lists.)

### Next Meeting

Next coordination meeting is scheduled for 14 April.
