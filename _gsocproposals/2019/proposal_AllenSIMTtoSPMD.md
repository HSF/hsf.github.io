---
project: Allen
title: SIMT to SPMD code translation
layout: gsoc_proposal
year: 2019
organization: CERN
---

## Description

At the LHCb detector, bunches of particles collide at a 30 MHz rate,
producing a peak data rate of 40 Tbit/s. A data selection is performed
over these data, in order to record interesting events from a particle
physics standpoint, in a process known as "triggering". The
[Allen](https://gitlab.cern.ch/lhcb-parallelization/Allen) software
framework provides a realization of the first stage of software trigger
of the LHCb reconstruction software for GPUs. The entirety of algorithms
in Allen is written in CUDA following the SIMT programming model, and
are thus restricted to NVIDIA graphics cards hardware. Nevertheless,
LHCb software should also support the baseline x86-64 architecture.

The SPMD programming model allows to write vectorized code on CPUs while
maintaining a regular coding structure. Under the SPMD model, the
programmer writes a program that generally appears to be a regular
serial program, though the execution model is actually that a number of
program instances execute in parallel on the hardware, in vector units.
The [Intel SPMD Program Compiler (ISPC)](https://ispc.github.io/) is a
realization of a compiler utilizing this model that targets primarily
x86 and x86-64 architectures.

The SIMT programming model exposed by CUDA and the SPMD programming
model required by ISPC share many commonalities, making the transition
from one language to another a nuanced translation exercise. The [LLVM
Compiler Infrastructure](https://llvm.org/) provides a modular compiler
and toolchain software infrastructure. LLVM supports compilation of CUDA
code, while ISPC is an open source compiler using the LLVM machinery as
a backend.

The project aims to provide a basic code translation engine from CUDA into
ISPC-understandable code. The student will be provided guidance both
through the LLVM infrastructure, and self-contained examples extracted
from the Allen codebase. The code translation engine would not only be helpful
for the GPU reconstruction under development in LHCb, but for any
existing CUDA code with a simple syntax.

## Tasks

- Convert basic CUDA examples to the SPMD model
- Automatize the conversion with an LLVM code conversion engine
- Generalize the code conversion engine to support the CUDA features required in Allen

## Expected results
Working implementation of a basic code translation engine from CUDA into
ISPC-understandable code using the LLVM machinery.

## Requirements
Compiler knowledge, CUDA, C

## Mentors
  * [Daniel Campora](mailto:dcampora@cern.ch)
  * [Axel Naumann](mailto:axel.naumann@cern.ch)
  * [Gerhard Raven](mailto:gerhard.raven@nikhef.nl)
  * [Niko Neufeld](mailto:niko.neufeld@cern.ch)

## Links
  * [Allen](https://gitlab.cern.ch/lhcb-parallelization/Allen)
  * [ISPC](https://ispc.github.io/)
  * [LLVM](https://llvm.org/)
