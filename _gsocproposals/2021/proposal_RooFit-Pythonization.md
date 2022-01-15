---
title: RooFit Developmnt - Intuitive Python bindings for RooFit
layout: gsoc_proposal
project: ROOT
year: 2021
organization:
  - CERN
---

# Description


RooFit is a C++ library for statistical analysis of data. It provides tools for model building, fitting and statistical tests. Since it is part of the ROOT data analysis framework, it comes with an automatically generated Python interface, which closely follows the C++ interface.
The goal of this project is to enhance the Python interface to make more "pythonic", i.e. easier to use. Moreover, some RooFit workflows are not possible to implement currently on the Python side without adding extra code requiring expertise of  ROOT and knowledge of C++ and Python.
Using the existing interfaces, short Python functions will be implemented, which will reduce the amount of code that users have to write and greatly simplified complex workflows.




## Task ideas and expected results
The initial task of the student will be adding Pythonizations to major RooFit API commands, such as `RooAbsPdf::fitTo`, using the Python
standard way to pass optional arguments to functions.
Afterwards, more advanced Pythonizations will be developed, making the analysis code using RooFit more Pythonic.
The RooFit interfaces requiring currently extra code in order to be used from Python, will be adapted such that some workflows will be greatly simplified. One of such example is the combination of RooFit data sets in in order to perform  a combined fit.
Tests and tutorial examples are also expected to be developed, including the migration of existing tutorials to the pythonizations developed in this project.


## Requirements
Good knowledge of Python, intermediate C++, some basic understanding of Math and Statistics


## Mentors
  * **[Jonas Rembser](mailto:Jonas.Rembser@cern.ch)**
  * [Lorenzo Moneta](mailto:Lorenzo.Moneta@cern.ch) 

Interested students please contact the mentors for a warm-up and evaluation task. 

## Links
  * [ROOT](https://root.cern/)
  * [RooFit](https://root.cern/topical/#roofit)
