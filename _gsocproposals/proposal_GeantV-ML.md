---
title: Optimisation of GeantV HPC workload balancing by use of unsupervised machine learning
layout: gsoc_proposal
project: GeantV
organization: 
  - CERN
  - NTUUKPI
---

## Description

GeantV is a project aiming to deploy massively parallel detector simulation workloads from workstations to distributed computing resources, including HPC clusters. The GeantV concurrency model[1] exploits optimally a single node using threads and features such as vectorization and machine topology discovery. We are developing a model to adapt GeantV to make efficient use also of HPC resources, minimizing the processing tails due to the inhomogeneity of distributed environments. The goal of the summer project is to test and optimize the HPC deployment model, using the idea of optimized job scheduling  based on evolutionary tuning of GeantV job parameters and spectral clustering[3] of HPC resources in optimal subregions based on a graph representation of them.

## Task ideas
 * Implement multi-tier master-worker communication layer using MPI or alternative communication protocol (ZeroMQ or others).
 * Design and implement multi-layer graph workflow[2] for HPC layer, integrate spectral clustering[3] in job processing schema.
 * Deploy and test the code on a cluster, adding evolutionary tuning module and deploy spectral clustering[4]. 

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

## References

  1. Apostolakis, J and Bandieramonte, M and Bitzes, G and Brun, R and Canal, P and Carminati, F and Licht, JC De Fine and Duhem, L and Elvira, VD and Gheata, A and others, Adaptive track scheduling to optimize concurrency and vectorization in GeantV, Journal of Physics: Conference Series, 608, 1, 012003, 2015, IOP Publishing
  2. Mikko Kivelä, Alex Arenas, Marc Barthelemy, James P. Gleeson, Yamir Moreno, Mason A. Porter; Multilayer networks. J Complex Netw 2014; 2 (3): 203-271. [doi: 10.1093/comnet/cnu016](https://doi.org/10.1093/comnet/cnu016)
  3. Andrew Y. Ng, Michael I. Jordan, and Yair Weiss. 2001. On spectral clustering: analysis and an algorithm. In Proceedings of the 14th International Conference on Neural Information Processing Systems: Natural and Synthetic (NIPS'01), T. G. Dietterich, S. Becker, and Z. Ghahramani (Eds.). MIT Press, Cambridge, MA, USA, 849-856. 
  4. Xiaowen Dong and Pascal Frossard and Pierre Vandergheynst and Nikolai Nefedov, Clustering with Multi-Layer Graphs: A Spectral Perspective, CoRR, abs/1106.2233, 2011, [https://arxiv.org/abs/1106.2233](http://arxiv.org/abs/1106.2233)
