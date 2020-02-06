---
title: Deep Learning Algorithms for Muon Momentum Estimation in the CMS Trigger System
layout: gsoc_proposal
project: CMS
year: 2020
organization:
  - CERN
  - Alabama
  - Florida
  - AUB
---

## Description

CMS experiment currently uses machine learning algorithms at the Level-1 (hardware) trigger to estimate the momentum of traversing particles such as Muons. The first algorithm implemented in the trigger system was a discretized boosted decision tree. Currently, CMS is studying the use of deep learning algorithms at the trigger level that requires microsecond level latency and therefore requires highly optimized inference. 

This project will focus on benchmarking, implementation and compression of deep learning algorithms for the trigger inference task. Currently implemented algorithms include boosted decision trees (BDTs), fully-connected deep neural networks (FCN) and convolutional neural networks (CNNs).


## Task ideas
 * Benchmarking of graph networks (GNN) for momentum regression in the trigger system
 * Development of DL compression algorithms for optimized inference
 * Prototyping of emulation of the DL-based trigger inference within realistic latency requirements


## Requirements
Python, C++, and some previous experience in Machine Learning. 

## Mentors
  * [Mujeon Kim](mailto:pq8556@ufl.edu)
  * [Ali Hariri]()
  * [Sergei Gleyzer](mailto:Sergei.Gleyzer@cern.ch) 

## Links
  * [Paper ](https://iopscience.iop.org/article/10.1088/1742-6596/1085/4/042042)
  