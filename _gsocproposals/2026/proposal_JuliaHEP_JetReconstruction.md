---
title: Parallel Processing Improvements in Julia Jet Reconstruction
layout: gsoc_proposal
project: JuliaHEP
year: 2026
organization:
  - DESY
difficulty: medium
duration: 350
mentor_avail: June-July, September-October
project_mentors:
  - email: graeme.andrew.stewart@desy.de
    organization: DESY
    first_name: Graeme
    last_name: Stewart
  - email: mateusz.jakub.fila@cern.ch
    organization: CERN
    first_name: Mateusz
    last_name: Fila
---

## Description

The Julia programming language offers a unique combination of speed,
interoperability, ease of use, and flexibility, making it an attractive option
for high-energy physics (HEP) research. Within the HSF context, the
[JuliaHEP](https://github.com/JuliaHEP) initiative aims to develop a set of
foundational packages in the Julia ecosystem that provide the essential
functionality required by HEP researchers.

For a number of years now, there has been a package which performs [serial jet
reconstruction](https://github.com/JuliaHEP/JetReconstruction.jl), an essential
task in high-energy physics, natively in Julia. Performance for serial running
is [excellent](https://doi.org/10.1051/epjconf/202533701067), usually a
little faster than the C++ standard package for this task,
[FastJet](https://fastjet.fr).

However, to date, there has been little investigation of how the Julia code
performs multi-threaded. Some initial investigations indicate the scaling is
less than optimal, but this has not been properly quantified.

Addressing this issue, and improving the code, is the aim of this GSoC project.

## Task ideas

- Develop proper benchmarks for parallel running of JetReconstruction.jl
  - Including suitable a suitable benchmark code with FastJet as a reference
- Analyse the performance of the code with these benchmarks
- Identify bottlenecks that are impacting performance
- Improve the code to better utilise multiple CPU code in parallel

## Expected results and milestones

- A well honed set of benchmarks to measure the parallel performance of JetReconstruction.jl, and compare with C++
- An analysis of the performance, with an understanding of bottlenecks
- Code improvements that allow for greater performance (e.g., by reducing allocations)
- Advice for users on how to run efficiently in multi-threaded mode (e.g., garbage collector options)

## Requirements

- Programming experience with C++ (advantageous, in order to be able to understand existing HEP codes)
- Prior experience in Julia (very advantageous)
- A background understanding of high-energy physics (advantageous)

## How to apply

Once CERN/HSF is accepted as a GSoC org, please write an email with a short
introduction to your interests and background to the mentors with the string
"gsoc26" in the subject. There will be a small evaluation task that we will
mail to you then.

## AI usage policy

AI assistance is allowed for this contribution. The applicant takes full
responsibility for all code and results, disclosing AI use for non-routine
tasks (algorithm design, architecture, complex problem-solving). Routine tasks
(grammar, formatting, style) do not require disclosure.

## Links

- [Julia Programming Language](https://julialang.org/)
- [JuliaHEP HSF Group](https://hepsoftwarefoundation.org/workinggroups/juliahep.html)
- [JetReconstruction.jl](https://github.com/JuliaHEP/JetReconstruction.jl)
- [Fast Jet Finding in Julia](https://doi.org/10.1051/epjconf/202533701067)
