---
title: MCnet/YODA - Improved unit testing and coverage reports from CI
layout: gsoc_proposal
project: MCnet
year: 2024
organization:
  - UCL
difficulty: medium
duration: 175
mentor_avail: June-October
---

# Description

YODA is a lightweight library for efficient multi-dimensional histogramming
and binned data analysis. It provides a lightweight common system for
Monte Carlo event generator validation analyses, particularly as the
core histogramming library used by the [Rivet](https://yoda.hepforge.org)
analysis toolkit.


## Task ideas

This project will improve the robustness of the YODA library and
release system through automated unit-test coverage reports
by the GitLab continuous integration system, and web-based
visualization of what code areas need better monitoring.


## Expected results and milestones

 * Familiarise with the YODA library;
 * Familiarise with the YODA unit test system, including current CI scripts;
 * Hook up existing unit tests with `gcov` for producing coverage report;
 * Familiarise and its visualization tools
 * Hook up existing unit tests with `gcov` and produce a coverage estimate;
 * Visualize coverage reports and produce web-based status displays;
 * Trigger automated coverage checks and visual displays in the CI.

## Requirements

 * C++
 * CI testing
 * git


## Mentors

 * **[Christian Gutschow](mailto:chris.g@cern.ch)**


## Links

 * [YODA](https://yoda.hepforge.org)
