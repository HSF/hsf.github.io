---
title: Go-HEP/groot - Create a pure-Go dataframe package to access ROOT TTrees with groot
layout: gsoc_proposal
project: GoHEP
year: 2019
organization:
  - LPC-Clermont
  - CC-IN2P3
---

# Description

[Go-HEP](https://go-hep.org) is a set of libraries and applications allowing High Energy Physicists (`HEP`) to write efficient analysis code in the [Go](https://golang.org) programming language.
[Go](https://golang.org) brings the fast edit-compile-run cycle that interpreted language users know and the runtime efficiency that compiled languages users expect.
[Go-HEP](https://go-hep.org) provides the needed `HEP` oriented packages on top of this concurrency-enabled language.

The Go-HEP project currently provides limited read access to [ROOT](https://root.cern) files, the binary format that all LHC experiments use to store data, _via_ its [groot](https://godoc.org/go-hep.org/x/hep/groot) package.
`groot` also allows to create ROOT files with histograms and graphs.

But Go-HEP is missing a pure-Go library to present ROOT TTrees as dataframes.
The [Gonum](https://gonum.org) organization is in the process of developing a dataframe package, built off the [Apache Arrow](https://arrow.apache.org) project.

## Tasks

The proposed project aims at implementing a thin API on top of the `groot/rtree` package to expose any ROOT TTree as a dataframe, providing Gonum with some feedback with regards to its proposed `dframe` package.

We propose the following steps:

 * extract a ROOT TTree's schema and convert it into an Apache Arrow schema
 * create a dataframe off an Arrow schema, connect it to the low-level data representation of a TTree
 * implement convenience functions to:
   * create a 1-dim histogram off a dataframe
   * create a 2-dim histogram off a dataframe
   * create 2-dim scatters off a dataframe
 * implement the ability to add user columns to a dataframe, based off a user provided function depending on other columns from the dataframe
 * implement the ability to easily plot quantities or columns from a dataframe
 * implement the ability to save a dataframe as a ROOT TTree.

## Expected results

A package that can expose a ROOT TTree as a dataframe, usable for various High Energy Physics analyses or data science tasks.

## Requirements

- Go
- git

## Mentors

  * [Sebastien Binet](mailto:binet@cern.ch)
  * [Sebastien Gadrat](mailto:sebastien.gadrat@cc.in2p3.fr)

## Links

  * [Apache Arrow](https://arrow.apache.org)
  * [Go](https://golang.org)
  * [GoHEP](https://go-hep.org)
  * [Gonum](https://gonum.org)
  * [ROOT](https://root.cern)
