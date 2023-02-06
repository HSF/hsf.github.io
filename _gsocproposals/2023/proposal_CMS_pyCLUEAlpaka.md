---
title: PyCLUE - Include Alpaka backend 
layout: gsoc_proposal
project:
 - Patatrack 
year: 2023
difficulty: medium 
duration: 350 
mentor_avail: June-October
organization:
  - CERN 
---

## Description

[CLUE][clue] is a fast and fully parallelizable density-based clustering algorithm, optimized for high-occupancy scenarios, where the number of clusters is much larger than the average number of hits in a cluster ([Rovere et al. 2020][cluepaper]). The algorithm uses a grid spatial index for fast querying of neighbors and its timing scales linearly with the number of hits within the range considered. 
It is currently used in the CMS and CLIC event reconstruction software for clustering calorimetric hits in two dimensions (x,y) based on their energy.
CLUE is implemented in C++ and can execute on CPU and GPUs thanks to the [Alpaka][alpakapaper] performance portability library. CLUE has been generalized to k-dimensions and has been wrapped as python library ([CLUEstering][pyclue]) to become more beneficial for the scientific community. 
The current Python integration does not support Alpaka, and therefore GPU offloading can't be exploited. 
For this reason having Alpaka integrated in the Python library would be extremely useful to add support to parallel backend and heterogeneous devices as GPUs and FPGAs.  

## Expected Results

* Integrating Alpaka with Python bindings to provide GPU acceleration support.
* Designing an intuitive interface for selecting the preferred device and backend.
* Evaluating the performance of the clustering algorithm on benchmark datasets.
* Comparing the performance of CLUE with other clustering algorithms, such as HDBScan.
* Optimizing the conversion of data structures for optimal performance on various devices.
* Identifying and addressing performance bottlenecks in the algorithm.
* Implementing continuous integration and continuous delivery (CI/CD) testing for every device and backend.


## Evaluation Task

Interested students please contact clue-dev@cern.ch 

## Technologies

 * C++, Python

## Desirable Skills

 * Experience with Python library development
 * Experience with Python C++ bindings
 * Experience with C++17

## Mentors

 * [Felice Pantaleo](mailto:felice.pantaleo@cern.ch) (CERN)
 * **[Wahid Redjeb](mailto:wahid.redjeb@cern.ch) (CERN RWTH)**
 * [Marco Rovere](mailto:marco.rovere@cern.ch) (CERN)

## Links

 * [CLUE][clue]
 * [alpaka][alpaka]
 
[clue]: https://gitlab.cern.ch/kalos/clue
[pyclue]: https://github.com/cms-patatrack/CLUEstering
[cluepaper]: https://www.frontiersin.org/articles/10.3389/fdata.2020.591315/full
[alpakapaper]: https://arxiv.org/abs/1602.08477
[alpaka]: https://github.com/alpaka-group/alpaka
