---
title: Optimization of Neural Network Operations
layout: gsoc_proposal
project: TMVA
year: 2019
organization:
  - CERN
  - KIT
---

## Description

ROOT provides via the TMVA package a new Deep Learning framework, which allows to build complex Machine Learning architectures which can be used for data classification or regressions. In addition to standard dense layers, this new Deep Learning framework supports also convolutional or recurrent layers.
The candidate will be working for TMVA, with the main goal to optimize the performance to evaluate trained deep learning methods and to compare the performance results with other existing Machine Learning libraries. Optimal performances are crucial for real time exploitation of Machine Learning tools in High Energy Physics.


## Task ideas
* Benchmark the most CPU consuming operations when evaluating a neural network on CPU using different backends such as BLAS and Eigen
* Develop some of these operations using the internal vectorization library of ROOT, VecCore
* Integrate the optimized version into ROOT for low latency inference of neural network models

## Expected results
* Report on performance benchmarking of different backends
* Optimization and vectorization of ROOT/TMVA Deep Neural Network operations


## Requirements
C++ skills, experience with large scale software development, vectorization, linear algebra libraries and profiling tools is a plus.

## Mentors
  * [Lorenzo Moneta](mailto:Lorenzo.Moneta@cern.ch)
  * [Stefan Wunsch](mailto:stefan.wunsch@cern.ch)

## Links
  * [ROOT TMVA](http://root.cern/tmva)
  * [TMVA source code](https://github.com/root-mirror/root/tree/master/tmva)
  * [BLAS](http://www.netlib.org/blas/)
  * [Eigen](http://eigen.tuxfamily.org/index.php?title=Main_Page)
