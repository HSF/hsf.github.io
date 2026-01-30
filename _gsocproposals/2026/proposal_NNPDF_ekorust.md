---
title: The EKO oxidation
layout: gsoc_proposal
project: NNPDF
year: 2026
organization:
  - UofSevilla
  - UofJyvaskyla
difficulty: medium
duration: 175
mentor_avail: June-September
project_mentors:
  - email: jcruz@us.es
    first_name: Juan M.
    last_name: Cruz Martinez
    organization: UofSevilla
  - email: felix.a.hekhorn@jyu.fi
    first_name: Felx
    last_name: Hekhorn
    organization: UofJyvaskyla
    is_preferred_contact: yes
---

# Description

EKO (Evolution Kernel Operators) is a software library, part of the NNPDF ecosytem, that solves the DGLAP equations in Mellin space to produce evolution kernel operators.
Uniquely, EKO is independent of the Parton Distribution Function (PDF), operators can be precomputed for a specific theoretical configuration (e.g., NLO, NNLO, QED) and stored.
This allows for extremely fast repeated evaluations during parameter fitting (e.g., during the extraction of PDFs), as the operators can simply be applied to varying initial conditions without re-solving the differential equations.

## Task idea

Originally, EKO was implemented entirely in Python.
While Python offers excellent readability, and a rich ecosystem, and JIT compilers such as numba it presents performance bottlenecks which are becoming harder to overcome.
The DGLAP evolution equations involve complex numerical integration and heavy matrix operations.
As EKO is extended to include higher orders extend EKO and QED effects, the computational cost grows dramatically.

As a result, we have started a process of "oxidizing" EKO.
This means rewriting the performance-critical DGLAP kernel in Rust.
Thanks to tools like PyO3 and Maturin, we can expose these Rust binaries as native Python modules which allows us to keep the user-friendly Python API while offloading the heavy lifting to a highly optimized Rust backend.

The goal of this project is to take this initial Rust port and mature it into a production-ready library.
The focus is on the automatization of the packaging and distribution process, benchmarking the library against the legacy python version (accuracy is our most important trait!) and having a robust interface to not only python, but also C++ or Fortran, ubiquitous in particle physics.

## Expected results and milestones

 * Familiarization with the rust/cargo toolchain 
 * Familiarization with the PyO3 toolchain 
 * Testing EKO's rust interface with different languages: C++, Fortran, Python
 * Benchmarking the rust and python implementation
 * Automatization of the EKO crate

## Requirements

 * Familiarity with UNIX/Linux, Rust, python
 * Familiarity with CI workflows


## How to apply

Once we are accepted as a GSoC org, please write an email with a short introduction to your interests and background to the mentors with the string "gsoc26" in the subject.
There will be a small evaluation task that we will mail to you then.


## Links

 * [EKO](https://eko.readthedocs.io/en/latest/)
