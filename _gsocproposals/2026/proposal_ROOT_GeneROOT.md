---
title: Enhance and develop GeneROOT infrastructure
layout: gsoc_proposal
project: ROOT
year: 2026
difficulty: medium
duration: 350
mentor_avail: June-October
organization:
  - CompRes
project_mentors:
  - email: vvasilev@cern.ch
    first_name: Vassil
    last_name: Vassilev
    is_preferred_contact: yes
  - email: mvassilev@uni-plovdiv.bg
    organization: University of Plovdiv
    first_name: Martin
    last_name: Vasilev
---

## Description

The extraction of the human genome has historically presented significant technological and financial challenges, often costing millions of dollars. Recent advancements in sequencing techniques have dramatically reduced these expenses, enabling large-scale genome extraction and data storage. For context, a fully sequenced human genome typically generates approximately 500 GB of data. Analyzing such datasets across large cohorts for various research purposes frequently results in data volumes exceeding petabytes. This exponential growth in genomic data raises critical challenges related to storage, retrieval, processing, and visualization.

On the other hand, CERN has extensive expertise in managing massive datasets, particularly through its software framework ROOT, which is designed for handling large-scale physics data. The GeneROOT project aims to adapt ROOT for the processing of biological data instead of physics data. Initial prototypes of GeneROOT have already demonstrated superior performance in certain aspects compared to established bioinformatics tools.

The project holds significant potential for further advancements in data compression, storage efficiency, retrieval speed, computational processing, and visualization techniques. Additionally, an important area of exploration is GeneROOT’s capability to operate in high-performance computing (HPC) environments, potentially unlocking new efficiencies in large-scale bioinformatics research.

## Expected Results

* Benchmark on heavy bioinformatics datasets
* Benchmark on various file formats
* Review data compression algorithms adapted for genomic sequences
* Optimize indexing and search capabilities for large genomic datasets
* Add support for sort, merge, split, stats, etc.

## Requirements
* C++ and Python programming
* Familiarity with Git
* Knowledge of ROOT and/or the BAM file formats is a plus.

## Links
* [Latest Presentation on GeneROOT](https://indico.cern.ch/event/655464/)
* [ROOT](https://root.cern/)
* [GeneROOT](https://github.com/GeneROOT)
* [Previous GSoC project](https://compiler-research.org/assets/presentations/Aditya_Pandey_GSoC2025_final.pdf)

## AI Policy

AI assistance is allowed for this contribution. The applicant takes full responsibility for all code and results, disclosing AI use for non-routine tasks (algorithm design, architecture, complex problem-solving). Routine tasks (grammar, formatting, style) do not require disclosure.

## How to Apply

In addition to reaching out to the mentors by email, prospective candidates are required to complete [this form](https://forms.gle/AYgrJthYCRmBwwFL8)
