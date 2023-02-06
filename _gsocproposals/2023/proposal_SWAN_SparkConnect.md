---
title: Leverage Spark Connect for interactive data analysis in Jupyter Notebooks
layout: gsoc_proposal
project: SWAN
year: 2023
difficulty: medium
duration: 175
mentor_avail: June-September
organization:
 - CERN
---

## Description

[SWAN](https://cern.ch/swan) (Service for Web-based ANalysis) is a platform to do interactive data analysis on a web browser. Scientists and engineers, both at [CERN](https://home.cern/) and at partner institutes, are using SWAN on a daily basis to develop algorithms required to perform their data analyses. The SWAN service builds on top of the widely-adopted [Jupyter Notebooks](http://jupyter.org) and, more recently, the new [JupyterLab](https://jupyterlab.readthedocs.io) interface. It integrates access to CERN software libraries, storage solutions and compute resources; notably, it leverages the storage synchronization and sharing capabilities of [CERNBox](https://cernbox.web.cern.ch) and the computational power of [Spark](https://spark.apache.org/)/[Hadoop](https://hadoop.apache.org/) clusters for scaling out.

Currently, SWAN uses the Apache Spark Python API to connect Python notebooks to Spark clusters. This works by allocating a Spark Session object that is private to the Python process (the user’s notebook session), which becomes the driver of the distributed computation. The Spark Session on the driver machine can then request worker processes, called executors, from the cluster manager and schedule Spark jobs to be run in parallel utilizing the executors’ resources.

Such architecture has proven to work well and provide a scale out solution to SWAN users. However, a few important limitations have come apparent when using Spark on notebooks, due to the tightly coupled Spark driver architecture. The lack of built-in client-server connectivity in Spark (up to version 3.3.x) means, for example, that users need to spawn a new Spark Session for each of their notebooks, an operation that is resource intensive and has a high latency. These and other limitations are addressed in the latest development by the Apache Spark community: the Spark Connect component ([SPARK-39375](https://issues.apache.org/jira/browse/SPARK-39375)). Spark Connect is a major improvement in Apache Spark and brings more flexibility to the interactive data analysis use cases with Jupyter notebooks. This is expected to improve the experience of SWAN users who offload computations to Spark clusters, since it allows to use Spark in client-server mode and hence share a connection to a Spark cluster across multiple notebooks, which also improves resource utilization.

Therefore, this project proposes to develop a JupyterLab extension that makes it easy to establish a connection to a Spark cluster and share it among multiple notebooks, by exploiting Spark Connect under the hood. Potentially, this extension could be used not only in SWAN but also in other JupyterLab deployments.

## Task ideas

  * Investigate Spark Connect and understand the advantages and limitations of its client-server architecture compared to the classic PySpark architecture
  * Explore and test how Spark Connect can be leveraged on Spark clusters at CERN
  * Develop a JupyterLab extension based on Spark Connect, with the following features:
    * Allows to create one or more connections to a Spark cluster, from a SWAN user session
    * Multiple notebooks can be clients of a single connection
    * Optionally, allows to check the status of Spark jobs for a given connection
  * Test and integrate the developed extension into SWAN

## Expected results

A working and easy-to-use extension, installable both in SWAN and in vanilla JupyterLab, which allows to leverage Spark Connect for connecting to Spark clusters and do interactive data analysis.

## Desirable Skills

* Knowledge of TypeScript and Python
* Knowledge of Linux and Git
* Experience with Jupyter Notebooks / JupyterLab
* Understanding of REST APIs

## Mentors

* [Enric Tejedor](mailto:etejedor@cern.ch)
* [Jose Carlos Luna](mailto:jose.carlos.luna@cern.ch)
* [Luca Canali](mailto:luca.canali@cern.ch)
* [Diogo Castro](mailto:diogo.castro@cern.ch)

## Links

* [CERN](https://home.cern/)
* [SWAN Website](https://cern.ch/swan)
* [SWAN Github](https://github.com/swan-cern)
* [Jupyter](http://jupyter.org)
* [Spark](https://spark.apache.org/)
