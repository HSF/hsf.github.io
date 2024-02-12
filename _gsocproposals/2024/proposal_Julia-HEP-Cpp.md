---
project: HSF
title: Julia interoperating with HEP C++ libraries 
layout: gsoc_proposal
year: 2024
difficulty: high
duration: 350
mentor_avail: May-October
organization:
  - CERN
  - CEA-IRFU
---

## Description
The [Julia](https://julialang.org) provides a combination of speed, interoperability, ease of use, and flexibility that makes it a very interesting choice for High Energy Physics (HEP) research. It can provide HEP researchers with the high-performance computing capabilities of C++, while still offering the ease of use of high-level languages, making it a powerful tool for HEP research. If the HEP community was adopting Julia as the main programming language, it could immediately benefit from the re-use of many existing software in the Julia ecosystem (more than 8000 packages) facilitated by the multi-dispatch feature of the language. But, the community has a number of key large software packages written in C++ that would need to interfaced to in order to provide the HEP specific functionality. The development effort invested in these packages is very large, counted on several hundred of person-years, and we need to preserve this investment.

For example, Geant4 is a widely used C++ library in HEP research for simulating the interaction of elementary particles in matter. Interfacing Julia with the Geant4 library can provide HEP researchers with a convenient way to use the capabilities of Geant4 in their Julia code. Similarly with ROOT, which is a widely used C++ data analysis framework in HEP research. These are in general large software projects with hundreds of C++ classes, unfortunately without a clear separation of a public API and its internal implementation, therefore any wrapping or binding solution based for example on [C++Wrap.jl](https://github.com/JuliaInterop/CxxWrap.jl) would need to be highly automated to generate the wrapper code of these many classes. Initial solutions for this automation exist (e.g. [WrapIt](https://github.com/grasph/wrapit/)) but would need to be fully tested and eventually extended to support all the C++ constructs used in these packages. The automation uses the [LLVM](https://llvm.org) compiler infrastructure to interpret the C++ code and generate the bindings.

The task of this project is the implementation, as automated as possible, of Julia bindings of common C++ HEP packages such as Geant4 and ROOT, in view to make available these packages within the Julia ecosystem and to evaluate their usability and performance. Quite deep knowledge of C++ would be beneficial for understanding the interfaces of these packages, however knowledge of particle physics is not required.

## Task ideas
 * Develop the Julia bindings for the Geant4 simulation toolkit and be able to illustrate its use with examples.
 * Develop the Julia bindings for the ROOT analysis framework simulation and examples.
 * Further develop and enhance the [WrapIt](https://github.com/grasph/wrapit) for the automatic generation of C++ to Julia bindings
 * Register a Julia package with the library with the wrappers and the binaries of the target C++ package to make the deployment as simple as possible.
 * Evaluate the performance and usability these interfaces, and their interoperability with other Julia packages. 

## Expected results
The expected result is a genuine Julia package that provides the functionality of either Geant4 or ROOT to the Julia ecosystem, and this is done in a very sustainable manner to follow the evolution of these packages with minimal effort by automating the wrapper generation as much as possible. 

## Evaluation Task
Interested students please contact [Pere](mailto:Pere.Mato@cern.ch) and [Philippe](mailto:philippe.gras@cern.ch) for more details and an evaluation task.

## Requirements
 * Good knowledge of C++ and some experience in Julia is required. Experience with some of the widely used HEP libraries (e.g. ROOT, Geant4) would be an advantage, as well as some experience of Julia packages such as C++Wrap.

## Mentors
 * **[Pere Mato](mailto:pere.mato@cern.ch)** CERN
 * [Philippe Gras](mailto:philippe.gras@cern.ch) CEA-IRFU

## Links
 * [Geant4](https://geant4.web.cern.ch)
 * [ROOT](https://root.cern.ch)
 * [Interoperability between Julia and other languages](https://github.com/JuliaInterop)
 * [LLVM](https://llvm.org)

