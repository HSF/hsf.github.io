---
project: Belle2
title: Belle II Event Display with Phoenix
layout: gsoc_proposal
year: 2023
difficulty: high
duration: 350
mentor_avail: May-October
organization:
  - LMU
  - KIT
---

## Description
The development of the software for the international Belle II collaboration started more than a decade ago. Since then technologies have evolved and offer improvements over currently implemented solutions. One of such cases is the tool to display the detector geometry, recorded signals, and reconstructed objects. The event display is used to monitor the detector performance, study reconstruction algorithms, and for education and outreach purposes.

The event display in the Belle II software is based on ROOT TEve. To display events the full Belle II software has to be installed on the user's local machine. This requirement is lifted in modern client-server based systems. The phoenix software offers such a solution. It exploits display capabilities of today's web browsers.

The task of this project is the implementation of a phoenix based event display for Belle II. The estimated effort is 350 hours and the task is well suited for a student with experience in Typescript and Angular. Knowledge of C++ would be beneficial for understanding the current implementation. Knowledge of (particle) physics is not required.

## Task ideas
 * Analyze the existing event display code and understand the requirements.
 * Set up a dummy version of a phoenix event display.
 * Extract Belle II detector geometry information and display it with phoenix.
 * Extract information of detector signals and display them with phoenix.
 * Extract information of simulated/reconstructed objects and display them with phoenix.
 * Improve the user experience, e.g. by customization options.
 * Write documentation for users and for developers who will maintain or extend the event display.
 * Roll out the new event display and collect user feedback.

## Expected results
The expected result is a Belle II event display implemented with phoenix. Not all components of the old event display may be fully implemented within this project, but all conceptual issues should be addressed.

## Evaluation Task
Interested students please contact [Thomas and Giacomo](mailto:Thomas.Kuhr@lmu.de,giacomo.pietro@kit.edu) for more details and an evaluation task.

## Requirements
 * Typescript, Angular, Web programming, knowledge of C++ and the ROOT event display would be an advantage.

## Mentors
 * **[Thomas Kuhr](mailto:Thomas.Kuhr@lmu.de)** LMU
 * [Giacomo De Pietro](mailto:giacomo.pietro@kit.edu) KIT

## Links
 * [Belle II](https://belle2.jp/)
 * [basf2](https://github.com/belle2/basf2)
 * [phoenix](https://github.com/HSF/phoenix)
 * [TEve](https://root.cern/doc/master/group__TEve.html)
