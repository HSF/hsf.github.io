---
title: GDML I/O for VecGeom geometry package

layout: gsoc_proposal
project: GeantV
year: 2018
organization: CERN
---

## Description

[VecGeom](http://iopscience.iop.org/1742-6596/608/1/012023/pdf/1742-6596_608_1_012023.pdf) is the new geometry library developed within the high-energy physics community, aiming to replace the legacy geometry navigation functionality provided by [Geant4](http://geant4.cern.ch/) and [ROOT](http://root.cern.ch) with optimized and vectorized algorithms. An important missing component of this library is I/O allowing to read geometry from application-independent formats such as the Geometry Description Markup Language ([GDML](https://gdml.web.cern.ch/GDML)).

The project aims to implementing first a GDML parser and possibly a writer allowing to make LHC geometry setups persistent and to minimize the loading time.

## Task ideas

* Contribute to developing the I/O component of a C++ geometry library
* Use XML parser and GDML schema for the implementation
* Test I/O implementation with existing geometry files

## Expected results

* Working implementation of GDML geometry reader and writer

## Requirements

* C++
* git
* Linux

## Mentors

* [Witold Pokorski](mailto:witold.pokorski@cern.ch)
* [Andrei Gheata](mailto:andrei.gheata@cern.ch)

## Links

[source code](https://gitlab.cern.ch/VecGeom/VecGeom.git)
