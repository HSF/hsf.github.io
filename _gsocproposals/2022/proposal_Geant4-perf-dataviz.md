---
title: Geant4 - Performance Data Visualization using d3.js
layout: gsoc_proposal
project: Geant4
year: 2022
difficulty: medium
duration: 175
mentor_avail: June-August
organization:
  - CERN
---

## Description

Experiments at the Large Hadron Collider (LHC) make extensive use of detector
simulation with [Geant4][geant4], consuming a large portion of the computing
resources available at the [Worldwide LHC Computing Grid (WLCG)][wlcg]. With
the next runs of the LHC approaching, the expected increases in beam luminosity
will increase demand for simulation far beyond the limits of what further hardware
upgrades can reach. Therefore, monitoring and improving the performance of the
simulation software, including Geant4, is of utmost importance to CERN's success.

Geant4 performance monitoring already happens on a regular basis, for example, via
the profiling and benchmarking work done at [FNAL][g4cpt], and with regular performance
analysis run locally by developers. However, in order to identify and fix performance
regressions more efficiently, we would like to create more visual performance reports
in HTML and improve performance data visualizations using [d3.js][d3js] or a similar
javascript visualization library.

## Expected Results

The expected result is a dynamic HTML-based report for summarizing and
visualizing performance data collected with [perf][perf] (potentially converted
to CSV or JSON format), and comparing performance differences between two given
versions of a Geant4 simulation. This report is expected to be included in a
dedicated continuous integration job that developers can use to assess the
performance impact of their proposed changes in Geant4.

Two examples of visualizations to be included in the report are
[flamegraphs][g4flame] and [treemaps][treemap].

## Evaluation Task

Interested students please contact Guilherme for a warm-up and evaluation task.
In lieu of an evaluation task, however, the interested student can submit prior
work on data visualizations using d3.js or another javascript library.

## Technologies

 * HTML5, javascript, d3.js, perf, Python, shell scripting

## Desirable Skills

 * Experience with HTML5 and data visualization using d3.js (required)
 * Experience with Linux profiling tools like perf (desirable)

## Mentors

 * **[Guilherme Amadio](mailto:amadio@cern.ch)** (CERN)
 * [Bernhard Manfred Gruber](mailto:bernhard.manfred.gruber@cern.ch) (CERN)

## Links

 * [Geant4 Simulation Toolkit][geant4]
 * [FNAL Geant4 Profiling and Benchmarking Page][g4cpt]
 * [d3.js Website][d3js]
 * [Linux Perf Wiki][perf]
 * [Brandan Gregg's perf examples][bg]
 * [The Unofficial Linux Perf Events Web-Page][perfdoc]

[d3js]: https://d3js.org/
[geant4]: https://geant4.web.cern.ch
[wlcg]: https://wlcg.web.cern.ch/
[g4cpt]: https://g4cpt.fnal.gov/
[g4flame]: https://amadio.web.cern.ch/flamegraphs/geant4.svg
[treemap]: https://cern.ch/amadio/treemap/cpi
[perf]: https://perf.wiki.kernel.org/index.php/Main_Page
[perfdoc]: https://web.eece.maine.edu/~vweaver/projects/perf_events/
[bg]: https://www.brendangregg.com/perf.html
