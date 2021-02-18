---
title: PODIO serialization back-end for ROOT RNTuple
layout: gsoc_proposal
project: HSF
year: 2021
organization:
    - DESY
    - CERN
---

## Description
PODIO is a C++ toolkit for the creation of event data models (EDMs) with a fast and efficient I/O layer.
An event data model is like a schema: it describes the structure of the data collected by a particle detector.
Event data models typically consist of collections of records that describe physics objects identified by the detector, for instance particles, tracks, jets, and clusters.
PODIO offers automatic code generation for efficiently implementing the EDM starting from a high level description of the objects.
PODIO uses plain-old-data (POD) structures to store the data of the objects and translates hierarchies of objects into vector of PODs for optimal I/O performance.
It is built in an extensible way so that different storage backends can be connected to read and writes the POD vectors.

The ROOT data analysis framework provides the fundamental tools for the processing of High-Energy Physics data.
ROOT RNTuple is the next-generation I/O subsystem of ROOT.
While PODIO supports ROOT's current production I/O subsystem ("TTree"), no such support exists yet for RNTuple.
The goal of this project is to add RNTuple support to PODIO.

## Task ideas and expected results
The project should develop a podio writer and reader that uses the ROOT RNTuple API in order to serialize and deserialize vectors of PODs.
The existing TTree reader and writer can be used as a template.
A first comparison between RNTuple and TTree files (e.g., file size, read and write throughput) would complete the project.

## Evaluation Task
Interested students please contact Jakob (jblomer@cern.ch) or Javier (j.lopez@cern.ch) for a warm-up and evaluation task.

## Requirements
 * C++, low-level data storage and access programming

## Mentors
 * **[Thomas Madlener](mailto:thomas.madlener@desy.de)**
 * [Valentin Volkl](mailto:valentin.volkl@cern.ch)
 * [Jakob Blomer](mailto:jblomer@cern.ch)

## Links
 * [POD I/O code](https://github.com/AIDASoft/podio)
 * [POD I/O Overview](https://www.epj-conferences.org/articles/epjconf/pdf/2020/21/epjconf_chep2020_05024.pdf)
 * [ROOT](https://root.cern/)
 * [RNTuple Overview](https://indico.cern.ch/event/773049/contributions/3474746/attachments/1937507/3211341/rntuple-chep19.pdf)
 * [RNTuple Code](https://github.com/root-project/root/tree/master/tree/ntuple/v7)
 * [RNTuple Tutorials](https://github.com/root-project/root/tree/master/tutorials/v7/ntuple)
