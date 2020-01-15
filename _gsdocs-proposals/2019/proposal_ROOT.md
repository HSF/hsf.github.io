---
title: Wonderful ROOT Documentation
layout: gsdocs_proposal
project: ROOT
year: 2019
organization:
 - CERN
---

## Description

[ROOT](https://root.cern) [1] [2] is *the* big data analytics tool used by virtually everyone
in high energy physics, at CERN and world-wide, to store (more than 1
exabyte), statistically analyze and visualize physics data. ROOT is
LGPL'ed (2.1 or later); it is written in C++ with dynamic Python
bindings sometimes aided by explicit "pythonizations". Due to its
capabilities and performance it is also used in industry - but because
much of ROOT's documentation is physics-oriented we make it more
difficult than necessary for non-physicists to pick up ROOT.

ROOT's documentation mainly consists of its [web page](https://root.cern) [1], its [users' guide](https://root.cern/guides/users-guide) [3], reference pages for its [C++ interfaces](https://root.cern/doc/master/) [4], and [tutorials](https://root.cern/doc/master/group__Tutorials.html) [5].

We are preparing a new web site based on [Jekyll](https://jekyllrb.com/) [6] to be released this
year. We are looking to improve ROOT's introduction for non-physicists
to make it more accessible; to streamline the web site to enable quick
access to documentation resources; and to learn how to systematically
improve our reference guide.

## Tasks

Possible tasks might include:

- Review of existing documentation: critique of the clarity of roles and
structure of the different elements (web site, users' guide, C++ reference)
- Creation of a compact, non-physics oriented introduction for the new
web site ("why ROOT?")
- Rewrite of the introduction in the users' guide
- Rewrite of the documentation for one of the most commonly used *old*
ROOT interfaces [7] [8] [9], also to demonstrate to the ROOT team how to
do this well for the old interface style
- Rewrite of the documentation for one of the most commonly used modern
ROOT interfaces [10] [11] [12], also to demonstrate to the ROOT team how
to do this well for the new interface style


## Related material

- [1] [Main Web page](https://root.cern)
- [2] [Github project](https://github.com/root-project/)
- [3] [User's Guide](https://root.cern/guides/users-guide)
- [4] [Developer's Guide (C++ Interfaces)](https://root.cern/doc/master/)
- [5] [Tutorials](https://root.cern/doc/master/group__Tutorials.html)
- [6] [Jekyll](https://jekyllrb.com/)
- [7] [Old interfaces, example 1](https://root.cern/doc/master/classTH1.html)
- [8] [Old interfaces, example 2](https://root.cern/doc/master/classTTree.html)
- [9] [Old interfaces, example 3](https://root.cern/doc/master/classTFormula.html)
- [10] [New interfaces, example 1](https://root.cern/doc/master/classROOT_1_1RDataFrame.html)
- [11] [New interfaces, example 2](https://root.cern/doc/master/classROOT_1_1Experimental_1_1RHist.html)
- [12] [New interfaces, example 3](https://root.cern/doc/master/classROOT_1_1Experimental_1_1RPad.html)

## Mentors
- [Axel Naumann](mailto:axel@cern.ch), CERN
- [Olivier Couet](mailto:Olivier.Couet@cern.ch), CERN
- [Stephan Hageboeck](mailto:stephan.hageboeck@cern.ch), CERN
- [Javier Cervantes Villanueva](mailto:javier.cervantes.villanueva@cern.ch), CERN
