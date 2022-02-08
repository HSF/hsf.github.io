---
title: ROOT - Automatic conversion of data stored in TTree form to RNTuple
layout: gsoc_proposal
project: ROOT
year: 2022
difficulty: medium
duration: 350
mentor_avail: June-August
organization:
  - CERN
---

# Description

A typical high-energy physics (HEP) data analysis only requires a subset of the
columns stored for each event. In this context, systems tuned for columnar access
are specially relevant. TTree is the ROOT's legacy columnar storage that has been
used to store more than 1 exabyte of HEP data during the last 25 years.
On the other hand, the RNTuple classes provide ROOT's new, experimental I/O subsystem
for HEP data. The RNTuple data layout is columnar and supports nested types (e.g.
vectors of floats), conceptually similar to Apache Arrow or Apache Parquet.

Given that RNTuple is backwards-incompatible with TTree, existing data in TTree
format will have to be converted to the RNTuple format. This project will consist of
the implementation of an automatic conversion tool that migrates both the schema
(i.e. fields and their types) and the user data. Note that replicating the schema is
not always possible because RNTuple does not currently support all the column types
supported in TTree.


## Task ideas and expected results

The expected result is a working implementation of a tool that allows migrating
existing TTree data sets (schema + data) to RNTuple.
The student should be prepared to write a progress report and present the results at
the end of the summer.


## Evaluation Task

Interested students please contact Javier (j.lopez@cern.ch) or Jakob (jblomer@cern.ch)
for a warm-up and evaluation task.

## Requirements

  * C++, low-level data storage and access programming


## Mentors

  * **[Javier Lopez-Gomez](mailto:j.lopez@cern.ch)**
  * [Jakob Blomer](mailto:jblomer@cern.ch)
  

## Links

  * [ROOT](https://root.cern/)
  * [ROOT user's guide: TTree](https://root.cern.ch/root/htmldoc/guides/users-guide/Trees.html)
  * [RNTuple Overview](https://indico.cern.ch/event/773049/contributions/3474746/attachments/1937507/3211341/rntuple-chep19.pdf)
  * [RNTuple Code](https://github.com/root-project/root/tree/master/tree/ntuple/v7)
  * [RNTuple Tutorials](https://github.com/root-project/root/tree/master/tutorials/v7/ntuple)
