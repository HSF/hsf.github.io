---
title: Improving Analysis Tool Documentation for the HSF
layout: gsdocs_proposal
project: analysis
year: 2022
organization:
---

## Description of project idea

Particle physics relies heavily on open-source codes that compute key quantities for both theory and experiment. Often such codes have been developed for many years, with early documentation rendered incorrect or incomplete by later developments. Key user-facing information can be very difficult to find (e.g. in automatically generated code-interface documentation). It can be difficult for new physics-oriented users and contributors to get involved: the docs that exist are more for the developers and often assume too much technical prowess.

We seek to advance the documentation in two areas of HEP research: interactive analysis based on C++; and reinterpretation of analysis results. Our intent is to build the sort of documentation that enables user engagement while being easy to update as our codes continue to evolve.

### Interactive Analysis

HEP researchers have developed several unique software technologies in the area of data analysis. Over the last decade we developed an interactive, interpretative C++ interpreter (aka REPL) as part of the ROOT data analysis project. We invested a significant effort to replace CINT, the C++ interpreter used until ROOT5, with a newly implemented REPL based on LLVM – Cling. Cling is a core component of ROOT and has been in production since 2014. Cling is also a standalone tool, which has a growing community outside of our field. It is recognized for enabling interactivity, dynamic interoperability and rapid prototyping capabilities for C++ developers. For example, if you are typing C++ in a Jupyter notebook you are using the xeus-cling Jupyter kernel.
We are in the midst of an important project to address one of the major challenges to ensure Cling’s sustainability and to foster that growing community: moving most parts of Cling into LLVM. Since LLVM version 13 we have a version of Cling called Clang-Repl. As we advance the implementation and generalize its usage we aim for improving the overall documentation experience in the area of interactive C++.

### Reinterpretation

“Reinterpretation” codes aim to reuse data to make new statements about fundamental physics. These codes are meant for wide use in the physics community, but for that to happen much better user-facing documentation needs to be created. We will focus on improvements to the Rivet and Gambit projects, two largely C++ physics applications for reinterpretation, which require a range of technical skills -- from command-line Unix to C++ programming -- in order to get the most from their capabilities.


## Detailed project description
* [Please see our full proposal draft here](./GoogleSeasonOfDocsHSF.pdf)

## Mentors
* David Lange [David.Lange@cern.ch](mailto:David.Lange@cern.ch) Princeton University
* Vassil Vassilev [Vassil.Vassilev@cern.ch](mailto:Vassil.Vassilev@cern.ch) Princeton University
* Andy Buckley [andy.buckley@cern.ch](mailto:andy.buckley@cern.ch) University of Glasgow

