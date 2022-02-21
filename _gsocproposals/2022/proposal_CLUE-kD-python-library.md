---
title: CLUE-kD - a generic energy density based python library
layout: gsoc_proposal
project: Patatrack
year: 2022
difficulty: medium
duration: 350
mentor_avail: June-October
organization:
  - CERN
---

## Description

[CLUE][clue] is a fast and fully parallelizable density-based clustering algorithm, optimized for high-occupancy scenarios, where the number of clusters is much larger than the average number of hits in a cluster ([Rovere et al. 2020][cluepaper]). The algorithm uses a grid spatial index for fast querying of neighbors and its timing scales linearly with the number of hits within the range considered. 
It is currently used in the CMS and CLIC event reconstruction software for clustering calorimetric hits in two dimensions (x,y) based on their energy.
CLUE is implemented in C++ and can execute on CPU and GPUs thanks to the [Alpaka][alpakapaper] performance portability library. 
Many clustering applications are however written in Python and cannot easily benefit from the CLUE algorithm. 
For this reason making a generalization in k-dimensions of the CLUE algorithm available as a Python library would be very beneficial for the scientific community. 

## Expected Results

* Generalization of two dimensional clustering algo to arbitrary number of dimensions
* Configurable metrics for evaluating distance between points and energy density 
* CLUE algorithm can be configured and executed with a couple of lines of Python code
* CLUE algorithm interfaced with pandas dataframes
* Evaluation of algorithm clustering performance on evaluation datasets
* Compare with other clustering algorithms (e.g. HDBScan)

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
 * [Tony Di Pilato](mailto:tony.dipilato@cern.ch) (CERN CASUS)
 * **[Wahid Redjeb](mailto:wahid.redjeb@cern.ch) (CERN RWTH)**
 * [Marco Rovere](mailto:marco.rovere@cern.ch) (CERN)

## Links

 * [CLUE][clue]
 * [alpaka][alpaka]
 
[clue]: https://gitlab.cern.ch/kalos/clue
[cluepaper]: https://www.frontiersin.org/articles/10.3389/fdata.2020.591315/full
[alpakapaper]: https://arxiv.org/abs/1602.08477
[alpaka]: https://github.com/alpaka-group/alpaka