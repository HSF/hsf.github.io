---
title: Fast Merging of RNTuple Data Sets
layout: gsoc_proposal
project: ROOT
year: 2020
organization: CERN
---

## Description

The [ROOT](https://root.cern/) Software Framework is the cornerstone of many software stacks used by High Energy Physics (HEP) experiments, at CERN and other prestigious laboratories. It provides components which are fundamental for the entire data processing chain, from particle collisions to final publications, including final user data analysis, including modern machine learning techniques.

The **[RNTuple](https://github.com/root-project/root/tree/master/tree/ntuple/v7/doc)** classes provide ROOT’s new, experimental I/O subsystem for high-energy physics data. The RNTuple data layout is columnar and supports nested types (e.g., vectors of floats), conceptually similar to Apache Arrow or Apache Parquet.

A frequent operation is merging of data sets, in particular at the end of distributed data pipelines. For instance, users might use a cluster of nodes to filter a large data set. The input file is split for the individual nodes and each node produces a new RNTuple file containing a subset of its input part. These individual filter outputs should then be merged back into a single file. A naive approach would read each and every row from every file and write it out to a result file. Fast merging, in contrast, makes use of the low level RNTuple data format. Instead of parsing individual rows, data can be merged as a meta-data only operation where only headers and footers are processed but the actual data blocks are copied as is.

The project should, in a first step, develop a fast merge routine for ROOT RNTuple data sets. In a second step, this facility should be used by ROOT’s **hadd** program, a general merge utility for ROOT files

## Task ideas
 * Given two RNTuple data sets, implement schema comparison using the header information to determine whether the data sets can be merged
 * Given two _compatible_ RNTuple data sets, implement a merge routine that copies the data blocks and adjusts the footer
 * In the ROOT hadd utility, add code to identify RNTuple data sets
 * Use the RNTuple merger to handle RNTuple data sets in ROOT files processed with hadd
 * Stretch goal: investigate fast merging on a copy-on-write file system, where the merged file could be created by cloning the data blocks instead of copying

## Expected results
Working implementation of an RNTuple data set merger and additions to hadd in order to correctly handle RNTuples.

## Evaluation Task
Interested students please contact Jakob (jblomer@cern.ch) for a warm-up and evaluation task.

## Requirements
C++, low-level data storage and access programming

## Mentors
  * [Jakob Blomer](mailto:jblomer@cern.ch)
  * [Philippe Canal](mailto:pcanal@fnal.gov)

## Links
  * [ROOT](https://root.cern/)
  * [RNTuple Overview](https://indico.cern.ch/event/773049/contributions/3474746/attachments/1937507/3211341/rntuple-chep19.pdf)
  * [RNTuple Code](https://github.com/root-project/root/tree/master/tree/ntuple/v7)
  * [RNTuple Tutorials](https://github.com/root-project/root/tree/master/tutorials/v7/ntuple)