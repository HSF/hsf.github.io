---
title: Enhancing a Next-Generation Platform for Computational Cancer Biology
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

CartopiaX is an emerging simulation and modeling platform designed to support computational cancer research through large-scale, agent-based biological simulations. The project builds on modern high-performance scientific computing practices and leverages technologies inspired by platforms such as BioDynaMo to model tumor growth, tissue microenvironments, cell-cell interactions, and diffusion of signaling molecules.

CartopiaX aims to provide a flexible research environment that enables computational scientists and domain biologists to collaboratively design, execute, and analyze large-scale biological simulations. The platform combines high-performance C++ simulation kernels with user-friendly interfaces and scripting capabilities to enable rapid experimentation and reproducible research workflows. Currently, CartopiaX provides a performant core simulation engine but still requires improvements in usability, extensibility, and performance portability to support wider adoption in computational oncology and systems biology communities.

This project invites contributors to explore improvements that help integrate, extend, and deploy CartopiaX for real-world research applications. Students are encouraged to propose approaches that enhance developer productivity, accessibility for domain scientists, and computational performance.

## Possible Directions

* Easy integration - a possible direction focuses on improving the usability of CartopiaX by developing more intuitive ways for researchers to configure and run simulations. Currently, simulations rely heavily on static configuration files and parameter definitions. Students may explore designing graphical or web-based interfaces that allow researchers to interactively define experiments, create structured configuration systems using formats such as YAML or JSON, and develop reusable experiment templates. This direction aims to make CartopiaX more accessible to domain scientists who may not have extensive programming experience while improving reproducibility and workflow management.

* Flexibility: A potential direction involves extending CartopiaX through Python integration to support flexible and rapid scientific experimentation. Many researchers in computational biology prefer Python due to its strong ecosystem for data analysis and prototyping. Students may investigate technologies such as cppyy to enable seamless interaction between the high-performance C++ simulation core and Python. This could allow scientists to define cell behaviors, simulation rules, or analysis pipelines directly in Python while preserving the performance advantages of the C++ backend. This area provides opportunities to work on language interoperability and mixed-language scientific workflows.

* HPC: a third direction explores improving the performance and scalability of CartopiaX by identifying and optimizing computational bottlenecks within the simulation engine. Agent-based biological simulations frequently involve expensive processes such as diffusion modeling and large-scale cell interaction calculations. Students may explore profiling the simulation engine, investigating GPU acceleration strategies for diffusion solvers or other parallelizable components, and developing benchmarking tools to evaluate performance improvements. This direction is particularly suited for students interested in high-performance computing and parallel programming techniques.

## Requirements

* Requirements may vary based on the direction of the project, and can range from graphical or web-based interface design, Python/C++ programming, and/or familiarity with parallel programming and simulation/modelling 

## Links
* [Repo](https://github.com/compiler-research/CARTopiaX)

## AI Policy

AI assistance is allowed for this contribution. The applicant takes full responsibility for all code and results, disclosing AI use for non-routine tasks (algorithm design, architecture, complex problem-solving). Routine tasks (grammar, formatting, style) do not require disclosure.

## How to Apply

In addition to reaching out to the mentors by email, prospective candidates are required to complete [this form](https://forms.gle/AYgrJthYCRmBwwFL8)
