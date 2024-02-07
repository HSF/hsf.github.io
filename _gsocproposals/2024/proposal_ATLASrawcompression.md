---
title: Lossless compression of raw data for the ATLAS experiment at CERN
layout: gsoc_proposal
project: ATLAS
year: 2024
organization: 
 - ANL
 - CERN
difficulty: medium
duration: 175
mentor_avail: July-September
---

## Description

[ATLAS](http://atlas.cern) is one of the particle physics experiments at the [Large Hadron Collider](http://home.web.cern.ch/topics/large-hadron-collider) (LHC) at [CERN](http://home.cern/). With the planned upgrade of the LHC (the so called High Luminosity phase), allowing for even more detailed exploration of fundamental particles and forces of nature, it is expected that recorded data rate will be even ten times greater than today. Therefore, the storage requirements of the experiment will be much higher, crossing the threshold of one exabyte of tape storage (already compressed). One of the methods of addressing this challenge is to improve the compression methods, as even a small enhancement of the compression ratio may have a significant impact.


## Task ideas

 * Implement (de)compression of ATLAS RAW data making use of state-of-the-art compression algorithms, such as `zstandard` and `brotli`.
 * Study performance of the algorithms in terms of (de)compression ratio and speed, taking into account e.g. algorithm's settings as well various data-taking conditions (such as luminosity).

## Expected results

 * Find best suited compression algorithms for lossless data (de)compression and decompression of ATLAS raw data.

## Requirements

 * C++

## Mentors

  * **[Maciej Szymański](mailto:maciej.szymanski@cern.ch)**
  * [Peter Van Gemmeren](mailto:peter.van.gemmeren@cern.ch)

## Links

 * [ATLAS Experiment](https://atlas.cern/)
