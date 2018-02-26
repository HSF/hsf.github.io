---
title: 3D-Clustering
layout: gsoc_proposal
project: HAhRD
year: 2018
organization:
  - LLR
---

## Description
The challenge of [HAhRD](https://github.com/grasseau/HAhRD/wiki) project is to implement new algorithms to classify 
objects from 3D images-like coming from the data acquisition of the 
[future sub-detector of CMS](https://cds.cern.ch/record/2020886). This 
detector that contains about 6 million channels will be used to reconstruct 
the 3D clusters from hundreds of impinging particles arising from the 
proton-proton collisions within the Large Hadron Collider. The initial 
implementation based on an image processing algorithm is already exploited. 
We want in this proposal implement several Deep Neural Networks (DNN) 
architectures (in particular Convolutional Neural Networks - CNN) to 
classify clusters of points and develop a chain suite to analyze the 
classification performed by the DNN/CNN.

## Task ideas and expected results
 * Start with the original source code and data
 * Implement one of the selected CNN architectures (GPUs can be used 
   on our platform)
 * Implement a validation tool chain to give results of the classification 
   quality.
 * Train the CNN with different objectives (different kind of objects to 
   identify).
 * Optimize the efficiency of the whole process.
 * Extend the application to different CNN architectures or propose a 
   software architecture


## Requirements
Good  C++/C skills, good python skills, familiar with GPUs if 
possible and visualization tools. Knowledge on machine learning 
or image processing or statistics would be appreciated. 

## Mentors 
  * [Florian Beaudette](mailto:Florian.Beaudette@llr.in2p3.fr), senior physicist
  * [Artur Lobanov](mailto:artur.lobanov@llr.in2p3.fr), physicist
  * [Arnaud Chiron](mailto:chiron@llr.in2p3.fr), computer scientist, CMS software expert
  * [Andrea Sartirana](mailto:sartiran@llr.in2p3.fr), computer scientist, Software environment expert (containers, ...)
  * [Gilles Grasseau](mailto:gilles.grasseau@llr.in2p3.fr), computer scientist and image processing
  
