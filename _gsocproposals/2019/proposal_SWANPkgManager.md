---
title: Package manager for SWAN/Jupyterlab
layout: gsoc_proposal
project: SWAN
year: 2019
organization:
  - CERN
---

## Description
[SWAN](https://cern.ch/swan) (Service for Web-based ANalysis) is the platform allowing CERN users to perform interactive data analysis by writing code and running it simply using a web browser. It builds on top of the widely-adopted [Jupyter Notebooks](https://jupyter.org/) by integrating the storage, synchronization and sharing capabilities of [CERNBox](http://cern.ch/cernbox) and the computational power of Spark/Hadoop clusters. In addition, [software packages](http://lcginfo.cern.ch/) are retrieved on the fly from an HTTP-based file system called [CVMFS](https://cernvm.cern.ch/portal/filesystem) (CernVM File System) allowing users to forget about installation, configuration, and compatibility of packages.

Thanks to CERNBox, SWAN has integrated sharing functionality inside its interface, allowing users to share "projects" between themselves thus fostering collaborative analysis. Due to the centrally managed software, provided by CVMFS, a user trying to open the shared notebook doesn’t have to worry about compatibility with its software stack, since they are the same. However, SWAN is also used by users who need to install their own packages, breaking this seamless sharing experience.

With this problem in mind, this project aims to provide a package manager for SWAN (in the shape of a Jupyterlab extension), that will allow users to keep track of the packages needed by its "projects", thus also allowing others to seamless install everything needed.

## Task ideas
  * Create a Jupyter interface extension to specify the names and versions of the packages required by a project
  * Automatically install and manage packages in the user storage
  * Make the installed packages available inside the notebook user environment
  * Intercept attemptive installations of software from inside the notebook
  * (Optional) Interface with the CVMFS packages information to suggest different software stacks to the users

## Expected results

A working Jupyter extension, installable both in SWAN and the vanilla Jupyterlab, that will allow the users to specify Python modules (and respective versions) via a user interface, making them available inside the notebook cells automatically.
Optionally, if installed in SWAN (or other CVMFS enabled Jupyterlab deployment), it should also be able to understand the packages available in its software stacks.

## Desirable Skills
  * Knowledge of Python and Javascript
  * Knowledge on how to develop Jupyterlab (or Jupyter Notebooks) extensions

## Mentors 
  * [Diogo Castro](mailto:diogo.castro@cern.ch)
  * [Jakub Moscicki](mailto:jakub.moscicki@cern.ch)
  * [Enrico Bocchi](mailto:enrico.bocchi@cern.ch)
  * [Enric Tejedor Saavedra](mailto:etejedor@cern.ch)

## Links
  * [SWAN](https://cern.ch/swan)
  * [Project Jupyter](https://jupyter.org/)
  * [CVMFS](https://cernvm.cern.ch/portal/filesystem)
  * [LCG Info](http://lcginfo.cern.ch/)
  * [CERNBox](http://cern.ch/cernbox)
