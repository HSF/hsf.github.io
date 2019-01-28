---
title: Packaging
layout: plain
redirect_from:
  - /workinggroups/2015/11/04/packaging.html
  - /activities/packaging.html
---

The software packaging and distribution activity and working group addresses common issues, tools, and approaches to building and distributing the software stacks used by HEP experiments.

The group is currently convened by Ben Morgan (Warwick) and Graeme Stewart (CERN), who took over from Liz Sexton-Kennedy (FNAL) and Benedikt Hegner (CERN) in October 2017.

# Getting Involved

Everyone is welcome to participate and contribute on the forum and to the ongoing meetings:

* [Packaging Group Discussion Forum](https://groups.google.com/forum/#!forum/hsf-packaging-wg){:target="_hsf_packaging_forum}

* [Contact the group convenors](mailto:ben.morgan@warwick.ac.uk,graeme.andrew.stewart@cern.ch)
  (Ben and Graeme)

* [Packaging Group Meetings Indico](https://indico.cern.ch/category/7975/){:target="_hsf_packaging_indico"}

# Goals

The aim of this working group is to foster communication and exchange among the experiments' librarians. We have identified various topics to work on, including

  1. Common build recipes and tools
  2. How to take most advantage of technologies like containers
  3. Proper support for developers in our collaborations

## Group Activities to Date

Software development in high energy physics follows the paradigm of open source software (OSS). Experiments as well as the theory community heavily rely on software being developed outside of the field. Creating a consistent and working stack out of 100s of packages, on a variety of platforms is a non-trivial task. Within the field multiple technical solutions exist to configure and build those stacks. None of this work is experiment specific and our working group agrees that this effort is being duplicated.

We held [an initial series of meetings](https://indico.cern.ch/category/7975/)
to look at the existing build and packaging solutions, including the
community-driven projects. Some of the tools looked at are listed below.

That initial work was summarised in a [Technical note on Build Tools](/technical_notes.html)
in March 2016.

Since then the group has been meeting to re-examine changes in the field and to have
more of a focus on deployment and end user development issues.

This resulted in the writing of

* A set of [use cases](https://docs.google.com/document/d/1h-r3XPIXXxmr5tThIh6gu6VcXXRhBXtUuOv14ju3oTI/edit?usp=sharing)
that give the high level goals for an integrated and shared suite of packaging tools.
* A [test stack](https://docs.google.com/document/d/1LW8OsTFFA9QwsJ9fASkRoJ2E6Gk3UGnOQIcElCL8UCM/edit?usp=sharing)
of core HEP software packages that can be used to demonstrate how different
tools perform against the use cases that were identified.

The group is currently working on the evaluation of  different tools, making
use of Docker containers to allow non-experts in a particular tool to
rapidly evaluate each tool for features, ease of use and flexibility.

Documentation for these *test drive* setups is in the group's
[GitHib](https://github.com/HSF/packaging) repository.

# Appendix

## Build Tools

### HEP Specific Build Tools

  * [aliBuild](http://alisw.github.io/alibuild/)
  * [cmsBuild](https://github.com/cmsbuild/cmsdist)
  * [LCGCMake](https://gitlab.cern.ch/sft/lcgcmake/)
  * [Worch](https://github.com/brettviren/worch)
  * Contractor (no public documentation)
  * SciSoft (no public documentation)

### General Open Source Build Tools

  * [Conda](http://conda.pydata.org/docs/)
  * [homebrew](http://brew.sh/)
  * [Nix](https://nixos.org/nix/)
  * [Portage](https://wiki.gentoo.org/wiki/Project:Portage)
  * [Spack](https://github.com/spack/spack)

## Existing build recipes

  * [cet-is](https://cdcvs.fnal.gov/redmine/projects/build-framework/repository)
  * [cmsdist recipes](https://github.com/cmsbuild/cmsdist)
  * [HEP-SPACK recipes](https://github.com/HSF/hep-spack)
  * [conda recipes by Daniela Remenska ](https://github.com/remenska/root-conda-recipes)
  * [aliDist recipes](https://github.com/alisw/alidist)
  * [LCGCMake recipes](https://gitlab.cern.ch/sft/lcgcmake)

## Other resources

  * [HSF Organization on GitHub](https://github.com/HSF)
  * [HSF cmaketools package ](https://github.com/HSF/cmaketools)
  * [Draft Technical Note on Platform Naming Conventions](/technical_notes.html)
  * [Packaging WG on GitHub](https://github.com/HSF/packaging)
  * [Packaging WG Technical Note HSF-TN-2016-03 ](/notes/HSF-TN-2016-03.pdf)
  * [HSF on DockerHub](https://hub.docker.com/u/hepsoftwarefoundation/dashboard/)
