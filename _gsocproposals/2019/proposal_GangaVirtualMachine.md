---
title: Create a user interface for Ganga that allows for the excution of tasks inside user specified virtual machines.
layout: gsoc_proposal
project: Ganga
year: 2019
organization:
  - ImperialCollege
  - MonashUniversity
---

## Description
Individual scientists are using the Ganga user interface as a frontend for performing very large computational tasks on computing resources that are spread out across the globe. As thse calculations are typically done within large collaborations, there has in the past been a set of common conventions on the exact operating system and software installed on the distributed resources. With the growth of opportunistic computing this is no longer a viable solution and the individual user will want more control over the environment their tasks are executing within. The project will implement a solution that allows the user not only to specify the task they want to execute on distributed resources but also in which virtual environment. The technology used will be Docker and Singularity - Docker due to its widespread use and Singularity as it due to its execution in pure userspace is easier to have support for on large computing farms.

## Task ideas
 * Demonstrate on a test bench that a task in Ganga can be executed within the docker container
 * Implement design of how a virtualisation environment is defined for a user
 * Create abstract interface for virtualisation to support both Docker and Singularity
 * Create interface to the Dirac resource broker that will allow for use of virtual containers within the High Energy Physics community.

## Expected results
Making it easy for a user of Ganga to specify that a given task should be executed within a user supplied virtual machine.

## Requirements
Python, Docker

## Mentors 
  * [Ulrik Egede](mailto:ulrik.egede@monash.edu)
  * [Alex Richards](mailto:a.richards@imperial.ac.uk)
  * [Mark Smith](mailto:mark.smith1@imperial.ac.uk)

## Links
  * [Ganga](https://github.com/ganga-devs/ganga)
  * [Singularity](https://www.sylabs.io/)
  * [DIRAC](http://diracgrid.org/)

