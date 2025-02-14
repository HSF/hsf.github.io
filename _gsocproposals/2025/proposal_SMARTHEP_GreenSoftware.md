---
title: Estimating the energy cost of ML scientific software
layout: gsoc_proposal
project: SMARTHEP
year: 2025
organization:
  - UManchester
  - CERN
difficulty: medium
duration: 350
mentor_avail: June-October (with 2-3 weeks mentor vacation where student will work independently with minimal guidance)
project_mentors:
  - email: caterina.doglioni@cern.ch
    organization: CERN
    first_name: Caterina
    last_name: Doglioni
  - email: tobias.fitschen@cern.ch
    organization: CERN
    role: Backup Mentor
    first_name: Tobias
    last_name: Fitschen
  - email: james.smith-7@manchester.ac.uk
    organization: University of Manchester
    role: Backup Mentor
    first_name: James
    last_name: Smith
---
# Description

At a time where “energy crisis” is something that we hear daily,
we can’t help but wonder whether our research software can be made more sustainable,
and more efficient as a byproduct.
In particular, this question arises for ML scientific software used in high-throughput scientific
computing, where large datasets composed of many similar chunks are analysed with similar operations
on each chunk of data.
Moreover, CPU/GPU-efficient software algorithms are crucial for the real-time data selection (trigger)
systems in LHC experiments,
as the initial data analysis necessary to select interesting collision events
is executed on a computing farm located at CERN that has finite CPU resources.

The questions we want to start answering in this work are:
   * what is the trade off between performance of a ML algorithm and its energetic efficiency?
   * can small efficiency improvements in ML algorithms running on Large Hadron Collider data
   have a sizable energetic impact?
   * how do these energy efficiency improvements vary
   when using different computing architectures (1) and/or job submission systems (2)?

## Task ideas

The students in this project will use metrics from the [Green Software Foundation](<https://greensoftware.foundation>)
and from other selected resources to estimate the energy efficiency of machine learning software from LHC experiments 
(namely, top tagging using ATLAS Open data) and from machine learning algorithms for data compression
(there is another GSoC project developing this code, called Baler).
This work will build on previous GSoC / Master's thesis work, and will expand these results for GPU architectures. 
If time allows, the student will then have the chance to make small changes to the code
to make it more efficient, and evaluate possible savings.

## Expected results and milestones

 * Understand and summarise the metrics for software energy consumption, focusing on computing resources at CERN;
 * Become familiar with running and debugging the selected software frameworks and algorithms;
 * Set up tests and visualisation for applying metrics to the selected software
 * Run tests and visualise results (preferably using a Jupyter notebook)
 * Vary platforms and job submission systems
 * Identify possible improvements, apply them, and run tests again

## Requirements

 * Python
 * git
 * Jupyter notebooks
 * PyTorch or equivalent ML toolkit 
 * Desirable: code profiling experience

## Links

 * (1) [Green Software Foundation course](<https://learn.greensoftware.foundation/>)
 * (2) [Code by the previous GSoC student](<https://summerofcode.withgoogle.com/archive/2023/projects/Nks9akq7>) 
