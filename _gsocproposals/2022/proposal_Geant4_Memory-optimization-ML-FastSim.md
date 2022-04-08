---
title: Geant4-FastSim - Memory footprint optimization for ML fast shower simulation 
layout: gsoc_proposal
project: Geant4
year: 2022
difficulty: medium
duration: 350
mentor_avail: July-October
organization:
  - CERN
---

# Description

In [Large Hadron Collider](https://home.cern/science/accelerators/large-hadron-collider) (LHC) experiments, at [CERN](https://home.cern/) in Geneva, the calorimeter is a key detector technology to measure the energy of particles. These particles interact electromagnetically and/or hadronically with the material of the calorimeter, creating cascades of secondary particles or showers. Describing the showering process relies on simulation methods that precisely describe all particle interactions with matter. A detailed and accurate simulation is based on the [Geant4](https://geant4.web.cern.ch/) toolkit. Constrained by the need for precision, the simulation is inherently slow and constitutes a bottleneck for physics analysis. Furthermore, with the upcoming [high luminosity upgrade](https://hilumilhc.web.cern.ch/) of the LHC with more complex events and a much increased trigger rate, the amount of required simulated events will increase. 
Machine Learning (ML) techniques such as generative modeling are used as fast simulation alternatives to learn to generate showers in a calorimeter, i.e. simulating the calorimeter response to certain particles. The pipeline of a fast simulation solution can be categorized into five components: data preprocessing, ML model design, validation, inference and optimization. The preprocessing module allows us to derive a suitable representation of showers, to perform data cleaning, scaling and encoding. The preprocessed data is then used by the generative model for training. In order to search for the best set of hyperparameters of the model, techniques such as Automatic Machine Learning (AutoML) are used. The validation component is based on comparing different ML metrics and physics quantities between the input and generated data. After training and validation the model is converted into a format that can be used for inference in C++. This allows its application directly in the frameworks of physics experiments. The optimization component is used to further reduce the memory footprint of the model at inference time. Moreover, optimization techniques are also used at training time to reduce the number of trainable parameters. 
The aim of this project is to optimize the ML pipeline of the fast simulation approach using the open-source platform [Kubeflow](https://github.com/kubeflow/kubeflow) with a focus on the memory footprint optimization of the model during training and inference. Furthermore, a byproduct of this project is that the student will gain expertise in cutting-edge ML techniques, and learn to use them in the context of high granularity image generation and fast simulation. Moreover, this project can serve as a baseline for future ML pipelines for all experiments at CERN. 


## Project Milestones

* Build Kubeflow pipeline from the existing project (optimization and inference)
* Benchmark optimization techniques to reduce the memory footprint of the model

## Expected results

An efficient ML pipeline with documentation that must include:

* Pipeline documentation 
* Plots and outputs of Kubeflow performance monitoring
* Comparison and evaluation of memory footprint optimization techniques

## Requirements

* Solid knowledge of ML
* Strong python skills

## Evaluation tasks

Python and ML exercises.

## Mentors

* **[Anna Zaborowska](mailto:anna.zaborowska@cern.ch)** (CERN)
* [Dalila Salamani](mailto:dalila.salamani@cern.ch) (CERN)

## Links

* [Geant4](https://geant4.web.cern.ch) 
* [Kubeflow](https://github.com/kubeflow/kubeflow) 
* [ML4Sim](https://indico.cern.ch/category/13860/)
