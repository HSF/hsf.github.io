---
title: Deep autoencoders for scientific data compression
layout: gsoc_proposal
project: SMARTHEP
year: 2023
organization:
  - LundU
  - CERN
difficulty: medium
duration: 350
mentor_avail: June-October (with 3 weeks mentor vacation where student will work independently with minimal guidance)
---
​
## Short description of the project
The Large Hadron Collider (LHC) hosts multiple large-scale experiments, LHC experiments such as ATLAS, ALICE, LHCb, and CMS. These together produce roughly 1 Petabyte of data per second, but bandwidth and storage limitations force them to only pick the most interesting data, and discard the rest. The final data stored on disk is roughly 1 Petabyte per day [[1](https://home.cern/news/news/computing/cern-data-centre-passes-200-petabyte-milestone)]. Despite such steep methods of data reduction, the upgraded High Luminosity LHC in 2029 will produce 10 times more particle collisions. This is a great improvement for the potential to discover new physics, but poses a challenge both for data processing and data storage, as the resources needed in both departments are expected to be 3 and 5 times larger than the projected resources available [[2](https://cerncourier.com/a/time-to-adapt-for-big-data/)][[3](https://doi.org/10.1051/epjconf/202024504035)].

Data compression would be the go-to solution to this issue, but general data formats used for big data and the ROOT data format used at the LHC are already highly compressed, meaning that the data does not compress much under normal loss-less compression methods like zip [[4](https://www.sciencedirect.com/science/article/abs/pii/S016890029700048X)]. However, since the observables in these experiments benefit from more events and higher statistics, lossy compression is a good alternative. By using lossy compression some data accuracy is lost, but the compression will allow for the storage of more data which will increase the statistical precision of the final analysis.

“Baler” is a compression tool undergoing development at the Particle Physics divisions of Lund University and the University of Manchester. Baler uses autoencoder neural networks as a type of lossy machine learning-based compression to compress multi-dimensional data and evaluate the accuracy of the dataset after compression. Baler is currently tested on ROOT data from the CMS and ATLAS experiment, which is a Hierarchical Data Format [[3](https://doi.org/10.1051/epjconf/202024504035)].

Since data storage is a problem in many fields of science and industry, Baler aims to be an Open Source tool that can support the compression of data formats from vastly different fields of science. For example, catalog data in astronomy and time series data in Computational Fluid Dynamics.

This project aims to work on the machine learning models in Baler to optimize performance for LHC data and evaluate its performance in real LHC analyses.

## Task ideas

* Run and document the performance of an existing Baler model to compress ATLAS data and data from other LHC experiments
* Improve the design and test the performance of different autoencoder models
* Performance should be measured using the fidelity of decompressed data with respect to original inputs, in terms of impact on the quality of the actual physics analysis
* Evaluate the performance compared to other lossy compression algorithms
* If time allows, try Baler on other datasets outside of high-energy particle physics

## Expected results

An improved compression performance with documentation and figures of merit that may include:
  * Plots made in matplotlib that demonstrate the performance of the new models compared to the old
  * Documentation of the design choices made for the improved models
  * Documented evaluation of a physics analysis on data before and after compression

## Requirements

Required: Good knowledge of UNIX, Python, matplotlib, Pytorch, Pandas, ROOT, and ability to work using Python libraries.

## Mentors
   * ***[Alexander Ekman](mailto:alexander.ekman@hep.lu.se)***
   * [Caterina Doglioni](mailto:caterina.doglioni@cern.ch) as backup mentor

## Links

* Previous work:
   * [Thesis by Eric Wulff, Lund University](https://lup.lub.lu.se/student-papers/search/publication/9004751)
   * [Thesis by Erik Wallin, Lund University](https://lup.lub.lu.se/student-papers/search/publication/9012882)
   * [GSOC 2020 project: Medium post by Honey Gupta](https://medium.com/@hn.gpt1/deep-compression-for-high-energy-physics-data-google-summer-of-code20-3dea5acc7bcf)    
   * [GSOC 2021 project: Zenodo entry by George Dialektakis](https://zenodo.org/record/5482611#.Y-I28S2l3fa)

 * [ROOT](https://root.cern/)
 * [Jupyter](http://jupyter.org)
 * [PyTorch](http://pytorch.org)
