-
title: Negative weight mitigation with cell resampling and tests with MCFM
layout: gsoc_proposal
project: Negative weight, MCFM
year: 2026
organization: Southern Methodist University
difficulty: medium
duration: 175
mentor_avail: June-October
project_mentors: Tobias Neumann (tneumann@mail.smu.edu), Saptaparna Bhattacharya (saptaparnab@smu.edu) 
---

## Description

MCFM (Monte Carlo for FeMtobarn processes) is a widely used software package in high-energy physics. It simulates particle collisions, such as those at the Large Hadron Collider (LHC), allowing physicists to compare theoretical predictions with experimental data. It specializes in high-precision predictions Next-to-Next-to-Leading Order and beyond) for a vast array of particle processes.

When physicists calculate predictions for these collisions using higher-order quantum field theory, the mathematics often requires "subtraction schemes" to handle infinities. A side effect of this is that some simulated events are assigned a "negative weight" (effectively a negative probability).

While these negative weights make sense mathematically—they cancel out other positive events to give the correct physical result—they are computationally very expensive. In downstream processing (like simulating how a particle detector responds), a negative event and a positive event must both be fully simulated only to cancel each other out later. This "statistical dilution" means we have to generate and store significantly more data just to achieve a standard level of precision.

A new method called "Cell Resampling" (proposed in [arXiv:2109.07851](https://arxiv.org/abs/2109.07851) and [arXiv:2303.15246](https://arxiv.org/abs/2303.15246)) offers a way to fix this by redistributing these negative weights locally in phase space, effectively removing them without changing the physical prediction.

We plan to implement this method within MCFM. This project is a collaboration between theorists and experimentalists to:
1. Prove the method works within a major parton-level Monte Carlo generator (MCFM).
2. Stress-test the method to ensure it is robust enough for use in large-scale experimental workflows.

Once successful, this work will result in a public release of MCFM featuring this efficiency upgrade.

## Task ideas
* Gain a working understanding of the MCFM codebase and how it handles event generation.
* Implement the cell resampling algorithm on "fake" data (pseudorandom distributions that mimic typical particle physics events) to understand the logic in a controlled environment.
* Integrate the cell resampling method directly into the MCFM source code.
* Run the modified MCFM, compare the results against the standard version to ensure physics accuracy, and document the performance gains.

## Expected results
Release a modified version of MCFM that successfully incorporates the negative weight mitigation strategy, demonstrating reduced statistical dilution.

## Requirements
* Experience with Fortran (as MCFM is largely written in Fortran) OR a strong willingness to learn it.
* Basic familiarity with C++ (useful for the resampling algorithm integration).
* Interest in numerical methods and efficiency optimization.
