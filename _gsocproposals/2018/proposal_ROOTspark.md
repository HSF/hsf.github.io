---
title: Distributed Big Data Analysis with ROOT and Spark
layout: gsoc_proposal
project: ROOT
year: 2018
organization: CERN
---

## Description

The [ROOT](https://root.cern/) Software Framework is the cornerstone of all software stacks used by High Energy Physics (HEP) experiments, at CERN and other prestigious laboratories. It provides components which are fundamental for the entire data processing chain, from particle collisions to final publications, including final user data analysis, including modern machine learning techniques.

[Spark](http://spark.apache.org) is an open-source software framework for large-scale big data processing on clusters. While it has become mainstream in industry, its adoption in the field of physics is still in its infancy. This project intends to explore new solutions for distributed physics analysis at CERN, and in particular the interplay of three technologies: ROOT, Spark and the [Jupyter](http://jupyter.org) notebooks, a well-known interface for interactive analysis.

The main development of this project will focus on making it easier to submit distributed analyses with ROOT and Spark, by means of a Python library that will offer a MapReduce-like interface. In addition, the project will address the integration of that library with the Jupyter notebook interface. Tests with real use cases of physics analysis will be then performed using the [SWAN](http://swan.web.cern.ch/) notebook service at CERN.

## Task ideas
 * Implement a Python library, with a MapReduce-like interface, that is able to submit Spark jobs receiving as input a ROOT columnar dataset and producing aggregated results (e.g. histograms).
 * Explore how ROOT’s dataframe class, TDataFrame, can be combined with the aforementioned Python library to drive the execution in every node of a Spark cluster.
 * Design and develop a programming model to facilitate the submission of ROOT Spark jobs from a Jupyter notebook, possibly involving JavaScript graphics. 
 * Perform tests with real code coming from CERN experiments (CMS, TOTEM).
 * Test the developments in the SWAN notebook service at CERN.

## Expected results
Working implementation of a Python library that hides the complexity of submitting ROOT-Spark jobs to computational clusters.

## Requirements
Spark, Python, JavaScript, Jupyter notebooks

## Mentors 
  * [Enric Tejedor](mailto:etejedor@cern.ch)
  * [Diogo Castro](mailto:diogo.castro@cern.ch)
  * [Danilo Piparo](mailto:danilo.piparo@cern.ch)
  * [Prasanth Kothuri](mailto:prasanth.kothuri@cern.ch)

## Links
  * [ROOT](https://root.cern/)
  * [Spark](http://spark.apache.org)
  * [Jupyter](http://jupyter.org)
  * [SWAN](http://swan.web.cern.ch)
