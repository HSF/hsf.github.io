---
title: Enabling efficient PODIO data model integration with ONNX for training and inference
layout: gsoc_proposal
project: Key4hep
year: 2024
organization: 
 - CERN
 - DESY
 - UManitoba
difficulty: medium
duration: 350
mentor_avail: May-October
---

## Description

[PODIO](https://github.com/AIDASoft/podio) is a data model definition package that provides the necessary functionality to generate C++ and Python code from a high level definition of an event data model in yaml format. EDM4hep is an example of a data model generated with PODIO, which serves as the common event data model for many HEP communities, brought together under the umbrella of the [Key4hep](https://github.com/key4hep) project.

With the increasing importance of artificial intelligence and machine learning workflows, there is a need to integrate PODIO data models into these workflows. In particular, this may require specification or conversions of array-of-struct or struct-of-array data storage models in PODIO data models or on collections based on these data models.

## Task ideas

 * Develop a (naive, possibly inefficient) PODIO-input, ONNX-output training example for a simple binary classification problem, in a PODIO unit test.
 * Develop a (naive, possibly inefficient) PODIO-input, ONNX-input, PODIO-output inference example for the previous simple binary classification problem.
 * Develop an approach to storing sufficient information about the PODIO-input in ONNX metadata to be able to check whether the ONNX model is compatible with the specified PODIO input.
 * Develop an approach to access PODIO in training and inference that avoids the need for copying into different data structures. Since ONNX requires dense arrays for tensors, this may require modifications to PODIO so underlying types are mapped onto a struct-of-arrays.

## Expected results

 * 

## Requirements

 * Python
 * C++

## Mentors

  * [Wouter Deconinck](mailto:wouter.deconinck@umanitoba.ca)
  * [Benedikt Hegner](mailto:benedikt.hegner@cern.ch)
  * [Thomas Madlener](mailto:thomas.madlener@desy.de)

## Links

 * [PODIO](https://github.com/AIDASoft/podio)
 * [Key4hep](https://github.com/key4hep)
