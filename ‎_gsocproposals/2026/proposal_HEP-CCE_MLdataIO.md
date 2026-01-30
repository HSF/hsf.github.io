---
title: Characterizing I/O Performance for ML Data Loaders at Scale Using Darshan
layout: gsoc_proposal
project: HEP-CCE
year: 2026
organization:
  - ANL, University of Oslo
difficulty: medium
duration: 175
mentor_avail: June-October
project_mentors:
  - email: Rui.Wang@cern.ch
    first_name: Rui
    last_name: Wang
    organization: ANL
    is_preferred_contact: yes
  - email: oyildiz@anl.gov
    first_name: Orcun
    last_name: Yildiz
    organization: ANL
    is_preferred_contact: yes
  - email: martin.foll@cern.ch
    first_name: Martin
    last_name: Foll
    organization: University of Oslo
    is_preferred_contact: no
---

## Description

Modern machine learning (ML) workflows in High Energy Physics (HEP) increasingly rely on large-scale detector-level datasets, where individual events are large and overall data volumes grow rapidly. As a result, data loading has become one of the most I/O-intensive components of ML training pipelines, often limiting achievable batch sizes, data throughput, and overall scalability on high-performance computing (HPC) systems.

This project aims to systematically characterize and analyze the I/O behavior of ML data loaders used in HEP by leveraging Darshan, a lightweight and widely deployed HPC I/O characterization tool. The study will focus on understanding how data format, access pattern, and data loader design impact I/O performance at scale.

Two primary classes of data loaders will be evaluated:

- The native PyTorch DataLoader, commonly used in ML training workflows
- A ROOT-based DataLoader for PyTorch, a newer development enabling native reading of ROOT and RNTuple data structures

These loaders will be benchmarked using representative HEP data formats, including ROOT RNTuple, HDF5, NumPy NPZ, and CSV, under realistic ML training workloads. By collecting and analyzing Darshan I/O traces on production HPC systems (e.g., NERSC Perlmutter), the project will identify performance bottlenecks, characterize I/O access patterns, and provide actionable recommendations for optimizing ML data ingestion pipelines in HEP.

## Task Ideas

- Design and implement a benchmark framework for ML training workflows using PyTorch with multiple data loaders and data formats.
- Run controlled I/O performance experiments on HPC systems using Darshan instrumentation
- Analyze Darshan logs to characterize I/O patterns such as file access frequency, read sizes, metadata operations, and concurrency.
- Compare I/O bandwidth, latency, and scalability across data loaders and formats
- Evaluate the impact of data loader configuration parameters (e.g., number of workers, prefetching, sharding)
- Summarize findings and propose optimization strategies for scalable ML data loading in HEP environments.

## Expected Results and Milestones

- Familiarization with HEP datasets for ML, PyTorch data loading, and Darshan I/O profiling
- Setup of benchmark environment and representative datasets on HPC systems
- Implementation of PyTorch and ROOT-based DataLoader benchmarks
- Large-scale I/O profiling and data collection using Darshan
- Analysis and comparison of I/O performance across data formats and loaders
- Optimization recommendations and documentation

## Requirements

- Python programming skills
- Familiarity with basic machine learning concepts
- Familiarity with basic I/O concepts
- Interest in performance analysis and large-scale computing

## AI Policy

AI assistance is allowed for this contribution. The applicant takes full responsibility for all code and results, disclosing AI use for non-routine tasks (algorithm design, architecture, complex problem-solving). Routine tasks (grammar, formatting, style) do not require disclosure.

## How to Apply

Email mentors with a brief background and interest in ML/large-scale computing. Please include "gsoc26" in the subject line. Mentors will provide an evaluation task after submission.

## Resources

- [HEP-CCE Project](https://www.anl.gov/hep-cce)
- [Darshan I/O Characterization Tool](https://www.mcs.anl.gov/research/projects/darshan/)
- [PyTorch DataLoader](https://docs.pytorch.org/tutorials/beginner/basics/data_tutorial.html) Documentation
- [ROOT](https://root.cern/doc/master/index.html) and [RNTuple](https://root.cern/doc/v622/md_tree_ntuple_v7_doc_README.html) Documentation
- [NERSC Perlmutter System Documentation](https://docs.nersc.gov/)


