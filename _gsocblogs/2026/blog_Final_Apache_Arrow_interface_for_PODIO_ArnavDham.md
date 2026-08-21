---
project: HSF
title: "GSoC 2026 Final Submission: Apache Arrow interface for PODIO"
author: Arnav Dham
photo: blog_authors/ArnavDham.jpg
avatar: https://avatars.githubusercontent.com/arnavdham
date: 21.08.2026
year: 2026
layout: blog_post
logo: hsf_logo_angled.png
intro: |
  This project aimed to implement a new Apache Arrow backend for PODIO (Plain-Old-Data I/O), a C++ library designed for high-performance data modeling in particle physics. Over the summer, I added an in-memory Apache Arrow backend(Along with parquet writing and reading capability) to enable language-independent, columnar data access for flat and nested structures, improving throughput and enabling modern heterogeneous computing workflows.
---

|  |  |
| --- | --- |
| Name | [Arnav Dham](https://github.com/arnavdham) |
| Organization | [CERN](https://home.cern/), [HSF](https://hepsoftwarefoundation.org/) |
| Mentors | [Dmitry Kalinkin](https://github.com/veprbl), [Wouter Deconinck](https://github.com/wdconinc) |
| Project | [Apache Arrow interface for PODIO](https://hepsoftwarefoundation.org/gsoc/2026/proposal_PODIO_Arrow.html) |

## Important Links
* **Problem Statement:** [Apache Arrow interface for PODIO](https://hepsoftwarefoundation.org/gsoc/2026/proposal_PODIO_Arrow.html)
* **Initial Proposal:** [Google Docs Link](https://docs.google.com/document/d/17sUP4Zuf_exjlZ7Vpv_L62VM8HAh9EjlNreMTpG9SNk/edit?tab=t.0)
* **Meetings Notes:** [Google Docs Link](https://docs.google.com/document/d/17j8daTdql9IqkXbE_RCasqxsH3EVS7_bUa1eVv21kNI/edit?tab=t.0#heading=h.ofkp8t9d422)
* **Slides for Final Presentation:** [Google Slides Link](https://docs.google.com/presentation/d/1Z0bmI0ekUmMYdcQHJa_47hRGsjZt8oV9rFPwqCtdU4E/edit?slide=id.p1#slide=id.p1)
* **Repository:** [AIDASoft/podio](https://github.com/AIDASoft/podio)
* **Tracking Issue:** [#967](https://github.com/AIDASoft/podio/issues/967)

## Goals of the Project
This project aimed to implement a new Apache Arrow backend for PODIO (Plain-Old-Data I/O), a C++ library designed for high-performance data modeling in particle physics. Currently, PODIO translates YAML-defined Event Data Models (EDM) into C++ code, providing persistence through ROOT and SIO formats. This project added an in-memory Apache Arrow backend to enable language-independent, columnar data access for flat and nested structures.

While ROOT provides a columnar backend when written to disk, this project introduces an in-memory columnar backend. This integration enables Selective Field Projection, allowing analysis tools to load only the specific subsets of data required for a calculation. Furthermore, it provides the capability for Inter-Process Communication (IPC), which is what truly enables streaming readout and reconstruction frameworks. This capability would also be highly useful for heterogeneous computing (e.g., on GPUs). It also removes serialization overhead and enables seamless serialization into industry-standard formats like Parquet.

## What I Did
Over the course of GSoC 2026, I completed the following major features:

* **Arrow Schema Generation:** Extended the PODIO code generation engine (using Jinja2 templates) to automatically generate an Apache Arrow Schema based on YAML-defined EDMs.
* **Frame-to-Table Conversion (Serialization):** Implemented the ability to convert a `podio::Frame` (the core container for event data) into an `arrow::Table`. This involved wrapping existing PODIO data vectors into `arrow::Buffer` objects to enable zero-copy memory access, as well as handling variable-length arrays (VectorMembers) and object relations.
* **Table-to-Frame Conversion (Deserialization):** Implemented the inverse engine, allowing the reconstruction of a `podio::Frame` from an `arrow::Table`. This cleanly recreates the relationship graph and resolves composite keys back to C++ ObjectIDs.
* **Backend Library Refactoring:** Refactored the dynamic backend loading mechanism in PODIO and successfully integrated the `PodioArrow` library suffix across CMake configurations.
* **Read Path Optimization:** Optimized the Arrow backend read path to maximize I/O throughput.
* **EDM4hep Integration:** Updated EDM4hep to build and install the `ArrowMapper` correctly when PODIO supports it, ensuring seamless integration for end users.
* **Parquet Integration:** Implemented reading and writing capabilities to the `.parquet` format for persistent storage using the `arrow::dataset` and `parquet` C++ libraries.
* **Performance Benchmarking & Optimization:** Designed a modular benchmark that isolates each stage of the data path via UNIX pipes. Processing a heavy EIC dataset (363 collections/event) achieved an Arrow IPC stream rate of 26.8 MB/s (18.1 frames/s). Using `perf`, we eliminated critical bottlenecks in the materialization stage (Arrow ➔ C++) by adding vector `.reserve()` capacities to avoid `sysmalloc` overhead and hoisting O(N) schema string lookups to O(1), bringing materialization time down to just 15ms per frame.

## Current State
The core functionality of the Apache Arrow backend for PODIO has been completed, merged, and validated. The `PodioArrow` library is capable of dynamically translating PODIO frames to and from Arrow columnar data formats with no data loss, correctly resolving both primitive values and complex object relations. The EDM4hep ecosystem is also successfully integrated with the new backend.

The Parquet serialization layer is fully implemented and is currently undergoing review upstream.

## What's Left to Do
**Merge Parquet Serialization:** The PR (#1002) for writing and reading from Parquet files is currently open and needs to be merged after final reviews.

## Pull Requests

### Upstream Merges (AIDASoft/podio & key4hep/EDM4hep)
* [MERGED] [feat: Add Apache Arrow schema mapper generation to code generator (#966)](https://github.com/AIDASoft/podio/pull/966)
* [MERGED] [FrametoTable for Arrow backend (#980)](https://github.com/AIDASoft/podio/pull/980)
* [MERGED] [Implement Arrow-to-Frame Conversion (Deserialization) for Arrow Backend (#987)](https://github.com/AIDASoft/podio/pull/987)
* [MERGED] [Clean up SIO and Arrow configuration export (#990)](https://github.com/AIDASoft/podio/pull/990)
* [MERGED] [Refactor backend library loading and rename Arrow suffix to PodioArrow (#999)](https://github.com/AIDASoft/podio/pull/999)
* [MERGED] [Optimize Arrow Backend Read Path (#1001)](https://github.com/AIDASoft/podio/pull/1001)
* [MERGED] [Build and install ArrowMapper if podio supports it (EDM4hep #502)](https://github.com/key4hep/EDM4hep/pull/502)
* [MERGED] [Update CMake configuration to use new PodioArrow library suffix (EDM4hep #509)](https://github.com/key4hep/EDM4hep/pull/509)
* [OPEN] [feat: writing/reading to parquet (#1002)](https://github.com/AIDASoft/podio/pull/1002)

### Benchmarking & Performance Validation
* [REFERENCE] [Benchmarking Scripts and Results (#3)](https://github.com/arnavdham/podio/pull/3) Note: This pull request contains the performance benchmarking code that was essential for validation. While it was not intended to be merged into the upstream repository, it played a critical role in verifying the project's I/O throughput improvements.

## Challenges and Learnings
* **Performance Profiling & Bottleneck Analysis:** A major technical challenge was configuring and getting the `perf` profiling tools to run correctly within our environment. I spent significant time conducting extensive performance runs and analyzing the output to identify critical I/O bottlenecks in the data path, which directly informed the optimization of the Arrow backend read path.
* **Parquet Storage Architecture:** A significant architectural challenge emerged when deciding how to structure the data for Parquet serialization. I had to carefully evaluate and benchmark the trade-offs between using a "wide schema" (storing all collections as columns in a single file) versus a "one category per file" approach. Balancing read/write performance, file size overhead, and query usability for end-users was a complex but highly rewarding dilemma to solve.
* **CMake & Build Systems:** Contributing to multiple interconnected repositories (PODIO and EDM4hep) expanded my understanding of CMake, dynamic library loading, and robust build system configuration.
