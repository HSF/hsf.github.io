---
title: Precompiled Analysis Array Operations
layout: gsoc_proposal
project: IRIS-HEP
year: 2019
organization:
  - Princeton
---

## Description

Most particle physics analysis today is performed by writing highly branching code to traverse nested data structures. These analysis programs suffer from several issues:

  * data structures linked with pointers require non-sequential memory access
  * dynamically allocated memory (to make nested data) is not even possible on some devices, like GPUs
  * branching code uses Single Instruction Multiple Data (SIMD) devices poorly
  * there's a steep trade-off between interactive analysis in Python and fast execution in C++.

In other academic fields and in data science, these issues are avoided by expressing analysis logic in SQL or an array programming language like MATLAB or Numpy. Particle physics, however, relies crucially on variable-sized, nested data structures that don't fit neatly into tables or arrays.

We have been developing extensions to array programming concepts for nested and heterogeneous data in a library called [awkward-array](https://github.com/scikit-hep/awkward-array). This library follows the syntax of Numpy, but for complex data:

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

Like array programming, a single expression performs calculations across whole datasets (alleviating the tradeoff between interactivity and performance) that are contiguous by type ([column-oriented data](https://towardsdatascience.com/the-beauty-of-column-oriented-data-2945c0c9f560)) and are fully portable to GPUs. Our working set of primitives is broader than those needed for flat-array processing, and we are discovering new operations by expressing particle physics programs as array-centric scripts.

In this project, we would like a student to create a library of pre-compiled primitives that efficiently use CPU and GPU vectorization. The project will focus on good software engineering principles to build a maintainable infrastructure.

## Task ideas

  * FIXME

## Expected results

FIXME

## Desirable Skills

  * FIXME

## Mentors

  * [Jim Pivarski](mailto:pivarski@princeton.edu)
  * [David Lange](mailto:david.lange@cern.ch)

## Links

  1. [awkward-array](https://github.com/scikit-hep/awkward-array)
  2. [uproot](https://github.com/scikit-hep/uproot)
  3. [Introduction to array-centric analysis for physicists](https://github.com/jpivarski/jupyter-talks/blob/master/2018-09-28-uproot3-update/uproot-3-evaluated.ipynb)
  4. [Presentation on array-centric analysis for physicists](https://indico.cern.ch/event/745288/contributions/3080203/attachments/1748811/2832682/pivarski-hsf-numpy.pdf)
