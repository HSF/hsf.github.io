---
title: Rucio - The ATLAS Distributed Data Management System
layout: gsoc_proposal
project: ATLAS
organization:
 - University of Oslo
 - CERN
---

## Description

The ATLAS experiment at the LHC is a general purpose particle physics detector designed to investigate physics at the energy frontier. the ATLAS DDM system manages now more than 250 petabytes spread on 130 storage sites and can handle file transfer rates of up to 30Hz. The current DDM system relies on the Rucio software project, developed during Long Shutdown 1 to address the scalability challenges of Run-2. It provides a catalogue for all ATLAS data and takes care of data transfers, deletions and many other data management operations. This version of the DDM system has been operating robustly, stably and effectively since the beginning of 2016. But, we need to gain one order of magnitude in computing capability to take ATLAS forward into the next years of high luminosity LHC running. For example, the necessary and increasing usage of the network will bring some interesting challenges in the coming years.

The proposed project will be to empower the ATLAS Distributed Data Management System with Google Cloud third party services. Rucio has a flexible design and a component oriented architecture favouring the evaluation of external services. Once integrated, these solutions will be evaluated at full scale (and beyond).

## Task ideas

The proposed project aims at extending or replacing some Rucio functionalities by Google cloud platform services addressing some the potential scalability issues. Therefore, we have identified the following services which can bring many benefits back to the ATLAS DDM system:

- Cloud based object stores (e.g., Google Cloud Storage) integration to store physics data to serve analysis jobs.
- Third party copy transfer service (e.g., Cloud Storage Transfer Service) to mass transfer data from/to institutional and cloud storage.
- NoSQL solution (e.g., BigTable) for physics data referencing and metadata searches.
- Content Delivery Network (e.g. Google Cloud CDN ) to transparently cache load balanced content close to the physicists or the analysis jobs requiring (WAN) data access. 

The integration of these components will require to find some compatible authentication, authorization and accounting model between the various involved services. 

## Expected results

A working implementation of the desired new functionalities and fully tested at large scale and in distributed environment.

## Requirements

- Python
- Git
- Shell cripting
- Linux
- Experience with relational and non-relational databases preferred (Sqlite, MySQL, ORACLE, Hadoop-based)
- Experience with distributed or concurrent software


## Mentors

- [Vincent Garonne](mailto:Vincent.Garonne@cern.ch)
- [Mario Lassnig](mailto:Mario.Lassnig@cern.ch)
- [Martin Barisits](mailto:Martin.Barisits@cern.ch)
- [Cedric Serfon](mailto:Cedric.Serfon@cern.ch)

## Links

- [Rucio Public Github Mirror](https://github.com/rucio01/rucio)
- [Rucio Website](http://rucio.cern.ch)
- [Google Cloud Services](https://cloud.google.com/)
