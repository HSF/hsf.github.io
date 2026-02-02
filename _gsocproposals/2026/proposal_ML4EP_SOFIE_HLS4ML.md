---
title: Integrating hls4ml with SOFIE for Fast ML Inference
layout: gsoc_proposal
project:
    - ML4EP
year: 2026
difficulty: medium
duration: 350
mentor_avail: June-October
organization: CERN
project_mentors:
  - email: sanjiban.sengupta@cern.ch
    first_name: Sanjiban
    last_name: Sengupta
    organization: CERN
    is_preferred_contact: yes
  - email: lorenzo.moneta@cern.ch
    first_name: Lorenzo
    last_name: Moneta
    organization: CERN
---
## Description

SOFIE (System for Optimized Fast Inference code Emit) is a Machine Learning Inference Engine within TMVA (Toolkit for Multivariate Data Analysis) in ROOT. SOFIE offers a parser capable of converting ML models trained in Keras, PyTorch, or ONNX format into its own Intermediate Representation, and generates C++ functions that can be easily invoked for fast inference of trained neural networks. Using the IR, SOFIE can produce C++ header files that can be seamlessly included and used in a 'plug-and-go' style.

SOFIE currently supports various Machine Learning operators defined by the ONNX standards, as well as a Graph Neural Network (GNN) implementation. It supports the parsing and inference of Graph Neural Networks trained using DeepMind Graph Nets.

As SOFIE evolves, there is a growing need for inference capabilities on models trained across a variety of frameworks. This project will focus on integrating hls4ml in SOFIE, thereby enabling generation of C++ inference functions on models parsed by hls4ml.

## Task ideas
In this project, the contributor will gain experience with C++ and Python programming, hls4ml, and their role in machine learning inference. The contributor will start by familiarizing themselves with SOFIE and running inference on CPUs. After researching the possibilities for integration with hls4ml, they will implement functionalities that ensure efficient inference of ML models parsed by hls4ml, which were previously trained in external frameworks like TensorFlow and PyTorch.

## Expected results and milestones
 * **Familiarization with SOFIE**: Understanding the SOFIE architecture, working with its internals, and running inference on CPUs.
 * **Research and Evaluation**: Exploring hls4ml, its support for Keras and PyTorch, and possible integration with SOFIE.
 * **Integration with hls4ml**: Developing functionalities for running inference on models parsed by hls4ml.

## Requirements
  * Proficiency in C++ and Python.
  * Knowledge of hls4ml
  * Familiarity with version control systems like Git/GitHub.

## AI Policy
AI assistance is permitted. The applicant is fully accountable for all code and results and must disclose AI use for non-routine work (e.g., algorithm design, architecture, complex reasoning). Routine use for grammar or formatting does not need to be reported.

## How to apply
Once CERN/HSF is accepted as a GSoC org, please write an email with a short introduction to your interests and background to the mentors with the string “gsoc26” in the subject. There will be a small evaluation task that we will mail to you then.

## Links
  * [SOFIE Repository](https://github.com/root-project/root/tree/master/tmva/sofie)
  * [hls4ml documentation](https://fastmachinelearning.org/hls4ml/)
  * [hls4ml Repository](https://github.com/fastmachinelearning/hls4ml)

