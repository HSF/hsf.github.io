---
title: Geant4-FastSim - Data Representation Optimisation for Generative Model-based Fast Calorimeter Shower Simulation
layout: gsoc_proposal
project: Geant4
year: 2025
difficulty: medium
duration: 350
mentor_avail: June-October
organization:
  - CERN
---

## Description

High energy physics experiments such as those operated at the Large Hadron Collider (LHC) fundamentally rely on detailed and realistic simulations of particle interactions with the detector. The state-of-the-art Geant4 toolkit provides a means of conducting these simulations with Monte Carlo procedures.  However, the simulation of particle showers in the calorimeter systems of collider detectors with such tools is a computationally intensive task. For this reason, alternative fast simulation approaches based on generative models have received significant attention, with these models now being deployed in production by current experiments at the LHC. In order to develop the next generation of fast simulation tools, approaches are being explored that would be able to handle larger data dimensionalities stemming from the higher granularity present in future detectors, while also being efficient enough to provide a sizable simulation speed-up for low energy showers. 

A shower representation which has the potential to meet these criteria is a point cloud, which can be constructed from the position, energy and time of hits in the calorimeter. Since Geant4 provides access to the (very numerous) individual physical interactions simulated in the calorimeter, it also provides a means to create a representation independent of the physical readout geometry of the detector. This project will explore different approaches to clustering these individual simulated hits into a point cloud, seeking to minimise the number of points while preserving key calorimetric observables.

## First Steps

1. Gain a basic understanding of calorimeter shower simulation ([G4FastSim](https://g4fastsim.web.cern.ch/))
2. Try simulating some electromagnetic particle showers with the [Key4hep](https://key4hep.github.io/key4hep-doc/) framework (see test)
3. Propose different approaches to clustering, with justification

## Project Milestones

* Survey different approaches to clustering
* Implement and experiment with the different methods
* Investigate the impact of varying the detector granularity on the performance of separate clustering algorithms
* If time allows, hadronic showers could also be investigated

## Expected Results

* A comparison of different approaches to clustering, with a performance evaluation in terms of the effect on calorimetric observables.
* An evaluation of the impact of varying the granularity of the detector readout on the performance of the clustering algorithm

## Requirements

* C++, Python
* Familiarity with PyTorch could be an advantage

## Evaluation Tasks and Timeline

1. Find the test [here](https://docs.google.com/document/d/1XYF8xFfprqiYYnjxu7Bzm8Ps-s646VJhIkDCQJd8n_8/edit?usp=sharing). Please submit it by 9:00 CET 17th March 2025 along with a short proposal (2 pages max) describing how you would approach the problem. See submission instructions in the test doc. Please don't forget to start the subject line with "GSoC'25 FastSim".
2. We will make the selections based on the test, short proposal and resume by 17:00 CET 24th March.
3. Selected candidates will then write the full proposal and submit it according to the official GSoC timeline.

## Mentors
(As we typically receive a large number of responses and we are not able to reply to all initial messages, please only contact us after completing the test)
* [Peter McKeown](mailto:peter.mckeown@cern.ch) (CERN)
* Piyush Raikwar (CERN)
* Anna Zaborowska (CERN)

## Links
* [G4FastSim](https://g4fastsim.web.cern.ch/)
* [CaloChallenge 2022: A Community Challenge for Fast Calorimeter Simulation](https://arxiv.org/abs/2410.21611)
