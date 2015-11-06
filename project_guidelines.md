---
title: "Project Guidelines"
author: "Benedikt Hegner"
layout: default
---

# Project Guidelines
The following is a skeleton for the minimal requirements for a project to be considered as part of he HSF. That main motivation being to ensure interoperability and usability of this project in other projects and being able to build consistent software stacks. In addition it should make it easier for other developers to contribute to existing projects.

This is work in progress and details will need to be discussed and agreed with community.

- **Suitable project name**. We need to ensure uniqueness. These names that will be used to name software artifacts like libraries, code namespaces, error messages, etc.  We need to avoid pre-existing trademarks for software products or services.

- **Code in a public repository**. The code should be accessible in anonymous read-only mode by anybody. Repositories like GitHub could be a solution.

- **Developers mailing list**. A mailing list to contact developers should be made available.  Better to have publicly and anonymously accessible
archives and be open for subscription and posting by the public.

- **Project web site**. Each project should have a web site to concentrate all the information useful for the users and developers. More concrete guidelines for the web site could be provided later.  Access to all sources of project information should be granted to search engine spiders.

- **Issue tracking**. Each project provides an issue (bug) tracker for users and developers to interact, allowing to view of both open and closed tickets anonymously by the public. We may recommend a number of common bug trackers.

- **HSF catalog**. Each project should be registered in the HSF software catalog, as well as all the project's dependencies.

- **Mandatory documentation**. A number of documents should be provided by the project. For example:  
  -  Build and install
  -  User’s Guide
  -  Reference Manual
- **Mandatory information**. Information available in the code and web site:
  -  License
  -  Readme
  -  How to contribute
  -  Pre-requisites (dependency on other packages)
  -  List of supported platforms (operating system + compiler)
- **Release Procedure**
  - Different release types: production, development, bug fixes, etc.
  - Version numbering schema (e.g. X.Y.Z)
  - common packaging
- **Best practices**. Defining a number of best practices that will allow building up complex systems.
  - common building instructions (e.g. configure/make )
  - co-existance of multiple versions
  - binary installation relocatability  
  - setting-up runtime environment
  - interface when used by other packages
  - define and run tests
  - generating documentation
