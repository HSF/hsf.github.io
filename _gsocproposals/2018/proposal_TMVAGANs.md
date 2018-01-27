---
title: Generative Adversarial Networks for Particle Physics Applications
layout: gsoc_proposal
project: TMVA
year: 2018
organization:
  - UdeA
  - UFlorida
  - CERN
  - KIT
  - Oproject
---

# Description

The use of Generative Adversarial Networks (GANs) is of particular interest for potential applications for particle physics in the area of fast detector simulations and reducing the systematic uncertainty related to applying machine learning algorithms. GANs are sets of networks competing with each other. For example a generator network produces simulated samples based on a training set, competing with a classification network that attempts to classify events. The use of GANs is of particular interest for potential applications focused on fast and accurate event simulation as well as other applications aimed at reducing the dependence of the classifier on specific parameters. 

Toolkit for Multivariate Analysis (TMVA) is a multi-purpose machine learning toolkit integrated into the ROOT scientific software framework, used in many particle physics data analysis and applications. In the past two years we have expanded TMVA’s capabilities to include robust implementations of various deep learning architectures: Fully-connected (DNN), Convolutional (CNN) and Recurrent (RNN). 

The goal of this project is to extend the existing deep learning libraries in TMVA to support GANs. 


## Task ideas and expected results
  * Production-ready GAN library
  * GPU support for training


**Requirements**: Strong C++ skills, solid knowledge of deep learning, understanding of GANs, familiarity with GPUs

**Mentors**: 
* [Sergei Gleyzer](mailto:sft-gsoc@cern.ch?subject=Other%20Machine%20Learning%20Projects%20in%20TMVA) 
* [Omar Zapata](mailto:sft-gsoc@cern.ch?subject=Other%20Machine%20Learning%20Projects%20in%20TMVA)
* [Stefan Wunsch](mailto:sft-gsoc@cern.ch?subject=Other%20Machine%20Learning%20Projects%20in%20TMVA)

**Links**:
  * [http://root.cern](http://root.cern)
  * [http://root.cern/tmva](http://root.cern/tmva)
  * [TMVA source code](https://github.com/root-project/root/tree/master/tmva)

