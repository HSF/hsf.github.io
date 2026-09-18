---
project: NNPDF
title: EKO Oxidation
author: Akshat Rai
photo: blog_authors/AkshatRai.jpg
date: 16.09.2026
year: 2026
layout: blog_post
logo: nnpdf.png
intro: |
    This project aimed to modernize EKO (Evolution Kernel Operators) by bridging its Python codebase with a Rust backend. Over the summer, I implemented a robust cross-language interoperability layer, developed two dedicated interface crates for C-ABI and Python bindings, backed by automated CI/CD workflows that deploy directly to PyPI and GitHub Releases.
---

<div align="center">
<img alt="NNPDF Logo" src="{{ site.baseurl }}/images/nnpdf.png" width="500"/>
</div>

## Mentors: Felix Hekhorn and Juan Manuel Cruz Martinez

## [Project Link (NNPDF Collaboration) - EKO](https://github.com/NNPDF/eko)

### The short version

EKO (Evolution Kernel Operators) is a Python library that solves the DGLAP equations used to extract Parton Distribution Functions from collider data. It precomputes solution operators independently of the actual PDF, which turns a repeated integro-differential problem into a one-off integration followed by fast linear algebra. That integration is expensive, and getting more expensive as EKO adds higher perturbative orders and QED effects, so the project has been "oxidizing": moving the hot loop from pure Python into Rust, one piece at a time, while `scipy` and `numba` keep the rest running.

Coming in, the Rust port already existed in prototype form. My job was to turn it into a documented architecture, an interface that doesn't leak memory and is quicker than the legacy code, a public C ABI and a PyO3 binding for consumers who aren't `eko` itself, and a release pipeline that gets all of that onto PyPI, GitHub Releases, and crates.io. Along the way, I also explored simplifying the core call chain, benchmarked the attempt thoroughly, and documented the negative result to establish clear constraints and validate the existing architecture.

### Mapping the architecture

The first task ([#516](https://github.com/NNPDF/eko/issues/516)) was to document what the current Python/Rust split actually does before changing any of it. [PR #521](https://github.com/NNPDF/eko/pull/521) walked the user entry point (`runner.solve`) down through `Operator` and `OperatorMatrixElement`, the parallel loop over target x-grid points, the inner loop over source basis functions and flavour labels, and finally into `scipy.integrate.quad` itself, comparing the pure-Python/Numba `quad_ker` path against the Rust `rust_quad_ker` entry point.

A companion PR, [#529](https://github.com/NNPDF/eko/pull/529), added `performance.md` alongside it: raw benchmark numbers and the commands used to produce them, kept separate from the narrative document so the two could be updated independently.

### Publishing what already existed

While the two crates (`ekore` and `eko`) were already publishing successfully, there was a problem with `eko` reaching PyPI ([#517](https://github.com/NNPDF/eko/issues/517)). [PR #522](https://github.com/NNPDF/eko/pull/522) fixed this by updating `maturin.yml` to call `bump-versions.py` and replacing the deprecated Maturin publish action with a modern build-and-upload step. I confirmed the pipeline end-to-end using a throwaway PyPI project (`akshat-eko-rs-test`).

### Negative attempt to improve performance

This is the part of the summer worth being specific about, because it's a negative result with real numbers behind it, not just an abandoned idea.

The architecture that ships today looks like this for the Rust-enabled path:

```text
scipy.integrate.quad(LowLevelCallable(rust_quad_ker, &cfg), 0.5, 1-ε)
  ↓ scipy's C backend calls the function pointer directly, no Python overhead
rust_quad_ker(u, *args)              [crates/eko/src/lib.rs]
  ↓
ekore (Rust) → anomalous dimensions
  ↓ callback
cb_quad_ker_qcd / cb_quad_ker_qed    [Numba]
  ↓
kernels/singlet.py, non_singlet.py → evolution operator matrix
  ↓
f64 returned to scipy
```

`scipy → Rust → Numba → Rust → scipy`. Rust owns the entry point and the anomalous-dimension computation, then hands off to Numba for the evolution operator matrix, which hasn't been ported yet.

While working on the kernel split, I tried inverting this: keep the `LowLevelCallable` entry point in Numba instead of Rust, using `nb.cfunc`, and call into Rust only for the anomalous dimensions via `ctypes`:

```text
scipy.integrate.quad(LowLevelCallable(quad_ker_llc, &cfg), 0.5, 1-ε)
  ↓
quad_ker_llc(u, *args)               [nb.cfunc]
  ↓ ctypes call into Rust
ekors.qcd_gamma_singlet / qcd_gamma_ns
  ↓
ekore (Rust) → anomalous dimensions
  ↓ back to Numba
kernels/singlet.py, non_singlet.py → evolution operator matrix
  ↓
f64 returned to scipy
```

After struggling with complex `ctypes` type coercion across the boundary, I used a `#[pyfunction]` stand-in to benchmark the approach (`poe lha -m nnlo and sv`).

The results were stark compared to the master branch (`rs → nb → rs`):

<table style="margin: 0 auto; border-collapse: collapse; text-align: left;">
  <thead>
    <tr>
      <th style="border: 1px solid #ccc; padding: 8px;">Metric</th>
      <th style="border: 1px solid #ccc; padding: 8px;">Master</th>
      <th style="border: 1px solid #ccc; padding: 8px;">Inverted (<code>nb &rarr; rs &rarr; nb</code>)</th>
      <th style="border: 1px solid #ccc; padding: 8px;">Ratio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Wall clock</td>
      <td style="border: 1px solid #ccc; padding: 8px;">11:16</td>
      <td style="border: 1px solid #ccc; padding: 8px;">20:24</td>
      <td style="border: 1px solid #ccc; padding: 8px;">~1.8&times; worse</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Peak RSS</td>
      <td style="border: 1px solid #ccc; padding: 8px;">616 MB</td>
      <td style="border: 1px solid #ccc; padding: 8px;">1953 MB</td>
      <td style="border: 1px solid #ccc; padding: 8px;">~3.2&times; worse</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Cost per <code>quad</code> call</td>
      <td style="border: 1px solid #ccc; padding: 8px;">~1.5 ms</td>
      <td style="border: 1px solid #ccc; padding: 8px;">~5 ms</td>
      <td style="border: 1px solid #ccc; padding: 8px;">~3.3&times; worse</td>
    </tr>
  </tbody>
</table>

Both regressions stemmed from Numba's compilation model:

* **Memory:** `ctypes` pointers prevent the use of `cache=True`. Instead of writing artifacts to disk and releasing them, Numba was forced to keep the entire compiled call graph resident in memory.
* **Time:** The inverted path pays a heavy Numba-to-Rust transition tax on *every* `quad` node evaluation. In contrast, the master path does the expensive setup in Rust exactly once beforehand.

Because the `Numba → Rust` pattern proved unviable for this workload, the PR was not merged. However, the reasoning and metrics were permanently documented in [architecture.md](https://github.com/NNPDF/eko/blob/master/extras/architecture.md) for future reference.

### ekore_capi: a stable C-ABI

To make `ekore` accessible to standard high-energy physics tooling (C, C++, and eventually Fortran) ([Issue #519](https://github.com/NNPDF/eko/issues/519)), [PR #537](https://github.com/NNPDF/eko/pull/537) introduced the `ekore_capi` crate. Before exposing this C interface, several prerequisite PRs were merged to harden the Rust codebase. This groundwork included ensuring benchmarks ran in `--release` mode, removing hidden heap allocations in favor of fixed caller-provided buffers, strictly scoping visibility (`pub(crate)`), centralizing workspace dependencies, updating MSRV, and bolstering unit tests and literature citations.

The `ekore_capi` crate relies on a few key FFI conventions:

* **Safe Layouts:** Complex numbers cross the boundary as a `#[repr(C)] ComplexF64` struct to avoid relying on C99 `double complex` layouts.
* **Opaque Pointers:** The Mellin-space harmonic cache is managed via `cache_new` and `cache_delete`.
* **Caller Allocation:** Computations use `<name>_result_len` helpers so callers can safely pre-allocate correctly sized buffers.
* **Automation:** `cargo-c` and `cbindgen` handle header and `pkg-config` generation automatically.

Finally, [PR #553](https://github.com/NNPDF/eko/pull/553) added `install-capi.sh`, a POSIX shell installer for pre-built binaries.

### ekore_py: direct PyO3 bindings

While `ekore_capi` supports C, C++, and Fortran, Python users seeking only the standalone physics functions lacked direct access. [PR #554](https://github.com/NNPDF/eko/pull/554) solved this by introducing `ekore_py`, which exposes `ekore`'s anomalous dimensions and operator matrix elements as native Python functions via PyO3 (packaged on PyPI as `ekore-rs`, imported as `ekore_rs`). This serves as a general-purpose physics library and is deliberately distinct from the internal `eko-rs` bridge package.

Most of the crate's logic resides in `macros.rs`, which uses a single macro to generate the `#[pyfunction]` boilerplate for the various anomalous dimension and OME wrappers.

### The libome exploration

The project's task list required preparation for a third-party C++ contribution. To test this before any real external attempt, [PR #562](https://github.com/NNPDF/eko/pull/562) evaluated whether `ekore` could successfully call out to an external C++ library. I wrote a mock C++ library (`extras/gsoc/libome`) to stand in for the real `libome`, compiled it via a Rust `build.rs` script using the `cc` crate, and consumed it from a new `as3.rs` file.

This demonstrated calling an external C++ library from `ekore` does not incur meaningful performance costs. It also demonstrated two legitimate ways to wire the connection. The first method is to vendor the real library as a submodule, build it with the `cmake` crate, and explicitly link its dependencies like GSL. The second method is to link directly against a pre-built `.so` file. In this latter case, Rust does not even need the C++ headers because `rustc` reads the function signatures directly from its own `unsafe extern "C"` declarations and `#[repr(C)]` structs.

However, integrating the real library is currently on pause. The real [libome](https://gitlab.com/libome/libome) operates in x-space, while the `ekore` OME machinery operates in Mellin N-space. Bridging this gap requires a dedicated transform layer and help from a third party, which currently has an indefinite timescale. The mock integration code itself is fine as is, but rather than merging it while we wait, [PR #562](https://github.com/NNPDF/eko/pull/562) was closed. We intentionally preserved the branch as a fully functional starting point for future developers once the third-party work is ready. Finally, [PR #567](https://github.com/NNPDF/eko/pull/567) officially documented this mismatch in `architecture.md` so the constraint is recorded rather than rediscovered.

### Fixing the release pipeline

The final stretch of the summer focused entirely on ensuring the release pipeline functioned correctly across all registries.

[PR #556](https://github.com/NNPDF/eko/pull/556) fixed macOS specific C-ABI linking errors, removed static library generation, and enabled dynamic versioning so `eko` wheel names tracked the correct release. [PR #561](https://github.com/NNPDF/eko/pull/561) standardized workflow names to a `<category>-<target>.yml` convention, restricted release triggers to semver tags, and added `workflow_dispatch` inputs for manual retries.

Testing these changes against real registries in [PR #569](https://github.com/NNPDF/eko/pull/569) required several fixes before succeeding. `eko` failed due to a dynamic versioning bug, `ekore-rs` published without a description, and `eko-rs` failed due to a misdirected trusted publisher entry. Fixing these got all three packages live. During this process, Felix also pointed out a risk: while manual tag inputs help retry broken releases, they introduce the danger of accidentally attaching new code to an old tag.

To secure the pipeline against that risk, [PR #573](https://github.com/NNPDF/eko/pull/573) added explicit tag validation, which does multiple checks to ensure the `workflow_dispatch` workflow is not overriding anything. It also closed out the remaining gaps by adding proper PyPI descriptions, bypassing dynamic versioning during manual workflows, and updating GitHub action versions across the board.

### What got merged

<table style="margin: 0 auto 10px auto; border-collapse: collapse; text-align: left;">
  <thead>
    <tr>
      <th style="border: 1px solid #ccc; padding: 8px;">Contribution</th>
      <th style="border: 1px solid #ccc; padding: 8px 50px 8px 8px;">PR</th>
      <th style="border: 1px solid #ccc; padding: 8px;">Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Architecture documentation (<code>architecture.md</code>)</td>
      <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://github.com/NNPDF/eko/pull/521">#521</a></td>
      <td style="border: 1px solid #ccc; padding: 8px;">Merged</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Fixed crate/package publishing (crates.io, PyPI)</td>
      <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://github.com/NNPDF/eko/pull/522">#522</a></td>
      <td style="border: 1px solid #ccc; padding: 8px;">Merged</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Inverted <code>Numba &rarr; Rust &rarr; Numba</code> call chain (benchmarked, rejected)</td>
      <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://github.com/NNPDF/eko/pull/526">#526</a></td>
      <td style="border: 1px solid #ccc; padding: 8px;">Not merged, documented in <code>architecture.md</code></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Performance benchmarking document</td>
      <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://github.com/NNPDF/eko/pull/529">#529</a></td>
      <td style="border: 1px solid #ccc; padding: 8px;">Merged</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Split integration kernel from the <code>Operator</code> class</td>
      <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://github.com/NNPDF/eko/pull/531">#531</a></td>
      <td style="border: 1px solid #ccc; padding: 8px;">Merged</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;"><code>eko-rs</code> workflow fix</td>
      <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://github.com/NNPDF/eko/pull/540">#540</a></td>
      <td style="border: 1px solid #ccc; padding: 8px;">Merged</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;"><code>--release</code> build flag fix</td>
      <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://github.com/NNPDF/eko/pull/541">#541</a></td>
      <td style="border: 1px solid #ccc; padding: 8px;">Merged</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Removed mallocs, single-buffer integration</td>
      <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://github.com/NNPDF/eko/pull/542">#542</a></td>
      <td style="border: 1px solid #ccc; padding: 8px;">Merged</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Tightened <code>ekore</code> visibility, split <code>constants.rs</code></td>
      <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://github.com/NNPDF/eko/pull/543">#543</a></td>
      <td style="border: 1px solid #ccc; padding: 8px;">Merged</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Centralised workspace dependencies</td>
      <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://github.com/NNPDF/eko/pull/544">#544</a></td>
      <td style="border: 1px solid #ccc; padding: 8px;">Merged</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">MSRV bump to 1.85.0 / Edition 2024</td>
      <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://github.com/NNPDF/eko/pull/545">#545</a></td>
      <td style="border: 1px solid #ccc; padding: 8px;">Merged</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Tests for <code>spacelike.rs</code></td>
      <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://github.com/NNPDF/eko/pull/546">#546</a></td>
      <td style="border: 1px solid #ccc; padding: 8px;">Merged</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Restored literature references</td>
      <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://github.com/NNPDF/eko/pull/550">#550</a></td>
      <td style="border: 1px solid #ccc; padding: 8px;">Merged</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;"><code>ekore_capi</code> crate addition</td>
      <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://github.com/NNPDF/eko/pull/537">#537</a></td>
      <td style="border: 1px solid #ccc; padding: 8px;">Merged</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;"><code>install-capi.sh</code> installer</td>
      <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://github.com/NNPDF/eko/pull/553">#553</a></td>
      <td style="border: 1px solid #ccc; padding: 8px;">Merged</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;"><code>ekore_py</code> crate addition, published as <code>ekore-rs</code></td>
      <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://github.com/NNPDF/eko/pull/554">#554</a></td>
      <td style="border: 1px solid #ccc; padding: 8px;">Merged</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">macOS release fixes, dynamic versioning</td>
      <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://github.com/NNPDF/eko/pull/556">#556</a></td>
      <td style="border: 1px solid #ccc; padding: 8px;">Merged</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Updated <code>architecture.md</code> with new crates</td>
      <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://github.com/NNPDF/eko/pull/559">#559</a></td>
      <td style="border: 1px solid #ccc; padding: 8px;">Merged</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Full GitHub workflow refactor</td>
      <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://github.com/NNPDF/eko/pull/561">#561</a></td>
      <td style="border: 1px solid #ccc; padding: 8px;">Merged</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;"><code>libome</code> external C++ interop prototype</td>
      <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://github.com/NNPDF/eko/pull/562">#562</a></td>
      <td style="border: 1px solid #ccc; padding: 8px;">Not merged, branch kept as reference</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Documented <code>libome</code> mismatch in <code>architecture.md</code></td>
      <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://github.com/NNPDF/eko/pull/567">#567</a></td>
      <td style="border: 1px solid #ccc; padding: 8px;">Merged</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Live PyPI release fixes (<code>eko</code>, <code>eko-rs</code>, <code>ekore-rs</code>)</td>
      <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://github.com/NNPDF/eko/pull/569">#569</a></td>
      <td style="border: 1px solid #ccc; padding: 8px;">Merged</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Package descriptions, tag validation</td>
      <td style="border: 1px solid #ccc; padding: 8px;"><a href="https://github.com/NNPDF/eko/pull/573">#573</a></td>
      <td style="border: 1px solid #ccc; padding: 8px;">Merged</td>
    </tr>
  </tbody>
</table>

**Left for later:** Fortran test coverage for `ekore_capi` was explicitly postponed to [#566](https://github.com/NNPDF/eko/issues/566). The C ABI supports it architecturally, but no automated Fortran suite exists yet.

### Final Architecture

<div align="center">
<img alt="Final Architecture" src="https://github.com/user-attachments/assets/54fa33cf-e766-41b5-80b1-d7d5cb028b95" width="900"/>
</div>

### What I'd tell next year's contributor

**Benchmark architectural intuition.** Inverting the `Numba`/`Rust` call chain seemed simpler but performed worse across all metrics: about 1.8&times; slower wall-clock time and over 3&times; worse peak memory and per-call cost. Catching this early with a `poe lha` benchmark prevented a permanent regression.

**Numba's caching model struggles with raw pointers.** Both major bugs I encountered (the `select_singlet_element` typing error and the `ctypes` memory blowup) stemmed from unintuitive cache invalidation. When integrating FFI into a Numba codebase, test caching behavior in isolation first.

**Scrutinize installer scripts like application code.** The initial `install-capi.sh` draft contained classic POSIX traps: a `read` failure under a pipe, shell injection from unquoted paths, and unescaped `&` characters in `sed`. These vulnerabilities often hide perfectly within the happy path.

**Document closed PRs.** The `libome` PR was closed unmerged, but preserving the branch and formally documenting the domain mismatch in `architecture.md` ensures future developers will not have to rediscover the same dead end.

### Thanks

A huge thank you to Felix Hekhorn and Juan Cruz-Martinez for bringing me onto this project and for their exceptional mentorship over the past few months. Their detailed feedback improved the code we shipped and profoundly shaped how I approach software design, performance profiling, and open-source development. I also want to express my sincere appreciation to the NNPDF team, the HEP Software Foundation, and GSoC team for making this summer project possible. I have learned an immense amount during this time, and I am deeply grateful for the experience and the opportunity to work alongside such talented developers. I am excited to stay involved and continue contributing to the repository well beyond the end of the program.
