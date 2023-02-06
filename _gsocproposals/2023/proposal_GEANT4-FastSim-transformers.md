---
title: Geant4-FastSim - Transformer-based architecture for fast shower simulation
layout: gsoc_proposal
project: Geant4
year: 2023
difficulty: medium
duration: 350
mentor_avail: June-October
organization:
  - CERN
---

## Description

In [Large Hadron Collider](https://home.cern/science/accelerators/large-hadron-collider) (LHC) experiments, at [CERN](https://home.cern/) in Geneva, the calorimeter is a detector that measures the energy of particles. These particles interact electromagnetically and/or hadronically with the material of the calorimeter, creating cascades of secondary particles or showers. Describing the showering process relies on simulation methods that precisely define all particle interactions with matter. A detailed and accurate simulation is based on the [Geant4](https://geant4.web.cern.ch/) toolkit. The simulation of showers, with large amounts of particles created and tracked, is inherently slow. With the upcoming [high luminosity upgrade](https://hilumilhc.web.cern.ch/) of the LHC with more complex events and a much increased trigger rate, the amount of required simulated events will increase. Machine Learning (ML) techniques such as generative models are used as fast simulation alternatives to learn to generate showers in a calorimeter, i.e. simulating the calorimeter response to certain particles.

Considering the recent advancements brought by foundation models (GPT-3, Dall-E-2, etc.) in AI, the idea is to study the applicability of a large-scale transformer-based model for fast simulation. In this regard, we already have a model in development with an architecture similar to [ViT](https://arxiv.org/abs/2010.11929) (Vision Transformers). Although a transformer is supposed to be a generalized architecture in terms of how it can handle any type of data (text, images, audio, etc.), its downside is having a tradeoff between the computation requirements and the generalizability of the architecture. As generalizability decreases, inductive bias increases, and hence it gets computationally efficient and vice-versa. There are a lot of successors to ViT e.g., [Swin Transformer](https://arxiv.org/abs/2103.14030) that emphasises on incorporating inductive biases for images to make the architecture computationally efficient. However, particle showers tend to be considerably different from images in terms of sparsity, range of values, dimensions, etc. Hence, the goal of this project would be to explore transformer-based architectures with custom attention, patching, positional encodings, and the overall design.

Furthermore, a byproduct of this project is that the student will get to work with generative transformers which are currently at the forefront of AI research, and learn to use them in the context of high-granularity shower data.


## First Steps

1. Understand how transformers work and how the original transformer architecture is modified for images.
2. Understand the [shower data](https://zenodo.org/record/6366324#.Y-DJ9ezMKdY).
3. Think of modifications that can bring benefit when using transformers for shower data.

## Project Milestones
* Survey promising transformer-based architectures.
* Implement the transformer-based architecture.
* Perform ablation studies around its hyperparameters.

## Expected Results

A custom transformer-based architecture specifically suited for particle showers.

## Requirements

* Solid knowledge of ML, DL, and Transformers
* Strong Python, TensorFlow/PyTorch skills

## Evaluation Tasks

Python and ML exercises.

## Mentors
* **[Dalila Salamani](mailto:dalila.salamani@cern.ch)** (CERN)
* [Piyush Raikwar](mailto:piyush.raikwar@cern.ch) (CERN)
* [Anna Zaborowska](mailto:anna.zaborowska@cern.ch) (CERN)

## Links
* [Repo](https://gitlab.cern.ch/praikwar/ml4fastsim/-/tree/pytorch_port)
* [ML4Sim](https://g4fastsim.web.cern.ch/)
