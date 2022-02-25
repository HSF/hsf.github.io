---
title: Interfacing PODIO to Julia
layout: gsoc_proposal
project: HSF
year: 2022
difficulty: medium
duration: 175
mentor_avail: June-September
organization:
    - CERN
    - DESY
---

# Description

<div style="text-align:center; padding:25px; float:right">
<img src="{{ '/images/others/julia.png' | relative_url }}" alt="Julia Logo" width="100px" />
</div>

Currently in high-energy physics (HEP) there are [two main languages
used][SCRoundtable]: **C++** for numerically intensive code, where execution
speed is paramount; and **Python**, for interactivity and ease of development
(often used as 'glue' between high-performance code modules). Recently there has
been [increasing interest][SCRoundtable] in [**Julia**][julialang] as an
alternative/additional language for HEP. This could offer the convenience
features of Python, but the optimal runtime speed of C++
([Julia in HEP Paper][JuliaHEPPaper], [Julia HEP Github][JHEPGH]).

In order to continue this investigation, this project will interface the data model library
PODIO with Julia. This will allow to read existing data files into a Julia program.

##  PODIO

PODIO is a data-model library based on the idea of representing information as plain-old-data (PODs) 
instead of using a deep object-oriented model. This allows for better performance and interoperability.
Data models are defined by a dedicated YAML-syntax and the corresponding code is auto-generated. So far 
both C++ and Python are supported.

## Task ideas and expected results

The task is to create a code generator to add support for Julia as end-user language, and to carry out 
some basic performance checks to compare the different language interfaces.

## Skills

Some prior experience with Julia would be highly desirable, but 
programming skills in C++ and Python should enable the candidate to learn Julia
sufficiently quickly for the project.

## Evaluation Task

The evaluation task comprises of manually translating a simple data model into a Julia representaiton. For details please contact the mentors.

If the candidate has prior experience in Julia they may submit this work as part
of their evaluation.

## Mentors

* **[Benedikt Hegner](mailto:Benedikt.Hegner@cern.ch)** (CERN)
* [Thomas Madlener](mailto:thomas.madlener@desy.de) (DESY)

## Links

### Julia

* [Julia Programming Language][Julialang]
* [Julia in HEP Github][JHEPGH]
* [S&C Roundtable Meeting on Programming Languages][SCRoundtable]
* [HSF Julia Mini-Workshop][HSFJulia]

### PODIO

 * [PODIO][PODIO]

### HEP Software Stacks

* [Key4hep][key4hep]
* [EMD4hep][edm4hep]

[PODIO]: https://github.com/AIDASoft/podio
[Julialang]: https://julialang.org/
[SCRoundtable]: https://indico.jlab.org/event/505/#day-2022-02-08
[JuliaHEPPaper]: https://arxiv.org/abs/2003.11952
[JHEPGH]: https://github.com/JuliaHEP
[HSFJulia]: https://indico.cern.ch/event/1074269/
[jethep]: https://en.wikipedia.org/wiki/Jet_%28particle_physics%29
[antikt]: https://arxiv.org/abs/0802.1189
[fastjet]: http://fastjet.fr/
[key4hep]: https://key4hep.github.io/key4hep-doc/
[edm4hep]: https://github.com/key4hep/EDM4hep
