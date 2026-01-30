---
title: Publication of Omnifold weights
layout: gsoc_proposal
project: Omnifold
year: 2026
organization: CERN
---

## Description


**Standardizing the publication, preservation, and reuse of ML-based unfolding results**

This project is an effort to define **how machine-learning–based unfolding results (in particular OmniFold)** should be published in a way that is reusable, and compatible with **HEPData**.

Modern unfolding methods produce *per-event weights and trained models*, rather than fixed binned histograms. While this enables flexibility and reinterpretation, it also raises new challenges for publication, reproducibility, and long-term usability. Our goal is to try and define a coherent set of specifications, tools, and reference implementations to address those challenges.

The project will be based on the public open-source [Omnifold repository](https://github.com/hep-lbdl/OmniFold/tree/main), which also contains examples of what omnifold weights are and using that as a starting point we want this project to define:

- **What results should be published when unfolding is performed using Omnifold**
- **How should the published weights be structured**
- **How they integrate with (HEPData)[https://www.hepdata.net/about]**
- **How users can consume and reinterpret results**


## Task ideas
Here is a list of ideas of what the sub-components of the package will be:
### 1. Data & Metadata Specification  
<!-- **Foundational layer** -->

Defines a schema for publishing OmniFold outputs, including:
- Event-level weights (nominal and systematic)
- Iteration structure (e.g. step-1 / step-2)
- Dataset selections
- Normalization
---

### 2. Per-Event Weights   

Standardized publication of:
- Per-event OmniFold weights
- Minimal associated metadata

### 3. Model & Training Details  

Optional publication of:
- Trained neural network checkpoints
- Architecture definitions
- Training configurations
- Feature preprocessing details


### 4. Observable Definitions  

Defines unfolded observables, including:
- Physics definitions
- Phase space restrictions
- Binning (when applicable)
- Reference implementations


### 5. Analysis & Reinterpretation   
**User-facing layer**

Tools to:
- Load published weights (locally or from HEPData)
- Apply weights to events
- Compute arbitrary observables
- Propagate statistical and systematic uncertainties
- Produce publication-quality plots

Enables reinterpretation **without rerunning the unfolding**.


### 6. Validation  

Provides standardized validation procedures, including:
- Closure tests
- Normalization checks
- Consistency tests

Ensures published results are scientifically robust and reviewable.


### 7. HEPData Integration Layer  

Merge OmniFold outputs with HEPData infrastructure:
- Mapping OmniFold results to HEPData records
- Submission templates and guidelines
- Metadata conventions
- Validation steps


### 8. Examples & Reference Implementations  

End-to-end examples using public datasets demonstrating:
- How to publish OmniFold outputs
- How to upload to HEPData
- How to reproduce published observables
- How to compute new observables post-publication

## Expected results
Working implementation of a Python library that hides the complexity of submitting distributed ROOT TDataFrame jobs to computational clusters.

## Requirements
  - Python
  - Jupyter notebooks
  - Interest in scientific software optimization 

## Mentors
  * [TANVI WAMORKAR](mailto:tanvi.wamorkar@cern.ch)
  * [Benjamin Nachman](mailto:nachman@stanford.edu)

## Links
  * [OmniFold](https://arxiv.org/abs/1911.09107)
  * [OmniFold Github](https://github.com/hep-lbdl/OmniFold)
  * [Omnifold PyPi package](https://pypi.org/project/omnifold/)
  

## How to Apply

Email mentors with a brief background and interest in scientific software stacks and high-energy physics. Please include "gsoc26" in the subject line. Mentors will provide an evaluation task after submission.  