---
project: HSF
title: RooFit - Pythonic interaction with the RooWorkspace
layout: gsoc_proposal
project: ROOT
year: 2023
difficulty: medium
mentor_avail: May-October
organization:
  - CERN
---

# Description

RooFit is a C++ library for the statistical analysis of data.
It provides tools for model building, fitting and statistical tests.
Since it is part of the ROOT data analysis framework, it also comes with an automatically generated Python interface.
RooFit models, data, and other information are managed in a so-called "RooWorkspace".
The user can build up the content with a domain-specific "factory" language inspired by C++, where snippets in this language are passed around as strings in the Python or C++ user code (see the tutorials linked below).

Since last year, the RooWorkspace also supports writing to and reading from JSON, where each model component is expressed as a mapping in JSON.
These mappings seamlessly translate to Python dictionaries, so it would be natural to support also interactively creating new objects in the workspace from Python dictionaries, using the JSON I/O backend.
This could replace the custom factory language for RooFit in Python, making the user experience more pythonic.
Pythons dynamic nature would also enable other Pythonizations that can make the RooFit model-building code more expressive.


## Task ideas and expected results

The main deliverable is a pythonic alternative to [RooWorkspace::factory()](https://root.cern.ch/doc/master/classRooWorkspace.html#ac4def578200696117aaf34c069c6d9d6), where the input is a Python dictionary that gets translated to a RooFit object in the same way as the mappings would get translated from a JSON file.
Much of the code for the JSON I/O can be reused to achieve this task, so the main challenge in this project will be to make the JSON I/O written in C++ work together with the pythonization code that is written in Python.
Furthermore, the successful student can make their own suggestions on how the interaction with the RooWorkspace could be made more pythonic and implement them.

For all the new developments, the student is expected to update the documentation and write tests and tutorials that showcase the new functionality.

## Evaluation Task
Interested students please contact [Jonas Rembser](mailto:Jonas.Rembser@cern.ch) for more details and an evaluation task.

## Requirements
Good knowledge of Python and C++.

## Mentors
  * **[Jonas Rembser](mailto:Jonas.Rembser@cern.ch)**
  * [Lorenzo Moneta](mailto:Lorenzo.Moneta@cern.ch)

## Links
  * [ROOT](https://root.cern/)
  * [RooFit](https://root.cern/topical/#roofit)
  * [RooFit tutorials](https://root.cern/doc/master/group__tutorial__roofit.html) in C++ and Python
    Look in paricular at the tutorials that **demonstrates the current way to interact with the RooWorkspace**:
    1. [Basic use of the RooWorkspace factory language](https://root.cern/doc/master/rf511__wsfactory__basic_8py.html)
    2. [Illustration of operator expressions in the workspace factory syntax](https://root.cern/doc/master/rf512__wsfactory__oper_8py.html)
  * Latest [presentation on the JSON serialization standard](https://docs.google.com/presentation/d/1tJeojfrc05cmc3PR3tk_t_3akng4Z0gciHH1VKHTXKA/edit#slide=id.p) (from the [(Re)interpretation of the LHC results for new physics](https://indico.cern.ch/event/1197680/) workshop)
  * Links to the codebase that you would work with:
    1. [Code to read/write RooFit models from/to JSON](https://github.com/root-project/root/tree/master/roofit/hs3)
    2. [Implementation of the existing RooWorkspace factory language](https://github.com/root-project/root/blob/master/roofit/roofitcore/src/RooFactoryWSTool.cxx)
    3. [RooFit pythonizations](https://github.com/root-project/root/tree/master/bindings/pyroot/pythonizations/python/ROOT/_pythonization/_roofit)
