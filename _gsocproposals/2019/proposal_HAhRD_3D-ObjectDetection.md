---
title: 3D-ObjectDetection
layout: gsoc_proposal
project: HAhRD
year: 2019
organization:
  - LLR
---

# Description
The challenge of [HAhRD](https://github.com/grasseau/HAhRD/wiki) project
is to implement new algorithms to classify objects from 3D images-like
coming from the data acquisition of the [future sub-detector of CMS](https://cds.cern.ch/record/2020886).
This detector which contains about 6 million channels will be used to reconstruct
the 3D cluster-like objects coming from hundreds of impinging particles arising from the
proton-proton collisions within the Large Hadron Collider. Previous successful
studies using Convolution Neural Networks (CNN), in particular in HSF-GSOC
program context, have been done for single object. In this proposal we
want to focus on object detection models to scan all clusters in our 3D image-like.
Recent cutting-edge models like R-CNN, fast(er) R-CNN, YOLO, etc. are in the top of the
ranking of the ImageNet competition. One of these models, called Mask R-CNN model have
already been evaluated in HAhRD project with 2D projections (of our 3D data), thanks
to a published implementation.
We propose for GSOC'19 to derivate a 3D version (true 3D input "gray" images), from the original 2D (RGB)
Mask R-CNN implementation.


## Task ideas and expected results
 * Start with the original implementation on our GPUs platform
 * Extend to 3D the core of the implementation (ResNet50/ResNet101).
 * Transform RGB values (int) to one gray value (float). Tests/Validation.
 * Extend to 3D the Feature Pyramid Network (FPN) module. Tests/Validation.
 * Extend to 3D the Region Proposal Network (RPN) with anchor extensions.
   Test/Validations.
 * Extent 3D to the remaining modules (I/O, configurations, etc.).
   Test/Validations.
 * Extent to other tools like visualization, evaluation.
 * Training on a simple cases (3D HGCAL images). Validation.
 * Test on more complex cases
 * Optimize the efficiency of the whole process.

## Requirements
Good knowledge on object detection (in particular R-CNN) and Deep Learning,
very good skills in TensorFlow and Keras, good python skills. Basic Knowledge
in physics would be appreciated.


## Mentors 
  * [Florian Beaudette](mailto:Florian.Beaudette@llr.in2p3.fr), senior physicist
  * [Artur Lobanov](mailto:artur.lobanov@llr.in2p3.fr), physicist
  * [Arnaud Chiron](mailto:chiron@llr.in2p3.fr), computer scientist, CMS software expert
  * [Andrea Sartirana](mailto:sartiran@llr.in2p3.fr), computer scientist, Software environment expert (containers, ...)
  * [Gilles Grasseau](mailto:gilles.grasseau@llr.in2p3.fr), computer scientist and image processing
  
