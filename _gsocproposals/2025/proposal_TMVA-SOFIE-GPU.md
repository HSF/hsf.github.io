---
title: TMVA SOFIE - GPU Support for Machine Learning Inference
layout: gsoc_proposal
project: ML4EP
year: 2025
organization: CERN
difficulty: medium
duration: 350
mentor_avail: Flexible
project_mentors:
  - email: lorenzo.moneta@cern.ch
    organization: CERN
    first_name: Lorenzo
    last_name: Moneta
    is_preferred_contact: yes
  - email: sanjiban.sengupta@cern.ch
    organization: CERN
    first_name: Sanjiban
    last_name: Sengupta
---

# Description
SOFIE (System for Optimized Fast Inference code Emit) is a Machine Learning Inference Engine within TMVA (Toolkit for Multivariate Data Analysis) in ROOT. SOFIE offers a parser capable of converting ML models trained in Keras, PyTorch, or ONNX format into its own Intermediate Representation, and generates C++ functions that can be easily invoked for fast inference of trained neural networks. Using the IR, SOFIE can produce C++ header files that can be seamlessly included and used in a 'plug-and-go' style.

SOFIE currently supports various Machine Learning operators defined by the ONNX standards, as well as a Graph Neural Network (GNN) implementation. It supports the parsing and inference of Graph Neural Networks trained using DeepMind Graph Nets.

As SOFIE continues to evolve, there's a need to enable inference on GPUs. This project aims to explore different GPU stacks (such as CUDA, ROCm, ALPAKA) and implement GPU-based inference functionalities in SOFIE. There is already a SYCL implementation for SOFIE, developed in 2023, which can serve as a reference for future development.

## Task ideas
In this project, the contributor will gain experience with GPU programming and its role in Machine Learning inference. They will start by understanding SOFIE and running inference on CPUs. After researching GPU stacks and methods of their integration with SOFIE, the contributor will implement GPU support for inference, ensuring the code is efficient and well-integrated with GPU technologies.

## Expected results and milestones
 * **Familiarization with TMVA SOFIE**: Understanding the SOFIE architecture, working with its internals, and running inference on CPUs.
 * **Research and Evaluation**: Analyzing various GPU stacks (CUDA, ROCm, ALPAKA, etc.) and determining their alignment with SOFIE.
 * **Implementation of GPU Inference**: Developing functionalities for GPU-based inference in SOFIE.
 * **[Optional] Benchmarking**: Evaluating the performance of the new GPU functionality by benchmarking memory usage, execution time, and comparing results with other frameworks (such as TensorFlow or PyTorch). 

## Requirements
  * Proficiency in C++ and Python.
  * Knowledge of GPU programming (e.g., CUDA).
  * Familiarity with version control systems like Git/GitHub.

## Links
  * [ROOT Project homepage](https://root.cern/)
  * [ROOT Project repository](https://github.com/root-project/root)
  * [SOFIE Repository](https://github.com/root-project/root/tree/master/tmva/sofie)
  * [Implementation of SOFIE-SYCL](https://github.com/root-project/root/pull/13550/)
  * [Accelerating Machine Learning Inference on GPUs with SYCL](https://dl.acm.org/doi/10.1145/3648115.3648123)
