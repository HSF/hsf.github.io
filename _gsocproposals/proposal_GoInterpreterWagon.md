---
title: Launching Wagon, a WebAssembly interpreter in Go
layout: plain
project: GoInterpreter
organization: LPC-Clermont
---

## Description

[Go](https://golang.org) is an open-source language with builtin primitives to easily handle concurrency.
It is now the building block of many cloud-based companies and is considered as the "language for the cloud". (_e.g:_ [Docker](https://www.docker.com), [Kubernetes](https://kubernetes.io), ...)
Go was explicitly designed to address software engineering at scale, and is thus a natural fit for many HEP use cases.
Indeed, Go has already great numerical and scientific libraries (for matrix operations, plotting, statistical analyses, graphs traversal, etc...) regrouped under the [Gonum](https://github.com/gonum) organization.
Go can also be used from [Jupyter](http://jupyter.org) thanks to the [gophernotes](https://github.com/gopherds/gophernotes) kernel developed by the [gopherds](https://github.com/gopherds) data science community.

However, the interpreter used by gophernotes to turn Go into a great data exploration environment is not a real `read-eval-print-loop` (REPL): it just recompiles snippets of Go code on the fly.
While this workaround is very serviceable, it carries its own set of issues, mainly with code that has side-effects.

This project intends to create the foundations for a Go interpreter, written in Go, for Go.
Writing an interpreter is a lot of work and is a daunting task.
The main development of this project will focus on creating the needed tooling (libraries and executables) to be able to consume [WebAssembly](http://webassembly.org) bytecode (`wasm`) and interpret it.
A package will be developed in Go to decode `wasm` binary files and display their sections, informations and content.
Another package will then implement a simple stack based interpreter, loading `wasm` files interactively and executing simple functions.
The creation of these `wasm` bytecode modules by the Go toolchain is out of the scope of this project.

## Task ideas

 * Design and implementation of a package to read `wasm` files
   * Display `wasm` sections and subsections
   * Create unit tests based on the official `wasm` specifications
   * Create a simple `readelf`-like executable (`readwasm` ?) for `wasm` files
   * Create a simple web server that displays the same informations than `readwasm`
 * Design and implementation of a package to load `wasm` bytecode functions
 * Design and implementation of a stack-based interpreter in Go that interprets `wasm` bytecode
   * Handling of bytecode instruction pointer
   * Handling of a few `wasm` bytecode instructions
   * Handling of the interpreter environment context (stack variables, `wasm` bytecode, ...)
 * Use cases:
   * apply the interpreter to the `"hello world"` function for interpreters (`add(i,j)` or `sum(a,b)`)
   * create a simple web server in Go that interprets `wasm` bytecode files

## Expected results

An interpreter that can interpret a `wasm` bytecode file containing the bytecode equivalent of:

```go
package main

func add(i, j int) int {
	return i+j
}

func main() {
	i := 42
	j := 666
	println("42+666=", add(i,j))
}
```

## Requirements

Go language, git.

## Mentors
  * [Sebastien Binet](mailto:binet@cern.ch)
  * [Alexandre Claude](mailto:alexandre.claude@clermont.in2p3.fr)

## Links
  * [Go](https://golang.org)
  * [WebAssembly](http://webassembly.org)
  * [WebAssembly bytecode specifications](http://webassembly.org/docs/binary-encoding/)
  * [Writing a python interpreter](http://www.aosabook.org/en/500L/a-python-interpreter-written-in-python.html)
  * [Writing an interpreter in Go](https://interpreterbook.com)
  * [go-interpreter community](https://github.com/go-interpreter)
