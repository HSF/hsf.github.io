---
title: Migrate the Smashbox test suite to Python 3
layout: gsoc_proposal
project: CERNBox
year: 2022
difficulty: medium
duration: 175
mentor_avail: June-September
organization:
  - CERN
  - ownCloud
---

## Description

[Smashbox](https://github.com/cernbox/smashbox) is a testing framework aimed at verifying the general behavior of a desktop synchronization client against CERNBox: the file sync and share solution at CERN. Its development started in 2014 and ever since it has grown to include additional test cases and features to increase the testing coverage.

Since 2014 Smashbox has been powered by Python 2.7 and so far, has been sufficient to keep up with the needs of our service. However, with newer versions of the sync client, new features are also included that need to extend Smashbox further in scope, with concurrency functionalities and libraries that are only available in modern versions of Python.

The scope of this project is to migrate the Smashbox codebase to Python3, removing potentially dead code from its codebase. Simplify its configuration model and explore alternatives to extending this test suite with new cases such as the [Windows VFS sync](https://doc.owncloud.com/desktop/next/vfs.html) mode.

## Task ideas

* Set up the environment to run the testing framework and its current pain-points
* Migrate the codebase to a modern version of Python (3.10)
* Simplify the framework's deployment model and the test results (e.g. integrate testing libraries)
* Extend the test suite with relevant test-cases to cover more functionalities
* Document the changes and additions in the context of the project

## Expected results

By the end of GSoC '22, we expect the student to understand the internals of the Smashbox testing framework, to have migrated the test suite to make use of the newer concurrency primitives offered by Python 3, and to be able to add new relevant test-cases to the existing suite. Extended its documentation and evaluated additional functional-testing approaches.

The student will learn about designing and implementing testing frameworks, concurrency and end-to-end validation of distributed systems in practice.

## Evaluation tasks

Interested students can contact Samuel (see contact below) to ask questions and to request an evaluation task.

## Requirements

* Mandatory
  * Python 3
  * Linux, Git, Docker
* Basic understanding
  * Distributed systems and parallelism
  * Networking and HTTP REST APIs

## Mentors

* **[Samuel Alfageme Sainz](mailto:samuel.alfageme.sainz@cern.ch)** (CERN)
* [Fabian Müller](mailto:fmueller@owncloud.com) (ownCloud)
* [Hannah von Reth](mailto:hannah.vonreth@owncloud.com) (ownCloud)

## Links

* [Smashbox on GitHub](https://github.com/cernbox/smashbox)
* [ownCloud, CERN and Smashbox](https://owncloud.com/news/owncloud-cern-smashbox/)
* [Smashbox in action](https://owncloud.com/news/smashbox-in-action/)
