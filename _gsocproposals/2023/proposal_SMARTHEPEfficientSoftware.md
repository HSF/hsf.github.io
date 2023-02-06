---
title: Estimating the energy cost of scientific software
layout: gsoc_proposal
project: SMARTHEP
year: 2023
organization:
  - UofManchester
  - CERN
difficulty: medium
duration: 350
mentor_avail: June-October (with 2-3 weeks mentor vacation where student will work independently with minimal guidance)
---
# Description

At a time where “energy crisis” is something that we hear daily,
we can’t help but wonder whether our research software can be made more sustainable,
and more efficient as a byproduct.
In particular, this question arises for scientific software used in high-throughput scientific
computing, where large datasets composed of many similar chunks are analysed with similar operations
on each chunk of data.
Moreover, efficient software algorithms are crucial for the real-time data selection (trigger)
systems in LHC experiments,
as the initial data analysis necessary to select interesting collision events
is executed on a computing farm located at CERN that has finite CPU resources.

The questions we want to start answering in this work are:
   * can small efficiency improvements in the software of Large Hadron Collider experiments
   have a large energetic impact, given that datasets are composed by billions of proton-proton
collisions that are reconstructed or analysed independently?
   * how do these energy efficiency improvements vary
   when using different computing architectures (1) and/or job submission systems (2)?

## Task ideas

The students in this project will use metrics from the [Green Software Foundation](<https://greensoftware.foundation>)
and from other selected resources to estimate the energy efficiency of software from LHC experiments
and from selected machine learning algorithms for data compression
(there is another GSoC project developing this code).
The students will then have the chance to make small changes to the code
to make it more efficient, and evaluate possible savings.
If time allows, the student will also test on different job submission systems
and computing architectures.

## Expected results and milestones

 * Understand and summarise the metrics for software energy consumption, focusing on computing resources at CERN;
 * Become familiar with running and debugging the selected software frameworks and algorithms;
 * Set up tests and visualisation for applying metrics to the selected software
 * Run tests and visualise results (preferably using a Jupyter notebook)
 * Identify possible improvements, apply them, and run tests again
 * Vary platforms and job submission systems

## Requirements

 * C++
 * Python
 * git
 * Jupyter notebooks

## Mentors

 * **[Caterina Doglioni](mailto:caterina.doglioni@cern.ch)**

## Links

 * (1) [Green Software Foundation course](<https://learn.greensoftware.foundation/hardware-efficiency>)
 * (2) [the CERN Green Big Data project Twiki](<https://twiki.cern.ch/twiki/bin/view/Main/GreenBigData>)
