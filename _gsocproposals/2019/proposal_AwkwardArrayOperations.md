---
title: Awkward Array Operations
layout: gsoc_proposal
project: IRIS-HEP
year: 2019
organization:
  - Princeton
---

## Description

Most particle physics analysis today is performed by physicists writing programs to traverse nested data structures. These one-time analysis programs suffer from several issues:

  * data structures linked with pointers/references are non-sequential in memory;
  * dynamic memory allocation (to make nested data) is not even possible on some devices, such as GPUs;
  * branchy code (frequent `if` statements) make poor use of Single Instruction Multiple Data (SIMD) devices;
  * there's a steep trade-off between interactive analysis in Python and fast execution in C++.

In other academic fields and in data science, these issues are avoided by expressing analysis logic in SQL or a suite of array operations in MATLAB or Numpy. Particle physics, however, relies crucially on variable-sized, nested data structures that don't fit neatly into tables or arrays. Every proton collision at the LHC produces a different number of electrons, gluons, and quarks with complex interrelationships.

We have been developing extensions to array programming concepts for nested, heterogeneous, and cross-linked data in a library called [awkward-array](https://github.com/scikit-hep/awkward-array). This library follows the syntax of Numpy, but for complex structures:

```python
>>> import awkward

>>> array = awkward.fromiter(
[[1.1, 2.2, None, 3.3, None],
 [4.4, [5.5]],
 [{"x": 6, "y": {"z": 7}}, None, {"x": 8, "y": {"z": 9}}]])

>>> (array + 100).tolist()
[[101.1, 102.2, None, 103.3, None],
 [104.4, [105.5]],
 [{'x': 106, 'y': {'z': 107}}, None, {'x': 108, 'y': {'z': 109}}]]
```

Like Numpy, a single expression performs calculations across whole datasets (alleviating the tradeoff between interactivity and performance) that are contiguous by type ([column-oriented data](https://towardsdatascience.com/the-beauty-of-column-oriented-data-2945c0c9f560)) and are fully portable to GPUs. Our set of awkward-array operations is broader than those needed for flat-array processing, and we are discovering new operations by translating traditional particle physics programs into array-centric scripts.

In this project, we would like you to create a library of precompiled awkward-array operations. Our current implementation of awkward-array is built in pure Numpy, which is portable but not as efficient as dedicated routines. The project will focus on good software engineering principles to build a maintainable infrastructure. We don't expect an optimized implementation of every operation by the end of the summer, just a clearly organized space to put new implementations when we need them.

## Task ideas

  * Extend the Python package infrastructure to allow layered installation: Numpy-only, precompiled routines for CPUs, and perhaps precompiled routines for GPUs. We expect [pybind11](https://pybind11.readthedocs.io/en/stable/) would be a good glue between Python and C++ (and possibly CUDA).
  * Develop a robust suite of unit tests to continuously verify equivalence of the implementations.
  * Document the organization of the new libraries for future developers.
  * Possibly incorporate a SIMD library, such as [Vc](https://github.com/VcDevel/Vc), [VecOps](https://root.cern.ch/doc/v614/group__tutorial__vecops.html), or [xsimd](https://github.com/QuantStack/xsimd) for CPU vectorization.
  * Possibly incorporate awkward-array operations into [Pandas](https://pandas.pydata.org).

## Expected results

By the end of the summer, we would like to see a well-established library structure. Even if the set of implemented operations is incomplete, it should be clear how the library will grow and be maintained.

## Desirable Skills

  * Good software engineering practices; well-organized coding.
  * Fluency in modern C++ and enough familiarity with Python to bridge the gap. (CUDA/GPU programming is optional.)
  * Rigorous testing and documentation.
  * Interest in data structures and optimization.

## Mentors

  * [Jim Pivarski](mailto:pivarski@princeton.edu)
  * [David Lange](mailto:david.lange@cern.ch)

## Links

  1. [awkward-array](https://github.com/scikit-hep/awkward-array)
  2. [uproot](https://github.com/scikit-hep/uproot)
  3. [Introduction to array-centric analysis for physicists](https://github.com/jpivarski/jupyter-talks/blob/master/2018-09-28-uproot3-update/uproot-3-evaluated.ipynb)
  4. [Presentation on array-centric analysis for physicists](https://indico.cern.ch/event/745288/contributions/3080203/attachments/1748811/2832682/pivarski-hsf-numpy.pdf)
