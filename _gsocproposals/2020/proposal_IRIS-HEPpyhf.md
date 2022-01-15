---
title: pyhf Hardware Acceleration Benchmarking with GPUS and TPUs
layout: gsoc_proposal
project: IRIS-HEP
year: 2020
organization: IllinoisUC
logo: pyhf-logo.png
---

## Description

High Energy Physics analyses are performed with statistical computations to ascertain the compatibility of the reported results with the existing Standard Model.
These computed likelihood fits are performed using tools implemented in [ROOT](https://root.cern.ch/) such as [RooFit](https://root.cern.ch/roofit) and [RooStats](https://root.cern/doc/master/group__Roostats.html).
In many cases, a binned, asymptotic likelihood fit is performed following a mathematical p.d.f. template called [HistFactory](https://cds.cern.ch/record/1456844).
This HistFactory p.d.f. template is per-se independent of its implementation in ROOT and it is useful to be able to run statistical analysis outside of the ROOT, RooFit, RooStats framework.
The [`pyhf`](https://github.com/scikit-hep/pyhf) library is a pure-python implementation of that statistical model for multi-bin histogram-based analysis and its interval estimation is based on the asymptotic formulas of "[Asymptotic formulae for likelihood-based tests of new physics](https://arxiv.org/abs/1007.1727)".
`pyhf` supports modern computational graph libraries such as TensorFlow and PyTorch in order to make use of features such as autodifferentiation and GPU acceleration.

The goal of the project is to develop a benchmarking suite in Python to test and benchmark the performance increase of the hardware accelerated backends on GPUs and TPUs on openly published physics data from LHC experiments [[10.17182/hepdata.89408](https://doi.org/10.17182/hepdata.89408), [10.17182/hepdata.92006](https://doi.org/10.17182/hepdata.92006)].
The benchmarking suite would preferably be written as a [`pytest`](https://docs.pytest.org/en/latest/) module.

## Task ideas

   * Write a hardware acceleration benchmarking suite for the GPU enabled backends (TensorFlow, PyTorch, and JAX) in Python (`pyhf` Issues [301](https://github.com/scikit-hep/pyhf/issues/301), [348](https://github.com/scikit-hep/pyhf/issues/348)).
   * Write comparison plot generation code in Python for the performance of the GPU enabled backends against each other and the CPU backends.
   * Thoroughly document the performance benchmarking in the form of a case study.
   * Evaluate the hardware acceleration test suite using Google TPUs.
   * Profile the `pyhf` codebase to determine where the hardware acceleration is making the largest difference.

## Expected results

By the end of Summer 2020, we would like to have a benchmarking suite written in Python (preferably using `pytest`) that can test and compare the performance of all the `pyhf` computational backends in fitting openly published likelihoods from the LHC.
This will require modularity in the benchmarking suite to allow it to be used on new data.
There is particular interest in also having the student use the benchmarking suite they developed to evaluate the performance of hardware accelerated `pyhf` on GPUs and TPUs, along with detailed documentation and a report for the `pyhf` website.

## Evaluation tasks

Contact the mentors for a task that can be used to evaluate candidates.
Contributing a "good first issue" PR to `pyhf` would be a rather advanced form of evaluation, but would also be an excellent test of how the student would work with the core developer team.

## Requirements

   * Code in Python 3 and adhere to the [Black](https://github.com/psf/black) code style
   * Comfort with switching between Python machine learning frameworks (PyTorch, TensorFlow, JAX, NumPy)
   * Basic understanding of functional minimization (e.g. [`scipy.optimize`](https://docs.scipy.org/doc/scipy/reference/optimize.html), [`minuit`](https://iminuit.readthedocs.io/en/latest/), and autodifferentiation)
   * Basic understanding of hardware acceleration
   * Ability to profile Python code

## Mentors

  * [Matthew Feickert](mailto:matthew.feickert@cern.ch)
  * [Lukas Heinrich](mailto:lukas.heinrich@cern.ch)
  * [Giordon Stark](mailto:giordon.holtsberg.stark@cern.ch)

## Links
  * [pyhf](https://github.com/scikit-hep/pyhf)
  * [IRIS-HEP](https://iris-hep.org)
  * [Scikit-HEP](https://scikit-hep.org)
  * [Openly published likelihoods](https://atlas.cern/updates/atlas-news/new-open-likelihoods)
