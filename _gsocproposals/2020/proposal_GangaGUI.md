---
title: Upgrading the Ganga graphical user interface
layout: gsoc_proposal
project: Ganga
year: 2020
organization:
  - ImperialCollege
  - MonashUniversity
---

## Description
The amount of data that is processed by individual scientists has grown hugely in the past decade. It is not unusual for a user to have data processed on tens of thousands of processors with these located at tens of different locations across the globe. The Ganga user interface was created to allow for the management of such large calculations. It helps the user to prepare the calculations, submitting the tasks to a resource broker, keeping track of which parts of the task that has been completed, and putting it all together in the end.

In addition to the ubiquitous command line interface, there exists a graphical user interface (GUI) to ganga.
Underused since it's inception, the code for this GUI has been abandoned and all but forgotten. The aim of this project
would be to breathe new life into this GUI by either updating the underlying technology and
making it more user friendly or by switching to a new web app based approach.

## Task ideas
 * Resurrect and understand the existing GUI code.
 * Make proposals for and carry out upgrading it to make it more usable both in terms of underlying technology but also
 features
 * If deemed appropriate, design and move the GUI to a web application framework

## Expected results
An updated, fully featured, capable and modern looking GUI which users will want to use.
Alternatively (or additionally) a modern web application layer over the Ganga interface to
act as a GUI capable of carrying out the same tasks users could do with the command line interface


## Requirements
Python programming
Python web frameworks (Django, cherrypy, flask)
GUI toolkit experience (Qt, tkinter, etc)
Web technology experience (HTML, CSS, JS, AJAX)

## Mentors 
  * [Ulrik Egede](mailto:ulrik.egede@monash.edu)
  * [Alex Richards](mailto:a.richards@imperial.ac.uk)
  * [Mark Smith](mailto:mark.smith1@imperial.ac.uk)

## Links
  * [Ganga](https://github.com/ganga-devs/ganga)
