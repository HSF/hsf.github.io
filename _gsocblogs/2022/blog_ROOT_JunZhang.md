---
project: ROOT
title: Optimize ROOT use of modules for large codebases
author: Jun Zhang
date: 25.07.2022
year: 2022
layout: blog_post
logo: ROOT-logo.png
intro: |
  A short progress report about how we optimize memory footprint using clang modules.
---

## Introduction

Hello everyone! My name's Jun and I'm so glad to be here as a Google Summer of Code student this year! This is a short report about the progress of my project and I hope you like it! Before we diving into my work, I would like to give you a brief introduction about what my project intends to do:

In very large C++ projects, redundant header parsing greatly slows down the compilation process (This is even worse for ROOT because we have to parse source code at runtime). To solve this issue, we have adopted Clang modules in ROOT, which alleviates the problem to some extent. However, the current module integration also has its limitations. For example, one source of performance loss is the need for symbol lookups across a very large set of modules. So my project this year is aiming to eliminate the unnecessary lookup for identifiers like a namespace to reduce memory pressure.

## Current Work

The first thing I need to do is to understand the related logic. After a deep discussion with my mentor and a long time reading source code, I submit my first [PR](https://github.com/root-project/root/pull/10910) against ROOT repo and passed the whole test suite. I have done some basic tests locally and confirmed that it does decrease the max memory usage to some extent. However, this is not enough and we need to test it in a more large-scale scenario.

## Future Direction

The next step is to verify how large an impact our work has made especially in a bigger project (for example CMSSW). I have applied to a CMSSW external account and will do deeper profiling after I'm granted CMSSW resources. Another issue we need to solve is that the current approach only works for top-level namespaces and we need to do more to make it work for all-level namespaces. When all of these are done, we'll also try to upstream our work to LLVM main repo.

## Summary

This is my first time participating in the open source community this deeply. It has been a wonderful experience for me and I have learned a lot from it. I would like to give my most sincere thanks to those who helped me here.

If you get this far, thanks for reading! See you next month!

~jun

:wq
