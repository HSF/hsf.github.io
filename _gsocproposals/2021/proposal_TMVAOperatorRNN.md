---
title: TMVA Deep Learning Developments: Inference Code Generation for Recurrent Neural Networks
layout: gsoc_proposal
project: ROOT
year: 2021
organization:
    - CERN
---

## Description

Toolkit for Multivariate Analysis (TMVA) is a multi-purpose machine learning toolkit integrated into the ROOT scientific software framework, used in many particle physics data analysis and applications. Currently, we are developing a fast inference system in TMVA that takes takes ONNX model as input and produces compilation-ready standalone C++ scripts as output. These scripts will then provide users an easy way to deploy their deep learning models in their physics software and analysis frameworks.

## Task ideas and expected results

This project will focus on development of some missing deep learning operations which will allow to build more complex networks within TMVA. Specifically, we propose to implement the inference functionality of ONNX RNN, LSTM and GRU operators in the code generation format. The student can choose to build this based on existing implementations in TMVA or build their own from scratch.

The expected result is a working implementation of modular operator classes that implement the RNN, LSTM and GRU operators as defined by the ONNX operator standards in the code generation format.

## Requirements
 * C++, familiarity with RNN

## Mentors
 * [Lorenzo Moneta](mailto:Lorenzo.Moneta@cern.ch)
 * **[Sitong An](mailto:s.an@cern.ch)**

## Links
 * [ROOT](https://root.cern/)
 * [TMVA](https://root.cern/manual/tmva/)
 * [ONNX](https://onnx.ai)
 * [ONNX Operators](https://github.com/onnx/onnx/blob/master/docs/Operators.md)
