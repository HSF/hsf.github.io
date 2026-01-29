---
title: Expanding User-Facing High-Energy Physics Spack Packages
layout: gsoc_proposal
project: Spack
year: 2026
organization:
  - umanitoba
difficulty: medium
duration: 175
mentor_avail: June-October
project_mentors:
  - email: wouter.deconinck@umanitoba.ca
    first_name: Wouter
    last_name: Deconinck
    organization: umanitoba
    is_preferred_contact: yes
---

## Description

Spack is a flexible package manager widely used in high-performance computing (HPC) to manage complex software stacks. It is commonly used in scientific computing environments, including particle physics research. For example, the key4HEP project uses Spack to manage complex software dependencies for high-energy physics (HEP) applications.

The key4HEP project has for several years maintained and curated an extensive selection of high-energy physics software packages in Spack, through the third-party `key4hep-spack` package repository. This selection of packages has formed the basis of large deployments of the key4HEP software stack on CVMFS.

However, changing directions for the deployment strategy of the key4HEP stack are affecting the sustainability of central support for the package collection. The package collection will therefore benefit from transitioning to an end-user community-support model by upstreaming the package recipes into the main Spack repository. This transition process is expected to play out over the course of several months, during the GSoC period.

## Task Ideas

- Enumerate and categorize the existing key4HEP Spack packages by usage and maintenance status (latest release, actively maintained, breadth of user-base, etc.)
- Identify discrepancies between key4HEP packaging practices and current Spack best practices
- Rank the list of packages to be upstreamed based on the previous analyses
- Upstream the highest priority packages into Spack, following Spack best practices
- Integrate new packages into Spack's continuous integration and testing infrastructure (HEP stack)

As a stretch goal, in case of rapid progress, we may consider as a next step the expansion of the continuous integration and testing infrastructure to include MacOS as a target platform for the HEP stack. This would allow Spack users on MacOS to more confidently rely on the functionality of high-energy physics packages.

## Expected Results and Milestones

- Familiarization with Spack's packaging and contribution processes
- Summarization of current package recipes in the key4HEP Spack repository
- Identification of plan of work for upstreaming packages
- Upstreaming of individual (or cohesive groups of) packages in multiple pull requests
- Testing and validation of the upstreamed packages

## Requirements

- Python programming skills
- Packaging and build system knowledge
- Some experience with continuous integration on GitLab
- Interest in scientific software stacks and high-energy physics

## AI Policy

AI assistance is allowed for this contribution. The applicant takes full responsibility for all code and results, disclosing AI use for non-routine tasks (algorithm design, architecture, complex problem-solving). Routine tasks (grammar, formatting, style) do not require disclosure.

## How to Apply

Email mentors with a brief background and interest in scientific software stacks and high-energy physics. Please include "gsoc26" in the subject line. Mentors will provide an evaluation task after submission.

## Resources

- [Spack](https://spack.io/)
