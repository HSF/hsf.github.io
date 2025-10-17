---
title: "Affiliated Projects and Software Guidelines"
author: Eduardo Rodrigues, Pere Mato, Graeme Stewart
layout: plain
---

In a spirit of openness and flexibility, the HSF maintains an evolving checklist
of best practices for HSF Affiliated Projects and Software, rather than a set of
strict requirements. [HSF Affiliated Projects and Software]({{ site.baseurl
}}/projects/affiliated.html) need to abide by at least a significant subset of
the guidelines (recognising that some may not be relevant for particular
projects).

The guidelines have been created to:

* Encourage projects to follow best practices;
* Help new projects discover what those practices are; and
* Help users know which projects are following best practices, meant as a guarantee of quality.

The guidelines can be updated in light of updates or release of community practices, such as those emerging from e.g. the [EVERSE project](https://everse.software).

The guidelines take inspiration from an [older HSF project page]( {{
site.baseurl}}/project_guidelines.html) and from the [Open Source Security
Foundation (OpenSSF)’s page](https://www.bestpractices.dev/en/criteria).

There are minimum standards that are required to be an affiliate, but beyond
that we encourage all projects to look at the criteria set out below and work
towards improvements.

## Best-practice Guidelines

The guidelines presented below are replicated in
[this Google template document](https://docs.google.com/document/d/1l8Tkruo0EEHwgRBQPmiHq-i4BuwwiR1choRRMUIv6qY/edit?usp=sharing) to make it easy for package/software evaluators to check things out against each guideline.
Please refer to [here]({{ site.baseurl }}/projects/affiliated.html) for the practicalities of an HSF evaluation.

### General Guidelines

Generally, all of the following must be met by a project to be an HSF Affiliated Project, and exceptions should be justified.

Any software library should strive to fulfil the following:

* **Availability of the code in a public repository.** The code should be accessible in anonymous read-only mode by anybody. GitHub is a very popular solution.
* **A suitable name.** It is good practice to choose a new name (a unique name is better, but often difficult) or at least a name that conveys what the library is about.
Avoid pre-existing trademarks for software products or services.
* **Licensing.** An open-source license should be attached to the software.
* **Installation.** Instructions for how to install the library should be trivial to find, and the installation procedure should be standard for (e.g., at least via pip if the programming language is Python).
* **Documentation.** The code should be suitably documented and a users guide (at least in the format of a “quick start”) should be highlighted. For small libraries a users guide may be provided in the repository README.
* **Test suite.** Code should always be (comprehensively) tested. Test coverage is strongly encouraged and should be displayed on the repository for a straightforward verification of the level of testing implemented.
* **Open to contributors.** The repository should encourage contributions from the community and should never disable pull/merge requests on the developer platform (such as GitHub).
* **Issue tracking.** Each library repository provides an issue (bug, wish) tracker for users and developers to interact, allowing anonymous view of both open and closed tickets.
* **General information.** It is often useful if not necessary to provide extra information such as library dependencies, platforms supported, operating systems supported, etc.

In addition, projects should consider having:

* **A project website.** Such a website is meant to concentrate all the information useful for users as well as developers. (Access to all sources of project information should be granted to search engine spiders.)
* **Developers mailing list.** A mailing list to contact developers should be made available. Better to have publicly and anonymously accessible archives and be open for subscription and posting by the public.

### C++ Specific Guidelines

[This repository](https://github.com/cpp-best-practices/cppbestpractices)
contains a Collaborative Collection of C++ Best Practices.
[WIP - more information will be provided in due course.]

### Julia Specific Guidelines

The Julia [language documentation](https://docs.julialang.org/) contains a Style Guide.
[WIP - more information will be provided in due course.]

### Python Specific Guidelines

The organisation [Scientific Python](https://scientific-python.org/) provides a rather comprehensive [Development Guide](https://learn.scientific-python.org/development/)
with a set of [Topical Guides](https://learn.scientific-python.org/development/guides/)
for the development and maintenance of Python libraries, which the HSF strongly encourages.
These guides provide a "cookiecutter" template for the setup of a new package,
and cover important topics such as packaging, code styling and documentation, testing and test coverage.

Compliance with respect to the guidelines is provided via a "repo review” framework
([GitHub repository](https://github.com/scientific-python/repo-review)).
The review can even be done [directly in a browser](https://learn.scientific-python.org/development/guides/repo-review/) for repositories hosted on GitHub!

## Differentiated Software Best Practices

Recognising that not all software is the same is very important to ensure that
appropriate guidelines are applied. Here we adopt roughly the [*three levels of
software*](https://everse.software/RSQKit/three_tier_view), originally developed by the
[Australian Research Data Commons](https://ardc.edu.au/) (ARDC)
and subsequently adopted by the [EVERSE Project](https://everse.software).

From these levels we have developed guidelines that projects can examine to
understand typical levels of maturity, developer support, community support and
engagement.

These guidelines lie in three major categories:

* Software engineering practices followed by the project (as described in the Best-practice Guideline section and with specifics for the programming language ecosystem).
* Sustainability and support structures of the project (e.g. number of active developers, discussion fora, documentation, training events, time to respond to issues, etc.)
* Level of adoption of the software by experiments and other projects, hence the impact of the project.

### Tier 3 Software

A.k.a. *analysis code* in the 3-tier model.

For the HSF we interpret this as guidelines suitable for a young endeavour,
likely evolving from and within a collaboration or experiment, but with the
potential for other communities or experiments to use. At this level the
category of best software practices is what is mainly required.

#### Basics

* The project should follow general and language-specific best practices as given for example in the HSF’s Best Practice Guidelines.
* The project source code should reside on a version-controlled repository that is publicly readable and has a URL (e.g., GitHub, GitLab).
* The README file at the top level should describe what the software does (what problem does it solve?).
* The project website or repository should provide information on how to:
obtain, provide feedback (as bug reports or enhancements), and contribute to the software.
* The contribution process should be explained (e.g., are pull requests used?).
* The software should be released on an Open Software license.
* The project should post the license(s) of its results in a standard location in their source repository.

#### Documentation

* The project should provide basic documentation for its software.
* The project should provide reference documentation that describes the external interface (both input and output) of the software produced by the project.
* The project should have one or more mechanisms for discussion (including proposed changes and issues) that are searchable, allow messages and topics to be addressed by URL, enable new people to participate in some of the discussions, and do not require client-side installation of proprietary software.
* The project should provide documentation in English and be able to accept bug reports and comments about code in English.

#### Change Control

* The project's source repository should track what changes were made, who made the changes, and when the changes were made.
* To enable collaborative review, the project's source repository should include interim versions for review between releases; it should not include only final releases.
* The project results should have a unique version identifier for each release intended to be used by users.
  We recommend using a well defined versioning scheme that is consistent with practices in your sub-domain, e.g. [Semantic Versioning](https://semver.org) or [Calendar Versioning](https://calver.org).
* The project should provide, in each release, release notes that are a human-readable summary of major changes in that release to help users determine if they should upgrade and what the upgrade impact will be.
* The release notes should not be the raw output of a version control log (e.g., the "git log" command results are not release notes).

#### Sustainability

* The project should be maintained.
* The project should have at least one long-term maintainer with a future commitment to the software of at least 1 year.
* The project should provide a process for users to submit bug reports (e.g., using an issue tracker or a mailing list).
* The project should use an issue tracker for tracking individual issues.
* The project should acknowledge a majority of bug reports submitted in the last 2-12 months (inclusive); the response need not include a fix.
* The project should respond to a majority (>50%) of enhancement requests in the last 2-12 months (inclusive).
* The project should have a publicly available archive for reports and responses for later searching.

#### Level of Adoption

* The software produced by the project should be of interest for the HEP experiments.
* The software should be adopted by at least one experiment/collaboration/project.

### Tier 2

A.k.a. *prototype tools* in the 3-tier model.

In the HSF we interpret this as projects moving towards strong
community support and adoption (e.g., adoption is still relatively shy,
maintenance is not secured at least in the medium term by more than a single
person). High standards of software engineering should be met. All the criteria
for Tier 3 should be fulfilled, with the addition of the following criteria.

#### Basics

* The project should follow general and language-specific best practices as given for example in the HSF’s Best Practice Guidelines.

#### Documentation

* The project should provide different kinds of documentation:
  * Basic documentation.
  * User documentation.
  * Reference manual.
  * Tutorials (e.g. notebooks).
* The project should provide specific training for users to use the software product.

#### Sustainability

* The project should be maintained and produce at least one new release a year if there are changes and fixes that have been accumulated.
* The project should have at least one long-term maintainer with a future commitment to the software of at least 2 years.
* The project should use an issue tracker for tracking individual issues.
* The project should acknowledge a majority of bug reports submitted in the last 1-3 months (inclusive); the response need not include a fix.
* The project should respond to a majority (>50%) of enhancement requests in the last 1-3 months (inclusive).

#### Level of Adoption

* The software should be adopted by at least 2 experiments/collaborations/projects.

### Tier 1

A.k.a. *research software infrastructure* in the 3-tier model.

This is for projects that are adopted by several collaborations and/or
experiments with a strong and long-term community support model. All the
criteria for Tier 2 should be fulfilled, with the addition of the following
criteria.

#### Documentation

* The project should provide specific training for users to use the software product or tool on a frequency of once a year.
* The project should organise user workshops or engage in community events as a means to collect feedback from the user community.

#### Sustainability

* The project should be actively maintained and produce at least one new release a year if there are changes, and produce patch releases as relevant to include fixes that have been accumulated.
* The project should have at least 3 long-term maintainers with a future commitment to the software of at least 2 years.
* The project should acknowledge a majority of bug reports submitted in the last 1-4 weeks (inclusive); the response need not include a fix.
* The project should respond to a majority (>50%) of enhancement requests in the last 1-4 weeks (inclusive).

#### Level of Adoption

* The software should be adopted by several (>2) large collaborations/projects and should be adopted by a number (>1) of small experiments/collaborations/projects.
