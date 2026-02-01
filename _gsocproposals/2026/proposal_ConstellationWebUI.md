---
title: Web Interface for Controlling and Monitoring Experimental Setups
layout: gsoc_proposal
project: Constellation
year: 2026
organization: DESY
difficulty: medium
duration: 350
mentor_avail: July-October
project_mentors:
  - email: stephan.lachnit@desy.de
    organization: DESY
    first_name: Stephan
    last_name: Lachnit
  - email: simon.spannagel@desy.de
    organization: DESY
    first_name: Simon
    last_name: Spannagel
---

## Description

Constellation is a framework used for lab setups or small-scale experiments in
HEP. In these setups, components frequently change and are connected to
different computers in a local network. Constellations aims to reduce the time
required to commission these setups by providing a set of Qt-based graphical
user interfaces as well as a a simple API for users which abstracts the
underlying network stack for controlling and monitoring.

## Task Idea

The idea of this GSoC project is evaluate the possibility of a flexible web
interface, allowing to control and monitor a setup from a browser. This would
allow to check the status of the setup from any computer in the local network
without a separate installation Constellation.

The web interface should communicate with the libraries of Constellation via a
websocket, thus offloading the complex networkinging to already existing code.

## Project Milestones

* Designing a web interface concept
* Establish communication between the web interface and Constellation's libraries
* Creation of fully-featured web interface for controlling and monitoring

## Requirements

* Excellent programming skill in either C++ or Python to interface with Constellation's libraries
* Knowledge of a web framework, prefarably Svelte
* Experience with websockets is a plus but not required
* Practical experience with Unix and git

## AI Usage Policy

AI assistance is allowed for this project as long as all code is fully
understood and can be explained by the applicant. The applicant takes full
responsibility for all code and results, disclosing AI use for non-routine
tasks (algorithm design, architecture, complex problem-solving). Routine
tasks (grammar, formatting, style) do not require disclosure.

## Links

* [Repository](https://gitlab.desy.de/constellation/constellation)
* [Documentation](https://constellation.pages.desy.de/)
