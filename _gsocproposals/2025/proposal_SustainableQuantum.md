---
project: QuantumForTracking
title: Sustainable Quantum Computing algorithms for particle physics reconstruction
layout: gsoc_proposal
difficulty: medium
duration: 350
mentor_avail: July-December
organization: CERN
project_mentors:
  - email: miriam.lucio.martinez@cern.ch
    organization: CERN
    first_name: Miriam
    last_name: Lucio
  - email: arantza.de.oyanguren.campos@cern.ch
    first_name: Arantza
    last_name: Oyanguren
    organization: IFIC-Valencia
---



## Description

Reconstructing the trajectories of charged particles as they traverse several detector layers is a key ingredient for event reconstruction at any LHC experiment. The limited bandwidth available, together with the high rate of tracks per second, makes this problem exceptionally challenging from the computational perspective. With this in mind, Quantum Computing is being explored as a new technology for future detectors, where larger datasets will further complicate this task. Furthermore, when choosing such alternative sustainability will play a crucial role and needs to be studied in detail. This project will consist in the implementation of both Quantum and Classical Machine Learning algorithms for track reconstruction, and using open-source, realistic event simulations to benchmark them from both a physics performance and an energy consumption perspective.

## First steps

* Basic understanding of track reconstruction at LHC using [ACTS](https://acts.readthedocs.io/en/latest/) and/or [Allen framework](https://allen-doc.docs.cern.ch/index.html).
* Familiarizing her/himself with trackML simulation datasets <https://www.kaggle.com/competitions/trackml-particle-identification/data?select=train_sample.zip>.
* Learning how to use the quantum simulator for QML algorithms https://pennylane.ai/. 


## Milestones

* Choosing a ML algorithm (or part of) in quantum computing and its classical counterpart for track reconstruction. 
* Mapping of track reconstruction problem to Ising-like Hamiltonian.
* Prototype implementation of classical and quantum track reconstruction using trackML simulation inputs.

## Expected results
 
* Benchmarking physics output and energy consumption of the classical and quantum algorithm.

## Requirements

* CUDA, python, C++

## Evaluation Tasks and Timeline

* To be completed




