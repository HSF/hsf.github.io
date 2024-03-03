---
title: Using ROOT in the field of genome sequencing
layout: gsoc_proposal
project: ROOT
year: 2024
organization: 
  - CERN
  - CompRes
---

## Description

The [ROOT](https://root.cern/) is a framework for data processing, born at CERN,
at the heart of the research on high-energy physics. Every day, thousands of
physicists use ROOT applications to analyze their data or to perform
simulations. The ROOT software framework is foundational for the HEP ecosystem,
providing capabilities such as IO, a C++ interpreter, GUI, and math
libraries. It uses object-oriented concepts and build-time modules to layer
between components. We believe additional layering formalisms will benefit ROOT
and its users.

ROOT has broader scientific uses than the field of high energy physics. Several
studies have shown promising applications of the ROOT I/O system in the field
of genome sequencing. This project is about extending the developed capability
in [GeneROOT](https://github.com/GeneROOT) and understanding better the
requirements of the field.


## Expected results
* Reproduce the results from previous comparisons against the ROOT master
* Investigate changing the compression strategies
* Investigate different ROOT file splitting techniques
* Produce a comparison report


## Requirements
C++, Python, Git, knowledge of ROOT or the BAM file formats is a plus.


## Mentors
  * [Martin Vasilev](mailto:mvassilev@uni-plovdiv.bg)
  * [Alexander Penev](mailto:alexander.p.penev@gmail.com)
  * [Vassil Vassilev](mailto:Vassil.Vassilev@cern.ch)


## Links
  * [ROOT](https://root.cern/)
  * [GeneROOT](https://github.com/GeneROOT)
