---
title: TMVA Deep Learning Developments - Data preprocessing in inference
layout: gsoc_proposal
project: TMVA
year: 2020
organization:
  - CERN
---

# Description

Toolkit for Multivariate Analysis [(TMVA)](http://root.cern/tmva) is a multi-purpose machine learning toolkit integrated into the [ROOT](http://root.cern) scientific software framework, used in many particle physics data analysis and applications. We provide in TMVA the functionality for building deep neural networks including fully connected, convolutional and recurrent layers. For the next stage of development of TMVA, we aim to provide a fast and convenient inference engine that takes ONNX model as input and produces compilation-ready standalone C++ scripts as output. These scripts will then provide users an easy way to deploy their deep learning models in their physics software and analysis frameworks.

This project will focus on development of some missing deep learning operations which will allow to build more complex networks within TMVA. The operators we are planning to implement will allow the inference code generator to support data preprocessing methods already supported by TMVA training methods, such as variable normalisation and decorrelation.




## Task ideas and expected results
 * Support of the existent TMVA data preprocessing methods in the new inference engine, in the code generator format

## Expected Results:
 * Production ready code-generator inference engine that supports common data preprocessing methods

## Requirements
Strong C++ skills, solid knowledge of deep learning. Familiarity with GPUs is a plus.

## Mentors
  * [Lorenzo Moneta](mailto:Lorenzo.Moneta@cern.ch)
  * [Sitong An](mailto:s.an@cern.ch)

Please DO NOT contact mentors directly by email, and instead please send project inquiries to MLSFT-GSOC@cern.ch with Project Title in the subject and relevant mentors will get in touch with you.

## Links
  * [http://root.cern/tmva](http://root.cern/tmva)
  * [TMVA source code](https://github.com/root-project/root/tree/master/tmva)
