---
title: "HSF GSoC Mentor Guidelines"
author: "Benedikt Hegner"
layout: default
---

# How to Add a New project in HSF GSoC

## Instructions for Adding a New Proposal

 * Option A: email GSoC [administrators](mailto:hsf-gsoc-admin@googlegroups.com) (currently: Valentin Volkl, Wouter Deconinck, Baidyanath Kundu)
 * Option B (via git): 
   * fork [git repository](https://github.com/HEP-SF/hep-sf.github.io) 
   * add `_gsocproposals/YEAR/proposal_YOURPROJECTyourproposal.md` (look at this example: [`proposal_ROOTspark.md`](https://raw.githubusercontent.com/HSF/hsf.github.io/master/_gsocproposals/2018/proposal_ROOTspark.md))
   * add a front matter as given in this
   [example](https://raw.githubusercontent.com/HSF/hsf.github.io/master/_gsocprojects/2019/project_HSF.md)
      * Make sure the `year` attribute is correct for your proposal
   * add an organization description to the current year folder (if not already done) as given in this [example](https://raw.githubusercontent.com/HSF/hsf.github.io/master/_gsocorgs/2020/cern.md):
      * It can be copied from last year if still valid
      * Remember that the name of the `organization: YOURORGANIZATION` will need to be referenced in the proposal and for each mentor
      * Add a logo to [images](https://github.com/HSF/hsf.github.io/tree/master/images)
   * update the list of mentors (at the end of the proposal AND in the file `gsoc/YEAR/mentors.md`)
      * Follow this format: `YOURNAME [YOUR@MAIL](mailto:YOUR@MAIL) YOURORGANIZATION`
      * The main mentor (responsible with student evaluation and exchanging with the Admins) has to be put in bold letters, only at the end of each proposal.
      * Insert mentor names sorted rather than to the end of the list

   * make a pull request (add as reviewers the admins). At least one approval from the admins is required.

**Every proposal must be attached to an organization (e.g. CERN, Fermilab...) and to a project (e.g. ROOT, GeantV...).** If you add your own proposal yourself, be sure add the appropriate `organization` and `project` attributes (not case sensitive) in the *front-matter* section of the proposal. See next sections if you need to add a new organization or project but if you use an existing project and organization for your proposal you don't have to do anything else that what was described above.

**Proposals have to be tuned this year for 90-hour 175-hour or 350h project length.** For 175h projects please propose coding topics having well-defined deliverables, rather than R&D with unforeseen timeline and results. Remember that your student will effectively work in total only about 30 days (6 hours/day) on the project!

Please do not forget to add **essential information** like *level of difficulty*, *duration* and an explicit statement about *mentor availability*. 
   
## Instructions for Adding a New Project

Proposals are attached to a project (e.g. ROOT, CMS...). If you want to add a project for your proposal, you need to create 
a Markdown file describing your project in `_gsocprojects/YEAR` directory (must start with `project_`,
look at [HSF project](https://raw.githubusercontent.com/HSF/hsf.github.io/master/_gsocprojects/2019/project_HSF.md) for an example).
This is a very simple file, containing only a *front matter* section that defines the attributes of
your organization. The 2 mandatory attributes are `project` (your project name) and `layout` (which must be `default`).
In addition you can use 2 optional attributes:

* `title`: the name of the project to use in the page title. By default, `project` attribute is used.
* `description`: a description of your project that will be added before the list of proposals attached to the project.

It can be several lines: look at the [example](https://raw.githubusercontent.com/hep-sf/hep-sf.github.io/master/_gsocprojects/2018/project_SixTrack.md)
for detailed syntax. The content is a standard Markdown text indented by at least one space (the number is not important
but must be the same for all lines).

* `logo`: the logo file name in directory `images` (please name your logo `PROJECTNAME-logo.png` and ensure it is less than 100kB)

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
[_gsocorgs/2020/cern.md](https://raw.githubusercontent.com/hep-sf/hep-sf.github.io/master/_gsocorgs/2020/cern.md),
create a file for your organization and edit its contents as appropriate.

Organization logos should be called `ORGANIZATION-logo.png` and be less than 100kB in size.

## HSF GSoC Mentor Guideline 2024

[2024 HSF GSoC Mentor Guideline](https://docs.google.com/document/d/1hrXwP_ebebhFO8q3Qj9lXQsyVA2QBQMKeAck5ReuZ_E/edit)
