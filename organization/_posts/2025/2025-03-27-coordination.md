---
title: "HSF Coordination Meeting #285, 27 March 2025"
layout: plain_toc
---

## Attending

Present/Contributing: Graeme Stewart, Eduardo Rodrigues, Claire Antel, Stefan Roiser, Ruslan Mashinistov, Ines Ochoa, Tommaso Lari, Torre Wenaus, Matthew Feickert, Alexander Moreno, Juan Miguel Carceller, Michel Jouvin, Luke Kreczko, Liz Sexton-Kennedy, Christian Wessel, Sapta Battacharya, Richa Sharma 

Apologies/Contributing: Mark Neubauer (US/EU Daylight shift caused meeting conflict for me)


## News, general matters, announcements

### European Strategy Update (EPPSU) final stages

We are in the final stages of the process. We have endorsements from ALICE, ATLAS, Belle II, ePIC, LHCb and MCnet.

There were a few ~minor comments (adding references, mainly) as endorsements arrived. The continually updated final draft is in [CERNBox](https://cernbox.cern.ch/s/XQ3wEp3L8UOVjjb).

CMS and DUNE are expected to endorse this week and WLCG will endorse when all LHC experiments are on board.

CMS asked how they could cite the document, so we have decided to put it onto Zenodo now, to have an immediate DOI. We will also put this final version on arXiv (but the arXiv publication delay means that that DOI will come too late).

### HSF/WLCG Workshop in May

- Abstracts have been coming our way - close to 20 now.
- Sessions are in preparation, in good shape but not yet published.
- Attendance seems low cf. previous workshops.
    - Please sign up!
    - A reminder will be sent to the HSF Forum.

### HSF Seminar Series and Compute Accelerator Forum

[Seminar Indico Category](https://indico.cern.ch/category/18810/).
[Compute & Accelerator Forum Category](https://indico.cern.ch/category/12741/)

The HSF Seminar on *technical debt in software* happened yesterday: <https://indico.cern.ch/event/1520114/>.
- Around 30(?) people in attendance (~6 people in the room)
- YouTube recording already uploaded: <https://youtu.be/BkSiusiqhSk?si=mTqOtJZa2IOv5PS0>.
- No slides uploaded yet but speaker will do so soon - not many plots but plots shown very interesting, e.g.:
<img src="https://codimd.web.cern.ch/uploads/upload_c89f24ba057a1a8882f01ed6843e2e99.png" alt="drawing" width="450" height="300"/>


Planned seminars:

- Planning a seminar on HS3 (HEP Statistics Serialization Standard) with multiple speakers. Finding suitable date in April/June - will exceptionally not be on last Wednesday of month (obviously avoid clash with CAF).
- 28th May: Seminar confirmed on AdePT and Celeritas update on detector simulation with GPUs via the Detector Simulation Activities conveners.

June has a clash with the EPPSU symposium - TBD if we have a seminar.

HSF seminar conveners are reachable at <mailto:hsf-seminar-conveners@gmail.com>.

* Please send your suggestions for this Spring seminars...

### Steering Group

Next SG meeting is being planned for w/b 14 April.

### HSF Affiliated Projects and Software

The review of the [nnpdf](https://github.com/NNPDF/nnpdf) package in underway and the GDoc will soon be make available for feedback via the HSF Forum.
- Reviewers are Steven Mrenna and Eduardo Rodrigues.

ACTS are amenable to becoming affiliated - Graeme will join one of their dev meetings to explain the process.

Conditions DB - July will be a good time for the review.

## Activities Updates

Planning chats between activity conveners and SG liaisons are underway.

{:.table .table-hover .table-condensed .table-striped}

| Group                                | SG Liaison        | Status
| ------------------------------------ | ----------------- | ----------|
| Data Analysis                        | Mark and Eduardo  |           |
| Detector Simulation                  | Torre             | Done      |
| Physics Generators                   | Stefan            | Scheduled |
| JuliaHEP                             | Pere              | Scheduled |
| PyHEP                                | Eduardo           | Done      |
| Reconstruction and Software Triggers | Claire and Paul   | Done      |
| Tools and Packaging                  | Liz               | Done      |
| Training                             | Nicole and Graeme | Done      |

The AA conveners should also feel free to reach out to their liaison to speed the planning!

Please remember to update your activity page on the HSF website with the names of the current conveners.

## Activity Updates

### Data Analysis

Will try to schedule the planning chat soon, see table above.

### Software Training

Ongoing events:

- [HSF/IRIS-HEP Analysis Reproducibility (Virtual)](https://indico.cern.ch/event/1508102/) - March 24-28.
    - 67 people registered
        - Position/Academic Level (69 responses)
            - 18 (26.1%) Junior Ph.D. Students
            - 14 (20.3%) Faculty/Staff/Scientist
            - 13 (18.8%) Senior Ph.D. Students
            - 13 (18.8%) Postdoctoral Researchers
        - HEP Experiment (69 responses)
            - 17 (24.6%) CMS
            - 12 (17.4%) Belle II
            - 10 (14.5%) LHCb
            - 4 (5.8%) DUNE
            - 2 (2.9%) ATLAS
        - Timezone (69 responses)
            - 38 (55.1%) Europe/Africa
            - 18 (26.1%) Americas
            - 13 (18.8%) Asia/Australia

Future events:

- [HSF/WLCG Workshop](https://indico.cern.ch/event/1484669/) - May 5-9. We will have a dedicated training session and we are working on the agenda
- [HSF/IRIS-HEP Software Basics Training (Hybrid)](https://indico.cern.ch/event/1516608/) - Jun 18-20. Hybrid at CERN
- [Deep Learning Train-the-Trainer Workshop](https://indico.desy.de/event/47263/) - Sept 15-19. Organized by the HSF and ErUM-Data-Hub. In-person in Potsdam. Registration is open! Deadline: August 4

ATLAS turnout was low this time - will improve advertising (worth checking their mailing lists for C&SW matters).

### Software Tools and Packaging

- Wouter is giving a talk on Spack at the Linux High Performance meeting Spack session
- Writing some documentation on Kubernetes development
- Thinking about future meetings on advanced practices of using IDEs
- Looking for the entry points of the AI related activities across the collaborations
    - Proposed idea to look at the CERN pilot assistant and contact with the first users
    - Graeme mentioned the talk on use AI for the code-review. This also sounds very inline with this activity  

### Detector Simulation

As mentioned above, we have scheduled talks on Celeritas and AdePT for the Seminar Series in May.

There will be a [Geant4 Technical Forum meeting](https://indico.cern.ch/event/1517917/) tomorrow March 28th.

### Physics Generators

The physics generators group will meet with Stefan from the Steering Group today at 17:00 CERN. We will report on the outcome of the discussion at the next coordination meeting.

### JuliaHEP

[JuliaHEP 2025 Workshop](https://indico.cern.ch/event/1488852/) will be held at Princeton from July 28 to 31.
- Abstract submission deadline: March 31!
- Early registration deadline for local participation: April 25
    - After April 25 an additional fee will apply
- Final registration deadline: July 7 

### GSoC program 2025

Student proposal period has begun.

---

## AOB

### Next Meeting

Next meeting will be [10 April](https://indico.cern.ch/event/1477075/).

### Chair This Meeting 👇

Please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing a future coordination meeting. (There is even a [HOWTO guide](https://hepsoftwarefoundation.org/organization/running-meetings.html)).
