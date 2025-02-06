---
title: "HSF Coordination Meeting #281, 30 January 2025"
layout: plain_toc
---

## Attending

Present/Contributing: Graeme Stewart, Matthew Feickert, Luke Kreczko, Eduardo Rodrigues, Alex Held, Paul Laycock, Peter Fackeldey, Tommaso Lari, Juan Migel Carceller, Ianna Osborne, Davide Costanzo, Ruslan Mashinistov, Krzysztof Genser, Joe Osborn, Richa Sharma, Saptaparna Bhattacharya, Patrick Gartung, Uwe Hernandez Acosta, Nick Smith, Alexander Moreno, Claire Antel, Liz Sexton-Kennedy, Steven Gardiner, Christian Wessel

Apologies/Contributing: Michel Jouvin, Michel Hernandez Villanueva

## News, general matters, announcements

### European Strategy Update (ESPPU)

We now have an [advanced draft](https://docs.google.com/document/d/1dTUBTlerXHjrKO37hAuK1MednfukOxvkCSnq0HrnPOM/edit?usp=sharing) - thanks to everyone who contributed to get the document to this stage.

Last week we got the inputs from the activity areas and Michel and Graeme did an editing pass, harmonising the style and drawing out key points as bulleted recommendations (for the TL;DR crew). A preamble and conclusion have been added.

The section on Event Generators still needs some more key input re. FCC-ee in particular; the other sections are close to final for this stage.

Timeline:

- HSF internal review this week (until Monday) - please read over and comment/improve
- Monday 3 Feb, Michel and Graeme will resolve all comments and prepare the first public draft
    - Having a robust section for generators by this stage is essential
- Tuesday 4 Feb, circulate public version, commenting period for ~2 weeks
    - In particular we will contact the experiment computing coordinators to pursue endorsment by the experiments
- Monday 24 Feb, prepare the final version of the document
    - Collect endorsements
- Before Monday 31 Mar, submit to EPPSU

Notes:

- We will stay in Google Docs for the public commenting period, then move to LaTeX in Overleaf for the final version
- To handle the pain of references, please add a literal `\cite{paper}` into the Google Doc text, together with the BibTeX citation at the bottom of the document
- The endorsement strategy will depend on feedback from the experiments
    - Individual endorsement doesn't make much sense if one's experiment is signing
- Activity area conveners will be added as editors
- The document is right on the limit for size (it's 12 pages in Google Docs, but much closer to 10 in LaTeX)
    - Therefore, if you want to suggested adding more, please also suggest what we can cut (zero sum suggestions!)
    - We will trim the document to fit into 10 pages (LaTeX) before circulation

### SHARIng Proposal

We have a request for a letter of support for the SHARing proposal from Davide Costanzo (Skills Hub for Accelerated Research Environments Inspiring the Next Generation proposal). This is an application for UKRI funds for Digital Research Infrastructure Skills Hubs for Accelerated Compute.

The proposal synopsis is attached to the agenda.

We have discussed in particular with Davide that we would anticipate working together on training, using HEP codes as test cases and helping on their advisory board from the HSF. Specifically:

- Participate in some of the workshops and some steering committees, overall once or twice a year. 
- The proposal is to fund "mini-projects" and we aim to have some of them to be in the particle physics area and with common interest with the HSF work. 
- We also aim to fund more training events, like the C++ school we had in Manchester last year, which was very well received. 

Comments to the Steering Group please!

### HSF/WLCG Workshop

Taking place on 5-9 May at IJClab, Orsay, Paris. The HSF organisation team is Michel, Nicole, Eduardo, Paul.
We at least need to have a "save the date" announcement and start herding abstracts et al. Can also put this on the website.

### HSF Seminar Series and Compute Accelerator Forum

[Seminar Indico Category](https://indico.cern.ch/category/18810/).
[Compute & Accelerator Forum Category](https://indico.cern.ch/category/12741/)

Next scheduled events are:
     
- 19 February: C&AF - Verrou, floating point stability check
- 26 February: HSF Seminar - 4D reconstruction
- 26 March: HSF Seminar - EPPSU

We have agreed to co-organise these meetings, so they can be coherent and reduce duplicated efforts. They will both live in the same Indico area to simplify attendees' scheduling. 

This could be in the new Indico Global instance - TBD.

### Steering Group

Next SG meeting is 11 February.

### Advisory Group

We had the first meeeting with the Advisory Group Friday 24 January - thanks to the experiments and communities who joined!

The outcomes of the meeting will be discussed with the SG and we'll report later.

### HSF Affiliated Projects and Software

*We need to find people to help do these reviews.* They are fairly lightweight and should not take a lot of time - we are checking usefulness and impact in the community, as well as software development and project best practices.

The [NNPDF collaboration](https://github.com/NNPDF) asked several months ago to be included - discussions with generator conveners to find an additional reviewer.

We should also start to approach our previous projects. Volunteers?

**Volunteer Corner:** People prepared to do 1 review in the next month: Graeme, Eduardo, Uwe

**Link to the review template:** <https://docs.google.com/document/d/1l8Tkruo0EEHwgRBQPmiHq-i4BuwwiR1choRRMUIv6qY/edit?usp=sharing>.

Todo: add on the HSF site a page with the list of affiliated projects. - now done, <https://github.com/HSF/hsf.github.io/pull/1639>.


## Activity Convener Updates

We are essentially concluded for the convener search of 2025.

We will be contacting the conveners for each group and arranging for planning meetings for activities with SG Liaisons.

- Data Analysis: Matthew Feickert (new), Nick Smith (continues), Jamie Gooding (continues), Luke Kreczko (new)
    - Thanks to Alexander Held who steps down
- Simulation: Makoto Asai (new), Tommaso Lari (continues), Anna Zaborowska (new)
    - Thanks to Kolja Kauder and Krzysztof Genser who step down
- Physics Generators: Saptaparna Bhattacharya (continues), Stephen Mrenna (continues), Steve Gardiner (continues)
    - Thanks to Phil Ilten who steps down
- PyHEP: Nikolai Hartmann (continues), Ianna Osborne (new), Peter Fackeldey (new), Matthew Feickert (stepping down but continues as advisory and to help with PyHEP)
    - Thanks to Eduardo Rodrigues and Jim Pivarski who step down
- Reconstruction and SW Triggers: Inês Ochoa (new), Joe Osborn (continues), Maarten Van Veghel (new), Christian Wessel (new)
    - Thanks to Claire Antel and Christina Agapopoulou who step down
- Development Tools and Packaging: Ruslan Mashinistov (new), Juan Migel Carceller (new), Wouter Deconinck (new)
    - Thanks to Andrea Valenzuela Ramirez, Patrick Gartung, Reiner Hauser who step down
- Training: Michel Hernandez Villanueva (new), Richa Sharma (new), Alexander Moreno (continues), Lera Lukashenko (continues)
    - Thanks to Holly Szumila-Vance and Jim Pivarski
- JuliaHEP: Pere Mato (continues), Jerry Ling (new), Alexander Moreno (continues), Uwe Hernandez Acosta (continues)
    - Thanks to Tamas Gal who steps down

Those conveners who are stepping down will be relieved of being on the mailing list after this meeting.

N.B. To better reflect our new nomenclature, we propose to rename the mailing list from `hsf-wg-convenors@googlegroups.com` to `hsf-activity-convenors@googlegroups.com`

## Activity Updates

### Data Analysis

Recent work focused on the EPPSU document.

### Software Training

Past events:

- HSF/IRIS-HEP Training Hackathon: Analysis Reproducibility (Preservation) - January 27,  17:00 CERN time

Future events:

- [12th HEP C++ Course and Hands-on Training - The Essentials](https://indico.cern.ch/event/1477096/) - March 10-14, at CERN. Registration is open. Mentors are welcome to help for the afternoon hands-on training sessions.
- HSF/IRIS-HEP Analysis Reproducibility (Virtual) - March 24-28. Registration will be open soon.

New Training Material:

- [Array oriented programming for particle physicists](https://hsf-training.github.io/array-oriented-programming/0-intro.html) (Developed by Jim Pivarski)
- Array oriented puzzles (Developed by Jim Pivarski)
- [Deep Learning for Particle Physicists](https://hsf-training.github.io/deep-learning-intro-for-hep/00-intro.html) (Developed by Jim Pivarski)

Training material in progress:

- Introduction to Databases for HEP (Led by Michel Hernandez Villanueva, Ruslan Mashinistov and Anil Panta)
 
Talks:

- How to train a HEP researcher - Lera Lukashenko - LHCb Computing Workshop, January 27-31

### Software Tools and Packaging


### Detector Simulation

Recent work focused on the ESPPU document.

### Reconstruction and Software Triggers

Recent work focused on the ESPPU document.

### PyHEP

Looking forward to meeting with the new conveners.

### Physics Generators

[NuSTEC](https://nustec.fnal.gov) is also preparing a ESPPU contribution that will discuss importance of neutrino event generators. Steven Gardiner is involved in both efforts.

LHC MC WG are also preparing an input - Stefan Roiser would be a good person to contact about this.

For FCC inputs Sapta is involved. We have contacts with a few experts to help with the HSF document.

### JuliaHEP

The next JuliaHEP workshop will be at Princeton University, 28-31 July: <https://indico.cern.ch/e/juliahep2025>. More details to follow soon.

Announcement is ready to go! And the poster!

### GSoC program 2025 announced

Contact hsf-gsoc-admin@googlegroups.com in case of questions.

We're very happy that Maciej Szymanski has joined the organising team.

---

## AOB

### Website

There was a clean up of stale issues and PRs for the website.

Currently we are planning to stay with Jekyll + Minima, and just to make incremental improvements.

### Archive no-longer-maintained repositories in github.com/HSF  organization?

Can be safely archived, if no new maintainer found (in my opinion, (Valentin Volkl)):

https://github.com/HSF/TrickTrack
https://github.com/HSF/cmaketools
https://github.com/HSF/hep-spack
https://github.com/HSF/spack

ACTION: archive these repos.

### Next Meeting

Next meeting will be [13 February](https://indico.cern.ch/event/1477071/)

### Chair This Meeting 👇

[Coordination meeting slots](https://indico.cern.ch/category/7970/) are booked for 2025 - the usual pattern every two weeks on *odd* weeks of the year.

Please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing a future coordination meeting.
