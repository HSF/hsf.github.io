---
title: TMVA Deep Learning Developments - Decision Tree Inference, Expansion of Supported Format
layout: gsoc_proposal
project: TMVA
year: 2020
organization:
  - CERN
---

# Description

Toolkit for Multivariate Analysis [(TMVA)](http://root.cern/tmva) is a multi-purpose machine learning toolkit integrated into the [ROOT](http://root.cern) scientific software framework, used in many particle physics data analysis and applications. We provide in TMVA the functionality for building deep neural networks including fully connected, convolutional and recurrent layers.

We have already a very efficient inference engine for decision tree based ML algorithms developed in TMVA. However, currently this engine only supports xgBoost model files. We would like to expand this support to existing TMVA XML formats and Scikit-learn pickles, as well as to support serialization of the model in ROOT format and conversion of other models into ROOT format.




## Task ideas and expected results
 * Support of decision tree inference on TMVA XML formats and Scikit-learn pickles
 * Support serialization of the model in ROOT format
 * Support conversion of other models into ROOT format

## Expected Results:
 * Production ready inference engine that supports common data data formats for decision tree inference

## Requirements
Strong C++ skills, knowledge of decision tree based machine learning algorithms. Familiarity with GPUs is a huge plus.

## Mentors
  * [Lorenzo Moneta](mailto:Lorenzo.Moneta@cern.ch)
  * [Stefan Wunsch](mailto:stefan.wunsch@cern.ch)

Please DO NOT contact mentors directly by email, and instead please send project inquiries to MLSFT-GSOC@cern.ch with Project Title in the subject and relevant mentors will get in touch with you.

## Links
  * [http://root.cern/tmva](http://root.cern/tmva)
  * [TMVA source code](https://github.com/root-project/root/tree/master/tmva)
