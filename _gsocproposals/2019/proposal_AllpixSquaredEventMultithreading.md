---
title: Implement Event based Seeding and Multi-Threading
layout: gsoc_proposal
project: AllpixSquared
year: 2019
organization:
  - CERN
  - Nikhef
---

# Description

Allpix Squared is a free and open-source simulation framework for silicon tracker and vertex detectors, written in modern C++. Its goal is to facilitate in-depth studies of silicon-based particle and radiation detectors widely used in high-energy physics. It uses the Geant4 software package to simulate the passage of particles through the detector material, followed by the simulation of the drift and diffusion processes of charge carriers in the silicon, and finally amplification and discrimination on the attached front-end electronics.

Allpix Squared is designed as a modular framework, allowing for both an easy starting point for beginners and possible extension to complex and specialized detector simulations. A modular setup also allows separation of the core of the framework from the implementation of the algorithms in modules, leading to a framework which is both easier to understand and to maintain. This architecture and the physics event-based nature of the simulation would allow for parallelization on an event level, where completely independent events are simulated in different threads in parallel.

GSoC 2018 saw the first implementation of an event-parallel approach, where issues involving the distribution of random seeds, mutexing within the data object types and the mode of information transfer between modules were dealt with. An eventual bottleneck was found however, within the interaction between Allpix Squared and Geant4. While Geant4 is well-equipped for multi-threaded event processing, it is currently implemented in a manner where it takes control of all threads, and is not designed to act in subservience to an external framework. A reimplementation of the Geant4 multi-threaded run manager, encapsulated within Allpix Squared, would allow this issue to be overcome and lead to the first fully event-parallel release. 

Once this issue is solved, benchmarking on many-core systems will be required in order to search for unnecessary mutexing or any other limitations which would prevent total processing time scaling. 


# Task ideas

* Explore the framework and understand the simulation chain
* Benchmark the existing multi-threading approach
* Implement a version of the Geant4 multi-threaded run manager within the framework, to accommodate event generation with Geant4 in different threads
* Test performance of the now complete parallelisation on different machines and as a function of number of worker cores
* Verify data object persistency during multi-threaded operation
* Write test cases / unit tests to ensure proper functionality (distribution of random seeds, performance, functionality with multi-threading off)
 
# Requirements
This project requires good knowledge of modern C++ (11/14), experience with multi-threading in C++11 is an advantage.

Undertaking this project will improve the understanding of processes in modern radiation detectors and the Monte Carlo simulation approach widely used in particle physics.


# Mentors
* [Simon Spannagel](mailto:allpix.squared@cern.ch)
* [Daniel Hynds](mailto:allpix.squared@cern.ch)
* [Koen Wolters](mailto:allpix.squared@cern.ch)

# Additional Resources

The following resources might provide a more complete picture of the software and its purpose. Especially the comprehensive user manual might be useful for a head start.

## Web site
[https://cern.ch/allpix-squared](https://cern.ch/allpix-squared)


## Source code

* Main repository @ CERN GitLab: [https://gitlab.cern.ch/allpix-squared/allpix-squared](https://gitlab.cern.ch/allpix-squared/allpix-squared)
* Mirror on GitHub: [https://github.com/simonspa/allpix-squared](https://github.com/simonspa/allpix-squared)
* Issue tracker: [https://gitlab.cern.ch/allpix-squared/allpix-squared/issues](https://gitlab.cern.ch/allpix-squared/allpix-squared/issues)

## Documentation

* User manual (HTML): [https://cern.ch/allpix-squared/usermanual/allpix-manual.html](https://cern.ch/allpix-squared/usermanual/allpix-manual.html)
* User manual (PDF): [https://cern.ch/allpix-squared/usermanual/allpix-manual.pdf](https://cern.ch/allpix-squared/usermanual/allpix-manual.pdf)
* Doxygen code reference: [https://cern.ch/allpix-squared/reference/](https://cern.ch/allpix-squared/reference/)
