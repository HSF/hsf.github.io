---
title: FALCON - optimize fast detector simulation package and multi-objective regression
layout: gsoc_proposal
project: FALCON
year: 2019
organization: 
 - FSU
 - Florida
 - OProject
---

## Description
[Falcon](http://inspirehep.net/record/1456803) is an ultra-fast non-parametric detector simulation package that automatically abstracts detector response, usually done by hand in fast-simulators used by particle physics experiments. Falcon uses [KDTrees](https://root.cern.ch/doc/v608/classTKDTreeBinning.html) to build a fast lookup table to map events at the parton shower level to events at the reconstruction level as described in the following [paper](http://inspirehep.net/record/1456803).

The goal of this project is to optimize the structure of the code by extending the KDTreeBinning class to include automatic re-partitioning as more points are added (ie. refining each bin) and capability to rapidly and efficiently access points inside of each partition. Additionally, the goal is to integrate multi-target regression capability into Falcon. 

## Task ideas and expected results
  * Optimize Falcon’s design for maximal timing efficiency.
  * Improve the training and KDTree binning and lookup time by using the latest ROOT classes.


## Requirements
Strong development skills, good knowledge of C++ and Python. Interest in Machine Learning algorithms and applications.

## Mentors 
  * [Harrison Prosper](mailto:sft-gsoc-ml@googlegroups.com?subject=FALCON)
  * [Sergei Gleyzer](mailto:sft-gsoc-ml@googlegroups.com?subject=FALCON)
  * [Omar Zapata](mailto:sft-gsoc-ml@googlegroups.com?subject=FALCON)

## Links
  * [http://root.cern](http://root.cern)
