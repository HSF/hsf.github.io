---
title: Phoenix, interactive data visualization - Development of an experiment independent javascript event display framework and data format
layout: gsoc_proposal
project: Phoenix
year: 2021
organization: 
  - UMass
  - Pittsburgh
  - CERN
---

<!-- Phoenix visualisation URLs can't be validated by the checker, for some reason -->

## Description

Visualising HEP event data is currently typically done per experiment (e.g. [VP1](http://atlas-vp1.web.cern.ch/atlas-vp1/home/), [Iguana](https://doi.org/10.1016/j.nima.2004.07.036), [Fireworks](https://iopscience.iop.org/article/10.1088/1742-6596/219/3/032014/pdf)), and normally involves the installation of dedicated software. However modern browsers are more than capable of showing complex detector geometry, as well as representations of the underlying physics. As the [Visualisation](https://arxiv.org/abs/1811.10309) section of HSF Community White Paper explained, using an intermediate data format (e.g. JSON) makes it possible to separate the event display from the underlying (experiment-specific) software framework. 

[Phoenix](https://hepsoftwarefoundation.org/phoenix/) is a framework that can be used by any typical (e.g. colliding beam) High Energy Physics experiment. It was initially based on work done for the TrackML [Kaggle](https://www.kaggle.com/c/trackml-particle-identification)/[Codalab](https://competitions.codalab.org/competitions/20112) challenges (and internal use by ATLAS). GSOC students in 2019 and 2020 ported it to angular, wrote and implemented a new menu system and much more. Most base functionality now exists for the core display - the task now is to polish this, and develop better the VR display.

## Task ideas
  * Together with the rest of the Phoenix team, investigate open-source VR menu systems and use the best option to improve the VR experience in Phoenix
  * Improve the dynamic cutting to allow for two cutting planes (so we can have small geometry wedges) 
  * Implement a phi cut widget (for use in the above, but also for standard physics objects)
  * Investigate support for more HEP geometry systems, such as GeoModel and DD4HEP
  * New visualisation techniques, such as projections into a calorimeter cluster plane
  * Implement better visualisation for compound objects, such as Photons and Muons (i.e. if a Muon is created from Tracks, Clusters etc, should visually link them i.e. with colour)

## Expected results
Some UI improvements for both normal views and VR, and possibly some improved core functionality. 

## Requirements
Angular, Typescript, Web development (GUI design experience and [threejs](https://threejs.org) knowledge a bonus).

## Mentors
  * Fawad Ali [m.fawaadali98@gmail.com][mailto:m.fawaadali98@gmail.com]
  * [Riccardo Maria Bianchi](mailto:riccardo.maria.bianchi@cern.ch) 
  * [Andreas Salzburger](mailto:andreas.salzburger@cern.ch)
  * **[Edward Moyse](mailto:edward.moyse@cern.ch)**

## Links
  * [Phoenix](https://github.com/HSF/phoenix)
  * [Kaggle challenge](https://www.kaggle.com/c/trackml-particle-identification)
  * [Codalab challenge](https://competitions.codalab.org/competitions/20112)

