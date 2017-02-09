---
title: Parallelization and C++ implementation of ultra-fast detector simulation package, FALCON 
layout: gsoc_proposal
project: FALCON
organization: 
 - FSU
 - UFlorida
 - UdeA
---

## Description
[Falcon](http://inspirehep.net/record/1456803) is an ultra-fast non-parametric detector simulation package that automatically abstracts detector response, usually done by hand in fast-simulators used by particle physics experiments. Falcon uses [KDTrees](https://root.cern.ch/doc/v608/classTKDTreeBinning.html) to build a fast lookup table to map events at the parton shower level to events at the reconstruction level as described in the following [paper](http://inspirehep.net/record/1456803)

## Task ideas
* Design new Build/Simulator classes integrated with ROOT for training and testing
* Create a plugin for simpler event input from Delphes
* Create a purely C++ implementation (currently Falcon is written in python and c++)
* Parallelization and timing studies with the purely C++ implementation

## Expected results 
* Plugin for faster event input
* Standalone parallelized C++ prototype of Falcon
* Precise timing studies on several benchmark processes

## Requirements
Intermediate skills in C/C++, interest in detector simulation.
 
## Mentors 
  * [Harrison Prosper](mailto:harry@hep.fsu.edu)
  * [Sergei Gleyzer](mailto:Sergei.Gleyzer@cern.ch)
  * [Omar Zapata](mailto:Omar.Zapata@cern.ch)

## Links
  * [http://root.cern](http://root.cern)
