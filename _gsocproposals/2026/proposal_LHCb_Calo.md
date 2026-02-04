---
title: Transformer-based Reconstruction for Electromagnetic Calorimeters in Future LHC Upgrade Experiments
layout: gsoc_proposal
project: LHCb
year: 2026
organization:
  - UB
  - CERN
difficulty: medium
duration: 175
mentor_avail: June-October
project_mentors:
  - email: felipe.luan@cern.ch
    first_name: Felipe Luan
    last_name: Souza de Almeida
    organization: UB
    is_preferred_contact: yes
  - email: carla.marin.benito@cern.ch
    first_name: Carla
    last_name: Marin Benito
    organization: UB
    is_preferred_contact: no
---

## Description

 Electromagnetic calorimeter reconstruction is a critical component of precision measurements involving neutral particles such as photons and neutral pions (π⁰). The achievable energy resolution directly impacts the sensitivity of physics analyses relying on these final states, including rare decays and CP violation measurements.

In the context of future LHC upgrades, calorimeter reconstruction must satisfy increasingly stringent real-time constraints, making both reconstruction quality and inference performance essential. Transformer-based machine learning models have recently emerged as a promising technology for modeling complex detector responses and long-range correlations, with potential advantages in reconstruction accuracy and scalability.

The goal of this project is to design, implement, and benchmark a Transformer-based reconstruction pipeline for electromagnetic calorimeters, focusing on energy resolution and inference performance. The developed approach will be quantitatively compared to existing standard reconstruction algorithms and GNN-based methods. The project emphasizes software implementation, validation, and benchmarking, rather than open-ended machine learning research, making it well suited for the GSoC timeline.

## Task Ideas

- Design, implementation, and benchmarking of a Transformer-based reconstruction pipeline for electromagnetic calorimeters

## Expected Results and Milestones

### Core deliverables

- A working, documented end-to-end Transformer-based reconstruction pipeline for electromagnetic calorimeter energy reconstruction.

- Energy response and resolution studies using single-photon simulated samples.

- Quantitative comparison with standard reconstruction algorithms and existing GNN-based approaches.

- Benchmarking of inference performance (e.g. latency and throughput) relevant for real-time reconstruction constraints.

### Stretch goals (depending on progress)

- Performance studies under high-luminosity conditions using single-photon events overlaid with minimum-bias background.

- Extended benchmarking studies across different model configurations and detector conditions.

## Requirements

* Intermediate-level Python programming skills
* Fundamentals of machine learning
* Familiarity with PyTorch or a similar ML framework
* Basic knowledge of particle physics or detector concepts is beneficial but not required

## AI Policy

AI assistance is allowed for this contribution. The applicant takes full responsibility for all code and results, disclosing AI use for non-routine tasks (algorithm design, architecture, complex problem-solving). Routine tasks (grammar, formatting, style) do not require disclosure.

## How to Apply

Email mentors with a brief background and interest in ML/particle physics. Please include "gsoc26" in the subject line. Mentors will provide an evaluation task after submission.

## Resources

*   *A Survey on Transformers* (<https://arxiv.org/abs/2106.04554>)
*   *Transformers are Graph Neural Networks* (<https://arxiv.org/abs/2506.22084>)
*   PyTorch documentation: [https://docs.pytorch.org/docs/stable/index.html](https://docs.pytorch.org/docs/stable/index.html)
*   [LHCb experiment](https://lhcb.web.cern.ch/)
*   *Calibration and performance of the LHCb calorimeters in Run 1 and 2 at the LHC* (<https://arxiv.org/abs/2008.11556>)
*   *Graph Clustering: a graph-based clustering algorithm for the electromagnetic calorimeter in LHCb* (<https://arxiv.org/abs/2212.11061>)
