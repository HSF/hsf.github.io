---
title: Improve the job submission and handling in the Ganga User interface
layout: gsoc_proposal
project: Ganga
year: 2021
organization:
  - ImperialCollege
  - MonashUniversity
---

## Description
The amount of data that is processed by individual scientists has grown hugely in the past decade. It is not unusual for a user to have data processed on tens of thousands of processors with these located at tens of different locations across the globe. The Ganga user interface was created to allow for the management of such large calculations. It helps the user to prepare the calculations, submitting the tasks to a resource broker, keeping track of which parts of the task that has been completed, and putting it all together in the end.

The scale of the computations submitted through the interface is placing increasing constraints on the system. When a given computational task is split up into maybe thousands of individual pieces, even a failure rate of one percent means many failures that have to be dealt with in a computational way. The aim of the project is to improve on the error reporting from individual computations and improve on the ability to recover from errors in a programmatic way.

## Task ideas
 * Collect the different wrapper scripts that are running to manage the jobs on different computational backends.
 * Set-up a local test system that implements a single node batch system using HTCondor and Slurm.
 * Identify failure modes that the wrapper scripts should identify and write a unified one for all backends.
 * Improve the user experience when part of a task is failing by allowing them to further split the task into smaller pieces.

## Expected results
A user interface where the user will have better information on why part of their task is failing to execute and make it easier to deal ith these failures in a programmatic way. 

## Evaluation Task
Interested students please contact Ulrik (see contact below) to ask questions and for an evaluation task.

## Requirements
Python programming
Linux command line experience

## Mentors 
  * [Alex Richards](mailto:a.richards@imperial.ac.uk)
  * [Mark Smith](mailto:mark.smith1@imperial.ac.uk)
  * **[Ulrik Egede](mailto:ulrik.egede@monash.edu)**

## Links
  * [Ganga](https://github.com/ganga-devs/ganga)
