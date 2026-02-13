---
title: Clad as a first-class gradient engine in LibTorch
layout: gsoc_proposal
project: Clad
year: 2026
difficulty: medium
duration: 350
mentor_avail: June-October
organization:
  - CompRes
project_mentors:
  - email: vvasilev@cern.ch
    first_name: Vassil
    last_name: Vassilev
    is_preferred_contact: yes
    organization: Princeton University
  - email: david.lange@cern.ch
    first_name: David
    last_name: Lange
    organization: Princeton University
---

## Description

This project will design, implement, benchmark, and integrate a proof-of-concept that uses Clad (compiler-based automatic differentiation) as a first-class gradient engine in LibTorch (the C++ API of PyTorch). The goal is to demonstrate how ROOT users can run high-performance, pure-C++ machine-learning training and inference pipelines, without relying on Python. The project will result in a working prototype that integrates Clad-generated backward routines into LibTorch via `torch::autograd::Function` or custom ATen operators.

Recent efforts have extended the ROOT framework with modern machine-learning capabilities. In particular, a ROOT Users Workshop 2025 contribution by Meyer-Conde et al. demonstrates the use of LibTorch directly inside ROOT for gravitational-wave data analysis [[1]](https://indico.cern.ch/event/1505384/contributions/6706597). Their “ROOT+” prototype library augments ROOT with advanced features such as complex tensor arithmetic on CPU/GPU and modern I/O mechanisms (HTTP, Kafka), while relying on LibTorch for ML training and inference. In practice, this enables ROOT to load and execute neural networks (via ONNX or LibTorch) entirely in C++, and to combine them seamlessly with ROOT’s data-processing tools such as RDataFrame and TMVA, all within a single environment.
In parallel, recent work in the Compiler Research community has demonstrated that Clad-generated gradients can match and even outperform PyTorch autograd on CPU when carefully optimized [[2]](https://compiler-research.org/blogs/gsoc25_rohan_final_blog). These results motivate a deeper exploration of compiler-driven automatic differentiation as a backend for machine learning frameworks. Building on both efforts, this project will culminate in a ROOT integration demo (for example, a simplified gravitational-wave analysis workflow) and a reproducible benchmarking suite comparing Clad-based gradients with PyTorch autograd for realistic HEP and GW workloads.

This project is expected to deliver tangible performance and usability benefits for machine-learning workflows in ROOT. By offloading gradient computation to Clad’s compiler-generated routines, meaningful speedups are expected for CPU-bound training workloads; prior results report speedups over PyTorch autograd on CPU [[2]](https://compiler-research.org/blogs/gsoc25_rohan_final_blog). This makes the approach particularly attractive for offline HEP and gravitational-wave analyses, where CPU efficiency is often a limiting factor. In addition, the project will enable fully native C++ machine-learning workflows in ROOT, allowing users to define, train, and evaluate models without Python dependencies and to integrate ML tightly with existing C++ analysis code, ROOT I/O, and data pipelines. The Clad-enhanced LibTorch backend will naturally complement ROOT’s existing ML ecosystem including TMVA, SOFIE, ONNX-based inference, and RDataFrame providing a flexible “best-of-both-worlds” solution that combines modern deep-learning frameworks with ROOT’s mature analysis infrastructure. Beyond the immediate prototype, this work will establish a solid foundation for future research on compiler-driven optimizations such as kernel fusion, reduced memory traffic, and eventual GPU acceleration.

## Expected Results

* Create a small C++ demo where a simple neural network is defined (e.g. MLP) and use Clad to generate its derivative functions. Integrate this with LibTorch by wrapping the Clad-generated gradient code as a custom `torch::autograd::Function` or operator. This follows the strategy outlined in the Clad-PyTorch project. The result is a model that uses LibTorch tensors for forward, but Clad’s code for backward.
* Measure training (forward + backward) performance on CPU for representative tasks (e.g. MNIST or a simple GW signal classification). Compare Clad-derived gradients vs PyTorch autograd. Focus on performance: optimize memory layout and avoid dynamic allocations to maximize throughput.
* Adapt the working prototype into the ROOT framework. For example, incorporate it into a ROOT macro or plugin so that one can run C++ ML code under root.exe or in PyROOT. Provide examples using ROOT’s data structures (TTrees, RDataFrame) feeding into the Clad-empowered model. Investigate loading pretrained models (via ONNX or TorchScript) and whether Clad can backpropagate through them.

## Requirements

* Automatic differentiation
* Parallel programming
* C++ programming
* Experience with LibTorch is a plus

## Links
* [Repo](https://github.com/vgvassilev/clad)

## AI Policy

AI assistance is allowed for this contribution. The applicant takes full responsibility for all code and results, disclosing AI use for non-routine tasks (algorithm design, architecture, complex problem-solving). Routine tasks (grammar, formatting, style) do not require disclosure.

## How to Apply

In addition to reaching out to the mentors by email, prospective candidates are required to complete [this form](https://forms.gle/AYgrJthYCRmBwwFL8)
