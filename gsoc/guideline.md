---
title: "HSF GSoC Mentor Guidelines"
author: "Benedikt Hegner"
layout: default
---

# How to Add a New project in HSF GSoC

## Instructions for Adding a New Proposal

 * Option A: email GSoC administrators: [Andrei Gheata](mailto:Andrei.Gheata@cern.ch), [Antoine Pérus](mailto:perus@lal.in2p3.fr)  and [Javier Cervantes Villanueva](mailto:javier.cervantes.villanueva@cern.ch) 
 * Option B (via git): 
   * fork [git repository](https://github.com/HEP-SF/hep-sf.github.io) 
   * add `_gsocproposals/YEAR/proposal_YOURPROJECTyourproposal.md` (for example `proposal_ROOTspark.md`)
   * add a front matter as given in this
   [example](https://raw.githubusercontent.com/HSF/hsf.github.io/master/_gsocprojects/2019/project_HSF.md)
      * Make sure the `year` attribute is correct for your proposal
   * make a pull request

**Every proposal must be attached to an organization (e.g. CERN, Fermilab...) and to a project (e.g. ROOT, GeantV...).** If you add your own proposal yourself, be sure add the appropriate `organization` and `project` attributes (not case sensitive) in the *front-matter* section of the proposal. See next sections if you need to add a new organization or project but if you use an existing project and organization for your proposal you don't have to do anything else that what was described above.
   
## Instructions for Adding a New Project

Proposals are attached to aproject (e.g. ROOT, CMS...). If you want to add a project for your proposal, you need to create 
a Markdown file describing your project in `_gsocprojects/2019` directory (must start with `project_`,
look at [HSF project](https://raw.githubusercontent.com/HSF/hsf.github.io/master/_gsocprojects/2019/project_HSF.md) for an example).
This is a very simple file, containing only a *front matter* section that defines the attributes of
your organization. The 2 mandatory attributes are `project` (your project name) and `layout` (which must be `default`).
In addition you can use 2 optional attributes:

* `title`: the name of the project to use in the page title. By default, `project` attribute is used.
* `description`: a description of your project that will be added before the list of proposals attached to the project.

It can be several lines: look at the [example](https://raw.githubusercontent.com/hep-sf/hep-sf.github.io/master/_gsocprojects/2018/project_SixTrack.md)
for detailed syntax. The content is a standard Markdown text idented by at least one space (the number is not important
but must be the same for all lines).

* `logo`: the logo file name in directory `images`

A proposal is attached to a project by its attribute `project` that must match (not case sensitive) the `project`
attribute defined in project MD file. This attribute can be a single value or a list. For a list, use the following
syntax in the *front matter* section:

```
project:
 - ROOT
 - GeantV
```

## Instructions for Adding a New Organization

Proposals are attached to an organization (e.g. CERN, Fermilab...). If you are a new organization, you need to create 
a MD file describing your organization in `gsoc` directory. This is a very simple file, containing only a
*front matter* section that defines the attributes of your organization.

A proposal is attached to an organization by its attribute `organization` that must match (case insensitive) the
`organization` attribute defined in organization MD file. This attribute can be a single value or a list. For a
list, use the following syntax in the *front matter* section:

```
organization:
 - CERN
 - Fermilab
```

To create a new organization, copy
[_gsocorgs/2019/cern.md](https://raw.githubusercontent.com/hep-sf/hep-sf.github.io/master/_gsocorgs/2019/cern.md),
create a file for your organization and edit its contents as appropriate.


## HSF GSoC Mentor Guideline 2019

[2019 HSF GSoC Mentor Guideline](https://docs.google.com/document/d/1K_VewNIUQS9U9KYhkVJCiCiYnBBNsjdRTUpYRjxTTcA/pub)


