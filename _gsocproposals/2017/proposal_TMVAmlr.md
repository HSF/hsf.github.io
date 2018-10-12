---
title: Interface mlr package with RMVA
layout: gsoc_proposal
project: TMVA
year: 2017
organization:
 - UdeA
 - CERN
---

# Description
[mlr](https://mlr-org.github.io/) is an [R](https://cran.r-project.org/) package that integrates almost all machine learning packages in R. [RMVA](http://oproject.org/RMVA){:data-proofer-ignore=""} is a set of plugins for TMVA based on [ROOTR](http://oproject.org/ROOT+R){:data-proofer-ignore=""} that allows the use of R in TMVA. The idea is to update the library RMVA to use mlr.

<!-- oproject is very slow and times out on html-proofer -->

## Task ideas
 * Write BaseMethod class for mlr package.
 * Implement a system to check if the required machine learning method has the R package installed.
 * Implement a system to check if the required machine learning method from R has support for multiclass classification, regression or weights in the data.
 * Write methods to support classification and regression.
 * Write a clear documentation with a table of options for every method.

**Expected results**:
 * working implementation with tests and documentation
 * A machine learning example using different methods for classification and regression.
 * Compare C50/RSVM and RSNNS using the current RMVA implementation and with the new MLR implementation.

**Requirements**: Advanced skills in C/C++, experience with R and machine learning.

**Mentors**:
  * [Omar Zapata](mailto:Omar.Zapata@cern.ch)
  * [Lorenzo Moneta](mailto:Lorenzo.Moneta@cern.ch)
  * [Diego Restrepo](mailto:alejandro.restrepo@udea.edu.co)

**Links**:

  * [http://root.cern](http://root.cern)
  * [http://mlr-org.github.io](https://mlr-org.github.io/mlr/)
  * [http://oproject.org/RMVA](http://oproject.org/RMVA){:data-proofer-ignore=""}
  * [http://oproject.org/ROOT+R](http://oproject.org/ROOT+R){:data-proofer-ignore=""}
