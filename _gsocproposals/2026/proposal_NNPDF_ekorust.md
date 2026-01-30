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
    first_name: Felix
    last_name: Hekhorn
    organization: UofJyvaskyla
    is_preferred_contact: yes
---

# Description

High-energy particle scattering, which is for example investigated with the LHC at CERN, is a part of fundamental research and aims at understanding the matter around us, in particular protons.
The inner structure of protons can be described by Parton Distribution Functions (PDFs), which are extracted from experimental measurements and which in turn are a major ingredient into many theoretical predictions.
With the increasing precision of experimental measurements we have reached an era of high-precision physics, which brings new challenges also to the theory side.

The evaluation of PDFs is tightly linked to the so-called DGLAP equations.
Within the NNPDF ecosystem we have develop the EKO (Evolution Kernel Operators) software library to execute this job.
Uniquely, EKO is independent of the actual PDFs, i.e. the solution operators can be precomputed for a specific theoretical configuration (e.g., NLO, NNLO, or even NNNLO perturbative accuracy) and stored on disk.
This allows for extremely fast repeated evaluations during parameter fitting (e.g., during the extraction of PDFs), as the operators can simply be applied to varying initial conditions without re-solving the differential equations.
Effectively, this approach turns a complicated integro-differential set of equations into a linear algebra problem.

## Task idea

Originally, EKO was implemented entirely in Python.
While Python offers excellent readability, a rich ecosystem, and JIT compilers such as numba, it also presents performance bottlenecks which are becoming harder to overcome.
The DGLAP evolution equations involve complex numerical integration and heavy matrix operations.
As EKO is extended to include higher orders and QED effects, the computational cost grows dramatically.

As a result, we have started a process of "oxidizing" EKO.
This means rewriting the performance-critical tasks in Rust.
Thanks to tools like PyO3 and Maturin, we can expose these Rust binaries as native Python modules which allows us to keep the user-friendly Python API while offloading the heavy lifting to a highly optimized Rust backend.

The goal of this project is to take this initial Rust port and mature it into a production-ready library.
The focus is on the full integration between Python and Rust, the automatization of the packaging and distribution process, benchmarking the library against the legacy python version (accuracy is our most important trait!) and having a robust interface to not only Python, but also C++ or Fortran, ubiquitous in particle physics.

## Expected results and milestones

 * Familiarization with the Rust/cargo toolchain
 * Familiarization with the PyO3 toolchain
 * Familiarization with the numba package
 * Setup and automatization of deployment in Rust
 * Prepare for potential third-party contribution written in C++ to the framework
 * Expose and test EKO's rust interface with different languages: C++, Fortran, Python
 * Potentially improve interface to other closely related Rust libraries within the NNPDF framework
 * Potentially continue translation from Python to Rust and benchmark between the two languages

## Requirements

 * Familiarity with UNIX/Linux, Rust, Python
 * Familiarity with CI workflows
 
## AI Policy

AI assistance is allowed for this contribution.
The applicant takes full responsibility for all code and results, disclosing AI use for non-routine tasks (algorithm design, architecture, complex problem-solving).
Routine tasks (grammar, formatting, style) do not require disclosure.

## How to apply

Once we are accepted as a GSoC org, please write an email with a short introduction to your interests and background to the mentors with the string "gsoc26" in the subject.
There will be a small evaluation task that we will mail to you then.

## Links

 * [EKO](https://eko.readthedocs.io/en/latest/)
