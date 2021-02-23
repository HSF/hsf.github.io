---
title: Cosmic-Ray Imaging Studies via Mission-Imagery from Space (CRISMIS)
layout: gsoc_proposal
project: CRISMIS
year: 2021
organization:
  - Alabama
  - JHUAPL
---

## Description

[CRISMIS](https://www.researchgate.net/publication/327526829_Observation_of_galactic_cosmic_ray_spallation_events_from_the_SoHO_mission_20-yr_operation_of_LASCO) is an open-source machine learning based tool to identify cosmic-ray artifacts in imaging data
 
Galactic cosmic rays are energetic particles in deep space that originate from supernova explosions. Studies of cosmic rays have revealed the nature of astrophysical processes, and led to the discovery of subatomic particles such as muons and pions. Currently, space-based cosmic ray experiments, including the [AMS](https://home.cern/science/experiments/ams) experiment on the [International Space Station](https://www.nasa.gov/mission_pages/station/main/index.html), are searching for evidence of dark matter and antimatter.
 
CCD-based cameras operate throughout the solar system, imaging the surfaces of other planets, our sun, and deep-space objects such as stars, extrasolar systems, and galaxies. These cameras are subjected to constant irradiation by galactic cosmic rays. Cosmic rays can interact with the CCD camera and produce image artifacts. Normal analysis of these images seeks to either correct the artifacts or remove the image from the data processing pipeline. As in the old adage “one man’s trash is another man’s treasure”, these cosmic-ray-induced image artifacts provide information about cosmic ray energies and flux, both of which vary in response to the strength of the magnetic field. While dedicated cosmic-ray monitoring experiments routinely conducted at Earth and Earth’s vicinity, they are not commonly performed via imaging measurements. 
 
The CRISMIS project focuses on development of an open-source, machine-learning based tool to identify cosmic-ray artifacts in CCD imaging data products. Such a tool would be useful for space science teams to automatically filter their data. Moreover, identifying cosmic-ray events in images, and classifying their nature and frequency opens a new path for studying cosmic-ray events throughout the solar system. 



## Task ideas and expected results
 * Develop automated image ingestion and processing code.
 * Develop artifact categorization routine
 * Perform cosmic-ray artifact identification and categorization


## Requirements 
Python, C++, and some previous experience in Machine Learning. 

## Mentors
  * [Patrick Peplowski](mailto:Patrick.Peplowski@jhuapl.edu) (JHUAPL)
  * [Sergei Gleyzer](mailto:Sergei.Gleyzer@cern.ch) (University of Alabama)
 
Please DO NOT contact mentors directly by email, and instead please send project inquiries to [ml4-sci@cern.ch](mailto:ml4-sci@cern.ch) with Project Title in the subject and relevant mentors will get in touch with you. 
