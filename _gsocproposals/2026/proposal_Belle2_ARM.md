---
title: Enabling Sustainable ARM Support for the Belle II Software
layout: gsoc_proposal
project: Belle2
year: 2026
organization:
  - LMU
  - KIT
difficulty: medium
duration: 350
mentor_avail: May-October
project_mentors:
  - email: giacomo.pietro@kit.edu
    first_name: Giacomo
    last_name: De Pietro
    organization: KIT
    is_preferred_contact: yes
  - email: Thomas.Kuhr@lmu.de
    first_name: Thomas
    last_name: Kuhr
    organization: LMU
  - email: vidya.vobbilisetti@pi.infn.it
    first_name: Vidya Sagar
    last_name: Vobbilisetti
    organization: CPPM
---

## Description

Belle II is a particle physics experiment at KEK in Tsukuba, Japan, which is designed to study rare processes and probe physics beyond the Standard Model. Its software framework, Belle II Analysis Software Framework (basf2), comprises a large and complex codebase with extensive dependencies on external libraries, and currently supports only on the x86 architecture.

With the increasing availability of ARM-based computing resources, including HPC systems and energy-efficient data centers, enabling ARM support for basf2 is a crucial step towards ensuring the long-term viability of Belle II computing. The aim of this project is to design and implement a sustainable, maintainable system for building basf2 and its external dependencies for ARM without introducing excessive code duplication or fragile, ad hoc solutions.

Instead of performing a single experimental port, the goal is to create a reproducible, architecture-aware build system that supports both x86 and ARM targets in a unified way, ideally allowing users to easily build the full software stack.

The project will explore alternatives to the current monolithic Makefile-based approach to managing dependencies, including modern package managers such as Spack, and evaluate how these can be integrated into the existing Belle II build and deployment ecosystem comprising (Buildbot, GitLab, CVMFS).

## Task Ideas

* Study the existing basf2 externals build infrastructure with a focus on architecture-dependent components
* Propose a sustainable, multi-architecture solution for managing and building basf2 externals (x86 and ARM)
* Investigate and experiment with modern dependency and package management tools (e.g. Spack)
* Compile and validate basf2 and its externals on ARM using the new build system

## Expected Results and Milestones

* Evaluation and prototypes of modern dependency/package management approaches (e.g. Spack)
* A maintainable build strategy for basf2 externals supporting multiple architectures (x86 and ARM) with minimal code duplication
* A unified build workflow that successfully builds basf2 on ARM and x86 systems
* Functional tests that verify performance and stability of basf2 on ARM
* Documentation of the build system, workflows, and guidelines for adding and updating packages

## Requirements

* Familiarity with Linux development environments
* Experience with C++ and build systems (Make, CMake, or similar)
* Basic understanding of software portability and architectures
* Experience with package managers (e.g. Spack) is a plus

## AI Policy

AI assistance is allowed for this contribution. The applicant takes full responsibility for all code and results, disclosing AI use for non-routine tasks (algorithm design, architecture, complex problem-solving). Routine tasks (grammar, formatting, style) do not require disclosure.

## How to Apply

Email mentors with a brief background and interest in computing and/or particle physics. Please include “gsoc26” in the subject line. Mentors will provide an evaluation task after submission.

## Useful Links

* [Belle II experiment](https://www.belle2.org/)
* [basf2 code repository](https://github.com/belle2/basf2)
* [basf2 externals code repository](https://github.com/belle2/externals)
* [Belle II software documentation](https://software.belle2.org/development/sphinx/index.html)
* [Spack](https://spack.io/)
