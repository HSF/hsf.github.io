---
title: "Understanding CMS Data Access"
layout: gsoc_proposal
project: IRIS-HEP
year: 2019
organization:
 - UCSD
---


## Description

The High-Luminosity Large Hadron Collider (HL-LHC) will produce roughly an exabyte of data per year for CMS. 
We are trying to understand access patterns in Run2, i.e. most recent couple years of CMS on the current accelerator, 
in order to provide input on the design of more cost-effective data access infrastructure for the HL-LHC. 

This involves understanding access patterns at the level of task, file, block, dataset, and object within files.
There are questions of predictability as well as optimal replication schemes. 

This project will include both analysis of usage data, and modeling of potential novel infrastructures. 

## Task ideas

- Analyze the available data.
  The analysis will include both global usage information,
  as well as local access patterns at the distributed Xrootd cache across Caltech and UCSD.
- Create a model of potential novel infrastructures.

## Expected results
Analyze the usage data and create a model of potential novel infrastructures.

## Desirable skills
 - Data analytics experience
 - Distributed computing

## Mentors
  * [Igor Sfiligoi](mailto:isfiligoi@ucsd.edu)

## Links
  * [High-Luminosity LHC](https://home.cern/science/accelerators/high-luminosity-lhc)
  * [XRootd](http://xrootd.org)
  * [A federated Xrootd cache](http://inspirehep.net/record/1699845)
