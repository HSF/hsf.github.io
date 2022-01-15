---
title: "HSF Packaging Group Meeting #19, February 21, 2018"
layout: meetings
---

# {{page.title}}

Agenda
======

[https://indico.cern.ch/event/704402/](https://indico.cern.ch/event/704402/)

Participants: Ben Morgan, Chris Green, Guilherme Amadio, Jim Amundson,
Oana Boeriu, Patrick Gartung, Graeme Stewart, Emil Obreshkov, Giulio
Eulisse, Marco Clemencic, Javier Cervantes Villanueva, Shahzad Malik
Muzaffar, Geri Ganis

Introduction - Graeme
=====================

-   Very brief! No updates on Use Cases and TestStack. Graeme and Ben
    will discuss later this week.
-   Talk on AliBuild - perspective of "user/developer" rather than
    "packager"
-   Open discussion on Spack, using Javier's talk/question from last
    time as a starting point

AliBuild Experience - Giulio
============================

-   aliBuild: packaging/build/setup tool for ALICE experiment. Used to
    build whole stack and prepare user work area/environment.
-   Aimed at both end user and packager/librarian
-   Started in July 2015, full implementation/use by end users in May
    2016
    -   \~5 months for initial implementation and infrastructure
    -   Ongoing aggregated 1FTE to improve build recipes, bug fixes,
        etc.
-   About 300-500 users (distinct installs)
-   Even mix of OS/Arch/Versions
-   Small set of current versions
-   Right choices:
    -   Git for all sources, even third party
    -   Bash for all build recipes, main point is allowing contributions
        from non-experts
    -   YAML for metadata
    -   Conventions over templates: conventions on environment that
        recipe runs in.
    -   Tarballs as file formats, rpms/dpkgs in separate step by FPM
    -   Dependency Management:
        -   No central "config" - derived only from set of dependencies
            (Graeme: back propagation? Yes, with build order determined from topological analysis)
        -   No recipe inheritance (e.g. not class-based like Spack's
            "CMakePackage")
            -   Generally quite explicit - prefer always writing
                "configure/make/make install" in the recipe than a
                function/method that does this behind the scenes.
        -   Recipe customisation: CSS like set of modifiers
            -   Change metadata and s// in the build scripts
    -   Question: can I build root6 with py2 rather than py3? Yes: via
        the recipe customisation.
    -   Question: How to handle optional deps (e.g. root6 plus "X")?
        Introduce X as a dependency, then recipe checks if dependency
        is available.
-   Right choices (other)
    -   aliBuild both a package manager and setup tool.
    -   Reuse homebrew/Redhat-devtools, Ubuntu pkgs. Good for end users,
        production is still on Grid with fully specified dependency
        chain. Focused on packages that are experiment/physics
        important (e.g Root, generators) vs common tools like zlib/gcc
        (barring version compatibility checks).
    -   Opt in Google Analytics to monitor audience/use cases
    -   Prefer locally cloned sources to allow contribution (e.g. ROOT)
-   Things that could be improved:
    -   Use of Python language - not the language itself, rather
        possibility of interaction with user's python environment
        (e.g. Conda, Py2, Py3).
    -   Use of rsync to distribute binary artifacts. Maybe S3
        distribution to scale to large user count?
    -   Recipes current have to hand-code modulefile generation: Maybe
        generate from package metadata?
    -   Split out Docker support
    -   Embrace CVMFS more, e.g., take packages from cvmfs, if available
    -   Recipes all in one place - break out into separate
        repos/Nix-overlays
-   Very long term ideas
    -   Use Nix!
    -   If GVFS is available, i.e. all sources in same place, could use
        Bazel build system.
-   Patrick: macOS builds? Does SIP have to be disabled? No, uses
    install\_name\_tool to relocate/prevent SIP issues.
-   Graeme: Environment setup, if driven from end result, does this
    result in a cascade of information? Mitigated by the smaller ALICE
    stack, plus some aggregation of information. Somewhat similar to
    views.
-   How specific is the tool to ALICE? FAIR is also using/trying it,
    though shares commonality with ALICE. SHiP tried it, but not only
    partially used, some issues with support levels. Graeme: They did
    like the portability, and had a small stack so easy to build
    everything. Giulio: Again, very similar stack, so quite a bit of
    reuse.

Spack Discussion - All
======================
-   Postponed until next meeting!

AOB
===
Next Meeting: 7 March 2018, let Graeme/Ben know on any topics/talks.

Talks about Gentoo Prefix at FOSDEM 2015 and 2018:
* [https://fosdem.org/2015/schedule/event/providing\_an\_lts\_distro\_with\_gentoo\_prefix](https://fosdem.org/2015/schedule/event/providing_an_lts_distro_with_gentoo_prefix)
* [https://fosdem.org/2018/schedule/event/unix\_windows\_gentoo](https://fosdem.org/2018/schedule/event/unix_windows_gentoo)
