---
title: Container deployment performance across Grid sites
layout: gsoc_proposal
project: ALICE
year: 2020
organization:
  - CERN
---

## Description

The ALICE Experiment at the CERN LHC relies on the WLCG, Worldwide LHC Computing Grid, for processing and analysing large quantities of its data. With clusters spread across hundreds computing sites worldwide, most of the computing resources provided by these sites vary greatly in both hardware and configurations. To assure a compatibility with the software requirements of its applications, ALICE is moving towards a new framework for executing tasks on the Grid using containers. To execute containers, the sites must  meet a series of prerequisites both in terms of operating system and container handling software. The readiness of the site to run containers must be ensured before configuring the task submission using the ALICE container framework. To that end, a test framework and testing methodology must be developed and executed on all sites providing resources for ALICE. The results of the test must be analysed and reported back to the site administrators for action in case of issues or incomplete provision of the necessary prerequisites.  

## Task ideas

 * Develop a simple submission framework within the JAliEn Grid environment for pre- configured containers to specific Grid sites;
 * Use the framework to start containers, gather and analyze the output of the submission to gauge the readiness of the site to execute the containers against a list of known conditions; 
 * Suggest modifications to the container configuration to simplify their execution.

## Expected results

## Requirements

## Mentors
 * [Maksim Storetvedt](mailto:maksim.melnik.storetvedt@cern.ch) (primary)
 * [Costin Grigoras](mailto:consting@cern.ch) (backup)

## Links
