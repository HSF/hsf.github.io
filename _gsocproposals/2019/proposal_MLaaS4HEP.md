---
title: Platform for Machine Learning as a Service in HEP
layout: gsoc_proposal
project: CMS
year: 2019
organization: 
  - Cornell
  - Université Clermont Auvergne
---

## Description

The CMS experiment is interested to continue its Machine Learning as a Service
R&D program to develop its MLaaS platform to work with HEP ROOT data. Our goal is
to provide a web based platform to simplify end-user experience with HEP
data and training ML models. We envision that ML workflows can be fully
automated via a slim web interface which will allow data inspection, visualization,
training and serving ML models for distributed HEP data. The successful
candidate will work on unifying previously developed components [1,2,3] into
a single framework and its deployment as a Service into a cloud infrastructure.

## Tasks

We have working prototype of MLaaS4HEP which includes the following components:

  * various components of MLaaS to read, pre-process and train ML models
    from remote distributed ROOT files (Python codebase)
  * fully functional TensorFlow as a Service web service (Go codebase)
  * Go based groot library for reading and visualizing ROOT files (Go codebase)

All of these tools should be streamlines into single platform which will allow
users to build their favorite ML models via web based interface, similar to
industry based solutions such as AmazonML, Microsoft Azure ML Studio, Google
Prediction API and ML engine, and IBM Watson platforms.

The main difference would be that MLaaS4HEP should be oriented to HEP
based workflows, e.g. read ROOT files, build ML from ROOT content, etc.

To complete the project we propose the following steps:

  * design and built web based interface to

    * discover and read remote ROOT files
    * visualize ROOT file content via histograms
    * build ML workflows
    * train ML models and inspect their performance

  * deploy new platform to OpenStack cloud solution via kubernetes setup
  * perform stress testing of the new platform on basic ML models with HEP ROOT
    files

## Expected results
Working implementation of the system and fully tested in distributed environment.

## Requirements
Solid knowledge of Go and Python langauges, some knowledge of containerized
solutions (docker, kubernetes), web design, front-end web UI development, JavaScript, git.

## Mentors 
  * [V. Kuznetsov](mailto:vkuznet@gmail.com)
  * [S. Binet](mailto:binet@cern.ch)

## Links
  * [https://github.com/vkuznet/MLaaS4HEP](https://github.com/vkuznet/MLaaS4HEP)
  * [https://github.com/vkuznet/TFaaS](https://github.com/vkuznet/TFaaS)
  * [https://arxiv.org/abs/1811.04492](https://arxiv.org/abs/1811.04492)
  * [https://go-hep.org](https://go-hep.org)
  * [https://github.com/go-hep/hep/tree/master/groot](Go-HEP groot)
