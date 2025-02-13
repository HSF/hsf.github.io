---
title: "HSF Coordination Meeting #282, 13 February 2025"
layout: plain_toc
---

## Attending

Present/Contributing: Graeme Stewart, Peter Fackeldey, Torre Wenaus, Luke Kreczko, Tommaso Lari, Juan Miguel Carceller, Alexander Moreno Briceño, Christian Wessel, Ruslan Mashinistov, Matthew Feickert, Stefan Roiser, Inês Ochoa, Wouter Deconinck, Michel Hernandez Villanueva, Michel Jouvin, Claire Antel, Saptaparna Bhattacharya, Pere Mato

Apologies/Contributing: Eduardo Rodrigues, Liz Sexton-Kennedy, Paul Laycock, Ianna Osborne

## News, general matters, announcements

### European Strategy Update (ESPPU)

The [HSF EPPSU document](https://docs.google.com/document/d/1dTUBTlerXHjrKO37hAuK1MednfukOxvkCSnq0HrnPOM/edit?usp=sharing) has now been open for public comments for more than a week. A lot of comments were received (thank you to those who took the time).

A first "resolving" pass was done on Monday, with some comments being passed back to the Activity Area conveners.

Second "resolving" run planned for Monday 17. Comments open until Tuesday 18. Plan remains to finalise the text by Monday 24 and to proceed with the LaTeXification.

We will re-contact the experiments to get their views on the document and endorsement again.

N.B. The text grew a bit as well (MCnet gave some strong inputs for the MCEG section, but more words!). Some judicious editing will be required to fit into 10 pages.

- See below for some detailed feedback on the Software Trigger and Reconstruction section
- Adding more on non-CERN based projects would be welcome (DUNE, Belle II, ...)

### SHAREing Proposal

The endorsement of the SHAREing proposal was approved and they got a letter from us.

### HSF/WLCG Workshop

Taking place on 5-9 May at IJClab, Orsay, Paris. A preliminary agenda has been agreed with the WLCG organisation team, we will be making a call for abstracts on "Software Sustainability, Community Software and Training" when the workshop will be announced very soon (hopefully later this week).

Indico event is <https://indico.cern.ch/event/1484669/>.

- Main items of timetable have been added, will be public soon, when the announcement is out at the latest
- Early bird registration will be €350, closing early April
    - Must ensure that abstracts are accepted by that time

The HSF organisation team is Michel, Nicole, Eduardo, Paul.

### HSF Seminar Series and Compute Accelerator Forum

- [Seminar Indico Category](https://indico.cern.ch/category/18810/).
- [Compute & Accelerator Forum Category](https://indico.cern.ch/category/12741/)

#### Recent and Planned Meetings

- 19 February: C&AF - Verrou, floating point stability check - video has been uploaded
- 26 February: HSF Seminar - 4D reconstruction
- 26 March: HSF Seminar - Technical debt on scientific SW (with a focus on some HEP frameworks)
    - Originally EPPSU seminar is postponed!
    - We could have this later in the year, even after the Venice Symposium

An email list is now available to join the seminar organisers: hsf-seminar-conveners@gmail.com

(from Claire, Michel, Nicole)

### Steering Group

Steering Group meeting happened on [11 February](https://indico.cern.ch/event/1509188/) (minutes in preparation).

Discussed feedback from the Advisory Group on points that we raised.

- We will investigate how to make the HSF a legal entity, as a Swiss Association
- As well as having the HSF as a recognised consortium or collaboration
    - This is a lengthy legal process, but should result in official recognition for the HSF
- We discussed with them the Activity Areas and got specific input re. the generators group (see below)
- For project affiliations (where the process is going slower than we hoped) the encouragement was to try to attract larger projects into the process to demonstrate its value
- Discussing the HSF's goals, we were strongly encouraged to advocate on *promoting commonality and collaboration in new developments* that would allow the HSF to play the most effective role it can for the community.

### HSF Affiliated Projects and Software

*We need to find people to help do these reviews.* They are fairly lightweight and should not take a lot of time - we are checking usefulness and impact in the community, as well as software development and project best practices.

The [NNPDF collaboration](https://github.com/NNPDF) asked several months ago to be included - discussions with generator conveners to find an additional reviewer.

- Steve Mrenna will help here

We should also start to approach our previous projects. Volunteers?

**Volunteer Corner:** People prepared to do 1 review in the next month: Graeme, Eduardo, Uwe

- We will setup a spreadsheet for people to volunteer and give their areas of expertise

**Link to the review template:** [here](https://docs.google.com/document/d/1l8Tkruo0EEHwgRBQPmiHq-i4BuwwiR1choRRMUIv6qY/edit?usp=sharing).

The Steering Group agreed to approach Dirac, Rucio, ACTS, HLS4ML and XrootD to discuss engaging.

The Training Group will offer to help projects who want to improve their tutorials (this is required for a Silver badge).

## Activities Updates

The Steering Group refreshed it's liaisons with the AAs and we are proceeding with planning chats with you all. The current assignments are:

{:.table .table-hover .table-condensed .table-striped}
| Group                                | SG Liaison        |
| ------------------------------------ | ----------------- |
| Data Analysis                        | Mark and Eduardo  |
| Detector Simulation                  | Torre             |
| Physics Generators                   | Stefan            |
| JuliaHEP                             | Pere              |
| PyHEP                                | Eduardo           |
| Reconstruction and Software Triggers | Claire and Paul   |
| Tools and Packaging                  | Liz               |
| Training                             | Nicole and Graeme |

The AA conveners should also free free to reach out to their liaison to speed the planning!

Please remember to update your activity page on the HSF website with the names of the current conveners.

### Mailing List

The activities list has been renamed to <hsf-activities-conveners@googlegroups.com>.

## Activity Updates

### Data Analysis

Recent work focused on the EPPSU document.

### Software Training

Future events:

- [12th HEP C++ Course and Hands-on Training - The Essentials](https://indico.cern.ch/event/1477096/) - March 10-14, at CERN. Registration for in person registration will close 2 March. Mentors are welcome to help for the afternoon hands-on training sessions.
- HSF/IRIS-HEP Analysis Reproducibility (Virtual) - March 24-28. Registration will be open soon.

### Software Tools and Packaging

Will meet soon to plan the priorities.

### Detector Simulation

Recent work focused on the ESPPU document.

### Reconstruction and Software Triggers

#### ESPPU input

HSF doc well circulated in ATLAS: Claire presented HSF input on Trig & Reco at ATLAS trigger general meeting.  HSF doc also highlighted at last week's ATLAS SW & Computing week.

HSF input vs ATLAS SW & Computing input: Complimentary in that HSF input focussed mainly on online challenges, and ATLAS input focussed on offline/sites.

##### Status of draft comments

A few to be addressed:

- Reference LHCb and ALICE in ML section -> Christina to cover this. Seems all experiments want contribution here: Will need to either make section longer or replace.
- Comment on expanding on usefulness of HLS4ML type projects/translation layers (also providing sw sim, competing standards for FW development, preserving/growing limited FW programming expertise). -> Addressing this will add a couple of lines.
- Comment on citing fastjet (but need to figure out where)
- My own comment on highlighting the sustainably developed GPU implementations for online processing by LHCb (Allen project) and ALICE (vendor-unlocked ITS reco) - at the moment, mention of the achievement of full online GPU implementations actually pretty crisp.
- A comment on recommendations summary.*

##### Review of recommendations

*Had a closer look at recommendations for our section. It's undergone a lot of changes and in particular, still needs to fit in properly with what we say in the section.

###### Current recommendations

1. Support R&D into heterogeneous architectures as well as training in relevant skills, particularly with support for AI/ML solutions on novel devices.
2. Continue investing into rapid data reduction techniques to reduce rates without compromising physics.
3. Invest in the development of new algorithms that improve physics from timing detectors.
4. Support common software solutions that can support and encourage collaboration between experiments.
5. Invest in software validation and quality assurance, infrastructure and training.

###### Issues

1. We did not previously link AI/ML with heterogeneous architectures. Heterogeneous computing is more than ML/AI.
2. “data reduction techniques” -> “real-time analysis” and “streaming readout”? Also aim is to _increase_ rate. Also, the purpose of these techniques is to not let physics programs _be_ compromised by tight event selections.
3. Statement a bit weak if we want to highlight that this is next generation reconstruction.
4. “support” is written twice -> just “encourage"?
5. This statement throws a lot of 'random' things into one line without a clear link.

###### Suggestions

1. Support R&D in heterogeneous architectures, including AI/ML solutions on novel devices, along with the associated skill development.
2. Invest (early?) in real-time and streaming readout data processing techniques with emphasis on reliability, to address growing storage pressures in ambitious HEP programs. 
3. Invest in new algorithm developments using evolving precision timing detector technology to significantly advance particle reconstruction in dense environments.
4. Support common software solutions that encourage collaboration between experiments, particularly in the widespread use of ML/AI.
5. Invest in sustainable software development by promoting software maintenance, validation, quality assurance, dedicated software groups and developer training.

(note: this wasn’t reviewed by Christina and Joe (Joe’s in the wrong damn timezone), but since this part wasn’t written by us I thought ok to share and discuss here).

#### HSF seminar on 4D reco

26 February, <https://indico.cern.ch/event/1465929/>.

Joe sent a reminder to speakers, prepared agenda and sent announcement to Trig&Reco mailing list.

*We will include this in next week's general announcement.*

#### New convener meetup

Old and new conveners in contact, meeting already planned, with SG liaisons.

A warm welcome again to Christian, Inês and Maarten!

### PyHEP

First planning meeting was yesterday. PyHEP.dev planned for Seattle the week after SciPy conference, which is also in WA.

Marcel Rieger (DESY, CMS) has also joined the PyHEP team.

### Physics Generators

AG feedback (from MCnet): very positive about the role that the HSF group can play in linking up to generators work in the neutrio and Higgs factory communities. Encouraging and developing common standards, together with the LHC community, would be a valuable contribution.

[NuSTEC](https://nustec.fnal.gov) is also preparing a ESPPU contribution that will discuss importance of neutrino event generators. Steven Gardiner is involved in both efforts.

LHC MC WG are also preparing an input - Stefan Roiser would be a good person to contact about this.

### JuliaHEP

The next JuliaHEP workshop will be at Princeton University, 28-31 July. Registration is already open!

For registration and abstract submission, please visit  <https://indico.cern.ch/e/juliahep2025>.

#### Student Sponsorships

A limited number of sponsorships are available for students, covering travel, accommodation, and meals.

#### Important deadlines

- 31st March: Abstract submission deadline
- 25th April: Early registration deadline for local participation
- After 25th April, an additional fee will apply
- 7th July: Final registration deadline

### GSoC program 2025 announced

Contact <mailto:hsf-gsoc-admin@googlegroups.com> in case of questions.

Project proposals should now be in place, but additional projects can still be submitted.

---

## AOB

### Archive no-longer-maintained repositories in github.com/HSF  organization?

The relevant repos were put into archive mode (one deleted).

### Linux Foundation's High Performance Software Foundation Meeting, May 5-8, Chicago

Input from the HEP community is particularly encouraged: <https://events.linuxfoundation.org/hpsf-conference/>

### EVERSE Network Launch Meeting

The [EVERSE project](https://everse.software) is setting up a network of those interested in improving the quality of research software. The online [Launch Event](https://indico.cern.ch/e/eversenetworklaunch) will happen Tuesday 18 February at 10h CET - all welcome to sign up.

### Next Meeting

Next meeting will be [27 February](https://indico.cern.ch/event/1477071/)

### Chair This Meeting 👇

Please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing a future coordination meeting. (There is even a [HOWTO guide](https://hepsoftwarefoundation.org/organization/running-meetings.html)).
