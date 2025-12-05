---
title: Machine Learning in Julia for Calorimeter Showers
layout: gsoc_proposal
project: JuliaHEP
year: 2024
organization:
  - CERN
difficulty: medium
duration: 175
mentor_avail: June-July; September-October
---

# Description

In high-energy physics experiments at [CERN](https://home.cern/), the calorimeter is a key detector technology to measure the energy of particles. These particles interact with the material of the calorimeter, creating cascades of secondary particles, or showers. Describing the showering process relies on simulation methods that precisely model all the particle interactions with matter, using the [Geant4](https://geant4.web.cern.ch/) toolkit. However, this approach is computationally expensive and future upgrades make this full simulation for all events even less feasible.

Machine Learning (ML) techniques, such as generative modelling, are used as fast simulation alternatives to learn how to generate showers in a calorimeter, i.e. simulating the calorimeter response to certain particles. Recently there has been significant advances in the fidelity of shower simulations, with the [Fast Calorimeter Simulation Challenge](https://calochallenge.github.io/homepage/) spurring development and comparison of various different models.

Also in HEP there has been [increasing interest](https://doi.org/10.1007/s41781-023-00104-x) in using [Julia](https://julialang.org/) as a language for HEP software that combines the ease of programming in interactive languages, e.g., Python, with the speed of compiled language, such as C++. One of the areas that merits investigation is to use Julia's machine learning tool kits and to compare ease of use and performance against current popular solutions.

## Task ideas

Review the most successful models implemented in the CaloChallenge, to understand which ML/AI approaches have been used. Prepare data for use in Julia, selecting suitable Julia packages for implementing the training. Retrain selected models in the Julia ecosystem, with generation of suitable metrics. Compare the training results between models, using the CaloChallenge metrics. Compare the inference times between Julia and Python/C++ models.

## Expected results and milestones

* Successful preparation of calorimeter training data for use in Julia
* Model training on CPU using Julia ML tool kits
* Comparison of training results between Julia and Python driven models
* Comparison of inference times in trained models between Julia and Python

## Requirements

* Programming experience with machine learning tool kits in Python
* Prior experience in Julia (very advantageous)
* A background understanding of high-energy physics (advantageous)

## Evaluation Exercise

**This project is not accepting more submissions to the evaluation project. If you have not yet been in contact with the mentors then please do not submit a solution.**

The evaluation exercise for this project is [here](https://github.com/graeme-a-stewart/hfs-julia-ml-gsoc/). 

## Mentors

* **[Graeme Stewart](mailto:graeme.andrew.stewart@cern.ch)**
* [Pere Mato](mailto:pere.mato@cern.ch)
* [Piyush Raikwar](mailto:piyush.raikwar@cern.ch)

## Links

* [Julia Programming Language](https://julialang.org/)
* [JuliaHEP HSF Group](https://hepsoftwarefoundation.org/activities/juliahep.html)
* [Potential of the Julia Programming Language for High Energy Physics Computing](https://doi.org/10.1007/s41781-023-00104-x)
* [CaloChallenge](https://calochallenge.github.io/homepage/)
* Some Julia ML toolkits:
    * [ADCME.jl](https://docs.juliahub.com/ADCME/b8Ld2/0.7.3/)
    * [Flux.jl](https://fluxml.ai/Flux.jl/stable/)
    * [InvertibleNetworks.jl](https://slimgroup.github.io/InvertibleNetworks.jl/dev/)
    * [MLJ.jl](https://alan-turing-institute.github.io/MLJ.jl/stable/)
    * [NormalizingFlows.jl](https://turinglang.org/NormalizingFlows.jl/dev/)
    * [RxInfer.jl](https://reactivebayes.github.io/rxinfer-website/)
