---
title: Testing framework for Jupyter notebooks
layout: gsoc_proposal
project: SWAN
year: 2019
organization: CERN
---

## Description

In the world of data analysis, [Jupyter notebooks](https://jupyter.org/) are the de-facto solution to write and execute code in an interactive fashion by simply using a web browser.
CERN provides a Jupyter notebook service called [SWAN](https://swan.web.cern.ch/), which builds on top of Jupyter notebooks by integrating the storage, synchronization and sharing capabilities of [CERNBox](http://cernbox.web.cern.ch) and the computational power of Hadoop clusters. Also, software packages are retrieved on the fly from the [CernVM File System](https://cernvm.cern.ch/portal/filesystem), allowing users to forget about installation, configuration, and compatibility of packages.

Jupyter notebooks, despite being easily accessible from an intuitive web-based interface, are a complex environment, especially when used together with [JupyterHub](https://github.com/jupyterhub/jupyterhub), custom extensions, external storage backends and computational clusters. This project aims at the development of a testing framework covering the many aspects of the Jupyter environment, which is able to both run synthetics tests and to mimic users' actions in the notebook interface.

## Task ideas

Design and development of a testing framework including:
  * Functional tests (e.g., access to CERNBox storage and software libraries from CernVM File System) to identify any issue potentially compromising the normal operation of the SWAN service;
  * Performance tests (e.g., the time needed to start a user session or to execute a predefined workload) to spot performance degradation impacting the users;
  * Regression tests (e.g., execute a predefined sequence of actions and contrast the expected results with the obtained one) to detect unintentional changes in the behavior of the system upon the release of new software.

The framework should be designed with maintainability and extensibility in mind so to allow the addition of new tests to cover new features of the SWAN service.
In addition, the framework should be self-contained and distributable by means of Docker containers.

## Expected results

A working implementation of a testing framework for Jupyter notebooks to troubleshoot issues and monitor performance.

## Requirements
  * Python, Shell scripting
  * Understanding of file systems, HTTP, Docker container platform
  * Experience with Jupyter notebooks is a plus

## Mentors
  * [Enrico Bocchi](mailto:enrico.bocchi@cern.ch)
  * [Diogo Castro](mailto:diogo.castro@cern.ch)
  * [Joao Calado Vicente](mailto:joao.calado.vicente@cern.ch)
  * [Jakub Moscicki](mailto:jakub.moscicki@cern.ch)
  * [Enric Tejedor Saavedra](mailto:enric.tejedor.saavedra@cern.ch)

## Links
  * [Jupyter notebooks](https://jupyter.org/)
  * [SWAN](https://swan.web.cern.ch/)
  * [CERNBox](http://cernbox.web.cern.ch)
  * [CernVM File System](https://cernvm.cern.ch/portal/filesystem)
  * [JupyterHub](https://github.com/jupyterhub/jupyterhub)
