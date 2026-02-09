---
title: Consolidate and advance the GPU infrastructure in Clad
layout: gsoc_proposal
project: Clad
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
  - email: david.lange@cern.ch
    first_name: David
    last_name: Lange
    organization: Princeton University
---

## Description

Clad is a Clang-based automatic differentiation (AD) plugin for C++. Over the past years, several efforts have explored GPU support in Clad, including differentiation of CUDA code, partial support for the Thrust API, and prototype integrations with larger applications such as XSBench, LULESH, a tiny raytracer in the Clad repository, and LLM training examples (including work carried out last year). While these efforts demonstrate feasibility, they are fragmented across forks and student branches, are inconsistently tested, and lack reproducible benchmarking.

This project aims to consolidate and strengthen Clad’s GPU infrastructure. The focus is on upstreaming existing work, improving correctness and consistency of CUDA and Thrust support, and integrating Clad with realistic GPU-intensive codebases. A key goal is to establish reliable benchmarks and CI coverage: if current results are already good, they should be documented and validated; if not, the implementation should be optimized further so that Clad is a practical AD solution for real-world GPU applications.

## Expected Results

* Recover, reproduce, and upstream past Clad+GPU work, including prior student projects and LLM training prototypes.
* Integrate Clad with representative GPU applications such as XSBench, LULESH, and the in-tree tiny raytracer, ensuring * correct end-to-end differentiation.
* Establish reproducible benchmarks for these codebases and compare results with other AD tools (e.g. Enzyme) where feasible.
* Reduce reliance on atomic operations, improve accumulation strategies, and add support for additional GPU primitives and CUDA/Thrust features.
* Add unit and integration tests and enable GPU-aware CI to catch correctness and performance regressions.
* Improve user-facing documentation and examples for CUDA and Thrust usage.
* Present intermediate and final results at relevant project meetings and conferences.

## Requirements

* Automatic differentiation
* Parallel/GPU programming
* Reasonable expertise in C++ programming

## Links
* [Repo](https://github.com/vgvassilev/clad)

## AI Policy

AI assistance is allowed for this contribution. The applicant takes full responsibility for all code and results, disclosing AI use for non-routine tasks (algorithm design, architecture, complex problem-solving). Routine tasks (grammar, formatting, style) do not require disclosure.

## How to Apply

In addition to reaching out to the mentors by email, prospective candidates are required to complete [this form](https://forms.gle/AYgrJthYCRmBwwFL8)
