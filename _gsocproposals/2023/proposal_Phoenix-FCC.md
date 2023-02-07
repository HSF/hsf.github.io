---
project: Phoenix
title: Improving the sense of scale and navigation in high energy physics event visualisation
layout: gsoc_proposal
year: 2023
difficulty: medium
duration: 350
mentor_avail: May-October
organization:
  - CERN
  - UMass
---


## Description

The [Phoenix](https://hepsoftwarefoundation.org/phoenix/) event display offers web based visualization of the high energy physics (HEP) events coming from various HEP experiments. It is build with the help of the angular web platform with visualizations itself done with the help of the [threejs](https://threejs.org) library. Typical HEP event contains vertexes, hits, tracks, jets and missing transverse energy, which needs to be visualized in an  intuitive yet accurate way. In case of the detectors for the FCC-ee accelerator the amount of objects in one event is expected to be relatively low allowing for the interactive investigation of interesting events being practical. To efficiently examine the interesting events one needs a good sense for the scale of the event and different features in it.

In order to improve navigation in an event for the Phoenix users several features can be developed, which would focus mainly on the improved sense for the scale of the event objects and detector itself, ranging from the simple scale indicator, 3D grid with ruler markings, to the interactive measurement tool. The design of the interactive measuring tool could be implemented in the manner compatible with AR/VR capabilities of Phoenix.


## Task ideas

 * Learn the intricacies of HEP event displays
 * Investigate the current event navigation
 * Propose features/tools to be implemented
 * Implement the proposed features
 * Document the implemented features


## Requirements
 * Typescript/javascript
 * (3D experience a bonus)

## Mentors
 * [Edward Moyse](mailto:edward.moyse@cern.ch) University of Massachusetts, Amherst
 * **[Juraj Smiesko](mailto:juraj.smiesko@cern.ch)** CERN


## Links
 * [Phoenix](https://github.com/HSF/phoenix)
 * [FCC](https://fcc.web.cern.ch/)