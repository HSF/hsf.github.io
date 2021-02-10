---
title: Upgrading the Ganga graphical user interface
layout: gsoc_proposal
project: Ganga
year: 2021
organization:
  - ImperialCollege
  - MonashUniversity
---

## Description
The amount of data that is processed by individual scientists has grown hugely in the past decade. It is not unusual for a user to have data processed on tens of thousands of processors with these located at tens of different locations across the globe. The Ganga user interface was created to allow for the management of such large calculations. It helps the user to prepare the calculations, submitting the tasks to a resource broker, keeping track of which parts of the task that has been completed, and putting it all together in the end.

In addition to the ubiquitous command line interface, there exists a web based graphical user interface (GUI) to ganga. The basic functionality of the GUI is there but it requires further development to include the correct information and to work in an intuitive way for users. 

## Task ideas
 * Understand the existing GUI code.
 * Make proposals to improve the visual aspects of the GUI and allow users to adjust it themselves.
 * Implement new features in the GUI and make it trivial for the user to start the GUI even if running Ganga through an ssh tunnel.

## Expected results
Have a modern web application layer over the Ganga interface to act as a GUI capable and is  capable of carrying out the same tasks users could do with the command line interface.

## Evaluation Task
Interested students please contact [Ulrik](ulrik.egede@monash.edu) to ask questions and for an evaluation task.

## Requirements
Python programming
Python web frameworks (flask)
Web technology experience (HTML, CSS, JS, AJAX)
Linux command line experience

## Mentors 
  * [Alex Richards](mailto:a.richards@imperial.ac.uk)
  * [Mark Smith](mailto:mark.smith1@imperial.ac.uk)
  * [Ulrik Egede](mailto:ulrik.egede@monash.edu)

## Links
  * [Ganga](https://github.com/ganga-devs/ganga)
