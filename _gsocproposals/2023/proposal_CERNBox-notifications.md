---
title: Extend and improve the CERNBox Notifications platform
layout: gsoc_proposal
project: CERNBox
year: 2023
difficulty: medium
duration: 175
mentor_avail: June-September
organization:
  - CERN
---


## Description

[CERNBox](https://cernbox.web.cern.ch) is a sync and share collaborative cloud storage solution developed at CERN, used by more than 37K users and storing over 18PB of data.

[Reva](https://github.com/cernbox/reva) is the core of the CERNBox service. It is a middleware framework, providing interoperability between storage and application providers using a universal set of APIs. This enables CERNBox to connect to an array of storages, allowing collaborative data services and applications to function at a large scale.

This Student Proposal aims to extend the capabilities of Reva’s notification system with more features to improve the user experience and the programmers' available API.


## Task ideas

* Extend the simple notifications in the Web front-end into a notifications center
* Implement a Mattermost notification extension
* Provide a richer set of actions for the notification API (filters, delayed actions, metrics)
* Create documentation for the new features

Any ideas the student comes up with while working on the project are welcome!


## Expected results

The scope and extent of the improvements will be tailored to the skills / available time of the student. We expect that at the conclusion of the project, the agreed upon new features of the CERNBox notification system will be implemented.


## Requirements
* Mandatory
  * Go and JavaScript (ES2020+)
  * Git
  * REST APIs
* Good to have
  * Distributed systems
  * VueJS
  * RDBMS (mySQL)


## Mentors
* **[Javier Ferrer](mailto:javier.ferrer@cern.ch)** CERN
* [Hugo Gonzalez Labrador](mailto:hugo.gonzalez.labrador@cern.ch) CERN


## Links
* [CERNBox project](https://cernbox.web.cern.ch)
* [Reva project](https://github.com/cs3org/reva)
