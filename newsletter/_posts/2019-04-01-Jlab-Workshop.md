---
title: HSF-OSG-WLCG Workshop at Jefferson Lab, HOW2019
author: Graeme Stewart
layout: newsletter
---

The annual [HEP Software Foundation
workshop](https://indico.cern.ch/event/759388/){:target="jlab_agenda"} happened
this year in [Jefferson
Laboratory](https://www.jlab.org){:target="jlab_webpage"}  from the 18th to 22nd
of March. This year we had the opportunity to join forces again with the
Worldwide LHC Computing Grid (WLCG) community and the  US Open Science Grid
(OSG). Almost 250 scientists, from LHC, HEP and non-HEP communities joined the
meeting.

On the first day we opened the meeting with an excellent introduction to JLab
from lab director Stuart Henderson and an overview of JLab computing and
software from Raffaella De Vita. That was followed by plenary talks from the LHC
experiments, other HEP experiments and many non HEP communities, including the
next generation US nuclear physics experiment, the Electron-Ion Collider. That
set the stage for the computing and software challenges we face in data
intensive science for the next decade.

<div style="text-align:center; padding:25px; float:left">
<img src ="/images/workshops/jlab-group.jpg" alt="JLab Workshop Group Photo" />
<br>Workshop Participants. Photo &copy; DOE Jefferson Laboratory
</div>

The theme of working more closely with other sciences was underlined by the
discussion on the *Evolution of the WLCG Collaboration* on Monday afternoon.
Sharing an infrastructure for big data sciences, building on what we know and
already have, received wide support, but the details of how to manage this, for
all communities, need to be worked out.

<div style="text-align:center; padding:25px; float:right">
<img src ="/images/workshops/jlab-plenary1.jpg" alt="JLab Workshop Group Photo" />
<br>Plenary Discussions. Photo &copy; DOE Jefferson Laboratory
</div>

Common sessions for HSF and WLCG on Tuesday looked at the evolution of
technology - processors, storage and networking - and how HEP is managing to
make use of HPC facilities, something that is a growing trend. As HPCs equip
themselves massively with compute accelerators this led very naturally to the
afternoon HSF session on *Software for Accelerators*. These devices are very
different from CPUs, for which we have written most of our software for up to
now, and pose serious challenges for developers. Integration with CPU frameworks
and finding the best way to maintain code for a heterogeneous future were among
the topics where the HSF will continue to work to identify prototypes and share
best practice. ALICE showed how they were using GPUs to achieve the required
throughput in Run 3. LHCb, who also face the stiff test of increased throughput
in Run 3,  is actively doing R&D work on GPUs and presented encouraging results.

Wednesday and Thursday saw the time of the HSF Working Groups to organise
their sessions. Our three new working groups were the stars of the show and
the quality of the sessions they organised were a testament to how much
good work and preparation has been done since the start of the year.

[*Detector Simulation*](/workinggroups/detsim.html){:target="wg_sim"} looked at
everything from physics improvements for the future to the speed boosts that we
need and how we can get them. The GeantV vectorisation R&D presented important
results and the approximate methods for fast simulation were discussed,
including progress in using machine learning.

[*Data Analysis*](/workinggroups/dataanalysis.html){:target="wg_ana"} presented
a summary of what we learned from their topical workshops, with new approaches
for the future. Declarative analysis is being explored in many R&Ds now, and
given the uncertainty in computing architectures for the future, this is a topic
worth investigating.

[*Reconstruction and Software
Triggers*](/workinggroups/recotrigger.html){:target="wg_reco"} looked at the
increasing tendency to produce analysis quality output close to the detector,
both in time and in space, so called *Real Time Analysis*. That touched again on
integrating compute accelerators, such as FPGAs as a way to do complex inference
within budget.

<div style="text-align:center; padding:25px; float:left">
<img src ="/images/workshops/jlab-RTA-2.jpg" alt="JLab Workshop Group Photo" />
<br>RTA Presentation. Photo &copy; Caterina Doglioni
</div>

Many of our other HSF working groups also organised sessions. [*Education and
Training*](/workinggroups/training.html){:target="wg_train"} is still a major
challenge for the community. A survey of what the training needs are for HEP
provides valuable input for how we organise schools and training in the future.
The LHCb StarterKit programme continues to shine as an example of bottom-up
training that is an inspiration for many other experiments.

The [*PyHEP*](/workinggroups/pyhep.html){:target="wg_pyhep"} group organised a
session that explored our links with the wider Python community, with an
emphasis on toolset approaches where different tools mesh together to form the
required pipeline. There was also a presentation from outside HEP, with Jonathan
Helmus from Anaconda introducing the numba Python JIT and the Conda package
distribution. In the latter our own community has contributed ROOT on Linux and
OS X platforms, which is already very popular.

The theme of packaging was touched on again in the [*Software Development
Tools*](/workinggroups/softwaredevelopertools.html){:target="wg_swtools"}
session. The HSF Packaging WG presented solutions that support the wider science
community and look like a good bet for the future. Closer to the code-face,
presentations on profiling and static analysis provided developers with good
advice about the best tools to use.

On Friday the sessions turned back to plenary mode and we heard from projects
being funded to provide the investment in software and computing that we so very
much need. It was therefore very appropriate to announce that the HSF Community
White Paper Roadmap was finally
[published](https://doi.org/10.1007/s41781-018-0018-8){:target="cwp_roadmap_csbs"}
in *Computing and Software for Big Science* during the week of the workshop.

That led us very neatly to a closing talk from JLab's Amber Boehnlein, on
her thoughts about the future of computing the field. Amber was the main
local organiser of the workshop and we were very happy to warmly thank
her and the rest of the team on a job well done. The dinner we enjoyed in the
local Mariners' Museum was greatly appreciated and offered a great backdrop
for continued discussions. We all enjoyed the early
Spring meeting at JLab and already look forward to next year's event.

<div style="text-align:center; padding:25px">
<img src ="/images/workshops/jlab-dinner.jpg" alt="JLab Workshop Group Photo" />
<br>Dinner in the Mariners' Museum. Photo &copy; DOE Jefferson Laboratory
</div>
