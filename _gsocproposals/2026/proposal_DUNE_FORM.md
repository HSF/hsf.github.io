---
title: Fine grained storage for the DUNE experiment
layout: gsoc_proposal
project: ATLAS
year: 2026
organization:
  - ANL
  - CERN
  - FNAL
difficulty: medium
duration: 175
mentor_avail: June-October
project_mentors:
  - email: wanwei.wu@anl.gov
    first_name: Wanwei
    last_name: Wu
    organization: ANL
    is_preferred_contact: yes
  - email: gemmeren@anl.gov
    first_name: Peter
    last_name: van Gemmeren
    organization: ANL
    is_preferred_contact: yes
---

## Description

Physics discoveries over the past decades have put neutrinos, an only weakly interacting almost massless particle, at the center of fundamental questions about the nature of matter and the evolution of the universe. The Deep Underground Neutrino Experiment (DUNE) is a leading-edge, international experiment for neutrino science to study these questions. DUNE will consist of two neutrino detectors placed in the world’s most intense neutrino beam at Fermilab in Batavia, Illinois and far away at the Sanford Underground Research Laboratory in Lead, South Dakota.
To support large data record sizes, the experiment is developing a new data processing framework with novel, fine grained data storage infrastructure. The I/O system will support eager writing of sub-records into individual containers without need for synchronization that could produce bottlenecks or require substantial system resources (such as memory). When reading data clients may have to access multiple different sub-records simultaneously and synchronization has to be provided on read.

## Task Ideas

- Study fine grained data placement in independent container
- Benchmark reading on non-synchronized containers, depending on different storage scenarios.
- Quantify performance and identify potential inefficiency
- Develop strategies, such as caching, to minimize inefficiencies.

## Expected Results and Milestones

- Familiarization with DUNE, Phlex framework and FORM I/O infrastructure
- Study fine grained data placement in independent container
- Benchmark reading on non-synchronized containers, depending on different storage scenarios.
- Quantify performance and identify potential inefficiency
- Develop strategies, such as caching, to minimize inefficiencies.

## Requirements

- Python programming skills
- Some C++ familiarity
- Analysis of test data
- Interest in scientific software optimization

## AI Policy

AI assistance is allowed for this contribution. The applicant takes full responsibility for all code and results, disclosing AI use for non-routine tasks (algorithm design, architecture, complex problem-solving). Routine tasks (grammar, formatting, style) do not require disclosure.

## How to Apply

Email mentors with a brief background and interest in Computing/particle physics. Please include "gsoc26" in the subject line. Mentors will provide an evaluation task after submission.

## Resources

- [DUNE Experiment](https://www.dunescience.org/)
- [DUNE Framework R&D](https://github.com/Framework-R-D)
