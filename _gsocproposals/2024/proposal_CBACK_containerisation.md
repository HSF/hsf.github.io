---
title: Containerisation of CBACK backup system
layout: gsoc_proposal
project: CBACK
year: 2024
organization:
  - CERN
difficulty: hard
duration: 350
mentor_avail: July-September
---

# Description
The Storage department at CERN is responsible for the preservation and backup strategy of 880PB+ of disk based data across various storage infrastructure solutions. 
Excluding physics data, Backups must also be provided for internal user facing name-spaces, one of the main projects used for this purpose at Cern is CBACK (Cern Backup.) 

CBACK is a scaleable backup Orchestrator that uses Restic combined with a central SQL DB to store information on different "jobs" (Backup, Restore, Prune, Verify) 
These jobs can be picked up by stateless agents of a corresponding type (e.g. backup job -> backup Agent) for completion, allowing the number of "agents" to easily
be scaled by operators as demand increases or decreases. CBACK is currently deployed as static infrastructure on VM's thus this expansion is manual. 

## Task ideas
This project proposes that the potential candidate undertakes the following tasks, with the primary aim of breaking this static nature:
* Develop A new "scheduler" agent type, responsible for polling the internal DB, and spawning other agents via kubernetes based on service demand.
* Write changes and Helm charts for existing agents, allowing for their containerization / spawning by the new "scheduler"
* With assistance, write changes that allow for a limitation of scope IRGT the file mounts of a node (or container) running a job agent by using cephx keys 
* Document the changes they are responsible for creating to cback

## Expected results and milestones
* Familiarise themselves with the use case, design and codebase of CBACK
* Propose a blueprint for the work to be carried out 
* Develop, test and debug solution based on their blueprint
* Benchmark solution, evaluate success, pros + shortcomings.
* Present final result of project to Mentors & Storage department.

## Requirements
* Python, Go, SQL
* Kubernetes, Docker
* Unix / Linux 
* Restic (a plus, but not necessary)

## Mentors
[Gianmaria Del Monte](mailto:gianmaria.del.monte@cern.ch) (CBACK)
[Enrico Bocchi](mailto:enrico.bocchi@cern.ch) (Kubernetes)
[Roberto Valverde](mailto:roberto.valverde@cern.ch) (CBACK)
**[Zachary Goggin](mailto:zachary.goggin@cern.ch) (CBACK)**

## Links
* [CBACK HEPiX Introduction](https://cds.cern.ch/record/2767135?ln=en)
* [CBACK in detail](https://cds.cern.ch/record/2855376?ln=en)
* [Restic](https://restic.net/)
