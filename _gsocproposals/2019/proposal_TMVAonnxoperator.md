---
title: Implementation of ONNX operators for Tensor Manipulation and Deep Learning
layout: gsoc_proposal
project: TMVA
year: 2019
organization:
  - CERN
  - KIT
---

## Description

[ROOT](https://root.cern) is proposing a new Deep Learning framework in the TMVA package. As part of the proposal, TMVA will support fast inference of pretrained neural network models, defined with the [ONNX](https://onnx.ai) format. The ONNX format designed to be able to describe any model generated from mainstream Deep Learning Frameworks, such as Tensorflow, PyTorch, and MXNet. ONNX models are defined with operators, with each operator representing a fundamental operation on the tensor in the computational graph. These operators range from the very simple and fundamental ones on tensor manipulation (such as "Concat"), to more complex ones like "BatchNormalization" and "LSTM". Refer to [this important document](https://github.com/onnx/onnx/blob/master/docs/Operators.md) for a full list of definitions on ONNX operators.

This GSoC project proposes to implement a subset of these ONNX operators for TMVA in C++, focusing on Tensor Manipulation and basic Machine Learning operations, with an extension to collaborate with the other GSoC student for TMVA to implement more complex RNN-related operators.

## Task ideas
  * On the first stage, implement ONNX operators for crucial tensor manipulation operations. These are numpy-like operators, including "Clip", "Compress", "Concat", "Expand", "Flatten", "Gather", "OneHot", "Reshape", "Scatter", "Shape", "Split", "Size", "Slice", "Squeeze", "Tile", "Transpose", "Unsqueeze", and "Where".
  * Next, depending on the student's progress, further implement a small selected subset of basic Deep Learning operators. For example, these could be (but are not limited to) "LpNormalization", "InstanceNormalization" and "Selu".
  * Finally, in collaboration with the other GSoC student working on the sister project "Development of LSTM and GRU layers in TMVA", implement Deep Learning operators "GRU", "LSTM" and "RNN" as well as supporting operators  "StringNormalizer" and "TfIdfVectorizer".
  * Provide unit testing for the operators implemented.
  * Profile and benchmark the performance of the operators implemented.

## Expected results
  * Efficient implementation of ONNX operators on Tensor Manipulation and basic Deep Learning operations.
  * Implementation of the RNN-related operators in teamwork.
  * Benchmark of the performance of the operators against numpy and major Deep Learning Frameworks.

## Requirements
C++ skills and knowledge of basic Machine Learning concepts, experience with large scale software development and low-level implementation of fundamental Data Science and Machine Learning operations is a plus.

## Mentors
  * [Sitong An](mailto:s.an@cern.ch)
  * [Stefan Wunsch](mailto:stefan.wunsch@cern.ch)
  * [Lorenzo Moneta](mailto:Lorenzo.Moneta@cern.ch)

## Links
  * [ROOT TMVA](http://root.cern/tmva)
  * [TMVA source code](https://github.com/root-mirror/root/tree/master/tmva)
  * [ONNX IR specs](https://github.com/onnx/onnx/blob/master/docs/IR.md)
  * [ONNX Operator Definitions](https://github.com/onnx/onnx/blob/master/docs/Operators.md)
  * [TMVA RTensor Class](https://github.com/root-project/root/pull/3221)
