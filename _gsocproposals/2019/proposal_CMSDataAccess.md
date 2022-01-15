---
title: "Tools for understanding CMS Data Access"
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

The raw data describing the access patterns is currently being collected and stored, 
but we lack the tools to properly curate and analyze it.
Moreover, CMS is currently lacking a comprehensive modeling framework that would allow for
predicting the access patterns within an alternate data access infrastructure. 

This project will be focused on the development of the needed frameworks and tools. 
Nevertheless, actual analysis of current usage data and modeling of potential novel infrastructures
will be required to validate their usefulness.

The analysis will include both global usage information,
as well as local access patterns at the distributed Xrootd cache across Caltech and UCSD.


## Task ideas

 - Identify, cleanse and extract the relevant data. 
  After the initial prototype stage, set in place tools and procedures that allow for the automation of the process.
 - Analyze the curated data.
  Put in place tools and procedures that allow for monitoring of deviations from discovered trends in the longer term.  
 - Put in place a modeling framework for predicting the access patterns within an alternate data access infrastructure. 
 - Create a model of potential novel infrastructures, and determine the predicted access pattern in it.

## Expected results
 - A set of tools for cleansing and extracting access pattern data.
 - A set of tools for extracting access pattern trends from cleansed data.
 - A modeling framework for predicting access patterns.
 - A report that validates the usefulness of the tools and frameworks through the analysis of the currently available data
   and the predicted access pattern using a model of potential novel infrastructure. 

## Desirable skills
 - Data analytics and modeling experience
 - Distributed computing

## Mentors
  * [Igor Sfiligoi](mailto:igor.sfiligoi@gmail.com)
  * [Frank Wuerthwein](mailto:fkw@ucsd.edu)
  * [Diego Davilla](mailto:davila.foyo@gmail.com)

## Links
  * [High-Luminosity LHC](https://home.cern/science/accelerators/high-luminosity-lhc)
  * [XRootd](http://xrootd.org)
  * [A federated Xrootd cache](http://inspirehep.net/record/1699845)
