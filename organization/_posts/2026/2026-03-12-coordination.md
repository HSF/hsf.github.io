---
title: "HSF Coordination Meeting #304, 12 March 2026"
layout: plain_toc
---

## Attending

Present/Contributing: Michel Villanueva, Claire Antel, Eduardo Rodrigues, Ruslan Mashinistov, Graeme Stewart, Stephen Mrenna, Steven Gardiner, Juraj Smiesko, Christian Wessel, Alexander Moreno, Stefan Roiser

Apologies/Contributing: Maarten van Veghel, Saptaparna Bhattacharya, Peter Fackeldey

## News, general matters, announcements

### HSF Seminar Series and Compute Accelerator Forum

Planned HSF seminars:
- Seminar on HS3: [25th March](https://indico.cern.ch/event/1622602/)
- Seminar by Kati Lassila-Perini (chair) on ICFA Data Lifecycle panel [best practice recommendations](https://icfa-data-best-practices.app.cern.ch/): [29th April]
- 2nd in series on AI-assisted SW tools organised by software tools & packaging - possibly separate seminar organised with sustainability group.

Seminars beyond April?
- Probably no seminar in May: Clashes with CHEP.
- Should consider topic ideas inspired by CHEP26 (speakers would have material ready).

HSF seminar conveners are reachable at <mailto:hsf-seminar-conveners@googlegroups.com>.
Please send your suggestions for next seminars.

### Steering Group & Advisory Group

Confirmed date for the **next WLCG/HSF Workshop is 2-6 November 2026, Bologna**.

- Let us know if you would like to suggest topics/themes for the workshop.

### HSF Affiliated Projects and Software

List of current reviews underway:

- DIRAC / DIRAC X - done, sent an email to DIRAC reps, being cross-checked
- NoPayloadDB Conditions Database - ongoing
- Pepper - ongoing (mostly done)
- MadGraph5_aMC@NLO - done, will be sent to SG for review
- Pythia - ongoing (mostly done)

Do not hesitate to discuss around you to identify relevant projects/libraries that could engage with the affiliation programme.

Thank you very much to those who accepted to act as a "reviewer" or spontaneously put themselves forward. This is super appreciated; it makes all the difference.

Very positive feedback from the Pythia developers about the process!

## Activities Updates

### GSoC 2026

Have received 39 project ideas, significantly more than last year.
Candidate selection for projects underway, application window for contributors opens March 16th, closes March 31st.

Sent out information and dashboard invites to mentors. As it needs a google account (but not a CERN-managed one) this process is unfortunately a bit complicated. Contact admins in case of problems.

Would be nice to get some inputs for the students from the Training WG after the projects kick off in May, will send a mail.

Graeme noticed that there is a European Summer of Code now (inspired by GSoC), <https://www.esoc.dev/#about>.

### Software Training

#### Next Trainings

- [14th HEP C++ Course and Hands-on Training - The Essentials](https://indico.cern.ch/event/1617123/), 9-13 March (hybrid)
    - Registration:
        - Attendance at CERN: 15
        - Remote Attendance: 82

- [Analysis Reproducibility Training (Virtual)](https://indico.cern.ch/event/1658598/) - April 27-30.
    - Modules: CI/CD GitHub Actions, Docker/Podman, Apptainer, CI/CD GitLab, and REANA
    - It will be announced this week

- There is interest in the SHiP (Search for Hidden Particles) collaboration to develop a Rust for HEP Training.
    - New framework will probably include Rust
    - DAQ and CondDB already use Rust
    - Plan:
        - Hackathon, early this Summer
        - First Rust training next fall

#### Papers

- Training on Data Analysis Reproducibility via Containerization with Apptainer. It will be submitted to The Journal of Open Source Education, JOSE, and also to the arXiv.

### Event generators

- Sapta's participation in GSoC: student selection ongoing.


### PyHEP

- PyHEP.dev 2026 is fixed: Sep 7 - 9, at Nikhef, Amsterdam.
- Indico page etc. will follow soon in coordination with the Nikhef contacts.
- During PyHEP.dev Peter F. will do a ~1h seminar talk at Nikhef about our PyHEP activities (Sep 8).

### JuliaHEP

- [Planning meeting](https://indico.cern.ch/event/1662091/) today at 16:00 CERN time.
    - JuliaHEP 2026 will be in Munich, October 19-23. We will start advertising the event next week!
    - JuliaCon 2026 - JuliaHEP Mini-Symposium - Julia for Nuclear and Elementary Particle Physics: From Precision Science to High-Performance Tools.
        - We have received 9 contributions!

## AOB
   
Do not hesitate to get in touch with the SG if you have/know of events useful to add to the HSF calendar.
The calendar is used by very many to check for available dates, constraints, and plan events. Thank you in advance.

### Physical Constants / HEPdata Library

Reminder that we proposed a C++ header-only library that defines physical constants and some salient HEPdata in a lightweight, easy-to-use manner. Also taking into account versioning.

We had a meeting 2 weeks ago.

There is now a "proof of concept" version of this, [hep-constants](https://github.com/HSF/hep-constants) that can process data from CODATA files, import units and prefixes from the Python hepunits package and generate C++ headers (using some symbolic manipulation). Now awaiting feedback from others on the general approach.

### Next Meeting

The next coordination meeting will be on March 26th.

### Chair This Meeting 👇

Please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing a future coordination meeting. (There is even a [HOWTO guide](https://hepsoftwarefoundation.org/organization/running-meetings.html)).
