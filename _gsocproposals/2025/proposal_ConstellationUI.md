---
title: Extending the User Interface
layout: gsoc_proposal
project: Constellation
year: 2025
organization: DESY
difficulty: medium
duration: 350
mentor_avail: June-August
project_mentors:
  - name: "Stephan Lachnit"
    email: "stephan.lachnit@desy.de"
    organization: "DESY"
  - name: "Simon Spannagel"
    email: "simon.spannagel@desy.de"
    organization: "DESY"
---

## Description

Constellation is a framework used for lab setups or small-scale experiments in
HEP. One of its most important goals is that the framework should be easy to
use for both scientists implementing new devices as well as experiment
operators.

Constellation features a Qt-based User Interfaces to control and monitor all
devices in the experimental setup. The focus of this GSoC project is to add new
user interfaces to Constellation and extend the current ones.

## Project Milestones

* Creating a new GUI to display monitoring data from devices using Qt Charts
* Modularization of UI elements into reusable Qt widgets
* Adding the monitoring widget to the existing GUI for device control

## Requirements

* Modern C++
* Knowledge of Qt is helpful but not required
* Practical experience with Unix and git


## Links

* [Repository](https://gitlab.desy.de/constellation/constellation)
* [Documentation](https://constellation.pages.desy.de/)
