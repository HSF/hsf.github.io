---
title: MCnet/Rivet - Modern plotting machinery for the LHC's MC event analysis tool
layout: gsoc_proposal
project: MCnet
year: 2021
organization:
  - UofGlasgow
  - CERN
---

# Description

Rivet is a software package for performing data analysis on simulated particle
collision events like those in the Large Hadron Collider. Analyses of real data
have to deal with the effects of the giant, complex particle detectors that
surround the beam interaction points, which are expensive to simulate, but use
of statistical techniques allows much faster methods to be employed for testing
theory models against data measurements. Rivet is the LHC's principle tool for
such lightweight model testing, using events simulated using Monte Carlo (MC)
methods. There are currently more than 1000 analysis routines registered on the
Rivet platform.

Visualisation of Rivet's output has been performed since project inception by a
set of Python scripts which generate LaTeX/pstricks graphics commands to draw
axes, error bands, data series, etc. This output is high-quality and suitable
for use in physics publications, but it is slow, and sometimes error-prone due
to the LaTeX backend and its sensitivities to deployment platforms. This project
will focus on designing and implementing a replacement for this system, based on
modern rendering technologies while preserving output quality.


## Task ideas

This project will involve a mixture of system design and implementation. The
ideal replacement for the existing plotting system will cast Rivet's data into a
platform-agnostic format which can then be rendered for presentation via
multiple frameworks, or for example in multiple styles suitable for different
contexts. These target platforms will include both publication-quality and
talk-quality plot styles, and Web-based interactive plotting. This data-flow
will also incorporate a single coherent treatment of data combination, for
example combination of multiple "variation" histograms into a single data series
with a structured uncertainty band. We envisage that the first target renderer
will be the Python matplotlib library.


## Expected results

 * design of a new data-flow for Rivet analysis histograms, performing semantic
   combinations of data objects (to create ratios, uncertainty bands, etc.),
   and export to multiple rendering targets with minimal code duplication;
 * building a first target renderer to publication-quality and presentation-quality
   matplotlib outputs, in particular handling MathText/LaTeX symbol-table completeness issues;
 * reviewing and recommending other rendering platforms for Web-based visualisation.


## Requirements

 * Python
 * matplotlib
 * git


## Mentors

 * [Andy Buckley](mailto:andy.buckley@cern.ch)
 * [Christian Bierlich](mailto:xxxxx@cern.ch)


## Links

 * [Rivet](https://rivet.hepforge.org)
 * [YODA](https://yoda.hepforge.org)
