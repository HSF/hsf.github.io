---
project: IRIS-HEP
title: Uproot + Dask: Blog 1
author: Kush Kothari
date: 25.07.2022
year: 2022
layout: blog_post
logo: iris-hep-logo.png
intro: |
  Introducing lazy Dask workflows to Uproot
---

### Introduction
Hello peeps, this is Kush Kothari, a CS student from Mumbai, India. This is going to be a short report on my work on Uproot. The primary project goal is to upgrade Uproot to use AwkwardArrays v2 and to create the `uproot.dask` function. This function is a reimplementation of `uproot.lazy`, and now uses Dask's ability to delay a task's computation. This project is a major revamp of the structure and codebase of Uproot and the changes will result in a new major version of Uproot, i.e. Uproot v5.

The work I did over the past 6 weeks is majorly split over 6 Pull Requests into Uproot.

### Dask Arrays
[This PR](https://github.com/scikit-hep/uproot5/pull/578) begun as the evaluation task for GSoC and was continued into the coding period. It introduces the `uproot.dask` function using the Dask Array collection. Setting `library=np` makes the function return a Python dict of dask-arrays, each representing a single TBranch of the root file. These dask-arrays are computed into Numpy arrays on calling `.compute()`. This also implements some features previously present in `uproot.lazy` like the `step_size` parameter that can be used to control the size of chunks in the dask arrays.

### Delay in opening files
[This PR](https://github.com/scikit-hep/uproot5/pull/603) solves [the feature request](https://github.com/scikit-hep/uproot5/issues/602) of delaying the opening of the ROOT files. Sometimes, reading the metadata from ROOT files is itself quite an expensive operation. We may want to delay this using dask. However, to build the dict of dask arrays, we need to know the keys. Now, when `uproot.dask([filename1, filename2...], open_files=False)` is called, Uproot only opens the first file to read the key names. Assuming the same key names in all files and making use of dask's "unknown chunk sizes" feature, the opening of the rest of the files is delayed through a dask delayed node.

### Num_entries
Uproot 3 had a `numentries` function which was not ported to Uproot 4. This feature was requested [here](https://github.com/scikit-hep/uproot5/issues/197) and introduced in [PR 609](https://github.com/scikit-hep/uproot5/pull/609). This function skips reading a lot of the metadata in the ROOT file, thus quickly providing the value of `fEntries` in the TTree metadata.

### Removing uproot.lazy
At this point, Uproot had transitioned to Uproot 5 on the main branch, and Uproot 4 in a secondary branch. A [small PR](https://github.com/scikit-hep/uproot5/pull/615) just removed `uproot.lazy`'s  implementation from Uproot 5, while keeping the docstring intact (since Uproot 4 and 5 share online documentation). Instead, calling `uproot.lazy` in Uproot 5 raises a `NotImplementedError`.

### Awkward v2 update
This was a major one. All instances of awkward usage in Uproot were upgraded to use Awkward v2. This is part of the change from Uproot 4 to Uproot 5. [This PR](https://github.com/scikit-hep/uproot5/pull/620) involved a lot of debugging and running of tests. I am really thankful for all the support I received from my mentor Dr Jim Pivarski during this time.

### Dask-Awkward Support
Currently, a work-in-progress, [this PR](https://github.com/scikit-hep/uproot5/pull/652) extends the `uproot.dask` function to use the newly developed `dask_awkward` collection. While a basic working model is ready, I am currently working on optimizing the Dask graph with the help of Douglas Davis, the maintainer of `dask_awkward`.
