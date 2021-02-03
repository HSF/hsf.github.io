---
project: CERNBox
title: Runtime plugin ecosystem support for OCIS
layout: gsoc_proposal
year: 2021
organization:
  - CERN
  - AARNet
  - ownCloud
---

## Description
[CERNBox](https://cernbox.web.cern.ch/cernbox/) is a sync and share collaborative cloud storage solution at CERN used by more than 37K users and storing over 12PB of data. CloudStore is ... that is great for science down-there ...

CERNBox and CloudStor are based on the ownCloud open source software. The new flagship product from the company is codenamed OCIS (ownCloud Infinite Scale). The new platform relies on the CERN originally developed Reva framework to connect to storage and application providers. Reva enables OCIS to connect to arbitraty storages and collaborative applications by extending it with plugings. The current plugin mechanism requires to re-compile the source codebase to add new pluggable functionality to the already ecosystem.

The aim of this project is to add runtime pluggability to the framework to accelerate the development experience at AARNet, ownCloud and CERN to enable a fast integration of well-known applications (RootJS, FileSender, ...) in the new ownCloud platform.


## Task ideas

* Study how runtime plugins are created and packaged in the the creation and packaging of runtime plugins the in the Traefik project 
* Complement the build-time plugings with runtime support using the Go Yaegi interpreter.
* Migrate an existing build-time plugin to the new runtime model


## Expected results
We expect at the end of the deliverable that pluggins can be added at runtime just pointing to a github repository containing the Go module.


### Requirements
* Go, GRPC, Protocol Buffers

### Mentors
* **[Ishank Arora](ishank.arora@cern.ch)** CERNBox
* [Hugo Gonzalez Labrador](hugo.gonzalez.labrador@cern.ch) CERNBox
* [XYZ](xyz@test.com) AARNet
* [XYZ](xyz@test.com) ownCloud

## Links
  * [CERBox project](https:/cernbox.web.cern.ch)
  * [OCIS project](https://owncloud.github.io/ocis/)
  * [Reva project](https://reva.link/)

