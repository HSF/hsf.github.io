---
title: Implementation of Quantum Machine Learning to Perform High Energy Physics Analysis at the LHC
layout: gsoc_proposal
project: QMLHEP
year: 2020
organization:
   -Wisconsin
   -Alabama
---

# Description
The ambitious [HL-LHC](https://hilumilhc.web.cern.ch) program will require enormous computing resources in the next two decades. New technologies are being sought after to replace the present computing infrastructure. A burning question is whether quantum computer can solve the ever growing demand of computing resources in High Energy Physics (HEP) in general and physics at [LHC](https://home.cern/science/accelerators/large-hadron-collider) in particular. Our goal here is to explore and to demonstrate that Quantum Computing can be the new paradigm (Proof of Principle).

Discovery of new physics requires the identification of rare signals against immense backgrounds. Development of machine learning methods will greatly enhance our ability to achieve this objective. However, with this ever-growing volume of data in the near future, current machine learning algorithms will require large computing resources and excessive computing time to achieve good performance. Quantum Computing in Qubit platform, where qubits are used instead of bits in classical computer, has the potential to improve the time complexity of classical algorithms.

With this project we seek to implement Quantum Machine Learning methods for LHC HEP analysis based on Google OpenFermion framework (“OpenFermion is an open source library for compiling and analyzing quantum algorithms to simulate fermionic systems”). This will enhance the ability of the HEP community to use Quantum Machine Learning methods. In addition, if possible, we also would like to develop a common QML interface for HEP which can support different quantum frameworks such as OpenFermion and qisikit.


## Task ideas and expected results
  * Implement a Quantum Variational method or a Quantum Neural Network method based on Google OpenFermion framework.
  * Apply the quantum machine learning method to one or two of the LHC flagship physics channels (e.g. double-Higgs production). Compare the quantum machine learning performance to the classical machine learning performance.
  * (Optional or partly) Implement a QML interface for HEP which can support different quantum frameworks such as OpenFermion and qisikit.


## Requirements 
  * Solid knowledge of machine learning and deep learning
  * Solid knowledge of quantum machanics.
  * Familiarity with c/c++
  * Strong python skills


## Mentors
  * [Wen Guan](mailto:wen.guan@cern.ch) University of Wisconsin-Madison
  * [Shaojun Sun](mailto:shaojun.sun@cern.ch) University of Wisconsin-Madison
  * [Chen Zhou](mailto:chen.zhou@cern.ch) University of Wisconsin-Madison
  * [Sergei V. Gleyzer](mailto:sergei@cern.ch) University of Alabama
  
## Links
  * [HL-LHC](https://hilumilhc.web.cern.ch)
  * [LHC](https://home.cern/science/accelerators/large-hadron-collider)
  * [OpenFermion](https://github.com/quantumlib/OpenFermion)
