---
title: Phoenix, interactive data visualization - Development of an experiment independent javascript event display framework and data format
layout: gsoc_proposal
project: Phoenix
year: 2019
organization: 
  - UMass
  - Pittsburgh
  - CERN
---

## Description

Visualising HEP event data is currently typically done per experiment (e.g. [VP1](http://atlas-vp1.web.cern.ch/atlas-vp1/home/), [Iguana](https://doi.org/10.1016/j.nima.2004.07.036), [Fireworks](https://iopscience.iop.org/article/10.1088/1742-6596/219/3/032014/pdf)), and normally involves the installation of dedicated software. However modern browsers are more than capable of showing complex detector geometry, as well as representations of the underlying physics. As the [Visualisation](https://arxiv.org/abs/1811.10309) section of HSF Community White Paper explained, using an intermediate data format (e.g. JSON) makes it possible to separate the event display from the underlying (experiment-specific) software framework. 

[Phoenix](https://hepsoftwarefoundation.org/phoenix/) is a framework that can be used by any typical (e.g. colliding beam) High Energy Physics experiment. It was initially based on work done for the TrackML [Kaggle](https://www.kaggle.com/c/trackml-particle-identification)/[Codalab](https://competitions.codalab.org/competitions/20112) challenges (and internal use by ATLAS). A LHCb example has since been added, so the underlying principle is well validated - and various "loaders" now exist to read JSON, Atlas JiveXML, LHCb and TrackML event data. The task now is to make it more user friendly, and to add functionality.

## Task ideas
 * Develop a better GUI (using open source tools). VP1 is a possible example of what should be aimed for.
 * Improve on 3D object selection (tracks in particular are very difficult to select)
 * Implement a runge-kutta propagator, which will allow use to store less data points per track
 * Continue to extend common JSON file format for event data, ensuring that it matches the needs of all potential clients
 * Add an example of the CMS experiment
 * Implement reading event data from a server, in preparation for data taking in 2021 (to visualise events in "real-time")
 * Further tests etc to improve code quality
 * New visualisation techniques, such as projects into a calorimeter cluster plan.
 * Animation of events

## Expected results
A more intuitive interface to allow complex object selection and visualisation, possibility to animate the events (for outreach and PR purposes). Better functionality and the ability to display events in "real time"

## Requirements
Angular, Typescript, Web development (GUI design experience a bonus).

## Mentors
  * [Edward Moyse](mailto:edward.moyse@cern.ch)
  * [Riccardo Maria Bianchi](mailto:riccardo.maria.bianchi@cern.ch) 
  * [Andreas Salzburger](mailto:andreas.salzburger@cern.ch)

## Links
  * [Phoenix](https://github.com/HSF/phoenix)
  * [Kaggle challenge](https://www.kaggle.com/c/trackml-particle-identification)
  * [Codalab challenge](https://competitions.codalab.org/competitions/20112)

