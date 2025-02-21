---
title: Integrating Support for Google XLS in HLS4ML
layout: gsoc_proposal
project: ML4EP
year: 2025
organization: CERN
difficulty: medium/high
duration: 350
mentor_avail: Flexible
project_mentors:
  - email: vladimir.loncar@cern.ch 
    organization: CERN
    first_name: Vladimir
    last_name: Loncar
    is_preferred_contact: yes
  - email: dimitrios.danopoulos@cern.ch
    first_name: Dimitrios
    last_name: Danopoulos
    organization: CERN
---

# Description

Google XLS (Accelerated Hardware Synthesis) is an advanced open-source framework for high-level hardware design, offering flexible and efficient synthesis for FPGA and ASIC applications. By integrating XLS into HLS4ML, a framework for translating machine learning models into FPGA-friendly code, we can leverage XLS’s optimizing compiler and domain-specific language to improve resource efficiency, performance, and portability. This integration will enable seamless generation of highly optimized hardware implementations for ML models while maintaining the ease of use that HLS4ML provides.

HLS4ML currently supports traditional HLS tools like Vivado HLS and Intel HLS, but adding XLS can bring further benefits such as better compilation times, improved hardware efficiency, and wider vendor compatibility. This project will focus on developing an interface between HLS4ML and XLS, allowing ML models to be translated into XLS IR and synthesized efficiently.

# Task Ideas

  * Develop a backend in HLS4ML that translates neural network layers into XLS Intermediate Representation (IR).
  * Implement the key ML operations (e.g., matrix multiplications, activations, and pooling) via XLS's DSLX language and map them to HLS4ML operations.
  * Benchmark and compare performance, resource utilization, and synthesis results against existing HLS4ML backends.
  * Extend HLS4ML’s configuration options to allow selection of XLS as a backend, ensuring ease of integration.

# Expected Results

  * A prototype of a backend in HLS4ML supporting XLS-based synthesis.
  * Conversion scripts to map ML operations to XLS IR.
  * Performance evaluation of XLS and existing HLS backends.
  * Documentation and tutorials for using XLS with HLS4ML.

## Requirements
  * Proficiency in Python and C++.
  * Knowledge of hardware and compiler design.
  * Basic familiarity with neural networks.
  * Familiarity with version control systems like Git/GitHub.


## Links
  * [hls4ml documentation](https://fastmachinelearning.org/hls4ml/)
  * [hls4ml Repository](https://github.com/fastmachinelearning/hls4ml)
  * [Google XLS documentation](https://google.github.io/xls/)
  * [Google XLS repository](https://github.com/google/xls)
