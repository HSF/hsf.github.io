---
title: ROOT Storage of Deep Learning models in TMVA  
layout: gsoc_proposal
project: ROOT
year: 2021
organization:
    - CERN
---

## Description

The Toolkit for Multivariate Data Analysis with ROOT (TMVA) provides a machine learning environment for the processing and evaluation of multivariate classification, both binary and multi-class, and regression techniques targeting applications in high-energy physics. The latest development in TMVA is a fast interference system, with its own intermediate representation of the deep learning model compliant with the ONNX standard. With this new inference system, TMVA aims to provide convenience for users in High Energy Physics in the deployment of their Deep Learning models in a production environment. To facilitate the usage, storage and exchange of these models, TMVA would like to propose a project that would allow the storage of Deep Learning models in the ROOT format, popular in the High Energy Physics community.

## Task ideas and expected results

The candidate will be integrated into the Machine Learning team of the ROOT project, working for the TMVA package. The main task will be to develop the capability to store and read back this intermediate representation describing the trained model in ROOT formats, using the serialisation functionality of ROOT. As a second step, converters from externally trained models, for example Keras h5 files or PyTorch pt files, could be developed. Alternatively, another potential task will be exploring the parsing of ScikitLearn pickle models and converting them to a ROOT format.

The expected result is a working implementation of a new functionality that allows the serialisation of the TMVA intermediate representation of deep learning models into ROOT format, and a converter from external models to this format.

## Requirements
 * C++, familiarity of ML/DL frameworks (Keras, PyTorch, ScikitLearn)

## Mentors
 * **[Anirudh Dagar](mailto:anirudhdagar6@gmail.com)**
 * [Lorenzo Moneta](mailto:Lorenzo.Moneta@cern.ch)
 * [Sitong An](mailto:s.an@cern.ch)

## Links
 * [ROOT](https://root.cern/)
 * [TMVA](https://root.cern/manual/tmva/)
 * [ONNX](https://onnx.ai)
