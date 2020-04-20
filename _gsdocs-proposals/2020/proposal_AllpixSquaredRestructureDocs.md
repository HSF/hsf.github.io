---
title: Generic Proposal Title
layout: gsoc_proposal
project: AllpixSquared
year: 2020
organization:
  - DESY
---

## Description of project idea

Allpix Squared is a mid-size project with a very active and diverse user community. Users come from all sorts of backgrounds, from PhD or master students to senior scientists, and from different fields. They come with different levels of knowledge on programming, on Monte Carlo simulations or on silicon detectors.
Having a comprehensive documentation was always a strong point of this project, and our goal for the documentation is to provide each user (from novice student to potential contributor and seasoned developer) the information he needs.

The documentation of our project consists of several parts, which live in different spaces as detailed below:

* **Website:** The first point of contact should be the website. It is built using the static website generator `hugo` based on the very simple `beautiful-hugo` theme and contains, most importantly, the "news" section used for publishing release announcements and release notes. Among others, users can furthermore find installation information and screenshots illustrating different use cases.
* **User Manual:** The main documentation of the framework consists of a 160-page user manual document which is generated from LaTeX code in the main software repository as well as Markdown files for individual parts of the framework - translated to LaTeX using `pandoc`. This happens automatically for new releases and it is published
    * Online as HTML version with a link from the website (using `latex2html`)
    * As PDF document, linked from the website (using `pdflatex`)
    
* **Doxygen Code Reference:** In addition to the user manual, also the source code is heavily documented and a HTML documentation of the code base is automatically generated using `doxygen` and deployed on the website.

With over 3.5 years of continuous development and additions, the documentation has become a bit cluttered and we would like to streamline it with your help:

* **Content:** We would like to separate more clearly which parts of the documentation are intended for users which are not expected to alter a single line of code - and which parts aim at developers who would like to contribute to the project or would like to extend their own copy. Also, we would like to review the current user manual for potentially lacking information or areas where we could improve.
* **Infrastructure:** We would like to streamline the way we present the documentation and especially improve its online representation. Optimally we would end up with a streamlined, fully-integrated online presence which coherently presents news, manual and code reference. One possibility for this would e.g. be moving the documentation to [Docsy.dev](https://www.docsy.dev/). The challenging part about this is that we would like to keep as much as possible of our current automatic deployment and workflow.
* **Bonus task:** For those of you who would like to dive a bit deeper into the scientific depth of this project - we currently do have a few examples for users to understand how to start using the framework and how to use certain features, but they are not very nicely presented and not very extensively documented. They could use a good polishing. Ultimately, these and further examples can be streamlined to follow a tutorial-like workflow.

## Project duration

We are open for both standard-length projects (3 months) and long-running (6 months) projects, depending on what you think is required to achieve the results we are aiming for.
Given the good overall level of documentation of the project, we think a standard project might suffice.

## Related material

  * Project website: [http://cern.ch/allpix-squared](http://cern.ch/allpix-squared)
  * Repository of website (hugo): [APSQ Website @ CERn GitLab](https://gitlab.cern.ch/allpix-squared/allpix-squared-website)
  * Project repository: [Allpix Squared @ CERN GitLab](https://gitlab.cern.ch/allpix-squared/allpix-squared)
  * Documentation within the repository: [doc/usermanual](https://gitlab.cern.ch/allpix-squared/allpix-squared/-/tree/master/doc%2Fusermanual)
  * Online documentation: [Online User Manual](https://project-allpix-squared.web.cern.ch/project-allpix-squared/usermanual/allpix-manual.html)
  * PDF documentation: [PDF User Manual](https://project-allpix-squared.web.cern.ch/project-allpix-squared/usermanual/allpix-manual.pdf)
  * Doxygen code reference: [Code Reference](https://project-allpix-squared.web.cern.ch/project-allpix-squared/reference)

## Expected results

* A restructured user manual which clearly separates content intended for users and developers
* A reviewed manual with previously missing information on the project and the framework
* A streamlined online presence which better integrates project website, documentation and code reference

## Experience required
Our current documentation workflow consists of a few tools and in order to rip them apart it would be good to have a solid understanding of:
LaTeX, Doxygen, pandoc, hugo, git, GitLab and its Continuous Integration - as well as of all the new and cool tools that you will introduce to make our documentation sparkle.

## Mentors
  * [Paul Schütze](mailto:paul.schuetze@desy.de)
  * [Simon Spannagel](mailto:simon.spannagel@desy.de)
