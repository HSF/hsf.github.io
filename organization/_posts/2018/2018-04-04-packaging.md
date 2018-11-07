---
title: "HSF Packaging Group Meeting #22, April 4, 2018"
layout: meetings
---

# {{page.title}}

Agenda
======
[https://indico.cern.ch/event/716297/](https://indico.cern.ch/event/716297/)

Participants: Graeme Stewart, Javier Cervantes Villanueva, Martin Ritter, Oana Boeriu, Patricia Mendez, Patrick Gartung, Pere Mato, Chris Green, Emil Obreshkov, Giulio Eulisse, Ben Couturier, Marco Clemencic, Chris Burr, Marco Petric

Introduction - Graeme
===========================
- LIM workshop will be 30 May.
- HSF rebranding - use the new name for the mailing list: `hsf-packaging-wg@googlegroups.com`. 


Summary of Packaging discussion in Naples - Giulio
==================================================

- Need to now do a sensible test drive on the tools.

- Test cases for the development environment probably need further expansion.
    - Incremental builds within packages might need to be reviewed (e.g., modify ROOT and rebuild only a few libraries without recompiling every downstream piece). This is not guaranteed to work, but with *caveat emptor*, can be useful to be able to accelerate development.
    - Alibuild allows developing several packages at the same time. CMT also (although this is deprecated). LCG CMake? (Marco Cle: it doesn't).

- Discussion on containerisation and its impact on packaging:
	- Giulio: We cannot have them everywhere so we still need all the features in the use cases anyway.
	- Ben: Having containers in most places changes the requirements.
	- Graeme: If all experiments gathered to ask for the same container solution (via WLCG), maybe the sites would migrate more quickly.
	- Containers **do** seem to be the future for production environments.
	    - Use experience can be rather different (native is best for developers).
	    - Can containers be used at the DAQ level? Not so clear, but we have more control here (Ben).
	- Martin - there is also docker in user space now. Experiment can bootstrap containers in their own pilot jobs.
	- OSG have an automatic way to build singularity containers from docker, when user has signed an AUP (so deployment is easier)


Nix Test Drive Report - Graeme
===================================

- Re. install failures for `python-3.6 jupyter`, which Nix channel did you use?
    - Unstable is installed by default - should change that (as `root`)
- Useful to have an overlay yourself to fix things (but this is not the first thing in the docs)
- There are more science packages in Nix - just along a different path (ROOT, Geant4)
- RapidJSON is there (but not for `x86_64-darwin`, which is odd as it's a header only package)
    - Post facto: this is the [package search interface](https://nixos.org/nixos/packages.html)
    - The Nix RapidJSON recipe also fixes the compile issue
- Dependencies - these are the dependencies you want to configure; you can encode these in the recipe
    - Upstream has some "native build inputs"
    - There is some extra magic in the build customisers
- Pere: Can you have a package called `out`? Buildpkg is a bit more robust than this shell script example, but it would be a bit tricky in that case.
- `nix-build` being retired in favour of `nix <argument>`, git style CLI.
    - There are some ways to find the `all-packages.nix` files more easily.
- Can Nix have different builds of packages side by side?
    - A. Yes, with an arbitrary degree of complexity - it's one of the things it does well.
- For python you can specify exactly what python modules should be available.
- Confirmed that one way to relocate for Spack is to make the `RPATH` relative.
- For CMVFS - could use an overlayfs or have a fake CVMFS (that has what you need and is writable), e.g., do this in Hydra
- Use case for developers requires "writing" to CVMFS.
    - Jakob could have thoughts on the use of overlayfs here .

- Giulio - personal experience was that it was confusing at the beginning, which is one thing that is off putting for a roll out to many users who are not experts
    - One hack is to just build "normally" on top of a nix environment, but that’s mixing two very different things, not great.

- Clarify, goal is to find a *common solution that saves effort*, but we need to make an honest investment into all the candidate tools to be able to decide on the best (so work for the test stack will involve some duplication).

AOB
===

- Brett Viren has [Wirecell and dependencies](https://github.com/WireCell/wire-cell-spack) in Spack, so we could look at that? 
- Are we really going to be able to do things in common? e.g., multiple ROOT options.
    - Official recipe should be flexible enough to cover major cases - can write things which cover most cases (in the end you should always be able to override).
    - ROOT is possibly the most convoluted example for building, lost of options, no plugins, users want different things
- Patrick Gartung has [CMSSW dependencies in spack](https://github.com/gartung/cmssw-spack).
- Pere - has been looking at multiple HW architectures and could report on that.

Next Meeting: [18 April 2018](https://indico.cern.ch/event/716297/).
