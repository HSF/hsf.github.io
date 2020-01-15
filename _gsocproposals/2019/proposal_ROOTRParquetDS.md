---
title: Apache Parquet support for ROOT's RDataFrame 
layout: gsoc_proposal
project: ROOT
year: 2019
organization:
  - CERN
---

## Description

[RDataFrame](https://root.cern/doc/master/classROOT_1_1RDataFrame.html) is a ROOT based data frame library, offering a high level declarative interface for the analysis of tabular and hierarchical data.
Transformations and filtering of the data is expressed as a set of lazily applied chained operations on the data frame itself, expressed using a syntax similar to the one of other popular packages like Pandas and Apache Spark.

[Apache Parquet](https://parquet.apache.org)  is a columnar storage format available to any project in the Hadoop ecosystem, regardless of the choice of data processing framework, data model or programming language.

RDataFrame provides an abstract interface, [RDataSource](https://root.cern.ch/doc/v614/classROOT_1_1RDF_1_1RDataSource.html), to ingest data from various backends, including ROOT `TTree`s, CSV files and Apache Arrow.

The goal of this project should be allowing RDataFrame to process Apache Parquet files.

## Task ideas

  * Implement the RDataSource itself, possibly adapting the work already done in `RArrowDS` to support Apache Arrow.
  * Support lazy read operations, where the parquet file is not read all at once but as needed.
  * Limit the actual reading to the columns actually being processed. 
  * Provide examples and tutorials on how to use it.
  * Benchmark the solution and provide comparisons with other `RDataSource` backends like ROOT `TFile`s or `CSV`.

## Expected results

A working RDataSource, tentatively named RParquetDS, which is able to read Parquet files and have them processed by ROOT via `RDataFrame`.

## Desirable Skills
  * Good knowledge of C++
  * Knowledge of ROOT and / or Apache Parquet a plus
  * Python experience a plus

## Mentors
  * [Giulio Eulisse](mailto:giulio.eulisse@cern.ch) CERN-EP-AIP
  * [Danilo Piparo](mailto:danilo.piparo@cern.ch) CERN-EP-SFT
