---
title: TMVA SOFIE - Enhancing Keras Parser and JAX/FLAX Integration
project: ROOT
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

As SOFIE continues to evolve, this project aims to:
* **Enhance the Keras parser** to support models trained in the latest TensorFlow v2.18.0, which introduces NumPy 2.0 compatibility.
* **Integrate JAX/FLAX support**, enabling SOFIE to generate C++ inference functions for models developed using JAX/FLAX.

## Task ideas
In this project, the contributor will gain experience with C++ and Python programming, TensorFlow/Keras and its storage formats for trained machine learning models, and JAX/FLAX for accelerated machine learning. They will begin by familiarizing themselves with SOFIE and its Keras parser. After researching the changes required to support the latest TensorFlow version, they will implement functionalities to ensure the successful generation of inference code for the latest Keras models. In the next phase, they will explore the JAX/FLAX library and investigate its potential integration with SOFIE.

## Expected results and milestones
** **Familiarization with TMVA SOFIE**: Understand the SOFIE architecture, run inference using the existing Keras parser, and analyze the current parser's capabilities.
* **Researching latest TensorFlow/Keras**: Investigate the latest TensorFlow/Keras developments and assess their alignment with SOFIE.
* **Improving the Keras Parser**: Implement parser enhancements to support the latest TensorFlow version and validate inference results.
* **JAX/FLAX Integration**: Design and develop a parsing mechanism for JAX/FLAX models, ensuring compatibility with SOFIE’s IR and further generation of inference code.

## Requirements
  * Proficiency in C++ and Python.
  * Knowledge of TensorFlow/Keras and JAX/FLAX.
  * Familiarity with version control systems like Git/GitHub.

## Links
  * [ROOT Project homepage](https://root.cern/)
  * [ROOT Project repository](https://github.com/root-project/root)
  * [SOFIE Repository](https://github.com/root-project/root/tree/master/tmva/sofie)
  * [Keras: The high-level API for TensorFlow](https://www.tensorflow.org/guide/keras)
  * [JAX Documentation](https://docs.jax.dev/en/latest/)
  * [FLAX Documentation](https://flax.readthedocs.io/en/latest/)
