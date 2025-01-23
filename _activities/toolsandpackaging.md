---
title: Software Developer Tools and Packaging
layout: plain
redirect_from:
  - /workinggroups/2015/11/04/packaging.html
  - /activities/packaging.html
  - /workinggroups/packaging.html
  - /workinggroups/softwaredevelopertools.html
  - /workinggroups/toolsandpackaging.html
---

## Software Developer Tools

The Software Developer Tools Activity Area aims to help the HEP community in developing the latest, modern feature-rich projects
with the aid of software tools such as code editors, static/dynamic code analysers, compilers, debuggers, performance analysers and so on.
The group plans to accomplish this by mainly serving as a forum where developers can share their experiences, discuss new/existing tools they utilise,
and learn from each other. To that point, contributions from the entire community are strongly encouraged.

## Packaging

The group has a particular focus also on solutions for building and deploying software stacks, through the evolution of the previous *HSF Packaging Working Group*.

### Packaging Goals

The aim of is to foster communication and exchange among the experiments' librarians. We have identified various topics to work on, including

  1. Common build recipes and tools
  2. How to take most advantage of technologies like containers
  3. Proper support for developers in our collaborations

### Group Activities to Date

Software development in high energy physics follows the paradigm of open source software (OSS). Experiments as well as the theory community heavily rely on software being developed outside of the field. Creating a consistent and working stack out of 100s of packages, on a variety of platforms is a non-trivial task. Within the field multiple technical solutions exist to configure and build those stacks. None of this work is experiment specific and our
group agrees that this effort is being duplicated.

We held [an initial series of meetings](https://indico.cern.ch/category/7975/)
to look at the existing build and packaging solutions, including the
community-driven projects. Some of the tools looked at are listed below.

That initial work was summarised in a [Technical note on Build Tools]({{ site.baseurl }}/technical_notes.html)
in March 2016.

Since then the group has been meeting to re-examine changes in the field and to have
more of a focus on deployment and end user development issues.

This resulted in the writing of

- A set of [use cases](https://docs.google.com/document/d/1h-r3XPIXXxmr5tThIh6gu6VcXXRhBXtUuOv14ju3oTI/edit?usp=sharing)
that give the high level goals for an integrated and shared suite of packaging tools.
- A [test stack](https://docs.google.com/document/d/1LW8OsTFFA9QwsJ9fASkRoJ2E6Gk3UGnOQIcElCL8UCM/edit?usp=sharing)
of core HEP software packages that can be used to demonstrate how different
tools perform against the use cases that were identified.

The group is currently working on the evaluation of  different tools, making
use of Docker containers to allow non-experts in a particular tool to
rapidly evaluate each tool for features, ease of use and flexibility.

Documentation for these *test drive* setups is in the group's
[Github](https://github.com/HSF/packaging) repository.

### Conveners

The group is currently coordinated by:


- Patrick Gartung (Fermilab)
- Nathan Brei (Jefferson Lab)
- Reiner Hauser (ATLAS)
- Andrea Valenzuela Ramirez (CMS)


All the coordinators can be reached [by email](mailto:gartung@fnal.gov,nbrei@jlab.org,reiner.hauser@cern.ch,andrea.valenzuela.ramirez@cern.ch). <!-- markdown-link-check-disable-line -->

### Activities

- The Indico pages for the group meetings can be found at <https://indico.cern.ch/category/7975/>
- For all technical discussions please use <hsf-tech-forum@googlegroups.com> (Tools) and <hsf-packaging-wg@googlegroups.com> (Packaging)

### Former Conveners

- Benedikt Hegner (CMS, EP-SFT), 2016-2017
- Elizabeth Sexton-Kennedy (CMS), 2016-2017
- Graeme A Stewart (ATLAS), 2017-2019
- Ben Morgan (ATLAS, superNEMO), 2017-2020
- Martin Ritter (Belle II), 2018-2020
- Giulio Eulisse (ALICE), 2018
- Mircho Rozodov (CMS), 2021
- Alaettin Serhan Mete (ATLAS and ANL), 2021-2022
- Marc Paterno (DUNE and Fermilab), 2021-2022
- Valentin Volkl (FCC and CERN), 2023
- Henry Schreiner (IRIS-HEP / Princeton), 2023
