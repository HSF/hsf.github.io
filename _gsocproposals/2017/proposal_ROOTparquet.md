---
title: Integration of Apache Parquet reading capabilities in ROOT data analyses
layout: gsoc_proposal
project: ROOT
organization: CERN
---

## Description
ROOT is a C++ software toolkit widely used for high-energy physics (HEP) analyses. It specializes in reading and writing large amounts of data efficiently, using a custom storage format known as ROOT files. TDataFrame is a new tool that allows ROOT users to quickly and efficiently setup data analyses through a high-level declarative syntax (i.e. functional chains).
The aim of this project is to seamlessly interface TDataFrame with common storage formats other than ROOT files, such as Apache Parquet. Users of TDataFrame will be able to transparently read data stored in these formats with minimal or no change required to the analysis code.

## Task ideas and expected results
 * Design of new internal facilities for ROOT to read from third-party file formats such as Apache Parquet
 * Design of a user-transparent interface to access these facilities through TDataFrame
 * Implementation, integration and testing of this interface in ROOT's TDataFrame, to make this feature readily available to users

## Requirements
Strong C++ and C++11 skills, familiarity with the Apache Parquet file formats. Familiarity with the ROOT software library is highly desirable.

## Mentors
  * [Enrico Guiraud](mailto:enrico.guiraud@cern.ch)
  * [Danilo Piparo](mailto:danilo.piparo@cern.ch)

## Links
  * [ROOT](https://root.cern/)
  * [TDataFrame](https://root.cern.ch/doc/master/group__dataframe.html)
  * [Apache Parquet](https://parquet.apache.org/)
