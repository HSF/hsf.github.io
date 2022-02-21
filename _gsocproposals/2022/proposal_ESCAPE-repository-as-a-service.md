---
title: Repository as a Service
layout: gsoc_proposal
project: ESCAPE-OSSR
year: 2022
difficulty: medium
duration: 300
mentor_avail: June-September
organization: ESCAPE
---

## Description

The [ESCAPE project](https://projectescape.eu/) is building an Open Source and collaborative 
environment in where to connect astronomy, astroparticle and particle physics project. This 
research environment is composed of the ESCAPE services. In this context, the Open-source 
Science and Service Repository (OSSR) provides a trusted repository that will be accessible 
through the ESFRI Science Analysis Platform (ESAP).

The successful candidate will be integrated into the ESCAPE project to develop a JupyterLab 
extension to create an user friendly connection between the repository and the analysis platform 
(the computing resources). This plugin will simplify the access to Zenodo (the Open Source 
Repository) that provides an open archive for scientists to share their analysis software  
and data.
 

## Task ideas and expected Results

* Create a JupyterLab extension that connects the Jupyter environment and Zenodo (Repository) using the  
eOSSR python library to display the repository entries.
* Participate in the development of the eOSSR library to integrate the developed extension. 
* Bring back the entry content to the Jupyter environment using the developed extension.
* Investigate the possibility of installing the different software entries available in the repository 
and find solutions to the different software languages libraries.
* Help defining the needed stages to publish back into Zenodo and the ESCAPE community.


## Technology:
 * Python, Web Technologies.

## Desirable Skills
 * Necessary knowledge: Python and Web technologies.
 * Experience with git, REST APIs and basic DevOps knowledge would be an asset.

## Mentors
 * **[Enrique Garcia](mailto:garcia@lapp.in2p3.fr)** ESCAPE/LAPP-CNRS
 * [Thomas Vuillaume](mailto:vuillaume@lapp.in2p3.fr) ESCAPE/LAPP-CNRS

## Links
 * [ESCAPE project](https://projectescape.eu/about-us)
 * [ESCAPE Open-source Scientific Software and Service Repository (OSSR)](http://purl.org/escape/ossr)
 * [ESCAPE OSSR content](https://zenodo.org/communities/escape2020)
 * [eOSSR library](https://gitlab.in2p3.fr/escape2020/wp3/eossr/)