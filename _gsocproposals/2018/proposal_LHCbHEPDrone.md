---
title: Extension and characterisation of the LHCb data isolation drone neural networks
layout: gsoc_proposal
project: LHCb
year: 2018
organization: CERN, NWO, STFC
---

## Description

Machine learning has proven to be an indispensable tool in the selection 
of interesting events in high energy physics. Such technologies will become 
increasingly important as detector upgrades are introduced 
and data rates increase by [orders of magnitude](http://iopscience.iop.org/article/10.1088/1742-6596/898/11/112002/meta). 

[HEPDrone](https://arxiv.org/abs/1712.09114) is a toolkit to enable the creation of a drone classifier from 
any machine learning classifier, such that different classifiers may 
be standardised into a single form and executed in parallel. 
This involves the creation of a drone neural network, which learns the required 
properties of the input neural network without the use of any training data, 
only using appropriate questioning of the input neural network.

While this technology has been proven to work converting one deep 
neural network to another the full extent of the drone suitability has yet to be determined. 
Work will need to be undertaken to give more flexibility to the drone model, 
i.e. giving more options for drone network types such as convolutional 
neural networks and long short-term memory capability. A detailed evaluation 
of the performance of different drone models in the real 
production environment of LHCb will give the collaboration a 
complete idea of not only the advantages of the drone model, 
but also the limits of drone complexity given the available computing resources.

## Task ideas

 * To create New extentions of the models used as drone neural networks in the LHCb C++ production environment.
 * Characterisation of the suitability of the networks compared to the standard deep neural network.
 * Characterisation of the performance of the extended models relative to the standard deep neural network.

## Expected results
* Working drone extentions in the LHCb C++ production environment.
* Documentation of characterisation studies.

## Requirements

* C++
* python
* Linear algebra


## Mentors

 * [Sean Benson](mailto:sean.benson@cern.ch)
 * [Konstantin Gizdov](mailto:konstantin.gizdov@cern.ch)


## Links
 * [HEPDrone arXiv](https://arxiv.org/abs/1712.09114)
 * [source code](https://github.com/HEPDrone)
