---
title: Hist plotting
layout: gsoc_proposal
project: IRIS-HEP
year: 2020
organization: princeton
---

## Description

The [Scikit-HEP](https://scikit-hep.org) project is a collection of several
dozen packages intended to facilitate the use of Python in High Energy Physics
(HEP), started in 2016. One of the major fronts of development is in
histogramming; a majority of HEP analysis is heavily reliant on histograms. To
this end, a new Python package was introduced for histogramming in Scikit-HEP,
boost-histogram, developed in close collaboration with the author of the Boost
C++ libraries' Histogram package. This package is intended to be a core package
for histogramming with no dependencies, much like Numpy is for data
structures.

Scikit-HEP developers are preparing an implementation of an analyst friendly
package, called "hist", built on top of boost-histogram and providing plotting,
saving/loading, and other commonly expected histogramming features. This package will allow a
wider range of dependencies and features not admissible in the core package. Two
other packages have already been developed that will help support Hist; one is Aghast,
a histogram conversion library that can convert formats and save histograms; and the other
is mplhep, a plotting helper library for matplotlib that can be integrated with the
Histogram objects being produced by Hist/boost-histogram.

The goal of this project will be to assist in the development of Hist, building
on top of the three existing libraries and enabling common analysis tasks to be
performed with a reasonable amount of readable code.

## Task ideas

   * Assist in developing a Hist class that associates meanings to axis
     metadata (names, units). A draft of this is already present in the Coffea
     framework.
   * Provide common analysis shortcuts. Possibly query users on Scikit-HEP
     communication channels for common needs, look over existing histograms in
     analyses to identify common tasks.
   * Work on integration with mplhep, a matplotlib HEP library also part of
     Scikit-HEP and under active development. Develop useful shorthands for
     common plots, similar to Pandas's dataframe.plot object.
   * Work on integration with Aghast, a histogram conversion library for
     loading/saving histograms also part of Scikit-HEP.
   * Enable common statistical tasks, such as efficiency calculations, to be
     performed without extensive user code.
   * Write documentation for above features.

## Expected results

By the end of the summer, Hist should be able to perform several common
plotting tasks easily, it should be able to save/load basic histograms, and it 
should be able to perform a few common statistical operations.

## Requirements

   * General software engineering skills; well-organized coding
   * Good familiarity with Python
   * Familiarity with plotting, ideally with matplotlib

## Evaluation tasks

Contact the mentors for a task that we'll use to evaluate candidates.

## Mentors

  * [Henry Schreiner](mailto:henryfs@princeton.edu) (primary)
  * [Jim Pivarski](mailto:pivarski@princeton.edu) (secondary)

## Links

  * [Scikit-HEP](https://scikit-hep.org)
  * [Boost.Histogram C++](https://www.boost.org/doc/libs/release/libs/histogram/doc/html/index.html)
  * [boost-histogram for Python](https://boost-histogram.readthedocs.io/en/latest/)
  * [Aghast](https://github.com/scikit-hep/aghast)
  * [mplhep](https://github.com/scikit-hep/mplhep)
