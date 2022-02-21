---
title: ROOT - Machine Learning Developments - Batch Generator for  training machine learning models 
layout: gsoc_proposal
project: ROOT
difficulty: medium/high
duration: 350
mentor_avail: April-October
year: 2022
organization:
    - CERN
---

## Description

Toolkit for Multivariate Analysis (TMVA) is a multi-purpose machine learning toolkit integrated into the ROOT scientific software framework, used in many particle physics data analysis and
applications. Since it is part of the ROOT data analysis framework, it comes with an automatically generated Python interface, which closely follows the C++ interface.
The goal of this project is to develop a generator in C++ and Python to read data from the ROOT I/O and input them to the Python machine learning tools such as Tensorflow/Keras and PyTorch.
The main aim of the generator is to efficiently input data from the ROOT I/O system to train machine learning models, and keep in memory only the data required to train a batch of events and not all
the data set. 

## Task ideas and expected results

The initial task will be to develop a Python generator for Tensorflow or PyTorch getting the data directly from a ROOT TTree, using the PyROOT interfaces for accessing the TTree.
The next task will be to write code can be integrated with the ROOT RDataFrame, allowing to directly generate a batch of events, possibly using multi-threads. 
Tests and tutorial examples are also expected to be developed, including the migration of existing tutorials to the pythonizations developed in this project.


## Evaluation Task

Interested students please contact the mentors for a warm-up and evaluation task.

## Requirements
 Good knowledge of Python and  C++, and very good familiarity with machine learning software tools such as Tensorflow or PyTorch. 

## Mentors
 * **[Lorenzo Moneta](mailto:Lorenzo.Moneta@cern.ch)**
 * [Sitong An](mailto:s.an@cern.ch)


## Links
 * [ROOT](https://root.cern/)
 * [TMVA](https://root.cern/manual/tmva/)
 * [RDataFrame](https://root.cern/manual/data_frame/)
