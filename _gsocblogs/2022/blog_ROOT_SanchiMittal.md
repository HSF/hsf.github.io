---
project: ROOT - Machine Learning Developments
title: Batch Generator for training machine learning models
author: Sanchi Mittal
photo: blog_authors/SanchiMittal.jpeg
date: 02.09.2022
year: 2022
layout: blog_post
logo: ROOT-logo.png
intro: |
  Develop a generator in C++ and Python to read data from the ROOT I/O and input them to the Python machine learning tools such as Tensorflow/Keras and PyTorch.
---

# Sanchi's Final Evaluation Blog for GSoC 2022

Through this blog, I'll be going over the work that I have done as a contributor
for GSoC 2022 program with CERN-HSF under the project "ROOT - Machine Learning
Developments : Batch Generator for training machine learning models".

<div align="center">
![CERN]({{ site.baseurl }}/images/CERN-HSF-GSoC-logo.png){:height="100px"} Google Summer of Code 2022
</div>

## Introduction

I'm a recent Computer Science and Engineering graduate, who'd always had a keen
sense of amazement for Physics and Science in general. That's why, it was like a
dream come true when I got this opportunity via Google Summer of Code to make a
contribution towards the High Energy Physics experimentations and the study of
the universe, while utilising the skills and knowledge of my domain, that is
Computer Science.

## About the Project Goals

Toolkit for Multivariate Analysis (TMVA) is a multi-purpose machine learning
toolkit integrated into the ROOT scientific software framework, used in many
particle physics data analysis and applications. Since it is part of the ROOT
data analysis framework, it comes with an automatically generated Python
interface, which closely follows the C++ interface. The goal of this project is
to develop a generator in C++ and Python to read data from the ROOT I/O and
input them to the Python machine learning tools such as Tensorflow/Keras and
PyTorch. The main aim of the generator is to efficiently input data from the
ROOT I/O system to train machine learning models, and keep in memory only the
data required to train a batch of events and not all the data set.

- **Goals**
  - Development of a Python generator for getting the data directly from a ROOT
    TTree using PyROOT interfaces with Documentation
  - Integration with ROOT RDataFrame with Documentation
  - Development of tests and tutorial example

## Community Bonding Period

During the community bonding, I made sure to plan out the to-do's for the
project and discuss, modify and reiterate over my project ideas. I familiarized
myself with ROOT, TMVA, RDataFrame, RTensor, TTree and other needed data
structures and tools via tutorials, to get a headstart before the coding period.
After finalizing, I communicated the revised expected project goals and timeline
to my mentors via a powerpoint presentation, and it was finalized to begin the
coding.

## Implementing the Prototype

It has been evident while working that this project for developing the Batch
Generator is something experimental and would require researching into different
approaches before implementing or directly packaging it into TMVA. Thus, I have
been working in a stand-alone repository over
[here](https://github.com/tmvadnn/tmva-batch-generator), where I made pull
requests for the experimental prototype.

1.  The first aim was to have a basic batch generator, for which I started with
    a for-loop in Python. This turned out to be both memory and
    time-inefficient.
    - [Link to Code](https://github.com/SanchiMittal/root/commit/8b63ff3d13acc385df064b970a84a198f69ba336)
2.  In the second approach, I decided to write a functor for the batch
    generator, while replacing the for-loop using the RTensor::Slice method.
    This made it time-efficient, but definitely data-copying still left it
    memory-inefficient.
    - [Link to Code](https://github.com/tmvadnn/tmva-batch-generator/pull/2/commits/34c6fd5e86dae48a2101ea4219b113e47c4729fb)
3.  In the third approach, I have replaced this slice method, removing the extra
    copying actions from the memory. I discovered that initializing the RTensor
    directly as a 'view' would help us achieve this goal.
    - [Link to Code](https://github.com/tmvadnn/tmva-batch-generator/pull/4/commits/94dcf93b8ee9f97b434fcacc1663a5c2171cbb9a)
4.  The next approach is where I have further optimized the memory operations by
    replacing the AsTensor() method by a template functor, such that an RTensor
    can be created out of a TTree / RDataframe without the need to copy the data
    while creation of the batches.
    - [Link to Code](https://github.com/tmvadnn/tmva-batch-generator/pull/4/commits/93ec68c86f5e01be01eee2e84f77cf228a3ba31d)
5.  As a next step, I have eliminated the recursive nature of the generator
    template functor using an interesting approach of using column sequence as
    parameter pack, for which I have added a separate dataloader for conversion
    from RDataFrame to RTensor.
    - [Link to Code](https://github.com/tmvadnn/tmva-batch-generator/pull/4/commits/536ebf315c4187c461dd50a3f9a6bfb36b4d0907)
6.  Additional useful features like random_shuffle and drop_last for the
    DataLoader are also added that can be found below.
    - [Link to Code](https://github.com/tmvadnn/tmva-batch-generator/pull/4/commits/536ebf315c4187c461dd50a3f9a6bfb36b4d0907)
7.  After a satisfactory C++ implementation, I have integrated a generator
    header with a Python batch generator for creating numpy batches from
    RDataFrame.
    - [Link to Code](https://github.com/tmvadnn/tmva-batch-generator/pull/4/commits/3e4bbc77f80b407af6f8dedfa1abf57634dd706c)
8.  Using the Python Batch Generator, I have created a tutorial with Keras
    classification model. For more improvements and most updated versions the
    following link can be followed:
    - [Link to Code](https://github.com/tmvadnn/tmva-batch-generator/blob/experimental/prototype_experimental/bg_keras_exp.py)

## Future Scope

It has been a great learning experience while working on the batch generator
project. I plan on continuing to contribute for the improvement of this project
in the future as well, some of the points under future scope are listed below:

- Further optimization of the memory intensive code wherever possible.
- Facilitating multi-threading over GPUs.

## Conclusion

I would like to express my gratitude to my mentors **Lorenzo Moneta, Omar
Zapata, Sanjiban Sengupta and Sitong An**, for they have been extremely
supportive with guidance and helped me put my efforts into the right direction,
since the beginning of the program.

You can find my final GSoC submission
[here](https://github.com/tmvadnn/tmva-batch-generator/wiki). Also, I have been
documenting my GSoC 2022 journey with CERN-HSF via blogs that can be found over
[here](https://sanchimittal.hashnode.dev/).

**\- Sanchi**
