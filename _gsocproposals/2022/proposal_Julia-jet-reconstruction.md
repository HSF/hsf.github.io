---
title: Jet Reconstruction with Julia
layout: gsoc_proposal
project: HSF
year: 2022
difficulty: medium
duration: 350
mentor_avail: June-July, September-October
organization:
    - CERN
---

# Description

<div style="text-align:center; padding:25px; float:right">
<img src="{{ '/images/others/julia.png' | relative_url }}" alt="Julia Logo" width=100px />
</div>

Currently in high-energy physics (HEP) there are [two main languages
used][SCRoundtable]: **C++** for numerically intensive code, where execution
speed is paramount; and **Python**, for interactivity and ease of development
(often used as 'glue' between high-performance code modules). Recently there has
been [increasing interest][SCRoundtable] in [**Julia**][julialang] as an
alternative/additional language for HEP. This could offer the convenience
features of Python, but the optimal runtime speed of C++
([Julia in HEP Paper][JuliaHEPPaper], [Julia HEP Github][JHEPGH]).

In order to continue this investigation, this project will re-implement some
important algorithms for HEP in Julia, with the aim of assessing developer
convenience and runtime performance compared to standard implementations in C++.

## Jet Reconstruction

<div style="text-align:center; padding:25px; float:right">
<img src="{{ '/images/others/ATLAS_VP1_event_display_run282712_evt474587238_2015-10-21T06-26-57_v3.png' | relative_url }}" alt="ATLAS Event Display" width=400px />
<br>ATLAS Event Display with multiple jets, &copy; ATLAS
</div>

The passage of high-energy particles through detectors like ATLAS and CMS at
CERN frequently results in showers of secondary particles that form a cascade,
which is captured in the calorimeters of these experiments. These particle
cascades are called [*jets*][jethep] and it is extremely important to
reconstruct the energy of the primary particle from the calorimeter
measurements.

Over the years the community have developed several well-tested algorithms for
doing this. One of the most popular is the [*anti-kt* algorithm][antikt], which
has a community standard implementation as part of the [FastJet package][fastjet]. <!-- markdown-link-check-disable-line -->

## Task ideas and expected results

The task is to write an Anti-Kt jet reconstruction algorithm in Julia. This will
read simulated calorimeter data files and implement the jet finding algorithm on
this data. Data will be output as clustered jets. To ensure correctness,
comparison with FastJet will be done, both numerically and using visualisation.
The speeds of the two codes will then be benchmarked on different platforms, for
both serial and multi-threaded running; the convenience for the developer and
code maintainability will be assessed.

## Skills

Some prior experience with Julia would be highly desirable, but strong
programming skills in C++ and Python should enable the candidate to learn Julia
sufficiently quickly for the project.

## Extensions

The task has many possible extensions that the candidate could tackle:

* Implement additional algorithms for jet reconstruction (longitudinally invariant kt; longitudinally invariant inclusive Cambridge/Aachen)
* Integration into the [Key4hep][key4hep] software stack, using the [EDM4hep][edm4hep] data model

## Evaluation Task

The evaluation task comprises of doing a simple timing of the current anti-kt
algorithm. For details please contact the mentors.

If the candidate has prior experience in Julia they may submit this work as part
of their evaluation.

## Mentors

* [Benedikt Hegner](mailto:Benedikt.Hegner@cern.ch) (CERN)
* [Graeme A Stewart](mailto:graeme.andrew.stewart@cern.ch) (CERN)

## Links

### Julia

* [Julia Programming Language][Julialang]
* [Julia in HEP Github][JHEPGH]
* [S&C Roundtable Meeting on Programming Languages][SCRoundtable]
* [HSF Julia Mini-Workshop][HSFJulia]

### Jets and Reconstruction Algorithms

* [Jets in HEP][jethep]
* [The anti-kt jet clustering algorithm][antikt]
* [FastJet][fastjet] <!-- markdown-link-check-disable-line -->

### HEP Software Stacks

* [Key4hep][key4hep]
* [EMD4hep][edm4hep]

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
