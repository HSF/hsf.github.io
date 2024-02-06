---
title: Any collection in Data model explorer
layout: gsoc_proposal
project: Key4hep
year: 2024
organization:
 - CERN
duration: 175
difficulty: medium
---

## Description

[EDM4hep](https://cern.ch/edm4hep) offers powerful set of objects to describe
event data from simulation up to analysis. At any step of this chain one can
inspect the event data containing various collections of the objects, e.g.
calorimeter clusters, tracker hits, reconstructed particles, etc. Traditionally
visualization of the event data is tied with the visualization of the detector
where visualized objects resemble their true shape. There is no visual tool
which offers detailed inspection of the data contained in the event.
[dmX](https://github.com/key4hep/dmx) offers only limited possibility to
visualize tree of MonteCarlo particles. The goal of the project will be
to extend the functionality of dmX to be able to visualize other types of
collections and relationships between them.

## Task ideas

* Implement loading of all collections of the EDM4hep
* For every collection type develop most suitable graphical representation
* Develop set of routines/actions to manipulate the visualized collections
* Test on simulated FCC events (pre-generated or new)

## Expected results
Visualization of any EDM4hep event data.

## Requirements
JavaScript

## Mentors
 * **[Juraj Smiesko](mailto:juraj.smiesko@cern.ch)** CERN

## Links
 * [EDM4hep](https://cern.ch/edm4hep)
 * [dmX](https://github.com/key4hep/dmx)
