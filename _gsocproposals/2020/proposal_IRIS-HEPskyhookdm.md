---
title: Extend SkyhookDM programmable object storage with statistics, sort/aggregate, or data compaction functions.
layout: gsoc_proposal
project: IRIS-HEP
year: 2020
organization: CROSS
---

## Description

The [Skyhook Data Management](http://www.skyhookdm.com) project extends Ceph distributed object storage to execute data management functions directly within storage at the object level.  Data is partitioned, formatted, and stored into objects and we have created functions that apply SQL operations such SELECT, PROJECT, AGGREGATE, and other custom processing methods.  We have also created methods to apply database physical design techniques such as indexing and transforming object data between row and columnar formats.  SkyhookDM supports loading data from several formats such as CSV, JSON, pyArrow, and [ROOT](https://root.cern/). Users can access SkyhookDM functions via two front-ends, Python and PostgreSQL.

Functions are developed using Ceph's dynamic object classes mechanism, and these classes and methods are applied to objects by Ceph Object Storage Devices. Internally, object data is formatted and accessed via two fast in-memory serialization libraries, [Google Flatbuffers](https://google.github.io/flatbuffers/) for row organizations and [Apache Arrow](https://arrow.apache.org) for columnar organizations and our methods utilize their corresponding APIs during data processing. Furthermore, data partitions are mapped to objects via several partitioning methods including [JumpConsistent Hash](https://arxiv.org/pdf/1406.2294.pdf) as well custom partitioning functions, and each object may contain a sequence of formatted sub-partitions.

This project proposes extending SkyhookDM with several new functionalities: (1) including data statistics collection, (2) SQL GROUPBY and ORDERBY, and (3) merge/split sub-partitions within an object.  Each of these will be developed as a new object class method that will be applied directly to formatted object data with the following benefits (1) improve query optimization and physical design tuning approaches (stats), (2) extend the types of query processing that can be pushed down into the storage layer (groupby, sort), or (3) improve data read time from disk (compaction).

## Task ideas

 * Implement a new custom method for statistics collection on data partitions stored in objects. [Github Issue](https://github.com/uccross/skyhookdm-ceph/issues/77)
 * Implement compaction of multiple formatted sub-partitions within an object into a single partition.  This could also incorporate compression. [Github Issue](https://github.com/uccross/skyhookdm-ceph/issues/33)
 * Extend current aggregation method to include sort/groupby for formatted database partitions in objects [Github Issue](https://github.com/uccross/skyhookdm-ceph/issues/23)
 
## Expected results

The task should be fully functional for data stored in both row and column formats (Flatbuffers and Arrow).  Larger scale experiments of 1--32 node clusters can be conducted on [NSF Cloudlab](https://www.cloudlab.us) to evaluate performance.

## Requirements

C++, some Python, storage systems or database background preferred

## Mentors

  * [JeffLeFevre](mailto:jlefevre@ucsc.edu)
  * [Aaron Chu](mailto:xchu1@ucsc.edu)

## Links

  * [Skyhook Data Management](http://www.skyhookdm.com)
  * [Ceph](https://ceph.io)
  * [SkyhookDM github repo](https://github.com/uccross/skyhookdm-ceph/wiki)
  * [SkyhookDM custom object classes](https://github.com/uccross/skyhookdm-ceph/tree/skyhook-luminous/src/cls/tabular)
  * [Google Flatbuffers](https://google.github.io/flatbuffers/)
  * [Apache Arrow](https://arrow.apache.org)
  * [ROOT](https://root.cern/)
  * [Ceph object classes with Lua example](https://ceph.io/geen-categorie/dynamic-object-interfaces-with-lua/)

