---
title: PRMON - Develop Logging Implementation For Process Monitor
layout: gsoc_proposal
project: HSF
year: 2021
organization:
  - CERN
  - ANL
---

# Description

The PRoccss MONitor (or `prmon`) is a utility programme used to monitor
resource consumption of jobs running on Linux hosts. It is widely used in the
Worldwide LHC Computing Grid (WLCG) to monitor the performance of the millions
of jobs run by the ATLAS experiment in particular. The output from prmon can
then be used to detect anomalies on the level of individual jobs or task
groups.

Prmon was first developed to monitor jobs running on CPUs, but is being extended in its
functionality to cover, e.g., GPU jobs.

## Task ideas

Prmon produces little output, but as its functionality expands the possibility of errors
is growing and the use cases against which developers want to test its behaviour
become more complex. It is therefore desirable to move from relatively simple
error messages printed to `std::clog` to a more sophisticated and configurable logging
scheme in C++.

This would allow logging levels to be adjusted dynamically and specialised to particular
logging modules (e.g., generally `INFO` but `DEBUG` for one problematic component).

Then the range of unit tests in prmon should be extended, in particular to
cover *unusual and unexpected cases* that have sometimes been observed in the
field (e.g., a metric source giving a suddenly unexpected value). This will
help make prmon more robust against unexpected inputs.

## Expected results

* Implement a few initial tests of different C++ logging libraries in `prmon`.
* Together with the project leads select the best candidate to move the implementation forward.
* Adapt all current logging messages to the new library.
  * Integrating this into the project's CMake build system.
  * Implement a mechanism to control logging levels from the command line and/or environment variables.
  * Write unit tests for the logging implementation.
  * Provide documentation on how to use the new logger for users.
* Adapt the prmon monitors to read data from *precooked* sources, instead of from `/proc`.
  * Implement an interface that allows these alternative sources to be used on demand.
  * Document the use of these alternatives.
* Develop unit tests that check that prmon responds correctly to unexpected inputs.

## Requirements

 * C++ Programming
 * Git and GitHub basic skills
 * CMake (desirable)
 * Python (desirable)

## Mentors

 * [Graeme A Stewart](mailto:graeme.andrew.stewart@cern.ch)
 * [Serhan Mete](mailto:alaettin.serhan.mete@cern.ch)

## Links

 * [PRMON Code](https://github.com/HSF/prmon)
 * [WLCG](https://wlcg.web.cern.ch/)
 * [ATLAS Experiment](https://atlas.cern/)
