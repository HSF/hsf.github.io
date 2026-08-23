---
project: Spack
title: Debuggable Installations For Spack Packages
author: Sebastian Paucar
avatar: https://avatars.githubusercontent.com/u/142455262?s=400&v=4
date: 23.08.2026
year: 2026
layout: blog_post
logo: hsf_logo_angled.png
intro: |
  A new machine- and build-system-agnostic debugging standard for Spack packages is implemented. DWARF-referenced in/out-of-tree and generated source code, along with split debug symbols, are preserved on demand alongside automated GDB configurations. An OCI buildcache infrastructure is built for debug info distribution (fetch/push).
---

<table>
<tr><td><strong>Name<strong></td><td>Sebastian Paucar</td></tr>
<tr><td><strong>Organisation<strong></td><td><a href="https://www.umanitoba.ca/">University of Manitoba</a>, <a href="https://home.cern/">CERN</a>, <a href="https://hepsoftwarefoundation.org/">HSF</a></td></tr>
<tr><td><strong>Mentor<strong></td><td>Wouter Deconinck</td></tr>
<tr><td><strong>Project<strong></td><td>Debuggable Installations For Spack Packages</td></tr>
</table>

---

## Introduction
 
Spack builds packages, strips embedded debug symbols when configured, and removes the compilation directory. Debug info is machine- and compilation-path-dependent throughout this process. If a package later crashes in production, there is often no practical way back to source-level debugging without rebuilding the exact package from scratch, often on a machine and with a toolchain that no longer exist.

This project builds a complete pipeline that makes any Spack-installed binary debuggable after the fact: capture debug sources and symbols at install time without bloating the installed package, split and store them out-of-prefix, recover them on-demand for packages that were installed without the flags, and publish them to an OCI registry automatically so that any machine, not just the one that built the package, can pull them down and get a working `gdb` session.
 
The work spans three repositories (`spack/spack`, `spack/spack-packages`, `spack/compiler-wrapper`) plus integration into EIC's own `eic/containers` build pipeline, where it now underlies a dedicated `dbg` container environment.

--

## Community Discussion Highlights

* [PR 52768](https://github.com/spack/spack/pull/52768) (`spack/spack`): DWARF-referenced source hook and symbol splitting plus GDB init for debuggable installations.
* [PR 19](https://github.com/spack/compiler-wrapper/pull/19) (`spack/compiler-wrapper`): `-ffile-prefix-map=<staging>=.` and `--build-id` injection in compiler-wrapper.
* [PR 5353](https://github.com/spack/spack-packages/pull/5353) (`spack/spack-packages`): set `SPACK_DEBUG_PREFIX_MAP` for `-ffile-prefix-map=<stage>=.` injection at compiler-wrapper level.
* [Issue 52580](https://github.com/spack/spack/issues/52580) (`spack/spack`): `.spack/` vs relative paths vs compiler-wrapper remaps.
* [Framework demo](https://github.com/SebastianPaucar/Spack-Debuggable-Installations/tree/main) (`SebastianPaucar/Spack-Debuggable-Installations`): Containerized demo to test Spack's new `--debug-source` and `--debug-symbols` install flags against a real package crash scenario.

--

## Implementation Highlights

* `spack/spack`: [`feature/debuggable-installations-source-v1.2.2`](https://github.com/SebastianPaucar/spack/tree/feature/debuggable-installations-v1.2.2) branch (**NEW**: implements install-time (`--debug-sources` and `--debug-symbols`) and on-demand (`spack debug stage-source` and `spack debug split-symbols`)) debug artifact generation and OCI artifact distribution (`spack buildcache push --debug-sources --debug-symbols` and `spack debug fetch`).
* `spack/compiler-wrapper`: [`feature/debug-prefix-map`](https://github.com/SebastianPaucar/compiler-wrapper/tree/feature/debug-prefix-map) branch (**NEW**: `--build-id` and `-ffile-prefix-map` injection for carrying ELF build-ID notes and normalized DWARF-recorded paths in a reproducible way).
* `spack/spack-packages`: [`feature/compiler-wrapper-build-id-v2026.06.0`](https://github.com/SebastianPaucar/spack-packages/tree/feature/compiler-wrapper-build-id-v2026.06.0) branch (**NEW**: wires in the new `feature/debug-prefix-map` compiler-wrapper version).
* `eic/containers`: [`feature/debuggable-installations-spack-v1.2.2`](https://github.com/eic/containers/tree/feature/debuggable-installations-spack-v1.2.2) branch (**NEW**: Implementation of the debuggable installation framework for the EIC container image build).

---

## Acknowledgements

Thanks to Wouter Deconinck for the architectural steering throughout, particularly on the OCI-as-storage framing for debug info distribution, and to the Spack community for review feedback on compiler-wrapper flag injection and DAG hash scoping.