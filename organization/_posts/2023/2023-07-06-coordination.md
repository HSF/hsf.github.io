---
title: "HSF Coordination Meeting #253, 6 July 2023"
layout: plain_toc
---

## Attending

Present/Contributing: Graeme Stewart, Benedikt Hegner, Eduardo Rodrigues, Claire Antel, Patrick Gartung, Michel Jouvin, Pere Mato, Liz Sexton-Kennedy, Nick Smith, Patick Gartung, Sudhir Malik, Tamas Gal, Valentin Volkl, Markus Diefenthaler, Matthew Feickert, Wouter Deconinck, Giulia Casarosa

Apologies/Contributing: Caterina Doglioni, Efe Yazgan

## News, general matters, announcements

### Google Summer of Code, 2023

- Representative for the mentors summit to be decided.
  - It shouldn't just be one of the coordinators, should be someone more involved in mentoring.

### LHCC

#### LHCC 154 (June)

The [LHCC Minutes](https://cds.cern.ch/record/2861565?ln=en) are now published. On analysis facilities:

> A focus session on Analysis Facilities has been organised during the LHCC week, where the current R&D work happening within the community and discussed in the HSF Analysis Facilities Forum has been presented. The HSF Analysis Facilities Forum has focused on the technical building blocks that can make the user experience more productive. Novel concepts of Analysis Facilities, integrating interactivity, scalability (offload) and Machine Learning tools are being built.

> The **LHCC recommends** that experiments engage in the process of developing and defining the structure of the future Analysis Facilities and **requests** they produce a document which defines the use cases in order to establish realistic benchmarks. This process should be coordinated with the HL-LHC Computing and SW review panel. The document is expected to be regularly updated in the process towards the HL-LHC.

#### LHCC 155 (September) and 156 (November)

The next LHCC meeting (155, September) foresees a discussion on training, in the normal 20' software slot. Liz and Graeme need to propose a speaker.

For LHCC meeting 156 (November), there will be a special session (~90') on generators.

#### Software Liaisons

There will be some change in the software liaison roles in WLCG. This will be presented in more detail next meeting.

## Working Group Updates

### Data Analysis

- Meeting on Monday on [Open Data](https://indico.cern.ch/event/1298400/)
  - Well attended (max 27) despite clashes with events and holidays
  - Talks from ATLAS, CMS, LHCb
- Want to follow up on these topics in ~6-12 months.
- This meeting connected really well with younger people actually doing analysis today.
- Video is posted to <http://videos.cern.ch> (and linked to Indico)
  - N.B. this is much preferred by CERN IT than posting large video files to Indico

### Software Training

- 13 Jul - 14 Jul HSF/IRIS-HEP Software Basics Training (Virtual)
- 12 Jul HSF/IRIS-HEP Python for Analysis Training (Virtual)
- Have had up to 200 registrants, but so for always managed to have enough mentors

#### C++ Course and Hands-on Training

- [Training in Manchester](https://indico.cern.ch/event/1266661/) is finalised, registration is open
- [Advanced C++ course](https://indico.cern.ch/event/1266628/) at CERN will run in October

### Software Tools and Packaging

- Adam Stewart (Spack developer) will come to CERN in fall (September? not yet fixed) and will make a presentation and be available for discussions at CERN
  - This will kick off a series of discussions
- Also invited the EasyBuild project to give us an update
- There is a look again at stack building tools in the Architects' Forum.
  - Marco Clemencic and Graeme Stewart are leading this, which focuses on why we do not converge on a single tool in the community and what the prospects for that are, particularly w.r.t. Spack.
  - Will discuss with SFT, LHC expts., Fermilab and FAIR (anyone else? please let us know)
  - Hope to conclude by autumn
  - And we will report and discuss in the HSF Packaging WG meeting

### Reconstruction and Software Trigger

- In touch with LHCP speaker on "zero waste computing" - speaker available in September

### PyHEP

- PyHEP.dev 2023 (in-person developers workshop):
  - In just 2 weeks from now, see <https://indico.cern.ch/e/PyHEP2023.dev> for details.
  - Programme (discussions, presentations) under active preparation, with topics being listed and people even added already via  the repository <https://github.com/HSF/PyHEP.dev-workshops>, which we created for this and future similar workshops.
- PyHEP 2023 (online users workshop):
  - Preparations started.
  - Open registration and call for abstracts really soon.
  - See <https://indico.cern.ch/e/PyHEP2023> for details.

### Event Generators

- Held online workshop on [HSF Event Generator Tuning](https://indico.cern.ch/event/1283969/) on June 27 and 28:
  - On the first day, we started with an overview of tuning MCEGs presented by Peter Skands (Monash University). Following this, representatives from various experimental collaborations, ALICE, ATLAS, CMS, ePIC, LHCb, and neutrino experiments, shared their tuning experience. The session ended with a hands-on session, delving into how different parameters influence observable distributions in Pythia.
  - The second day featured an insightful overview of semi-automated tuning by Andy Buckley (University of Glasgow). This was followed by a community discussion, fostering knowledge exchange and collaboration. At the end of the workshop, we engaged in a hands-on tuning tutorial using RIVET and Professor.

- Restart monthly meetings, survey planned for topics of interest.

#### Discussion

- Was the meeting recorded?
  - The first day, yes; the second not, due to technical problems.

- There is a meeting planned on the use of GPUs in event generators. This will happen at CERN in the autumn (November?), dates not fixed yet. Stefan Roiser and Andrea Valassi are involved in the planning.

### Frameworks

- Will have a presentation on the experience of HPX by ATLAS soon.

## Other Interest and Activity Areas

### JuliaHEP

- Preparation of the JuliaHEP workshop ongoing.
  - So far we have 36 participants, ~7 of them in person.
- Decided to start the JuliaHEP community meetings after the workshop.

### Compute Accelerator Forum

Next meeting, Wednesday 12 July: [ALICE O2](https://indico.cern.ch/event/1264298/)

---

## AOB

### Community Calendar

Should we open the calendar to events from other communities? e.g., Einstein Telescope.

- Yes, we think this is fine for relevant events.
- Try to find someone in the organisation who would be responsible for posting items (see [instructions](https://hepsoftwarefoundation.org/calendar.html)).

### Website

Benedikt started an [issue in GitHub](https://github.com/HSF/hsf.github.io/issues/1411) to gather ideas about reorganising and revamping the website to better reflect our areas of actual activity.

### HSF Twitter

Because of recent changes to Twitter (*explicative deleted*), our twitter feed on the website isn't working.

Should we be considering other social media platforms?

- There are now so many alternatives popping up it's very hard to say where the next space will actually be - we may just need to pause our social media presence until it's all much clearer. (And we can see, e.g., where CERN, Fermilab media teams go.)

### Next Meeting

The next meeting will be, on [20 July](https://indico.cern.ch/event/1225019/) (back to 32/S-C22 at CERN).

Propose then to take a break until 31 August.

Please [sign up](https://docs.google.com/spreadsheets/d/1Z1Z4payCpieOLiVFcC6y9j-KCj71u6xX232LHUgIHfI/edit) for chairing this or one of the future coordination meetings.
