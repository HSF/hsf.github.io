---
title: IRIS-HEP - Uproot-Dask
layout: gsoc_proposal
project: IRIS-HEP
year: 2022
difficulty: high
duration: 350
mentor_avail: June-August
organization:
  - princeton
---

# Description

[Uproot](https://github.com/scikit-hep/uproot4) is a pure Python reader and writer of the ROOT file format, the primary format for High Energy Physics data. It converts ROOT files on disk to and from NumPy arrays, [Awkward Arrays](https://github.com/scikit-hep/awkward-1.0), and Pandas DataFrames for analysis.

Uproot is primarily "eager," in that a request for ROOT data to be read into memory is executed immediately, with the exception of one function, [uproot.lazy](https://uproot.readthedocs.io/en/latest/uproot.behaviors.TBranch.lazy.html). This function is currently only supported by Uproot's Awkward Array backend, and it relies on the VirtualArray and PartitionedArray array types that are being deprecated in favor of a new [dask-awkward](https://github.com/ContinuumIO/dask-awkward/) collection type. [Dask](https://dask.org/) is an industry standard library for delayed and distributed computation in Python.

The goal of this project would be to reimplement `uproot.lazy` (now `uproot.dask`) using the new `dask.awkward` collection. In addition, the new function should also support the NumPy and Pandas backends, leveraging the [dask.array](https://docs.dask.org/en/stable/array.html) and [dask.dataframe](https://docs.dask.org/en/stable/dataframe.html) collection types in Dask.

It is part of a larger project to update Uproot 4 to use Awkward Array version 2, of which the migration to Dask is one part. `uproot.dask` will be a key feature of Uproot version 5.

## Project tasks

As written, these tasks are not sequential: implementation will likely be iterative, and your understanding should grow throughout the process.

  * Understand the current implementation of `uproot.lazy`, how Uproot reads data from local and remote files, schedules I/O and interpretation tasks internally, and how it uses Awkward version 1 to build a lazy array.
  * Understand the new `dask.awkward` collection type, how to substitute the deprecated VirtualArray and PartitionedArray node types.
  * Understand the metadata available in ROOT files and possibly modernize the [uproot3.numentries](https://github.com/scikit-hep/uproot3/blob/54f5151fb7c686c3a161fbe44b9f299e482f346b/uproot3/tree.py#L2087-L2150) function to scan a large set of files for metadata.
  * Implement the new `uproot.dask` for the NumPy backend (first; should be the easiest of the three).
  * Implement it for the Awkward Array backend, using all of the above.
  * Implement it for DataFrames.
  * Test in a variety of cases: only constructing the DAG, synchronous and futures-based evaluation in one core, multithreading, multiprocessing, and distributed. All single-process tests should be added to Uproot's [continuous testing suite](https://github.com/scikit-hep/uproot4/tree/main/tests).
  * Document the new function with inline docstrings, to populate the [online reference](https://uproot.readthedocs.io/), and add "how-to" explanations in the [Getting started guide](https://uproot.readthedocs.io/en/latest/basic.html).
  * Present and/or demo the new function, fully integrated into Dask (with the dashboard and other diagnostics).
  * Collaborate with the larger Uproot 5 project.

## Expected results

The new `uproot.dask` function should return a Dask DAG node ([high level](https://docs.dask.org/en/stable/high-level-graphs.html)), suitable for further processing in `dask.array`, `dask.dataframe`, or the new `dask.awkward`. All modes of processing: synchronous, asynchronous, multithreaded, multiprocessing, and distributed, should work without unnecessary copying of data. This should be demonstrated with diagnostics.

## Evaluation Task

Interested students please contact Jim (pivarski@princeton.edu) for an evaluation task.

## Requirements

  * Strong Python skills
  * Familiarity with Dask

## Mentors

  * **[Jim Pivarski](mailto:pivarski@princeton.edu)**

## Links

  * [Uproot](https://github.com/scikit-hep/uproot4), [documentation](https://uproot.readthedocs.io/)
  * [Awkward Array](https://github.com/scikit-hep/awkward-1.0), [documentation](https://awkward-array.org/)
  * [Dask](https://dask.org/), [documentation](https://docs.dask.org/)
