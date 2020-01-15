---
title: Repartitioning spatial data with spark3D
layout: gsoc_proposal
project: AstroLab
year: 2019
organization: LAL
---

## Description

While there are many packages based on [Apache Spark](https://spark.apache.org/) to manipulate spatial 2D datasets (e.g. Geospark, Geomesa, Magellan, GeoTrellis), there are very few initiatives to process and analyse 3D data sets which were hitherto too costly to be processed efficiently. [spark3D](https://astrolabsoftware.github.io/spark3D/) is an extension of the Apache Spark framework, and more specifically the Spark SQL module, focusing on the manipulation of three-dimensional data sets. 

We propose here to tackle the challenge of repartitioning large spatial 3D data sets. Often the data is not written on disks the way we would like to have it distributed. Repartitioning the space is a way to re-organise the data to speed-up later queries, to ease the exploration of the data set or to enable visualisation. In spark3D, we want to provide easy ways to define and apply custom partitioners, that is associating each object in the dataset with a user-defined partition number.
Unfortunately, repartitioning the space involves potentially large shuffle between executors which have to send and receive data according to the new partitioning scheme. Depending on the network capacity and the size of the initial data set, this operation can be costly and the repartition becomes a game-changer only if multiple queries have to be performed. Last but not least, the Spark DataFrame API does not yet expose many facilities to repartition your data as you would like (unlike the RDD API), hence we decided to bring in spark3D new DataFrame feature!

## Task ideas

We propose first to extend spark3D with new partitioning schemes such as the very popular KD-Tree. 
Second, the student will focus on optimizing existing novel spark3D methods to repartition datasets (time and/or memory). A capability to interact with the Catalyst optimizer directly would be a plus. A special attention will be put in performing reproducible benchmarks on existing datasets. 

## Expected results

Ultimately, the developments described above will be integrated in the Apache Spark-based framework for processing large-scale spatial 3D data, spark3D.

## Desirable Skills

* At least one of the following programming language: Scala (preferred), Java, or Python.
* Knowledge of distributed computing (cluster and grid computing).
* Being aware of the Big Data challenges and issues.
* Working with or willing to learn Spark.

## Mentors
  * [Julien Peloton](mailto:peloton@lal.in2p3.fr)
  * [Chris Arnault](mailto:arnault@lal.in2p3.fr)

## Links
   1. [AstroLab Software](https://astrolabsoftware.github.io/)
   2. [spark3D](https://astrolabsoftware.github.io/spark3D/)
   3. [Apache Spark](https://spark.apache.org/)
