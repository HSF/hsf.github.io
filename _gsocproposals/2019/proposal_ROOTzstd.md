---
title: Novel Applications of Zstandard (ZSTD) compression algorithm to ROOT
layout: gsoc_proposal
project: ROOT
year: 2019
organization:
  - UNL
---

## Description
ROOT [1] is a framework for data processing, born at CERN, at the heart of the research on high-energy physics. ROOT consists of multiple components such as I/O, a C++ interpreter, GUI, and math libraries.  One of its tasks is to reduce the on-disk usage of physics data; a typical approach is to use various compression techniques.  ROOT I/O subsystem supports data compression using common compression algorithms such as ZLIB, LZMA and LZ4.

Zstd [2] is interesting fast, a lossless compression algorithm that can offer higher compression ratios comparing to most LZ-based compression algorithms, such as ZLIB or LZMA.  ZSTD offers higher decompression data rates, as it is shown in standalone benchmarks [3] tested by Facebook. Other ZSTD functionality includes a special training mode, used to tune the algorithm for specific data patterns. The result of this training is stored in a buffer (a dictionary) which must be loaded before compression and decompression. Use of these dictionaries significantly improves the compression ratio of small data buffers, as found in ROOT-formatted files.

This project is to investigate application of ZSTD within the ROOT framework; benchmark it in comparison to the other algorithms; test it against real LHC data files; and investigate schemes to integrate dictionary-based compression in ROOT files.

## Task ideas
  * Work on integration of ZSTD compression algorithm as a part of supported algorithms by  ROOT I/O subsystem.
  * Introduce and improve a training mode for compression and decompression ROOT files.
  * Provide performance compression tests on various LHC experiment data sets.


## Expected results
Investigate application of ZSTD within the ROOT framework, benchmark it against real LHC data files and investigate schemes to integrate dictionary-based compression in ROOT files.

## Desirable Skills
  * C++ knowledge
  * Interest in compression algorithms technologies

## Mentors
  * [Oksana Shadura](mailto:oksana.shadura@cern.ch)
  * [Brian Bockelman](mailto:bbockelman@morgridge.org)

## Links
   1. [https://github.com/root-project/root](https://github.com/root-project/root)
   2. [https://github.com/facebook/zstd](https://github.com/root-project/root)
   3. [https://github.com/facebook/zstd#benchmarks](https://github.com/root-project/root)
