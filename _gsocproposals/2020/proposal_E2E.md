---
title: End-to-end Deep Learning Reconstruction for CMS experiment
layout: gsoc_proposal
project: E2E
year: 2020
organization:
  - CERN
  - Alabama
  - Brown
  - Florida
---

## Description

One of the important aspects of searches for new physics at the [Large Hadron Collider (LHC)](https://home.cern/science/accelerators/large-hadron-collider 
) involves the identification and reconstruction of single particles, jets and event topologies of interest in collision events. The End-to-End Deep Learning (E2E) project in the CMS experiment focuses on the development  of these reconstruction and identification tasks with innovative deep learning approaches.   

This project will focus on the integration of E2E code with the [CMSSW](https://github.com/cms-sw/cmssw) inference engine for use in reconstruction algorithms in offline and high-level trigger systems of the [CMS](https://home.cern/science/experiments/cms ) experiment.



## Task ideas
 * Integration/interface of E2E with the CMSSW inference engine
 * Test and optimization of the E2E inference for given reconstruction task
 * Integration of prototype with CMSSW Particle Flow (PF) classes
 * Test and benchmarking of inference on GPUs

## Expected results
 * Integrated code within CMSSW classes
 * Benchmark of end-to-end deep learning inference on cpu and gpu


## Requirements
Python, Keras, PyTorch, C++, and some previous experience in Machine Learning.

## Mentors
  * [Mujeon Kim](mailto:pq8556@ufl.edu) 
  * [Sergei Gleyzer](mailto:Sergei.Gleyzer@cern.ch) 

Please DO NOT contact mentors directly by email, and instead please send project inquiries to MLSFT-GSOC@cern.ch with Project Title in the subject and relevant mentors will get in touch with you. 

## Links
  * [Paper 1](https://arxiv.org/abs/1807.11916)
  * [Paper 2](https://arxiv.org/abs/1902.08276)
  