---
title: Container deployment performance across Grid sites
layout: gsoc_proposal
project: ALICE
year: 2020
organization:
  - CERN
---

## Description
The [ALICE Experiment](https://home.cern/science/experiments/alice) at the [CERN](https://home.cern) LHC relies on the [WLCG](https://wlcg.web.cern.ch/), Worldwide LHC Computing Grid, for processing and analysing large quantities of its data. With clusters spread across hundreds [computing sites](http://alimonitor.cern.ch/map.jsp) worldwide, most of the computing resources provided by these sites vary greatly in both hardware and configurations.

To assure compatibility with the software requirements of its applications, ALICE is moving towards a [new framework](https://gitlab.cern.ch/jalien/jalien) for executing tasks on the Grid using containers. To execute containers, the sites must meet a series of prerequisites both in terms of operating system and container handling software. The readiness of the site to run containers must be ensured before configuring the task submission using the ALICE container framework.

To that end, a test framework and testing methodology must be developed and executed on all sites providing resources for ALICE. The results of the test must be analysed and reported back to the site administrators for action in case of issues or incomplete provision of the necessary prerequisites.

## Task ideas
 * Develop a simple submission framework within the JAliEn Grid environment for pre-configured containers to specific Grid sites;
 * Use the framework to start containers, and gather and analyze the output of the submission to gauge the readiness of the site to execute the containers against a list of known conditions;
 * Suggest modifications to the container configuration to simplify their execution.

## Expected results
  * Develop a tool to assess the WLCG Grid sites readiness to run ALICE Grid jobs in containers

## Requirements
  * Java experience is required
  * Python experience is recommended
  * Experience with containerization technologies is a plus
  * Bash and Linux skills are beneficial

## Mentors
 * [Maksim Storetvedt](mailto:maksim.melnik.storetvedt@cern.ch) (primary)
 * [Costin Grigoras](mailto:costin.grigoras@cern.ch) (backup)

## Links
 * [JAliEn git repository](https://gitlab.cern.ch/jalien/jalien)
 * [ALICE Grid monitoring](http://alimonitor.cern.ch)
