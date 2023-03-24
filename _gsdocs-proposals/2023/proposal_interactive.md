---
title: Improving Analysis Tool Documentation for the HSF
layout: gsdocs_proposal
project: analysis
year: 2022
organization:
---

## Description of project idea

Particle physics relies heavily on open-source codes that compute key quantities for both theory and experiment. Often such codes have been developed for many years, with early documentation rendered incorrect or incomplete by later developments. Key user-facing information can be very difficult to find (e.g. in automatically generated code-interface documentation). It can be difficult for new physics-oriented users and contributors to get involved: the docs that exist are more for the developers and often assume too much technical prowess.

We seek to advance the documentation in the area of interactive analysis, both in the context of C++ and support for C++/Python interoperability.  Our intent is to build the sort of documentation that enables user engagement while being easy to update as our codes continue to evolve and improve.

### Interactive Analysis

HEP researchers have developed several unique software technologies in the area of data analysis. Over the last decade we developed an interactive, interpretative C++ interpreter (aka REPL) as part of the ROOT data analysis project. We invested a significant effort to replace CINT, the C++ interpreter used until ROOT5, with a newly implemented REPL based on LLVM – Cling. Cling is a core component of ROOT and has been in production since 2014. Cling is also a standalone tool, which has a growing community outside of our field. It is recognized for enabling interactivity, dynamic interoperability and rapid prototyping capabilities for C++ developers. For example, if you are typing C++ in a Jupyter notebook you are using the xeus-cling Jupyter kernel. 

We are in the midst of an important project to address one of the major challenges to ensure Cling’s sustainability and to foster that growing community: moving most parts of Cling into LLVM. Since LLVM version 13 we have released a version of Cling called Clang-Repl within LLVM itself. We subsequently focused on the language interoperability capabilities of Cling. One user facing application of our libInterOp, together with Clang-Repl, is Xeus-Clang-Repl, which is a replacement for xeus-cling using these new codes. As we advance the implementation and generalize its usage we aim for improving the overall documentation experience in the area of interactive programming in various environments.

This project will audit the existing documentation for the
Clang-Repl (interactive C++),
Xeus-Clang-Repl (notebook-based C++ and Python platform) and
libInterOp (bridging automatically C++ and Python).
We aim to Identify gaps in the information or presentation from the point-of-view of new, science-oriented users.

## Detailed project description
* [Please see our full proposal draft here](GoogleSeasonOfDocsHSF.pdf)

## Mentors
* David Lange [David.Lange@cern.ch](mailto:David.Lange@cern.ch) Princeton University
* Vassil Vassilev [Vassil.Vassilev@cern.ch](mailto:Vassil.Vassilev@cern.ch) Princeton University

