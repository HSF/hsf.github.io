---
title: Convolutional Deep Neural Networks on GPUs for Particle Physics Applications
layout: gsoc_proposal
project: TMVA
year: 2018
organization:
  - Florida
  - CERN
  - OProject
  - ETH
  - EPFL
---

# Description

Toolkit for Multivariate Analysis (TMVA) is a multi-purpose machine learning toolkit integrated into the ROOT scientific software framework, used in many particle physics data analyses and applications. In the past two years we have expanded TMVA’s capabilities to include various deep learning architectures: Fully-connected (DNN), Convolutional (CNN) and Recurrent (RNN) Neural Networks. Currently, only the DNN supports interactive training on GPUs. This summer we would like to expand the GPU implementations to include convolutional and possibly recurrent deep neural networks (CNN and RNN).  Both have very promising applications in particle physics such as particle and event classification, imaging calorimetry and particle tracking, allowing physicists to use new techniques to identify particles and search for new physics.


## Task ideas
 * Production-ready gpu version of the convolutional deep learning library.
 * Support for GPUs for training.


**Requirements**: Strong C++ skills, solid knowledge of deep learning, understanding of convolutional and/or recurrent networks, familiarity with GPU interfaces a plus

**Mentors**: 
* [Sergei Gleyzer](mailto:sft-gsoc@cern.ch?subject=TMVA%20CNN) 
* [Lorenzo Moneta](mailto:sft-gsoc@cern.ch?subject=TMVA%20CNN) 
* [Vladimir Ilievski](mailto:sft-gsoc@cern.ch?subject=TMVA%20CNN)
* [Saurav Shekhar](mailto:sft-gsoc@cern.ch?subject=TMVA%20CNN)

**Links**:
  * [http://root.cern/tmva](http://root.cern/tmva)
  * [TMVA source code](https://github.com/root-project/root/tree/master/tmva)

