---
title: Making Exabytes of LHC data seamlessly accessible on Jupyter Notebooks
layout: gsoc_proposal
project: SWAN/Rucio
year: 2020
organization:
 - CERN
---

## Description

The LHC experiments at [CERN](https://home.cern/) produce an enormous amount of scientific data. One of the main computing challenges is to make such data easily accessible by scientists and researchers. Technologies and services are being developed at CERN and at partner institutes to face this challenge, ultimately allowing to turn scientific data into knowledge.

[SWAN](https://cern.ch/swan) (Service for Web-based ANalysis) is a platform allowing CERN users to perform interactive data analysis directly using a web browser. This service builds on top of the widely-adopted [Jupyter Notebooks](http://jupyter.org). It integrates storage, synchronisation, and sharing capabilities of CERNBox and the computational power of Spark/Hadoop clusters. Both scientists at CERN and at partner institutes are using SWAN on a daily basis to develop algorithms required to perform their data analysis. In fact, a full analysis can be performed using Notebooks as long as all the required data are available locally. 

The [Rucio](https://rucio.cern.ch) data management system was principally developed by the ATLAS experiment to deal with Exabytes of data in a scalable, modular, and reliable way. Nowadays, Rucio has become the de-facto data management system in High Energy Physics and many other scientific communities (Astronomy, Astrophysics, Environmental Science) are evaluating and adopting it.

In the Exabytes-scale era, the challenge to move large amounts of data in the local file system of a Notebook is faced on a daily basis by each individual scientist, causing duplication of effort and delaying the analysis results. The integration of Rucio in the Jupyter Notebook environment is a challenging but necessary R&D activity from which the worldwide scientific community would greatly benefit. This will be achieved by using the Rucio API since it represents the cutting-edge technology to orchestrate such amount of data.



## Task ideas

  * Develop a JupyterLab extension that integrates Rucio functionalities inside the JupyterLab UI
    * Link experiment data into notebooks that require them
    * Make the extension transparently fetch the required data using Rucio through API calls
    * Add configuration options to decide where the data should be stored
    * Make the staging process progress visible to the user
  * Integrate the developed extension into SWAN

## Expected results

A working, and easy-to-use extension, installable both in SWAN and vanilla JupyterLab, which will allow users to easily stage data available on a Rucio server for interactive analysis.

## Desirable Skills
* Knowledge of JavaScript and Python
* Knowledge of Linux and GIT
* Experience with Jupyter Notebooks
* Understanding of REST APIs

## Mentors
* [Aristeidis Fkiaras](mailto:aristeidis.fkiaras@cern.ch)
* [Riccardo Di Maria](mailto:Riccardo.Di.Maria@cern.ch)
* [Rizart Dona](mailto:rizart.dona@cern.ch)
* [Mario Lassnig](mailto:Mario.Lassnig@cern.ch)
* [Enric Tejedor](mailto:etejedor@cern.ch)
* [Enrico Bocchi](mailto:enrico.bocchi@cern.ch)
* [Diogo Castro](mailto:diogo.castro@cern.ch)
* [Martin Barisits](mailto:martin.barisits@cern.ch)

## Links
* [CERN](https://home.cern/)
* [SWAN Website](https://cern.ch/swan)
* [SWAN Github](https://github.com/swan-cern)
* [Jupyter](http://jupyter.org)
* [Rucio Website](https://rucio.cern.ch)
* [Rucio Github](https://github.com/rucio/rucio)