---
title: Generative-AI Assisted Testing of Complex Stacks of Spack Packages
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

Spack is a flexible package manager widely used in high-performance computing (HPC) to manage complex software stacks. It is commonly used in scientific computing environments, including particle physics research. In high-energy physics (HEP), for example, Spack is used to manage complex software dependencies for the extensive stacks in HEP environments.

In contrast to traditional package managers, Spack is designed to support multiple versions with multiple variants at the same time. This allows for the necessary flexibility in HEP environments where for reasons of reproducibility and stability we may want to keep some dependencies at older versions while upgrading other dependencies to newer versions. However, this flexibility comes at the cost of increased complexity in testing the Spack packages, where the focus of testing is typically on the leading-edge configurations: the newest versions with the newest dependencies. This can lead to subtle and invisible breakages in configurations where older packages are combined with newer packages in user-defined configurations.

Based on recent advances in generative AI, it would appear to be feasible to compose specific test scenarios (away from the leading-edge of package versions already tested in CI) that are most likely to uncover breakages in Spack packages. For example, if a package has no upper limits on its dependency versions but other packages do typically have upper limits, then this may indicate that also here upper limits should be added.

This project will explore how generative AI can be used to assist in the identification and creation of such test scenarios for complex stacks of Spack packages, while at the same time developing a methodology to validate the effectiveness of the generated tests and reduce the probability of running large numbers of ineffective tests or repeated tests.

## Task Ideas

- Develop a scalable method to summarize information from multiple Spack packages for input into generative AI models
- Develop a method to record and propagate past successfull test scenarios to avoid generating duplicate tests
- Develop a strategy to schedule and run generated test scenarios in an efficient manner
- Develop a methodology to validate the effectiveness of generated test scenarios in uncovering breakages
- Integrate the automatic test scenarios into Spack's existing continuous integration and testing infrastructure

## Expected Results and Milestones

- Familiarization with Spack's packaging practices and testing infrastructure
- Analyze classes of common off-leading-edge configurations that may lead to breakages
- Summarization of potential strategies for generative-AI assisted test generation
- Design of a solution for generative-AI assisted test generation
- Test the design in the context of Spack packages
- Documentation and integration into Spack

## Requirements

- Python programming skills
- Generative AI knowledge and experience
- Packaging and build system knowledge
- Interest in scientific software stacks

## AI Policy

AI assistance is allowed for this contribution. The applicant takes full responsibility for all code and results, disclosing AI use for non-routine tasks (algorithm design, architecture, complex problem-solving). Routine tasks (grammar, formatting, style) do not require disclosure.

## How to Apply

Email mentors with a brief background and interest in scientific software stacks and high-energy physics. Please include "gsoc26" in the subject line. Mentors will provide an evaluation task after submission.

## Resources

- [Spack](https://spack.io/)
