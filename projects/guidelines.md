---
title: "Affiliated Projects and Software Guidelines"
author: Eduardo Rodrigues, Pere Mato, Graeme Stewart, Caterina Doglioni, Stefan Roiser
layout: plain
---

The HSF curates a list of best practices for HSF Affiliated Projects and
Software, that makes software easy to adopt, trust and contribute to.
[HSF Affiliated Projects and Software]({{ site.baseurl }}/projects/affiliated.html)
adhere to these best practices.

The guidelines have been created to:

* Encourage projects to follow best practices;
* Help new projects discover what those practices are; and
* Help users know which projects are following best practices, meant as a guarantee of quality.

The guidelines can be updated in light of updates or release of community practices, such as those emerging from e.g. the [EVERSE project](https://everse.software). For a short summary of the EVERSE project and its goals, follow [this link]({{ site.baseurl }}/projects/everse.html).   

The guidelines take inspiration from an [older HSF project page]( {{
site.baseurl}}/project_guidelines.html) and from the [Open Source Security
Foundation (OpenSSF)’s page](https://www.bestpractices.dev/en/criteria).

Affiliated projects must satisfy minimum standards. 
We also set out further recommendations for community software that projects can work towards. 

## Best-practice Guidelines

The guidelines presented below are replicated in
[this Google template document](https://docs.google.com/document/d/1l8Tkruo0EEHwgRBQPmiHq-i4BuwwiR1choRRMUIv6qY/edit?usp=sharing) to make it easy for package/software evaluators to check things out against each guideline.
Please refer to [here]({{ site.baseurl }}/projects/affiliated.html) for the practicalities of an HSF evaluation.
The General Guidelines are required for affiliation.
The language-specific guidelines point to the best practices of each programming-language ecosystem, which the HSF recommends projects follow.

### General Guidelines

All of the following must be met by a project to be an HSF Affiliated Project:

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

The [Standard C++ Foundation](https://isocpp.org/) maintains a repository with a comprehensive set of [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines).
[This repository](https://github.com/cpp-best-practices/cppbestpractices)
also contains a Collaborative Collection of C++ Best Practices.

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

## Software Tiers and Differentiated Recommendations

Not all software is the same, in terms of purposes and audience.
Differentiated recommendations according to the tier of software
(analysis software, research software tools, research software infrastructure)
are described on a [separate page]({{ site.baseurl }}/projects/software-tiers.html).
