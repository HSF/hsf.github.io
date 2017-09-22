---
title: Packaging
layout: plain
redirect_from: /workinggroups/2015/11/04/packaging.html
---

The software packaging and distribution activity and working group is getting underway to address common issues, tools, and approaches, convened by Liz Sexton-Kennedy (FNAL) and Benedikt Hegner (CERN). The activity was launched with a meeting on Feb 25 2015. All are welcome to join the forum and participate:

[Software Packaging Tools Discussion Forum](https://groups.google.com/forum/#!forum/hep-sf-packaging-wg)

# Goals
The aim of this working group is to foster communication and exchange among the experiments' librarians. We identified various topics to work on. Some of them are:

  1. Common build recipes and tools
  2. How to take most advantage of technologies like dockers
  3. Exchange of experience with the CMake eco-system

We started by tackling the first item.

## Common Build Recipes and Tools
Software development in high energy physics follows the paradigm of open-source software (OSS). Experiments as well as the theory community heavily rely on software being developed outside of the field. Creating a consistent and working stack out of 100s of packages, on a variety of platforms is a non-trivial task. Within the field multiple technical solutions exist to configure and build those stacks. None of this work is experiment specific and our working group agrees that this effort is being duplicated.

We held various meetings to look at the existing build and packaging solutions

{:.table .table-hover .table-condensed .table-striped}
| Date                                              | Main topic            |
| ------------------------------------------------- | --------------------- |
| [25.2.2015](https://indico.cern.ch/event/373973/) | Brainstorming session |
| [2.6.2015](https://indico.cern.ch/event/398344/)  | DUNE approach         |
| [9.6.2015](https://indico.cern.ch/event/400272)   | LCGCMake              |
| [16.6.2015](https://indico.cern.ch/event/402229/) | cmsBuild              |
| [23.6.2015](https://indico.cern.ch/event/403790/) | SciSoft, Contractor   |
| [4.11.2015](https://indico.cern.ch/event/457365/) | AliBuild              |
| [18.11.2015](https://indico.cern.ch/event/462334/) | Conda                |
| [10.02.2016](https://indico.cern.ch/event/484006/) | Spack                |
| [02.11.2017](https://indico.cern.ch/event/581338/) | Gentoo's Portage     |

During these meetings we looked at the following community-driven projects

  * [aliBuild](http://alisw.github.io/alibuild/)
  * [cmsBuild](https://github.com/cmsbuild/cmsdist)
  * [LCGCMake](https://gitlab.cern.ch/sft/lcgcmake/)
  * [Worch](https://github.com/brettviren/worch)
  * Contractor (no public documentation)
  * SciSoft (no public documentation)

and the following open-source projects

  * [Conda](https://conda.io/docs/){:data-proofer-ignore} <!-- Unknown error from Travis HTML proofing -->
  * [homebrew](http://brew.sh/)
  * [Nix](https://nixos.org/nix/)
  * [Portage](https://wiki.gentoo.org/wiki/Project:Portage)
  * [Spack](https://github.com/LLNL/spack) 

The summary of our analysis has been summarized in a [Technical note on Build Tools](/technical_notes.html)

## Existing build recipes

  * [cet-is](https://cdcvs.fnal.gov/redmine/projects/build-framework/repository)
  * [cmsdist recipes](https://github.com/cmsbuild/cmsdist)
  * [HEP-SPACK recipes](https://github.com/HEP-SF/hep-spack)
  * [conda recipes by Daniela Remenska ](https://github.com/remenska/root-conda-recipes)
  * [conda recipes by Brett Viren](https://github.com/brettviren/lbne-conda) (deprecated)
  * [aliDist recipes](https://github.com/alisw/alidist)
  * [LCGCMake recipes](https://gitlab.cern.ch/sft/lcgcmake)


# Other resources

  * [HSF Organization on GitHub](https://github.com/HEP-SF)
  * [HSF cmaketools package ](https://github.com/HEP-SF/cmaketools)
  * [Draft Technical Note on Platform Naming Conventions](/technical_notes.html)
