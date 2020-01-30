---
title: MCnet/CONTUR - Develop an interactive graphical interface for a physics re-interpretation tool
layout: gsoc_proposal
project: MCnet
year: 2020
organization:
  - UGlasgow
  - CERN
  - UCL
---

# Description

COntraining New Theories Using RIVET [(CONTUR)](https://hepcedar.gitlab.io/contur-webpage/) is a Python-based package which uses the bank of LHC searches and measurements preserved in [Rivet](https://rivet.hepforge.org) and the [Herwig](https://herwig.hepforge.org/) event generator, to set constraints on new beyond-the-Standard-Model (BSM) theroies. Fundamentally, CONTUR uses Herwig to generate simulated events for a grid of parameter values for the new model, and checks for each point in the grid, whether the BSM signal would already have been see in any of the existing LHC results. It can then produce an exclusion "heatmap" for the grid, and define exclusion contours at the 68% and 95% confidence level.

The bank of measurements and searches used by CONTUR includes hundreds of measured distributions, across ~100 LHC results, arranged into dozens of analysis pools. Understanding the exclusions from the heatmaps often involves checking how the BSM signal would look in these measured distributions. Furthermore, depending on the number of parameters in the model, there can be hundreds, or even thousands of grid points to check. At the moment, extracting these plots and digesting them is a laborious and time-consuming process. That is where you come in.

## Tasks

The task for this project would be to put together an user-friendly interface to be able to "drill down" into the heatmaps produced by CONTUR and understand the origin of the exclusion of a particular model for a particular set of parameters. This could be a graphical user interface (GUI) or a web-page, where the user could simply "click" or "hover" over a point of the heatmap, and this would bring up the set of measurements which give the analysis pools with the most exclusion power, with the option of drilling down futher to view the results for a given measurement, or even a given measured distribution.

Producing the plots for these visualisations can be a time-consuming process, so part of the task may be to create a system where a database is dynamically created and populated for each heatmap.

The problem of how to visualise scans of models in more than 2 dimensions would also need to be addressed. This could take the form of a "slider" on a web-page, where the user could select the values of each parameter and see the heatmap update in real time. 

Creating such tools to help users visualise (and debug) exclusions from CONTUR would significantly speed up the processing and understanding of CONTUR results, and subsequently could play an important role in quickly ruling out new theories (and saving time for researchers to work on other theories which are not ruled out).


## Expected results

- Produce a GUI or website to help "drill down" into the result of CONTUR heatmaps
- Ensure that the GUI/webiste runs quickly and efficiently by producing a database of plots and figures (on-the-fly) for each heatmap
- Extend the capaility to visualise multi-dimensional scans by adding a slider (or otherwise) to the heatmaps on the site

## Requirements

- Python (and related packages, e.g. matplotlib)
- git
- PHP/HTML
- SQL

## Mentors

  * [Andy Buckley](mailto:andy.buckley@cern.ch)
  * [Louie Corpe](mailto:louie.corpe@cern.ch)
  * [Jon Butterworth](mailto:j.butterworth@cern.ch)

## Links
  * [CONTUR](https://hepcedar.gitlab.io/contur-webpage/)
  * [YODA](https://yoda.hepforge.org)
  * [Rivet](https://rivet.hepforge.org)
  * [Herwig](https://herwig.hepforge.org/)
