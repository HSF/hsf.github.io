-
project: HSF
title: HSF
layout: default
logo: hsf_logo_angled.png
description: |
  The HEP Software Foundation encourages cooperation and common
  development of software in High Energy Physics. The HSF hosts
  a number of software projects where developers are working to
  solve current problems in particle physics.
---

{% include gsoc_project.ext %}

-
title: Negative weight mitigation with cell resampling in ATLAS workflows
layout: gsoc_proposal
project: Negative weight, ATLAS event generator workflows
year: 2026
organization: Southern Methodist University
project_mentors: Saptaparna Bhattacharya (saptaparnab@smu.edu)
---

## Description

Negatively weighted events arise as a result of subtraction schemes in next-to-leading (or higher) order event generators. The fraction of negatively weighted events vary as a function of phase space requirements that are imposed in experimental analyses making it imperative to store these events for time consuming downstream processing like detector simulation. They are a severe source of inefficiency in event generator workflows, requiring large datasets to mitigate statistical dilution caused by negatively weighted events.  

A method to redistribute negatively weighted events was proposed in arXiv:2109.07851 and subsequently in  arXiv:2303.15246. We plan to use this method for ATLAS event generator workflows. The method has been previously implemented in CMS for small-scale tests. In this project, we will extend the scope of previous explorations in both ATLAS and CMS by identifying computationally intensive workflows and running validation tests that are designed to ensure that distributions of physical observables are not sculpted as a result of the removal of negatively weighted events.

The eventual goal of the project is to integrate the negative weight mitigation scheme into a realistic ATLAS workflow and setup a validation pipeline that ensures that the method is performing as desired.   

## Task ideas
 * Establish familiarity with ATLAS event generator workflows
 * Run cell resampling method with fake data (generated with a pseudorandom generator thrown from distributions that are indicative of experimental data) 
 * Run cell resampling with ATLAS event generator workflows
 * Setup a validation suite
 * Document results with distributions of variables before and after the method has been applied with a metric that shows computational gains in terms of lower fraction of negatively weighted events

## Expected results
 * Design an event generator workflow and validation suite that tests the cell resampling method for negative weight removal

## Requirements
 * Familiarity with python and C++  

## Mentors
  * [Saptaparna Bhattacharya](mailto:saptaparna.bhattacharya@cern.ch)

## Links
  * [Cell resampling](https://cres.hepforge.org/)
