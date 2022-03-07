---
title: Rucio WebUI Revamp
layout: gsoc_proposal
project: Rucio
year: 2022
difficulty: medium
duration: 350
mentor_avail: June-September
organization:
    - CERN
---

## Description

[Rucio](https://rucio.cern.ch) is an open-source software framework that provides functionality to scientific collaborations to organize, manage, monitor, and access their distributed data and dataflows across heterogeneous infrastructures. Rucio was originally developed to meet the requirements of the high-energy physics experiment ATLAS, and is continuously enhanced to support diverse scientific communities. Since 2016 Rucio orchestrated multiple Exabytes of data access and data transfers globally.

[Rucio WEBUI](https://github.com/rucio/rucio/tree/master/lib/rucio/web/ui), currently, is a Flask(python) application that is used by different types of users in the collaborating communities to access, monitor and manage their distributed data. 

This Flask application serves Jinja2 templates with custom JQuery code that queries the Rucio Server and renders the retrieved information. There are some special cases with direct database access occurs on the Flask side.

The first goal of this proposal is to migrate the WEBUI to a pure REST'ful architecture. This would require identifying and implementing new REST endpoints on the Rucio Server and developing a dynamic cross-platform ReactJS application that consumes the REST API directly, instead of having a middle layer in Flask, like we currently have.

The second goal of the proposal is to improve the overall user experience for the different types of users. In additional to migration of existing Rucio UI views to ReactJS app, we'd also like to introduce a new `Dashboard` view that would allow users to get a quick overview of relevant activity and provide quick access to frequently used functionalities. 



## Tasks

The tasks are as follows:
 * Migrate the existing views from [Jinja2 templates](https://github.com/rucio/rucio/tree/master/lib/rucio/web/ui/flask/templates)/[JQuery](https://github.com/rucio/rucio/tree/master/lib/rucio/web/ui/static) to corresponding ReactJS components and pages.
 * Create a React Component Library and a lightweight frontend framework(React + Next.js) that is used to standardize the authenticated requests made to the REST endpoints exposed by the Rucio Server, handle the rendering of components based on the browsers/platform (mobile views/desktop views) and manage routing(The existing url scheme needs to be preserved).
 * Implement a Dashboard View for logged in users. The dashboard must contain most recent DID's, Transfers and their status, Account/Group Usage.
 * Add new REST endpoints or modify existing REST endpoints in Rucio Server to support the functions of the React App. This is especially required for the new Dashboard view.


## Requirements

 * Mandatory
   * ReactJS + Redux
   * Next.js
   * Jest/React Testing Library
   * JavaScript (ECMA6), TypeScipt
   * HTML5, CSS/Sass 
   * Python 3
   * Flask
   * Linux, Git, and Docker
 * Basic understanding ( Good to know )
   * Webpack
   * Github Actions
   * HTTP REST APIs
   * OpenID Connect/x509 protocols

## Expected results

By the end of GSoC'22 we expect a Rucio WebUI ReactJS application that 
1. Interfaces with the REST endpoints provided by the Rucio Server for rendering the main functionalities from the existing UI
2. Presents the users with a new Dashboard View  

## Mentors
 * **[Mayank Sharma](mailto:mayank.sharma@cern.ch)**
 * [Cedric Serfon](mailto:cedric.serfon@cern.ch)
 * [Martin Barisits](mailto:martin.barisits@cern.ch)

## Links
 1. [Rucio GitHub](https://github.com/rucio/rucio)
 1. [Rucio UI presentation](https://docs.google.com/presentation/d/1mXw8Xo3bknO8Ahyd6RvKlNP0OwgXdKJxz6fWiuLYOdI/edit?usp=sharing)
 2. [Rucio Documentation](https://rucio.readthedocs.io/en/latest/)
 2. [Rucio system overview journal article (Springer)](https://doi.org/10.1007/s41781-019-0026-3)
 3. [Rucio operational experience article (IEEE Computer Society)](http://sites.computer.org/debull/A20mar/p9.pdf)
