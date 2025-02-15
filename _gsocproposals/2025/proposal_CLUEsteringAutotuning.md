---
title: Development of an auto-tuning tool for the CLUEstering library
layout: gsoc_proposal
project: Patatrack
year: 2025
organization: CERN
difficulty: medium
duration: 350
mentor_avail: June-October
project_mentors:
  - email: simone.balducci@cern.ch
    organization: CERN UNIBO
    first_name: Simone
    last_name: Balducci
    is_preferred_contact: yes
  - email: felice.pantaleo@cern.ch
    organization: CERN
    first_name: Felice
    last_name: Pantaleo
---

## Description
[CLUE][clue] is a fast and fully parallelizable density-based clustering algorithm, optimized for high-
occupancy scenarios, where the number of clusters is much larger than the average number of hits
in a cluster ([Rovere et al. 2020][cluepaper]). The algorithm uses a grid spatial index for fast querying of
neighbors and its timing scales linearly with the number of points within the range considered. It is
currently used in the CMS and CLIC event reconstruction software for clustering calorimetric hits in
two dimensions based on their energy. The CLUE algorithm has been generalized to an arbitrary
number of dimensions and to a wider range of applications in [CLUEstering][cluestering], a general purpose
clustering library, with the backend implemented in C++ and providing a Python interface for
easier use. The backend can be executed on multiple backends (serial, TBB, GPUs, ecc) thanks
to the [Alpaka][alpakapaper] performance portability library. One feature currently lacking from CLUEstering
and that would be extremely useful for every user, is an autotuning of the parameters, that given
the expected number of clusters computes the combination of input parameters that results in the best
clustering.  
For this task, one of the options to be explored is “The Optimizer”, a Python library developed by
the Patatrack group of the CMS experiment which provides a collection of optimization algorithm,
in particular MOPSO (Multi-Objective Particle Swarm Optimization).

## Expected results
* Consider the best techniques and tools for the task
* Develop an auto-tuning tool for the parameters of CLUEstering
* Test it on a wide range of commonly used datasets
* Benchmark and profile to identify the bottlenecks of the tool and optimize it

## Evaluation Task
Interested students please contact simone.balducci@cern.ch

## Technologies
* C++, Python

## Desirable skills
* Experience with development in C++17/20
* Experience with GPU computing
* Experience with machine learning and optimization techniques
* Experience with development of Python libraries


## Links
  * [CLUE][clue]
  * [CLUEstering][cluestering]
  * [Alpaka][alpaka]

[clue]: https://gitlab.cern.ch/kalos/clue
[cluestering]: https://github.com/cms-patatrack/CLUEstering
[cluepaper]: https://www.frontiersin.org/articles/10.3389/fdata.2020.591315/full
[alpakapaper]: https://arxiv.org/abs/1602.08477
[alpaka]: https://github.com/alpaka-group/alpaka
