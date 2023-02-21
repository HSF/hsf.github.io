---
title: CERNBox - Dynamic capabilities for smarter client interactions
layout: gsoc_proposal
project: CERNBox
year: 2022
difficulty: medium
duration: 175
mentor_avail: June-August
organization:
  - CERN
---

## Description

[CERNBox](https://cernbox.web.cern.ch) is a sync and share, collaborative cloud storage solution developed at CERN, used by more than 37K users and storing over 15PB of data.

At the heart of the CERNBox service lies [Reva](https://reva.link/), a middleware framework that provides interoperability between storage and application providers through a universal set of APIs. This allows CERNBox to connect to arbitrary storages and enable collaborative data services and applications at a massive scale.

Clients connecting to the service are made aware of the various protocols and functionalities that are offered by a particular Reva instance. Currently, these are really limited and specified via a configuration file. The goal of the project is to expand the set of such capabilities and infer these dynamically from the enabled services and service drivers. These could also be determined based on the characteristics of the end-user.


## Task ideas

* Gather requirements for which services and corresponding parameters should be advertised.
* Design a new component that integrates into the existing microservice architecture seamlessly and can scale to new requirements.
* Implement this inference mechanism and expose this to the end users via a scalable API.
* (optional) Modify the existing clients to make smarter interactions with Reva based on this new service.

### Expected results

We expect that, at the end of GSOC '22, based on this new service that advertises server capabilities, client interactions with Reva would become smarter, which in turn would reduce the complexity involved with deploying such a system. Documentation of the service and the functionality for other developers is also expected.

## Evaluation Task

Interested students can contact Ishank (see contact below) to ask questions and for an evaluation task.

## Requirements

Go, gRPC, REST, Protocol Buffers


## Mentors

* **[Ishank Arora](mailto:ishank.arora@cern.ch)** CERN
* [Hugo Gonzalez Labrador](mailto:hugo.gonzalez.labrador@cern.ch) CERN
  

## Links

* [CERNBox project](https://cernbox.web.cern.ch)
* [Reva project](https://github.com/cs3org/reva)
