---
title: Generalise the ROOT Parallel Declarative Analysis Framework to non-HEP Big Data
layout: gsoc_proposal
project: ROOT
year: 2018
organization: CERN
---

## Description

The [ROOT](https://root.cern/) Software Framework is the cornerstone of all software stacks used by High Energy Physics (HEP) experiments, at CERN and other prestigious laboratories. It provides components which are fundamental for the entire data processing chain, from particle collisions to final publications, including final user data analysis, including modern machine learning techniques.

ROOT features a declarative analysis sub-system, [TDataFrame](https://root.cern.ch/doc/master/classROOT_1_1Experimental_1_1TDataFrame.html), which has proven to be a solution to scale in-process parallel HEP data analysis to ~100 cores with a simple and intuitive programming model.

This project aims to build up on this result increasing the impact of TDataFrame in other disciplines dealing with Big Data such as Astrophysics or Genomics and even non scientific activities - and this exploiting both the Python and C++ interfaces of TDataFrame.

## Task ideas
* Expand the set of data formats which can be accessed by TDataFrame beyond ROOT, CSV and experiment specific ones. This step is to be performed writing adequate TDataSources. More precisely, widely adopted data formats in data science such as [Parquet](https://parquet.apache.org/), [HDF5](https://support.hdfgroup.org/HDF5/) or [Avro](https://avro.apache.org/). The TDataSources will be developed as standalone packages, in a first phase external to ROOT itself but depending on it. These can be properly integrated, if time allows, within the present ROOT CMake based build system.
* Increase the programmability of TDataFrame allowing users to write customised data transformations in order to allow non-HEP users to take advantage from the high performance delivered by TDataFrame to take care of tasks which are natively not supported by the tool. These developments require writing highly performant code, natively ready for parallelism. The increase of programmability will imply a design effort to distil a minimal, expressive and powerful programming model to describe the operations to carry out on the data, for example exploiting a streams-based formalism.
* As a spin-off of the previous idea, synergy with the machine learning subsystem of ROOT. 

## Expected results
Working implementation of one or more TDataSources for the aforementioned formats

## Requirements
C++, Parquet/HDF5/Avro would be a plus, knowledge about ROOT and TDataFrame can be acquired during the project

## Mentors 
  * [Enrico Guiraud](mailto:enrico.guiraud@cern.ch)
  * [Danilo Piparo](mailto:danilo.piparo@cern.ch)

## Links
  * [ROOT](https://root.cern/)
  * [TDataFrame](https://root.cern.ch/doc/master/classROOT_1_1Experimental_1_1TDataFrame.html)
  * [Parquet](https://parquet.apache.org/)
  * [HDF5](https://support.hdfgroup.org/HDF5/)
  * [Avro](https://avro.apache.org/)
