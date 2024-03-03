---
title: ROOT Superbuilds
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

Currently, ROOT is built as all-in-one package. We are working to create
a modular version of ROOT that provides a minimal base install of core features,
then later add functionality via incremental builds. This requires introducing
new layering mechanisms and extending the functionality of the existing ROOT
package manager prototype.


## Expected results
* Enhance the existing CMake build system rules to enable lazy building of packages
* Bootstrap "RootBase"
* Demonstrate "layered" lazy builds


## Requirements
CMake, C++, Python, Git, Github Actions.


## Mentors
  * [Vassil Vassilev](mailto:Vassil.Vassilev@cern.ch)
  * Second mentor: To be announced


## Links
  * [ROOT](https://root.cern/)
