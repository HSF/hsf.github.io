---
project: Ganga
title: Implement a deprecation system to keep code up to date
layout: gsoc_proposal
year: 2025
difficulty: medium
duration: 350
mentor_avail: May-November
organization:
  - ImperialCollege
  - MonashUniversity
---

## Description
The amount of data that is processed by individual scientists has grown hugely in the past decade. It is not unusual for a user to have data processed on tens of thousands of processors with these located at tens of different locations across the globe. The [Ganga](https://github.com/ganga-devs/ganga) user interface was created to allow for the management of such large calculations. It helps the user to prepare the calculations, submitting the tasks to a resource broker, keeping track of which parts of the task that has been completed, and putting it all together in the end.

As code that has developed over many years, there are part of the API that has become redundant. This means that for a period of time there will be both the old and now deprecated API as well as the new way of doing things. At the moment Ganga is missing a formal way of deprecating code. This means that warnings about using something deprecated are non-uniform and there is also very old code that has never been cleaned up.

The idea in this project is to formalise the way that code can be declared deprecated and then use the continuous integration to ensure that the code eventually is deleted. 

## Task ideas
 * Have a well defined way of marking plugins, functions etc as deprecated with a warning about when they will be removed. Building on top
 of the python package [deprecated](https://pypi.org/project/Deprecated/) might be an idea.
 * Run tests in the testing framework that will alert developers to that certain parts of the code can now be removed.
 * Apply in the testing framework a similar system that will identify when deprecated python features are used when moving to a new python version.
 * Apply the deprecation system to parts of the code that is already deprecated.

## Expected results
Obtain a cleaner code base where very old and since long deprecated code is no longer present. Provide the end user with consistent warnings about their use of deprecated code as well as when it will be removed.

As a student, you will gain experience with the challenges of large scale computing where some tasks of a large processing chain might take several days to process, have intermittent failures and have thousands of task processing in parallel. You will get experience with working within a large code base that has gone through many developments.

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
