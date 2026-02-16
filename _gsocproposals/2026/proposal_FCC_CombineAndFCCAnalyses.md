---
title: Integration of Combine with FCCAnalyses
layout: gsoc_proposal
project:
  - FCC
year: 2026
organization:
  - CERN
  - MIT
difficulty: medium
duration: 175
mentor_avail: June-October
project_mentors:
  - email: juraj.smiesko@cern.ch
    first_name: Juraj
    last_name: Smiesko
    organization: CERN
    is_preferred_contact: yes
  - email: jan.eysermans@cern.ch
    first_name: Jan
    last_name: Eysermans
    organization: MIT

---

## Description

[Combine](https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit) (also
known as CMS Combine) is a domain-agnostic statistical tool designed for High
Energy Physics that facilitates model building, statistical testing, and result
validation. Originally developed to search for the Higgs boson, it has since
become the standard tool for a wide range of measurements.  It enables
physicists to compare expected observation models against experimental data to
perform tasks such as claiming particle discoveries, setting new physics limits,
and measuring cross sections. The package is versatile enough to handle a broad
range of HEP workflows, including simple counting experiments, unfolded
measurements, and complex Effective Field Theory (EFT) fits.

[FCCAnalyses](https://hep-fcc.github.io/FCCAnalyses/) is a high-performance
Python/C++ framework designed for physics reach studies and detector
optimizations of the Future Circular Collider, implemented within the Key4hep
ecosystem. Built upon ROOT's RDataFrame, it enables efficient, multi-threaded
processing of EDM4hep datasets, allowing physicists to define complex event
selections and calculate observables with minimal overhead. The framework acts
as a bridge between reconstructed data and final statistical inputs, providing a
standardized set of analysis building blocks, ranging from the calculation of
simple physics variables to jet clustering or flavor tagging.

This project aims to streamline the transition from event selection to
statistical inference within the Future Circular Collider (FCC) analysis
software ecosystem. Currently, FCCAnalyses excels at processing EDM4hep events
into histograms; however, performing statistical fits often requires manual,
error-prone translation into external tools. This project will develop a native
interface to Combine, allowing users to interact with the tool through an
integrated workflow. By automating the underlying generation of datacards and
workspaces, this interface will enable seamless limit setting, significance
tests, and precision measurements.


## Expected Results and Milestones

- Familiarization with the current Key4hep packaging processes
- Packaging of Combine within the Key4hep stack
- Collection of reference physics analyses for benchmarking
- Validation and stability testing of the reference analyses results
- Design of the Combine integration with the FCCAnalyses framework
- Implementation of the integration
- Design of tests for the integration in FCCAnalyses


## Requirements

- C++ programming skills
- Working knowledge of the CMake build system
- Proficiency in Python
- Familiarity with the Linux operating system
- Interest in scientific software and high-energy physics

## AI Policy

AI assistance is allowed for this contribution. The applicant takes full
responsibility for all code and results, disclosing AI use for non-routine tasks
(algorithm design, architecture, complex problem-solving). Routine tasks
(grammar, formatting, style) do not require disclosure.


## How to Apply

Write an email to the mentors with a brief introduction of your interests and
background. Please include "gsoc26" in the subject line. The mentors will
provide you with a small evaluation task afterwards.


## Resources

- [FCCAnalyses](https://hep-fcc.github.io/FCCAnalyses/)
- [FCC Software](https://fccsw.web.cern.ch/)
- [Key4HEP Documentation](https://key4hep.web.cern.ch/)
- [Combine Documentation](https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/)
