---
title: Aparche Arrow interface for PODIO
layout: gsoc_proposal
project: PODIO
year: 2026
organization:
  - bnl
  - umanitoba
difficulty: medium
duration: 175
mentor_avail: June-October
project_mentors:
  - email: dmitry.kalinkin+eic@gmail.com
    first_name: Dmitry
    last_name: Kalinkin
    organization: bnl
    is_preferred_contact: yes
  - email: wouter.deconinck@umanitoba.ca
    first_name: Wouter
    last_name: Deconinck
    organization: umanitoba
---

## Description

Typical data analysis in High-Energy Physics or Nuclear Physics operates on events containing lists of structures describing signals recorded in the experiment. Depending on the type of the hardware (detector component) that produces the signals, the structures will contain different fields (amplitudes, charge integrals, times, channel IDs, etc), defining the distinct "type" of the structure. A collection of possible types that are used within an experiment can be refferd to as "Event Data Model" (EDM). Those types can be defined directly in C++ as `class A` or `struct A`, but many solutions employ custom ways to define types: their names, their fields and possible object-to-object relations. One of such solutions is PODIO:

> PODIO, or plain-old-data I/O, is a C++ library to support the creation and handling of data models in particle physics. It is based on the idea of employing plain-old-data (POD) data structures wherever possible, while avoiding deep-object hierarchies and virtual inheritance. This is to both improve runtime performance and simplify the implementation of persistency services.

PODIO uses YAML to define EDM, which it automatically translates into C++ code that implements all the types used to represent the objects and collections (lists) of objects. The library is used to enable ongoing studies at the future Electron-Ion Collider (EIC) and several other proposed projects such as Future Circular Collider (FCC), Muon Collider (IMCC) and others. It is used as a key component of an EICrecon framework that will enable streaming readout and reconstruction at the future ePIC experiment at the EIC.

The PODIO allows storage of the objects in the ROOT file format and in SIO file format. The proposed project will aim at adding another backend for PODIO that instead of providing a file format would allow conversion to an in-memory format provided by the Apache Arrow library:

> Apache Arrow defines a language-independent columnar memory format for flat and nested data, organized for efficient analytic operations on modern hardware like CPUs and GPUs. The Arrow memory format also supports zero-copy reads for lightning-fast data access without serialization overhead.

This will out-of-box enable serialization/deserialization to various formats (such as Avro, Orc, Parquet and Feather) as well as IPC, heterogenious computing and convenient columnar access to the data.

## Expected results and milestones

 - Participant is familiar with principle of how PODIO data model works from YAML specification to its generated C++ code
 - A new Arrow backend is implemented for PODIO in addition to the existing ROOT and SIO backends
 - Implementation is validated with a round trip: conversion of a PODIO Frame to Arrow Table and back to PODIO Frame
 - (Optional goal) Conversion to Parquet and to ROOT formats are benchmarked for speed and disk space use

## Requirements

 - Ability to work in Linux/UNIX
 - Ability to program in C++
 - (Preferred) Ability to program in Python

## AI Policy

AI assistance is allowed for this contribution. The applicant takes full responsibility for all code and results, disclosing AI use for non-routine tasks (algorithm design, architecture, complex problem-solving). Routine tasks (grammar, formatting, style) do not require disclosure.

## How to apply

Once CERN/HSF is accepted as a GSoC org, please write an email with a short introduction to your interests and background to the mentors with the string “gsoc26” in the subject. There will be a small evaluation task that we will email to you then.

## Resources

 - [Apache Arrow](https://arrow.apache.org/)
 - [PODIO](https://github.com/AIDASoft/podio)
 - [C++’s Next Decade - Herb Sutter - CppCon 2024](https://www.youtube.com/watch?v=FNi1-x4pojs&t=3720s)
