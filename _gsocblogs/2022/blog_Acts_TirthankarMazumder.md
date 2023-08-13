---
project: Acts
title: Acts — Vectorized Linear Algebra Implementation
author: Tirthankar Mazumder
avatar: https://avatars.githubusercontent.com/u/63574588?s=400&v=4
date: 3.10.2022
year: 2022
layout: blog_post
logo: ACTSlogo.gif
intro: |
  This blog is about my experiences and what I learned during my GSoC project, which involved adding a new math backend to algebra-plugins, to make ACTS faster.
---

Hi everyone! Since starting this year, blogs are mandatory for all CERN-HSF
contributors, I decided to take this time to make my own blog. I have written
about my journey extensively there. Do
[give it a visit](https://wermos.github.io/blog/)!

I have broken down the midterm project report into multiple blog posts:

The [first blog post](https://wermos.github.io/blog/gsoc/gsoc-first-blog-post/)
discusses what GSoC is in general, for those who might just stumble upon my blog
by happenstance.

The
[second blog post](https://wermos.github.io/blog/gsoc/gsoc-the-details-of-my-project/)
delves into the technical details about what my project actually is, what
repository I would be working with, mentions our weekly meeting schedule, and
describes my three mentors.

The [third blog post](https://wermos.github.io/blog/gsoc/gsoc-the-work-so-far/)
finishes up the trilogy by exhaustively discussing the work up till now,
including benchmarking data and conclusions, and the current direction of the
work.

That being said, I will also share a short report of the work I am doing, and
the link to the things I have done so far below:

## My progress

### Fast 5×5

#### Benchmarking Suite for `algebra-plugins`

One of the main things we need, to efficiently figure out what to improve first,
is a comprehensive benchmarking suite for the existing math backends. To that
end, I added Google Benchmark to the
[`algebra-plugins` repository](https://github.com/acts-project/algebra-plugins),
in [PR #69](https://github.com/acts-project/algebra-plugins/pull/69). Writing
those benchmarks is still a work-in-progress.

#### Investigating Matrix Math Libraries

Then, my mentors and I spent a lot of time testing out 3 possible math backend
alternatives (the custom-made `fast5x5`,
[`blaze`](https://bitbucket.org/blaze-lib/blaze/src/master/), and
[`Fastor`](https://github.com/romeric/Fastor) in a repository of mine called
[Fast 5×5](https://github.com/wermos/Fast5x5) and comparing their performance to
that of [`Eigen`](https://eigen.tuxfamily.org/index.php?title=Main_Page). This
repository was something I forked from some
[prior work done on this front](https://gitlab.in2p3.fr/CodeursIntensifs/Fast5x5).

#### How Matrix Math Libraries Work

All matrix math libraries use something called
[SIMD](https://en.wikipedia.org/wiki/Single_instruction,_multiple_data) (short
for Single Instruction, Multiple Data) to achieve a speed-up compared to a naïve
implementation.

Let's take the example of adding two 4-dimensional vectors together. The naïve
way of doing it is to take one element from each vector, add it, and then store
the result in the result vector. This takes 4 add instructions to complete.
However, with a SIMD ISA
([Instruction Set Architecture](https://en.wikipedia.org/wiki/Instruction_set_architecture))
all one needs to do is load the 4 elements of each vector into a SIMD register,
add them, and store the result in a result vector. This takes just 1 add
instruction to complete.

<center><a href="https://commons.wikimedia.org/wiki/File:SIMD2.svg#/media/File:SIMD2.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/SIMD2.svg/400px-SIMD2.svg.png" alt="SIMD2.svg"></a></center>

<center><caption>Representation of a SIMD register <br/>(Picture Credits: Wikipedia, courtesy of <a href="https://commons.wikimedia.org/w/index.php?title=User:Vadikus">Vadikus</a>)</caption></center>

<br/>In the same vein, libraries like `Eigen`, `blaze`, `Fastor`, and `fast5x5`
use SIMD instructions to create optimized routines for tasks like matrix
multiplication.

##### My Project

However, it was found that the performance of Eigen, which is the library that
ACTS uses for matrix computations, could be improved. As a proof-of-concept, the
Fast5×5 project was created to demonstrate this. The Fast5×5 library which uses
[`xsimd`](https://github.com/xtensor-stack/xsimd/) under the hood for a
compiler-agnostic way of exposing SIMD intrinsics.

Therefore, my GSoC project is primarily about investigating how much of a
performance we stand to gain by switching matrix libraries in these projects
([detray](https://github.com/acts-project/detray),
[traccc](https://github.com/acts-project/traccc), and ACTS).

#### Midterm Work Summary

Once we started with the GSoC project, my mentors asked me to look at the
[original Fast5×5 repository](https://gitlab.in2p3.fr/CodeursIntensifs/Fast5x5)
and get an idea of where we stand with respect to the prior work in this
project. I improved the repository in many ways, including (but not limited to)

- removing the `Dockerfile` and a Bash script (among other things) in
  [`2a62718`](https://github.com/wermos/Fast5x5/commit/2a627183458fd25366087c2be8e8d3fd14cde294)
  because it would not be required in this project.
- revamping the project structure to make it easier for outsiders to understand
  where things reside. This was done multiple times (in order to keep the
  project structure up-to-date with the new changes), for example, in
  [`85ad3fd`](https://github.com/wermos/Fast5x5/commit/85ad3fd1de82ee6313bb2685e2a02f368d7e5e6a),
  [`20d4fb9`](https://github.com/wermos/Fast5x5/commit/20d4fb9940f01c547272cb3b2e775335992d8ea6),
  [`125a084`](https://github.com/wermos/Fast5x5/commit/125a084f374c92936a2bc9f8e41d561c31346588),
  and
  [`69bd4d8`](https://github.com/wermos/Fast5x5/commit/69bd4d8cc3f6e3aeb0c6baf21d9510b931984799).
- adding `xsimd` and `Eigen` as Git submodules instead of requiring the end user
  to have these libraries already installed in their system. This has the added
  advantage of allowing us to easily switch between versions of `Eigen` and
  `xsimd` as maintainers of those repositories continue to make bugfixes and
  improvements. This was done in
  [`21aad0e`](https://github.com/wermos/Fast5x5/commit/21aad0e2a38425e0c959b259359e6e67084ec282)
- updating `Eigen` (first in
  [`18dbd4e`](https://github.com/wermos/Fast5x5/commit/18dbd4eab48ed6dcda108c4545632e9d431d6305),
  and then in
  [`0e702b0`](https://github.com/wermos/Fast5x5/commit/0e702b0607c28631a24875d94aa1a5acb80a5554))
  and `xsimd` (in
  [`e1e1c71`](https://github.com/wermos/Fast5x5/commit/e1e1c71aed01d2aee8e24a8b63bcf4360916df81)).
  The original Fast5×5 project had not been touched since 2019. In the 3 years
  since then, all these libraries had undergone some major version releases.
- changing the benchmarking method from using `/usr/bin/time` to using Google
  Benchmark. Google Benchmark gives us an easy way of automating benchmarking
  tasks. Moreover, its `DoNotOptimize()` function allows us to guarantee that
  the operations we are benchmarking were indeed performed and not just
  optimized out by the compiler.
- changing the way the random matrix generation works in
  [`ff821df`](https://github.com/wermos/Fast5x5/commit/ff821df8906a226749408e24b40e627d21fa3894).
  The original Fast 5×5 code used index-based operations to fill up the matrix,
  which is not the best way to generate reliable benchmarking data. The original
  code did the following for generating the matrices:

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

I rewrote the matrix generation code using the random number generators in the
`<random>` header, and mimicked `Eigen`'s `Random()` implementation, which
generates a random float in the range [-1, 1]:

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

Apart from my work on Fast5×5, I also fired off a
[small PR](https://github.com/acts-project/acts/pull/1384) which cleaned up the
CI workflow files in the ACTS repository.

For the comprehensive list of changes and improvements, be sure to check out my
[blog post](https://wermos.github.io/blog/gsoc/gsoc-the-work-so-far/) dedicated
to the work I did!

### Post-Midterm Work

Pre-midterm, I spent quite a bit of time writing benchmarks for testing the
performance of `Eigen`, `fast5x5`, `blaze`, and `Fastor` in various matrix
computation tasks like
[matrix multiplication](https://github.com/wermos/Fast5x5/tree/a495e9bf66303c76550797a1cbdf09ad6a555baa/include/benchmarks/gemm),
[matrix inversion](https://github.com/wermos/Fast5x5/tree/a495e9bf66303c76550797a1cbdf09ad6a555baa/include/benchmarks/inversion),
computing the
[similarity transform](https://github.com/wermos/Fast5x5/tree/a495e9bf66303c76550797a1cbdf09ad6a555baa/include/benchmarks/similarity)
and computing
[coordinate transforms](https://github.com/wermos/Fast5x5/tree/a495e9bf66303c76550797a1cbdf09ad6a555baa/include/benchmarks/coord-transform)
in various matrix dimensions (more specifically, in 4×4, 6×6, 6×8, and 8×8).

I ran the benchmarks on my own machine and analyzed the performance of each
backend. After a deep look into the assembly generated by each backend, as well
as a look at the performance each library brought to the table, we decided to
use Fastor because it was consistently first or second in all the benchmarks we
threw at it, and its assembly generation was the cleanest (i.e. free of cruft
and the pointless register shuffling that plagued a few of the other backends).

One of the big things I worked on post-midterm was on the visualization of the
benchmarking results. We had the data, but no easy way to visualize it. I put
together two Python scripts:
[one](https://github.com/wermos/Fast5x5/blob/c474a3d76802a75c1cc5baa98e3c25684874d928/plots/generate_general_plots.py)
for generating comparative plots with all the backends together, and
[one](https://github.com/wermos/Fast5x5/blob/c474a3d76802a75c1cc5baa98e3c25684874d928/plots/generate_backend_plots.py)
to demonstrate how each backend fares alone.

#### Benchmark Plots

Here are the comparative plots I generated:

<center><a href="https://user-images.githubusercontent.com/63574588/203063061-1c49a14f-4ef4-499f-871d-529f1940a75f.png"><img src="https://user-images.githubusercontent.com/63574588/203063061-1c49a14f-4ef4-499f-871d-529f1940a75f.png" width="800" height="450"></a></center>
<center><caption>Benchmark plot for GEMM with <code>float</code> matrices.</caption></center>

<center><a href="https://user-images.githubusercontent.com/63574588/203063874-df9c055b-7f57-4e1a-905b-bb2115166cff.png"><img src="https://user-images.githubusercontent.com/63574588/203063874-df9c055b-7f57-4e1a-905b-bb2115166cff.png" width="800" height="450"></a></center>
<center><caption>Benchmark plot for GEMM with <code>double</code> matrices.</caption></center>

<center><a href="https://user-images.githubusercontent.com/63574588/203063983-6363ba9a-f3f5-4bc3-9619-4a0d43502299.png"><img src="https://user-images.githubusercontent.com/63574588/203063983-6363ba9a-f3f5-4bc3-9619-4a0d43502299.png" width="800" height="450"></a></center>
<center><caption>Benchmark plot for matrix inversion with <code>float</code> matrices.</caption></center>

<center><a href="https://user-images.githubusercontent.com/63574588/203063992-22725e6c-98bb-4a48-8acf-d168a28b9eec.png"><img src="https://user-images.githubusercontent.com/63574588/203063992-22725e6c-98bb-4a48-8acf-d168a28b9eec.png" width="800" height="450"></a></center>
<center><caption>Benchmark plot for matrix inversion with <code>double</code> matrices.</caption></center>
<br/>Note that the bar graphs for the `custom` backend for the 6×6 and 8×8 dimensions do not exist. This is an intentional and recurring theme: The `Custom` backend has a size limitation which prevents it from being usable for 6×6 and 8×8 matrices without the AVX512 instruction set, which [my processor](https://ark.intel.com/content/www/us/en/ark/products/132228/intel-core-i712700h-processor-24m-cache-up-to-4-70-ghz.html) does not support. For this reason, the `custom` 6×6 and 8×8 data is missing from all of my benchmark plots.

<center><a href="https://user-images.githubusercontent.com/63574588/203063990-112b848c-76ca-4192-905f-5c90f86b03a2.png"><img src="https://user-images.githubusercontent.com/63574588/203063990-112b848c-76ca-4192-905f-5c90f86b03a2.png" width="800" height="450"></a></center>
<center><caption>Benchmark plot for the similarity transform with <code>float</code> matrices.</caption></center>

<center><a href="https://user-images.githubusercontent.com/63574588/203063987-10bea51c-0fb0-4315-bc6d-d9953f7c2ffb.png"><img src="https://user-images.githubusercontent.com/63574588/203063987-10bea51c-0fb0-4315-bc6d-d9953f7c2ffb.png" width="800" height="450"></a></center>
<center><caption>Benchmark plot for the similarity transform with <code>double</code> matrices.</caption></center>

<center><a href="https://user-images.githubusercontent.com/63574588/203063866-3120d95f-d17e-4847-9e5a-793b57bd2073.png"><img src="https://user-images.githubusercontent.com/63574588/203063866-3120d95f-d17e-4847-9e5a-793b57bd2073.png" width="800" height="450"></a></center>
<center><caption>Benchmark plot for the free coordinates to bound coordinates transform with <code>float</code> matrices.</caption></center>

<center><a href="https://user-images.githubusercontent.com/63574588/203063885-88a3f2f2-3550-4296-ad30-ca9d98551ee5.png"><img src="https://user-images.githubusercontent.com/63574588/203063885-88a3f2f2-3550-4296-ad30-ca9d98551ee5.png" width="800" height="450"></a></center>
<center><caption>Benchmark plot for the free coordinates to bound coordinates transform with <code>double</code> matrices.</caption></center>

<center><a href="https://user-images.githubusercontent.com/63574588/203063883-e7d80d2a-d265-4ee6-9195-0ef9085f1d18.png"><img src="https://user-images.githubusercontent.com/63574588/203063883-e7d80d2a-d265-4ee6-9195-0ef9085f1d18.png" width="800" height="450"></a></center>
<center><caption>Benchmark plot for the bound coordinates to free coordinates transform with <code>float</code> matrices.</caption></center>

<center><a href="https://user-images.githubusercontent.com/63574588/203063885-88a3f2f2-3550-4296-ad30-ca9d98551ee5.png"><img src="https://user-images.githubusercontent.com/63574588/203063885-88a3f2f2-3550-4296-ad30-ca9d98551ee5.png" width="800" height="450"></a></center>
<center><caption>Benchmark plot for the bound coordinates to free coordinates transform with <code>double</code> matrices.</caption></center>

It is clear from these plots that Fastor is consistently near the top (i.e.
either the fastest or the second-fastest in all of these tasks).

## Integrating Fastor into `algebra-plugins`

I first had to define the math functions that live in the
[`math` subdirectory](https://github.com/wermos/algebra-plugins/tree/528327c51d46cf198fe79fd83856c47b29d6d2b1/math/fastor)
in terms of `Fastor` primitives and functions. After that, I had to declare the
standard litany of types in the
[`storage` subdirectory](https://github.com/wermos/algebra-plugins/tree/528327c51d46cf198fe79fd83856c47b29d6d2b1/storage/fastor).
Then, I had to define the
[`fastor_fastor` frontend](https://github.com/wermos/algebra-plugins/tree/528327c51d46cf198fe79fd83856c47b29d6d2b1/frontend/fastor_fastor)
so that the backend is actually usable and the tests can be written.

After that, I wrote the
[tests](https://github.com/wermos/algebra-plugins/tree/528327c51d46cf198fe79fd83856c47b29d6d2b1/tests/fastor).
However, we ran into a small hurdle as the tests (which were written in a
generic way, abstracted away from any specific backend) expect `operator*` to be
defined for matrix-matrix and matrix-vector multiplication. However, Fastor
overloads `operator%` for matrix-matrix and matrix-vector multiplication, and
also offers the `Fastor::matmul` function. (It uses `operator*` for element-wise
multiplication, instead.) This issue is yet to be resolved (at the time of
writing.)

For a slightly more detailed report of what I did to integrate Fastor into
`algebra-plugins`, check out my
[final GSoC blog post on my personal blog](https://wermos.github.io/blog/gsoc/gsoc-the-final-status-report/).

### Concluding Remarks

This concludes my CERN-HSF 2022 GSoC blog post! It was a great learning
experience for me as I got to learn a lot about SIMD and vectorization.
Moreover, the opportunity to work with CERN was a great honor to me, and I also
enjoyed working with mentors from different countries.

Thank you for reading!
