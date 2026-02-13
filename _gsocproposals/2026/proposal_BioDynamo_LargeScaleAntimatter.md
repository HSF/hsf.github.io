---
title: BioDynaMo Large-Scale Antimatter Simulation
layout: gsoc_proposal
project: BioDynamo
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
    organization: Princeton University
  - email: lukas.johannes.breitwieser@cern.ch
    first_name: Lukas
    last_name: Breitwieser
    organization: CERN
---

## Description

Deliver a self-contained BioDynaMo module and research prototype that enables validated, reproducible simulations of charged antiparticle ensembles in Penning-trap-like geometries at scales beyond existing demonstrations. The project generalizes prior BioDynaMo Penning-trap work into a reusable, documented, and scalable module suitable for antimatter-motivated studies and other charged-particle systems.

The student will extend BioDynaMo with a focused set of features (pluginized force models, neighbor search tuned for charged particles, elastic runtime hooks, and analysis/visualization pipelines), validate the models on canonical testcases (single-particle motion, small plasma modes), and demonstrate scaling and scientific workflows up to the largest feasible size within available resources. BioDynaMo already provides an agent/plugin API, parallel execution (OpenMP), and visualization hooks (ParaView/VTK). A prior intern report demonstrates a Penning-trap proof-of-concept and identifies directions for extension (custom forces, multi-scale runs, hierarchical models, CI, containerization)[[1]](https://repository.cern/records/7capf-rqp49). 

## Engineering Goals
* Implement a BioDynaMo plugin module (“AntimatterKernel”) optimized for charged-particle workloads, including SoA-compatible data layouts, spatial decomposition, and an efficient neighbor search.
* Enable elastic and reproducible execution via containerized workflows and runtime configuration for local, HPC, or cloud environments.
* Provide performance instrumentation and a small, well-documented benchmark suite integrated with BioDynaMo’s tooling.

## Physics/Scientific Goals
* Implement physics components as BioDynaMo plugins: Penning-trap external fields, Coulomb interactions (pairwise with documented extension points for approximations), stochastic annihilation handling, and basic species support.
* Validate against analytic and reference scenarios (single-particle trapping, basic plasma oscillation modes), with clearly stated assumptions and limits.
* Perform a limited parameter sweep (e.g. density, magnetic field, trap voltage) at increasing scale to explore collective behavior observable within accessible regimes.

## Expected Results
* A BioDynaMo plugin/module implementing charged-particle dynamics suitable for antimatter-motivated simulations.
* A set of validated physics testcases reproducing canonical scenarios, with documented assumptions and limitations.
* A scalable and reproducible simulation workflow, including performance instrumentation and example benchmark configurations.
* Elastic execution artifacts (containers and run scripts) enabling consistent execution across local, HPC, and cloud systems.
* Analysis and visualization pipelines producing scientifically meaningful observables (e.g. density profiles, energy spectra, annihilation maps).
* A public open-source release with documentation and a short technical report or draft publication suitable for a workshop or conference.


## Requirements

* Automatic differentiation
* Parallel programming
* Reasonable expertise in C++ programming

## Links
* [Repo](https://github.com/BioDynaMo/biodynamo)

## AI Policy

AI assistance is allowed for this contribution. The applicant takes full responsibility for all code and results, disclosing AI use for non-routine tasks (algorithm design, architecture, complex problem-solving). Routine tasks (grammar, formatting, style) do not require disclosure.

## How to Apply

In addition to reaching out to the mentors by email, prospective candidates are required to complete [this form](https://forms.gle/AYgrJthYCRmBwwFL8)
