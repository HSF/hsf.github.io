---
title: Rucio - Namespace synchronisation for shared OpenData
layout: gsoc_proposal
project: Rucio
year: 2023
difficulty: medium
duration: 350
mentor_avail: June-August
organization:
  - CERN
---

# Description

Rucio is an open-source software framework that provides scientific collaborations the functionality to organize, manage, transfer, monitor, and access their distributed data across heterogeneous infrastructures. Rucio was originally developed to meet the requirements of the high-energy physics experiment ATLAS, and now is continuously enhanced to support diverse scientific communities. Since 2016 Rucio orchestrated multiple Exabytes of data access and data transfers globally.

With this project we seek to enhance Rucio to support a new mechanism to share data across Rucio instances. Different communities and experiments that are using Rucio have the need to share data in a safe and efficient manner, however right now this would require non-atomic and client-side operations. Such operations inadvertently lead to inconsistencies across Rucio instances and must be avoided. In this project we propose a native server-side mechanism, embedded in the Rucio core, such that safe and efficient data sharing can be achieved.

## Objectives

Set up multiple typical Rucio-instances for scientific experiments:
 * Develop the necessary extensions to the development environment to easily spawn such a distributed testing environment
 * Develop a distributed data producing pipeline to feed the Rucio environments with fake data

Rucio core developments:
 * Develop cross-instance authorisation mechanism
 * Develop remote namespace query mechanism
 * Develop the namespace synchronisation mechanism
 * Develop shared upload and download mechanisms

By the end of GSoC’23 we expect that the student has developed the necessary changes in Rucio including unit tests and successfully demonstrated the above mentioned use cases.

## Evaluation task

Interested students please contact Mario and Martin directly for the evaluation, which includes setting up the Rucio development environment using the Kubernetes & Docker-based tutorial. Then, a low-difficulty development task will have to be implemented and the according pull request will have to be submitted. The pull request must pass the CI/CD pipeline.

## Requirements

 * Python
 * Linux, Git, and Kubernetes/Docker

## Mentors

 * **[Mario Lassnig](mailto:mario.lassnig@cern.ch)**
 * [Martin Barisits](mailto:martin.barisits@cern.ch)

## Links
 1. [Rucio GitHub](https://github.com/rucio/rucio)
 2. [Rucio Documentation](https://rucio.readthedocs.io/en/latest/)
 2. [Rucio system overview journal article (Springer)](https://doi.org/10.1007/s41781-019-0026-3)
 3. [Rucio operational experience article (IEEE Computer Society)](http://sites.computer.org/debull/A20mar/p9.pdf)
