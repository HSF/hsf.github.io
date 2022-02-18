---
title: Etherpad plugin as a ScienceMeshDocs editor
layout: gsoc_proposal
project: CERNBox
year: 2022
organization:
  - CERN
  - WWU
  - ScienceMesh
---

## Description

[CERNBox](https://cernbox.web.cern.ch) is a sync and share, collaborative cloud storage solution built at CERN on top of EOS. The service is used by more than 37K users and stores over 15PB of data. CERNBox has responded to the high demand in our diverse community to an easily and accessible cloud storage solution, which provides integrations with other CERN services for Big Science: visualisation tools, interactive data analysis and real-time collaborative editing. For the latter, a number of applications have already been integrated, by leveraging the [WOPI](https://docs.microsoft.com/en-us/microsoft-365/cloud-storage-partner-program/rest) open specifications.

[ScienceMesh](https://cs3mesc4eosc.eu) is an emerging pan-European federated cloud infrastructure, which aims at bringing together several sync and share platforms across Europe. In the context of ScienceMesh the integration of CodiMD has been demonstrated through WOPI _bridge_ extensions.

The goal of this proposal is to implement an [Etherpad](https://etherpad.org) plugin that would leverage on the CS3 WOPI server _bridge_ extensions and allow storing Etherpad files in sync & share storages connected in ScienceMesh. Particular focus is to be put on collaborative scenarios across federated sharing. Etherpad is a popular real-time collaborative editor that features an API and a rich ecosystem of plugins.

As the project is expected to deal with the [CS3 WOPI server](https://github.com/cs3org/wopiserver), it could be extended to include unit-testing the _bridge_ extensions as well as integrating the WOPI validator test suite provided by Microsoft.

## Task ideas

* Analyse the Etherpad plugins system and APIs, and identify the operations required to fetch/push documents 
* Implement the connector in Etherpad and in the CS3 WOPI server
* Test the integration, possibly writing appropriate unit tests for the WOPI server
* Document the Etherpad connector and contribute it upstream

## Expected results
By the end of GSoC 2022 we expect an Etherpad plugin that can connect to CS3-compatible sync&syare systems.

## Evaluation tasks

Interested students can contact Giuseppe (see contact below) to ask questions and for an evaluation task.

## Requirements

* Mandatory
  * JavaScript, Node.js
  * Linux, Git, Docker
* Basic understanding
  * Python 3
  * gRPC and Protocol Buffers
  * HTTP REST APIs

## Mentors

* **[Giuseppe Lo Presti](mailto:giuseppe.lopresti@cern.ch)** (CERN)
* [Daniel Müller](mailto:daniel.mueller@uni-muenster.de) (WWU)
* [Gianmaria Del Monte](mailto:gianmaria.del.monte@cern.ch) (ScienceMesh)

## Links

* [CS3 WOPI server GitHub](https://github.com/cs3org/wopiserver)
* [CS3 Reva GitHub](https://github.com/cs3org/reva)
* [Etherpad GitHub](https://github.com/ether)
* [ScienceMesh](https://sciencemesh.io)
