---
title: "CERNBox: Bring Your Own Application"
layout: gsoc_proposal
project: CERNBox
year: 2019
organization:
 - CERN
 - ownCloud
 - AARNet
---


## Description

CERNBox is a sync and share collaborative cloud storage solution at CERN used by more than 16K users
and storing close to 7PB of data. The service has evolved from being a platform providing sync and share 
services to a collaboration hub which empowers end-users to perform work collaboratively every single day. 

Collaboration happens thanks to the integration of the open source cloud storage 
sync and share (CS3) platform ownCloud and with a variety of application providers 
like Office 365, OnlyOffice and SWAN. Unfortunately, current
integrations with different application providers are difficult to 
be re-used across platforms and require a huge development effort to achieve the desired integration.

Since the move to cloud based services the user freedom was lost.  The users do not have anymore the possibility to choose the applications they want to use to perform their job; it is the site administrator who decides for them. The goal of this project is to provide a mechanism using a well-defined communication protocol to integrate any collaborative service with the ownCloud platform. For such purpose, the student will leverage on the existing CS3 APIs created at CERN and will focus on the integration of the new ownCloud Web interface (code-named Phoenix) with the CERN REVA platform using Google gRPC and Google Protocol buffers technologies.

## Task ideas

- Development of a Phoenix settings application (client-side) to associate different mime types or file extensions with an application provider
- Definition of a settings/user preferences CS3 API  in Google ProtocolBuffers
- Implementation on the REVA platform of the settings API using gRPC
- Definition of a Collaboration CS3 API for integration between ownCloud and Application Provider.
- Reference implementation of a Phoenix App and Application Provider related with HEP (Job submission viewer, ROOT viewer, ...)

## Expected results
We expect the end deliverable to be a collection of two Phoenix applications (User Preferences App and Reference Collaborative App)
with the corresponding server-side implementations in REVA using the CS3 APIS. The reference application will be related to HEP
activities, like a Job submission viewer or a ROOT file viewer. This HEP-related application will be used as the example app to enable
other people to develop any CS3 API certified application to boost their productvitiy.
The deliverable will be tested on two sites: CERN and AARNet

## Requirements
Javascript, HTML, CSS3, Vue.js, Go

## Mentors
  * [Hugo Labrador](mailto:hugo.gonzalez.labrador@cern.ch)
  * [Michael D'Silva](mailto:michael.dsilva@aarnet.edu.au)
  * [Thomas Müller](mailto:deepdiver@owncloud.com)

## Links
  * [CERNBox](https://cernbox.web.cern.ch/)
  * [CERN EOS](https://eos.web.cern.ch/)
  * [Phoenix](https://github.com/owncloud/phoenix)
  * [Go](https://golang.org/)
  * [Google gRPC](https://grpc.io/)
  * [Google Protocol Buffers](https://developers.google.com/protocol-buffers/)
