---
title: ROOT -  Developments - Improve Python interface for HIstograms  
layout: gsoc_proposal
project: ROOT
difficulty: medium
duration: 350
mentor_avail: May-September
year: 2024
organization:
    - CERN
---

## Description

The goal of this project is to enhance the Python interface to make more "pythonic", i.e. easier to use, popular classes in ROOT such as histograms and graphs.  Within Python it is natural to use the native language feature to configure the methods.

## Task ideas and expected results

The initial task will be to develop easy conversions of histograms and graph ROOT classes to Numpy arrays.  Afterwards it is expected to implement the Universal Histogram Interface (UHI, see [https://uhi.readthedocs.io/en/latest/](https://uhi.readthedocs.io/en/latest/) ) for the ROOT histograms. This will allow interoperability in Python between different histogram packages. 
Tests and tutorial examples are also expected to be developed, including the migration of existing tutorials to the pythonizations developed in this project.


## Evaluation Task

Interested students please contact the mentors for a warm-up and evaluation task.

## Requirements
 Good knowledge of Python and  C++, familiarity with machine learning software tools

## Mentors
 * **[Lorenzo Moneta](mailto:Lorenzo.Moneta@cern.ch)**
 * [Jonas Rembser](mailto:jonas.rembser@cern.ch)


## Links
 * [ROOT](https://root.cern/)
