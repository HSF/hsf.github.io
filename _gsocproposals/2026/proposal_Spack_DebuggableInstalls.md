---
title: Debuggable Installations for Spack Packages
layout: gsoc_proposal
project: Spack
year: 2026
organization:
  - UM
difficulty: medium
duration: 175
mentor_avail: June-October
project_mentors:
  - email: wouter.deconinck@umanitoba.ca
    first_name: Wouter
    last_name: Deconinck
    organization: UM
    is_preferred_contact: yes
---

## Description

Spack is a flexible package manager widely used in high-performance computing (HPC) to manage complex software stacks. It is commonly used in scientific computing environments, including particle physics research. For example, the key4HEP project uses Spack to manage software dependencies for high-energy physics applications.

Spack builds packages from scratch in a staging directory, which is then installed into a Spack-managed prefix. However, this approach can make debugging installation issues challenging, as the build artifacts are not easily accessible after installation. Symbols in the installed binaries may not correspond to the original source files, complicating debugging efforts.

There are some workarounds to ensuring debuggable installs in Spack, such as using `spack dev-build` or `spack develop`, but these methods have limitations and do not fully address the issue in a streamlined manner. This project will focus on ensuring that the source trees used for compilation can be installed in the prefix alongside the built binaries, allowing for easier debugging and symbol resolution. This project will have to ensure that temporary build products are still cleaned up properly to avoid bloating the installation prefix.

## Task Ideas

- Assess the limitations of the current approaches for installing source trees alongside built binaries in Spack
- Develop a robust solution to enable debuggable installs for Spack packages with out-of-source-tree build systems
- Test the implementation with a variety of packages and build systems, with a focus on high-energy physics software

As a stretch goal, in case of rapid progress, we may consider a next step which involves installing debug symbols in a separate location for access with `debuginfod`. This would allow installed binaries to be stripped of debug symbols, reducing their size and increasing performance, while still providing access to the symbols when needed for debugging.

## Expected Results and Milestones

- Familiarization with Spack's build and install processes
- Summarization of current limitations and potential solutions
- Design of a solution for debuggable installs
- Analyze design for anticipated challenges
- Implementation of the solution
- Testing and validation with various packages
- Documentation and integration into Spack

## Requirements

- Python programming skills
- Packaging and build system knowledge (in particular CMake)
- Interest in scientific software stacks and high-energy physics

## AI Policy

AI assistance is allowed for this contribution. The applicant takes full responsibility for all code and results, disclosing AI use for non-routine tasks (algorithm design, architecture, complex problem-solving). Routine tasks (grammar, formatting, style) do not require disclosure.

## How to Apply

Email mentors with a brief background and interest in scientific software stacks and high-energy physics. Please include "gsoc26" in the subject line. Mentors will provide an evaluation task after submission.

## Resources

- [Spack](https://spack.io/)
