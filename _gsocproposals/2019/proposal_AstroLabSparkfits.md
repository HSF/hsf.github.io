---
title: Apache Spark: migrating FITS Data Source API to V2
layout: gsoc_proposal
project: AstroLab
year: 2019
organization: LAL
---

## Description

High Energy Physics & Astrophysics experiments typically describe their data with complex data structures that are stored into structured file formats such as for example Hierarchical Data Format 5 (HDF5), ROOT files, or Flexible Image Transport System (FITS). For example, the FITS file format has been introduced more than thirty years ago with the requirement that developments to the format must be backward compatible. This data format has been used successfully to store and manipulate the data of a wide range of astrophysical experiments over the years, hence it is considered as one of the possible data format for future surveys like the Large Synoptic Survey Telescope (LSST) which will produce PB of data over the next years.

At [AstroLab Software](https://astrolabsoftware.github.io/), we investigate how to connect the FITS format to [Apache Spark](http://spark.apache.org/) in order to process and analyse more efficiently future large data sets in astronomy. 
To this purpose, we designed and implemented a FITS data source for Spark SQL and DataFrames, called [spark-fits](https://astrolabsoftware.github.io/spark-fits/), to handle sets of FITS files arbitrarily large. For flexibility and high throughput, Apache Spark uses an abstraction of the storage layer defined in the Data Source API. spark-fits follows this convention and it has been written with the Data Source API V1.
However, one the most important features of the recent Apache Spark 2.3 release is the Data Source API V2, which introduces more generality and flexibility.

## Task ideas

We propose first to migrate the existing FITS Data Source to the new Data Source API V2.
Second, the student will focus on optimizing the performance of the connector, especially when dealing with a huge number of small files (+10,000), and s/he will implement new functionalities to the connector (column pruning, filters). 

## Expected results

Ultimately, the developments will be integrated in the spark-fits package.

## Desirable Skills

* Some knowledge on Scala.
* Knowledge of distributed computing (cluster and grid computing).
* Being aware of the Big Data challenges and issues.
* Working with or willing to learn Spark.

## Mentors
  * [Julien Peloton](mailto:peloton@lal.in2p3.fr)
  * [Chris Arnault](mailto:arnault@lal.in2p3.fr)

## Links
   1. [AstroLab Software](https://astrolabsoftware.github.io/)
   2. [spark-fits](https://astrolabsoftware.github.io/spark-fits/)
   3. [Apache Spark](https://spark.apache.org/)
