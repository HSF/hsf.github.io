---
title: A new Training Center Website
layout: gsoc_proposal
project: hsf
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

* Typescript
* HTML
* web development basics

## Steps and task ideas

**Core goals:**

* Run a local version of learn.astropy.org from a fork of the project
* Adapt the data sources to read from yaml files that point to arbitrary web content (rather than reading Jupyter notebooks of a single repository)
* Change the side menus based on the new content listed
* Adapt the design to that of the HSF
* Help to beploy a first version of the website
* Ensure that there is sufficient documentation for continued maintenance after the internship ends

**Stretch goals:**

* Collect user feedback after the site went live and incorporate requests for improvement
* Add code to collect the number of visitors and searches
* Add a full text search engine for the new content

## Expected results

A deployed training center webpage with basic filters. See the "core goals" section above.

## Mentors

* Kilian Lieret [kl5675@princeton.edu](mailto:kl5675@princeton.edu) Princeton University
* TBD
