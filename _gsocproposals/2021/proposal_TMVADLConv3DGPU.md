---
title: TMVA Deep Learning Developments - 3D Convolutions for GPU
layout: gsoc_proposal
project: ROOT
year: 2021
organization:
  - CERN
---

# Description

Toolkit for Multivariate Analysis (TMVA) is a multi-purpose machine learning toolkit integrated into the ROOT scientific software framework, used in many particle physics data analysis and
applications. We have expanded TMVA's capabilities to include a deep learning library (DNN) supporting 2Dconvolutional layers with training on both CPU and GPUs. This summer we would like to complete it
with the 3D convolution operator.
3D CNNs have very promising applications in particle physics, such as imaging calorimetry and particle tracking, allowing physicists to use new techniques to identify particles and search for new physics. In addition they can be used as Generative Adversarial Networks for fast imaging detector simulations.




## Task ideas and expected results
The initial task of the student will be validating and integrating in ROOT the  CPU implementation for 3D convolution that was developed last summer .
Afterwards, the main task will be the development of the 3D convolution for Nvidia GPU using the cuDNN library, following the current implementation present in ROOT/TMVA for the 2D operator. 
The developed code should support both the training and inference for deep learning models.

## Requirements 
Strong C++ skills, solid knowledge of deep learning, familiarity with GPUs

## Mentors
  * **[Lorenzo Moneta](mailto:Lorenzo.Moneta@cern.ch)**
  * [Omar Zapata](mailto:Omar.Zapata@cern.ch)
  
Interested students please contact the mentors for project inquiries and evaluation task. 

## Links
  * [ROOT](https://root.cern/)
  * [TMVA](https://root.cern/manual/tmva/)
  * [cuDNN](https://docs.nvidia.com/deeplearning/cudnn/developer-guide/index.html)
