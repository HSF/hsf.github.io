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

---

## Community Discussion Highlights

* [PR 52949](`https://github.com/spack/spack/pull/52949`): Post-install source-staging and symbol-splitting hook, merge-aware gdbinit generation, and autopush of debug artifacts to an OCI buildcache (`releases/v1.2`).
* [PR 52768](https://github.com/spack/spack/pull/52768) (`spack/spack`): DWARF-referenced source hook and symbol splitting plus GDB init for debuggable installations.
* [PR 19](https://github.com/spack/compiler-wrapper/pull/19) (`spack/compiler-wrapper`): `-ffile-prefix-map` and `--build-id` injection in compiler-wrapper.
* [PR 5353](https://github.com/spack/spack-packages/pull/5353) (`spack/spack-packages`): set `SPACK_DEBUG_PREFIX_MAP` for `-ffile-prefix-map=<stage>=.` injection at compiler-wrapper level.
* [Issue 52580](https://github.com/spack/spack/issues/52580) (`spack/spack`): `.spack/` vs relative paths vs compiler-wrapper remaps.
* [Framework demo](https://github.com/SebastianPaucar/Spack-Debuggable-Installations/tree/main) (`SebastianPaucar/Spack-Debuggable-Installations`): Containerized demo to test Spack's new `--debug-source` and `--debug-symbols` install flags against a real package crash scenario.
* [Full GSoC project presentation](https://drive.google.com/file/d/1MtUounbk6Lr6g-pj6lehSRe5fCoRCwUT/view): Framework development overview, covering feedback, architecture, implementation, and proof-of-concepts.

---

## Implementation Highlights

* `spack/spack`: [`feature/debuggable-installations-source-v1.2.2`](https://github.com/SebastianPaucar/spack/tree/feature/debuggable-installations-v1.2.2) branch (**NEW**: implements install-time (`--debug-sources` and `--debug-symbols`) and on-demand (`spack debug stage-source` and `spack debug split-symbols`)) debug artifact generation and OCI artifact distribution (`spack buildcache push --debug-sources --debug-symbols` and `spack debug fetch`).
* `spack/compiler-wrapper`: [`feature/debug-prefix-map`](https://github.com/SebastianPaucar/compiler-wrapper/tree/feature/debug-prefix-map) branch (**NEW**: `--build-id` and `-ffile-prefix-map` injection for carrying ELF build-ID notes and normalized DWARF-recorded paths in a reproducible way).
* `spack/spack-packages`: [`feature/compiler-wrapper-build-id-v2026.06.0`](https://github.com/SebastianPaucar/spack-packages/tree/feature/compiler-wrapper-build-id-v2026.06.0) branch (**NEW**: wires in the new `feature/debug-prefix-map` compiler-wrapper version).
* `eic/containers`: [`feature/debuggable-installations-spack-v1.2.2`](https://github.com/eic/containers/tree/feature/debuggable-installations-spack-v1.2.2) branch (**NEW**: Implementation of the debuggable installation framework for the EIC container image build).

---

## Design

### Debug-inspired compiler flag injection

The `spack/compiler-wrapper` repository contains the shell script `cc.sh` that sits between every Spack package's build system and the actual compiler, intercepting compiler invocations to reorder and inject flags. This wrapper was extended to inject two things at link time: `--build-id`/`-Wl,--build-id`, which makes every produced binary carry a standard ELF build-ID note, and a second `-ffile-prefix-map` remap (`<build-dir>=./build`, alongside the existing `<source-dir>=.` remap) so DWARF-recorded paths are normalized and portable across machines rather than embedding one machine's absolute build path. This is the foundation for making the installations debuggable and the recorded DWARF paths reproducible. Spack previously did not include these flags, which made debug information for debug-mode-installed packages not identifiable by build ID and dependent on ephemeral, host-machine-specific absolute paths used at compilation time that no longer exist once the installation is complete.

### Two capture paths, one cache format

For actual debugging sessions, GDB needs to find DWARF-referenced sources and debug symbols. These debug artifacts now live in an out-of-prefix cache, `$debug_source_root/<pkg>-<version>-<dag_hash>/` (with `$debug_source_root` configured in Spack, defaulting to `~/.spack/debug-sources` if not configured), deliberately outside the install prefix so it never affects the package installation prefix and never ships inside a regular buildcache tarball, as requested by the community. Two independent Spack subcommands write to this cache:

**Install-time (`spack install --debug-source --debug-symbols`)**: While the package's build directory is still alive, `--debug-source` parses the DWARF `DW_AT_comp_dir`/`DW_AT_name` pairs out of every compiled ELF binary via `readelf` and copies exactly the source files GDB will ask for, including generated sources, headers, and files from an out-of-source build directory that were never in the pristine source tarball. `--debug-symbols` then runs `objcopy --only-keep-debug`/`--strip-debug` on every ELF binary, shrinking the installed package while keeping full debug info retrievable.

**On-demand (`spack debug stage-source` / `spack debug split-symbols`)**: This is the fallback for anything already installed without the `--debug-*` flags. `stage-source` re-fetches the pristine upstream tarball and stages it. `split-symbols` needs no original build context at all; it operates purely on the installed binary, so it works identically whether the package was built locally or fetched from a buildcache mirror.

Both paths converge to generate a ready-to-use GDB command file (`gdbinit`) with `substitute-path` and `debug-file-directory` rules pointing at the cache. This is merge-aware, so running `split-symbols` after `stage-source` (or vice versa) never clobbers the other's file contribution.

### Debug artifact buildcache redistribution

The capture pipeline being correct on one machine only helps that machine. The second half of the project makes the cache portable: `spack buildcache push --debug-source --debug-symbols` packages the split symbols and captured DWARF-referenced source into an OCI manifest per build ID (since a debuginfod-style consumer uses the build ID as a lookup key), pushes it as `debuginfo-<build-id>` alongside the regular package tag, and a matching `spack debug fetch` on any other machine pulls it back down into the local debug cache layout, regenerating a correct `gdbinit` in place.

This is also integrated into Spack's existing autopush mechanism, which already auto-pushes every from-source install to whichever OCI mirrors are marked `autopush: true` in `mirrors.yaml`, using the same credentials and mirror configuration as the regular package push.

---

### Landing it in EIC's containers

`eic/containers` builds the family of EIC container images (`xl`, `ci`, `prod`, `cvmfs`, `dbg`, and others) from a single multi-stage Dockerfile, orchestrated by `scripts/build-eic.sh` and driven by per-environment Spack manifests under `spack-environment/`.


The Dockerfile's `builder_installation_default`/`builder_installation_custom` stages are the only ones that compile from source; `runtime_installation_default`/`runtime_installation_custom` install exclusively `--use-buildcache only` and never touch a compiler. Since `--debug-sources` only have anything to capture during an actual compile, the flags only make sense in the builder stages, and only for one environment: `dbg`, a container purpose-built for debugging whose HEP packages are already declared with `build_type=Debug`. `dbg`'s environment manifest (`spack-environment/dbg/spack.yaml` and its `epic/spack.yaml`) also pins the compiler-wrapper prototype that emits build-ID notes and the `-ffile-prefix-map` remap the whole debuggable mechanism depends on.

The actual EIC Spack artifact publishing happens through a Spack-side mechanism, `hooks/autopush.py`, a post-install hook that fires after every from-source install and pushes to whichever mirrors `mirrors.yaml` marks with `autopush: true` (`eicweb` and `ghcr`), both of which are already configured in the repository's `mirrors.yaml`, with credentials wired through the Dockerfile's existing `--mount=type=secret` blocks.

The end state, accessible from any machine with `eicweb`/`ghcr` access: each compiled `dbg` binary gets an OCI `debuginfo-<build-id>` tag containing two layers: the split `.debug` symbols and a tarball of the DWARF-referenced source tree. `spack debug fetch` retrieves these artifacts, reconstructs the local cache, and regenerates a working `gdbinit`, whether the artifacts were captured locally or fetched from the registry. Thus, a crash in a `dbg`-built EIC binary can be fully debugged (with source and symbols) on a machine that never built it.

---

## Acknowledgements

Thanks to Wouter Deconinck for the architectural steering throughout, particularly on the OCI-as-storage framing for debug info distribution, and to the Spack community for review feedback on compiler-wrapper flag injection and DAG hash scoping.