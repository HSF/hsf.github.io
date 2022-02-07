---
title: "HSF Coordination Meeting #220, 9 December 2021"
layout: plain_toc
---

Present/Contributing: Graeme Stewart, Benedikt Hegner, Pere Mato Vila, Serhan Mete, Torre Wenaus, Allison Hall, Paul Laycock, Liz Sexton-Kennedy, Alexander Moreno, Nicola Skidmore, Michel Jouvin, Krzysztof Genser, Marc Paterno, Stefan Roiser, Michel Villanueva, Ben Morgan, Michel Jouvin

Apologies/Contributing: Dorothea Vom Bruch

## News, general matters, announcements

### HSF Talks

### HSF Review of 2021

There was a [Software and Computing Roundtable meeting](https://indico.jlab.org/event/420/#day-2021-12-07) this week. Benedikt gave an *HSF Review of 2021* talk, highlighting many successes in a (still) challenging year.

Tried to also convey the message that we want to improve engagement with non-LHC experiements.

### ASCR Workshop on the Science of Scientific-Software Development and Use

There is a DOE supported [ASCR workshop](https://web.cvent.com/event/1b7d7c3a-e9b4-409d-ae2b-284779cfe72f/summary) 13-15 December on scientific software. Graeme, Liz and Eduardo wrote/contributed to [a paper we submitted](https://docs.google.com/document/d/1f3wcOgE8tqh-Q88A3wzQrZaWhLazPl196g1lLkv0XZo/edit?usp=sharing), that has now been accepted.

Liz will participate in a 'roundtable' format and needs to prepare something like a poster summary of the paper. Do we have any HSF posters? AFAWK no, but we do have plenty of talks to draw on.

(The list of HSF talks is a bit out of date, Graeme will try to update it for 2021.)

### Workshops in 2022

- Possible Analysis Ecosystems workshop in May still being sounded out. Gordon is looking for dates to host at CPPM in Marseille.

- Would like to have a review/discussion of progress on simulation on GPUs (AdePT, Celeritas), probably also in May (not the same week!).

## Working Group Updates

### Mandates for 2022

Call for WG Conveners is open and closes this weekend (Sunday 12). Quite a few nominations received, but always happy to get more.

We [added](https://github.com/HSF/hsf.github.io/pull/1034) a clarification on the [WG page]({{ site.baseurl }}/what_are_WGs.html) that we seek convener diversity, particularly from different experiments in the team.

### Data Analysis

- Meeting held yesterday on [Workflow management tools](https://indico.cern.ch/event/1102574/) with contributions from Snakemake, LAW and REANA. Very well attended (25 participants). May attempt a second meeting on this.
  - These tools are very independent of experiment codes so looks like a profitable area for us to work in.

- Metadata document formatted and sent to authors for final review 

### Detector Simulation

- To hold a meeting on using FPGAs for Simulations on Monday
  - <https://indico.cern.ch/event/1096432/>

### PyHEP

- There was a PyTorch tutorial yesterday, which was recorded and it's also available as a Jupyter notebook.
  - Agenda: <https://indico.cern.ch/event/1098618/>

### Software Training

- Software Carpentry Workshop will be held on Dec 13 - 15, 2021. Indico page: <https://indico.cern.ch/event/1097111/>.
  - 50 students registered.
  - 3 instructors from The Carpentries, 4 from the HEP community.

- Report of the status of Training in the Nuclear Physics community during our weekly meeting. Interest to join efforts with the HSF. 
  - Several tools are common with the HEP community and current modules available are already useful. 

- C++ Course regular curriculumn development meeting next week, <https://indico.cern.ch/category/14413/>.

- Possibility of an FPGA programming course, if there is sufficient interest - Stefan will get in touch with LHC computing coordinators

## Other Interest and Activity Areas

### Compute Accelerator Forum

There was a [meeting yesterday](https://indico.cern.ch/event/975017/) which covered the very interesting VecMem library (from ACTS) and GPU simulation from the beams department (as usual, videos are uploaded to CDS and YouTube).

The organising team (Graeme, Ben, Stefan, Maria, Michael) have started putting together the programme for next year, so suggestions always welcome!

### Software and Computing Roundtable

As mentioned above, there was a  [Software and Computing Roundtable meeting](https://indico.jlab.org/event/420/#day-2021-12-07) this week where Benedikt gave an *HSF Review of 2021* talk. There were also talks from the BNL and JLab perspectives.

The meetings for next year are also being organised... contact Graeme, Torre and Paul if you have suggestions for topics.

### Differentiable Computing

Noted that there's really no HSF activity here, so we agree to drop this as an HSF activity.

### Quantum Computing

Noted that there's really no HSF activity here (cf. CERN QTI), so we agree to drop this as an HSF activity.

---

## AOB

### Conditions Databases

A new HSF Activity for Conditions Databases?  BNL are adapting the Belle II conditions database design, which largely follows HSF CWP best practice, for the sPHENIX experiment.  In so doing they are taking this as an opportunity to design something that incorporates as much of the experience and expertise from other experiments as possible.  Paul Laycock, Andrea Formica and Giacomo Govi are interested in attempting to define "the" API for a conditions database (independent of technology choices).  Other interesting discussion topics would be technology choices for the server, payload serialisation, calibration workflows, etc.  This also relates to the relevant parts of the Data Analysis working group's "Metadata" summary paper, particularly analysis global tags.  The interested community is small but that makes knowledge exchange all the more important.  Would it make sense to make this an HSF activity?  It already covers experts from ATLAS, CMS, Belle II, DUNE and sPHENIX!

Supported in the meeting and noted that a lot of work was done around the CWP, with considerable consensus achieved. Hope to define the API and then give a reference implementation? Benedikt volunteers to help as well. Should contact André Sailer for Key4hep link.

### Google Summer of Code

GSoC 2022 is coming!

Who will follow up and coordinate the next round in 2022?

Our current organisers have been doing a great job, for quite a few years, so we can foresee some rotation for next year. Please contact Benedikt if you would be interested (or want to volunteer someone!).

### Calendar for 2022

Reminder to put in events into the calendar.

### Next Meeting

This is the last meeting for 2021, so we wish everyone a really good break over the holiday period!

We will restart meetings on 6 January - dedicate that meeting to review of 2021 and starting to think about planning for 2022.

The meeting slots in [Indico](https://indico.cern.ch/category/7970/) for next year are now booked.
