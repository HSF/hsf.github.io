---
title: Petabyte-Scale Cloud Storage File Manager
layout: gsoc_proposal
project: CERNBox
year: 2018
organization: CERN, AARNet, ownCloud
---

## Description

[CERNBox](http://cernbox.web.cern.ch) is a cloud storage synchronisation service
for CERN users: it allows syncing
and sharing files on all major mobile and desktop platforms (Linux, Windows,
MacOSX, Android, iOS) aiming to provide offline availability to any data stored
in the [CERN EOS](http://eos.web.cern.ch) infrastructure. 

CERNBox is based on ownCloud, a cloud sync and share platform written in PHP
following a Model-View-Controller architecture sofware pattern. In the last
months the service started an architectural migration from a monolithic architecture to
microservices. The monolithic-based application was providing different
functionalities: access to storage, sharing of files, authentication,
authorization and also the web user interface. The service is under a heavy 
re-design, moving a good amount of logic from the monolithic to microservices to
improve agility and scalability.

This project aims to provide a prototype of a new web UI for CERNBox that will
provide an immersive user experience. The application will load instantly even
in uncertain network conditions and re-engage users thanks to push notifications.

## Task ideas
- Development of a Web UI using Vue.js and modern JS libraries to create a PWA
  with offline capabilities and resilency to slow networks (resuming of uploads,
local manipulation of files, etc).
- Development of a server in Go programming language to support the Web UI
  (CORS, WebSockets, GraphQL...).
- Perform tests with the real production service at CERN.

## Expected results
Working web application that can manage the files stored in CERN EOS
using the ownCloud Synchronisation Protocol based on WebDAV.

## Requirements
Javascript, HTML, CSS3, Vue.js, Golang

## Mentors
  * [Hugo Labrador](mailto:hugo.gonzalez.labrador@cern.ch)
  * [Michael D'Silva](mailto:michael.dsilva@aarnet.edu.au)
  * [Thomas Müller](mailto:deepdiver@owncloud.com)

## Links
  * [CERNBox](https://cernbox.web.cern.ch/)
  * [CERN EOS](https://eos.web.cern.ch/)
  * [Vue.js](https://vuejs.org/)
  * [Progressive Web Applications](https://developers.google.com/web/progressive-web-apps/)
  * [Golang](https://golang.org/)
