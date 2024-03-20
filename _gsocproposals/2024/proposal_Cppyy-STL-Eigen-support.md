---
title: STL/Eigen - Automatic conversion and plugins for Python based ML-backends 
layout: gsoc_proposal
project: Cppyy
year: 2024
difficulty: medium
duration: 350
mentor_avail: June-October
organization:
  - CompRes
---

## Description

Cppyy is an automatic, run-time, Python-C++ bindings generator, for calling C++ from Python and Python from C++. Cppyy uses pythonized wrappers of useful classes from libraries like STL and Eigen that allow the user to utilize them on the Python side. Current support follows container types in STL like std::vector, std::map, and std::tuple and the Matrix-based classes in Eigen/Dense. These cppyy objects can be plugged into idiomatic expressions that expect Python builtin-types. This behaviour is achieved by growing pythonistic methods like `__len__` while also retaining its C++ methods like `size`.

Efficient and automatic conversion between C++ and Python is essential towards high-performance cross-language support. This approach eliminates overheads arising from iterative initialization such as comma insertion in Eigen. This opens up new avenues for the utilization of Cppyy’s bindings in tools that perform numerical operations for transformations, or optimization.

The on-demand C++ infrastructure wrapped by idiomatic Python enables new techniques in ML tools like JAX/CUTLASS. This project allows the C++ infrastructure to be plugged into at service to the users seeking high-performance library primitives that are unavailable in Python.

## Project Milestones

* Extend STL support for std::vectors of arbitrary dimensions
* Improve the initialization approach for Eigen classes
* Develop a streamlined interconversion mechanism between Python builtin-types, numpy.ndarray, and STL/Eigen data structures
* Implement experimental plugins that perform basic computational operations in frameworks like JAX
* Work on integrating these plugins with toolkits like CUTLASS that utilise the bindings to provide a Python API


## Requirements

* C++ programming
* Python programming
* Familiarity with STL types and the Eigen library is an advantage

## Mentors
* **[Aaron Jomy](mailto:aaron.jomy@cern.ch)**
* [Wim Lavrijsen](mailto:wlavrijsen@lbl.gov)
* [Vassil Vassilev](mailto:vvasilev@cern.ch)
* [Jonas Rembser](mailto:jonas.rembser@cern.ch)

## Links
* [Repo](https://github.com/wlav/cppyy)
