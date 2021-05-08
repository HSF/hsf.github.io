---
title: WLCG-HSF Workshop in Naples
author: Graeme Stewart
layout: newsletter
---

The [WLCG-HSF joint workshop](https://indico.cern.ch/event/658060/overview){:target="_naples_workshop"}
took place in Naples from 26-29 of March. There was a great deal of interest
in the event, with 211 people registering, far exceeding the size of any
workshop hosted by WLCG or HSF alone. The idea
of tackling the challenges in HEP computing for the next decade *in common*,
struck a real chord with the community.

The workshop opened with Liz Sexton-Kennedy [laying out the big picture of
the HEP science goals](https://indico.cern.ch/event/658060/contributions/2844782/attachments/1622746/2582912/ScienceGoalsWLCG-HSFworkshop2018.pdf){:target="_naples_scigoals"},
covering the motivations that drive research in
particle physics, astro-particle physics and cosmology. New facilities for
the exascale era are under construction. For HL-LHC, DUNE, SKA, LIGO and LSST and we need to undertake
major R&D in software and computing to ensure these programmes
are a success.

<div style="text-align:center; padding:25px"><img src="{{ '/images/workshops/naples-ws-liz.jpg' | relative_url }}" alt="Liz opens the workshop's science programme" /></div>

Eduardo Rodrigues then reviewed the [HSF Community White Paper Roadmap](https://indico.cern.ch/event/658060/contributions/2876976/attachments/1622751/2582923/2018-03-26_WLCG-HSFWorkshopNaples.pdf){:target="_naples_cwp"}
that was [published last year](https://arxiv.org/abs/1712.06982){:target="_cwp_roadmap_arxiv"}
and was the major driver for the workshop. He outlined each of the CWP's
chapters along with its major R&D goals and stressed again the approach
of working together, re-characterising "CWP" as *Community Wide Projects*.

After this great introduction to the workshop, and a further review of the important
technology trends and use cases, we continued with a mixture of
plenary and parallel sessions that covered the major areas the community
needs to invest in.

Recognising the large cost of data storage and data management for WLCG,
and anticipating the data volumes of HL-LHC, optimising our storage
systems is an important and challenging area for study. Consolidating storage into larger units,
sometimes called a *data lake*, is one area to study; the anticipation
is that much more use of the wide area network will be made in the future
to deliver data on demand to where it is needed. Successes from the HEP programme,
like the [Rucio data management system](https://rucio.cern.ch/){:target="_rucio"}
could offer a broad engagement with other sciences also facing massive
distributed data challenges. Later technical sessions dived into the details.
There will be a strong coupling to how we can actually characterise
and measure the effectiveness of our workloads on our grid infrastructures,
which the two sessions of the *Performance and Cost Modeling* group looked
at. There will be a lot of follow up to define the real R&D goals as well
as the way to measure success in such a complex coupled and large-scale
system. The *Workload Management* teams look to be involved there too
as the data processing frameworks are a key actor here. Our current systems
are rather diverse, but there are many shared goals.

In addition to these technical developments, using our large distributed computing
systems securely and evolving how we authenticate and responding to threats
was discussed in the *Security* session of the workshop.

The challenges of processing data in heterogeneous resource clusters were laid out
at the beginning of the *Frameworks and Infrastructure* session, before two presentations
from frameworks (ALFA
and [CLARA](http://claraweb.jlab.org/clara/){:target="_naples_clara"}{:data-proofer-ignore=""}) implementing a design that addresses that very
challenge. How to evolve the other frameworks used across the HEP experiments
was a discussion that continued in the parallel session, where the group
plans regular meetings and a follow up at CHEP. Even the tricky question
of using new languages, outside our comfort zone of C++ and Python, was
discussed, generating lively discussion.

<div style="text-align:center; padding:25px"><img src="{{ '/images/workshops/naples-ws-group-photo.jpg' | relative_url }}" alt="Group Photo" /></div>

In the analysis domain, where workloads are far more diverse than for organised
production activities, there are many interesting developments to follow-up.
Systems like [SWAN](https://swan.web.cern.ch/){:target="_naples_swan"} have had success in bringing notebook technology to
HEP analysis. The SWAN team now plans R&D to scale up to future challenges. In
the meantime, data science tools like Apache Spark achieve a
scale and ease of use which is admirable and our community would like
to emulate, albeit that this is much harder to achieve with HEP
analysis data. There was a fascinating talk and live demonstration of the Dask
system for cluster based data analysis and analytics in the Python ecosystem.
Improvements in *Data Preservation* practice might well also link into
these new, easier to capture, analysis workflows.

Back at the production end of HEP, where data is taken from the detector
and reconstructed, we heard about the use of FPGAs to perform surprisingly
complicated reconstruction tasks in the LHCb RICH. Advances in making such
devices easy to program offer the prospect of more wide-spread use
of this technology in the future. Looking at other reconstruction challenges
modern hardware could be used more efficiently if the right algorithms
are found; that might include replacing some traditional programmed
solutions with *machine learning* that can usually run well on
wide vector registers, multiple CPU cores or even GPUs. That challenge might also be
faced more effectively in common through the use of community toolkits,
such as VecCore, that help code adapt to the changing hardware landscape.
An intense discussion about the strategy to be used here, and how much specific HEP solutions
are really required, took place and typifies many of the open questions
our R&D programme needs to address.

There were two full sessions dedicated to the event simulation domain.
Producing events with better underlying physics is needed for both
HL-LHC and the intensity frontier programs, where accuracy of understanding
rare processes is a key to success. In addition, there is a need to speed
up simulation. This takes a few forms, such as better use of current hardware,
tested via the GeantV R&D line, and the use of approximate techniques that reproduce
complex processes more cheaply. Machine learning again looks very promising
here, particularly for calorimeter simulation. Past fast simulation efforts
have been very detector specific so the challenge is how to make faster
techniques more generic, including the process of training networks and
performing validation. The community is very active here and a vigorous
and diverse R&D is underway.

Work on event displays, a key part of *Visualisation* in HEP saw interest
in consolidation and starting common projects to share best practice and
ideas.

The Software Development session reviewed progress made by the
HSF's [Packaging Working Group](/activities/packaging.html){:target="_naples_packaging_wg"}. A common
solution here will be of great benefit to our R&D projects in the future
as it will allow a wider base of users to more easily test early
releases. A decision was also made to consolidate information and best
practice on performance monitoring and tooling, which will help developers
across the field.

Helping establish best practice for development is one part of the training
challenge our community faces. Ensuring that our software is well written
and tested is a key part of making code more sustainable for experiments
with multi-decade lifetimes. The training session gathered speakers
involved in many of the community's training areas, in experiments and
from dedicated schools, and there was discussion about the best way to address the
needs in the future. Agreeing that a solid base was the best place
to start, the group will try and ensure that as many basic training needs
are satisfied in common. Contributions to training should be recognised
as a part of the career profile of our developers, but long term career
prospects remain a concern, as with many other areas in HEP.

<div style="text-align:center; padding:25px"><img src="{{ '/images/workshops/naples-ws-banquet.jpg' | relative_url }}" alt="Well fed at the banquet" /></div>

Opening the final session of the workshop was
[a talk from Anna Scaife](https://indico.cern.ch/event/658060/contributions/2940455/attachments/1625101/2587580/WLCG-180329.pdf){:target="_naples_ska"}
from the Square Kilometre Array Telescope and AENEAS projects. This is
one of the other sciences facing a data deluge in the future and there
can be a very healthy relationship with HEP, which has been recognised
in the establishment of an MoU with CERN and WLCG.

That set the scene for conveners reviewing their sessions and pointing
the way to the R&D which is needed in the next years. Common projects
for development and plans were presented. There is much still to define
and a lot of work that we still need to do, but the workshop was a
great step forward. Feedback from the attendees
highlighted the success of the event, particularly in the way that
it brought the software and computing communities together to encourage
useful discussion and fruitful interaction.

Overall the workshop was a great success and there is clearly enthusiasm for
repeating it. That will be the next community wide checkpoint for
our *software upgrade* R&Ds.
