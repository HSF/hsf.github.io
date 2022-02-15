---
title: Advanced Belle II Software Validation
layout: gsoc_proposal
project: Belle II
year: 2022
organization: LMU
---

## Description
The international Belle II collaboration relies on custom software for the simulation, reconstruction, and analysis of the data recorded by the Belle II detector. The software was developed by hundreds of physicists over more than a decade. The development process will continue for several years to optimize algorithms for better physics performance or resource efficiency, to adjust the code to technological evolutions, or to implement new ideas.

With such a large, diverse, and quickly changing development team the quality assurance of the software is a challenge. Belle II has implemented several mechanisms to monitor the software quality. An essential tool is the high-level validation. It runs algorithms on large datasets and produces plots of distributions of quantities that are relevant for physics analyses. The distributions are displayed on a web page and compared with previous versions and a reference. With this degradations can be quickly identified and fixed.

While the validation system is used in production successfully, several items are know that could be improved:
- A bookkeeping of known degradations
- A better referencing to individual plots
- More information to encourage the reuse of artifacts
- Improvements to make the root cause analysis of degradations easier

This project seeks to enhance the user experience of the Belle II software validation page and make workflows more efficient by appropriate technical solutions. The estimated effort is 175 (or 300?) hours and the task is well suited for a student with experience in python and web programming. Knowledge of (particle) physics is not required.

## Task ideas
 * Analyze the existing code base and understand the requirements.
 * Discuss technical solutions with the mentors and implement them.
 * Roll out new versions and collect user feedback.

## Expected results
The expected result is an enhanced validation page that makes it easier to identify, keep track of, and resolve degradations introduced in the Belle II software.

## Evaluation Task
Interested students please contact Thomas (Thomas.Kuhr@lmu.de) for more details and an evaluation task.

## Requirements
 * Python, web programming, linux. Knowledge of cherrypy would be an advantage.

## Mentors
 * [Thomas Kuhr](mailto:Thomas.Kuhr@lmu.de)

## Links
 * [Belle II](https://belle2.jp/)
 * [basf2](https://github.com/belle2/basf2)
