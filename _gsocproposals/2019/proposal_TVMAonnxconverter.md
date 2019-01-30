---
title: Development of a ONNX - ROOT converter
layout: gsoc_proposal
project: TMVA
year: 2019
organization: CERN
---

## Description

ROOT (https://root.cern) is proposing a new Deep Learning framework via the TMVA package. As part of the proposal, TMVA will support fast inference of pretrained neural network models, defined with the ONNX (https://onnx.ai) format. ONNX files are read and written with [protobuf](https://developers.google.com/protocol-buffers/). To reduce footprint and external dependency, we propose storing neural network models in ROOT file format, following the definitions of [ONNX Intermediate Representation specifications](https://github.com/onnx/onnx/blob/master/docs/IR.md).


## Task ideas
  * Design and implement support for efficient storage of pre-trained neural network models in ROOT files with ROOT I/O
  * Develop a converter from ONNX file format to this newly implemented ROOT format model files

## Expected results
  * Efficient conversion strategy from ONNX to the ROOT file format
  * Benchmark of the IO performance and storage efficiency compared to protobuf

## Requirements
C++ skills, experience with large scale software development and machine learning tools is a plus.

## Mentors
  * [Sitong An](mailto:s.an@cern.ch)
  * [Stefan Wunsch](mailto:stefan.wunsch@cern.ch)
  * [Lorenzo Moneta](mailto:Lorenzo.Moneta@cern.ch)

## Links
  * [ROOT TMVA](http://root.cern/tmva)
  * [TMVA source code](https://github.com/root-mirror/root/tree/master/tmva)
  * [Protobuf](https://developers.google.com/protocol-buffers/)
  * [ONNX IR specs](https://github.com/onnx/onnx/blob/master/docs/IR.md)
