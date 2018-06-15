---
title: "HSF Packaging Group Meeting #25, June 13, 2018"
layout: default
---

# {{page.title}}


Agenda 
=======

[https://indico.cern.ch/event/730538/](https://indico.cern.ch/event/730538/)

Participants: Graeme Stewart, Ben Morgan, Ben Couturier, Marco
Clemencic, Chris Burr, Pere Mato, Guilherme Amadio, Chris Green, Rafal
Pacholek, Patrick Gartung, Dmitri Konstantinov, Liz Sexton-Kennedy,
David Lange

Introduction - Ben
==================
-   Please advertise the [RSE conference](http://rse.ac.uk/conf2018/), even though we're not presenting.
-   Feedback on next meeting date please - let us know if a meeting on 4 July
    makes sense.

R&D Projects - Graeme
=====================
-   LIM Workshop
    -   Excellent overview of current and short term improvements to
        tools/procedures from CERN/LHC experiments.
    -   Not so much about future of packaging overall - that is more within the
        remit of this WG.
-   WG so far:
    -   Use cases doc useful and well received.
    -   Test stack less so. Any good PM can handle them. But good to
        check availability of build recipes for them.
    -   Test drive: good for basic tests, experiments need a lot more.
        Useful for comparison, but not a short term priority. Continue
        but at a lower priority
-   Points from LIM:
    -   Reliance on system vs packager built.
    -   System vs Build the World tension - maybe take each end as
        "sweet spots" for work?
-   Deployment/Production:
    -   Bet on Containers? Future resources mean we have less control
        over customization of site system packages.
    -   More customization -\> less stability.
    -   Also means we don't have to try and build modern suite on old
        system.
    -   Doesn't mean "fat" containers, can use CVMFS.
        -   Ben C: Also want flexibility to have "fat" containers to
            handle use case when site doesn't support CVMFS.
        -   Chris: Unlikely to get CVMFS at many HPC sites.
        -   Graeme: Can have "fat" container only bringing in what's
            needed. HPC may also have very fast filesystems, so maybe
            less cost in starting up fat system.
        -   Marco/Ben C: Need tools to build the container, layer
            appropriately. Problem isn't sharing the compilation (we
            have resources), it's sharing the tools to organise the
            container.
        -   Tension between when we have CVMFS and when we don't. In the
            later case, we have to put everything we need (and only
            that) in the container image.
-   Full Stacks?
    -   Entire self contained stacks have advantages in consistency.
    -   But... Is a lot of work. E.g. in min of 350 packages for
        functional development machine in CentOS7, Ubuntu 16.
    -   Only seems manageble by leveraging work of larger project (take
        pick of distro or project, e.g., Portage, Nix)
    -   This use case matches well with Chris Burr's work in LHCb.
    -   Liz: CMS also used to build from libc upwards, possibly still
        now. David: not building libc upwards now.
-   Modernise the Base OS?
    -   Many rebuilds due to old (ancient!) base OS.
    -   So need newer Python/C++ etc.
    -   Updating the toolchain (Compiler/Interpreters), hence ABI
        changes require us to rebuild packages we otherwise might
        take from the system.
    -   Advantage: focus on core task of packaging HEP software.
    -   Worries: Longevity of release and support? Alleviated by
        containerised deployment?
    -   What about release timescales?
    -   Developing software now for deployment in 2020. So need newer
        compiler now, to ensure working software then.
    -   Compiler vs binutils vs assembler consistency?
    -   This is only to explore the possibility of this, not to solve
        everything.
    -   What about running older stacks? Containers/Emulators could help
        here, related to whole data preservation effort(s).
    -   David: Site specific software like EOS? Graeme: also xrootd,
        probably explore later in the R&D effort. Ben C: In Dirac, use
        binary compatible xrootd plugin, but that uses middleware
        compatible interfaces.
-   Developers
    -   Containers lighter than VMs, but developers do prefer to run
        native.
    -   On Linux: "prefix" environment as in Nix/Portage (independent of
        distro other than kernel) worthwhile exploring.
    -   MacOS/Windows? More tricky to support from base toolchains.
    -   Use of such a "prefix/view" explored by FNAL's SpackDev.
-   "R&D Inventory"
    -   Recognise strengths - a common place to share ideas and
        experience
    -   Small doc on each ongoing project: very light (who/what/where).
-   Other areas where we could improve: docs.

Test Drive Round Table - All
============================
-   Javier has a container with LCGCMake almost ready
    -   Questions on the core list of packages - not the whole superset, see the trimmed list in
        the test drive area.
-   Experience of dockers on Mac not so great - slow and slow disks
    -   E.g., Qt5 compile took a very long time.
    -   There are [special mount
        options](https://docs.docker.com/storage/bind-mounts)
        for volumes that relax synchronisation on OS X and improve
        performance a lot, e.g., \`delegated\`.


