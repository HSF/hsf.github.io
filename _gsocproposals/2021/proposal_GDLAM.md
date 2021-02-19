---
title: Graph Neural Networks for Particle Momentum Estimation in the CMS Trigger System
layout: gsoc_proposal
project: GDLAM
year: 2021
organization:
  - Alabama
  - Beirut
  - Florida

---

## Description

CMS experiment currently uses machine learning algorithms at the Level-1 (hardware) trigger to estimate the momentum of traversing particles such as Muons. The first algorithm implemented in the trigger system was a discretized boosted decision tree. Currently, CMS is studying the use of deep learning algorithms at the trigger level that requires microsecond level latency and therefore requires highly optimized inference. 

This project will focus on implementation and benchmarking of deep learning algorithms for the trigger inference task. 

## Task ideas
 * Development and Benchmarking of graph networks (GNN) for momentum regression in the trigger system
 
## Expected results
 *  Benchmarks of deep network model inference for muon momentum assignment for prompt and displaced particles

## Requirements
Python, C++, and some previous experience in Machine Learning. 

## Mentors
  * [Suzanne Rozenzweig](mailto:srhelfrich@ufl.edu)
  * [Efe Yigibasi] (mailto:efe.yigitbasi@cern.ch)
  * [Darin Acosta](mailto:acostad@ufl.edu)
  * [Sergei Gleyzer](mailto:Sergei.Gleyzer@cern.ch) 
  * [Ali Hariri] (mailto:aah71@mail.aub.edu)


Please DO NOT contact mentors directly by email, and instead please send project inquiries to ml4-sci@cern.ch with Project Title in the subject and relevant mentors will get in touch with you. 


## Links
  * [Paper ](https://iopscience.iop.org/article/10.1088/1742-6596/1085/4/042042)