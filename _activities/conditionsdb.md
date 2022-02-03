---
title: "Conditions Databases"
author: "Paul James Laycock"
layout: plain
---

Discussions between Conditions Database experts across several HEP experiments took place as part of the HSF Community White Paper process in 2016/2017, producing a white paper describing best practice for a Conditions Database schema design: HSF-CWP-2017-03 [(arXiv)](https://arxiv.org/abs/1901.05429). That document provides a starting point for continuing cross-experiment discussions.  The level of consensus across the experiments on guiding principles was very encouraging, with agreement that good design features include:

* Loose coupling between client and server using RESTful interfaces
* The ability to cache queries as well as payloads
* Separation of payload queries from metadata queries

Importantly, the group needed to agree on a definition of “conditions data”, concluding that in the context of large scale NHEP computing challenges it is the subset of non-event data used in event-data processing, often using distributed computing resources.  These use cases have strong connections to several other HSF working groups, including 
[Reconstruction and Software Triggers]({{ site.baseurl}}/workinggroups/recotrigger.html),
[Detector Simulation]({{ site.baseurl}}/workinggroups/detsim.html),
[Data Analysis]({{ site.baseurl}}/workinggroups/dataanalysis.html), and
[Frameworks]({{ site.baseurl}}/workinggroups/frameworks.html).
Meanwhile, several of those involved in the CWP work continue to discuss solutions around the topics of Conditions Database use cases and functionality.

----

## Coordination

* Andrea Formica (ATLAS)
* Giacomo Govi (CMS)
* Paul Laycock (Belle II, DUNE, sPHENIX)

[Email the coordination team](mailto:Andrea.Formica@cern.ch, giacomo.govi@cern.ch, laycock@bnl.gov)

----

## Goal

The main goal of this HSF activity is to provide a forum for cross-experiment Conditions Database discussions with as broad an audience as possible.  By first discussing and documenting use cases and their associated functionality, one aim of the group is to then converge on an API specification with a reference implementation.


