---
title: Next generation Big Data Analysis monitoring tools with ROOT
layout: gsoc_proposal
project: ROOT
year: 2019
organization: CERN
---

## Description

The [ROOT](https://root.cern/) Software Framework is the cornerstone of all software stacks used by High Energy Physics (HEP) experiments. It provides components which are fundamental for the entire data processing chain, from particle collisions to final publications, including final user data analysis and modern machine learning techniques.

ROOT features a declarative analysis sub-system, [RDataFrame](https://root.cern.ch/doc/master/classROOT_1_1RDataFrame.html), which has proven to be a solution to scale in-process parallel HEP data analysis to ~100 cores with a simple and intuitive programming model. Moreover, recent developments on previous GSoC editions have extended RDataFrame to offload heavy computations on external clusters using the [Spark](http://spark.apache.org) task distribution layer. Preliminary tests on ~5TB of real analysis data revealed the capacity of this interface to decrease the computational time from a dozen of hours to less than 5 minutes running on more than 500 external workers in parallel.

To allow scientists to perform massive analysis on much bigger datasets with interactive or quasi-interactive response times, it is crucial to have relevant performance metrics at the level of application in order to optimize existing bottlenecks, thus making the most out of the available resources.

The main goal of this project will be designing a high level display that can collect and show monitoring information from a Spark distributed application, in a way that feels intuitive and helpful for the user. While there is already a monitoring system for Spark and [Jupyter](http://jupyter.org) notebooks, this only covers details concerning Spark metrics, such as number of tasks. The goal of this project is to extend such monitoring system with relevant information coming from a ROOT application.

## Task ideas
 * Design and implementation of a modular API to collect relevant metrics from a ROOT Application.
   * New metrics have to be easily added.
 * Implement mechanism to dump collected information into a file for later processing.
   * Following a similar approach to the `perf` linux tool (perf.data and perf.report files).
 * Develop logic to gather desired metrics while a ROOT application is locally running.
   * Similar to a logger system with ROOT specific information.
   * Added overhead should be as low as possible.
   * Frequency at which samples are collected should be configurable by the user.
 * Explore how to send custom information from tasks/workers to the main client when running on a distributed environment.
 * Integration of this information into the existing monitoring tool.
 * Integration tests with real code coming from CERN experiments (CMS, TOTEM).

## Expected results
 * Working implementation of a ROOT monitoring system able to report application metrics when running distributed ROOT RDataFrame jobs on computational clusters.

## Requirements
 * C++, Python
 * Spark, JavaScript, Jupyter Notebooks would be a plus
 * Knowledge about ROOT and RDataFrame can be acquired during the project

## Mentors
  * [Javier Cervantes Villanueva](mailto:javier.cervantes@cern.ch)
  * [Enric Tejedor Saavedra](mailto:etejedor@cern.ch)
  * [Danilo Piparo](mailto:danilo.piparo@cern.ch)
  * [Prasanth Kothuri](mailto:prasanth.kothuri@cern.ch)

## Links
  * [ROOT](https://root.cern/)
  * [Spark](http://spark.apache.org)
  * [Jupyter](http://jupyter.org)
