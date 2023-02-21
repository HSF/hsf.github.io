---
title: "HSF Coordination Meeting #229, 12 May 2022"
layout: plain_toc
---

Present/Contributing: Graeme Stewart, Ben Morgan, Kyle Knoepfel, Efe Yazgan, Nicole Skidmore, Allie Hall, Caterina Doglioni, Wouter Deconinck, Paul Laycock, Krzysztof Genser, Michel Jouvin, Stefan Roiser, Liz Sexton-Kennedy, Pere Mato, Serhan Mete, Pete Elmer, Jin Huang, Killian Lieret, Marc Paterno, Mark Neubauer, Michael Hernandez, Daniel Elvira, Valentin Volkl

Apologies/Contributing: Benedikt Hegner, Andrea Valassi, Torre Wenaus, Markus Diefenthaler

## News, general matters, announcements

### POSE Submission

NSF have a funding call for ["Pathways to Open Source Ecosystems"](https://www.nsf.gov/pubs/2022/nsf22572/nsf22572.htm). [A proposal](https://drive.google.com/file/d/1f6h--VlQYekzXJnozuIxN8y4xixc5mCr/view?usp=sharing) has been put together by Pete Elmer, Allie Hall and Carlos Maltzahn, which would develop a strategy whereby the HSF could engage more directly with industry.

A [letter of collaboration](https://docs.google.com/document/d/12lalCI60Sf_6TXZLuK6ACiWogG71iYgelJajWOxpvQ4/edit?usp=sharing) was prepared and was supported by the HSF Coordination group.

The meeting approved support for this.

If funded, this would start January 2023.

### Workshops in 2022

#### Analysis Ecosystems Workshop

23-25 May: <https://indico.cern.ch/e/aew2>

- May 10: 114 registrants, 76 in person, 38 virtual
  - Registration open until Sunday (at least for in-person this would be the deadline)
- Logistics under control
- Preliminary (but reasonably elaborated!) agenda is available
  - Session conveners working to sort out the concrete content of each session
  - Lot of time devoted to discussions, some during plenary sessions, others in parallel sessions (2h per topic)
- We are preparing a [reading list](https://docs.google.com/document/d/1y-Q7g_dq9fApjZ5pqNxErJon5HXeTxbgZbTiFsKumEk/edit?usp=sharing) so that everyone comes to the workshop prepared

#### Detector Simulation on GPU Community Meeting

- HSF Detector Simulation on GPU Community Meeting was held 3-6 May
  - <https://indico.cern.ch/e/simgpu>
  - See the [Live Notes](https://docs.google.com/document/d/1ntMp74hZDFL9-e1YKC44UVPP5-ozxp1r2XIOiUp8nYc/edit) linked on the agenda for questions and discussions
- Productive meeting giving excellent overview of progress, and useful discussions. Many thanks to the organizers and presenters!
  - Good input from a few experiment people, though hope to expand on this going forward.
  - Expect to have working meeting in coming months, likely at CERN, so opportunities for in-person discussion/engagement then.
- AdePT and Celeritas have working simulations of EM showers on GPU!
  - Both as "all on device" and as offload from a larger Geant4 application (using fast simulation hooks or tasks)
- Performance numbers from each project show promise
  - Runs of simple "TestEm3" problem on both single GPU workstations and Summit show
    - AdePT at least as fast on consumer GPU vs 32-core CPU Geant4
    - Runs of Celeritas and AdePT on Summit (OLCF) show 40x speed-up for 1CPU-GPU (V100) versus 7-core CPU Geant4 runs
  - Choice of implementation for workflow/geometry does not change things by more than x2
  - Major bottlenecks however are identified, so avenues for improvement.
  - Developers caution on scale of problems benchmarked so far and given known bottlenecks and functionality still in development, but cause for optimism. No hard blockers on being able to run simulation on GPU identified, though some algorithms might remain bottlenecks due to poor match to GPU architecture.
- Key topics going forward
  - Workflow structure: kernels, track level parallelism across events, hits/scoring
  - Benchmarking: develop shared set of "problems" covering geometry, input events, output data.
  - Request for community feedback here especially on what metrics to use for performance as well as realistic hardware configurations for current/anticipated production systems.
  - Similarly for integration in current/future experimental frameworks/workflows
  - Evolving geometry modelling/navigation codes for GPU is crucial - ongoing discussion/prototyping between VecGeom/ORANGE, input from reconstruction side (ACTS).
- Other discussion/future topics
  - Questions on future evolution of projects towards a single code. Both feel it's not the time to do this, as different development lines still highly useful at this stage, however, end goal is not to end up with the community having to choose between two.
  - Noted that the combination of physics and computational expertise was valuable, and needs to be maintained and the community here supported.
  - Questions/Discussion on future for non-EM physics. Neutrons primary topic here.
  - Whether to look at/revisit simulation algorithms and design/architecture for coming CPU/GPU architectures

### Google Summer of Code / Season of Docs

GSoC - ranked list of proposals has been prepared. Have asked for ~28 slots (basically, all proposals where we have a strong candidate).

GSoD - some credible interest shown in the proposal.

### HSF History Paper

Liz wrote some text into the Overleaf document, following up on Andrea's comment, and notified the list of coordinators. The text is surrounded by a comment with the initials LSK.  So far I have heard back from Andrea that he is satisfied with it, and have had no other comments.

Graeme has added the major contributors to the text, viz. Graeme, Liz and Pete, as contact editors.

Ready to go? Post to arXiv was favoured.

### Talks

Graeme gave talk on ["Sustainability and future of software frameworks"](https://zenodo.org/record/6538707). The talk was well received with FA representatives, including the European Commission, present.

Thanks to everyone that gave inputs.

## Working Group Updates

### Data Analysis

- Not so much news - all busy with EcoSystems workshop preparation
- Resubmitted the MetaData paper (after a delay to get an "authorship form" signed) - will also resubmit Arxiv version

### Detector Simulation

- Next meeting 23rd May on DD4HEP Status, joint with Reconstruction and Software Triggers.
  - Agenda being finalized, but expect a general update plus Q&A
  - <https://indico.cern.ch/event/1146364/>
- Thinking about future meetings, though June/July already quite busy on the community calendar.

### Reconstruction and Software Trigger

- In contact with potential speaker for topical meeting on GNNs for tracking, date in May to be confirmed
  - Related workshop announced to WG: [Graph Neural Networks for Tracking](https://indico.cern.ch/event/1128328/)

### Software Tools and Packaging

- We have been trying to schedule a follow-up to a talk in September, 2020 <https://indico.cern.ch/event/949460> on measurement of build performance from the Acts project. 
  - Scheduling has been very difficult but we seem to be converging (as of email this morning) to the first week of July, but avoiding both the US holiday on July 4, and ICHEP starting July 6. 
  - We have not received confirmation yet from the speaker(s) to make the date certain.

### Event Generators

Past:

- 10th March:     Snowmass Generators Whitepaper
- 24th March:     ATLAS V+jets [(minutes)](https://hepsoftwarefoundation.org/organization/2022/03/24/generators.html)
- 7th April:     Further Sherpa efficiency improvements by Enrico Bothmann  [(minutes)](https://hepsoftwarefoundation.org/organization/2022/04/07/generators.html)
- 5th May:     Neutrino [(minutes)](https://hepsoftwarefoundation.org/organization/2022/05/05/generators.html)

Future:

- 2nd June:     Automating scattering amplitudes with chirality flow - Master thesis - Zenny Wettersten (confirmed)
- June 23    EIC/NP Generators usage - Markus D. (confirmed)
- 7th July:     Event generation with Julia - Uwe (confirmed)
- 1st Sept.:     AI/ML-focussed discussion - Ask Anja Butter for an overview talk for ML for generators following <https://arxiv.org/pdf/2203.07460.pdf>

### Frameworks

- We had a [meeting last week](https://indico.cern.ch/event/1138384/) with a presentation from Mu2e regarding their framework usage.  Somewhat disappointing attendance.  Not sure what to do about this.
- Our [next meeting](https://indico.cern.ch/event/1138383/) will be 25th May, where NOvA will present on its framework usage.
- Nothing scheduled yet for June.

### Software Training

- New Slack channel (migrated from CERN mattermost because of difficulties with non-CERN members). Will add invite to homepage soon. For now: [invite](https://join.slack.com/t/hsftraining/shared_invite/zt-18sa7y3s6-5QuNY0sSnlP6HSNvoFREkg)
- Planning:
  - Carpentries Workshop 13-15th July (Eastern Time): Will call for mentors for last day (HEP specific) soon.
  - Small hackathon for improving matplotlib training module (probably June)
- Ongoing discussion about improving organization (shared folder, note taking, todo tracking)
- C++ course meeting next week + last course post-mortem

## Other Interest and Activity Areas

### General

Next [Compute Accelerator Forum](https://indico.cern.ch/event/1073643/) meeting will be on June 8, with updates on CERN's GPU infrastructure and on SYCL.

---

## AOB

### Zenodo

The ORCID account for the HSF stopped working for managing the HSF Zenodo community. We do still have access via a shared account `hsf-editorial-secretariat` - Graeme, Michel and Eduardo (at least) have the password.

There is 1 pending submission to the HSF community, [*Set of N integers between -30 and 30 with sum and cubic sum up to zero for 4<N<13*](https://zenodo.org/record/5526707). We don't find this too relevant and we don't know the author, so we are minded to refuse it (unless, e.g., the generators conveners think it's worthwhile?).

- Comment was no one thought this was relevant, so we refuse it.

### HSF Mail in Spam?

Graeme has been following this with CERN IT (RQF2007631). The problem is that messages forwarded to `not_junk@office365.microsoft.com` are not appearing in the dashboard that the CERN admins have. Microsoft support has not been great, e.g., suggesting an Outlook plugin (not everyone uses Outlook) that doesn't even work for the CERN servers (as they are self-hosted).

Some hints that forwarding from Thunderbird is working better. We do encourage people to check their `Junk E-Mail` folder and forward email *as an attachment* to `not_junk@office365.microsoft.com`.

The issue is now being escalated by CERN IT.

#### Workaround

Graeme setup shadow lists for the coordination group and WG convener group, viz., `hsf-coordination@cern.ch` and `hsf-wg-conveners@cern.ch`. *No intention to switch to these permanently*, but at least they can be used more reliably to contact people until the problem is fixed.

### GPU Hackathon

Got in contact with one of the <https://gpuhackathons.org> organizers in Helmholtz. Idea came up to organize one of those hackathons at CERN. Question if there is interest from within our community? Please contact [Stefan Roiser](mailto:stefan.roiser@cern.ch) in case.

### CSBS

In a recent Editorial Board for [Computing & SW for Big Science](https://www.springer.com/journal/41781) (CSBS) journal, we got the last update of CSBS growth which is very good, with 2 topical issues in 2021. CSBS is now indexed by most of the main indexes (Astrophysics Datasystem, INSPIRE, SCOPUS...) with generally a very good cite scores that makes attractive to publish in CSBS!

Next milestone is to be indexed by the Web of Science which updates its list of indexed journal in June...

### Next Meeting

Next coordination meeting is scheduled for 9 June (we skip 26 May as it is the Ascension holiday, observed by CERN and many European countries).
