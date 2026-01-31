---
title: Optimisation and validation of shower data for ML-based calorimeter simulation
layout: gsoc_proposal
project:
    - Geant4
    - ML4EP
year: 2026
difficulty: medium
duration: 350
mentor_avail: June-October
organization: CERN
project_mentors:
  - email: peter.mckeown@cern.ch
    first_name: Peter
    last_name: McKeown
    organization: CERN
    is_preferred_contact: yes
    additional_information: (As we typically receive a large number of responses and we are not able to reply to all initial messages, please only contact us after completing the test)
  - first_name: Anna
    last_name: Zaborowska
    organization: CERN
---
## Description

Particle physics experiments, such as those operated at the Large Hadron Collider, fundamentally rely on accurate simulations of interactions between particles and the detector. The Geant4 toolkit provides the state-of-the-art means of conducting these simulations with traditional Monte Carlo techniques. However, the vastly increased simulation requirements of future experiments, such as those which will be operated at the HL-LHC, require the adoption of alternative approaches. This is particularly true for particle shower simulation in the calorimeter systems of experiments. Fast simulation approaches based on generative models have been shown to provide fast yet accurate simulation surrogates, and have recently started to be deployed in production by current LHC experiments.

This project seeks to produce calorimeter shower datasets in the form of point clouds, which are a flexible representation of showers, particularly suited to highly granular calorimeters. Physics validation of the dataset will be conducted to ensure appropriate optimisation of the algorithm used to produce the point cloud, as well as sufficient coverage of the detector. This work will be done in the Key4hep framework under development for future colliders.

## First Steps

1. Gain a basic understanding of calorimeter shower simulation ([G4FastSim]((https://g4fastsim.web.cern.ch/)))
2. Try simulating some electromagnetic particle showers with the [Key4hep](https://key4hep.github.io/key4hep-doc/) framework (see test)
3. Propose a work plan towards producing a dataset appropriate for training an ML model, including studies related to physics validation

## Project Milestones

- Starting with electromagnetic showers, tune existing algorithms to produce point cloud representations of showers, ensuring appropriate preservation of single-shower observables 
- Perform initial studies into detector coverage, to ensure sufficient training statistics across the detector
- Repeat these procedures for hadronic showers

## Expected Results

- A complete workflow for producing large-scale datasets of calorimeter showers in the form of point clouds that are suitable for use for training a production-ready ML model
- A complete validation of the physics performance of the obtained point cloud, which minimises the number of points while retaining physics accuracy
- If time allows, finalised datasets for both electromagnetic and hadronic showers

## Requirements

* C++, Python
* Familiarity with PyTorch could be an advantage

## Evaluation Tasks and Timeline

1. Find the test [here](https://docs.google.com/document/d/1nieJAOx0t4V1ZoxegGFsCqflkHziakCxMGor1o5zDsQ/edit?usp=sharing). Please submit it by 9:00 am CET 9th March 2026 along with a short proposal (2 pages max) describing how you would approach the problem. See submission instructions in the test document. Please don't forget to start the subject line with “GSoC’26 FastSim”.
2. We will make the selections based on the test, short proposal and resume by 17:00 CET 16th March.
3. Selected candidates will then write the full proposal and submit it according to the official GSoC timeline.

## Mentors
(As we typically receive a large number of responses and we are not able to reply to all initial messages, please only contact us after completing the test)
* [Peter McKeown](mailto:peter.mckeown@cern.ch) (CERN)
* Anna Zaborowska (CERN)

## Links
* [G4FastSim](https://g4fastsim.web.cern.ch/)
* [CaloChallenge 2022: A Community Challenge for Fast Calorimeter Simulation](https://arxiv.org/abs/2410.21611)
* [step2point dataset](https://arxiv.org/abs/2509.22340)
* [LEMURS dataset](https://arxiv.org/html/2509.05108v2)
* [A First Full Physics Benchmark for Highly Granular Calorimeter Surrogates](https://arxiv.org/abs/2511.17293)

