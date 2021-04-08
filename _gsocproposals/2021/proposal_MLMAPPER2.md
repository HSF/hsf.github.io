---
title: Machine Learning Model for the Lunar Albedo
layout: gsoc_proposal
project: LUNARPROSPECTOR
year: 2021
organization:
 - Alabama
 - Georgia
 - JHUAPL
---

## Description

The goal of the project is to use machine learning techniques to identify relationships between planetary mapped datasets, with the goal of providing deeper understanding of planetary surfaces and to have predictive power for planetary surfaces with incomplete datasets.

Planetary surfaces are observed as all electromagnetic wavelengths (e.g. radar, infrared, optical, ultraviolet, x-ray, gamma-ray), and each wavelength provides unique information about the chemistry, mineralogy, and history of the surface. Yet the information is not entirely independent. For example, the chemical element iron, which is mapped with x-rays and gamma rays, is highly related to optical albedo on the Moon. Knowing this, we can develop high-spatial resolution predictive maps of iron based on optical data. On other planets, the relationships between the observations are less well know, and indeed some datasets are missing.

We seek to study planetary surfaces by inputting maps of surfaces at all wavelengths available to discover the relationships between the measurements and to make predictions about chemistry that are not directly sampled by observations. This provides a way of studying the geologic history of a planet with existing data, which is valuable given the infrequent opportunities for new measurements by planetary spacecraft.

## Task ideas
  * Implement a deep multi-objective regression model to predict the chemical composition of the Moon based on data collected by the Lunar Prospector mission.

## Expected results
  * Accurate models of albedo and chemical composition based on Lunar Prospector mission data
   
## Requirements 
Python, previous experience in Machine Learning. 


## Mentors

  * [Patrick Peplowski](mailto:ml4-sci@cern.ch) (JHUAPL)
  * [Sergei Gleyzer](mailto:ml4-sci@cern.ch) (University of Alabama)
  * [Jason Terry](mailto:ml4-sci@cern.ch) (University of Georgia)
 
Please DO NOT contact mentors directly by email, and instead please send project inquiries to [ml4-sci@cern.ch](mailto:ml4-sci@cern.ch) with Project Title in the subject and relevant mentors will get in touch with you. 
