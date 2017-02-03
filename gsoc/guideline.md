---
title: "HSF GSoC Mentor Guideline 2017"
author: "Benedikt Hegner"
layout: default
---

# How to Add a New project in HSF GSoC

## Instructions for Adding a New Project

 * Option A: email GSoC administrators: Sergei Gleyzer <a href="mailto:sergei@cern.ch">sergei@cern.ch</a> and Enric Tejedor Saavedra <a href="mailto:etejedor@cern.ch">etejedor@cern.ch</a>
 * Option B (via git): 
   * fork git repository 
   * add project_YOURPROJECT.md (for example project_ROOT.md)
   * add _gsocproposals/proposal_YOURPROJECTyourproposal.md (for example proposal_ROOTspark.md)
   * add a front matter as given in this [example](https://raw.githubusercontent.com/HEP-SF/hep-sf.github.io/master/_gsocproposals/proposal_ROOTspark.md)
   * make a pull request
   
## Instructions for Adding a New Organization

Projects are attached to an organization (e.g. CERN, Fermilab...). If you are a new organization, you need to create 
a MD file describing your organization in `gsoc` directory. This is a very simple file, containing only a *front matter* section that defines the attributes of
your organization. 

A project is attached to an organization by its attribute `organization` that must match (case insensitive) the `organization` attribute defined in organization MD file. This attribute can be a single value or a list. For a list, use the following syntax in the *front matter* section:

```
organization:
 - CERN
 - Fermilab
```

To create a new organization, copy `gsoc/cern.md` and edit its contents as appropriate.


## HSF GSoC Mentor Guideline 2017

Date: 01/23/2017

[HSF GSoC 2017 Mentor Guideline](https://docs.google.com/document/d/1EzHknPt3NCCk860gOltTWx_iOg5vmCwKS9p0zKBX1YY/pub)


