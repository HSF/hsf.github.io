---
title: Optimisation of GeantV HPC workload balancing by use of unsupervised machine learning
layout: plain
project: GeantV
organization: CERN
---

## Description

GeantV is a project aiming to deploy massively parallel detector simulation workloads from workstations to distributed computing resources, including HPC clusters. The GeantV concurrency model exploits optimally a single node using threads and features such as vectorization and machine topology discovery. We are developing a model to adapt GeantV to make efficient use also of HPC resources, minimizing the processing tails due to the inhomogeneity of distributed environments. The goal of the summer project is to test and optimize the HPC deployment model, using the idea of optimized job scheduling  based on evolutionary tuning of GeantV job parameters and spectral clustering of HPC resources in optimal subregions based on a graph representation of them.

## Task ideas
 * Implement multi-tier master-worker communication layer using MPI or alternative communication protocol (ZeroMQ or others).
 * Design and implement multi-layer graph workflow[2] for HPC layer, integrate spectral clustering in job processing schema.
 * Deploy and test the code on a cluster, adding evolutionary tuning module and deploy spectral clustering. 

## Expected deliverables
Deployment of GeantV in a cluster, demonstrating improvement in workload balancing compared to naive workload deployment.
Optimization based on ML techniques demonstrating improvements with respect to the initial heuristic-based implementation.

## Desired programming experience
C/C++

## Desired knowledge
HPC, linear algebra, machine learning algorithms

## Mentors 
  * [Andrei Gheata](mailto:andrei.gheata@cern.ch)
  * [Oksana Shadura](mailto:oksana.shadura@cern.ch)
  
## Links
  * [Geant](http://geant.web.cern.ch)
