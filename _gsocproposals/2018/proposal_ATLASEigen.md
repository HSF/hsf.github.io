---
title:  Faster matrix algebra for ATLAS
layout: gsoc_proposal
project: ATLAS
year: 2018
organization:
  - RAL
---

## Introduction

In an environment like the Large Hadron Collider, we have millions of collisions per second, each producing thousands of particles passing through our detectors. Particle physics experiments like ATLAS rely on thousands of computers using clever algorithms to identify different types of particles and find interesting collisions, such as the production of Higgs bosons or even new particles. The optimisation of these algorithms can dramatically improve the physics we are sensitive to. ATLAS pattern recognition makes heavy use of matrix algebra, implemented with the Eigen library. 
 
## Task 

Eigen is a fast, robust, open source linear algebra library, used by e.g. the Google Tensorflow and Large Survey Synoptic Telescope projects as well as ATLAS. Most algorithms in ATLAS software use symmetric matrices, which are unfortunately missing from Eigen. This would make our calculations more efficient: since the upper and lower triangular parts of the matrix are the same, only the upper/lower half of the matrix needs to be stored or used in operations.

Your task will be to implement an efficient symmetric matrix class storing only the needed parts. This will help ATLAS find particles while using less computing power and less storage space.

## Expected results

A working implementation of symmetric matrices in Eigen, ready to be submitted as a patch for Eigen 

## Requirements

- C++
- python
- basic linear algebra

## Mentors

 * [Stewart Martin-Haugh](mailto:stewart.martin-haugh@stfc.ac.uk)
 * [Dmitry Emeliyanov](mailto:dmitry.emeliyanov@stfc.ac.uk)
