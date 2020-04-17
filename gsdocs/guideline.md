---
title: "HSF GSoC Mentor Guidelines"
author: "Benedikt Hegner"
layout: default
---

# How to Add a New project in HSF GSDocs

## Instructions for Adding a New Proposal

 * Option A: email GSoC [administrators](mailto:hsf-gsdocs-admin@googlegroups.com) (currently: Andrei Gheata, Antoine Pérus and Xavier Valls)
 * Option B (via git): 
   * fork [git repository](https://github.com/HEP-SF/hep-sf.github.io) 
   * add `_gsdocs-proposals/YEAR/proposal_YOURPROJECTyourproposal.md` (look at this example: [proposal_ROOTgeneric.md](https://raw.githubusercontent.com/HSF/hsf.github.io/master/_gsdocs-proposals/2020/proposal_ROOTgeneric.md))
   * use the above template and fill all sections, which are required
      * Make sure the `year` attribute is correct for your proposal
   * add an organization description to the current year folder (if not already done) as given in this [example](https://raw.githubusercontent.com/HSF/hsf.github.io/master/_gsdocs-orgs/2020/cern.md):
      * It can be copied from the _gsocorgs folder if available, but remember to modify it to include gsdocs_proposal.ext instead of gsoc_proposal.ext 
      * Remember that the name of the `organization: YOURORGANIZATION` will need to be referenced in the proposal and for each mentor
      * Add a logo to [images](https://github.com/HSF/hsf.github.io/tree/master/images)
   * update the list of mentors (`gsdocs/YEAR/mentors.md`)
      * Follow this format: `YOURNAME [YOUR@MAIL](mailto:YOUR@MAIL) YOURORGANIZATION`
      * Insert mentor names sorted by last name rather than to the end of the list
   * make a pull request

**Every proposal must be attached to an organization (e.g. CERN, Fermilab...) and to a project (e.g. ROOT, GeantV...).** If you add your own proposal yourself, be sure add the appropriate `organization` and `project` attributes (not case sensitive) in the *front-matter* section of the proposal. See next sections if you need to add a new organization or project but if you use an existing project and organization for your proposal you don't have to do anything else that what was described above.
   
## Instructions for Adding a New Project

Proposals are attached to a project (e.g. ROOT, CMS...). If you want to add a project for your proposal, you need to create 
a Markdown file describing your project in `_gsdocs-projects/YEAR` directory (must start with `project_`,
look at [ROOT project](https://raw.githubusercontent.com/HSF/hsf.github.io/master/_gsdocs-projects/2020/project_ROOT.md) for an example).
This is a very simple file, containing only a *front matter* section that defines the attributes of
your organization. The 2 mandatory attributes are `project` (your project name) and `layout` (which must be `default`).
In addition you can use 2 optional attributes:

* `title`: the name of the project to use in the page title. By default, `project` attribute is used.
* `description`: a description of your project that will be added before the list of proposals attached to the project.

It can be several lines look at the ROOT example above for detailed syntax. The content is a standard Markdown text indented by at least one space (the number is not important but must be the same for all lines).

* `logo`: the logo file name in directory `images` (please name your logo `PROJECTNAME-logo.png` and ensure it is less than 100kB)

A proposal is attached to a project by its attribute `project` that must match (not case sensitive) the `project`
attribute defined in project MD file. This attribute can only a single value.

Note that there are already many projects in the folder `_gsocprojects`. If you plan to reuse one of those, make sure you copu to the directory `gsdocs-projects` and change at least the inclusion of `gsdocs_project.ext` instead of `gsoc_project.ext`

## Instructions for Adding a New Organization

Proposals are attached to an organization (e.g. CERN, Fermilab...). If you are a new organization, you need to create 
a MD file describing your organization in `gsdocs-orgs` directory. This is a very simple file, containing only a
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
[_gsdocs-orgs/2020/cern.md](https://raw.githubusercontent.com/HSF/hsf.github.io/master/_gsdocs-orgs/2020/cern.md), create a file for your organization and edit its contents as appropriate.

Organization logos should be called `ORGANIZATION-logo.png` and be less than 100kB in size.

## Season of Docs Resources 2020

 * [Announcement for Season of Docs 2020](https://groups.google.com/forum/#!topic/season-of-docs-announce/x04Gl7D4dm8)
 * [Mentor guide for Season of Docs 2020](https://developers.google.com/season-of-docs/docs/mentor-guide)
 * [Guideline for what project ideas could contain](https://developers.google.com/season-of-docs/docs/project-ideas)

