---
title: Using ROOT in the field of genome sequencing
layout: gsoc_proposal
project: ROOT
year: 2025
difficulty: medium
duration: 350
mentor_avail: June-November
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
* Reproduce the results based on previous comparisons against ROOT master
* Investigate and compare the latest compression strategies used by [Samtools](https://www.htslib.org/) for conversions to BAM, with RAM(ROOT Alignment Maps).
* Explore ROOT's [RNTuple](https://root.cern/doc/v622/md_tree_ntuple_v7_doc_README.html) format to efficiently store RAM maps, in place of the previously used `TTree`.
* Investigate different ROOT file splitting techniques
* Produce a comparison report


## Requirements
* C++ and Python programming
* Familiarity with Git
* Knowledge of ROOT and/or the BAM file formats is a plus.


## Mentors
* [Martin Vasilev](mailto:mvassilev@uni-plovdiv.bg)
* [Jonas Rembser](mailto:Jonas.Rembser@cern.ch)
* [Fons Rademakers](mailto:Fons.Rademakers@cern.ch)


## Links
* [Latest Presentation on GeneROOT](https://indico.cern.ch/event/655464/)
* [ROOT](https://root.cern/)
* [GeneROOT](https://github.com/GeneROOT)
