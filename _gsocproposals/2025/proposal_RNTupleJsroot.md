---
title: RNTuple in JSROOT
layout: gsoc_proposal
project: ROOT
year: 2025
organization: CERN
difficulty: medium
duration: 350
mentor_avail: June-October
project_mentors:
  - email: S.Linev@gsi.de
    organization: CERN
    first_name: Serguei
    last_name: Linev
    is_preferred_contact: yes
  - email: giacomo.parolini@cern.ch
    organization: CERN
    first_name: Giacomo
    last_name: Parolini
---

# Description
RNTuple is the next-generation data format for high-energy physics (HEP) data collected from the LHC.
It is part of ROOT, a cornerstone software package for the storage, visualization and analysis of scientific data, widely used in the scientific community and particularly in HEP.
ROOT is a C++ and Python framework, but it recently became available in the browsers as well through a Javascript implementation of some of its parts: *JSROOT*.
Since RNTuple is still in the experimental phase, it currently lacks a JSROOT interface and its contents cannot be visualized in the browser, a common and desirable property of many ROOT objects.
The goal of this project is filling this gap by making JSROOT able to read and display data stored inside an RNTuple.

## Task ideas
In this project, the student will learn the internals of the RNTuple binary format and use this knowledge to implement a Javascript interface to expose RNTuple to JSROOT.

## Expected results and milestones
 * Familiarize with the JSROOT framework, understanding how to integrate new components into it;
 * read and implement (a subset of) the RNTuple [binary format specifications](https://github.com/root-project/root/blob/master/tree/ntuple/v7/doc/BinaryFormatSpecification.md), in Javascript; this will concretely mean implementing the deserialization code from a binary blob to a RNTuple object that may be used by JSROOT;
 * enable the visualization of an RNTuple's fields in the browser, leveraging the existing framework in JSROOT.

## Requirements
  * Knowledge of Javascript / ES6
  * Basic knowledge of "low-level" programming (primitive types binary layouts, bit-level manipulations, reinterpreting bytes as different types, ...)
  * Experience with git / github
  * (Bonus): familiarity with any binary format

## Links
  * [ROOT Project homepage](https://root.cern/)
  * [ROOT Project repository](https://github.com/root-project/root)
  * [JSROOT homepage](https://root.cern/js/)
  * [JSROOT repository](https://github.com/root-project/jsroot)
  * [Introduction to RNTuple](https://root.cern/blog/rntuple-update/)
  * [RNTuple architecture overview](https://github.com/root-project/root/blob/master/tree/ntuple/v7/doc/Architecture.md)
  * [RNTuple Binary Specification](https://github.com/root-project/root/blob/master/tree/ntuple/v7/doc/BinaryFormatSpecification.md)
