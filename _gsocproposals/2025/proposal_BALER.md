---
title: The rise of the machine (learning) in data compression for high energy physics and beyond
layout: gsoc_proposal
project: BALER
year: 2025
organization:
  - baler
  - umanchester
difficulty: medium
duration: 350
mentor_avail: June-August
---
​
## Short description of the project
The Large Hadron Collider (LHC) hosts multiple large-scale experiments, LHC experiments such as ATLAS, ALICE, LHCb, and CMS. These together produce roughly 1 Petabyte of data per second, but bandwidth and storage limitations force them to only pick the most interesting data, and discard the rest. The final data stored on disk is roughly 1 Petabyte per day [[1](https://home.cern/news/news/computing/cern-data-centre-passes-200-petabyte-milestone)]. Despite such steep methods of data reduction, the upgraded High Luminosity LHC in 2029 will produce 10 times more particle collisions. This is a great improvement for the potential to discover new physics, but poses a challenge both for data processing and data storage, as the resources needed in both departments are expected to be 3 and 5 times larger than the projected resources available [[2](https://cerncourier.com/a/time-to-adapt-for-big-data/)][[3](https://doi.org/10.1051/epjconf/202024504035)].

Data compression would be the go-to solution to this issue, but general data formats used for big data and the ROOT data format used at the LHC are already highly compressed, meaning that the data does not compress much under normal loss-less compression methods like zip [[4](https://www.sciencedirect.com/science/article/abs/pii/S016890029700048X)]. However, since the observables in these experiments benefit from more events and higher statistics, lossy compression is a good alternative. By using lossy compression some data accuracy is lost, but the compression will allow for the storage of more data which will increase the statistical precision of the final analysis.

BALER is a compression tool undergoing development at the particle physics division of the University of Manchester. BALER uses autoencoder and otherneural networks as a type of lossy machine learning-based compression to compress multi-dimensional data and evaluate the accuracy of the dataset after compression.

Since data storage is a problem in many fields of science and industry, BALER aims to be an open source tool that can support the compression of data formats from vastly different fields of science. For example, catalog data in astronomy and time series data in computational fluid dynamics.

This project aims to work on the machine learning models in BALER to optimize performance for LHC data and evaluate its performance in real LHC analyses.

## Task ideas

This internship can focus on a range of work packages, and the project can be tailored to the intern. Possible projects include:

  * New auto-encoder models could be developed, better identifying correlations between data objects in a given particle physics dataset entry (event, typically containing thousands of objects and around 1MB each). New models could also improve performance on live / unseen data. 
  * Existing models could be applied on an FPGA, potentially significantly reducing latency and power consumption, opening the possibility of live compression before transmission of data on a network.
  * BALER could also be integrated into standard research data storage formats and programs used by hundreds of thousands of physics researchers (ROOT).
  * Finally the compression could be applied to particle physics datasets and the affect on the physics discovery sensitivity of an analysis could be assessed and compared to the possible increased sensitivity from additional data bandwidth. 

Ideas from the intern are also welcomed.

## Expected results

An improved compression performance with documentation and figures of merit that may include:
  * Plots made in matplotlib that demonstrate the performance of the new models compared to the old
  * Documentation of the design choices made for the improved models
  * Documented evaluation of a physics analysis on data before and after compression

## Requirements

The candidate should have experience with the python language and a Linux environment, familiarity with AI fundamentals, and familiarity with PyTorch.

Desirable skills include familiarity with AI fundamentals including transformers and/or graph neural networks, particle physics theory and experiments, PyTorch, FPGA programming and/or simulation, 


## Mentors
   * ***[James Smith](mailto:james.smith-7@manchester.ac.uk)***
   * [Caterina Doglioni](mailto:caterina.doglioni@cern.ch) as backup mentor

## Links

  * [BALER GitHub](https://github.com/baler-collaboration/baler)
  * [BALER Paper](https://arxiv.org/abs/2305.02283)

  * Previous work:
    * [Thesis by Eric Wulff, Lund University](https://lup.lub.lu.se/student-papers/search/publication/9004751)
    * [Thesis by Erik Wallin, Lund University](https://lup.lub.lu.se/student-papers/search/publication/9012882)
    * [GSOC 2020 project: Medium post by Honey Gupta](https://medium.com/@hn.gpt1/deep-compression-for-high-energy-physics-data-google-summer-of-code20-3dea5acc7bcf)    
    * [GSOC 2021 project: Zenodo entry by George Dialektakis](https://zenodo.org/record/5482611#.Y-I28S2l3fa)

  * [ROOT](https://root.cern/)
  * [Jupyter](http://jupyter.org)
  * [PyTorch](http://pytorch.org)
