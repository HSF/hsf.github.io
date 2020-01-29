---
title: Workflow configuration import and validation for AliECS
layout: gsoc_proposal
project: ALICE
year: 2020
organization:
  - CERN
---

## Description
In preparation for LHC Run 3 starting spring 2021, the ALICE Experiment at CERN LHC is undergoing
a major upgrade, which includes a new computing system called O² (Online-Offline). To ensure the
efficient operation of the upgraded experiment along with its newly designed computing system, a
reliable, high performance and automated experiment control system is being developed with the
goal of managing all O² synchronous processing software, and of handling the data taking activity
by interacting with the detectors, the trigger system and the LHC.

The ALICE Experiment Control System (AliECS) is a distributed system based on state of the art
cluster management and microservices which have recently emerged in the distributed computing
ecosystem. AliECS is being built from scratch in Go and takes advantage of Apache Mesos for its
cluster resource management capabilities, with the goal of controlling tens of thousands of
processes over hundreds of nodes. It includes a distributed state machine, hierarchical
configuration facilities with Consul as key-value store, a Git-based workflow template system and
both command-line and graphical user interfaces. Thanks to its novel design and fresh technical
foundation, AliECS aims to deliver unprecedented operational flexibility, performance,
reliability and data taking efficiency.

For ALICE O², 2020 is a year of intense system integration activity. As part of this collective
effort, it is necessary to improve the workflow configuration import capabilities of AliECS.

A workflow template is a file (YAML) which describes a set of data-driven processes to run and control
throughout the O²/FLP cluster at LHC Point 2. For developers of processing software, the high
level interface is called DPL (O² Data Processing Layer). This component is able to generate
dumps of data-driven workflows (i.e. files describing a set of processes to run and how they
talk to each other), which currently cannot directly be imported into AliECS. Besides DPL dumps,
it would also be interesting to be able to import other experiment-agnostic workflow descriptions
for use in the ALICE O²/FLP farm.

Furthermore, while AliECS defines its own workflow template input format, this format has been
extended over time and isn't subject to a formal schema. It would be very useful to be able to
validate this kind of configuration input against a schema, both in AliECS and in a future DPL
to AliECS workflow converter tool.

While the files in question describe ALICE O²-specific configuration structures, the student does
not need to be familiar with experiment-specific concepts and most of the code produced by the
student need not be experiment-specific. Even so, the tasks listed below provide
ample opportunity for creative solutions to real world challenges in large physics experiment data
acquisition.

The completed work would become an essential software component of ALICE experiment operations at
the LHC, starting 2021.

## Task ideas
 * Develop an importer or format converter tool, which would acquire a DPL workflow dump and
 output an AliECS workflow template. As DPL cannot provide all information necessary to
 generate a valid AliECS workflow template, different modes of operation could be considered for
 this command-line tool, such as an interactive mode and a non-interactive one with more clever
 guesswork. The student will be provided with file examples and documentation.
 * Develop a format validation package based on YAML schema, plus add format validation to DPL
 importer tool. While the schemata are necessarily ALICE-specific, the package need not be.
 * Extend configuration validation facilities to other forms of AliECS-managed configuration,
 such as component-specific configuration files.
 * Develop a "configuration simulator" tool which would accept a workflow configuration file
 plus some variables, and graphically represent the workflow as it would appear in the O²/FLP
 cluster.
 * Extend the importer tool to support DDS topology files, which are not experiment-specific and
 would allow AliECS to consume any FairMQ-based processing chain.
 * Develop an exporter tool or package, allowing the user to generate a DPL, DDS and/or other
 experiment-agnostic workflow description starting from an AliECS workflow template.
 * Further integration opportunities include schema validation in commit hooks, Ansible
 inventory integration, Consul as data source during conversion, etc.

## Expected results
Full-featured workflow configuration import and validation facilities.

Integration of said facilities into AliECS, documentation, tests.

Optionally other additional configuration import interfaces can be considered, such as Web UI or
graphical terminal, or other configuration input related improvements.

## Requirements
* Go programming
* YAML and JSON
* Experience with any of the following is a bonus: 
Linux terminal programming, curses, C++, shell programming, Python, Consul, Web frameworks, Go text/template, Jinja

## Mentors 
  * [Vasco Chibante Barroso](mailto:vmcb@cern.ch) (backup)
  * [Teo Mrnjavac](mailto:teo.m@cern.ch) (primary)

## Links
  * [AliECS](https://github.com/AliceO2Group/Control)
  * [Examples of AliECS workflow configuration](https://github.com/AliceO2Group/ControlWorkflows)
