---
title: Tessellated geometry support for DD4hep and ROOT/TGeo
layout: gsoc_proposal
project:
  - DD4hep
year: 2018
organisation: CERN
---

## Description
For the success of an experiment it is important to provide a consistent detector description to simulation, reconstruction and analysis applications from a single source. [DD4hep](http://dd4hep.cern.ch) is a framework for the complete description of detector models based on a single source of information.  When referring to the detector description this includes, in addition to the geometry and the materials used in the device, also parameters describing e.g. the detection techniques, constants required for alignment and calibration, description of the readout structures and conditions data. The main motivation behind the [DD4hep](http://dd4hep.cern.ch) framework is to devise a toolkit that addresses all these issues for all the stages of an experiment. The tool relies on usage of pre-existing and widely used software, combining it into a consistent generic detector description. The main components are the [ROOT](https://root.cern.ch/) geometry package (TGeo), which is used for construction and visualisation of the geometry, and the [Geant4](http://geant4.cern.ch/) simulation toolkit, which can be interfaced via [DD4hep](http://dd4hep.cern.ch) to perform detector simulation in complex detector designs.

The core element of [DD4hep](http://dd4hep.cern.ch) is the the so-called Generic Detector Description Model (based on [ROOT](https://root.cern.ch/)/TGeo ). The generic detector description is an in-memory model that consists of a set of objects containing geometry and auxiliary information about the detector. The aim of the project is to extend support for tessellated solids in [ROOT](https://root.cern.ch/)/TGeo and later adopt this implementation to [DD4hep](http://dd4hep.cern.ch) to allow import and simulation of CAD designs.


## Task ideas
 * Reuse [VecGeom](http://aidasoft.web.cern.ch/USolids) implementation of tessellated solids
 * [ROOT](https://root.cern.ch/) is able to convert in memory on demand all the solids in the [ROOT](https://root.cern.ch/)/TGeo into their [VecGeom](http://aidasoft.web.cern.ch/USolids) equivalents
 * Develop a tessellated [ROOT](https://root.cern.ch/)/TGeo shape to convert from
 * Implement a wrapper that has this shape's constructor and stores the facets data
 * Subsequently re-use the existing converter in [ROOT](https://root.cern.ch/)/TGeo to create the [VecGeom](http://aidasoft.web.cern.ch/USolids) tessellated solid based on that
 * Adopt [DD4hep](http://dd4hep.cern.ch) to read tessellated data and build the Generic Detector Description Model based on the newly developed support for tessellated solids in [ROOT](https://root.cern.ch/)/TGeo
 * Perform detector simulation with [DD4hep](http://dd4hep.cern.ch) and validate the new developments
 * Develop [DD4hep](http://dd4hep.cern.ch) plugin to support possible CAD to tesselled solid converters like [CADMesh](https://github.com/christopherpoole/CADMesh)
 

## Expected results
A functional workflow that allows to simulate CAD design in [DD4hep](http://dd4hep.cern.ch) using the newly developed support for tessellated solids in [ROOT](https://root.cern.ch/)/TGeo

## Requirements
C++, Python

## Mentors 
  * [Markus Frank](mailto:Markus.Frank@cern.ch)
  * [Andrei Gheata](mailto:Andrei.Gheata@cern.ch)
  * [Andre Sailer](mailto:andre.philippe.sailer@cern.ch)
  * [Marko Petric](mailto:marko.petric@cern.ch)

## Links
  * [DD4hep](http://dd4hep.cern.ch)
  * [ROOT](https://root.cern/)
  * [VecGeom](http://aidasoft.web.cern.ch/USolids)
  
