---
title: "HSF Packaging Group Meeting #14, November 15, 2017"
layout: default
---

# HSF Packaging Group Meeting #14, November 15, 2017

#### *Present*: Ben Morgan, Chris Green, Dario Menasce, Graeme Stewart, Patrick Gartung, Martin Ritter, Emil Obreshkov, Javier, Rafal, Guilherme

#### [Indico Agenda and Presentations](https://indico.cern.ch/event/678307/){:target="_hsf_packaging_14"}

## Introduction

* Next meeting on the 29th November
  * Graeme has booked room 40-R-D10 at CERN.
* Call for volunteers to give talks on their projects/experiment needs.
  * Specifically on Use Cases and on the contents of the Test Stack.
* Offer to get external speaker on Portage. Maybe not next meeting but beyond.
* Looking at speakers from ATLAS and CVFMS.

## Test Stack
* Went through the [Google Doc](https://docs.google.com/document/d/1LW8OsTFFA9QwsJ9fASkRoJ2E6Gk3UGnOQIcElCL8UCM)
* Ben M had some discussion with Andrea Valassi that we may want to follow up on (HEP_OSLibs meta RPM to define
  base system).
* Proposed that we maybe start with a reduced package std - [notes taken directly in the document](https://docs.google.com/document/d/1LW8OsTFFA9QwsJ9fASkRoJ2E6Gk3UGnOQIcElCL8UCM).
* Dario - we do need to foresee scaling up the complexity.
* We anticipate that individual experiments will build their own stacks - our main goal is to provide a tool to do that with ease and flexibility.
* ABI incompatibilities we will need to be capable of dealing with, but don’t need to worry too much about it right now. (Chris - clang is definitely having issues in the last few versions).
* Patrick - we have the HSF spack repo so most of these should be covered (some were upstreamed). Guilherme thinks most of this is also described in portage.
* Deliverables:
  * build system into a container would be a first step.
  * Ben M - demonstrate from scratch source/binary install

## Use Cases for Packaging
* Went through the [Google Doc](https://docs.google.com/document/d/1h-r3XPIXXxmr5tThIh6gu6VcXXRhBXtUuOv14ju3oTI)
* Graeme motivated Use Cases
  * [HSF Packaging Tech Note](http://hepsoftwarefoundation.org/notes/HSF-TN-2016-03.pdf) enumerated required
    features but not so clear on the use cases that lead to these.
  * Not much about on installation and runtime use cases.
  * Some offline discussion with WG/users on the above to get started.
* Draft [Google Doc](https://docs.google.com/document/d/1h-r3XPIXXxmr5tThIh6gu6VcXXRhBXtUuOv14ju3oTI) split
  into sections to cover
  * Build: how the package is built from source into binary
  * Install/Deployment: how/where the binary products are distributed for end use
  * Development: how a user sets up their environment to use the products
* Discussion:
  * Item 3.c (incremental builds) in Build section considered very important in LHCb and ATLAS.
    Example use case(s) of reusing both system packages and packages from another "layer",
    in this case the LCG stack.
  * Patrick - similar in CMS, but more use of rpms to define reuse
  * Suggested that implementing a GUI to track which recipes were used would be useful
  * Comment that containers could help to define a runtime environment.
  * Additional discussion mentioned issue of "one container per release" leading
    to duplication. Possiblility to mount local or other container filesystem in container
    might mitigate this.
  * Question on how to handle Debug symbols in a package stack. Comment that traditionally
    there's a separate stack of Debug packages, but does duplicate things. Should
    look at possibility of stripping Debug symbols and storing somewhere, as Linux
    distros do.
  * Call for input and comments on [Google Doc](https://docs.google.com/document/d/1h-r3XPIXXxmr5tThIh6gu6VcXXRhBXtUuOv14ju3oTI)

## AOB
* [Next meeting](https://indico.cern.ch/event/681894) in 2 weeks, 29th November.
* Guilherme - could give live demo of how portage could handle topics discussed today.
* Link to paper on use of [Gentoo Linux and Portage in Neuroscience](https://zenodo.org/record/269626)

