---
title: Implementation of Quantum Generative Models to Perform High Energy Physics Analysis at the LHC
layout: gsoc_proposal
project: QMLHEP
year: 2022
organization:
 - Alabama
 - Wisconsin
 - Waterloo
 - Brown
---

## Description
The ambitious [HL-LHC](https://hilumilhc.web.cern.ch) program will require enormous computing resources in the next two decades. New technologies are being sought after to replace the present computing infrastructure. A burning question is whether quantum computer can solve the ever growing demand of computing resources in High Energy Physics (HEP) in general and physics at [LHC](https://home.cern/science/accelerators/large-hadron-collider) in particular. Our goal here is to explore and to demonstrate that Quantum Computing can be the new paradigm (Proof of Principle).

Discovery of new physics requires the identification of rare signals against immense backgrounds. Development of machine learning methods will greatly enhance our ability to achieve this objective. However, with this ever-growing volume of data in the near future, current machine learning algorithms will require large computing resources and excessive computing time to achieve good performance. Quantum Computing in Qubit platform, where qubits are used instead of bits in classical computer, has the potential to improve the time complexity of classical algorithms.

With this project we seek to implement Quantum Machine Learning methods for LHC HEP analysis based on Google TensorFlow Quantum (“TF Quantum is an open source library for quantum machine learning”). This will enhance the ability of the HEP community to use Quantum Machine Learning methods. In addition, if possible, we also would like to develop a common QML interface for HEP which can support different quantum frameworks such as TensorFlow Quantum.

## Duration

Total project length: 175 hours.

## Task ideas
  * Implement a Quantum Generative Adversarial Network (QGAN) method based on Google Tensorflow Quantum framework.
  * Apply the quantum machine learning method to one LHC flagship physics channel (e.g. double-Higgs production). Compare the quantum machine learning performance to the classical machine learning performance.
 
## Expected results
  * Trained Quantum Generative Adversarial Network method based on Google TensorFlow Quantum framework.
  * Successfully apply the Quantum Machine Learning method to LHC physics analyses and obtain performance benchmarks to compare to classical machine learning methods.
  
## Test

Please use this link to access the test for this project. Tests will be published in March.
  
## Requirements 
  * Solid knowledge of machine learning and deep learning
  * Some knowledge of quantum mechanics desired
  * Familiarity with c/c++
  * Strong python skills


## Mentors
  * [Rui Zhang](mailto:ml4-sci@cern.ch) (University of Wisconsin-Madison)
  * [Shaojun Sun](mailto:ml4-sci@cern.ch) (University of Wisconsin-Madison)
  * [Chen Zhou](mailto:ml4-sci@cern.ch) (University of Wisconsin-Madison)
  * [Sergei Gleyzer](mailto:ml4-sci@cern.ch) (University of Alabama)
  * [Raphael Koh](mailto:ml4-sci@cern.ch) (University of Waterloo)
  * [Wen Guan](mailto:ml4-sci@cern.ch) (University of Wisconsin-Madison)
  * [Emanuele Usai](mailto:ml4-sci@cern.ch) (Brown University)

## Links
  * [HL-LHC](https://hilumilhc.web.cern.ch)
  * [LHC](https://home.cern/science/accelerators/large-hadron-collider)
  * [TensorFlow Quantum](https://www.tensorflow.org/quantum/overview)


Please **DO NOT** contact mentors directly by email. Instead, please email [ml4-sci@cern.ch](mailto:ml4-sci@cern.ch) with Project Title and **include your CV** and **test results**. The mentors will then get in touch with you.
