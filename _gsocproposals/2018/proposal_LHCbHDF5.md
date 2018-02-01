---
title: Integration of the HDF5 file format within the LHCb analysis framework
layout: gsoc_proposal
project: LHCb
year: 2018
organization:
  - CERN
  - Cincinnati
  - UZH
---

## Description

The [LHCb experiment](http://lhcb-public.web.cern.ch/lhcb-public/) software stack is based on the [Gaudi](http://gaudi.web.cern.ch/gaudi/) framework, which is designed to provide a common environment for simulation, filtering, reconstruction, and analysis applications for High Energy Physics (HEP) experiments. It uses [ROOT](https://root.cern.ch/), a widely used data analysis framework within the HEP community, as its data format, since it allows for flexible and efficient storage of various types of objects, including complex data structures.

User-level data analysis typically deals with much simpler data structures, namely arrays of values corresponding to particle properties, with one event (or particle candidate) per row, which are stored by the framework as ROOT `TTree`s. Traditionally, these trees have been analysed using the ROOT tools, either in C++ or using their Python bindings. But, lately, the advent of high-performance, open-source python scientific computing tools, such as [numpy](http://www.numpy.org/) or [pandas](https://pandas.pydata.org/), and powerful machine learning frameworks such as [scikit-learn](http://scikit-learn.org/) or [tensorflow](https://www.tensorflow.org/), have shifted the analysis paradigm. This creates the need for an intermediate step where analysis data are converted to HDF format for the use within these tools, making analysis workflows unnecessarily complex.

The GSoC participant will integrate the HDF file format in the Gaudi framework as a possible output for these user-level data analysis tools, thus helping the integration of the python scientific computing tools in the day-to-day arsenal of HEP physicists, and opening the way for more streamlined analysis workflows. Several compression algorithms for HDF file format (blosc, gzip) can be benchmarked and compared with the original ROOT format to choose the most suitable one. If time allows, an implementation of the [Apache Parquet](https://parquet.apache.org/) data format, also compatible with pandas, could also be implemented and benchmarked against HDF.

This work has far reaching implications, as the Gaudi framework is used, besides LHCb, by the [ATLAS](http://atlas.web.cern.ch/Atlas/) collaboration at CERN, and several other experiments including [HARP](http://harp.web.cern.ch/harp/) or [BESIII](http://bes3.ihep.ac.cn/).


## Task ideas

 * Understand the kind of data HEP physicists produce and what is a possible model for storage in HDF format
 * Learn how data conversion services are implemented in Gaudi
 * Integrate the HDF C++ API into Gaudi
 * Create a conversion service for the output of user-level analysis data
 * Create dedicated tests and usage example
 * Benchmark the implementation of the HDF format and its compression options vs the standard ROOT implementation
 * (Optional) Implement the Apache Parquet file format and benchmark it against HDF and ROOT
 
## Expected results

 * Working implementation, along with tests and documentation
 * Performance comparison of HDF vs ROOT with several compression options. If implemented, add Apache Parquet to the comparison.
 * Public release of this extension to the Gaudi framework


## Requirements

* C++ expertise
* Working experience with git
* Experience with HDF5 and Apache Parquet (optional) would be an advantage

## Mentors

* [Albert Puig](mailto:albert.puig@cern.ch)
* [Eduardo Rodrigues](mailto:Eduardo.Rodrigues@cern.ch)
* [Paul Seyfert](mailto:Paul.Seyfert@cern.ch)


## Links

 * [Gaudi](http://gaudi.web.cern.ch/gaudi/)
 * [hdfgroup.org](https://www.hdfgroup.org/)

