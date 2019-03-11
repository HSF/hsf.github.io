---
title: Integrate of cuDNN library in TMVA  
layout: gsoc_proposal
project: TMVA
year: 2019
organization: CERN
---

## Description

ROOT provides via the TMVA package a new Deep Learning framework, which supports convolutional and recurrent layers in addition to dense layers. The models can be trained also on NVIDIA GPU using CUDA. The CUDA implementation for convolutional layers is not fully optimized for Nvidia graphics cards. A possible way to improve its performance is to use the NVIDIA dedicated library for training and evaluating deep learning models, cuDNN.  
The main goal is then to re-implement the GPU backend for convolutional network using this library from NVIDIA. As a further extension, capable candidates will also gain experiences from implementing a cuDNN rucurrent layers.

## Task ideas
* Develop a new GPU implementation for convolutional networks using the NVIDIA CuDNN library
* Integrate this implementation inside TMVA
* Develop a similar backend for recurrent neural network. Currently no GPU implementation is available in ROOT for recurrent networks.
* Perform validation and benchmarking tests using some standard HEP datasets

## Expected results
* Working cuDNN implementation of convolutional neural networks
* Working cuDNN implementation of recurrent neural networks
* Integration of the implementation into TMVA
* Validation and performance benchmarking of the new implementation


## Requirements
C++ skills, experience with large scale software development and GPU programming is a plus.

## Mentors
  * [Lorenzo Moneta](mailto:Lorenzo.Moneta@cern.ch)
  * [Sitong An](mailto:s.an@cern.ch)

## Links
  * [ROOT TMVA](http://root.cern/tmva)
  * [TMVA source code](https://github.com/root-mirror/root/tree/master/tmva)
  * [cuDNN](https://developer.nvidia.com/cudnn)
