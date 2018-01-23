---
title: Big Data Tools for Physics Analysis
layout: gsoc_proposal
project: ROOT
year: 2017
organization: CERN
---

## Description

[Spark](http://spark.apache.org)  is an open-source software framework for large-scale big data processing on clusters. While it has become mainstream in industry, its adoption in the field of physics is still in its infancy. This project intends to explore the use of Spark for physics analysis at CERN, and in particular its interplay with two technologies: (i) [ROOT](http://root.cern.ch), a software toolkit widely used for high-energy physics analysis, and (ii) the [Jupyter](http://jupyter.org) notebooks, a well-known interface for interactive analysis.
The main development of this project will focus on making it easier to manage Spark computations from a Jupyter notebook. A plugin will be developed so that notebook users can monitor the status of a Spark job submitted from a notebook cell, and even cancel it if necessary. The main use case of the plugin will be a parallel physics analysis with ROOT and Spark, with a possible second use case in distributed machine learning. The plugin can then be integrated into the [SWAN](http://swan.web.cern.ch/) notebook pilot service at CERN.

## Task ideas
 * Creation of a testbed for submission of Spark jobs from a Jupyter notebook
 * Design and implementation of a plugin to monitor Spark jobs from a notebook
   * Display information such as progress bars, task statistics and errors
   * Allow to cancel ongoing Spark jobs
 * Use cases: apply the plugin to a couple of distributed Spark applications
   * ROOT physics analysis
   * Machine learning
 * Tests on CERN IT infrastructure (Spark clusters)
 * Integration of the plugin into the SWAN notebook service at CERN

## Expected results
Working implementation of the notebook plugin to manage ROOT-Spark jobs

## Requirements
Spark, Python, JavaScript, Jupyter notebooks

## Mentors 
  * [Enric Tejedor](mailto:etejedor@cern.ch)
  * [Danilo Piparo](mailto:danilo.piparo@cern.ch)
  * [Prasanth Kothuri](mailto:prasanth.kothuri@cern.ch)
  * [Kacper Surdy](mailto:kacper.surdy@cern.ch)

## Links
  * [ROOT](https://root.cern/)
  * [Spark](http://spark.apache.org)
  * [Jupyter](http://jupyter.org)
