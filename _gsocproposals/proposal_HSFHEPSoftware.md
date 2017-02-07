---
title:   hepsoftware.org - The HEP Software and Computing Knowledge Base
layout: plain
project: HSF
organization:
  - BNL
  - CERN
---

## Description

The High Energy Physics (HEP) Software & Computing Knowledge Base at hepsoftware.org is a collection point for HEP related software projects and information on HEP software and computing. Its development was one of the earliest priorities of the HEP Software Foundation (HSF). It catalogues existing software, provides visibility and discoverability for new  and emerging projects seeking collaborators, and disseminates knowledge on who is using what.

It is implemented as an intelligent, highly responsive javascript client served by a Node.js based service backed by relational and (optionally) nosql database repositories and an in-memory (Redis) transient store. A prominent design objective is that editing new and existing content be open to all and (almost) as simple as using the content already there. -- to make contributing content as close as possible to being fun, thereby lowering the potential barrier for attracting contributors. The intent of the knowledge base is that building it is the task of the whole HEP S&C community.

The present implementation is a spare-time prototype developed by a former Fortran programmer, physicist and javascript neophyte, ie not so good. The objective of this project is to reengineer and reimplement hepsoftware.org from scratch as a high quality intelligent web app. 

## Task ideas

The foremost objective is to reimagine and reimplement (creatively, with plenty of room for improvement) hepsoftware.org with at least the feature set of the present version.

Further objectives for a particularly productive developer could be adding un-implemented functionality, such as
- a full implementation of the 'people' component, allowing users to create a profile and relate themselves to experiments, organizations, software projects etc.
- implementation of group support, allowing for group-specific (e.g. experiment-specific) content, which may be private to the group or public
- extending the integration with other information sources, e.g. google calendar integration was recently added to automatically ingest the HSF Community Calendar (but flowing content the other direction is not yet implemented
- many more.

## Expected results

A new production capable implementation of hepsoftware.org, ideally with an expanded feature set, fully open source and maintainable by the HSF with the ongoing participation of the GSoC developer should they choose.

## Requirements

- javascript based intelligent web client development
- Node.js based web server development
- relational and nosql database familiarity
- client/server, real-time, and concurrent programming familiarity
- web development
- Linux server sysadmin familiarity

## Mentors

 * [Benedikt Hegner](mailto:benedikt.hegner@cern.ch)
 * [Pere Mato](mailto:pere.mato@cern.ch)
 * [Torre Wenaus](mailto:wenaus@gmail.com)

