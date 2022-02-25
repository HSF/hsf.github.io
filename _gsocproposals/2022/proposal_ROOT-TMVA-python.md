---
title: ROOT - TMVA  Developments - Improve Python interface for TMVA  
layout: gsoc_proposal
project: ROOT
difficulty: medium
duration: 350
mentor_avail: May-September
year: 2022
organization:
    - CERN
---

## Description

Toolkit for Multivariate Analysis (TMVA) is a multi-purpose machine learning toolkit integrated into the ROOT scientific software framework, used in many particle physics data analysis and
applications. Since it is part of the ROOT data analysis framework, it comes with an automatically generated Python interface, which closely follows the C++ interface.
The goal of this project is to enhance the Python interface to make more "pythonic", i.e. easier to use. Moreover, several machine learning methods require using option strings to be
configured. Within Python it is natural to use the native language feature to configure the methods.

## Task ideas and expected results

The initial task will be to develop a Pythonization of the TMVA method configuration, using similar code already developed for the notebook interface in a previous GSOC project.
Afterwards it is expected that the interface of the TMVA workflow for both training and inference will be improved in Python, with the possibility to pass directly Numpy collections such as Python
arrays. This will require some extra code in order to be used efficiently from Python.
Another task will be to integrate also the new developments in the variable plotter inside TMVA and provide a Python interface to the TMVA GUI.
Tests and tutorial examples are also expected to be developed, including the migration of existing tutorials to the pythonizations developed in this project.


## Evaluation Task

Interested students please contact the mentors for a warm-up and evaluation task.

## Requirements
 Good knowledge of Python and  C++, familiarity with machine learning software tools

## Mentors
 * **[Lorenzo Moneta](mailto:Lorenzo.Moneta@cern.ch)**
 * [Sitong An](mailto:s.an@cern.ch)


## Links
 * [ROOT](https://root.cern/)
 * [TMVA](https://root.cern/manual/tmva/)
