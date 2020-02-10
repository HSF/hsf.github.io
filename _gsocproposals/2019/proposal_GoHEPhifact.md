---
title: Go-HEP/hifact - Create a HistFactory compatible Go package for statistical models
layout: gsoc_proposal
project: GoHEP
year: 2019
organization:
  - CERN
  - LPC-Clermont
---

# Description

A large fraction of statistical models within HEP can be expressed through a flexible, declarative template, `HistFactory`, for binned densities of observables.
Originally implemented only for `ROOT` and `RooStats`, `HistFactory` has recently been re-implemented based on the scientific python packages in order to make use of auto-differentiation and hardware acceleration via an integration with Machine Learning tensor libraries such as TensorFlow and PyTorch.

The Go scientific ecosystem is lacking such a facility.

During this GSoC project, you will work on implementing a similar library and class of models in Go using Machine Learning libraries such as `Gorgonia`.

## Tasks

We propose the following steps:

 * Implement missing array computation (_e.g._ `einsum`) in Go ML libraries,
 * Import/export models from/to XML
 * Import models from ROOT
 * Implement HistoSys, OverallSys and ShapeSys
 * Implement NormFactor, ShapeFactor and StatError
 * Implement Multiple Channels
 * Implement Luminosity Uncertainty
 * Implement multiple backends:
   * [Gorgonia](https://gorgonia.org)
   * [Gonum/optimize](https://godoc.org/gonum.org/v1/gonum/optimize)

## Expected results

A package that creates statistical models for multi-bin histogram-based analyses, written in [Go](https://golang.org).

## Requirements

- Go
- Python
- Git
- Machine Learning

## Mentors

  * [Lukas Heinrich](mailto:lukas.heinrich@cern.ch)
  * [Sebastien Binet](mailto:binet@cern.ch)

## Links

  * [ROOT](https://root.cern)
  * [HistFactory](https://github.com/root-project/root/tree/master/roofit/histfactory/doc)
  * [pyhf](https://scikit-hep.org/pyhf/)
  * [Go](https://golang.org)
  * [Go-HEP](https://go-hep.org)
  * [Gonum](https://gonum.org)
  * [Gorgonia](https://gorgonia.org)
