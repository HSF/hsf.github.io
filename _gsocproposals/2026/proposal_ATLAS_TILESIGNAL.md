---
title: AI-Accelerated Reconstruction for the ATLAS Tile Calorimeter at the HL-LHC
layout: gsoc_proposal
project: ATLAS
year: 2026
organization:
  - CERN
  - IFIC
difficulty: medium
duration: 350
mentor_avail: June-October
project_mentors:
  - email: Luca.Fiorini@cern.ch
    first_name: Luca
    last_name: Fiorini
    organization: IFIC
    is_preferred_contact: yes
  - email: fernando.carrio@cern.ch
    first_name: Fernando 
    last_name: Carriò
    organization: IFIC, CERN
    is_preferred_contact: yes
---

## Description

ATLAS will produce data at an unprecedented scale at the High-Luminosity LHC (HL-LHC). This project offers the opportunity to work on a real problem at the intersection of machine learning, real-time computing, and the experimental physics frontier, with direct relevance for the future ATLAS detector upgrade.

The student will develop and evaluate deep-learning-based signal reconstruction methods for the ATLAS Tile Calorimeter (TileCal), comparing them with classical algorithms and exploring how to deploy efficient inference on modern hardware accelerators (GPU and/or FPGA-friendly models).

Recent studies indicate that AI-based reconstruction can be implemented on FPGAs and outperform classical methods in amplitude and timing estimation, especially in challenging pile-up regimes. However, for real deployment, models must satisfy strict constraints on:
- latency (sub-microsecond scale, trigger-compatible),
- resource usage (memory and compute),
- robustness and reproducibility.

This project contributes to ongoing R&D for the TileCal readout upgrade and the development of sustainable, energy-efficient computing strategies and it addresses a real challenge for the next decade of LHC physics. The developed methods are also highly transferable to other domains requiring fast reconstruction, such as medical imaging and industrial monitoring.

## Task Ideas

- Understand the TileCal signal reconstruction problem
- Implement baseline reconstruction methods
- Develop a compact ML model for reconstruction
- Benchmark and compare performance
- Explore model optimization for deployment

## Expected Results and Milestones

- A reproducible reconstruction pipeline (baseline + ML)
- Quantitative performance comparison under HL-LHC-like conditions
- A trained compact model suitable for fast inference
- A final technical report and presentation

## Requirements

- Python programming skills
- ML fundamentals 
- Time series analysis or anomaly detection experience
- Interest in scientific software optimization 

## AI Policy

AI assistance is permitted. The applicant is fully accountable for all code and results and must disclose AI use for non-routine work (e.g., algorithm design, architecture, complex reasoning). Routine use for grammar or formatting does not need to be reported.

## How to Apply

Email mentors with a brief background and interest in Computing/particle physics. Please include "gsoc26" in the subject line. Mentors will provide an evaluation task after submission.

## Resources

- [ATLAS Experiment](https://atlas.cern/)
- [ATHENA Framework](https://atlas-software.docs.cern.ch/athena/basics/intro/)
- [TileCal IFIC Group](https://tilecal.ific.uv.es/tilecalweb/)
