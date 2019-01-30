---
title: Development of LSTM and GRU layers in TMVA
layout: gsoc_proposal
project: TMVA
year: 2019
organization: CERN
---

## Description

Toolkit for Multivariate Analysis (TMVA) is a multi-purpose machine learning toolkit integrated into the ROOT scientific software framework, used in many particle physics data analyses and applications. In the past years we have expanded TMVA’s capabilities to include various deep learning architectures: Fully-connected (DNN), Convolutional (CNN) and Recurrent (RNN) Neural Networks. Currently the RNN implementation includes only the standard (vanilla) type layer. This summer we would like to expand the implementations to include the LSTM and GRU layer types. The candidate is expected to develop CPU and GPU based implementations.

Both layer types have very promising applications in particle physics such as jet tagging and particle tracking. For more information see [this publication](https://doi.org/10.1146/annurev-nucl-101917-021019).

## Task ideas
* Implementation of the forward and backward pass for the LSTM and GRU layer types
* Optimization for the CPU and GPU platform

## Expected results
* Working implementation of the LSTM and GRU layer types
* Runnable on CPU and GPU with performance comparable to existing implementations
* Demonstrator solving a ML task using the implementation


## Requirements
C++ skills, experience with large scale software development and machine learning tools is a plus.

## Mentors
  * [Lorenzo Moneta](mailto:Lorenzo.Moneta@cern.ch)
  * [Sitong An](mailto:s.an@cern.ch)

## Links
  * [ROOT TMVA](http://root.cern/tmva)
  * [TMVA source code](https://github.com/root-mirror/root/tree/master/tmva)
  * [Deep Learning and Its Application to LHC Physics](https://doi.org/10.1146/annurev-nucl-101917-021019)
