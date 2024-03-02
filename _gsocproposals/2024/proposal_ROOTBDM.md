---
title: Improving performance of BioDynaMo using ROOT C++ Modules
layout: gsoc_proposal
project: ROOT
year: 2024
organization: 
  - CERN
  - CompRes
---

## Description

The [ROOT](https://root.cern/) is a framework for data processing, born at CERN,
at the heart of the research on high-energy physics. Every day, thousands of
physicists use ROOT applications to analyze their data or to perform
simulations. The ROOT software framework is foundational for the HEP ecosystem,
providing capabilities such as IO, a C++ interpreter, GUI, and math
libraries. It uses object-oriented concepts and build-time modules to layer
between components. We believe additional layering formalisms will benefit ROOT
and its users.

BioDynaMo is suite that enables users to perform simulations of previously
unachievable scale and complexity, making it possible to tackle challenging
scientific research questions. BioDynaMo leverages technologies such as ROOT to
enable large scale computations. The project has wide range of applications in
the field of cancer research, epidemiology, and social sciences.

BioDynaMo incorporates ROOT as a subsystem and uses the ROOT data storage
facilities to provide efficient reflection information about user-defined
simulation actions written as C++ classes. This project is about upgrading the
reflection system to use C++ modules improving scalability of user-defined
classes.


## Expected results
* Rework the cmake rules to incorporate efficiently ROOT via `FetchContent`
* Replace invocations of `genreflex` in favor of `rootcling`
* Enable C++ modules in `rootcling`
* Produce a comparison report


## Requirements
C++, CMake Python, Git, knowledge of ROOT is a plus.


## Mentors
  * [Vassil Vassilev](mailto:Vassil.Vassilev@cern.ch)
  * [Lukas Breitwieser](mailto:lukas.johannes.breitwieser@cern.ch)
  * [Tobias Duswald](mailto:tobias.duswald@cern.ch)
  * [Fons Rademakers](mailto:Fons.Rademakers@cern.ch)


## Links
  * [ROOT](https://root.cern/)
  * [BioDynaMo](https://github.com/BioDynaMo/biodynamo)
  * [C++ Modules](https://github.com/root-project/root/blob/master/README/README.CXXMODULES.md)
