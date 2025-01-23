---
project: Ganga
title: A concurrency model for the monitoring in Ganga
layout: gsoc_proposal
year: 2022
difficulty: medium
duration: 350
mentor_avail: June-August
organization:
  - ImperialCollege
  - MonashUniversity
---

## Description
The amount of data that is processed by individual scientists has grown hugely in the past decade. It is not unusual for a user to have data processed on tens of thousands of processors with these located at tens of different locations across the globe. The [Ganga](https://github.com/ganga-devs/ganga) user interface was created to allow for the management of such large calculations. It helps the user to prepare the calculations, submitting the tasks to a resource broker, keeping track of which parts of the task that has been completed, and putting it all together in the end.

The scale of the computations submitted through the interface is placing increasing constraints on the system. Keeping track of where the tasks are executing, what the status of them are and subsequently dealing with the data that they create has become a bottleneck using the existing solution based on a simple ThreadPool in Python. We are looking for a new implementation of this overall monitoring aspect of Ganga.

## Task ideas
 * Explore the relative benefits of using different concurrency/parallelism methods (asyncio, threads, multiprocessing)
 * Set-up a local system that can be used to test and develop the monitoring without having dependencies on
   externals.
 * Develop a new monitoring system that utilise concurrency in the optimal way to reduce latency in the system.
 * Improve the user feedback in Ganga by making it easier to see the progress of the monitoring and to understand what
   monitoring operations are queued for execution.

## Expected results
Moving Ganga from the present situation where the monitoring often falls behind, leading to frustrated usesrs that can't get hold of their results even if the tasks are finished, to a new monitoring system that is able to keep the user's session responsive and that doesn't fall behind in the monitoring of tasks.

As a student, you will gain experience with the challenges of concurrency and how different solutions will have to be used when implementing this in a large existing framework. You will of course also gain experience with working within an open source environment, presenting your work, writing test cases and utilise continuous integration as part of your development cycle.

## Evaluation Task
Interested students please contact Ulrik (see contact below) to ask questions and for an evaluation task.

## Requirements
Python programming (advanced), use of concurrency in Python (intermediate), Linux command line experience (novice).

## Mentors 
  * [Alex Richards](mailto:a.richards@imperial.ac.uk)
  * [Mark Smith](mailto:mark.smith1@imperial.ac.uk)
  * **[Ulrik Egede](mailto:ulrik.egede@monash.edu)**

## Links
  * [Ganga](https://github.com/ganga-devs/ganga)
