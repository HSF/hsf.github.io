---
title: "HSF Packaging Meeting #32, 27 February, 2019"
layout: meetings
---

# {{page.title}}

## Agenda
[<span class="underline">https://indico.cern.ch/event/796240/</span>](https://indico.cern.ch/event/796240/)
Participants: Graeme Stewart, Ben Morgan, Patrick Gartung, Chris Burr,
Chris Green, Pere Mato, Giulio Eulisse, Javier Cervantes, Geri Ganis,
Martin Ritter, Hadrien Grasland

## Introduction (Ben)
  - FCC Demo, summer student probably comes in June.
  - SuperNEMO:
      - Problem with Homebrew is the size of the final product, 6-7GB
        as all graphics packages are rebuilt (slow and heavy).
          - Similar problems seen when building CMSSW into images.
          - Spack can use a native X11 setup.
          - Conda seems to be a lot smaller (600MB for X11 set of
            packages).
      - Container image is a bit smaller than before.
      - Learning how to deliver a runtime.
      - `spack load -r snemo` is a package - but want to update it to
        be a bundle to get dependencies, to be investigated.
      - Discuss this further next meeting!
  - [HOW2019](https://indico.cern.ch/event/759388/) - will cover main activities and talks given recently in
    the group.
      - Send Graeme any relevant items to highlight.
  - Chris - Conda OS X builds are now working (thanks Henry). Chris
    has merge rights now, so can rapidly deploy stuff!

## Nix (Chris B)
  - Presentation at
    [<span class="underline">NixCon</span>](https://nixcon2018.org)
    last year.
      - Many areas, but lots of users from HPC.
      - E.g: GRICAD HPC (Grenoble), Blue Brain Project, Compute
        Canada, Supercompute/Quantum Chemistry groups,
        Academic/Commercial HPC.
      - Some rebuild (14000 packages) from scratch due to different
        store or security (external binary) concerns.
  - “Single user” Nix prototype:
      - New software: experts or CI.
      - Users: only install indirectly, but experts can use S3.
  - But, multiuser installs more common:
      - Daemon: intermediary between users and nix, security via
        permissions and sandboxing.
  - Nix store can be shared via NFS:
      - GRICAD combine NFS with multiuser Nix.
      - Users can install only on a small set of “head” nodes where
        the daemon runs. All installs still sandboxed/permissions.
      - Graeme: Is the build on NFS? No, these are in `/tmp`.
      - Scales well, but not for LHC.
  - Nix talks to daemon via socket, so can communicate remotely.
      - E.g. Request build to “server”, this then builds, publishes on
        CVMFS.
      - No need for local write access to store.
      - O(1 minute) updates to shared filesystem probably o.k.
  - Store directories have three levels:
      - User level “profile” directories.
      - Versioned Symlinks to “environments”.
      - “Environments” contain symlinks and directories to the actual Package directories.
  - All dirs in Nix store are immutable:
      - So each dir could be RO disk image.
      - CVMFS client could then unpack, maybe faster to ship one
        “large” file than lots of small ones.
      - Dependencies between store dirs known, so could CVMFS prefetch
        deps?
      - Graeme: With disk images, would you need to download entire
        disk image to just access one file? Yes, but depends on access
        model, maybe split packages into smaller subsets. Graeme:
        Might it be related to what CVMFS were looking in exploding
        Docker images onto CVMFS?
  - Nix supports direct builds on Docker/Singularity:
      - Docker images are graphs of layers, but do not have to depend
        on previous.
      - Nix store immutability could improve caching:
          - One package per layer, but docker 125 layer limit.
          - Algorithms to choose best grouping?
      - See blog post for more details.
  - Relocation:
      - Store path is in directory hash.
      - If purity ignored, then can relocate if store prefix is same
        length.
      - Otherwise, can extend/compress hash.
  - Development environments:
      - Nix knows how to build everything, so use for setting up
        development envs with incremental builds?
      - Prototype put together to use generic builder, student at
        NixCon may work more on this.
  - More users of Nix than expected, including HPC.
  - Main weakness still accessibility.
  - How to install a package with specifying build dependencies, i.e.,
    gcc and some dependent library?
      - Can do it, but it will be quite strict on dependencies and may
        rebuild a lot.

## Spack (Chris G)
  - Recap:
      - MVP 1.0 out since 2018-08-29 for RHEL7 only.
      - Updates recently fixed some issues with remote URLs and tag
        updates.
      - Further testing and feedback from all welcome!
  - News and activities:
      - Now a Spack HEP channel for communication:
          - Contact Chris if you want to be added/join this Channel.
      - Some in this group added on Spack GitHub with limited
        authority to commit/merge PRs.
          - Policy to not merge any core or general packages without
            consultation other Spack developers.
          - Intent is to speed up merge/updates of HEP only packages.
      - Major updates to spack-dev in use of spack as external command
        and concretization performance.
      - Work on LArSoft MVP: recipes contributed to upstream Spack for
        Geant4/VecGeom/CLHEP, plus other more specific neutrino ones.
  - Discussion document for desired/in process changes in Spack and/or
    Spack recipes needed by HEP:
      - Link in document.
      - Categorized list of needed/wanted changes to Spack core and
        recipes.
      - Markdown dump will be posted to the Spack\#hep Slack channel
          - Discussion welcome and expected!
      - Examples:
          - External Spack subcommands (like `git <extcmd>`),
            including subcommand facilities and flake8 testing.
            Graeme: Is that part of the CI testing? Yes, is run as an
            automatic check.
          - Layering of Spack installations (“spack chain”, PRs
            present, but needs updating).
          - Better tracking of hashes when recipes updated with new
            variants, so don’t have to reinstall just because a
            variant has been added (all other things in the
            build/dependencies being equal). Javier: at moment, we
            freeze/tag the recipes for given release of the stack.
            Chris: Have `.spack` directories which might provide some
            info that could enable tracking. Chris B: Similar issue in
            Conda, finding binaries has insufficient set of
            constraints.

## AOB
  - Next meeting proposed for 27th March
