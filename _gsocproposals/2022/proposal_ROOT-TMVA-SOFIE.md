---
title: ROOT - TMVA SOFIE Developments - Inference Code Generation for Deep Learning models
layout: gsoc_proposal
project: ROOT
difficulty: medium
duration: 175
mentor_avail: May-September
year: 2022
organization:
    - CERN
---

## Description

Toolkit for Multivariate Analysis (TMVA) is a multi-purpose machine learning toolkit integrated into the ROOT scientific software framework, used in many particle physics data analysis and
applications. Currently, we are developing a fast inference system in TMVA, called SOFIE,  that takes takes ONNX model as input and produces compilation-ready standalone C++ scripts as output. These scripts will then provide users an easy way to deploy their deep learning models in their physics software and analysis frameworks.

## Task ideas and expected results

This project will focus on development of some missing deep learning operations which will allow to build more complex networks within TMVA. Specifically, we propose to implement the inference
functionality of some ONNX operators in the code generation format. The student can choose to build this based on existing implementations in TMVA or other existing machine learning software tools or  build their own from scratch.
The expected result is a working implementation of modular operators classes that implement the operators as defined by the ONNX standards in the code generation format. The project requires also to
write the corresponding unit tests need to validate the written code


## Evaluation Task

Interested students please contact the mentors for a warm-up and evaluation task.

## Requirements
 * C++, familiarity with machine learning operators

## Mentors
 * **[Lorenzo Moneta](mailto:Lorenzo.Moneta@cern.ch)**
 * [Sitong An](mailto:s.an@cern.ch)


## Links
 * [ROOT](https://root.cern/)
 * [TMVA](https://root.cern/manual/tmva/)
 * [TMVA/SOFIE](https://github.com/root-project/root/blob/master/tmva/sofie/README.md)
 * [ONNX](https://onnx.ai)
 * [ONNX Operators](https://github.com/onnx/onnx/blob/master/docs/Operators.md)
