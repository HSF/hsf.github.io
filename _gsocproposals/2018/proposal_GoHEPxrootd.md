---
title: Go-HEP/xrootd - Create a pure-Go client for XRootD
layout: gsoc_proposal
project: GoHEP
year: 2018
organization: LPC-Clermont
---

# Description

[Go-HEP](https://go-hep.org) is a set of libraries and applications allowing High Energy Physicists (`HEP`) to write efficient analysis code in the [Go](https://golang.org) programming language.
[Go](https://golang.org) brings the fast edit-compile-run cycle that interpreted language users know and the runtime efficiency that compiled languages users expect.
[Go-HEP](https://go-hep.org) provides the needed `HEP` oriented packages on top of this concurrency-enabled language.

The Go-HEP project currently provides limited read access to [ROOT](https://root.cern) files, the binary format that all LHC experiments use to store data.
But Go-HEP is missing a pure-Go library to access to data repositories, something that is tackled by [XRootD](http://xrootd.org), a LGPL-licensed C++ library.

## Tasks

The proposed project aims at implementing a pure-Go BSD-3 client library for XRootD.
As the C++ XRootD library is licensed under LGPL, a fair amount of the proposed project work will involve reading the [XRootD protocol specifications (PDF)](http://xrootd.org/doc/dev45/XRdv310.pdf) without looking at the original C++ code.

We propose the following steps:

 * implement the client/server initial handshake
 * implement the client request format
 * implement the server response format
 * implement the following client requests: 
   * `auth`, `bind`, `unbind`,
   * `close`, `open`, `read`,
   * `ping`, `protocol`,
 * add tests and benchmarks (CPU, Mem, I/O) for each step
 * leverage Go builtin features to make the XRootD client concurrent and scalable.

## Expected results

Working command line client for XRootD (built on top of a clean API) that can read files served by a XRootD server.

## Requirements

- Go
- git

## Mentors

  * [Sebastien Binet](mailto:binet@cern.ch)

## Links

  * [Go](https://golang.org)
  * [GoHEP](https://go-hep.org)
  * [ROOT](https://root.cern)
  * [XRootD](http://xrootd.org)
