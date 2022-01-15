---
title: Implementation of a new Unfolding Procedure
layout: gsoc_proposal
project: ROOT
year: 2018
organization: 
  - CERN
  - icelanduniversity
---

## Project Description

An Unfolding procedure based on a Mixture Density Model is used for correcting experimental data for distortions due to finite resolution and limited detector acceptance. The true distribution is estimated by a weighted sum of probability density functions with positive weights and with the width of the densities acting as a regularization parameter responsible for the smoothness of the result. To obtain better smoothing in less populated regions, the width parameter is chosen inversely proportional to the square root of the estimated density. Cross-validation is employed to determine the optimal values of the resolution and the method parameters. This approach is directly applicable to multidimensional problems. 

## Tasks

  * Development and implementation of C++ code for Densities Mixture Unfolding procedure 
  * Integrate of code in the ROOT software framework as a plugin-method
  * Code optimization and porting to parallel computation
  * Development of code examples (tutorials) and reference documentation	


## Requirements

Strong knowledge of C++11; being able to produce clean, reliable code; knowledge of basic statistics and numerical computation.


## Mentors
  
  * [Nikolay Gagunashvili](mailto:nikolay@hi.is)
  * [Lorenzo Moneta](mailto:Lorenzo.Moneta@cern.ch)


## Links

  * [ROOT](https://root.cern/)
  * N. Gagunashvili, [Densities mixture unfolding for the data obtained from detectors with finite resolution and limited acceptance](https://arxiv.org/abs/1410.1586), Nucl. Instrum. Meth. A 778 (2015) 92. 

