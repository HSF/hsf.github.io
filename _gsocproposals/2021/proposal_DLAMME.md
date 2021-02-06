---
title: Deep Learning Algorithms for Muon Momentum Estimation in the CMS Trigger System
layout: gsoc_proposal
project: DLAMME
year: 2021
organization:
  - Alabama
  - Florida
---

## Description

CMS experiment currently uses machine learning algorithms at the Level-1 (hardware) trigger to estimate the momentum of traversing particles such as Muons. The first algorithm implemented in the trigger system was a discretized boosted decision tree. Currently, CMS is studying the use of deep learning algorithms at the trigger level that requires microsecond level latency and therefore requires highly optimized inference. 

This project will focus on benchmarking, implementation and compression of deep learning algorithms for the trigger inference task. Currently implemented algorithms include boosted decision trees (BDTs), fully-connected deep neural networks (FCN) and convolutional neural networks (CNNs).


## Task ideas
 * Benchmarking of graph networks (GNN) for momentum regression in the trigger system
 * Development of DL compression algorithms for optimized inference
 * Prototyping of emulation of the DL-based trigger inference within realistic latency requirements

## Task ideas and expected results
 * Functional prototype emulator for deep-learning based trigger task of muon momentum assignment for fully connected networks
 * Functional prototype emulator for deep-learning based trigger task of muon momentum assignment for convolutional and graph networks
 * Benchmarks of deep network model inference for muon momentum assignment for prompt and displaced muons


## Requirements
Python, C++, and some previous experience in Machine Learning. 

## Mentors
  * [Mujeon Kim](mailto:pq8556@ufl.edu)
  * [Darin Acosta](mailto:acostad@ufl.edu)
  * [Sergei Gleyzer](mailto:Sergei.Gleyzer@cern.ch) 

Please DO NOT contact mentors directly by email, and instead please send project inquiries to MLSFT-GSOC@cern.ch with Project Title in the subject and relevant mentors will get in touch with you. 

## Links
  * [Paper ](https://iopscience.iop.org/article/10.1088/1742-6596/1085/4/042042)
  