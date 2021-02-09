---
project: CERNBox
title: Scientific Notebook support in ownCloud Infinite Scale
layout: gsoc_proposal
year: 2021
organization:
  - CERN
  - ownCloud
---


## Description
[SWAN](https://swan.web.cern.ch/swan/) (Service for Web-based ANalysis) is the leading platform allowing CERN users to perform interactive data analysis by writing code and running it simply using a web browser. It builds on top of the widely-adopted Jupyter Notebooks by integrating the storage, synchronization and sharing capabilities of [CERNBox](https://cernbox.web.cern.ch/cernbox/).

[CERNBox](https://cernbox.web.cern.ch/cernbox/) is a sync and share collaborative cloud storage solution at CERN used by more than 37K users and storing over 12PB of data. CERNBox has responded to the high demand in our diverse community to an easily and accessible cloud storage solution that provides integration with other CERN services for big science: visualization tools, interactive data analysis and real-time collaborative editing. The integration with SWAN has been a widely used feature to explore notebooks in the glimpse of an eye. 

The aim of this project is to add adapt the existing integration SWAN/CERNBox to the new ownCloud architecture codenamed OCIS to continue supporting the vast scientific community that rely on this synergy.

## Task ideas
* Develop a SWAN OCIS application to explore scientific notebooks from the CERNBox UI.
* Allow the integration of the application with vanilla JupyterHub/JupyterLab environments
* Document the application and publish in the OCIS marketplace
* Test the application in the new CERNBox UI

## Expected results
We expect at the end of GSOC '21, a VueJS application that can be enabled in CERNBox and SWAN to explore scientific notebooks in the new ownCloud platform.

##  Requirements
* JS, VueJS, Python, Go

## Mentors
* **[Samuel Alfageme](mailto:samuel.alfageme.sainz@cern.ch)** CERN
* [Lukas Hirt](mailto:lhirt@owncloud.com) ownCloud
* [Diogo Castro](mailto:diogo.castro@cern.ch) CERN
* [Krishnan Raghavan](mailto:krishnan.raghavan@cern.ch) CERN
* [Hugo Gonzalez Labrador](mailto:hugo.gonzalez.labrador@cern.ch) CERN

## Links
* [SWAN project](https://swan.web.cern.ch)
* [CERBox project](https://cernbox.web.cern.ch)
* [OCIS project](https://owncloud.github.io/ocis/)
