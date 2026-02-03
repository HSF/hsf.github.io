---
title: Publication of Omnifold weights
layout: gsoc_proposal
project: Omnifold
year: 2026
organization: 
   - CERN
   - StanfordUniversity
difficulty: medium
duration: 175
mentor_avail: June-October
project_mentors:
  - email: tanvi.wamorkar@cern.ch
    first_name: Tanvi
    last_name: Wamorkar
    organization: StanfordUniversity
    is_preferred_contact: yes
  - email: nachman@stanford.edu
    first_name: Benjamin
    last_name: Nachman
    organization: StanfordUniversity
    is_preferred_contact: no
---

## Description


**Standardizing the publication, preservation, and reuse of ML-based unfolding results**

This project is an effort to define **how machine-learning–based unfolding results (in particular OmniFold)** should be published in a way that is reusable, and compatible with **HEPData**.

Modern unfolding methods produce *per-event weights and trained models*, rather than fixed binned histograms. While this enables flexibility and reinterpretation, it also raises new challenges for publication, reproducibility, and long-term usability. Our goal is to try and define a coherent set of specifications, tools, and reference implementations to address those challenges.

The project will be based on the public, open-source [Omnifold repository](https://github.com/hep-lbdl/OmniFold/tree/main), which  contains examples of what omnifold weights are.Using that as a starting point, we want this project to define:

- **What results should be published when unfolding is performed using Omnifold**
- **How should the published weights be structured**
- **How they integrate with [HEPData](https://www.hepdata.net/about)**
- **How users can consume and reinterpret results**


## Task ideas
### 1. Data & Metadata Specification  
- Design a formal schema (YAML/JSON) describing OmniFold results
- Specify required vs optional fields
- Define conventions for:
  - Event-level weights (nominal and systematic)
  - Iteration structure (e.g. step-1 / step-2)
  - Dataset provenance (generators, detector simulation, selections)
  - Normalization and cross-section information

### 2. Per-Event Weights   
- Define a standard container format (e.g. HDF5 or Parquet)
- Specify naming conventions and indexing
- Support:
  - Nominal weights
  - Statistical replicas or bootstrap variations
  - Systematic variations
- Ensure scalability to large datasets

### 3. Model & Training Details  
- Define minimal vs full model publication options
- Standardize storage of:
  - Trained model checkpoints
  - Architecture definitions
  - Training hyperparameters
  - Feature preprocessing details
- Clarify which components are required for reinterpretation vs full retraining


### 4. Observable Definitions  
- Define a standard observable description format
- Include:
  - Physics definitions
  - Phase space restrictions
  - Object definitions
  - Binning (when applicable)
- Provide reference implementations in Python


### 5. Analysis & Reinterpretation   
- Develop a user-facing Python API to:
  - Load published weights (locally or from HEPData)
  - Apply weights to events
  - Compute arbitrary observables
  - Propagate statistical and systematic uncertainties
- Support common analysis workflows and plotting styles


### 6. Validation  
- Implement standardized validation procedures:
  - Closure tests
  - Normalization checks
  - Stability across iterations
- Define expected outputs and pass/fail criteria


### 7. HEPData Integration Layer  (Additional stretch goal)
Merge OmniFold outputs with HEPData infrastructure:
- Mapping OmniFold results to HEPData records
- Submission templates and guidelines
- Metadata conventions
- Validation steps


### 8. Examples & Reference Implementations  
- Provide complete examples using public datasets:
  - Unfolding → publication → reinterpretation
- Demonstrate:
  - How to publish OmniFold outputs
  - How to upload results to HEPData
  - How to reproduce published observables
  - How to compute new observables post-publication

## Expected results
By the end of the project, a Python package will be created that produces OmniFold weights in a standardized format, accompanied by data and metadata specifications for per-event weights, dataset selections, and optional model information. The project will also provide user-facing tools to apply weights, compute observables, and generate publication-quality plots, along with reference examples demonstrating integrating with HEPData.

## Requirements
  - Python
  - Jupyter notebooks
  - Interest in scientific software optimization 

## Links
  * [OmniFold](https://arxiv.org/abs/1911.09107)
  * [OmniFold Github](https://github.com/hep-lbdl/OmniFold)
  * [Omnifold PyPi package](https://pypi.org/project/omnifold/)
  

## How to Apply

Email mentors with a brief background and interest in scientific software stacks and high-energy physics. Please include "gsoc26" in the subject line. Mentors will provide an evaluation task after submission.  