---
title: TMVA Graph Neural Networks
layout: gsoc_proposal
project: TMVA
year: 2020
organization:
  - CERN
  - Alabama
  - OProject
---

# Description

Toolkit for Multivariate Analysis [(TMVA)](http://root.cern/tmva) is a multi-purpose machine learning toolkit integrated into the ROOT scientific software framework, used in many particle physics data analysis and applications. We have expanded TMVA's capabilities to include a deep learning library (DNN) supporting fully-connected, convolutional and recurrent architectures. This summer we would like to expand the toolkit with a graph neural network [(GNN)](https://towardsdatascience.com/a-gentle-introduction-to-graph-neural-network-basics-deepwalk-and-graphsage-db5d540d50b3) library on CPU and GPU. GNNs are currently used by many promising applications in particle physics in physics analysis classification, calorimetry reconstruction, particle tracking and triggering systems, allowing physicists to use new techniques to identify particles and search for new physics. Additionally, they are useful for detector simulation.

## Task ideas and expected results
 * Create alpha version of GNN in TMVA based on existing DL suite
 * GPU support for GNN training and inference 


## Expected results
 * Prototype of basic GNN classes in the TMVA-DNN infrastructure
 * Tests of the classes for simple use cases


## Requirements 
Strong C++ skills, solid knowledge of deep learning, familiarity with GPUs

## Mentors
  * [Lorenzo Moneta](mailto:Lorenzo.Moneta@cern.ch)
  * [Sitong An](mailto:s.an@cern.ch)
  * [Sergei Gleyzer](mailto:Sergei.Gleyzer@cern.ch) 

Please DO NOT contact mentors directly by email, and instead please send project inquiries to MLSFT-GSOC@cern.ch with Project Title in the subject and relevant mentors will get in touch with you. 

## Links
  * [http://root.cern/tmva](http://root.cern/tmva)
  * [TMVA source code](https://github.com/root-project/root/tree/master/tmva)

