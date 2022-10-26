---
project: Acts 
title: Vectorized Linear Algebra Implementation for Acts
author: Tirthankar Mazumder
avatar: https://avatars.githubusercontent.com/u/wermos?s=400&v=4
date: 3.10.2022
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

That being said, I will also share a short report of the work I am doing, and the link to the things I have done so far below:

## My progress

### Fast 5×5
#### Benchmarking Suite for `algebra-plugins`
One of the main things we need, to efficiently figure out what to improve first, is a comprehensive benchmarking suite for the existing math backends. To that end, I added Google Benchmark to the [`algebra-plugins` repository](https://github.com/acts-project/algebra-plugins), in [PR #69](https://github.com/acts-project/algebra-plugins/pull/69). Writing those benchmarks is still a work-in-progress.

#### Investigating Matrix Math Libraries
Then, my mentors and I spent a lot of time testing out 3 possible math backend alternatives (the custom-made `fast5x5`, [`blaze`](https://bitbucket.org/blaze-lib/blaze/src/master/), and [`Fastor`](https://github.com/romeric/Fastor) in a repository of mine called [Fast 5×5](https://github.com/wermos/Fast5x5) and comparing their performance to that of [`Eigen`](https://eigen.tuxfamily.org/index.php?title=Main_Page). This repository was something I forked from some [prior work done on this front](https://gitlab.in2p3.fr/CodeursIntensifs/Fast5x5).

#### How Matrix Math Libraries Work
All matrix math libraries use something called [SIMD](https://en.wikipedia.org/wiki/Single_instruction,_multiple_data) (short for Single Instruction, Multiple Data) to achieve a speed-up compared to a naïve implementation.

Let's take the example of adding two 4-dimensional vectors together. The naïve way of doing it is to take one element from each vector, add it, and then store the result in the result vector. This takes 4 instructions to complete. However, with a SIMD ISA ([Instruction Set Architecture](https://en.wikipedia.org/wiki/Instruction_set_architecture)) all one needs to do is load the 4 elements of each vector into a SIMD register, add them, and store the result in a result vector. This takes just 1 instruction to complete.

<center><a href="https://commons.wikimedia.org/wiki/File:SIMD2.svg#/media/File:SIMD2.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/SIMD2.svg/400px-SIMD2.svg.png" alt="SIMD2.svg"></a></center>

<center><caption>Pictorial Depiction of a SIMD register <br/>(Picture Credits: Wikipedia, courtesy of <a href="https://commons.wikimedia.org/w/index.php?title=User:Vadikus">Vadikus</a>)</caption></center>

<br/>In the same vein, libraries like `Eigen`, `blaze`, `Fastor`, and `fast5x5` use SIMD instructions to create optimized routines for tasks like matrix multiplication.

##### My Project
However, it was found that the performance of Eigen, which is the library that ACTS uses for matrix computations, could be improved. As a proof-of-concept, the Fast5×5 project was created to demonstrate this. The Fast5×5 library which uses [`xsimd`](https://github.com/xtensor-stack/xsimd/) under the hood for a compiler-agnostic way of exposing SIMD intrinsics.

Therefore, my GSoC project is primarily about investigating how much of a performance we stand to gain by switching matrix libraries in these projects ([detray](https://github.com/acts-project/detray), [traccc](https://github.com/acts-project/traccc), and ACTS).

#### Work Summary
Once we started with the GSoC project, my mentors asked me to look at the [original Fast5×5 repository](https://gitlab.in2p3.fr/CodeursIntensifs/Fast5x5) and get an idea of where we stand with respect to the prior work in this project. I improved the repository in many ways, including (but not limited to)
- removing the `Dockerfile` and a Bash script (among other things) in [`2a62718`](https://github.com/wermos/Fast5x5/commit/2a627183458fd25366087c2be8e8d3fd14cde294) because it would not be required in this project.
- revamping the project structure to make it easier for outsiders to understand where things reside. This was done multiple times (in order to keep the project structure up-to-date with the new changes), for example, in [`85ad3fd`](https://github.com/wermos/Fast5x5/commit/85ad3fd1de82ee6313bb2685e2a02f368d7e5e6a), [`20d4fb9`](https://github.com/wermos/Fast5x5/commit/20d4fb9940f01c547272cb3b2e775335992d8ea6), [`125a084`](https://github.com/wermos/Fast5x5/commit/125a084f374c92936a2bc9f8e41d561c31346588), and [`69bd4d8`](https://github.com/wermos/Fast5x5/commit/69bd4d8cc3f6e3aeb0c6baf21d9510b931984799).
- adding `xsimd` and `Eigen` as Git submodules instead of requiring the end user to have these libraries already installed in their system. This has the added advantage of allowing us to easily switch between versions of `Eigen` and `xsimd` as maintainers of those repositories continue to make bugfixes and improvements. This was done in [`21aad0e`](https://github.com/wermos/Fast5x5/commit/21aad0e2a38425e0c959b259359e6e67084ec282)
- updating `Eigen` (first in [`18dbd4e`](https://github.com/wermos/Fast5x5/commit/18dbd4eab48ed6dcda108c4545632e9d431d6305), and then in [`0e702b0`](https://github.com/wermos/Fast5x5/commit/0e702b0607c28631a24875d94aa1a5acb80a5554)) and `xsimd` (in [`e1e1c71`](https://github.com/wermos/Fast5x5/commit/e1e1c71aed01d2aee8e24a8b63bcf4360916df81)). The original Fast5×5 project had not been touched since 2019. In the 3 years since then, all these libraries had undergone some major version releases.
- changing the benchmarking method from using `/usr/bin/time` to using Google Benchmark. Google Benchmark gives us an easy way of automating benchmarking tasks. Moreover, its `DoNotOptimize()` function allows us to guarantee that the operations we are benchmarking were indeed performed and not just optimized out by the compiler.
- changing the way the random matrix generation works in [`ff821df`](https://github.com/wermos/Fast5x5/commit/ff821df8906a226749408e24b40e627d21fa3894). The original Fast 5×5 code used index-based operations to fill up the matrix, which is not the best way to generate reliable benchmarking data. The original code did the following for generating the matrices:

```cpp
float a[SIZE * SIZE];
float b[SIZE * SIZE];

// the BaseMatrix data type in fast5x5.hpp has a constructor
// that takes in C-style arrays. So, the code simply filled
// up two arrays and then made two BaseMatrix objects out
// of them.

for (int i = 0; i < SIZE; i++) {
    for (int j = 0; j < SIZE; j++) {
        a[i * SIZE + j] = i + j;
    }
}

for (int i = 0; i < SIZE; i++) {
    for (int j = 0; j < SIZE; j++) {
        float val;
        if (i == 0 && j == 1) val = -1;
        else if (i == 1 && j == 0) val = 1;
        else if (i > 1 && i == j && i % 2) val = -1;
        else if (i > 1 && i == j && !(i % 2)) val = 1;
        else val = 0;
        b[i * SIZE + j] = val;
    }
}
```

I rewrote the matrix generation code using the random number generators in the `<random>` header, and mimicked `Eigen`'s `Random()` implementation, which generates a random float in the range [-1, 1]:
```cpp
// random.hpp
#include <random>
#include <limits>

inline float randomFloat(float min, float max) {
    // Returns a random real in [min, max].
    static std::uniform_real_distribution<float> distribution(
        min, std::nextafter(max,
            std::numeric_limits<float>::infinity()
            )
        );

    static std::mt19937_64 generator;

    return distribution(generator);
}

// this is the matrix generation code
float a[SIZE * SIZE];

for (int i = 0; i < SIZE; i++) {
    for (int j = 0; j < SIZE; j++) {
        a[i * SIZE + j] = randomFloat(-1.0, 1.0);
    }
}
```
Apart from my work on Fast5×5, I also fired off a [small PR](https://github.com/acts-project/acts/pull/1384) which cleaned up the CI workflow files in the ACTS repository.

For the comprehensive list of changes and improvements, be sure to check out my [blog post](https://wermos.github.io/blog/gsoc/gsoc-the-work-so-far/) dedicated to the work I did!

### Final Conclusions

We spent quite a bit of time writing benchmarks for testing the performance of `Eigen`, `fast5x5`, `blaze`, and `Fastor` in various matrix computation tasks like [matrix multiplication](https://github.com/wermos/Fast5x5/tree/a495e9bf66303c76550797a1cbdf09ad6a555baa/include/benchmarks/gemm), [matrix inversion](https://github.com/wermos/Fast5x5/tree/a495e9bf66303c76550797a1cbdf09ad6a555baa/include/benchmarks/inversion), computing the [similarity transform](https://github.com/wermos/Fast5x5/tree/a495e9bf66303c76550797a1cbdf09ad6a555baa/include/benchmarks/similarity) and computing [coordinate transforms](https://github.com/wermos/Fast5x5/tree/a495e9bf66303c76550797a1cbdf09ad6a555baa/include/benchmarks/coord-transform) in various matrix dimensions (more specifically, in 4×4, 6×6, 6×8, and 8×8).

We ran the benchmarks on my own machine, and also ran a subset of these tests on a Threadripper machine used for ACTS work. After a deep look into the assembly generated by each backend, as well as a look at the performance each library brought to the table, we decided to use Fastor because it was consistently first or second in all the benchmarks we threw at it, and its assembly generation was the cleanest (i.e. free of cruft and the pointless register shuffling that plagued a few of the other backends).

Hence, the next steps for me and my GSoC project are to
1. integrate Fastor into `algebra-plugins`, and
2. write the front-end for it so that we can see Fastor in action in a more realistic setting.

To that end, I already integrated Fastor to the repository in [PR #77](https://github.com/acts-project/algebra-plugins/pull/77), and am currently working on writing the front-end.
