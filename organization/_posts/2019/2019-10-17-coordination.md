---
title: "HSF Weekly Meeting #173, 17 October, 2019"
layout: meetings
---

# {{page.title}}

*Present/Contributors:* Graeme Stewart, Eduardo Rodrigues, Andrea Valassi, David Lange, Attila Krasznahorkay, Agnieszka Dziurda, Chris Jones, Daniel Elvira, Witek Pokorski, Stefan Roiser, Serhan Mete, Liz Sexton-Kennedy, Mark Neubauer, Kyle Knopfel, Nikos Kasioumis

*Apologies:* Pere Mato, Caterina Doglioni

## News and General Matters

### Working Groups in 2020

- We discussed the future of working groups in 2020 in the coordination group
- The decision was that for the current appointed groups we allow convenors to carry on for another year, as we are very pleased with the outcomes of the groups
    - Most convenors have said yes to this proposal (thank you very much!)
    - However, Danilo (Analysis) and Heather (Simulation) have had to step down, due to other commitments
    - We shall therefore call for nominations to replace them
- We also decided that the nomination and appointment process is a successful one and that it should be used more consistently for working groups from now on
    - So we are also going to call for nominations for convenors in the following groups
        - PyHEP
        - Software Tools and Packaging
        - Physics Event Generators
        - Training
    - Current, active, convenors in these areas are stongly encouraged to be nominated, including self-nomination
    - Note that we decided that *Software Tools* and the *Packaging* group can be usefully merged into one
    - Three convenors are sought for each group
- Areas where the HSF activity has been more sporadic and informal will be rebadged as *Activity Areas*
    - These will not have formally appointed convenors, but carry on with the input from motivated members of the community
    - This type of activity is very much encouraged when people would like to start a new interest group (evolution to a working group would be possible, in time)
    - At the moment we propose that *Visulaisation* and *Quantum Computing* become activity areas
- Timeline:
    - Call for nominations next week until mid-November (post CHEP)
    - Comments for the community for ~2 weeks after that (end November?)
    - Appointments to be made in December, if we can, for 2020
        - These will be as now, 1 year, renewable
- **Meeting approved this plan**

### Post-JENAS Meeting

- As discussed in previous HSF coordination meetings & announced on the mailing list, Caterina organised a [meeting](https://indico.cern.ch/event/852242/) with the Nuclear, Dark Matter, Astroparticle communities as a follow-on from the [JENAS Workshop](https://jenas-2019.lal.in2p3.fr/)
    - We presented an overview of the HSF
    - Followed by contributions from nuclear, neutrino, dark matter and ESCAPE communities
        - HSF-ESCAPE interaction encouraged by APPEC in this context
    - Very much a first *getting to know you* meeting
    - The level was quite senior
    - Feedback was positive, but not immedately clear how to take next steps
    - Two interesting concrete things came from the discussions with ESCAPE
        - Training event at LAPP that HEP could be involved in
        - Software directory that is being built as a deliverable for ESCAPE and could be promoted for HEP software projects
    - Caterina and Graeme are thinking we can probably continue interactions at the Lund workshop next year, inviting a few key people (not that we do nothing else untl then!)

## Activity and Working Group Updates

### Detector Simulation
- Next meeting will be on Dec 4th due to CHEP and other experiments' meetings between now and then. We plan it will be on feed-back on use of new geometry tools by experiments. We will contact them soon to fix the agenda. For first meeting next year we would like to invite non-LHC experiments.
- There was a [GeantV dedicated meeting on Tuesday](https://indico.cern.ch/event/818702/). There will be a formal write-up of the results obtained. At the end Pere Mato and Philippe Canal presented directions for future activities. We should follow this up regularly next year.
- Directions on accelerators are now interesting. Will the GeantV group look at this? No, it will be done with new R&D projects. We know that this is hard and will require new approaches.
- Geant Exascale project is exploring this area.
- Contact between ORNL and CERN recently

### Reconstruction and Software Triggers
- Next meeting, targeting "Algorithmic approaches and data structures to efficiently exploit many-core architectures" moved from 9th October to "after CHEP" due to unavailability of the speaker. 

### Software Tools

- In case you missed it, there was a [TAU talk last Monday](https://indico.cern.ch/event/845622/) (monitoring tool)
- To be followed up with a hands-on session, most probably will take place on January 20th at CERN:
    - Imperative to focus on HEP use cases. 
    - It might be nice to give priority to accelerator related examples.
    - Please let us know if you have a workload that you'd like us to focus on.

### PyHEP

- PyHEP 2019 workshop now taking place in Abingdon, U.K., 16-18 Oct., see https://indico.cern.ch/e/PyHEP2019.

![PyHEP 2019 workshop photo](https://codimd.web.cern.ch/uploads/upload_5557a26f5c5546e6cd8b22d4f8964a1e.jpg)

### Frameworks
- Will have a meeting next Wednesday. Plan to have presentation from DUNE. Workflow is quite different from HEP collider experiments. Speaker TBC.

### Training

- [Software Carpentry at CERN, 27-29 November](https://indico.cern.ch/event/834411/)
- A lot of progress in organising the event
- Registration opens tomorrow...
- Advertise this also via HSF lists, particularly to call for helpers

### Event Generators

- No meetings yet after the summer
- Have not pinged or heard back from the Argonne team working on Madgraph on GPUs
- Josh McFayden is working on a setup to allow standalone runs of several generators, which eventually may be incorporated into the HEP-workloads benchmarking suite using Docker containers
- Steve Mrenna will give an overview of activities at the Latin American workshop in Mexico

### Packaging

- [Meeting last week](https://indico.cern.ch/event/848215/) had a very useful discussion on best practices for package relocatability from Ben Morgan
- There are a few packaging contributions we know of at CHEP
- Plan to have another meeting before the end of the year

## Workshops
### Next HSF/WLCG Workshop

- Caterina is offline today, but happy to start the discussion on progress with logistics, program... if we want a dedicated kick-off meeting that we then summarize, we could do next Thu in the HSF slot?
    - Will poll on coordination list
    - We need to setup an IOC

### Pre-CHEP, Analysis Systems: From Future Facilities to Final Plots (2-3 November)

- Event is now very well planned
- Just putting the finishing touches to the interactive sessions to try and get these to go smoothly
    - All topics have confirmed *animators* to help the discussions
    - We will try to have group 'coordinators' (someone who guides the smaller group writing process and discussion)
    - We will circulate information shortly to all participants so that people know what to expect

### Latin American Workshop on Software and Computing Challenges in HEP (Mexico, Nov 20-23)

- Good attendance expected (32 people registered): Latin American PIs, international speakers, students 
- Workshop URL <https://indico.cern.ch/event/813325>
- Giving final touches to the agenda
- We are missing three important topics/speakers:
    - Detector simulation (Pere, any progress identifying a speaker? HSF simulation converners consulted, posibility of a CERN speaker)
    - Reconstruction (IRIS-HEP will support travel if speaker is US-based). D. Lange, P. Elmer, G. Watts trying to find a suitable speaker from an NSF-funded institution. Alternatively, Giuseppe Cerati is available and willing to do it.
    - "HPC lanscape for science applications". We are trying to get someone from Oakridge. Not clear we will succeed. Ideas?
- Everyone: you still have time to register and attend! Excellent opportunity to network with Latin American collaborators.

## AOB

- We experimented with switching to CERN's collaborative Markdown editor, CodiMD, for the meeting minutes this week
    - More convenient to write notes in the format needed by the website than to have to convert from Google Docs
    - Unfortunately it seems that lightweight accounts cannot edit these documents on the CERN service
    - Options:
        - Get CERN to allow lightweight editing
        - Switch back to Google Docs
        - Use the CodiMD demo service, e.g. with a [note like this one](https://demo.codimd.org/COseSwVnQRuYOAWpHC756Q?both)
            - Notes can be set to be editable by anyone at all (freely) or by logged in people (editable) - to login a GitHub account can be used
    - Nikos (CERN IT): want to understand the needs
        - In a nutshell, we have HSF people who do not have full CERN accounts, so we do need something that everyone can contributed to
        - Federated identity is advancing fast - eduGAIN would be an option, as all of our people should have institutional credentials of some kind

- Next coordination meeting...
    - CHEP is very soon, do people want to have a meeting on 31 October? Or wait till afterwards, 14 November
    - Agreed next meeting is after CHEP
        
