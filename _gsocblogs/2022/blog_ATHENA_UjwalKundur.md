---
project: ATHENA
title: Electromagnetic Cluster Finding on GPUs
author: Ujwal Kundur
avatar: https://avatars.githubusercontent.com/u/54140487?s=400&u=75e8458ece81adfb9b12bca1aaaa2aa23f4c6b1a&v=4
date: 22.07.2022
year: 2022
layout: blog_post
logo: ATHENA-logo.png
intro: |
  Parallelizing the IslandCluster Algorithm for the EIC ECAL - A foray into HPC and Hardware Accelerators.
---

---

### Code Contributions

1. [Container with SYCL Support](https://eicweb.phy.anl.gov/containers/eic_container/-/merge_requests/306)
2. [SYCL Enabled IslandClustering](https://eicweb.phy.anl.gov/EIC/juggler/-/merge_requests/469)

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

My mentor, Dr. Wouter Deconinck, was kind enough to grant me access to Compute Canada's HPC facilities for testing on a full-blown Linux environment.
I'll have figured out a way to Profile and hopefully finish porting the Algorithm by mid-August.

#### Post Midterm

---

## Turning Point

> 1.08.2022 - 23.08.2022

This period was by far the most gruelling. Without VTune, I had no guidance as to which functions I should be focusing on. While I tried reading documentation and looked up quite a few videos and articles on the web, I could not make progress.

My mentors helped me here by providing an alternative build plan which enabled me to directly use **Juggler** (the algorithm library which IslandCluster is a part of) without the *Gaudi Framework*. This was possible due to the **PODIO** package, which allows read / write to ROOT files.

With a bit of tweaking, tuning and reading lots of documentation, I arrived at the following workflow:

1. Generate Events using an existing script used for benchmarking - [`gen_particles.py`](https://eicweb.phy.anl.gov/EIC/benchmarks/reconstruction_benchmarks/-/blob/master/benchmarks/clustering/scripts/gen_particles.py)

2. Simulate particle interactions with `ddsim`

3. Use Gaudi to run the initial Hit Digitization + Cell-ID mapping and output the Digitized and Reconstructed hits for clustering as a ROOT file.

My test program kicks in here and reads this ROOT file and outputs the result of IslandClustering. There were a few linking errors with ROOT and I had to (again) look up documentation and use an arcane flag `-Wl,--copy-dt-needed-entries` to instruct the linker to look up symbols recursively across libraries.

It took us a whole month to reach this point and I was really happy when the hard work paid off.

This testing code was used for the remainder of the project and enabled me to profile and parallelize the Algorithm properly without interference. The Testing code can be found in my repo [here](https://github.com/Ajax-Light/GSoC-cernhsf-final).

## Sick SYCL Code

> 23.08.2022 - 23.09.2022

As a lot of time was spent trying to get stuff to work, I didn't really have any Code contributions to show. With the final submission dates looming and nothing to show, I had to request an extension by 2 weeks which was approved by both my mentor and Org-Admin. This was a life-saver and I had enough time to work on the C++ / SYCL side of things.

I was pretty new to C++ when I started and working on the project helped me learn a lot about the language features. Learning SYCL taught me to think in terms of parallelism and performance. After spending a good few weeks reading research papers and parallel algorithms to replicate a DFS done as a part of IslandCluster, I came up with a simple algorithm to emulate hit assignments, which I detail in the code. This period again, was very taxing mentally as I had to learn a lot of things quickly but I am all the better for it.

However, the final results were pretty disappointing. SYCL code performed worse than "normal" sequential code at varying workloads. Why? No GPU support - During this time I realized that the Intel provided OneAPI containers that oneapi_jug_xl was based on did not provide **CUDA** as a backend as it was still in experimental stage. This was another blow to an already difficult project. This meant we had to re-evaluate the entire SYCL setup and it was agreed upon that this was out of scope of the current project.

Since we had no access to AMD GPUs - which support OpenCL by default (the GPGPU scene is dominated by NVidia and CUDA), I had to settle for performance comparisions of both SYCL and Non-SYCL code on the same AMD EPYC 32-core CPU used in Compute Canada's HPC systems. Hence, the comparision results you see below are sub-par and show poor performance on SYCL's part. However, I believe that given proper hardware, software stack and tuning, many algorithms in Juggler will greatly benefit from SYCL support.

![Wall-Time Cmpr](https://github.com/Ajax-Light/GSoC-cernhsf-final/raw/master/reports/WallTime-compare.png)

The SYCLized code was merged into master, Merge Request [here](https://eicweb.phy.anl.gov/EIC/juggler/-/merge_requests/469).

## Conclusion

Few things which remain to be worked on are:

* Smaller image size for `oneapi_jug_xl`
* Adding `CUDA` support to the oneapi containers
* Further optimizations and tuning for the SYCLized `IslandCluster` Algorithm

While the project has been *way*, *way* harder to work on than I had initially anticipated, it was incredibly rewarding and I'm grateful to have had the opportunity to contribute to such an exotic project and work with amazing people in a completely different discipline from mine.

I cannot thank my mentors, Dr. Wouter Deconinck and Sylvester Joosten enough for their help and for being so patient with me even when I bombard them with questions :)

I hope to continue contributing to Juggler and the EIC Software after GSoC as well and am looking forward to see the software in action in the near future.

If you've reached the bottom of this page, Thank You!

Cheers,
Ujwal.

---

Reach out to me at: ujwal.kundur@gmail.com \|\| [GitHub](https://github.com/Ajax-Light) \|\| [LinkedIn](https://www.linkedin.com/in/ujwal-kundur/)

---
