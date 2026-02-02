---
title: ML Inference on heterogeneous architectures using SOFIE
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
  - first_name: Lorenzo
    last_name: Moneta
    organization: CERN
---
## Description

SOFIE (System for Optimized Fast Inference code Emit) is a Machine Learning Inference Engine within TMVA (Toolkit for Multivariate Data Analysis) in ROOT. SOFIE offers a parser capable of converting ML models trained in Keras, PyTorch, or ONNX format into its own Intermediate Representation, and generates C++ functions that can be easily invoked for fast inference of trained neural networks. Using the IR, SOFIE can produce C++ header files that can be seamlessly included and used in a 'plug-and-go' style.

SOFIE currently supports various Machine Learning operators defined by the ONNX standards, as well as a Graph Neural Network (GNN) implementation. It supports the parsing and inference of Graph Neural Networks trained using DeepMind Graph Nets.

As SOFIE continues to evolve, there's a need to enable inference on heterogeneous architectures, especially GPUs. Experiments on integrating SOFIE with the alpaka library is continuing to generate C++ code that can be executed in different architectures. This project aims to extend the SOFIE-alpaka implementation by implementing alpaka kernels for several ML operations.

## Task ideas
In this project, the contributor will gain experience with GPU programming and its role in Machine Learning inference. They will start by understanding SOFIE and the alpaka library. After understanding the SOFIE-alpaka integration, the contributor will implement alpaka kernels for inference on heterogeneus architectures, ensuring the code is efficient and well-integrated with GPU backends.

## Expected results and milestones
 * **Familiarization with SOFIE**: Understanding [SOFIE](https://github.com/root-project/root/tree/master/tmva/sofie), working with its internals, and running inference on CPUs.
 * **Familiarization with alpaka**: Exploring [alpaka](https://alpaka.readthedocs.io/) - an abstract library for portability across accelerators for heterogeneous programming, understanding its methods, constructs, and usage for kernel implementations.
 * **Implementation of GPU Inference**: Developing kernels for inference on heterogeneous architectures within the [SOFIE-alpaka](https://github.com/ML4EP/SOFIE/tree/gpu/alpaka) implementation. 
 * **[Optional] Benchmarking**: Evaluating the performance of the developed kernels by benchmarking memory usage, execution time, and comparing results with other frameworks (such as ONNX-GPU or PyTorch). 

## Requirements
  * Proficiency in C++ and Python.
  * Knowledge of GPU programming (e.g., CUDA).
  * Familiarity with version control systems like Git/GitHub.

## AI Policy
AI assistance is permitted. The applicant is fully accountable for all code and results and must disclose AI use for non-routine work (e.g., algorithm design, architecture, complex reasoning). Routine use for grammar or formatting does not need to be reported.

## How to apply
Once CERN/HSF is accepted as a GSoC org, please write an email with a short introduction to your interests and background to the mentors with the string “gsoc26” in the subject. There will be a small evaluation task that we will mail to you then.

## Links
* [SOFIE](https://github.com/root-project/root/tree/master/tmva/sofie)
* [alpaka](https://alpaka.readthedocs.io/)
* [SOFIE-alpaka Implementation](https://github.com/ML4EP/SOFIE/tree/gpu/alpaka)
* [ACAT'25 presentation describing SOFIE-alpaka implementation](https://indico.cern.ch/event/1488410/contributions/6561436/)

