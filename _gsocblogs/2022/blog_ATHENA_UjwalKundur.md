---
project: ATHENA
title: A foray into HPC and Hardware Accelerators
author: Ujwal Kundur
date: 22.07.2022
year: 2022
layout: blog_post
logo: ATHENA-logo.png
intro: |
  Parallelizing the IslandCluster Algorithm for the EIC ECAL, a progress report.
---

## Introduction

Hello readers, I'm Ujwal and this is my first blogpost ever. Is this how YouTubers feel like when they talk in front of a camera? :)

This post is meant to be a progress update to my mentors, amusing read for the physicist-developer and absolute nonsense for the uninitiated. Nevertheless, I hope this is accessible to the interested layman without sacrificing the technical accuracy so coveted in Physics.

The project is pretty straight-forward, at least on the surface; Porting a clustering algorithm used in the reconstruction of particle collision events at the Electron-Ion Collider (**EIC**) to **SYCL**.
The clustering algorithm needs to scale in order to process increasing number of hits as the Sensor resolution is upgraded over the years, this requires hardware acceleration which is already being used significantly in AI/ML to train models using GPUs. Other hardware accelerators do exist, for example, FPGAs and ASICs (Application Specific Integrated Circuits) which are prominently used in Bitcoin-mining. We stick to GPUs in this project.

SYCL aims to make programmers' lives easier by allowing us to target all these different hardware architectures from a single codebase. While many implementations of the SYCL standard exist, similar to how there are many implementations of *ISO C*, Intel's offering - **Intel OneAPI DPC++** (Data Parallel C++) seems to be the most mature project and we stick to it for our SYCL needs.

## The Software Stack and SYCL Set-up

> 13.06.2022 - 15.07.2022

The first task at hand was to add SYCL support to the existing software stack. The EIC software is distributed as containers - both Docker and Singularity Images are available.
The Docker Images are available on DockerHub [here](https://hub.docker.com/u/eicweb). To quickly get started with simulations, you can run the *jug_xl* container like so:

``` docker run -it eicweb/jug_xl:nightly ```

The Singularity Images are available on **CVMFS** (CERN VM File System).

The existing software stack has 3 layers:

1) Base Layer - consisting of the base *Debian* Images

2) Jug_dev - containing the dependencies for various simulation software. E.g: ROOT, Geant4, etc.

3) Jug_xl - containing the full simulation stack. E.g: Juggler, DD4HEP, etc.

You can find more information in the [Athena Docs](https://doc.athena-eic.org/en/latest/overview/containers.html).

The challenge was making sure all the components play nice and work together, which of course is easier said than done. There were multiple version conflicts, Compiler mismatches, etc. After a ton of trail and error, I found that using *Debian Stable* (Debian 11 - Bullseye at the time of writing) as the base fixed most of the issues. The experience increased my respect for the Debian Devs and package maintainers, 'tis a tough job.

My contributions were merged into master, Merge Request can be found [here](https://eicweb.phy.anl.gov/containers/eic_container/-/merge_requests/306). You can run the container with oneAPI support like so:

``` docker run -it eicweb/oneapi_jug_xl:nightly ```

Now I could move onto the actual C++ code!

## Event Horizon

> 15.07.2022 - 1.08.2022

My satisfaction with having a working container lasted but a few days. Intel's **VTune** Profiler which was meant to guide my optimization / parallelization efforts doesn't work with Python in containers as detailed in their [Docs](https://www.intel.com/content/www/us/en/develop/documentation/vtune-cookbook/top/configuration-recipes/profiling-in-docker-container.html).
Why Python? The reconstruction algorithms are executed by the *Gaudi framework* which has up-to-date Python bindings, but the C++ Invocations and Documentation is dated and I could not make it work without Python bindings. This was unexpected and we are still trying to sort this out.

My mentor, Dr. Wouter Deconinck was kind enough to grant me access to Compute Canada's HPC facilities for testing on a full blown Linux environment.
I'll have figured out a way to Profile and hopefully finish Porting the Algorithm by mid-August and maybe I could write about how we solved the current problem in my final post.

It has been a great learning experience and I'm really grateful to have awesome mentors and a cool community which I can be a part of. So Thanks CERN-HSF!!

If you've reached the bottom of this page, Thank You! See you in a month,
Cheers,
Ujwal.

---

Reach out to me at: ujwal.kundur@gmail.com \|\| [GitHub](https://github.com/Ajax-Light)

---
