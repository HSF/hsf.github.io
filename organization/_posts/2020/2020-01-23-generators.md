---
title: "HSF Generator Meeting #8, 23 January 2020"
layout: meetings
---
# {{page.title}}

*Agenda: <https://indico.cern.ch/event/880274>*

Present: 
- In the room: Andrea Valassi, Stefan Roiser, Efe Yazgan, Markus Schulz, Josh Bendavid
- Remote: Andy Buckley, Duncan Alexander Leggat, Graeme Stewart, Gurpreet Singh Chahal, Holger Schulz, Josh McFayden, Lukasz Kreczko, Olivier Mattelaer, Qiang Li, Stefan Hoeche, Stephen Jiggins, Steve Mrenna, Taylor Childers, Walter Hopkins, Luca Mantani

Apologies: -

## News, general matters (1)

Thanks to Stefan Hoeche, Steve Mrenna and Taylor Childers for their work as co-conveners of this WG in 2018-2019, and welcome to Efe Yazgan as a new co-convenor!

Please feel free to contribute to the live notes of the meeting on codimd!

## Update about MadGraph on GPU (Walter Hopkins)

This is a follow-up to the [talk](https://indico.cern.ch/event/831652/contributions/3511812) by Kyle Fielman at the WG meeting in July 2019, about the Argonne work on MadGraph on GPUs. See also Junichi Kanzaki's [talk](https://indico.cern.ch/event/759388/contributions/3303060) at the HOW2019 workshop in March 2019 about previous work in this area in Japan.

Work has been done mainly on the phase space integration (VEGAS on GPU, aka gVEGAS), not on event generation (gSPRING). So far the matrix element calculation within gVEGAS has not been ported to GPUs.

Event generation is most likely more time consuming overall than phase space integration. A more detailed profiling and verification of that is planned.

There is one postdoc at Argonne working on an ATLAS qualification task on these topics.

Qiang: starting with any specific MadGraph version? Answer: did not get to integrating with MG yet, but plan to use the version used in CMS.

Taylor: there are frameworks like kokkos which are more portable than CUDA. StefanR: we also have a workshop upcoming in April on alpaka, including one day of public training on April 27 (<https://indico.cern.ch/event/858758>), plus three days of hands-on (<https://indico.cern.ch/event/867700>, but this is by invitation only and slots are already full). Walter: could be very interesting for our use case.

JoshMF: will you work also on the event generation (gSPRING)? From an analyser's point of view, integration is the most painful part, but overall the largest time spent is event generation. Walter: apparently gSPRING already exists, but have not obtained Junichi's code yet. 

Andrea: is the ME calculation ported on GPU yet? Walter: it is meant to exist, but have not managed to run it yet. Olivier: plan to work on that.

Andrea: very important work, very good that many people are interested in it, we should take it offline and try to understand how to best collaborate.

JoshMF: is there some training for GPU development? Graeme: following up with Maria Girone in Openlab. Walter: not an expert and doing some learning, it's totally not obvious and sometimes the algorithms need to be changed. JoshMF: should we maybe go another direction, and instead of porting doing a reengineering? Olivier: also just starting on CUDA, but definitely plan to spend some time on this.

Stefan: was difficult last year to get all relevant pieces of MadGraph on GPU together in one place, can this be done? Walter: already put a link there.

JoshB: for the user the integration is the painful process. So working on easier gridpack creation from users is also very important, not just event generation.

Olivier: note that GPU port is at present only conceivable for LO, while for NLO it would be much more complex, due to the need for 1-loop libraries. But e.g. DY+4 jets at LO (which is already a pain for CMS users) would be possible. 

## Machine Learning techniques for MC integration (Josh Bendavid)

Matrix elemnt calculation is the dominant computational cost. A DNN approach increases the integration or unweighting efficiency, hence it reduces the number of matrix element calculations needed.

JoshMF: how hard would it be to integrate this in MadGraph? JoshB: presently working on a future development branch of MG using python, it would be more complex on the present Fortran based implementation. This work is still at the R&D stage.

Taylor: how far away are you from using an actual process, rather than just using some test functions? JoshB: still having some numerical stability issues.

Andrea: does the DNN have an impact on the physical precision? JoshB: as long as the coverage of all the phase space is done correctly in the NN, this should not be an issue.

Andrea: is this portable to any generator like sherpa, not just MG? JoshB: yes, general idea applies to all generators, then the problem is just doing the integration with a specific generator.

## Google Summer of Code projects (StefanR/AndyB)

Stefan: introduction to GSOC. Generally people are very happy with the quality of students.

AndyB: proposing to a GSOC some work on GPU implementation of ME might be a huge thing, it requires supervision from physics experts. Markus: for a summer project this might be too much. Stefan: already doing some profiling could be something. But definitely we would need help from authors. Andrea/Josh: also need some benchmarking suites to start.

Steve: should the mentors be at CERN? Graeme: no, neither mentors nor students are meant to be at CERN, they can be remote.

Graeme: often difficult to attract students, so we should start with why physics is exciting!

JoshMcF: The implementation of HDF5 as replacement for LHEF might be a nice thing to add to Stefan's proposal? This was done for sherpa/pythia8 but it could be done for other generators. Holger: the code which exists is generator-independent.

Graeme: can submit many projects, but you need to have a mentor for each.

JoshMF: volunteers to be a mentor. Thanks!

## News, general matters (2)

### HSF/WLCG Workshop in Lund (11-15 May 2020) - AndreaV

The next HSF/WLCG Workshop will take place in Lund from 11 to 15 May (more information on [indico](https://indico.cern.ch/event/867789)). The agenda is still being prepared. We should expect to give a summary of the WG activities there. We can also organise a parallel session, keeping in mind that Lund is the 'home' of Pythia and many relevant experts on MC generators are based there.

Graeme: can have more than one slot of 90 minutes, could for instance have one slot of talks and one of discussions. JoshMF: yes this is a nice idea. Andrea: focus should be computational aspects.

Steve: will be there in April for the Pythia8 meeting, unfortunately not at the sam etime. 

### Review of the HL-LHC computing strategy (18-20 May 2020) - AndreaV

LHCC have requested a review of High-Luminosity computing for the LHC (see [charge document](https://indico.cern.ch/event/865280/contributions/3645561/attachments/1967531/3271925/HL-LHC-Charge-v3.pdf) attached to the agenda). The first phase is 18-20 May at CERN. Five documents will be requested. **The HSF is in charge of preparing a ~20 page Common Tools and Community Software document, which has to be ready by 1 May**, well before the Lund workshop. The document should cover software directly impacting on resources (**Event Generation**, Detector Simulation, Reconstruction, Data Analysis) and we agreed that each of the relevant HSF working groups takes charge of the corresponding section in the document. The current skeleton of the document is available on [googledoc](https://docs.google.com/document/d/1ai7m7kFyiGgl2tKralJKyPX6rlD9tffU7B6wPj_vpZU/edit).

Draft HSF Timeline:
- Setup document and discuss parameters - January
- Write initial text, roughly 4 pages per software area - February
(Contact with important contributors should be made at this time)
- Circulate to wider community for comments and suggestions - March
(At least one meeting per section should be arranged)
- Finalise text for LHCC - April

**The HSF generator WG should thus prepare ~4 pages of text**. Starting point should be the CWP and the goals laid out there. R&D plans should be outlined (for further scrutiny of the progress by the review panel after 18 months, in the fall 2021).

Graeme: perfectly ok to discuss important things that are not yet being done, and this is maybe very important for generators. Andrea: yes, for instance pointing out importance of computational work on generators, need to attract/keep the right people; also, forecasts of LO/NLO/NNLO needs from a physics perspective.

## ATLAS and CMS event generator accounting (JoshMF and Efe)

### ATLAS

JoshMF: in the past the ATLAS accounting was done in seconds, not HS06 seconds. Have been working on HS06 numbers, will first present them today!

Andrea: so ballpark is that for MC production, 20% ifs generation, 60% is simulation, 20% is reco? JoshMF: yes, an dMC production is around 70% of all of ATLAS time. So generation is around 14% overall.

Stefan: is digitization part of reco? JoshMF: yes it is put together. Efe: if like CMS, then it is very small.

### CMS

In previous results, we had an approximate GEN/SIM split. In the new campaign (since ~September 2019) we now have separate GEN and SIM information because CMS launches GEN and SIM jobs separately. Also, HS06 numbers are now available.

Note that some of the results we gave in the table previously is now lost because the monitoring is only kept for 18 months!

Slide 3: note 4th and 5th line are the slowest. The 4th is MG GEN-only, it is as slow as the 5th that is sherpa GEN+SIM and includes one more jet. So it is a bit surprising.

For ttbar only, in the past we estimated GEN to be 4% of full MC chain, now it is around ~7%. And this number is around 7% to 35% for the different channels.

Steve: are you taking into account the different matching efficiencies? JoshB: yes, in the end, the numbers we get are how many unweighted events we produce.

### Discussion

Andrea, so in summary we should compare for fraction of CPU time for GEN over all time in a MC campaign: 20% for ATLAS, against 7% to 35% for CMS. This is not so different. Then we should try to get an average for all processes. The idea is to get a prediction for a typical year, now and eventually at HL-LHC. Our goal should be to try and get precise numbers, so that we can prioritise where we need to invest to improve generation time, if relevant.

JoshB: aside, note that MINLO is a very slow generator because it recomputes pdfs, so if we add it to the table it would appear very slow.

## AOB

### Common EOS space for ATLAS/CMS generator files (AndreaV)

This is a follow-up to the talk by Kyle Cormier and Javier Fernandez during the [June 27 WG meeting](https://indico.cern.ch/event/821205). Andrea is discussing this with the EOS team in SNOW ticket [RQF1470291](https://cern.service-now.com/service-portal/view-request.do?n=RQF1470291). 

A few points from Kyle:
- File types would be LHE files, HepMC files, or experiment-specific versions there-of (e.g. EVNT files in ATLAS which store data similar to what is found in a typical HepMC file)
- Harder to say is the number of files and how often they will be accessed, and the growth in the next few years
- On the ATLAS side, Kyle's work will be taken over by Mike Fenton

A few open questions from Andrea:
- We need a name for this EOS project, ok for hsf-generators? (there is already an hsf-phoenix space)
- We need a name of a service account for this EOS project, of for hsfgen?
- Is 1TB with maximum 1M files enough?

Gurpreet: mainly working on sherpa in CMS, would be very interested from the CMS side about that.

### Next meetings

Aim for one meeting per month on average, more frequently when needed (e.g. while preparing the Lund workshop and the HL-LHC review).

Possible topics for some of the next meetings:
- Update by JoshMF about reproducible setups to run generators in a configuration representative of the actual ATLAS/CMS use cases?
- Discussion (by Steve Mrenna?) about the HDF5 format for parton level events (this is an HPC friendly replacement for LHE Les Houches Event files, which are in ASCII format)
- Suggestion by StefanH: presentation by Enrico Bothmann of his work on NN integration (see <http://arxiv.org/abs/arXiv:2001.05478> and <http://arxiv.org/abs/arXiv:2001.05486>)
