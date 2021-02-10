---
title: TMVA Deep Learning Developments - Inference
layout: gsoc_proposal
project: TMVA
year: 2020
organization:
  - CERN
---

# Description

Toolkit for Multivariate Analysis [(TMVA)](http://root.cern/tmva) is a multi-purpose machine learning toolkit integrated into the [ROOT](http://root.cern) scientific software framework, used in many particle physics data analysis and applications. We provide in TMVA the functionality for building deep neural networks including fully connected, convolutional and recurrent layers. For the next stage of development of TMVA, we aim to provide a fast and convenient inference engine that takes ONNX model as input and produces compilation-ready standalone C++ scripts as output. These scripts will then provide users an easy way to deploy their deep learning models in their physics software and analysis frameworks.

This project will focus on development of some missing deep learning operations which will allow to build more complex networks within TMVA. We expect the student to implement LSTM/GRU in the code generation format. The student can choose to build this based on existing implementations in TMVA or build their own from scratch. However, this does not mean the proposal is limited to this. As in this project we expect the student to work closely with the supervisor and play a role in shaping the inference engine, we welcome proposals, suggestions or ideas that help us advance towards the goal of compilation of ML/DL model into C++ scripts for deployment and students can propose tasks/projects that they think are more suitable for this goal.



## Task ideas and expected results
 * Support for LSTM/GRU operator in the code generation format

## Expected Results:
 * Production ready code-generator inference engine component for RNN-based network

## Requirements
Strong C++ skills, solid knowledge of deep learning. Familiarity with GPUs is a bonus.

## Mentors
  * [Lorenzo Moneta](mailto:Lorenzo.Moneta@cern.ch)
  * [Sitong An](mailto:s.an@cern.ch)

Please DO NOT contact mentors directly by email, and instead please send project inquiries to MLSFT-GSOC@cern.ch with Project Title in the subject and relevant mentors will get in touch with you.

## Links
  * [http://root.cern/tmva](http://root.cern/tmva)
  * [TMVA source code](https://github.com/root-project/root/tree/master/tmva)
