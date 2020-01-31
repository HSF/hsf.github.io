---
title: Pre-conditioners applied to ROOT compression algorithms
layout: gsoc_proposal
project: ROOT
year: 2020
organization:
  - UNL
  - MIR
---

## Description

Pre-conditioning is an algorithm that rearranges typed, binary data to improve compression. More information can be found here: [1],[2]

The idea of the project is to develop different filtering or transformation schemes, that could be applied to ROOT data, while stored in intermediate I/O buffers (baskets). 

In ROOT, the serialization of variable-sized data (containing C-style arrays) produces two internal arrays: one contains the branch data for each of events while the other contains the byte offset of each of events in the branch data. LZ4 [3] compression algorithm achieves its performance by looking for byte-aligned patterns (as opposed to ZLIB [4] compresison algorithm, which works on individual bits) and lacks the Huffman encoding pass, this results in the offset array sequence being effectively incompressible using LZ4.

Some time ago, [Bitshuffle preconditioner](https://github.com/kiyo-masui/bitshuffle)[10] was demonstrated as a possible pre-conditioner for ROOT data with LZ4 for lossless compression [6]. To improve the performance of LZ4 in this case, we investigated the combination of LZ4 with various “pre-conditioners”. Pre-conditioners transform the sequence of input bytes according to a simple, deterministic algorithm prior to applying the compression algorithm. The two algorithms investigated, inspired by the Blosc library [2], are Shuffle and BitShuffle [10]. Both preconditioners rearrange the input array’s bytes by reading through the data using fixed strides. The resulting output of the preconditioner often contains long sequences of repeated bytes, improving the compression ratio for LZ4. One of the issues exposed was that it is difficult for ROOT to compress its buffers now due to its 9-byte header.

The goal of the project is to validate the possibility to use pre-conditioners in the ROOT compression layer used to compress both ROOT file formats (TTree [9] and RNTuple [10]) for the fastest ROOT compression algorithms [6]: LZ4, ZSTD [5].

The second part of the project could be to understand how we can extend feature in the context of both lossy and lossless compression algorithms.

Extra task that could be investigated is new BYTE_STREAM_SPLIT encoding [8] that improves compression ratio and compression speed for certain types of floating-point data where the upper-most bytes of a values do not change much. The exisiting compressors and encodings in ROOT do not perform well for such data due to noise in the mantissa bytes. The new encoding improves results by extracting the well compressible bytes into separate byte streams which can be afterwards compressed by a compressor like ZSTD. [7]

## Task ideas
 * Integrate pre-conditioners in ROOT compression layer (based on our preliminary tests).
 * Test pre-conditioners for existing fast ROOT compression algorithms.
 * Validate results for the both ROOT file formats: ROOT TTree and ROOT RNTuple.

## Expected results
The deliverable of the project will be a demonstrator showing compression improvement compared to the existing implementation, as well as a detailed report and presentation on performance comparison of the pre-conditioners and compression algorithms used in ROOT. ROOT’s compression library and build system should be extended to support pre-conditioners for compression algorithms. 

## Requirements
We're seeking a candidate proficient in C++ with understanding how compression algorithms work.

## Mentors
  * [Oksana Shadura](mailto:oksana.shadura@cern.ch)
  * [Brian Paul Bockelman](mailto:bbockelman@morgridge.org)
  * [Ken Bloom](mailto:kenbloom@unl.edu)

## Links
  * [A compression scheme for radio data in high performance computing](https://arxiv.org/abs/1503.00638)
  * [Blosc](https://blosc.org/pages/blosc-in-depth/)
  * [LZ4](https://github.com/lz4/lz4)
  * [ZLIB](https://www.zlib.net/)
  * [ZSTD](https://github.com/facebook/zstd)
  * [ROOT I/O compression algorithms](https://arxiv.org/abs/1906.04624)
  * [Byte stream split in Apache Parquet format](https://github.com/apache/parquet-format/blob/master/Encodings.md#byte-stream-split-byte_stream_split--9)
  * [Evaluation of BYTE_STREAM_SPLIT encoder for Apache Arrow](https://github.com/martinradev/arrow-fp-compression-bench/blob/master/LOSSLESS.md)
  * [TTree](https://root.cern.ch/root/htmldoc/guides/users-guide/Trees.html)
  * [RNTuple](https://root.cern.ch/doc/master/md_tree_ntuple_v7_doc_README.html)
  * [Bitshuffle preconditioner](https://github.com/kiyo-masui/bitshuffle)
