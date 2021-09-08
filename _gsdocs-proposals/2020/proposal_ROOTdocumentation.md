---
title: ROOT Documentation
layout: gsdocs_proposal
project: ROOT
year: 2020
organization:
  - CERN
---

## Description of project idea

The ROOT system [1] [2] is the main data analysis and data presentation tool used in high
energy physics world-wide. More than 1 exabyte of data are stored in the ROOT format.

ROOT is being made available under the LGPL 2.1+, which allows
ROOT to be used in a wide range of open and closed environments.

ROOT it is written in C++ with dynamic Python bindings. Thanks to its
capabilities and performance it is also used in industry.

ROOT's documentation and web site are a key parts of the ROOT project [6]. They are
evolving in parallel and complement each other. The basis is the reference Guide [4]
documenting all the ROOT C++ components. A large set of tutorials [5], helping to
enter the ROOT world, is also provided. And finally a "Manual"
guides users through the ROOT tools and concepts [7].

ROOT's documentation needs to be improved in various areas:
  - It is difficult for non-physicists.
  - Some important parts like the Python bindings are weakly documented.
  - We are missing tutorials illustrating the functionalities provided by ROOT 7.
  - New key data format need detailed Technical specifications.

## Tasks

 Possible tasks might include:

- Because ROOT's documentation is mainly physics-oriented, it is more
  difficult for non-physicists to pick up ROOT. The Manual should address this.
- The ROOT Python bindings suffers from a lack of documentation. It should be extended in
  the reference guide.
- Series of new "tutorials for modern analysis" is needed to illustrate the
  functionalities provided by ROOT 7.
- RNTuple is the new data format ROOT will provide in the future. It will be the successor
  of the TTree object which is used to stored the 1 exabyte of data previously mentioned.
  Therefore, detailed Technical specifications of this new object is crucial.

## Project duration

This is expected to be a long (6 months) project which will possibly continue
after this period.

## Related material

  1. [ROOT web site](https://root.cern)
  2. [ROOT GiHub repository](https://github.com/root-project/)
  3. [ROOT User's Guide](https://root.cern/guides/users-guide)
  4. [ROOT Reference Guide](https://root.cern/doc/master/)
  5. [ROOT tutorials](https://root.cern/doc/master/group__Tutorials.html)
  6. [ROOT web site GitHub repository](https://github.com/root-project/web)
  7. [ROOT manual in the web site](https://root-project.github.io/web/manual/)

## Expected results

The deliverables of the projects will be directly visible online in the various area
mentioned in the "Tasks" paragraph. The writers will directly commit his work as pull
requests to the web site repository.

The minimum results for each task to consider the project successful are:

- Make sure the manual, at least in the introductory part of each section, does not
  require physics knowledges.
- With the help of the ROOT Python experts implement the structure of a guide for ROOT python
  bindings.
- Start to implement new "tutorials for modern analysis" to illustrate the
  functionalities provided by ROOT 7.
- At least a skeleton of the RNTuple Technical specifications should be implemented.

## Experience required

Besides good technical writer skills, the following additional technical skills are mandatory:

  - Programming Knowledges (python and C++)
  - Web coding (html, markdown, jekyll, etc ..)
  - Tools : git/github

## Mentors

  * [Olivier Couet](mailto:olivier.couet@cern.ch)
  * [Axel Naumann](mailto:axel.naumann@cern.ch)
