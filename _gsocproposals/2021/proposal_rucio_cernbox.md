---
title: Rucio and CS3APIs: enabling data management for the ScienceMesh cloud
layout: gsoc_proposal
project: Rucio
year: 2021
organization:
    - CERN
---

## Description

[CERNBox](https://cernbox.web.cern.ch/cernbox/) is a sync and share collaborative cloud storage solution at CERN used by more than 37K users and storing over 12PB of data. The service has evolved from a simple platform providing sync and share services to a collaboration hub to empower scientists. The service has been upgraded to include the [Reva](https://reva.link) daemon in its core, implementing the vendor-neutral [CS3APIs](https://cs3org.github.io/cs3apis/) interfaces to bridge the gap between heterogeneous storage systems and a wide variety of application providers.

[Rucio](https://rucio.cern.ch) is an open-source software framework that provides functionality to scientific collaborations to organize, manage, monitor, and access their distributed data and dataflows across heterogeneous infrastructures. Rucio was originally developed to meet the requirements of the high-energy physics experiment ATLAS, and is continuously enhanced to support diverse scientific communities. Since 2016 Rucio orchestrated multiple Exabytes of data access and data transfers globally.

The goal of this proposal to bring support to Rucio to connect to CS3 compliant clouds. Such integration will enable Rucio to become a key player in the pan-European [ScienceMesh](https://cs3mesh4eosc.eu/) federated cloud and a key technology to orchestrate data transfers amongst European institutions.

## Tasks

The tasks are as follows:
 * Analyse the CS3APIs and find set of operations needed by Rucio for metadata and data handling
 * Implement the CS3API-client connector in Rucio
 * Test integration between Rucio and CERNBox
 * Document the Rucio CS3 connector

## Requirements

 * Mandatory
   * Python 3
   * Linux, Git, and Docker
 * Basic understanding
   * gRPC and Protocol Buffers
   * Protocol Buffers
   * HTTP REST APIs

## Expected results

By the end of GSoC'21 we expect at the end of the deliverable a Rucio plugin that can connect to CS3-compatible clouds, demonstrating data transfers between two endpoints in ScienceMesh.

## Mentors
 * [Martin Barisits (Rucio)](mailto:martin.barisits@cern.ch)
 * [Hugo Gonzalez Labrador (CS3MESH4EOSC)](mailto:hugo.gonzalez.labrador@cern.ch)
 * [Mario Lassnig (Rucio)](mailto:mario.lassnig@cern.ch)
 * [Giuseppe Lo Presti (CERNBox)](mailto:giuseppe.lopresti@cern.ch)

## Links
 1. [Rucio GitHub](https://github.com/rucio/rucio)
 2. [Rucio Documentation](https://rucio.readthedocs.io/en/latest/)
 2. [Rucio system overview journal article (Springer)](https://doi.org/10.1007/s41781-019-0026-3)
 3. [Rucio operational experience article (IEEE Computer Society)](http://sites.computer.org/debull/A20mar/p9.pdf)
