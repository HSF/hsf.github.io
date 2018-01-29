---
title: CernVM-FS powered WebAssembly I/O
layout: gsoc_proposal
project: CernVM-FS
year: 2018
organization:
  - CERN
---

## Introduction

The physics experiments at the Large Hadron Collider (LHC) created millions of
lines of scientific C++ code, most of it is targeted to the Linux
platform.  The [emscripten](http://kripken.github.io/emscripten-site/index.html)
compiler allows us to compile C++ into asm.js or WebAssembly, and thus enables
us to [use any browser as a computing device](http://jblomer.web.cern.ch/jblomer/emscripten/main01.html)!

File based I/O in the browser's JavaScript sandbox, however, is a notorious problem. Many
physics applications load some data from files in order to do useful work,
for instance particle detector geometry, parton distribution functions,
parameter sets for Monte Carlo event generators. In Linux applications, such
data can be loaded from the [CernVM File System](https://github.com/cvmfs/cvmfs),
an HTTP based, read-only POSIX file system implemented in Fuse.

The emscripten compiler provides a [file system interface](http://kripken.github.io/emscripten-site/docs/api_reference/Filesystem-API.html#filesystem-api)
similar to Fuse.  It can be extended by custom file system backends.  The goal
of this project is to prototype a CernVM-FS backend for emscripten.


## Task

The emscripten JavaScript sources should be extended by a custom, new file system implementation.
The new file system implementation should be able to understand CernVM-FS repositories
and to load data from them. That will require, amongst other things, getting information
from sqlite files and zlib decompression implemented in JaveScript (or compiled from C into JavaScript/wasm).


## Expected results

A file system backend for emscripten such that C++ programs compiled with
emscripten can use C/C++ read-only file I/O on files in a CernVM-FS repository.


## Requirements

- C/C++
- JavaScript
- Understanding of POSIX file systems

## Mentors

 * [Jakob Blomer](mailto:jblomer@cern.ch)
 * [Radu Popescu](mailto:radu.popescu@cern.ch)
