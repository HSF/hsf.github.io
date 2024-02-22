---
title: Geant4-FastSim - Fast inference of Diffusion models
layout: gsoc_proposal
project: Geant4
year: 2024
difficulty: medium
duration: 350
mentor_avail: June-October
organization:
  - CERN
---

## Description

In high-energy physics experiments such as the [Large Hadron Collider](https://home.cern/science/accelerators/large-hadron-collider) (LHC), some particles interact electromagnetically and/or hadronically with the material of the calorimeter, creating cascades of secondary particles, or showers. Describing the showering process relies on simulation methods that precisely define all particle interactions with matter. A detailed and accurate simulation is based on the Geant4 toolkit. The simulation of showers, with large amounts of particles created and tracked, is inherently slow. Alternatively, machine learning techniques such as generative models are used to speed up the generation of showers in a calorimeter, i.e., simulating the calorimeter response to certain particles.

Considering this, we are investigating a few different kinds of generative models such as VAE, VQ-VAE, and Diffusion based on transformer architecture. Diffusion models have proven to be significantly more accurate than others, which is what we need. However, these diffusion models come at the cost of slow inference. Therefore, this project aims to make the inference of diffusion models faster.

Furthermore, a byproduct of this project is that the student will get to work with diffusion transformer models which are currently at the forefront of AI research and learn to use them in the context of high-granularity shower data (a part of [CaloChallenge](https://calochallenge.github.io/homepage/)).

## First Steps

1. Understand how transformers and diffusion models work.
2. Understand the [shower data](https://zenodo.org/record/6366324#.Y-DJ9ezMKdY).
3. Propose ideas (with justification) for faster inference of diffusion models.

## Project Milestones
* Survey promising methods to make diffusion faster.
* Implementing and experimenting with those methods.
* Perform ablation studies around time vs accuracy


## Expected Results

A fast and accurate diffusion model for fast simulation of calorimetry showers.

## Requirements

* Solid knowledge of ML, DL, and Transformers
* Strong Python, TensorFlow/PyTorch skills

## Evaluation Tasks and Timeline

1. Find the test [here](https://docs.google.com/document/d/14HTFBO845FQlU0oYerkR_1dFzQsoZ3mgOPThjsJ6BTQ/edit?usp=sharing). Please submit it via email by 9:00 CET 7th March 2024.
2. We will make the selections based on the test and resume by 17:00 CET 8th March.
3. Students should write a short proposal (2 pages max) describing how they would approach the problem. Submit this by 18th March. We advise you to not start working on the proposal before you hear from us on 8th March.
4. We will do a second round of selection based on the short proposal. Then students will write the full proposal and submit it according to the official GSoC timeline.

## Mentors
(Please don't email before completing the test. It's not possible to reply to everyone.)
* [Piyush Raikwar](mailto:piyush.raikwar@cern.ch) (CERN)
* Peter McKeown

## Links
* [Repo](https://gitlab.cern.ch/fastsim/diffusion4sim/-/tree/DiT_renato?ref_type=heads)
* [G4FastSim](https://g4fastsim.web.cern.ch/)
