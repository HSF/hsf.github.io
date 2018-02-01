---
title: Implement Event based Seeding and Multi-Threading
layout: gsoc_proposal
project: AllpixSquared
year: 2018
organization:
  - CERN
---

# Description

Allpix Squared is a free and open-source simulation framework for silicon tracker and vertex detectors written in modern C++. Its goal is to facilitate in-depth studies of silicon-based particle and radiation detectors widely used in high-energy physics. It uses the Geant4 software to simulate the passage of particles through the detector material and them simulates the drift and diffusion processes of charge carriers in the silicon material, and the amplification and discrimination on the attached front-end electronics.

Allpix Squared is designed as a modular framework, allowing for both an easy starting point for beginners and possible extension to complex and specialized detector simulations. A modular setup also allows to separate the core of the framework from the implementation of the algorithms in the modules, leading to a framework which is both easier to understand and to maintain. This architecture and the physics event based nature of the simulation would allow for parallelization on event level, where completely independent events are simulated in different threads in parallel.

Currently, only a very simple approach to multi-thread is implemented, which splits up the different detector modules and executes them in parallel. However, this approach does not make good use of the available CPU time and it depends on the number of simulated detectors. E.g. single detectors do not profit at all from the capabilities.

In the future we would like to process independent physical events in parallel. This would allow to use the available resources better and also scales independently of the number of detectors simulated.

The tricky part here is that we still want to rely on a fixed order of events, e.g. for modules which simulate buffers in front-end electronics, but also to allow seeding of the framework with a fixed random seed. This order would be defined by the seeds given out to initialize random number generators for every event, i.e. event based seeding. The one module requiring multiple events in order would then have to join the different event threads in correct (and predictable) order.

# Task ideas

* Explore the framework and understand the simulation chain
* Benchmark the currently existing multi-threading approach
* Validate the framework's thread safety
* Implement draft of parallel event processing with event-based seeding using existing (or new) thread pool implementation
* Test performance of the new parallelization model on different machines
* Write test cases / unit tests to ensure proper functionality (distribution of random seeds, performance, functionality with multi-threading off)
* Possibly implement a new module which relies on joining threads (buffer front-end simulation)

# Requirements
This project requires good knowledge of modern C++ (11/14), experience with multi-threading in C++11 is an advantage.

Undertaking this project will improve the understanding of processes in modern radiation detectors and the Monte Carlo simulation approach widely used in particle physics.


# Mentors
* [Simon Spannagel](mailto:allpix.squared@cern.ch)
* [Andre Sailer](mailto:allpix.squared@cern.ch)
* [Daniel Hynds](mailto:allpix.squared@cern.ch)

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
* User manual (PDF): [https://cern.ch/allpix-squared/allpix-manual.pdf](https://cern.ch/allpix-squared/allpix-manual.pdf)
* Doxygen code reference: [https://cern.ch/allpix-squared/reference/](https://cern.ch/allpix-squared/reference/)
