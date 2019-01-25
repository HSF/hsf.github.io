---
title: Optimisation of the Ganga toolkit in terms of memory consumption and persistent storage
layout: gsoc_proposal
project: Ganga
year: 2019
organization:
  - ImperialCollege
  - MonashUniversity
---

## Description
The amount of data that is processed by individual scientists has grown hugely in the past decade. It is not unusual for a user to have data processed on tens of thousands of processors with these located at tens of different locations across the globe. The Ganga framework was created to allow for the management of large calculations by helping the user prepare the calculations, submitting the tasks to the resource broker, keeping track of which parts of the task that has been completed, and putting it all together in the end.

The scale of user calculations means that the memory consumption of the Ganga framework has grown very large as it has not been a priority to consider in the the past. The same issue arises for the persistent storage of all finished and ongoing tasks. The project will perform an evaluation of the memory consumption of the framework and explore methods for reducing it. The aim will be to create a memory management and persistent system for Ganga that can scale to the user requirements in science for the next decade.

## Task ideas
 * Perform a careful audit of the memory consumption of Ganga when used in a real life situation.
 * Turn the existing coarse lazy loading already implemented into a cached memory management system that on a more fine grained level will load and unload data as required.
 * Create prototype of persistent storage in Ganga that exploits the repetitive nature of much of the metadata.
 * Implement a new persistent storage model and create a migration tool for existing users.

## Expected results
A significant reduction in the memory footprint of the Ganga process when processing very large data volumes. A system that persists the metadata about jobs in a more compact form thus reducing both storage requirements and time to read the data.

## Requirements
Python

## Mentors 
  * [Ulrik Egede](mailto:ulrik.egede@monash.edu)
  * [Alex Richards](mailto:a.richards@imperial.ac.uk)
  * [Mark Smith](mailto:mark.smith1@imperial.ac.uk)

## Links
  * [Ganga](https://github.com/ganga-devs/ganga)
