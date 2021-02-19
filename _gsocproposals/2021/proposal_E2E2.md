---
title: Graph Neural Networks for End-to-End Particle Identification with the CMS experiment
layout: gsoc_proposal
project: E2E
year: 2021
organization:
  - Alabama
  - Brown
  - CMU
---

## Description

One of the important aspects of searches for new physics at the [Large Hadron Collider (LHC)](https://home.cern/science/accelerators/large-hadron-collider 
) involves the identification and reconstruction of single particles, jets and event topologies of interest in collision events. The End-to-End Deep Learning (E2E) project in the CMS experiment focuses on the development  of these reconstruction and identification tasks with innovative deep learning approaches.   

This project will focus on the development of end-to-end graph neural networks for particle (tau) identification and [CMSSW](https://github.com/cms-sw/cmssw) inference engine for use in reconstruction algorithms in offline and high-level trigger systems of the [CMS](https://home.cern/science/experiments/cms ) experiment.

## Task ideas
 * Development of end-to-end graph neural networks for low-momentum tau identification
 * Test and benchmarking of inference on GPUs

## Expected results
 * Trained end-to-end graph neural network model for tau identification 
 * Benchmark of end-to-end GNN inference on gpu


## Requirements
C++, Python, PyTorch and some previous experience in Machine Learning.

## Mentors

  * [Davide DiCroce](mailto:davide.di.croce@cern.ch) 
  * [Emanuele Usai](mailto:emanuele.usai@cern.ch)   
  * [Sergei Gleyzer](mailto:Sergei.Gleyzer@cern.ch)
  * [Michael Andrews](mailto:michael.andrews@cern.ch)


Please DO NOT contact mentors directly by email, and instead please send project inquiries to ml4-sci@cern.ch with Project Title in the subject and relevant mentors will get in touch with you. 



## Links
  * [Paper 1](https://arxiv.org/abs/1807.11916)
  * [Paper 2](https://arxiv.org/abs/1902.08276)
