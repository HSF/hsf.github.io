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

Visualising HEP event data is currently typically done per experiment (e.g. [VP1](http://atlas-vp1.web.cern.ch/atlas-vp1/home/), [Iguana](https://doi.org/10.1016/j.nima.2004.07.036), [Fireworks](https://iopscience.iop.org/article/10.1088/1742-6596/219/3/032014/pdf)), and normally involves the installation of dedicated software. However modern browsers are more than capable of showing complex detector geometry, as well as representations of the underlying physics. As the [Visualisation](https://arxiv.org/abs/1811.10309) section of HSF Community White Paper explained, using an intermediate data format (e.g. JSON) makes it possible to separate the event display from the underlying (experiment-specific) software framework. It should also be possible to specify a common data format, and create an experiment-agnostic event display.

[Phoenix](https://github.com/HSF/phoenix) is an attempt at a framework that could be used by any typical (e.g. colliding beam) High Energy Physics experiment. It is based on work done for the TrackML [Kaggle](https://www.kaggle.com/c/trackml-particle-identification)/[Codalab](https://competitions.codalab.org/competitions/20112) challenges (and internal use by ATLAS), so the underlying principle is well validated but it now needs to be extended with a more sophisticated GUI, better visualisation techniques, unit tests etc. The common event data format also needs to be tested/extended with data from experiments other than ATLAS and TrackML.

## Task ideas
 * Investigate open source GUI libraries and develop improved GUI, capable of selecting/visualising specific physics object(s)
 * Extend common JSON file format for event data, ensuring that it matches the needs of all potential clients
 * Investigate and implement convertors from TGeo / GEANT4 geometry to display in phoenix
 * Investigate and implement mechanisms to publish event data
 * Investigate and implement convertors from other event data formats

## Expected results
A browser-based event display, capable of showing some simple detector geometry as well as visualisations of the event data (charged particles, photons, jets etc). The event display should be capable of displaying a subset of physics data, depending on user defined selections. We should specify a data format, complete enough to represent the data from a typical High Energy Physics experiment.

## Requirements
JavaScript, Web development (GUI design experience a bonus).

## Mentors
  * [Edward Moyse](mailto:edward.moyse@cern.ch)
  * [Riccardo Maria Bianchi](mailto:riccardo.maria.bianchi@cern.ch) 
  * [Andreas Salzburger](mailto:andreas.salzburger@cern.ch)

## Links
  * [Phoenix](https://github.com/HSF/phoenix)
  * [Kaggle challenge](https://www.kaggle.com/c/trackml-particle-identification)
  * [Codalab challenge](https://competitions.codalab.org/competitions/20112)

