---
title: Extend SkyhookDM programmable object storage functions
layout: gsoc_proposal
project: IRIS-HEP
year: 2020
organization: CROSS
---

## Description

The [Skyhook Data Management](http://www.skyhookdm.com) project extends Ceph distributed object storage to execute data management functions directly within storage at the object level.  Data is partitioned, formatted, and stored into objects and we have created functions that apply SQL operations such SELECT, PROJECT, AGGREGATE, and other custom processing methods.  We have also created methods to apply database physical design techniques such as indexing and transforming object data between row and columnar formats.  SkyhookDM supports loading data from several formats such as CSV, JSON, pyArrow, and [ROOT](https://root.cern/). Users can access SkyhookDM functions via two front-ends, Python and PostgreSQL.

Functions are developed using Ceph's dynamic object classes mechanism, and these classes and methods are applied to objects by Ceph Object Storage Devices. Internally, object data is formatted and accessed via two fast in-memory serialization libraries, [Google Flatbuffers]() for row organizations and [Apache Arrow]()for columnar organizations and our methods utilize their corresponding APIs during data processing. Furthermore, data partitions are mapped to objects via several partitioning methods including JumpConsistent Hash as well custom partitioning functions, and each object may contain a sequence of formatted sub-partitions.

This project proposes extending SkyhookDM with several new functionalities: including data statistics collection, SQL GROUPBY and ORDERBY, and merge/split sub-partitions within an object.  Each of these will be develop as a new object class method that will be applied directly to formatted object data in order to (1) improve query optimization and physical design tuning approaches (stats), (2) extend the types of query processing that can be pushed down into the storage layer (groupby, sort), or (3) improve data read time from disk (compaction).

## Task ideas
 * Implement compaction of multiple formatted sub-partitions within an object into a single partition.  This could also incorporate compression.
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


## Links
  * [ROOT](https://root.cern/)
  * [TDataFrame](https://root.cern.ch/doc/master/classROOT_1_1RDataFrame.html)
  * [Lua example](https://ceph.io/geen-categorie/dynamic-object-interfaces-with-lua/)

