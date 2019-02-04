---
title: Implementation and optimisation in ACTS of algorithms exposed in TrackML challenge
layout: gsoc_proposal
project: ACTS
year: 2019
organization: CERN, LAL
---

## Description

Tracking particles at the High Luminosity LHC accelerator will be a major challenge. In short, for each collision of two bunches of protons, approximately 100.000 3D points have to be associated into 10.000 trajectories, approximate arc of helices.
The Tracking Machine Learning challenge (TrackML) took place on Kaggle
from May to August 2018 and on Codalab from October to March 2019. A wealth of track pattern algorithms have been
exposed : some pure
combinatorial using trajectory following, some assisted with Machine Learning, some with unsupervised clustering. Given
that this was a competition, the ultimate algorithm is most likely a combination of good ideas (some being very original) used by different competitors.
ACTS is the C++ tracking tool suite which has been used to simulate the TrackML dataset. This versatile framework also allow reconstruction algorithms to be run.
The goal of this project is to examine a number of TrackML submitted algorithms, to port the most promising ones (two or
three) to ACTS and to build an optimal one using ideas exposed in the two phases of the challenge.

## Task ideas
 * Run some of the algorithms as submitted by the participants.
 * Evaluate the algorithms in terms of quality, speed, uniqueness, difficulty of the implementation
 * Implement in ACTS the data flow which will allow the evaluation (both in term of accuracy and in speed) the performance of the implemented algorithms
 * Implement one of the simplest algorithm submitted (clustering based)
 * Implement the more complex ones
 * Implement blending of algorithms


## Expected results
A suite of efficient tracking reconstruction algorithms implemented in ACTS framework

## Requirements
Experienced with C++ and python

## Mentors
  * [David Rousseau](mailto:rousseau@lal.in2p3.fr)
  * [Moritz Kiehn](mailto:moritz.kiehn@cern.ch)

## Links
  * [ACTS](http://acts.web.cern.ch/ACTS/)
  * [TrackML](https://sites.google.com/site/trackmlparticle/)
  * [Kaggle](https://www.kaggle.com/c/trackml-particle-identification)
  * [Codalab](https://competitions.codalab.org/competitions/20112)
