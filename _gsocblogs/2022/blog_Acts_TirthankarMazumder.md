---
project: Acts 
title: Vectorized Linear Algebra Implementation for Acts
author: Tirthankar Mazumder
avatar: https://github.com/wermos.png
date: 10.02.2022
year: 2022
layout: blog_post
logo: ACTSlogo.gif
intro: |
  This blog is about my experiences and what I learned during my GSoC project, which involved adding a new math backend to algebra-plugins, to make Acts faster.
---

Hi everyone! Since starting this year, blogs are mandatory for all CERN-HSF contributors, I decided to take this time to make my own blog. I have written about my journey extensively there. Do [give it a visit](https://wermos.github.io/blog/)!

I have broken down the midterm project report into multiple blog posts:

The [first blog post](https://wermos.github.io/blog/gsoc/gsoc-first-blog-post/) discusses what GSoC is in general, for those who might just stumble upon my blog by happenstance.

The [second blog post](https://wermos.github.io/blog/gsoc/gsoc-the-details-of-my-project/) delves into the technical details about what my project actually is, what repository I would be working with, mentions our weekly meeting schedule, and describes my three mentors.

The [third blog post](https://wermos.github.io/blog/gsoc/gsoc-the-work-so-far/) finishes up the trilogy by exhaustively discussing the work up till now, including benchmarking data and conclusions, and the current direction of the work.

That being said, I will also share a short report of the work of the work I am doing, and the link to the things I have done so far:

## My progress

### Fast 5×5
One of the main things we need, to efficiently figure out what to improve first, is a comprehensive benchmarking suite for the existing math backends. To that end, I added Google Benchmark to the [`algebra-plugins` repository](https://github.com/acts-project/algebra-plugins), in [PR #69](https://github.com/acts-project/algebra-plugins/pull/69).

Then, my mentors and I spent a lot of time testing out 3 possible math backend alternatives (the custom-made `fast5x5`, `blaze`, and `Fastor` in a repository of mine called [Fast 5×5](https://github.com/wermos/Fast5x5). This repository was something I forked from some [prior work on this front](https://gitlab.in2p3.fr/CodeursIntensifs/Fast5x5).

Prior to my project, the performance of the matrix computations done in Fast5×5 had been found to be unsatisfactory, and one of the possibilities that was entertained, was writing the matrix operation code ourselves, tailor-made for the smaller dimensions that ACTS uses. The result was the custom-written Fast5×5 library, which uses [`xsimd`](https://github.com/xtensor-stack/xsimd/) under the hood for a platform-agnostic way of exposing SIMD intrinsics to the end user.

Once we started with the GSoC project, my mentors asked me to look at the repository and get an idea of where we stand with respect to the prior work in this project. I improved the repository in many ways, including (but not limited to)
- I removed a `Dockerfile` and a Bash script (among other things) in [`2a62718`](https://github.com/wermos/Fast5x5/commit/2a627183458fd25366087c2be8e8d3fd14cde294) because it would not be required in this project.
- redoing the project structure to make it easier for outsiders to understand where things reside. This was done multiple times, for example, in [`85ad3fd`](https://github.com/wermos/Fast5x5/commit/85ad3fd1de82ee6313bb2685e2a02f368d7e5e6a), [`20d4fb9`](https://github.com/wermos/Fast5x5/commit/20d4fb9940f01c547272cb3b2e775335992d8ea6), [`125a084`](https://github.com/wermos/Fast5x5/commit/125a084f374c92936a2bc9f8e41d561c31346588), and [`69bd4d8`](https://github.com/wermos/Fast5x5/commit/69bd4d8cc3f6e3aeb0c6baf21d9510b931984799).
- adding `xsimd` and `Eigen` as Git submodules instead of requiring the end user to have these libraries already installed in their system. This has the added advantage of allowing us to easily switch between versions of `Eigen` and `xsimd`, as the maintainers of those repositories continue to make bugfixes and improvements. This was done in [`21aad0e`](https://github.com/wermos/Fast5x5/commit/21aad0e2a38425e0c959b259359e6e67084ec282)
- updating `Eigen` (first in [`18dbd4e`](https://github.com/wermos/Fast5x5/commit/18dbd4eab48ed6dcda108c4545632e9d431d6305), and then in [`0e702b0`](https://github.com/wermos/Fast5x5/commit/0e702b0607c28631a24875d94aa1a5acb80a5554)) and `xsimd` (in [`e1e1c71`](https://github.com/wermos/Fast5x5/commit/e1e1c71aed01d2aee8e24a8b63bcf4360916df81)). The original Fast5×5 project had not been touched since 2019. In the 3 years since then, all these libraries had undergone some major versions releases.
- changing the benchmarking method from using `/usr/bin/time` to using Google Benchmark. Using a simple timer like `/usr/bin/time` is goog for a first-order approxmiation, but not good for an in-depth analysis. Any one run of a benchmark might be very fast due to it being the only thing running on the system, or very slow due to many background tasks simultaneously running. For this reason, using a library dedicated to micro-benchmarks like Google Benchmark is the best way to generate reliable benchmarks. I did this in commit [`d5b40f4`](https://github.com/wermos/Fast5x5/commit/d5b40f478668863102f0c03e98d9918af1e2e2b5).
- changing the way the random matrix generation works in [`ff821df`](https://github.com/wermos/Fast5x5/commit/ff821df8906a226749408e24b40e627d21fa3894). The original Fast 5×5 code was using index based operations to fill up the matrix, which is not the best way to generate reliable benchmarking data.

For the comprehensive list of changes and improvements, be sure to check out my [blog post](https://wermos.github.io/blog/gsoc/gsoc-the-work-so-far/) dedicated to the work I did!

### Final Conclusions

We spent quite a bit of time writing benchmarks for testing the performance of `Eigen`, `fast5x5`, `blaze`, and `Fastor` in various matrix computation tasks like matrix multiplication, matrix inversion, computing the similarity transform and computing coordinate transforms in multiple matrix dimensions (4×4, 6×6, 6×8, and 8×8).

We ran the benchmarks on my own machine, and also a subset of these tests on a Threadripper machine used for ACTS work. After a deep look into the assembly generated by each backend, as well as a look at the performance each library brought to the table, we decided to use Fastor because it was consistently first or second in all the benchmarks we threw at it, and its assembly generation was the cleanest (i.e. free of cruft and pointless register shuffling).

Hence, the next steps for me and my GSoC project are to integrate Fastor into `algebra-plugins`, and write the front-end for it so that we can see Fastor in action in a more realistic setting. To that end, I already integrated Fastor to the repository in [PR #77](https://github.com/acts-project/algebra-plugins/pull/77), and am currently working on writing the front-end.
