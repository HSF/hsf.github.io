---
title: TMVA Deep Learning Developments - 3D Convolutions
layout: gsoc_proposal
project: TMVA
year: 2020
organization:
  - CERN
  - OProject
---

# Description

Toolkit for Multivariate Analysis (TMVA) is a multi-purpose machine learning toolkit integrated into the ROOT scientific software framework, used in many particle physics data analysis and applications. We have expanded TMVA's capabilities to include a deep learning library (DNN) supporting 2D convolutional layers with training on both CPU and GPUs. This summer we would like to expand the toolkit with 3D convolutional operators implemented both for CPU and GPU. For the GPU the implementation will be based on the cuDNN library.
3D CNNs have very promising applications in particle physics such as imaging calorimetry and particle tracking, allowing physicists to use new techniques to identify particles and search for new physics. In addition they can be used as Generative Adversarial Networks for fast imaging detector simulation.


## Task ideas and expected results
  * Production-ready 3D CNNs implementation.
  * GPU support for training.


## Requirements 
Strong C++ skills, solid knowledge of deep learning, familiarity with GPUs

## Mentors
  * [Lorenzo Moneta](mailto:Lorenzo.Moneta@cern.ch)
  * [Omar Zapata](mailto:Omar.Zapata@cern.ch)

## Links
  * [http://root.cern/tmva](http://root.cern/tmva)
  * [TMVA source code](https://github.com/root-project/root/tree/master/tmva)

