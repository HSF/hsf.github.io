---
title: Third HSF Workshop
author: Michel Jouvin
layout: newsletter
---

# Third HSF Workshop (May 2-4, 2016)

![Workshop Group Photo]({{ site.baseurl }}/images/lal_workshop.jpg){:height="400px" width="600px" .centered-image}

The HSF had its third workshop at LAL (Orsay, France) on May 2-4, 2016. It 
was well attended (70 people) representing many different laboratories, 
universities and institutions (~30) from both sides of the Atlantic, 
involved in different experiments (LHC, BELLE II, Intensity Frontier...). 
We were happy to see a lot of new faces!
The [Agenda](https://indico.cern.ch/event/496146/timetable/) was a mix 
of (lively!) general discussions and topical/hands-on sessions. Live 
notes of these discussions are 
[available]({{ site.baseurl }}/organization/2016/05/04/Workshop-summary.html). 
This newsletter summarizes them.

![HSF Logo]({{ site.baseurl }}/images/hsf_logo_angled.png){:height="100px" width="150px" .centered-image}

One of the breaking news is that the HSF now has a logo! Thanks to 
J. Lingemann, the winner of the logo contest, and to all of you who took the
time to submit a logo proposal.


## Projects and Project Support

We had a session dedicated to some of the HSF SW projects and related initiatives
* [AIDA2020 WP3](http://aida2020.web.cern.ch/activities/wp3-advanced-software): the software work package of the EU-funded project about detector R&D. AIDA2020 expressed that they want to put their development under the HSF umbrella.
* [Next Generation Conditions Database](https://github.com/HSF/PhysCondDB): a project started jointly by CMS and ATLAS that is becoming attractive to others. This project benefits from the collaborative spirit resulting from the HSF.
* The HEP Software and Computing Knowledge Base: this is a project started by the HSF to facilitate software sharing. It is easy to use and allows crosslinking of software, experiments, organisations, events... **Register your favorite software!**
* [WikiToLearn](https://en.wikitolearn.org/Main_Page): a new platform allowing the sharing and improving of training materials through collaboration between authors and users. Developed in Italy (University of Milano), its developers are committed to making it useful for, and usable by the HSF.
* [DIANA-HEP](http://diana-hep.org/) (Data Intensive Analysis for HEP): a NSF-funded project to promote common analysis tools for data intensive research in HEP, using ROOT at its core. This US project shares many goals with the HSF.


Helping software projects is the main goal of the HSF. During the last year, 
the HSF has produced a Best Practices document (currently a [Technical Note draft](https://github.com/HSF/documents/blob/master/HSF-TN/draft-2016-PROJ/draft-HSF-TN-2016-PROJ.md))
and implemented it in a [Project Starter Kit](https://github.com/HSF/tools).
 This year, the HSF wants to continue its efforts on project support, focusing
 on helping projects get more visibility, and promoting the interoperability 
 of software projects.

In addition, a new activity is starting: peer-reviews of software projects. 
The first review has been requested by GeantV, and will take place this October.


## Software Packaging

One of the topical sessions was about packaging. Software build tools and 
packaging are a key piece of software interoperability. As we cannot 
envision all of the projects adopting the same tools, the effort has concentrated 
on a review of the existing tools, and an attempt to identify a tool with the 
 greatest potential as an integrating layer. One tool from the HPC world, 
 [Spack](https://spack.io/), generated a lot of interest. Some people tried to experiment with it in various 
 contexts in the past few months.  The workshop session facilitated an in-depth 
 dicussion about Spack's potential and it's limits. We reached consensus about how to move forward.  We will continue to collaborate with the Spack developer community.  When the features identified by the working group and documented in our technical note are available we'll start to recommend it to new projects and facilitate adoption by older projects.

See the [Packaging WG]({{ site.baseurl }}/workinggroups/2015/11/04/packaging.html) section on the web site for more details.


## Learning from Others

We got three interesting presentations from non-HEP projects with goals similar
to the HSF:
* [BioConductor](https://www.bioconductor.org/): an open-source project portal associated with an ecosystem of tools for bioinformatics
* [Netherlands eScience Center (NeSC)](https://www.esciencecenter.nl/): a team of computing experts working with a diversity of scientific fields, building a common expertise that can benefit all of them
* [Depsy](http://depsy.org/): a project and platform to promote credit for software in science. Currently focused on Python and R ecosystems, it analyses software packages and sources to identify contributions and make visible people's contributions even when this is made of "small contributions" to many projects.

## Machine Learning

The second large topical session at the workshop, was divided into presentations 
about ML activities going on in the community, and a 3 hour RAMP (Rapid Analysis 
Machine Learning Prototype) session. Many topics were covered, including:

* Summary of OpenLab Workshop (industry)
* Machine Learning Challenges (e.g. HiggsML)
* Deep Learning
* TMVA updates
* Common Tracking Software (ACTS)

This activity is developing very quickly in the community, and a few months ago 
an Interexperiment Machine Learning (IML) forum was created. The IML forum 
intends to coordinate its activity with the HSF and will be the entry point to
any ML activities in the HSF.

## Software Performance

THe third topical session was devoted to sharing experience and questions
about software performance, in particular the challenges of using efficiently 
the new hardware with their requirement of large-scale parallelization. There 
were reports from the LHC experiments, GeantV, ROOT, Art/LArSoft and 
astrophysics simulation. The discussion tackled several questions, in particular:

* What hardware to focus on? Commodity vs. GPU vs. HPC
* Do we understand what to expect in terms of future hardware?
* Can we decouple low-level optimization (experts) from high-level code (physicists) via libraries?
  * Interesting input from Astrophysics

We are still far from definitive answers to these questions. There was an 
agreeement that this topic is of primordial importance for the future, and 
should become more visible in the HSF. The new Software Technical Evolution 
forum (a follow-up for the Software Concurrency forum) will be in charge of 
convening this activity inside the HSF.

## Initiatives for the Future

### Community White Paper

The HSF demonstrated some initial collaborative activities but to address 
the challenges ahead (e.g. HL-LHC) it needs more and dedicated resources. 
To convince funding agencies, and get a chance to obtain these resources, 
some US collegues launched the idea of a Community White Paper that will 
contain a description of the challenges ahead of us, with a roadmap to address
them. The idea is to build for computing something similar to the P5 process 
for HEP experiments in the US. In fact, the LHCC committee (that reviews the 
LHC experiments computing and WLCG infrastructure) recently asked the WLCG to 
prepare a HL-LHC computing TDR in a similar timeframe. Both processes could 
benefit from each other.

There was a consensus that this was a high priority activity for the coming year. The proposal is to hold a series of HSF-branded workshops and come up with a Community White Paper and roadmap by mid-2017. We are currently discussing the possibility of a kick-off meeting around CHEP (probably either colocated or end of October at CERN).

### Software and Computing Journal

Some German colleagues, supported by Springer, proposed the idea of creating a journal dedicated to Data Intensive Science Sofware and Computing. Currently, there is no such journal, making it difficult to publish articles related to the computing aspect of our science (this is suitable neither for physics journals, nor for computer science journals). The goal is to have a refereed, abstracted and indexed journal that could acoomplish the following goals:

* Authoritative and central reference archive
* Help with career paths
* Do not restrict to HEP strictly: open to Data-Intensive Physics. Fields organized as large collaborations around large-scale experiments
* Scope should cover all aspects of computing: from infrastructure to data analysis…

The plan is to have a continuous publishing, without any paper issue or volume.

There are still many "details" to sort out but the idea was well received, and the HSF is ready to help in moving forward with it.


## HSF Next Steps

The workshop demonstrated that the HSF is well alive with significant 
progress accomplished in the last year, yielding an increasing motivation.
In addition to the initiatives already mentioned and the follow-up of existing 
activities, the main actions agreed for the coming year are: 

* HSF communication: explore the use of StackExchange, a well-identified open forum, for questions about HEP computing
  * At some point it may become an attractive alternative for (some) mailing-list based forums in HSF
* Increase software project support, develop project peer-review activity
* Look for an official blessing of the HSF by bodies like ECFA/ICFA
* Find some dedicated resources for the HSF work (currently best effort by motivated people on their "spare" time!). A proposal of creating HSF Centers in our laboratories/universities/institutions has been made: this could become visible parts of HSF hosted by various parties.

We also discussed (again!) the possibility of a legal entity to support HSF. Despite not reaching a consensus yet, we agreed to further explore the possibility with funding agencies and lawyers. The general idea was that this entity, if created, should focus initially on IPR management, in a way similar to the Apache Software Foundation, to make possible IPR transfer.

