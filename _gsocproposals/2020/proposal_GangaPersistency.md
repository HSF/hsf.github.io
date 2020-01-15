---
title: Upgrading the Ganga user interface to use a relational database for persistent storage
layout: gsoc_proposal
project: Ganga
year: 2020
organization:
  - ImperialCollege
  - MonashUniversity
---

## Description
The amount of data that is processed by individual scientists has grown hugely in the past decade. It is not unusual for a user to have data processed on tens of thousands of processors with these located at tens of different locations across the globe. The Ganga user interface was created to allow for the management of such large calculations. It helps the user to prepare the calculations, submitting the tasks to a resource broker, keeping track of which parts of the task that has been completed, and putting it all together in the end.

The scale of user calculations means that just the metadata from the Ganga framework associated wit hthe users tasks has grown large. Until now the data has been stored in a simple uncompressed XML format. The aim will be to create a new model, most likely based on a relational database, that can serve as the persistent system for Ganga. It should be able to support caching of information in memory in an efficient way and should scale to the use cases within science over the next decade.

## Task ideas
 * Perform a careful audit of the memory consumption of Ganga when used in a real life situation.
 * 
 * Implement a new persistent storage model and create a migration tool for existing users.

## Expected results
A more responsive user interface that can transfer information to and from the persistent storage in a faster and more efficient way. A caching in memory that will allow Ganga to keep a fixed size in memory. 

## Requirements
Python

## Mentors 
  * [Ulrik Egede](mailto:ulrik.egede@monash.edu)
  * [Alex Richards](mailto:a.richards@imperial.ac.uk)
  * [Mark Smith](mailto:mark.smith1@imperial.ac.uk)

## Links
  * [Ganga](https://github.com/ganga-devs/ganga)
