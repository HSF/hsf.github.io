---
title: Precision Recovery in Lossy-Compressed Floating Point Data for High Energy Physics
layout: gsoc_proposal
project: ATLAS
year: 2025
organization:
  - ANL
  - CERN
difficulty: medium
duration: 350
mentor_avail: July-September
project_mentors:
  - email: maciej.szymanski@cern.ch
    first_name: Maciej
    last_name: Szymański
  - email: peter.van.gemmeren@cern.ch
    first_name: Peter
    last_name: Van Gemmeren
---

## Description

[ATLAS](http://atlas.cern) is one of the particle physics experiments at the [Large Hadron Collider](http://home.web.cern.ch/topics/large-hadron-collider) (LHC) at [CERN](http://home.cern/). With the planned upgrade of the LHC (the so-called High Luminosity phase), allowing for even more detailed exploration of fundamental particles and forces of nature, it is expected that the recorded data rate will be up to ten times greater than today. One of the methods of addressing this storage challenge is data compression. The traditional approach involves lossless compression algorithms such as zstd and zlib. To further reduce storage footprint, methods involving lossy compression are being investigated. One of the solutions in High Energy Physics is the reduction of floating point precision, as stored precision may be higher than detector resolution. However, when reading data back, physicists may be interested in restoring the precision of the floating point numbers. This is obviously impossible in the strict sense, as the process of removing bits is irreversible. Nevertheless, given that the data volume is high, some variables are correlated, and follow specific distributions, one may consider a machine learning approach to recover the lossy-compressed floating-point data.

## Task ideas

 * Perform lossy compression of data sample from the ATLAS experiment
 * Investigate ML techniques for data recovery, prediction and upscaling
 * Integrate the chosen technique into HEP workflow

## Expected results

 * Implementation of ML-based procedure to restore precision of lossy-compressed floating-point numbers in ATLAS data
 * Evaluation of the method's performance (decompression accuracy) and its applicability in HEP workflow

## Requirements

 * C++, Python, Machine Learning

## Links

 * [IEEE_754](https://en.wikipedia.org/wiki/IEEE_754)
 * [Implementation of FloatCompressor in Athena](https://gitlab.cern.ch/atlas/athena/-/blob/main/Control/CxxUtils/Root/FloatCompressor.cxx)
 
