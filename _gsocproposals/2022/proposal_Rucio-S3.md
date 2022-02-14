---
title: Rucio: S3-compatible access interface for analysis facilities
layout: gsoc_proposal
project: Rucio
year: 2022
difficulty: medium
duration: 350
mentor_avail: June-August
organization:
  - CERN
  - TUM
---

# Description

Rucio is an open-source software framework that provides functionality to scientific collaborations to organize, manage, monitor, and access their distributed data and dataflows across heterogeneous infrastructures. Rucio was originally developed to meet the requirements of the high-energy physics experiment ATLAS, and is continuously enhanced to support diverse scientific communities. Since 2016 Rucio orchestrated multiple Exabytes of data access and data transfers globally.

With this project we seek to enhance Rucio to support a new mechanism for analysis facilities, which are oriented towards object stores in order to provide a portable destination for HEP analyzers to store data products produced in their research in a portable, shareable and standardized way.

## Task ideas and expected results

As a user I want to
 * create S3-like buckets that are publicly readable by anyone within my experiment
 * be able to interact with the bucket using standard S3 clients
 * be able to get credentials from Rucio via API and CLI
 * share a file with analysis team

As a user I want to have
 * buckets writable by me and other selected members of my experiment
 * multiple buckets under my user scope (e.g., user.mlassnig.bucket1, user.mlassnig.bucket2, ...)
 * buckets under other scopes that I can write to (e.g., group.higgs.analysis123/mlfiles/mymlthing.hdf5, ...)
 * a quota in the order of 10'000 objects that I can rotate

 By the end of GSoC’22 we expect that the student has developed the necessary changes in Rucio including unit tests and successfully demonstrated the above mentioned use cases.

 As a stretch goal, performance optimisation for high throughput Exascale data management is of course very appreciated.

## Evaluation Task

Interested students please contact Mario, Martin, and Lukas directly for the evaluation.

## Requirements

 * Python
 * Linux, Git, and Docker
 * Cloud storage (AWS, GCS, MinIO, ...)

## Mentors

 * **[Mario Lassnig](mailto:mario.lassnig@cern.ch)**
 * [Martin Barisits](mailto:martin.barisits@cern.ch)
 * [Lukas Heinrich](mailto:lukas.heinrich@cern.ch)

## Links
 1. [Rucio GitHub](https://github.com/rucio/rucio)
 2. [Rucio Documentation](https://rucio.readthedocs.io/en/latest/)
 2. [Rucio system overview journal article (Springer)](https://doi.org/10.1007/s41781-019-0026-3)
 3. [Rucio operational experience article (IEEE Computer Society)](http://sites.computer.org/debull/A20mar/p9.pdf)
