---
title: A new Training Center Website
layout: gsoc_proposal
project: HSF
year: 2023
organization:
- princeton
- iris-hep
difficulty: low
duration: 175
mentor_avail: May-October
---

## Description

There is a large number of training resources for newcomers in the field of High Energy Physics. The [HSF Training group](https://hepsoftwarefoundation.org/workinggroups/training.html) together with [IRIS-HEP](https://iris-hep.org/) has started to compile a curriculum of such training modules that helps to get beginners up to speed quickly. However, the [current listing](https://hepsoftwarefoundation.org/training/curriculum.html) in the form of a static table is quickly becoming overwhelming, and we cannot include many resources because of space limitations.
This project is about creating a new training center that turns the static page into a dynamic list of training content that can be filtered by attributes such as programming language, common tasks, type of training, HEP experiment, etc. The candidate can start with the code of <https://learn.astropy.org/> (an unrelated training website of a popular astrophysics package) and change the underlying data sources: rather than being based on a series of Jupyter notebooks, configuration files should allow listing arbitrary content.

## Requirements

* JavaScript
* HTML
* web development basics

## Steps and task ideas

**Core goals:**

* Run a local version of learn.astropy.org from a fork of the project
* Adapt the data sources to read from yaml files that point to arbitrary web content (rather than reading Jupyter notebooks of a single repository)
* Change the side menus based on the new content listed
* Adapt the design to that of the HSF
* Help to deploy a first version of the website
* Ensure that there is sufficient documentation for continued maintenance after the internship ends

**Stretch goals:**

* Collect user feedback after the site went live and incorporate requests for improvement
* Add code to collect the number of visitors and searches
* Add a full text search engine for the new content

## Expected results

A deployed training center webpage with basic filters. See the "core goals" section above.

## Mentors

* Kilian Lieret [kl5675@princeton.edu](mailto:kl5675@princeton.edu) Princeton University

For this project only, **please include the mailing list [hsf-training-center-gsoc@googlegroups.com](mailto:hsf-training-center-gsoc@googlegroups.com) in CC**.

Please see the instructions below for the phase 1 application.

## Phase 1 Application

Please send us your CV and motivation for this project.

We also have a qualification task to make a fair selection of candidates. It should take you no more than 1-2 days to complete (depending on prior knowledge). 

**For fairness, you will have 48h to send us your solutions after you receive the instructions.** 

We understand that your schedule might be busy, so we proceed as follows:

1. Send us a start date and time **in Eastern Time zone (EST)**. Please let us know **1-2 working days in advance** to ensure we can schedule the email in time. Your submission should be completed by Mar 12, so the **latest start date is Mar 10**. Please make sure to CC hsf-training-center-gsoc@googlegroups.com.
2. We will send a quick confirmation email within 1-2 working days.
3. The email with the qualification task instructions will be sent at the time specified in step 1.
4. You work for 1-2 days and submit your results (we will take into account if you submit after 1 or 2 days)
5. We will confirm receiving your solutions within 1-2 working days.
6. We will announce the result of this phase 1 selection on Mar 14.

For fairness, we will not provide additional information about the qualifiction task other than the project information above.