---
title: Bytewise Online Autoregressive (BOA) Constrictor for HEP data compression
layout: gsoc_proposal
project: BOA
year: 2026
organization: UManchester
difficulty: medium
duration: 350
mentor_avail: June-October
project_mentors:
  - email: caterina.doglioni@manchester.ac.uk
    first_name: Caterina
    last_name: Doglioni
    organization: University of Manchester
    is_preferred_contact: yes
  - email: sanjiban.sengupta@cern.ch
    first_name: Sanjiban
    last_name: Sengupta
    organization: CERN
    is_preferred_contact: no
  - email: akshat.gupta-4@postgrad.manchester.ac.uk
    first_name: Akshat
    last_name: Gupta
    organization: University of Manchester
    is_preferred_contact: yes
---

## Description

As global demand for data storage and sharing continue to grow, managing such volumes has become increasingly challenging. This issue is particularly acute in high-energy physics (HEP), where vast and complex datasets routinely push the limits of existing compression and storage technologies: each year, experiments at the Large Hadron Collider (LHC) at CERN produce approximately thirty petabytes of data. 

Current solutions, such as the ROOT framework combined with algorithms like Lempel–Ziv–Markov chain Algorithm (LZMA) and ZLIB, are currently used to address these challenges. The Bytewise Online Autoregressive (BOA) Constrictor is a streaming lossless compressor built on the Mamba architecture and coupled to a parallelised range coder, aiming to achieve greater gains in storage efficiency through improved lossless compression methods. 
Currently, this improved compression comes at the expense of lower throughput on current hardware, highlighting the deployment trade-offs for neural compressors in HEP. 

In this project, we aim to support the ongoing developments of BOA by expanding the existing end-to-end experiment scripts into a comprehensive benchmark suite, by focusing on small models and physics-informed priors, and by benchmarking alternative backbones to quantify when/why Mamba is competitive for neural compression. 

## Task ideas

- integrate physics-informed-style constraints (e.g., conservation/symmetry/equivariance; key challenge is applying this to a byte stream) and run controlled ablations;  
- extend experiment configurations to run parameter/compute-matched sweeps across model sizes (tiny→small), including pruning/quantisation/distillation variants; 
- add backbone benchmarks that are alternative to Mamba (e.g., Transformer, GRU/LSTM, CNN-style, MinGRU, and other lightweight sequence models) under identical coding and evaluation pipelines (this may lead to us finding better alternatives to Mamba)

## Expected results and milestones

- expanded scripts/configs covering multi-backbone, multi-size grids; 
- reproducible ablation runs; 
- consolidated results report identifying the best size–compression–physics trade-offs and a fair comparison of Mamba versus competing backbones.

## Requirements

- Python and C++ programming skills
- Expertise in ML/AI (experience with the models and techniques mentioned above is preferred)
- Familiarity with GitHub for project collaboration and open source development

## AI Policy

AI assistance is allowed for this contribution, but its use will not be welcomed in the candidate selection exercise or for writing the initial proposal. 
The applicant takes full responsibility for all code and results, disclosing AI use for non-routine tasks (algorithm design, architecture, complex problem-solving). 
Routine tasks (grammar, formatting, style) do not require disclosure.

## How to apply

Please email the mentors with a brief background and interest in green computing and sustainable research. Include "gsoc26" in the subject line. Mentors will provide an evaluation task after submission.

## Resources

- [BOA paper on arXiv](https://arxiv.org/abs/2511.11337)
- [BOA GitHub repository (from Zenodo)](https://zenodo.org/records/17571973)
