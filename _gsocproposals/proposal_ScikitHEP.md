---
title: Efficient Python routines for analysis on massively multi-threaded platforms - Python bindings for the Hydra C++ library
layout: plain
project: SciKit-HEP
organization:
 - Cincinnati
 - DianaHEP
---

## Description
The Hydra project consists of a header-only C++ template library designed for data-intensive analysis in massively multi-threaded environments, with a focus on performance and precision. Hydra is coded on top of Thrust and STL, and exploits heavily static polymorphism in order to execute the same source code deploying on OpenMP, TBB and CUDA enabled devices.
Currently, Hydra implements functionality to generate large samples of  weighted and unweighted phase-space Monte Carlo, to perform multidimensional numerical integration and likelihood fits, and to evaluate functions in parallel over large data sets. The typical speed up compared to traditional tools ranges from 10x to 10000x faster depending on the use case.

The Scikit-HEP project is a community-driven and community-oriented project with the aim of providing Particle Physics at large with a Python package containing core and common tools; it's goal is similar to that of Astropy in Astronomy.
The project initiated in Autumn 2016 and is presently under consolidation.

The GSoC participant will develop the Python interface to Hydra, to make it a package affiliated with Scikit-HEP, i.e. a package that is not part of the core tools but builds on the ideas of Scikit-HEP, conforms to a series of rules on usage, documentation, etc., and exposes extra functionality for specific purposes.

## Task ideas
The main tasks necessary to achieve the project goals are the following:

* Use Boost.Python, pybind11 and PyBindGen to prepare the core code to expose the Hydra classes to Python.
* Set up a series of simple examples on how to use the Python package for well-defined tasks such as the generation of large samples of phase-space decays.
* Prepare an adequate documentation and test suite for the Python package.

## Expected results
First release of a Python interface for Hydra, with set of basic examples of use case.

## Requirements
* Good API design skills.
* C++ and Python expertise.
* Working experience developing Python bindings is a big plus.

## Mentors
  * [Antonio Augusto Alves Jr](mailto:aalvesju@cern.ch): Author of Hydra project and its main developer
  * [Eduardo Rodrigues](mailto:eduardo.rodrigues@cern.ch): Scikit-HEP core team member

## Links
  * [Hydra](https://github.com/MultithreadCorner/Hydra)
  * [Scikit-HEP GitHub repository](https://github.com/scikit-hep/scikit-hep)
  * [Scikit-HEP homepage](http://scikit-hep.org/) (under development)
  * [Boost.Python](https://wiki.python.org/moin/boost.python): exposes C++ classes functions and objects to Python, and vice-versa, using just C++ compiler
  * [pybind11](https://github.com/wjakob/pybind11): similar to Boost.Python, but with a clean header-only implementation for C++11-capable compilers
  * [PyBindGen](http://code.google.com/p/pybindgen): Python bindings code generator for pure C or C++ APIs. The generator is written in Python and has low complexity. The generated code is clean, efficient, and highly readable
