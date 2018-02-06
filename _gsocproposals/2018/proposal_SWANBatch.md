---
title: Large-scale computing backend for Jupyter notebooks: HTCondor batch job submission and monitoring using the Ganga toolkit
layout: gsoc_proposal
project: SWAN
year: 2018
organization: CERN
---

## Description

Nowadays, in the data analysis field, there is a noticeable trend towards web-based interactive analysis, where the user interacts with an on-line service by means of a web-browser. One of the preferred interfaces for this interactive analysis is [Jupyter](http://jupyter.org) notebooks.

CERN provides a notebook service, called [SWAN](http://swan.web.cern.ch), where users can create notebooks on demand and access the software and data they need to run those notebooks. This model of data analysis works for small, exploratory computations, where the interactivity of the notebook is the perfect match, but physicists also often need to submit more expensive computations to larger resources. Traditionally, this has been done at CERN by submitting batch jobs -- using open-source toolkits such as [Ganga](http://cern.ch/ganga) --  that operate on a set of input data and produce some results. 

In order to integrate the interactive mode with the batch mode, this project aims to develop a plugin for Jupyter notebooks that allows users to easily offload big computations to external resources and monitor them. 

## Task ideas
 * Design and implementation of a plugin, based on the Ganga toolkit, to easily submit and monitor batch jobs from a notebook
   * Display information such as progress bars, job statistics and errors
   * Allow to cancel ongoing jobs
 * Use cases: apply the plugin to real batch jobs at CERN using [HTCondor](http://research.cs.wisc.edu/htcondor)
 * Tests on CERN batch infrastructure
 * Integration of the plugin into the SWAN notebook service at CERN

## Expected results
Working implementation of a Python/Javascript library that allows to easily submit and monitor batch jobs from a Jupyter notebook

## Requirements
Python, JavaScript, Jupyter notebooks

## Mentors 
  * Ulrik Egede (Imperial College London)
  * Jakub Moscicki (CERN IT-ST)
  * Ben Jones (CERN IT-CM)
  * Enric Tejedor (CERN PH-SFT)
  * Diogo Castro (CERN PH-SFT)

## Links
  * [Jupyter](http://jupyter.org)
  * [SWAN](http://swan.web.cern.ch) 
  * [Ganga](http://cern.ch/ganga)
  * [HTCondor](http://research.cs.wisc.edu/htcondor)
  


{% include gsoc_project.ext %}

