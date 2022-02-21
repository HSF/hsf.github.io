---
title: Electromagnetic Cluster Finding on GPUs
layout: gsoc_proposal
project: ATHENA
year: 2022
difficulty: high
duration: 350
mentor_avail: May-September
organization:
  - ANL
  - EIC
  - UManitoba
---
## Description
The ATHENA collaboration at the Electron-Ion Collider (EIC) is planning to build
a novel electromagnetic calorimeter (ECAL) that combines AstroPix silicon pixel
detector imaging layers with plastic scintillating fibers embedded in lead and
read out at the ends. Due to the increase in segmentation that is associated with
the 500-um pitch pixel detectors, the computational demands on finding clusters
of hits caused by a single particle shower are much larger than for traditional
electromagnetic calorimeters. For typical events that we expect to encounter at
the EIC, we expect to spend the majority of computing time on this cluster
reconstruction if we use traditional algorithms. Since the EIC experiments will
use streaming readout, this corresponds to a bottleneck on the data rates that we
will be able to sustain.

In this project we aim to parallelize the clustering algorithm to run efficiently
on GPUs, and separate the clustering algorithms into a separate library with an
interface based on the standardized EDM4hep data model. We aim to focus from the 
start on the SYCL cross-platform abstraction layer, mirroring an approach which 
is already used by other components of our event reconstruction environment.

## Task Ideas
This project will involve the re-implementation or modification of the current
electromagnetic imaging and scintillating fiber calorimeter clustering algorithms
using SYCL.

## Milestones
 * Gain an understanding of the current clustering algorithm by using well-chosen
   benchmark data sets provided by the mentors.
 * Identify the algorithm components that are most likely to benefit from GPU
   acceleration.
 * Develop a plan for the implementation of the identified algroithm componetns
   in SYCL.
 * Convert a first algorithm component, and test the achieved performance gain
   on a single target architecture.
 * Convert all identified algorithm components, and test the performance gain
   on a single target architecture.
 * Compare the performance gain on various accelerated hardware systems.

## Expected Results
The expected result is a working implementation of a GPU-accelerated clustering
algorithm for the electromagnetic calorimenter in the Gaudi-based reconstruction
environment of the ATHENA collaboration, along with an summary of accuracy and
performance on several hardware configurations for which access will be provided
by the hosts.

The student should be prepared to write a progress report and present the results
at the end of the project period.

## Technology:
 * C/C++, template programming, GPU programming.

## Desirable Skills
 * Necessary knowledge: C or C++ programming; data structures and algorithms.
 * Experience with GPU programming would be an asset.

## What You Will Learn
 * Real-world experience with SYCL, a cross-platform higher-level programming
   model for various hardware accelerators.
 * Expertise with operation of clustering algorithms on multi-dimensional data
   sets in a production environment.

## Evaluation Task
Interested students should contact the mentors for a warm-up and evaluation task.

## Mentors
 * **[Wouter Deconinck](mailto:wouter.deconinck@umanitoba.ca)** (University of Manitoba)
 * [Sylvester Joosten](mailto:sjoosten@anl.gov) (Argonne National Lab)

## Links
 * [SYCL](https://www.khronos.org/sycl/)
 * [hipSYCL](https://github.com/illuhad/hipSYCL)
 * [ATHENA Collaboration](https://athena-eic.org)
 * [Juggler](https://eicweb.phy.anl.gov/EIC/juggler)
