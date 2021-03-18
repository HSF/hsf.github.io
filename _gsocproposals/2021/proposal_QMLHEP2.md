---
title: Quantum Neural Networks for High Energy Physics Analysis at the LHC
layout: gsoc_proposal
project: QMLHEP
year: 2021
organization:
 - Alabama
 - Wisconsin
 - Waterloo
---

## Description
The ambitious [HL-LHC](https://hilumilhc.web.cern.ch) program will require enormous computing resources in the next two decades. New technologies are being sought after to replace the present computing infrastructure. A burning question is whether quantum computer can solve the ever growing demand of computing resources in High Energy Physics (HEP) in general and physics at [LHC](https://home.cern/science/accelerators/large-hadron-collider) in particular. Our goal here is to explore and to demonstrate that Quantum Computing can be the new paradigm (Proof of Principle).

Discovery of new physics requires the identification of rare signals against immense backgrounds. Development of machine learning methods will greatly enhance our ability to achieve this objective. However, with this ever-growing volume of data in the near future, current machine learning algorithms will require large computing resources and excessive computing time to achieve good performance. Quantum Computing in Qubit platform, where qubits are used instead of bits in classical computer, has the potential to improve the time complexity of classical algorithms.

With this project we seek to implement Quantum Machine Learning methods for LHC HEP analysis based on Google TensorFlow Quantum (“TF Quantum is an open source library for quantum machine learning”). This will enhance the ability of the HEP community to use Quantum Machine Learning methods. In addition, we also would like to develop a common QML interface for HEP which can support different quantum frameworks such as TensorFlow Quantum.


## Task ideas
  * Implement a Quantum Convolutional Neural Network (QCNN) method based on Google Tensorflow Quantum framework.
  * Apply the quantum machine learning method to a benchmark high-energy physics analysis and benchmark the quantum machine learning performance compared to classical machine learning methods
 
## Expected results
  * Trained Quantum Convolutional Neural Network with TensorFlow Quantum framework.
  * Apply the Quantum Machine Learning method to LHC physics analysis and ompare to classical machine learning methods.
  
## Requirements 
  * Solid knowledge of machine learning and deep learning
  * Some knowledge of quantum mechanics desired
  * Familiarity with c/c++
  * Strong python skills


## Mentors
  * [Rui Zhang](mailto:ml4-sci@cern.ch) (University of Wisconsin-Madison)
  * [Shaojun Sun](mailto:ml4-sci@cern.ch) (University of Wisconsin-Madison)
  * [Chen Zhou](mailto:ml4-sci@cern.ch) (University of Wisconsin-Madison)
  * [Alkaid Cheng](mailto:ml4-sci@cern.ch) (University of Wisconsin Madison)
  * [Sergei Gleyzer](mailto:ml4-sci@cern.ch) (University of Alabama)
  * [Raphael Koh](mailto:ml4-sci@cern.ch) (University of Waterloo)
  * [Wen Guan](mailto:ml4-sci@cern.ch) (University of Wisconsin-Madison)
  * [Emanuele Usai](mailto:ml4-sci@cern.ch) (Brown University)

Please DO NOT contact mentors directly by email, and instead please send project inquiries to [ml4-sci@cern.ch](mailto:ml4-sci@cern.ch) with Project Title in the subject and relevant mentors will get in touch with you. 
