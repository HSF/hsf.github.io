---
title: Automatic conversion of data stored in TTree form to RNTuple
layout: gsoc_proposal
project: ROOT
year: 2021
organization:
    - CERN
---

## Description
The ROOT Software Framework is the cornerstone of many software stacks used by High Energy Physics (HEP) experiments, at CERN and other prestigious laboratories. It provides components which are fundamental for the entire data processing chain, from particle collisions to final publications, including final user data analysis, including modern machine learning techniques.

Analyses of High-Energy Physics data typically only require a subset of the properties stored for each event. In this context, row-wise event storage (i.e. one record per event) has been proved to be suboptimal as it causes unneeded data to be read from persistent storage. In contrast, a columnar storage organizes the data set in columns and internally groups values that belong to the same data member. TTree is the ROOT's legacy columnar storage that has been used to store more than 1 exabyte of HEP data during the last 25 years. On the other hand, the RNTuple classes provide ROOT's new, experimental I/O subsystem for high-energy physics data. The RNTuple data layout is columnar and supports nested types (e.g., vectors of floats), conceptually similar to Apache Arrow or Apache Parquet. RNTuple has been designed for efficiency and to take advantage of modern storage systems, particularly low-latency high-bandwidth SSDs and object storages, e.g. Intel DAOS.

As said previously, a vast amount of data has been collected by experiments and stored in TTree format. Given that RNTuple is a complete backwards-incompatible redesign, the development of an automatic conversion tool that permits the migration of existing TTree data into RNTuple is a must. In this regard, both the schema (i.e., fields and their types) and the data will have to migrated. Note that replicating the schema is not always possible because RNTuple does not currently support all the column types supported in TTree. If the schema migration succeeds, existing data, i.e. rows, shall also be imported into the RNTuple.

## Task ideas and expected results
The project should, in a first step, develop a routine for translating an existing TTree schema into its RNTuple equivalent. In a second step, all rows in the entire data set should be imported.

The expected result is a working implementation of a tool that allows migrating existing TTree data sets (schema + data) to RNTuple. The student should be prepared to write a progress report and present the results at the end of the summer.

## Evaluation Task
Interested students please contact Jakob (jblomer@cern.ch) or Javier (j.lopez@cern.ch) for a warm-up and evaluation task.

## Requirements
 * C++, low-level data storage and access programming

## Mentors
 * [Jakob Blomer](mailto:jblomer@cern.ch)
 * **[Javier Lopez-Gomez](mailto:j.lopez@cern.ch)**

## Links
 * [ROOT](https://root.cern/)
 * [ROOT user's guide: TTree](https://root.cern.ch/root/htmldoc/guides/users-guide/Trees.html)
 * [RNTuple Overview](https://indico.cern.ch/event/773049/contributions/3474746/attachments/1937507/3211341/rntuple-chep19.pdf)
 * [RNTuple Code](https://github.com/root-project/root/tree/master/tree/ntuple/v7)
 * [RNTuple Tutorials](https://github.com/root-project/root/tree/master/tutorials/v7/ntuple)
