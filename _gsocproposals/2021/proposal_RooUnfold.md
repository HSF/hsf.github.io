---
project: RooUnfold
title: RooUnfold - Efficient deconvolution using state of the art algorithms
layout: gsoc_proposal
year: 2021
organization:
  - Tufts
  - CERN
---

## Description
[RooUnfold](https://roounfold.web.cern.ch) is a powerful modular analysis tool is for the unfolding (AKA "deconvolution" or "unsmearing") of distributions.
Unfolding is the statistical process in which the 'true' underlying processes that govern the interactions of fundamental forces of the universe are estimated from both simulated and measured data.
To facilitate these data intensive analyses, RooUnfold is built on the [ROOT](https://root.cern/) Software Framework and is used in the publication of hundreds of LHC analyses every year.
RooUnfold was designed to provide a common interface for a number of analysis algorithms and was [recently upgraded](https://arxiv.org/abs/1910.14654) to leverage the power of the ROOT statistical modelling package RooFit in order to provide a statistical comparison of the various algorithms.

This project aims to address obsolescence in the underlying RooUnfold implementation that would allow the RooUnfold package to act as a lightweight member class to ROOT whilst retaining its functionality and the ability for users to define new algorithms including machine learning based solutions, and data intensive tasks. 

## Task Ideas
* Learn about the algorithms and statistics that govern the LHC's most precise measurements.
* Implement a lightweight RooUnfold base class using modern C++ that is able to efficiently replicate current usage.
* Design and develop an interface for analysis algorithms that is compatible with the new array of statistical tests available.
* Explore the implementation of deep learning based algorithms that leverage sparse weighted events rather than histograms.
* Expand the suite of data visualisation tools and performance metrics provided for the unfolding procedure.

## Expected results
Working implementation of a new C++ base class that is optimised for usage with abstracted unfolding algorithms.

## Requirements
C++, CMake, python

## Mentors
* [**Vincent Croft**](mailto:vincent.croft@cern.ch)
* [Lydia Brenner](mailto:lydia.brenner@cern.ch)
* [Tim Adye](mailto:T.J.Adye@rl.ac.uk)
* [Carsten Burgard](mailto:carsten.burgard@cern.ch)
* [Pim verschuuren](mailto:pim.verschuuren@rhul.ac.uk)
