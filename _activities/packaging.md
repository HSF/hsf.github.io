---
title: Packaging
layout: plain
redirect_from: /workinggroups/2015/11/04/packaging.html
---

The software packaging and distribution activity and working group addresses common issues, tools, and approaches to building and distributing the software stacks used by HEP experiments.

The group is currently convened by Ben Morgan (Warwick) and Graeme Stewart (CERN), who took over from Liz Sexton-Kennedy (FNAL) and Benedikt Hegner (CERN) in October 2017.

# Getting Involved

Everyone is welcome to participate and contribute on the forum and to the ongoing meetings:

[Packaging Group Discussion Forum](https://groups.google.com/forum/#!forum/hep-sf-packaging-wg){:target="_hsf_packaging_forum}

[Packaging Group Meetings Indico](https://indico.cern.ch/category/7975/){:target="_hsf_packaging_indico"}

# Goals
The aim of this working group is to foster communication and exchange among the experiments' librarians. We identified various topics to work on, including

  1. Common build recipes and tools
  2. How to take most advantage of technologies like containers
  3. Exchange of experience with the CMake eco-system

## Common Build Recipes and Tools
Software development in high energy physics follows the paradigm of open-source software (OSS). Experiments as well as the theory community heavily rely on software being developed outside of the field. Creating a consistent and working stack out of 100s of packages, on a variety of platforms is a non-trivial task. Within the field multiple technical solutions exist to configure and build those stacks. None of this work is experiment specific and our working group agrees that this effort is being duplicated.

We held [an initial series of meetings](https://indico.cern.ch/category/7975/) to look at the existing build and packaging solutions, including the community-driven projects

  * [aliBuild](http://alisw.github.io/alibuild/)
  * [cmsBuild](https://github.com/cmsbuild/cmsdist)
  * [LCGCMake](https://gitlab.cern.ch/sft/lcgcmake/)
  * [Worch](https://github.com/brettviren/worch)
  * Contractor (no public documentation)
  * SciSoft (no public documentation)

and the general open-source projects

  * [Conda](http://conda.pydata.org/docs/)
  * [homebrew](http://brew.sh/)
  * [Nix](https://nixos.org/nix/)
  * [Portage](https://wiki.gentoo.org/wiki/Project:Portage)
  * [Spack](https://github.com/spack/spack)

The summary of our initial findings is found in the [Technical note on Build Tools](/technical_notes.html).

## Existing build recipes

  * [cet-is](https://cdcvs.fnal.gov/redmine/projects/build-framework/repository)
  * [cmsdist recipes](https://github.com/cmsbuild/cmsdist)
  * [HEP-SPACK recipes](https://github.com/HSF/hep-spack)
  * [conda recipes by Daniela Remenska ](https://github.com/remenska/root-conda-recipes)
  * [conda recipes by Brett Viren](https://github.com/brettviren/lbne-conda) (deprecated)
  * [aliDist recipes](https://github.com/alisw/alidist)
  * [LCGCMake recipes](https://gitlab.cern.ch/sft/lcgcmake)

# Other resources

  * [HSF Organization on GitHub](https://github.com/HSF)
  * [HSF cmaketools package ](https://github.com/HSF/cmaketools)
  * [Draft Technical Note on Platform Naming Conventions](/technical_notes.html)
