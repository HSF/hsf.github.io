---
title: Automatic code generation for fast inference in the CMS tracking software
layout: plain
project: CMS
organization: CERN
---

## Description
During Run 4, the increased luminosity with the consequent increased pile-up will pose significant new challenges for CMS detector, 
in particular for the reconstruction of tracks in the Silicon Tracker and inside showers in the High Granularity Calorimeter.
When a charged particle produced after the collision flies through the detector, it leaves traces (hits).
Tracking is the art of connecting the correct traces recreating particles' trajectories. 
Timing can easily explode in reconstructing “which dot belongs to which particle” due to combinatorics and 
it will be heavily affected by the increased track density expected in the next decade. 
It is of paramount importance to choose the correct paths to follow and the correct hits to add to the path.

Start of many track finding algorithms is the building of track seeds: groups of 2 or 3 measurements 
that are compatible with each other and  with a crude track hypothesis. 
Compatibility between two hits can be also based on the hit shape. It can be imagined like the a footprint.
The shape of a hit depends on the energy released in the layer, on the crossing angle of the hit of the detector and on the type of particle.
Machine learning techniques applied on images can come in aid to reduce the combinatorics and find more stringent compatibility requirements for mitigating the combinatorial explosion. However, the integration of trained networks in the CMS software, while achieving optimal computing performance is very challenging.  
A C++ code generator for integrating an externally trained network with a fixed number of nodes for inference in the CMS event reconstruction software, would enable high-performance cluster shape recognition.



## Task ideas
 Development of a C++ code generator from a fixed size NN. Test the inference generator on the cluster shape filter by:
 * Extracting shape information from simulated CMS events
 * Using Tensorflow to train a DNN based on the shape of the hits, detector information and Montecarlo Truth
 * Measuring efficiency and fake rejection
 * Integrate in the CMS software the trained network
 
## Expected results
Reduction of the combinatorics with improvements in timing. Possibly, improvement in physics performance.

## Requirements
C++, Tensorflow, experience with ML

## Mentors 
  * [Felice Pantaleo](mailto:felice.pantaleo@cern.ch)
  * [Vincenzo Innocente](mailto:vincenzo.innocente@cern.ch)
  * [Marco Rovere](mailto:marco.rovere@cern.ch)
