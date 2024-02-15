---
project: JuliaHEP
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

The [Julia](https://julialang.org) provides a combination of speed, interoperability, ease of use, and flexibility that makes it a very interesting choice for High Energy Physics (HEP) research. It can provide HEP researchers with the high-performance computing capabilities of C++, while still offering the ease of use of high-level languages, making it a powerful tool for HEP research. If the HEP community was adopting Julia as the main programming language, it could immediately benefit from the re-use of a good deal of existing software in the Julia ecosystem (more than 8000 packages) facilitated by the multi-dispatch feature of the language. But, the community has a number of key large software packages written in C++ that would need to interfaced to in order to provide the HEP specific functionality. The development effort invested in these packages is very large, counted on several hundred of person-years, and we need to preserve this investment.

In this context, the [WrapIt](https://github.com/grasph/wrapit/) tool has been developed to automatize the generation of Julia bindings to C++ libraries. It has been used to develop the Julia interface to Geant4, [Geant.jl](https://github.com/JuliaHEP/Geant4.jl), a widely used C++ library in HEP research for simulating the interaction of elementary particles in matter. The popular C++ data analysis framework in HEP research, ROOT, has been partially interfaced to Julia, as an example provided by the WrapIt tool.

This project will consist in a contribution to the effort of providing a Julia interface to HEP C++ libraries. A proposal is discussed in the next session. Other contributions are possible, and the project can be refined together with the mentors taking into account the fields of interest of the candidate.

## Adding ROOT file write support to Julia.

The ROOT framework provides a file format suited to store the large data sets produced in HEP (hundreds of Petabytes of data), in particular at the CERN Large Hadron Collider. It provides a fast access, a structured data organisation with columnar data support, compression, and self-contained data model description. Support for this format is essential for HEP application.

The [UnROOT](https://github.com/JuliaHEP/UnROOT.jl) package, implemented purely in Julia, provides support allows reading the file in ROOT format. Write support is lacking from the Julia ecosystem. Its implementation is more difficult than for the read support. For this reason, the development plan of the UnROOT package is to limit the package for reading files.

We propose to develop a Julia package that will provide ROOT file write support. The package will use as backend the genuine ROOT C++ libraries interface to Julia thanks to CxxWrap and WrapIt. The package will offer a convenient interface to write Julia data into a ROOT file, that can then be read back from other frameworks, both C++-based like the plain C++ ROOT and Python-based like PyROOT and uproot. 

The package will support:

  * Write of columnar data (tables, also known as data frames) from the Julia ecosystem DataFrame or Table types;
  * Row-by-row write of columnar data provided as a set of variables with the contents of the respective table cells;
  * The following cell data type: scalars (Int, Float32, etc..); struct, vectors, and tuples of scalars; struct arrays;
  
It will focus in providing a user-friendly and Julia-like interface. It will be safe, in the sense of preventing segmentation fault in case of bad usage.

 
## Expected results

The expected result is a genuine Julia package that will provide ROOT file format write support to the Julia ecosystem. The packages will be registered in the general Julia repository.

## Evaluation Task

Interested students please contact [Pere](mailto:Pere.Mato@cern.ch) and [Philippe](mailto:philippe.gras@cern.ch) for more details and an evaluation task.

## Requirements

 * For the ROOT file write support project, a fair knowledge of C++ and some experience in Julia is required. Experience with ROOT would be an advantage, as well as some experience of Julia packages such as CxxWrap. In case the candidate would prefer a project focused on a contribution to the WrapIt tool development, a solid knowledge of C++ would be required.

## Mentors
 * **[Pere Mato](mailto:pere.mato@cern.ch)** CERN
 * [Philippe Gras](mailto:philippe.gras@cern.ch) CEA-IRFU

## Links
 * [Geant4](https://geant4.web.cern.ch)
 * [ROOT](https://root.cern.ch)
 * [Interoperability between Julia and other languages](https://github.com/JuliaInterop)
 * [LLVM](https://llvm.org)
 
 *Updated on Feb. 15, 2024*
