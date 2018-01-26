---
title: Processing large-scale 3D data sets using Apache Spark
layout: gsoc_proposal
project: Spark3D
year: 2018
organization: LAL
---

## Description

The volume of data recorded by current and future High Energy Physics & Astrophysics experiments, and the complexity of their data set require a broad panel of knowledge in computer science, signal processing, statistics, and physics.
Exact analysis of those data sets produced is a serious computational challenge, which cannot be done without the help of state-of-the-art tools.
This has to be matched by sophisticated and robust analysis performed on many powerful machines, as we need to process or simulate several times data sets.

While a lot of efforts have been made to develop cluster computing systems for processing large-scale spatial 2D data, there are very few frameworks to process and analyse 3D data sets which were hitherto too costly to be processed efficiently.
With the recent development of fast and general engine such as [Apache Spark](http://spark.apache.org), taking advantage of distributed systems, we enter in a new area of possibilities.

## Task ideas

Following the [GeoSpark](http://geospark.datasyslab.org) approach, we propose to extend its
construction (based on Apache Spark) with a set of out-of-the-box 3D Spatial Resilient Distributed Datasets that deal efficiently with large-scale 3D data sets across machines.
A special attention will be put in developing geometrical and Spatial Queries for 3D data sets (indexation, location, aggregation, join), including the benchmarking on existing data sets.

## Expected results

Ultimately, the developments will be integrated in an Apache Spark-based framework for processing large-scale spatial 3D data.

## Requirements

  * At least one of the following programming language: scala (preferred), java, or python.
  * Knowledge of distributed computing (cluster and grid computing).
  * Being aware of the Big Data challenges and issues.
  * Working with or willing to learn Spark.

## Mentors
  * [Christian Arnault](mailto:arnault@lal.in2p3.fr)
  * [Julien Peloton](mailto:peloton@lal.in2p3.fr)

## Links
  * [Spark](http://spark.apache.org)
  * [GeoSpark](http://geospark.datasyslab.org)
