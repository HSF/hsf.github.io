---
title: Distributed Big Data Analysis with TDataFrame
layout: gsoc_proposal
project: ROOT
year: 2018
organization: CERN
---

## Description

The [ROOT](https://root.cern/) Software Framework is the cornerstone of all software stacks used by High Energy Physics (HEP) experiments, at CERN and other prestigious laboratories. It provides components which are fundamental for the entire data processing chain, from particle collisions to final publications, including final user data analysis, including modern machine learning techniques.

ROOT features a declarative analysis sub-system, [TDataFrame](https://root.cern.ch/doc/master/classROOT_1_1RDataFrame.html), which has proven to be a solution to scale in-process parallel HEP data analysis to ~100 cores with a simple and intuitive programming model.

This project aims to address the distributed execution of TDataFrame analysis programs. This could be accomplished by developing a generic library with a MapReduce-like interface. Such library would sit on top of connectors for specific task schedulers that would distribute the application tasks, for instance [Spark](http://spark.apache.org), an open-source software framework for large-scale big data processing on clusters. Additionally, a plugin could be implemented to facilitate the submission of such distributed analyses from [Jupyter](http://jupyter.org) notebooks, a well-known interface for interactive analysis.

## Task ideas
 * Implement a Python library, with a MapReduce-like interface, that is able to submit distributed jobs receiving as input a ROOT columnar dataset and producing aggregated results (e.g. histograms).
 * Implement one or more connectors for the aforementioned library, e.g. a Spark connector.
 * Explore how ROOT’s dataframe class, TDataFrame, can be combined with the aforementioned library to drive the execution in every node of a cluster.
 * Design and develop a programming model to facilitate the submission of distributed ROOT jobs from a Jupyter notebook, possibly involving JavaScript graphics.
 * Perform tests with real code coming from CERN experiments (CMS, TOTEM).

## Expected results
Working implementation of a Python library that hides the complexity of submitting distributed ROOT TDataFrame jobs to computational clusters.

## Requirements
Python, Spark, JavaScript, Jupyter notebooks

## Mentors
  * [Enric Tejedor](mailto:etejedor@cern.ch)
  * [Diogo Castro](mailto:diogo.castro@cern.ch)
  * [Danilo Piparo](mailto:danilo.piparo@cern.ch)
  * [Prasanth Kothuri](mailto:prasanth.kothuri@cern.ch)
  * [Enrico Guiraud](mailto:enrico.guiraud@cern.ch)
  * [Javier Cervantes](mailto:javier.cervantes@cern.ch)

## Links
  * [ROOT](https://root.cern/)
  * [TDataFrame](https://root.cern.ch/doc/master/classROOT_1_1RDataFrame.html)
  * [Spark](http://spark.apache.org)
  * [Jupyter](http://jupyter.org)
