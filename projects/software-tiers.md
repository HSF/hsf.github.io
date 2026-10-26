---
title: "Software Tiers and Differentiated Recommendations"
author: Eduardo Rodrigues, Pere Mato, Graeme Stewart, Caterina Doglioni, Stefan Roiser
layout: plain
---

This page complements the [best-practice guidelines]({{ site.baseurl }}/projects/guidelines.html)
for [HSF Affiliated Projects and Software]({{ site.baseurl }}/projects/affiliated.html)
with differentiated recommendations according to the tier of software.
Affiliation requires the best-practice guidelines only.
A project that would like a *differential review* against the recommendations for its tier is welcome to ask for one;
this requires discussion with the [HSF Steering Group]({{ site.baseurl }}/organization/team.html) beforehand and reviewers with the relevant expertise.

Not all software is the same, in terms of purposes and audience. 
To classify software, we adopt a scheme inspired by the [*three levels of
software*](https://everse.software/RSQKit/three_tier_view), originally developed by the
[Australian Research Data Commons](https://ardc.edu.au/) (ARDC)
and subsequently adopted by the [EVERSE Project](https://everse.software). 
The starting point for the following definitions is the [RSQKit *three levels of software* page](https://everse.software/RSQKit/three_tier_view). 

**Analysis software** is research software that captures computational research processes and methodology, often used in simulation, data generation, preparation, analysis and visualisation. It typically represents software created for personal use with a small scope, such as scripts quickly put together to analyse data.

**Research software tools** (also called _prototype tools_) are research software that demonstrates a new idea, method or model for use beyond the project in which it originated, often as a substantive intellectual contribution or a proof of concept. These software tools are designed to answer multiple research questions and are typically developed and used by more than one person. They often began as a collection of analysis scripts before evolving into more comprehensive tools.

**Research software infrastructure** includes software that captures broadly accepted ideas, methods and models for use in research, often warranting close involvement of researchers in its development. This kind of software is broadly applicable, but it does not necessarily mean that its codebase will be large. A research software classed as infrastructure could be a comprehensive toolkit meeting a research need, but it could also be a smaller focused software package that is essential for several research communities. In the case of research software infrastructure, the maturity of the codebase, developer support, community support and engagement warrant specific recommendations.

We expect software developers seeking a differential review to identify the category their software fits in, which will be listed at the beginning of the review document, and consider the differential guidelines below as best-practice basis for supporting users effectively.

These guidelines lie in three major categories:

* Software engineering practices followed by the project (as described in the [best-practice guidelines]({{ site.baseurl }}/projects/guidelines.html) and with specifics for the programming language ecosystem).
* Sustainability and support structures of the project (e.g. discussion fora, documentation, training events, time to respond to issues, etc.)
* Level of adoption of the software by experiments and other projects, hence the impact of the project.

## Analysis software

A.k.a. *analysis code* in the 3-tier model.

For the HSF we interpret this as guidelines suitable for a young endeavour,
likely evolving from and within a collaboration or experiment, but with the
potential for other communities or experiments to use. At this level the
category of best software practices is what is mainly required.

### Basics

* The project should follow general and language-specific best practices as given for example in the HSF’s Best Practice Guidelines.
* The project source code should reside on a version-controlled repository that is publicly readable and has a URL (e.g., GitHub, GitLab).
* The README file at the top level should describe what the software does (what problem does it solve?).
* The project website or repository should provide information on how to:
obtain, provide feedback (as bug reports or enhancements), and contribute to the software.
* The contribution process should be explained (e.g., are pull requests used?).
* The software should be released on an Open Software license.
* The project should post the license(s) of its results in a standard location in their source repository.

### Documentation

* The project should provide basic documentation for its software.
* The project should provide reference documentation that describes the external interface (both input and output) of the software produced by the project.
* The project should have one or more mechanisms for discussion (including proposed changes and issues) that are searchable, allow messages and topics to be addressed by URL, enable new people to participate in some of the discussions, and do not require client-side installation of proprietary software.
* The project should provide documentation in English and be able to accept bug reports and comments about code in English.

### Change Control

* The project's source repository should track what changes were made, who made the changes, and when the changes were made.
* To enable collaborative review, the project's source repository should include interim versions for review between releases; it should not include only final releases.
* The project results should have a unique version identifier for each release intended to be used by users.
  We recommend using a well defined versioning scheme that is consistent with practices in your sub-domain, e.g. [Semantic Versioning](https://semver.org) or [Calendar Versioning](https://calver.org).
* The project should provide, in each release, release notes that are a human-readable summary of major changes in that release to help users determine if they should upgrade and what the upgrade impact will be.
* The release notes should not be the raw output of a version control log (e.g., the "git log" command results are not release notes).

### Sustainability

* The project should be maintained by at least one long-term maintainer, preferably with a future commitment to the software of at least 1 year (subject to funding).
* The project should provide a process for users to submit bug reports (e.g., using an issue tracker or a mailing list).
* The project should use an issue tracker for tracking individual issues.
* The project should acknowledge a majority of bug reports submitted in the last 2-12 months (inclusive); the response need not include a fix.
* The project should respond to a majority (>50%) of enhancement requests in the last 2-12 months (inclusive).
* The project should have a publicly available archive for reports and responses for later searching.

### Level of Adoption

* The software produced by the project should be of interest for the HEP experiments.
* The software should be adopted by at least one experiment/collaboration/project.

## Research software tools

A.k.a. *prototype tools* in the 3-tier model.

In the HSF we interpret this as projects moving towards strong
community support and adoption (e.g., adoption is still relatively shy,
maintenance is not secured at least in the medium term by more than a single
person). High standards of software engineering should be met. All the criteria
for Tier 3 should be fulfilled, with the addition of the following criteria.

### Basics

* The project should follow general and language-specific best practices as given for example in the HSF’s Best Practice Guidelines.

### Documentation

* The project should provide different kinds of documentation:
  * Basic documentation.
  * User documentation.
  * Reference manual.
  * Tutorials (e.g. notebooks).
* The project should provide specific training for users to use the software product.

### Sustainability

* The project should be maintained by at least one long-term maintainer, preferably with a future commitment to the software of at least 1 year (subject to funding).
* The project should produce at least one new release a year if there are changes and fixes that have been accumulated.
* The project should use an issue tracker for tracking individual issues.
* The project should acknowledge a majority of bug reports submitted in the last 1-3 months (inclusive); the response need not include a fix.
* The project should respond to a majority (>50%) of enhancement requests in the last 1-3 months (inclusive).

### Level of Adoption

* The software should be adopted by at least 2 experiments/collaborations/projects.

## Research Software Infrastructure

A.k.a. *research software infrastructure* in the 3-tier model.

This is for projects that are adopted by several collaborations and/or
experiments with a strong and long-term community support model. All the
criteria for Tier 2 should be fulfilled, with the addition of the following
criteria.

### Documentation

* The project should provide specific training for users to use the software product or tool on a frequency of once a year.
* The project should organise user workshops or engage in community events as a means to collect feedback from the user community.

### Sustainability

* The project should be actively maintained and produce at least one new release a year if there are changes, and produce patch releases as relevant to include fixes that have been accumulated.
* The project should be maintained by more than one long-term maintainer, preferably with a future commitment to the software of at least 1 year (subject to funding).
* The project should acknowledge a majority of bug reports submitted in the last 1-4 weeks (inclusive); the response need not include a fix.
* The project should respond to a majority (>50%) of enhancement requests in the last 1-4 weeks (inclusive).

### Level of Adoption

* The software should be adopted by several (>2) large collaborations/projects and should be adopted by a number (>1) of small experiments/collaborations/projects.
