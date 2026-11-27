---
project: ML4EP
title: ML Inference on Heterogeneous Architectures using SOFIE
author: Harsh Chauhan
photo: blog_authors/HarshChauhan.jpg
date: 01.11.2026
year: 2026
layout: blog_post
logo: ML4EP-logo.png
intro: |
  SOFIE (System for Optimized Fast Inference code Emit), part of ROOT's TMVA, turns a trained machine learning model into C++ inference code with BLAS as its only dependency. Its GPU code generation uses alpaka, so one generated source runs on NVIDIA GPUs, AMD GPUs and CPUs, with matrix products going through sofieBLAS. Over 22 weeks I ported and fixed operators on the GPU path, added support for input shapes known only at run time so that a generated model runs at any input size without regenerating code, built the matching dynamic GEMM support in sofieBLAS, and brought the GPU test suite to both vendors. This report covers the implementation, the state of the pull requests and what comes next.
---

<style>
.highlight .c1, .highlight .cm { color: #6a737d; font-style: italic; }
.highlight .k, .highlight .kr { color: #d73a49; }
.highlight .kt { color: #d73a49; }
.highlight .cp { color: #6f42c1; }
.highlight .s, .highlight .s1, .highlight .s2 { color: #032f62; }
.highlight .mi, .highlight .mf { color: #005cc5; }
.highlight .nf { color: #6f42c1; }
</style>

## Details

| | |
|---|---|
| Name | [Harsh Chauhan](https://github.com/harz05) |
| Organisation | [CERN-HSF](https://hepsoftwarefoundation.org/activities/gsoc.html) and [ML4EP](https://github.com/ML4EP) |
| Project | [ML Inference on heterogeneous architectures using SOFIE](https://hepsoftwarefoundation.org/gsoc/2026/proposal_ML4EP_SOFIE_ALPAKA.html) |
| Mentors | [Sanjiban Sengupta](https://github.com/sanjibansg), [Dr. Lorenzo Moneta](https://github.com/lmoneta) |
| GSoC project page | [https://summerofcode.withgoogle.com/programs/2026/projects/NE74dwRu.html](https://summerofcode.withgoogle.com/programs/2026/projects/NE74dwRu.html) |
| Repositories | [ML4EP/SOFIE](https://github.com/ML4EP/SOFIE), [ML4EP/sofieBLAS](https://github.com/ML4EP/sofieBLAS) and [root-project/root](https://github.com/root-project/root/tree/master/tmva/sofie) |
| Period | Community bonding from 1 May 2026, coding 25 May to 26 October 2026 (22 weeks) |
{: .table}

## 1 About the project

Machine learning models are now part of how the LHC experiments process data, including in trigger systems with high throughput, low latency and tight memory limits, where deploying PyTorch or TensorFlow inside a C++ framework brings heavy dependencies and clashes with the framework's own threading.

SOFIE (System for Optimized Fast Inference code Emit), part of ROOT's TMVA, takes a trained model and generates C++ code for its inference, with BLAS as the only dependency. The generated code is small, has no model interpreter at run time, and on CPUs it matches or beats ONNX Runtime on several LHC models.

The High-Luminosity LHC pushes more of this work onto GPUs, and each vendor brings its own programming model, memory layout and BLAS library. "Heterogeneous architectures" in the title means that the same generated inference code should run on NVIDIA GPUs, AMD GPUs and CPUs. SOFIE gets there in two layers: the generated code uses alpaka for its kernels and buffers, so one source compiles for every backend, and matrix products go through sofieBLAS, which gives the generated code one BLAS interface and picks the vendor library underneath.

When this project started, that GPU path covered part of the operator set, worked only for input sizes fixed at generation time, and had only ever run on NVIDIA. The aim was to close those three gaps.

## 2 SOFIE and sofieBLAS in brief

<img src="https://gist.github.com/user-attachments/assets/be288bac-e36c-44d3-8ada-997b2241bac6" alt="SOFIE pipeline: Keras, PyTorch or ONNX model, parser, RModel, inference code generator, C++ output with alpaka or SYCL" width="100%">

*Figure: the SOFIE pipeline, from S. Sengupta and L. Moneta, EuCAIFCon 2026.*

The figure above is the whole pipeline. A trained model (ONNX, Keras or PyTorch) is parsed into SOFIE's model object, which knows every operator, its attributes and its tensor shapes. Code generation then writes a header with a `Session` class: the constructor loads the weights and allocates every intermediate tensor once, and `infer()` runs the operators in order.

For GPUs the same generator emits alpaka code. Every operator becomes a kernel launched on a device queue, the tensors live in alpaka device buffers, and the `Session` takes the backend as a template argument: `Session<alpaka::TagGpuCudaRt>` for NVIDIA, `Session<alpaka::TagGpuHipRt>` for AMD. Nothing else in the generated file changes.

Matrix products do not go through a hand-written kernel. They go to sofieBLAS, which exposes one GEMM call and routes it to cuBLASLt, hipBLASLt or a CPU BLAS depending on that same tag. sofieBLAS also owns the vendor-side objects a GEMM needs (matrix layouts, operation descriptors, the chosen algorithm) and caches them. A good part of my work landed in that layer.

## 3 Project plan and deliverables

The GPU backend was built by my mentors and earlier contributors before this project, and several operators landed between my proposal in March and the start of coding, so my first weeks went to testing them rather than writing them. The table below is the operator coverage on the `gpu/alpaka` branch at three dates, with the last row being what this project added.

| Date | Operators with an alpaka GPU path |
|---|---|
| 19 March 2026 (proposal) | BasicBinary, BasicUnary, Cast, Concat, Constant, Expand, Gather, GatherND, Gemm, LeakyRelu, Relu, Reshape, ScatterElements, Shape, Sigmoid, Split, Tile, Transpose |
| 27 May 2026 (coding start) | the March set plus BasicIs, BatchNormalization, Clip, Comparison, Conv (batch and groups), Identity, LayerNormalization, Logic, Not, Reduce, Slice, Tanh, Trilu, Where |
| 23 October 2026 | the May set plus **Pool, Pad, Elu, Selu, Gelu, Softmax, TopK, BasicNary, Range** (this project) and operators from the upstream ROOT sync |
{: .table}

The plan drafted with my mentors in June set these outputs:

1. Operator support: finish the GPU operators needed for complete models.
2. Dynamic inputs: extend the GPU code generation to input shapes known only at run time, starting with a dynamic batch dimension.
3. Inference on AMD GPUs through the HIP backend and hipBLASLt.
4. GPU CI for NVIDIA and later AMD.
5. Operator fusion.
6. Profiling of time and memory.
7. Memory reuse on the GPU path, as the CPU path already has.

This report covers the first three, plus the testing and quantisation work that grew out of them.

## 4 Community bonding (1 to 24 May)

I had been contributing to SOFIE in ROOT since March: seven fixes to the CPU code generation were merged before GSoC started ([#21683](https://github.com/root-project/root/pull/21683), [#21733](https://github.com/root-project/root/pull/21733), [#21735](https://github.com/root-project/root/pull/21735), [#21757](https://github.com/root-project/root/pull/21757), [#21773](https://github.com/root-project/root/pull/21773), [#21776](https://github.com/root-project/root/pull/21776), [#21793](https://github.com/root-project/root/pull/21793)), so the SOFIE code base itself was familiar. Community bonding went to the part that was not: the standalone [ML4EP/SOFIE](https://github.com/ML4EP/SOFIE) repository and its alpaka code generator in `RModel_ALPAKA.cxx`.

- Built both repositories and read the alpaka generation path end to end, from parser to the emitted `Session`.
- ROOT [#21730](https://github.com/root-project/root/pull/21730), merged 3 May: the Conv dynamic-shape output formula emitted wrong C++ for stride > 1 (issue [#21729](https://github.com/root-project/root/issues/21729)). The same bug came back later in the GPU generator, see [5.2 Dynamic input shapes](#52-dynamic-input-shapes-on-the-gpu-path-45).
- ML4EP/SOFIE [#20](https://github.com/ML4EP/SOFIE/pull/20), 12 May: first tests for Conv on GPU with batch > 1 (issue [#18](https://github.com/ML4EP/SOFIE/issues/18)). Issue [#21](https://github.com/ML4EP/SOFIE/issues/21), 24 May: groups > 1 had no test either. These two set the pattern for the first coding weeks.

## 5 Implementation

### 5.1 Operators

#### 5.1.1 Fixes and optimisations on the Conv path

The Conv GPU path existed but large parts of it had never been exercised by a test. Writing the tests found the bugs.

- Groups > 1 ([#22](https://github.com/ML4EP/SOFIE/pull/22)): output channels 0 and 1 right, 2 and 3 wrong. Cause: the GEMM column count was no longer divided by the group count after a refactor. Issue [#23](https://github.com/ML4EP/SOFIE/issues/23), fix [#24](https://github.com/ML4EP/SOFIE/pull/24).
- Dilation > 1: the kernel shape was inflated for dilation and the dilation was passed to im2col again, so it was applied twice. Silently wrong on GPU, segfault on CPU. Issue [#32](https://github.com/ML4EP/SOFIE/issues/32), fix [#34](https://github.com/ML4EP/SOFIE/pull/34) for both paths, and the same fix upstream in ROOT [#22474](https://github.com/root-project/root/pull/22474).
- Bias, 1D and 3D Conv ([#31](https://github.com/ML4EP/SOFIE/pull/31)) and SAME_UPPER autopad ([#35](https://github.com/ML4EP/SOFIE/pull/35), issue [#33](https://github.com/ML4EP/SOFIE/issues/33)) tests.
- Two optimisations proposed and prototyped: move the weight-vector kernel out of `infer()` into session construction (issue [#25](https://github.com/ML4EP/SOFIE/issues/25)), and replace the per-sample GEMM loop with one strided-batched GEMM (issue [#29](https://github.com/ML4EP/SOFIE/issues/29), PR [#30](https://github.com/ML4EP/SOFIE/pull/30)).

The lesson from these weeks stayed with me for the rest of the project. A code path the generator can emit but no test ever runs is not "supported", it is untested, and it stays wrong until the first test for it exists. Every operator I added after this came with its test in the same pull request.

#### 5.1.2 New operators

- Pool ([#27](https://github.com/ML4EP/SOFIE/pull/27), issue [#26](https://github.com/ML4EP/SOFIE/issues/26)): MaxPool, AveragePool and GlobalAveragePool in 1D, 2D and 3D. One thread per output element; the thread recovers its output coordinates from the flat index and walks the window. The asymmetric-padding fix from ROOT was ported in [#28](https://github.com/ML4EP/SOFIE/pull/28).
- Pad ([#40](https://github.com/ML4EP/SOFIE/pull/40)): constant mode with initialised pads and constant value, matching what the CPU operator supports.
- Element-wise activations: Elu ([#38](https://github.com/ML4EP/SOFIE/pull/38)), Selu with configurable alpha and gamma ([#39](https://github.com/ML4EP/SOFIE/pull/39), which also changed the CPU operator), Gelu ([#69](https://github.com/ML4EP/SOFIE/pull/69)).
- Softmax and TopK, first opened as [#41](https://github.com/ML4EP/SOFIE/pull/41) and [#42](https://github.com/ML4EP/SOFIE/pull/42), then carried into the dynamic-inputs PR below. BasicNary (Max, Min, Sum, Mean with broadcasting) and Range were added there too.

Softmax is the one with a design point. The textbook version takes three passes over a row: find the maximum, sum the exponentials, normalise. The GPU kernel uses the online form, which folds the first two passes into one by rescaling the running sum whenever the maximum moves:

```text
// Softmax GPU kernel, one block per row (simplified)
each thread, over its strided share of the row:
    m = first element; d = 0
    for each x:
        m_new = max(m, x)
        d = d * exp(m - m_new) + exp(x - m_new)      // rescale the running sum when the max moves
        m = m_new

combine the threads' (m, d) pairs in shared memory with the same rule:
    (m_a, d_a) + (m_b, d_b) = (M, d_a * exp(m_a - M) + d_b * exp(m_b - M)),  M = max(m_a, m_b)

second pass: Y[x] = exp(x - M) / d                   // LogSoftmax: x - M - log(d)
```

The TopK kernel was reworked later in the project for AMD; that story is in [5.4 Testing](#54-testing).

### 5.2 Dynamic input shapes on the GPU path ([#45](https://github.com/ML4EP/SOFIE/pull/45))

- Issue [#43](https://github.com/ML4EP/SOFIE/issues/43), 22 June: the alpaka generator handled static shapes only. Every buffer size and every loop bound was a compile-time constant in the generated file.
- The generated `Session` gained dynamic device buffers and shape parameters on the constructor (the maximum sizes, used to allocate once) and on `infer()` (the sizes of this call). Operators extended to emit shape-dependent code: Gemm/MatMul, Conv, BatchNormalization, BasicBinary, Comparison, Reduce, Gather, Transpose, Concat, Slice, Tile, Range. New kernels: TopK, Softmax, BasicNary.

```cpp
// from tests/alpaka/TestAlpakaConv.cxx: the runtime sizes are passed twice
SOFIE_DynamicConv1D::Session<TestTag> session("DynamicConv1D.dat", N, P);   // maximum sizes, buffers allocated once
auto result = session.infer(N, P, input_d);                                  // sizes of this call
```

- Sanjiban extended the PR on top of this with Reduce specialisations, Range, a grid-stride LayerNormalization, a hierarchical TopK search and dynamic support for GatherND, ScatterND, Split, Trilu and Expand.
- Result at merge on 15 September: 140 of 140 alpaka tests pass on H100. `ParticleNet.onnx`, which I used as the test model because its particle and vertex counts vary per event (248 nodes, 29 operator types), generates, compiles and runs on GPU with outputs matching the CPU reference, and one `Session` serves three different input sizes (this needs sofieBLAS #11, [section 5.3](#53-sofieblas-gemm-for-sizes-known-only-at-run-time-11)).
- The stride > 1 bug from community bonding reappeared in the GPU generator and was fixed with the same change.

Most of the work was turning every size in the generated file from a literal into an expression of the session's shape parameters, in the buffer allocations, the work divisions and the GEMM calls, without changing the static path for models that do not need it, and a review pass before merge cut about 560 lines and caught six bugs. The first run at two sizes also threw inside sofieBLAS, which is [section 5.3](#53-sofieblas-gemm-for-sizes-known-only-at-run-time-11).

`ParticleNet.onnx` generates, compiles and runs on the current head of gpu/alpaka ([484f93c](https://github.com/ML4EP/SOFIE/commit/484f93cb54b9a6b020acb0c0aa2c8858979a3489)) with sofieBLAS dev ([1977fbb](https://github.com/ML4EP/sofieBLAS/commit/1977fbb89dcb562a75d628c06fd3a5bb74ec1076)). Nsight Systems kernel time per inference, mean over 100 inferences after 20 warm-up runs, at batch 1, 100 particles and 10 vertices on an H100, 31 October 2026. The 126 kernels account for 383 us of GPU time inside a 563 us inference, the rest being launch gaps.

| Kernel class | Kernels | GPU Total Time |
|---|---|---|
| GEMM through sofieBLAS | 21 | 90 us |
| TopK | 3 | 86 us |
| ReduceMean | 3 | 35 us |
| Conv im2col | 15 | 33 us |
| BatchNormalization with fused ReLU | 17 | 30 us |
| Fused elementwise kernels | 12 | 22 us |
| Conv weight layout | 15 | 19 us |
| Everything else | 40 | 68 us |
{: .table}

### 5.3 sofieBLAS: GEMM for sizes known only at run time ([#11](https://github.com/ML4EP/sofieBLAS/pull/11))

- The first multi-size `ParticleNet.onnx` run threw `std::out_of_range`: cuBLASLt matrix layouts were registered once per `Session` for one size (issue [#10](https://github.com/ML4EP/sofieBLAS/issues/10)).
- What merged on 8 September: layouts are created on first use for any size; the vendor's algorithm search runs once per shape and descriptor, is warmed at registration and cached, with an optional LRU limit on the cache; `addOperationConfig` takes a portable `Epilogue` enum (Default, Bias, ReluBias, GeluBias) so the generated code never names a vendor.

```text
// sofieBLAS after #11 (simplified). Api is a table of cuBLASLt or hipBLASLt names.

Session constructor, once per GEMM in the model:
    blas.addOperationConfig(m, n, k, transA, transB, epilogue)
        create the layouts for A, B and C if this shape is new
        run the vendor's algorithm search once and cache it under (transA, transB, epilogue, shapeA, shapeB)

every GEMM inside infer(), with this call's sizes:
    blas.gemm(A, B, C, shapes...)
        key = (transA, transB, epilogue, shapeA, shapeB)
        hit:  reuse the cached algorithm, no vendor call
        miss: create layouts, search once, insert; with a cache limit, evict the least recently used entry
        Api::matmul(..., cached algorithm)
```

- The structure is the part worth highlighting: all of the layout, descriptor and algorithm logic lives once in a shared template, `BlasLt<Api>`, and each vendor contributes only a table of API names, about 110 lines each for cuBLASLt and hipBLASLt. The HIP backend got the feature by construction and was verified on MI100.
- Measured on `ParticleNet.onnx`, the change buys the tail latency and the memory, not throughput: the vendor's algorithm search no longer runs on live events, and the cache stops growing with the number of distinct sizes.

This work also produced a measurement that matters for BOA ([section 6](#6-talks-and-collaboration)). BOA's batch size is a GEMM dimension chosen at run time, and while testing #11 on `ParticleNet.onnx` I found that two different kernel choices for the same GEMM give results that differ in the last bits against the same CPU reference. Since the vendor library picks its kernel from the matrix shape, two runs at different sizes can disagree in those bits. That is why BOA cannot rely on fp32 vendor BLAS between its encoder and decoder, and why the integer GEMM path in [5.5 Quantisation](#55-quantisation-sofieblas-15-draft-pr) is the one that matters for it.

### 5.4 Testing

- sofieBLAS [#13](https://github.com/ML4EP/sofieBLAS/pull/13), merged 21 September (issue [#12](https://github.com/ML4EP/sofieBLAS/issues/12)): the CUDA and HIP test files were copies of each other. One templated fixture in `tests/gpu/unit_test.tpp`, instantiated per alpaka tag, replaced them; `tests/test.cc` went from 852 to 285 lines; the CI matrix gained OpenBLAS and MKL on CPU. Verified on H100 and MI100.
- ML4EP/SOFIE [#55](https://github.com/ML4EP/SOFIE/pull/55), merged 22 October (issue [#51](https://github.com/ML4EP/SOFIE/issues/51)): the same idea for the whole alpaka test suite. A `TestTag` chosen at build time replaced 101 hard-coded CUDA tags, 98 `cudaDeviceSynchronize()` calls were removed, and a HIP build target was added. First all-green AMD run on 22 October (MI100, 243 of 243). CI flavours for W7900 and MI300X added.

```cpp
// tests/alpaka/TestAlpakaCommon.h: the backend under test comes from the build, not from the test
#if defined(ALPAKA_ACC_GPU_CUDA_ENABLED)
using TestTag = alpaka::TagGpuCudaRt;
#elif defined(ALPAKA_ACC_GPU_HIP_ENABLED)
using TestTag = alpaka::TagGpuHipRt;
#endif
using TestAcc = alpaka::TagToAcc<TestTag, Dim, Idx>;
// every test then writes SOFIE_Model::Session<TestTag> and never names a vendor
```

Two kernels that passed every NVIDIA test broke on AMD's 64-wide wavefronts:

- Reduce (issue [#68](https://github.com/ML4EP/SOFIE/issues/68)): the block reduction shuffled over `warpSize` lanes, so a 32-thread block on a 64-wide wavefront read lanes 32 to 63, which hold no thread. The shuffle width is now the smaller of warp size and block size.
- TopK: per-thread candidates were merged into a block-shared list behind a spin lock. AMD lanes in one wavefront run in lockstep with no independent forward progress, so a lane spinning on a lock held by a sibling lane deadlocks. The lock is gone, replaced by the warp shuffle merge below, which is also the faster kernel on both vendors.

```cpp
// generated TopK kernel after #55, the warp merge. Each lane holds its best K values (myV)
// and their indices (myI), sorted best first. warpSize is 32 on NVIDIA and 64 on AMD.
for (std::int32_t offset = warpSize / 2; offset > 0; offset >>= 1) {
    T oV[K]; int64_t oI[K];
    for (int p = 0; p < K; ++p) {
        oV[p] = alpaka::warp::shfl_down(acc, myV[p], offset);   // read the partner lane's list, no memory, no lock
        oI[p] = alpaka::warp::shfl_down(acc, myI[p], offset);
    }
    mergeBestK(myV, myI, oV, oI);   // best K of both lists, ties to the lower index like the CPU path
}
// lane 0 now holds the warp's best K. Each warp writes its list to shared memory, one block
// barrier, and the first warp runs the same rounds over those lists for the final result.
```

The portability lesson is short. A kernel that passes on NVIDIA has only shown that its assumptions hold for a warp of 32 with independent thread scheduling. The AMD run is the first time those assumptions are tested at all, and the fixes it forces are better kernels on both vendors.

<img src="https://gist.github.com/user-attachments/assets/379be40b-b10f-4785-8c12-4b62daa19095" alt="Latency per inference before and after the lock-free TopK kernel, ParticleNet at four input sizes and TopKBig" width="100%">

*Figure: latency per inference with the commit just before #55 and with #55, built from the same tree and run on the same machine within the same hour, so the TopK kernel is the only difference. ParticleNet runs 1.3x to 2.0x faster end to end depending on the input size, and the TopKBig model 5.1x.*

### 5.5 Quantisation (sofieBLAS [#15](https://github.com/ML4EP/sofieBLAS/pull/15), draft PR)

- Why: Shaun Lee's [ML4EP/SOFIE #53](https://github.com/ML4EP/SOFIE/pull/53) brings INT8 and FP8 quantised inference to SOFIE, with the quantised GEMMs calling cuBLASLt directly, so CUDA only. The review asked for those GEMMs to go through sofieBLAS so the HIP backend gets them too. #15 is that sofieBLAS side.
- Done so far: int8 inputs with int32 accumulation and an int8-output variant, fp16, and FP8 (E4M3 and E5M2 with per-tensor scale pointers), with one cache group per input type so descriptors of different precisions never mix. On H100 all int8 and fp16 tests pass; on MI100 fp16 passes and int8-output cases skip cleanly through a support probe (no such kernels on gfx908). FP8 is implemented but not yet run on a GPU.
- For BOA this is the step that matters: int8 with int32 accumulation is order-independent, so a vendor BLAS becomes usable where bit-exact results are required.

This work continues after GSoC: the remaining tests on both vendors, then the SOFIE side so the quantised models in #53 run through sofieBLAS on NVIDIA and AMD.

### 5.6 Fixes upstream in ROOT along the way

- [#22438](https://github.com/root-project/root/pull/22438), 31 May: MaxPool and AveragePool read the wrong pad indices for asymmetric padding.
- [#22474](https://github.com/root-project/root/pull/22474), 5 June: Conv dilation counted twice in im2col (found by the GPU tests in [5.1.1](#511-fixes-and-optimisations-on-the-conv-path)).
- [#22564](https://github.com/root-project/root/pull/22564), 9 July: the Swish operator existed but was not registered in the ONNX parser.
- [#21685](https://github.com/root-project/root/pull/21685), 12 July: Keras Conv2D same padding ignored dilation (opened in March, merged during the programme).
- [#23200](https://github.com/root-project/root/pull/23200), 31 August: Range output size for symbolic INT64 inputs did not compile (found while running `ParticleNet.onnx`).
- Issue [#22523](https://github.com/root-project/root/issues/22523): AveragePool with ceil_mode divided the partial window by the full kernel size; fixed upstream by Jonas Rembser in [#22862](https://github.com/root-project/root/pull/22862).
- Issue [#23226](https://github.com/root-project/root/issues/23226): proposed splitting the ONNX test file by operator category; declined, but it opened a discussion with the ROOT maintainers on separating SOFIE's model representation from its code emission (see [8 Future plans](#8-future-plans)).

## 6 Talks and collaboration

Through the summer this work was also reported into the weekly [Summer of BOA](https://indico.global/event/18421/) meetings run by Caterina Doglioni (University of Manchester). [BOA](https://github.com/boa-collaboration/boa-constrictor) (Bytewise Online Autoregressive Constrictor) is a byte-level lossless neural compressor for physics data, and the SOFIE part of the programme was running its network through SOFIE so that compression and decompression run on NVIDIA and AMD GPUs from the same generated code. What I reported each week is in the table, with the slides linked.

| Date | Where | What |
|---|---|---|
| 10 June 2026 | [ML4EP Meeting](https://indico.cern.ch/event/1696954/), CERN | Project introduction and plan |
| 1 July 2026 | [Summer of BOA](https://indico.global/event/18421/) weekly, round table | Project introduction to the BOA group ([slides](https://drive.google.com/file/d/14ICsVBaf5tespEK9xbifwBmqaLx7bf6J/view?usp=sharing)) |
| 22 July 2026 | Summer of BOA weekly | Conv and Pool PRs, `ParticleNet.onnx` on GPU ([slides](https://drive.google.com/file/d/1N18AkHiudr2atRadigaEfY1VvzwG0f4q/view?usp=drive_link)) |
| 29 July 2026 | Summer of BOA weekly | sofieBLAS layouts and caching, kernel choice and reproducibility ([slides](https://drive.google.com/file/d/1mBdaZjiDcXCS_NzulBuBnL3vECVp8WzG/view?usp=drive_link)) |
| 5 August 2026 | Summer of BOA weekly | Progress report, what SOFIE gives BOA ([slides](https://drive.google.com/file/d/1GZ9GkNXwfsVWRxTjh0u_sPnMZbpIuVi8/view?usp=drive_link)) |
| 12 August 2026 | [ML4EP Meeting](https://indico.cern.ch/event/1717429/), CERN, Summer Students Reports | Operator and PR inventory, dynamic inputs, `ParticleNet.onnx` results, sofieBLAS ([slides](https://indico.cern.ch/event/1717429/contributions/7224965/attachments/3326586/5957696/ML4EP_aug12_meet.pdf)) |
| 19 August 2026 | Summer of BOA weekly | Multi-size inference, CUDA/HIP test fixture, next steps ([slides](https://drive.google.com/file/d/1gvPzSxkt-h0ciBzxYTj3X0miYg7kDChn/view?usp=drive_link)) |
{: .table}

Co-author on conference abstracts:

- [Enabling portable and optimized Machine Learning Inference through code generation](https://indico.physi.uni-heidelberg.de/event/1277/contributions/4239/), S. Sengupta, L. Moneta et al., EuCAIFCon 2026, Heidelberg, 27 August.
- [A summer of BOA for scientific data compression](https://indico.physi.uni-heidelberg.de/event/1277/contributions/4237/), C. Doglioni et al., EuCAIFCon 2026, Heidelberg, 27 August.
- [High-performance and portable ML Inference using SOFIE](https://indico.global/event/15240/contributions/165344/), S. Sengupta, L. Moneta et al., ML4Jets 2026, Vienna, 17 September.

## 7 Status of pull requests and issues

### 7.1 ML4EP/SOFIE

| Pull request | Issue | Status |
|---|---|---|
| **[#20](https://github.com/ML4EP/SOFIE/pull/20)** Conv GPU tests, batch > 1 | [#18](https://github.com/ML4EP/SOFIE/issues/18) | [![merged](https://img.shields.io/badge/merged-8250df?style=flat-square)](https://github.com/ML4EP/SOFIE/pull/20) |
| **[#22](https://github.com/ML4EP/SOFIE/pull/22)** Conv GPU tests, groups > 1 | [#21](https://github.com/ML4EP/SOFIE/issues/21) | [![merged](https://img.shields.io/badge/merged-8250df?style=flat-square)](https://github.com/ML4EP/SOFIE/pull/22) |
| **[#24](https://github.com/ML4EP/SOFIE/pull/24)** grouped Conv fix and regression test | [#23](https://github.com/ML4EP/SOFIE/issues/23) | [![merged](https://img.shields.io/badge/merged-8250df?style=flat-square)](https://github.com/ML4EP/SOFIE/pull/24) |
| **[#27](https://github.com/ML4EP/SOFIE/pull/27)** Pool GPU operator | [#26](https://github.com/ML4EP/SOFIE/issues/26) | [![merged](https://img.shields.io/badge/merged-8250df?style=flat-square)](https://github.com/ML4EP/SOFIE/pull/27) |
| **[#28](https://github.com/ML4EP/SOFIE/pull/28)** Pool asymmetric padding fix | ROOT [#22436](https://github.com/root-project/root/issues/22436) | [![merged](https://img.shields.io/badge/merged-8250df?style=flat-square)](https://github.com/ML4EP/SOFIE/pull/28) |
| **[#16](https://github.com/ML4EP/SOFIE/pull/16)** error handling in model generator scripts | [#15](https://github.com/ML4EP/SOFIE/issues/15) | [![merged](https://img.shields.io/badge/merged-8250df?style=flat-square)](https://github.com/ML4EP/SOFIE/pull/16) |
| **[#38](https://github.com/ML4EP/SOFIE/pull/38)** Elu GPU operator | | [![merged](https://img.shields.io/badge/merged-8250df?style=flat-square)](https://github.com/ML4EP/SOFIE/pull/38) |
| **[#31](https://github.com/ML4EP/SOFIE/pull/31)** Conv GPU tests, bias, 1D, 3D | | [![merged](https://img.shields.io/badge/merged-8250df?style=flat-square)](https://github.com/ML4EP/SOFIE/pull/31) |
| **[#34](https://github.com/ML4EP/SOFIE/pull/34)** Conv dilation fix, GPU and CPU | [#32](https://github.com/ML4EP/SOFIE/issues/32) | [![merged](https://img.shields.io/badge/merged-8250df?style=flat-square)](https://github.com/ML4EP/SOFIE/pull/34) |
| **[#35](https://github.com/ML4EP/SOFIE/pull/35)** Conv GPU test, SAME_UPPER | [#33](https://github.com/ML4EP/SOFIE/issues/33) | [![merged](https://img.shields.io/badge/merged-8250df?style=flat-square)](https://github.com/ML4EP/SOFIE/pull/35) |
| **[#39](https://github.com/ML4EP/SOFIE/pull/39)** Selu GPU operator | | [![merged](https://img.shields.io/badge/merged-8250df?style=flat-square)](https://github.com/ML4EP/SOFIE/pull/39) |
| **[#40](https://github.com/ML4EP/SOFIE/pull/40)** Pad GPU operator | | [![merged](https://img.shields.io/badge/merged-8250df?style=flat-square)](https://github.com/ML4EP/SOFIE/pull/40) |
| **[#45](https://github.com/ML4EP/SOFIE/pull/45)** dynamic input shapes on the GPU path | [#43](https://github.com/ML4EP/SOFIE/issues/43) | [![merged](https://img.shields.io/badge/merged-8250df?style=flat-square)](https://github.com/ML4EP/SOFIE/pull/45) |
| **[#55](https://github.com/ML4EP/SOFIE/pull/55)** backend-neutral tests, HIP build, AMD fixes | [#51](https://github.com/ML4EP/SOFIE/issues/51), [#68](https://github.com/ML4EP/SOFIE/issues/68) | [![merged](https://img.shields.io/badge/merged-8250df?style=flat-square)](https://github.com/ML4EP/SOFIE/pull/55) |
| **[#69](https://github.com/ML4EP/SOFIE/pull/69)** Gelu GPU operator | | [![merged](https://img.shields.io/badge/merged-8250df?style=flat-square)](https://github.com/ML4EP/SOFIE/pull/69) |
| **[#30](https://github.com/ML4EP/SOFIE/pull/30)** strided-batched Conv GEMM | [#29](https://github.com/ML4EP/SOFIE/issues/29) | [![open](https://img.shields.io/badge/open-1a7f37?style=flat-square)](https://github.com/ML4EP/SOFIE/pull/30) changes requested |
| **[#48](https://github.com/ML4EP/SOFIE/pull/48)** Pool tests sharing a session helper | | [![open](https://img.shields.io/badge/open-1a7f37?style=flat-square)](https://github.com/ML4EP/SOFIE/pull/48) superseded by the test move in #55 |
| **[#41](https://github.com/ML4EP/SOFIE/pull/41)** Softmax, **[#42](https://github.com/ML4EP/SOFIE/pull/42)** TopK | | [![closed](https://img.shields.io/badge/closed-cf222e?style=flat-square)](https://github.com/ML4EP/SOFIE/pull/41) carried into #45 |
| **[#14](https://github.com/ML4EP/SOFIE/pull/14)** BatchNormalization GPU test | | [![closed](https://img.shields.io/badge/closed-cf222e?style=flat-square)](https://github.com/ML4EP/SOFIE/pull/14) upstream landed BatchNormalization first |
{: .table}

Issues without a PR yet: [#25](https://github.com/ML4EP/SOFIE/issues/25) weight-vector kernel into session init, [#36](https://github.com/ML4EP/SOFIE/issues/36) Conv + ReLU fusion, [#74](https://github.com/ML4EP/SOFIE/issues/74) contribution guidelines in the README.

### 7.2 ML4EP/sofieBLAS

| Pull request | Issue | Status |
|---|---|---|
| **[#11](https://github.com/ML4EP/sofieBLAS/pull/11)** runtime GEMM dimensions, algorithm caching | [#10](https://github.com/ML4EP/sofieBLAS/issues/10) | [![merged](https://img.shields.io/badge/merged-8250df?style=flat-square)](https://github.com/ML4EP/sofieBLAS/pull/11) |
| **[#13](https://github.com/ML4EP/sofieBLAS/pull/13)** templated CUDA/HIP test fixture | [#12](https://github.com/ML4EP/sofieBLAS/issues/12) | [![merged](https://img.shields.io/badge/merged-8250df?style=flat-square)](https://github.com/ML4EP/sofieBLAS/pull/13) |
| **[#15](https://github.com/ML4EP/sofieBLAS/pull/15)** quantised GEMM (int8, fp16, FP8) | | [![draft](https://img.shields.io/badge/draft-6e7781?style=flat-square)](https://github.com/ML4EP/sofieBLAS/pull/15) |
{: .table}

### 7.3 root-project/root

| Pull request | Issue | Status |
|---|---|---|
| **[#21730](https://github.com/root-project/root/pull/21730)** Conv dynamic output formula, stride > 1 | [#21729](https://github.com/root-project/root/issues/21729) | [![merged](https://img.shields.io/badge/merged-8250df?style=flat-square)](https://github.com/root-project/root/pull/21730) |
| **[#22438](https://github.com/root-project/root/pull/22438)** Pool asymmetric padding indices | [#22436](https://github.com/root-project/root/issues/22436) | [![merged](https://img.shields.io/badge/merged-8250df?style=flat-square)](https://github.com/root-project/root/pull/22438) |
| **[#22474](https://github.com/root-project/root/pull/22474)** Conv dilation double count | [#22473](https://github.com/root-project/root/issues/22473) | [![merged](https://img.shields.io/badge/merged-8250df?style=flat-square)](https://github.com/root-project/root/pull/22474) |
| **[#22564](https://github.com/root-project/root/pull/22564)** register Swish in the ONNX parser | [#22552](https://github.com/root-project/root/issues/22552) | [![merged](https://img.shields.io/badge/merged-8250df?style=flat-square)](https://github.com/root-project/root/pull/22564) |
| **[#21685](https://github.com/root-project/root/pull/21685)** Keras Conv2D same padding with dilation | [#21684](https://github.com/root-project/root/issues/21684) | [![merged](https://img.shields.io/badge/merged-8250df?style=flat-square)](https://github.com/root-project/root/pull/21685) |
| **[#23200](https://github.com/root-project/root/pull/23200)** Range output size, symbolic INT64 | [#23186](https://github.com/root-project/root/issues/23186) | [![merged](https://img.shields.io/badge/merged-8250df?style=flat-square)](https://github.com/root-project/root/pull/23200) |
{: .table}

Issues without a PR of mine: [#22523](https://github.com/root-project/root/issues/22523) AveragePool ceil_mode divisor (fixed in #22862), [#23226](https://github.com/root-project/root/issues/23226) test split (closed, see [8 Future plans](#8-future-plans)).

## 8 Future plans

- Finish the quantised GEMM support in sofieBLAS ([#15](https://github.com/ML4EP/sofieBLAS/pull/15)) and merge it.
- Then the SOFIE side: review and merge of the quantisation PR ([#53](https://github.com/ML4EP/SOFIE/pull/53)) on top of it, so quantised models run through sofieBLAS on both vendors.
- Separate SOFIE's model representation from code emission. Today each operator class holds both its attributes and its CPU and GPU `Generate` methods, so CPU and GPU work collide in every operator file. Jonas Rembser suggested on [#23226](https://github.com/root-project/root/issues/23226) moving emission into per-backend emitters, which would let ROOT and the standalone repository share the parser and model. No one has started this yet; ROOT [#23443](https://github.com/root-project/root/pull/23443), which made the operator headers private, is the closest groundwork.
- Keep working with the ML4EP team on the GPU backend: the open follow-ups above, operator coverage as models need it, and whatever else comes up as the backend is used.

## 9 Conclusion

In May the alpaka backend of SOFIE could run a fixed-size model on an NVIDIA GPU if the model happened to use only the operators it had. In October it runs models with pooling, padding, the common activations, Softmax and TopK, accepts input sizes that change from call to call, keeps one BLAS algorithm per shape instead of searching on every new size, and passes the same 243 tests on an AMD MI100 as on an H100. The testing work changed how the project catches bugs: operators now ship with their tests, the tests no longer name a vendor, and a second GPU vendor in CI is what found the last two kernel bugs. Quantised GEMM in sofieBLAS and the separation of SOFIE's model from its code emission are the two threads I am carrying on with the ML4EP team after the programme.

## 10 Acknowledgements

A huge thank you to my mentors, [Sanjiban Sengupta](https://github.com/sanjibansg) and [Dr. Lorenzo Moneta](https://github.com/lmoneta). Sanjiban helped and guided me through every part of this project, and his constructive feedback and the techniques he showed me along the way made me far more comfortable picking up new things and made my own software work better with every review. Both of them kept me encouraged for the whole twenty-two weeks, and I could not have asked for better mentors.

A huge thank you as well to CERN and the ML4EP group for the CERN access and a smooth experience throughout, which is what made the GPU work and all of the testing on real hardware possible. Thanks to [Jonas Rembser](https://github.com/guitargeek) for his reviews of my ROOT pull requests.

Thanks to [Prof. Caterina Doglioni](https://github.com/caterina-doglioni) and the University of Manchester for the Summer of BOA group, a weekly room of students working on related problems that I learned a lot from, and to my fellow SOFIE interns at CERN, Shaun Lee and Antreas Ioannou, for the work alongside mine.

Lastly, thank you to Google and the HSF for this wonderful opportunity: the people I met, the learning curve, the open source community, and the chance to work with such a prestigious lab and collaborate with these wonderful colleagues. And to my family, friends and parents, for everything else.
