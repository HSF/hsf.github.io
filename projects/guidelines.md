---
title: "Affiliated Projects and Software Guidelines"
author: Eduardo Rodrigues, Pere Mato
layout: plain
---

In a spirit of openness and flexibility, the HSF maintains an evolving checklist of best practices for HSF Affiliated Projects and Software, rather than a set of requirements.
[HSF Affiliated Projects and Software]({{ site.baseurl }}/projects/affiliated.html) need to abide by (at least a subset of) the guidelines,
which are used for their endorsement and attribution of Bronze, Silver or Gold levels of recognition.

The guidelines have been created to:
* Encourage projects to follow best practices;
* Help new projects discover what those practices are; and
* Help users know which projects are following best practices, meant as a guarantee of quality.

The guidelines can be updated in light of updates or release of community practices, such as those emerging from e.g. the [EVERSE project](https://everse.software).

The guidelines take inspiration from the [“old HSF page”](https://hepsoftwarefoundation.org/project_guidelines.html) and from the [Open Source Security Foundation (OpenSSF)’s page](https://www.bestpractices.dev/en/criteria).

## Best-practice Guidelines

### General guidelines

Any software library should strive to the following:
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

### C++ specific guidelines

[This repository](https://github.com/cpp-best-practices/cppbestpractices)
contains a Collaborative Collection of C++ Best Practices.
[WIP - more information will be provided in due course.]

### Julia specific guidelines

The Julia [language documentation](https://docs.julialang.org/) contains a Style Guide.
[WIP - more information will be provided in due course.]

### Python specific guidelines

The organisation [Scientific Python](https://scientific-python.org/) provides a rather comprehensiVE [Development Guide](https://learn.scientific-python.org/development/)
with a set of [Topical Guides](https://learn.scientific-python.org/development/guides/)
for the development and maintenance of Python libraries, which the HSF strongly encourages.
These guides provide a "cookiecutter" template for the setup of a new package,
and cover important topics such as packaging, code styling and documentation, testing and test coverage.

Compliance with respect to the guidelines is provided via a "repo review” framework
([GitHub repository](https://github.com/scientific-python/repo-review)).
The review can even be done [directly in a browser](https://learn.scientific-python.org/development/guides/repo-review/) for repositories hosted on GitHub!

## Endorsement Badge Levels

Three endorsement levels are defined to distinguish mainly the level of maturity, developer support, community support and engagement: Bronze, Silver and Gold.
For each level a number of requisites need to be demonstrated.
Each level adds more requisites to the previous level.
These requisites lay in three major categories:
* Software engineering practices followed by the project (as described in the Best-practice Guideline section and with specifics for the programming language ecosystem).
* Sustainability and support structures of the project (e.g. number of active developers, discussion fora, documentation, training events, time to respond to issues, etc.)
* Level of adoption of the software by experiments and other projects, hence the impact of the project.

The keywords *MUST*, *SHOULD*, *MAY* that appear in the criteria in this document are to be interpreted as described in [RFC 2119](https://datatracker.ietf.org/doc/html/rfc2119):
* The term MUST is an absolute requirement, and MUST NOT is an absolute prohibition.
* The term SHOULD indicates a criterion that is normally required, but there may exist valid reasons in particular circumstances to ignore it.
* The term MAY provides one way something can be done, e.g., to make it clear that the described implementation may differ and be acceptable.

### Bronze

The purpose of this entry level is for a young endeavour, likely evolving from and within a collaboration or experiment, but with the potential for other communities or experiments to use. At this level the category of best software practices is what is mainly required.

#### Basics
* The project SHOULD follow general and language-specific best practices as given for example in the HSF’s Best Practice Guidelines.
* The project source code MUST reside on a version-controlled repository that is publicly readable and has a URL (e.g., GitHub, GitLab).
* The README file at the top level MUST describe what the software does (what problem does it solve?).
* The project website or repository MUST provide information on how to:
obtain, provide feedback (as bug reports or enhancements), and contribute to the software.
* The contribution process MUST be explained (e.g., are pull requests used?).
* The software MUST be released on an Open Software license.
* The project MUST post the license(s) of its results in a standard location in their source repository.

#### Documentation

* The project MUST provide basic documentation for its software.
* The project MUST provide reference documentation that describes the external interface (both input and output) of the software produced by the project.
* The project MUST have one or more mechanisms for discussion (including proposed changes and issues) that are searchable, allow messages and topics to be addressed by URL, enable new people to participate in some of the discussions, and do not require client-side installation of proprietary software.
* The project MUST provide documentation in English and be able to accept bug reports and comments about code in English.

#### Change Control

* The project's source repository MUST track what changes were made, who made the changes, and when the changes were made.
* To enable collaborative review, the project's source repository SHOULD include interim versions for review between releases; it SHOULD NOT include only final releases.
* The project results MUST have a unique version identifier for each release intended to be used by users.
  We recommend to use either [Semantic Versioning](https://semver.org) or [Calendar Versioning](https://calver.org) as appropriate, since popular schemes.
* The project MUST provide, in each release, release notes that are a human-readable summary of major changes in that release to help users determine if they should upgrade and what the upgrade impact will be.
The release notes SHOULD NOT be the raw output of a version control log (e.g., the "git log" command results are not release notes).

#### Sustainability

* The project MUST be maintained.
* The project SHOULD have at least one long-term maintainer with a contract longer than 2 years.
* The project MUST provide a process for users to submit bug reports (e.g., using an issue tracker or a mailing list).
* The project SHOULD use an issue tracker for tracking individual issues.
* The project SHOULD acknowledge a majority of bug reports submitted in the last 2-12 months (inclusive); the response need not include a fix.
* The project SHOULD respond to a majority (>50%) of enhancement requests in the last 2-12 months (inclusive).
* The project MUST have a publicly available archive for reports and responses for later searching.

#### Level of adoption

* The software produced by the project MUST be of interest for the HEP experiments.
* The software SHOULD be adopted by at least one experiment/collaboration/project.

### Silver

Are for projects aiming for Gold but in an earlier phase towards strong community support and adoption (e.g., adoption is still relatively shy, maintenance is not secured at least in the medium term by more than a single person).
High standards of software engineering should be met.
All the criteria for Bronze MUST be fulfilled, with the addition of the following criteria.

#### Basics

* The project MUST follow general and language-specific best practices as given for example in the HSF’s Best Practice Guidelines.

#### Documentation

* The project MUST provide different kinds of documentation:
  - Basic documentation.
  - User documentation.
  - Reference manual.
  - Tutorials (e.g. notebooks).
  - The project SHOULD provide specific training for users to use the software product.

#### Sustainability

* The project MUST be maintained and produce at least one new release a year if are changes and fixes that have been accumulated..
* The project MUST have at least one long-term maintainer with a contract longer than 2 years.
* The project MUST use an issue tracker for tracking individual issues.
* The project MUST acknowledge a majority of bug reports submitted in the last 1-3 months (inclusive); the response need not include a fix.
* The project SHOULD respond to a majority (>50%) of enhancement requests in the last 1-3 months (inclusive).

#### Level of adoption

* The software MUST be adopted by at least 2 experiments/collaborations/projects.

### Gold

HSF endorsement level for projects that are adopted by several collaborations and/or experiments with a strong and long-term community support model.
All the criteria for Silver MUST be fulfilled, with the addition of the following criteria.

#### Documentation

* The project MUST provide specific training for users to use the software product or tool on a frequency of once a year.
* The project SHOULD organise user workshops or engage in community events as a means to collect feedback from the user community.

#### Sustainability

* The project MUST be actively maintained and produce at least one new release a year if there are changes, and as needed patch releases to include fixes that have been accumulated.
* The project MUST have at least 3 long-term maintainers with a contract longer than 2 years.
* The project MUST acknowledge a majority of bug reports submitted in the last 1-4 weeks (inclusive); the response need not include a fix.
* The project MUST respond to a majority (>50%) of enhancement requests in the last 1-4 weeks (inclusive).

#### Level of adoption

* The software MUST be adopted by several (>2) large collaborations/projects and SHOULD be adopted by a number (>1) of small experiments/collaborations/projects.
