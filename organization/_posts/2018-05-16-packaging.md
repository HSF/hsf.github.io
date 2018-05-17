---
title: "HSF Packaging Group Meeting #24, May 16, 2018"
layout: default
---

# {{page.title}}

Agenda
======
[https://indico.cern.ch/event/727088/](https://indico.cern.ch/event/727088/)

Participants: Graeme Stewart, Ben Morgan, Oana Boeriu, Patrick Gartung, Chris Burr, Rafal Pacholek, Javier Cervantes Villanueva, Guilherme Amadio, Chris Green

[Introduction - Graeme](https://indico.cern.ch/event/727088/contributions/2992555/attachments/1643141/2640438/HSF_Packaging_Group_Intro_2018-05-16.pdf)
===========================
- Follow on from micro-architecture builds: Ben has [link on HSF/packaging github](https://github.com/HSF/packaging/tree/master/istools) to discuss this/collate information. PRs to update welcome!
- [HSF tech note on naming build platforms](http://hepsoftwarefoundation.org/technical_notes.html) promoted to consultation document
  - Needs people to take a look and finalise
  - E.g., Add micro-microarchitecture piece, compiler release numbers (e.g. for GCC only major version should matter now)
  - How to comment/edit? To check, but probably on HSF/technotes GitHub.
- Graeme: Overview on [Guix Cern Computing Seminar](https://indico.cern.ch/event/719851/) (pronounced "gix"!)
  - No slides, but link to recording available
  - Nutshell: very similar to nix in how packages built, hashed.
  - High reproducibility (up to 95% bitwise identical).
  - Nix-style runtime env setup
  - Everything lives under `/guix` (must be writable, user builds supported by daemon). Binary builds supported, but not relocatable (prefix enters package hash).
  - User Base: mostly HPC, big shared filesystems user are close to (Graeme commented at seminar that typical HEP case is different; CVMFS etc)
  - Good points like Nix: reproducibility, user control, composability (overlays)
  - Differences: Scheme language vs Nix DSL (claimed Scheme makes use/extension easier). No mention of license
  - Interesting for us? Yes, but lives very close to Nix. Limited resources, so not a priority unless someone wants to take it on. Maybe more important if we move in a Nix-like direction. Then differences between Nix DSL vs Scheme etc.
  - Some observations: seems to have smaller package base than Nix, no apparent macOS distribution (but might build from source).
- [CHEP timetable now available](https://indico.cern.ch/event/587955/timetable/#20180709)
  - [Our packaging talk](https://indico.cern.ch/event/587955/sessions/266674/#20180711) followed by two Spack talks (one by Chris Green, one by IceCube)
  - Guilherme: will have a [talk on robust binaries](https://indico.cern.ch/event/587955/contributions/2938043/) (RPATH, how linker finds libraries etc).
- Today: Test Drive Round Table
- SFT LIM Workshop in two weeks, so next meeting 13th June.
- Just let Graeme and Ben know of any material you'd like to present.


[Test Driving Round Table - Ben, all](https://indico.cern.ch/event/727088/contributions/2992556/attachments/1643140/2640160/HSF-TestStack.pdf)
========================
- Ben:
  - [Github repo](https://github.com/HSF/packaging/tree/master/testdrive) has been updated with more instructions and guidance
  - One directory per packager
  - Overall README and a template for each specific tool
  - Walk through the minimum packages and versions
  - Demonstrate basic functionality first
  - Template can be filled in so that each package manager is well described and easy to use by the non-expert test driver
- Graeme: time limited on progress on Nix due to meetings and travel.
- Chris Burr: With Nix, now packaging LHCb up to reconstruction packages.
- Javier - has discussed with Patrick which repo to use for package descriptions. HSF looks the best. CERN one is very out of date.
- Patrick has built most of the CMSSW stack, most updates went into HSF. Chris has been adding more versions, PRs going directly upstream into Spack. There is a FNAL fork that has useful changes to Spack itself and to some of the packages.
  - Could add that information to packaging github repo, so that people could find it.
  - Shazad has been working on a tool to convert SCRAM->CMake configurations, but it was taking too long for CMS (10 minutes - too slow!). CMake 3.11 is improved. Ninja target was faster than make. Some technical improvements being worked on.
- Ben: Giulio has submitted a PR for an [aliBuild testdrive](https://github.com/HSF/packaging/pull/12). Comments/Review by all welcome!
- Guilherme - wants to make a special container for the Portage. Will put information on the website.

AOB
===
- Due to the [LIM workshop on 30 May](https://indico.cern.ch/event/720948/) the next meeting will be on the [13th June](https://indico.cern.ch/event/730538/)
- Noted the "HSF" user on DockerHub : Ask Graeme if you want to be added here to add images for test driving, etc.

