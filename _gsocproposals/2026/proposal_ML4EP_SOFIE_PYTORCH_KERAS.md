---
title: Improving the Keras and PyTorch Parsers for ML Inference in SOFIE
layout: gsoc_proposal
project:
    - ML4EP
year: 2026
difficulty: medium
duration: 350
mentor_avail: June-October
organization: CERN
project_mentors:
  - email: lorenzo.moneta@cern.ch
    first_name: Lorenzo
    last_name: Moneta
    organization: CERN
    is_preferred_contact: yes
  - email: sanjiban.sengupta@cern.ch
    first_name: Sanjiban
    last_name: Sengupta
    organization: CERN
---
## Description

SOFIE (System for Optimized Fast Inference code Emit) is a Machine Learning Inference Engine within TMVA (Toolkit for Multivariate Data Analysis) in ROOT. SOFIE offers a parser capable of converting ML models trained in Keras, PyTorch, or ONNX format into its own Intermediate Representation, and generates C++ functions that can be easily invoked for fast inference of trained neural networks. Using the IR, SOFIE can produce C++ header files that can be seamlessly included and used in a 'plug-and-go' style.

SOFIE currently supports various Machine Learning operators defined by the ONNX standards, as well as a Graph Neural Network (GNN) implementation. It supports the parsing and inference of Graph Neural Networks trained using DeepMind Graph Nets.

As SOFIE continues to evolve, this project aims to:
* **Enhance the Keras parser** to support models trained in the latest versions TensorFlow and improve the parser interface.
* **Improve the PyTorch parser** to support parsing custom functions from models trained in PyTorch, extend the operator support, and improve the interface.

## Task ideas
In this project, the contributor will gain experience with C++ and Python programming, TensorFlow/Keras and PyTorch and their storage formats for trained machine learning models. They will begin by familiarizing themselves with SOFIE and its Keras and PyTorch parser. After researching the changes required to support the latest versions of TensorFlow and PyTorch, they will implement functionalities to ensure the successful generation of inference code for the latest models. In the next phase, they will explore models in PyTorch with custom operations, and implement changes in the respective PyTorch Parser to support them.

## Expected results and milestones
 * **Familiarization with SOFIE**: Understanding [SOFIE](https://github.com/root-project/root/tree/master/tmva/sofie), working with its internals, and running inference using the existing Keras and PyTorch parser, and analyze the current parser's capabilities.
* **Researching latest TensorFlow/Keras and PyTorch**: Investigate the latest TensorFlow/Keras and PyTorch developments and assess their alignment with SOFIE.
* **Improving the Keras and PyTorch Parser**: Implement parser enhancements to support the latest TensorFlow and PyTorch versions and validate inference results.
* **PyTorch Custom models Extensions**: Design and develop a parsing mechanism for custom functions from PyTorch models, ensuring compatibility with SOFIE’s IR and further generation of inference code.

## Requirements
  * Proficiency in C++ and Python.
  * Knowledge of TensorFlow/Keras and PyTorch.
  * Familiarity with version control systems like Git/GitHub.

## AI Policy
AI assistance is permitted. The applicant is fully accountable for all code and results and must disclose AI use for non-routine work (e.g., algorithm design, architecture, complex reasoning). Routine use for grammar or formatting does not need to be reported.

## How to apply
Once CERN/HSF is accepted as a GSoC org, please write an email with a short introduction to your interests and background to the mentors with the string “gsoc26” in the subject. There will be a small evaluation task that we will mail to you then.

## Links
  * [ROOT Project homepage](https://root.cern/)
  * [ROOT Project repository](https://github.com/root-project/root)
  * [SOFIE Repository](https://github.com/root-project/root/tree/master/tmva/sofie)
  * [Keras: The high-level API for TensorFlow](https://www.tensorflow.org/guide/keras)
  * [PyTorch: Tensors and Dynamic neural networks in Python with strong GPU acceleration](https://github.com/pytorch/pytorch)
