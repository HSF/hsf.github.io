---
project: TMVA Developments
title: Improve Python interface for TMVA
author: Harshal Shende
date: 25.07.2022
year: 2022
layout: blog_post
logo: TMVA-logo.png
intro: |
 This project aims to simplify complex workflows and enhancement of the python interface, greatly reducing the amount of code that has to be written, including pythonizations for TMVA GUI and Hist functions and converters for PyROOT NumPy arrays to convert RTensor from and to PyROOT NumPy arrays.
---


## Abstract

This report outlines the deliverables completed for the TMVA development project, as a part of the Google Summer of Code 2022 program, under the CERN-HSF organization. Toolkit for Multivariate Analysis (TMVA) is a multi-purpose machine learning toolkit integrated into the ROOT scientific software framework. It comes with an automatically generated Python interface, which closely follows the C++ interface. This project aims to simplify complex workflows and enhancement of the python interface, greatly reducing the amount of code that has to be written, including pythonizations for TMVA GUI and Hist functions and converters for PyROOT NumPy arrays to convert RTensor from and to PyROOT NumPy arrays.

A pythonization is a piece of code that injects some new behaviour in a ROOT class, e.g. to add new methods, to make the class iterable from Python or to override arithmetic operators. Pythonizations can be implemented in Python or in C++ (via the Python/C API). In order to make it easier to use ROOT from Python, or to use a more pythonic syntax, PyROOT provides many pythonizations for ROOT classes. Callback is a function or callable object taking two arguments: the Python proxy class to be pythonized and its C++ name. In cppyy, Python callbacks, can be written to lazily pythonize a class:

```
from ._utils import _kwargs_to_tmva_cmdargs, cpp_signature


class TMVAClass(object):
@cpp_signature("")
def __init__(self, *args, **kwargs):
   # Redefinition of `TMVAClass` constructor for keyword arguments.
   args, kwargs = _kwargs_to_tmva_cmdargs(*args, **kwargs)
   self._init(*args, **kwargs)


def ClassMethod(self, *args, **kwargs):
    # TMVA::ClassMethod() function is pythonized with keyword CmdArg pythonization.
    args, kwargs = _kwargs_to_tmva_cmdargs(*args, **kwargs)
    return self._BookMethod(*args, **kwargs)
```
Following pythonizations and improvements have been implemented along with formatting and pythonization of tutorial files, making them more pythonic and less verbose.

## Deliverables

### [PR 1](https://github.com/root-project/root/pull/11069)
- Added pythonizations for the TMVA Classes and methods, using the Python standard way to pass arguments and keyword arguments to functions. 
- Updated tests and tutorials for the pythonizations, and added documentation. 
- Translated the TMVA tutorial files into python.

```
factory = TMVA.Factory(
    "TMVA_CNN_Classification",
    outputFile,
    V=False,
    ROC=True,
    Silent=False,
    Color=True,
    AnalysisType="Classification",
    Transformations=None,
    Correlations=False,
)
```

### [PR 2](https://github.com/root-project/root/compare/master...Harshalzzzzzzz:root:hist-pythonizations)
- Added pythonizations for TGraph and Hist methods, functions to create Histograms objects (TH1, TH2, TH3) from NumPy arrays and TGraph's objects from NumPy.


## Relevant Links

 - [Project Presentation](https://docs.google.com/presentation/d/15zMAqtXGF_JnOSiL8Pe5A9m1hezotmRIGW_Dgp9ZJHQ/edit#slide=id.p)
 - [Merged Contributions](https://bit.ly/merged_contributions)
