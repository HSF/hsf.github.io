---
title: "HSF Coordination Meeting #227, 14 April 2022"
layout: plain_toc
---

Present/Contributing: Graeme Stewart, Markus Diefenthaler, Benedikt Hegner, Stefan Roiser, Efe Yazgan, Michel Jouvin, Allie Hall, Torre Wenaus, Paul Laycock, Krzysztof Genser, Liz Sexton-Kennedy, Marc Paterno, Matti Kortelainen, Dorothea vom Bruch, Eduardo Rodrigues, Kyle Knoepfel, David Lange, Kevin Pedro, Mason Proffitt, Michael Hernandez, Daniel Elvira, Jin Huang

Apologies/Contributing: Serhan Mete, Andrea Valassi


## News, general matters, announcements

### Workshops in 2022

#### Analysis Ecosystems Workshop

23-25 May: <https://indico.cern.ch/e/aew2>

**Registration is open!** (limited this to 80 in-person places).

2022-03-31: 61 people have registered, 50 in-person

- We are now filling out ideas for the timetable, proposing 1 hour of plenary discussion per topic and up to 3 hours of parallel activity
- Aim is to have a block timetable for early next week and then to re-advertise the workshop

*Do think about key people to invite.*

#### Detector Simulation on GPU Community Meeting

- HSF Detector Simulation on GPU Community Meeting to be held 3-6 May
  - <https://indico.cern.ch/e/simgpu>
  - The agenda topics are now mostly filled in.

### Google Summer of Code / Season of Docs

GSoC proposal period ends 19 April (not much time left!).

### HSF History Paper

The [History Paper](https://www.overleaf.com/read/pmcmkjwmpmdv) has been converted to LaTeX and uploaded to overleaf.

References need to be redone properly, but the text should be fine.

Ask Graeme if you want to help (to get the editing link).

Authorship - propose to name those who helped write the paper, then "for the HSF".

### Talks

Graeme will give a talk on "Software Frameworks" in the [JENAS meeting](https://indico.cern.ch/event/1040535/) in Madrid 3-8 May ("frameworks" to be interpreted broadly as the whole data processing pipeline). Would like to highlight multi-experiment projects (like ACTS) and adaption to heterogeneous hardware (like Allen) as broad themes.

Meeting is primarily European, but see ICFA point below.

Draft slides will appear next week...

## Working Group Updates


### Data Analysis

- Had a successful topical [meeting on systematics](https://indico.cern.ch/event/1148158/) in data analysis this week, with ~18 participants


### Detector Simulation

- Successful meeting on CaloChallenge (~2 dozen participants)
- DD4hep meeting scheduled for May 23
- See above re: detector simulation on GPU meeting

### Reconstruction and Software Trigger

* After two topical meetings in March, Reco/Soft-Trigger group does not plan an event in April.
* The May meeting will focus on Graphic Neural Network in tracking reco application. Date TBD with on-going discussion with potential speakers
* We have been exchanging an idea with the organizers of the Streaming Workshop X (in particular Markus Diefenthaler) about the possibility of an HSF session at the workshop. The idea was welcomed by the organizer. Meanwhile, the conclusion is to have such a session in future Streaming Workshop, as this editing will focus on reorganizing the EIC streaming community after detector proposal selection. 
* We aim to have 1-2 PID (RICH type) reconstruction meetings. Reached out to a few potential speakers who prefer later in the year for such a meeting. We plan to also reach out to [RICH Pattern Recognition Challenges](https://agenda.infn.it/event/30966/) for a summary in our meeting. 


### PyHEP
- The PyHEP 2022 workshop now has an Indico page - <https://indico.cern.ch/e/PyHEP2022>.
    - News and advert imminent.
- Next topical meeting will take place on June 1st.

### Software Tools and Packaging

No substantial update yet. We are still arranging a time for our next meeting; we discussing times with speakers for an update from a long-ago ACTS talk, concentrating on build time and monitoring.

### Event Generators

Recent meetings:

* 10th March: Snowmass Generators Whitepaper
* 4th March: ATLAS V+jets.
* 7th April: Further Sherpa efficiency improvements by Enrico Bothmann.

Future meetings: 

* 5th May: Neutrino event generators (confirmed)
* 2 June: Master thesis on chirality flow formalism (TBC)
* 23 June: EIC/NP Generators usage (TBC)
* 7th July: Event generation with Julia (confirmed)
* 1st Sept.: AI/ML-focussed discussion (TBC)


### Frameworks

Our speaker for yesterday (13 April) had to reschedule for 25 May.  The next meetings will be:

- May 4, [Mu2e and its Framework Usage](https://indico.cern.ch/event/1138384/) (Roberto Soleti, LBNL)
- May 25, [NOvA and its Framework Usage](https://indico.cern.ch/event/1138383/) (Gavin Davies, University of Mississippi)

### Software Training

* Software Carpentry: Aftermath
    * Feedback from students is positive in overall.  
    * Issues from students without CERN accounts not able to use collaborative tools (Mattermost, SWAN, etc). We will consider alternatives. 
    * Certificate of participation provided to students who have requested. 
        - Tools to generate the certificates are public and we are discussing how to validate them for the next event. 
    * For the next event: determine the milestiones to determine whether people completed the training.
        - Push Jupyter notebooks to Git and point us to them.

* Next Matplotlib training to be held 21-22 Apr 2022 (Virtual).
    * Link to Indico: <https://indico.cern.ch/event/1058838/>
    * 2 days, targeting a 4-5 hours event. 
    * 50 participants registered at the moment. 
    * Material is ready, having a meeting next week to finish details. 


## Other Interest and Activity Areas

### Licensing

We have all but concluded on the HepMC3 re-licensing - time for the PR...

### Conditions Databases

The first meeting of the activity went ahead last week: <https://indico.cern.ch/event/1143958/>

The idea of the meeting was to first see if we could agree on the definition of the problem(s) we are trying to solve, looking at workflows and use cases.  Very encouraging that we seemed to have consensus in the meeting, so there doesn't seem to be a pressing need to discuss "what we missed".  A preliminary strawman (and incomplete) list of requirements was discussed to kick off discussions.  Again we had encouraging consensus and positive contributions.  The idea is to now move on and write this up, i.e. attempt to write a short white paper defining the use cases and requirements.

## AOB

### Computing Training Mentors Request

We have been contacted by Igor Slazyk about a [Norwegian summer school](https://indico.cern.ch/event/1104691/) which will be held from 26 June to 8 July. They are looking for people to help with their hands-on computing tutorial on 1 July in the IT Auditorium. There seem to be no set exercises, but general help with Python and ML and data analysis is likely to be something the students want to do.

### HSF Mail in Spam?

Graeme put in a ticket with CERN about HSF email being mischaracterised as spam, which seems to have been a problem in the last few months. (There is little/no actual spam from HSF lists.)

CERN IT have been active in trying to help with this, which relies on understanding why emails forwarded from users are not landing in the anti-spam training dashboard. However, Microsoft support seems a bit lacking for now...

In the meantime we recommend:

- For sending email to HSF lists, favour plain text
- For people with CERN email, check your Junk E-Mail folder for HSF mail
- Setup a whitelist in your mail client, if you can

### Software in ICFA

A few people discussed with the [ICFA](https://icfa.hep.net) secretary about software in the context of the ICFA. In the last panel meeting it was agreed to go forward with a little discussion round with representatives across the field. The discussion should take place before the next ICFA meeting.

### Next Meeting

Next coordination meeting is scheduled for 28 April.

