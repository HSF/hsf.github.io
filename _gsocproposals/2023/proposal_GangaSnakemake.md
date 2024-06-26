---
project: Ganga
title: Interfacing Ganga with the Snakemake system
layout: gsoc_proposal
year: 2023
difficulty: medium
duration: 350
mentor_avail: May-November
organization:
  - ImperialCollege
  - MonashUniversity
---

## Description
The amount of data that is processed by individual scientists has grown hugely in the past decade. It is not unusual for a user to have data processed on tens of thousands of processors with these located at tens of different locations across the globe. The [Ganga](https://github.com/ganga-devs/ganga) user interface was created to allow for the management of such large calculations. It helps the user to prepare the calculations, submitting the tasks to a resource broker, keeping track of which parts of the task that has been completed, and putting it all together in the end.

The large scale processing of data is often only one part of a long processing chain for obtaining the results that eventually will end up in an academic publication though. Calibrations need to be performed, plots should be made, checks run for systematic effects etc. To do all these small tasks, the snakemake tool is increasingly used. The idea for ths project is to implement Ganga as a plugin for snakemake. There is already support for various batch systems in snakemake, so this will take it one step further.

## Task ideas
 * Explore the relative benefits of interfacing Ganga with snakemake using the [foreign workflow management system](https://snakemake.readthedocs.io/en/stable/snakefiles/foreign_wms.html) versus creating a new [cloud execution backend](https://snakemake.readthedocs.io/en/stable/project_info/contributing.html#contributing-a-new-cluster-or-cloud-execution-backend).
 * Modify Ganga to work in a mode where it easily act as a client for snakemake.
 * Implement intelligent code in Ganga that can ensure that intermittent failures in the processing are recovered from in a grceful way.
 * Develop continuous integration tests that can ensure that the integration with snakemake is always functional.

## Expected results
For the scientific users of Ganga, they will be able to integrate their large scale data processing into their overall snakemake workflow.

As a student, you will gain experience with the challenges of large scale computing where some tasks of a large processing chain might take several days to process, have intermittent failures and have thousands of task processing in parallel. You will work as part of a small team that carries out the developments and support for Ganga.

## Evaluation Task
Interested students please contact Ulrik (see contact below) to ask questions and for an evaluation task.

## Requirements
Python programming (advanced), Linux command line experience (intermediate), use of git for code development and continuous integration testing (intermediate)

## Mentors 
  * [Alex Richards](mailto:a.richards@imperial.ac.uk)
  * [Mark Smith](mailto:mark.smith1@imperial.ac.uk)
  * **[Ulrik Egede](mailto:ulrik.egede@monash.edu)**

## Links
  * [Ganga](https://github.com/ganga-devs/ganga)
  * [Snakemake](https://snakemake.readthedocs.io/en/stable/index.html)
