---
project: "EIC ATHENA"
title: "Clustering on GPUs"
layout: default
logo: hsf_logo_angled.png
description: |
  The ATHENA collaboration at the Electron-Ion Collider (EIC) is planning to build
  a novel electromagnetic calorimeter (ECAL) that combines AstroPix silicon pixel
  detector imaging layers with plastic scintillating fibers embedded in lead and
  read out at the ends. Due to the increase in segmentation that is associated with
  the 500-um pitch pixel detectors, the computational demands on finding clusters
  of hits caused by a single particle shower are much larger than for traditional
  electromagnetic calorimeters. For typical events that we expect to encounter at
  the EIC, we expect to spend the majority of computing time on this cluster
  reconstruction if we use traditional algorithms. Since the EIC experiments will
  use streaming readout, this corresponds to a bottleneck on the data rates that we
  will be able to sustain.

  In this project we aim to parallelize the clustering algorithm to run efficiently
  on GPUs, and separate the clustering algorithms into a separate library with an
  interface based on the standardized EDM4hep data model. We aim to focus from the 
  start on the SYCL cross-platform abstraction layer, mirroring an approach which 
  is already used by other components of our event reconstruction algorithm.
---

{% include gsoc_project.ext %}
