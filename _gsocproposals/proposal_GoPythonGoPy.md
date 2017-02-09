---
title: Updating gopy to support Python3 and PyPy
layout: gsoc_proposal
project: GoPython
organization: LPC-Clermont
---

## Description

[Go](https://golang.org) is an open-source language with builtin primitives to easily handle concurrency.
[Python](https://python.org) is the _de facto_ glue language in science.
More and more analyses are written in Python with performance hotspots being rewritten in `C/C++` or `Cython`.

What if we could leverage the concurrency features of `Go` from `Python`?

This is the goal of the [gopy](https://github.com/go-python/gopy) tool.
`gopy` takes a `Go` package, inspects it and generates `C` code to wrap it with the `CPython-2` API.
This is a process that is made relatively straightforward thanks to the high level constructs of `Go` and its standard libraries to inspect `Go` code (mainly `go/build` and `go/types`.)

However, `gopy` only generates wrappers for `CPython-2`.
The science ecosystem is finally migrating to `Python-3`: `gopy` needs to support this migration.

This project intends to modify the code generation mechanism to generate (pure Python) `cffi` code so that `Go` packages can be used from `CPython` (2 and 3), `PyPy` and `IronPython`.

## Task ideas

 * Design and implement a mechanism to share values and types between `Go (>=1.6)` and _a_ `Python` VM
   * Migrate the current `gopy` unit tests to this new mechanism
   * Implement wrapping of functions with builtin arguments
   * Implement wrapping of functions with slices/arrays of builtin arguments
   * Implement wrapping of functions with user types
   * Detect functions returning a `Go` `error` and make them pythonic (raising an `Exception`)
   * Implement wrapping of user types
   * Implement wrapping of `Go` `map`s
   * Implement wrapping of `Go` interfaces

## Expected results

A new `gopy` command that can generate wrapping code (using `cffi`) for the current set of unit tests of `gopy`, with `Go >= 1.5`.

## Requirements

Go language, Python language, git.

## Mentors
  * [Sebastien Binet](mailto:binet@cern.ch)
  * [Thomas Bellembois](mailto:thomas.bellembois@clermont.in2p3.fr)

## Links
  * [Go](https://golang.org)
  * [Python](https://python.org)
  * [gopy](https://github.com/go-python/gopy)
  * [gopy tutorial](https://blog.gopheracademy.com/advent-2015/gopy/)
  * [cffi](http://cffi.readthedocs.io/en/latest/)
