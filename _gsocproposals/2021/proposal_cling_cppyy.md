---
title: Improving Cling Reflection for Scripting Languages
layout: gsoc_proposal
project: IRIS-HEP
year: 2021
organization: princeton
---

## Description

Cling has basic facilities to make queries about the C++ code that it has
seen/collected so far. These lookups assume, however, that the caller knows
what it is looking for and the information returned, although exact, usually
only makes sense within C++ and is thus often too specific to be used as-is.

A scripting language, such as Python, that wants to make use of such lookups
by name, is forced to loop over all possible entities (classes, functions,
templates, enums, ...) to find a match. This is inefficient. Furthermore,
many lookups will be multi-stage: a function, but which overload? A template,
but which instantiation? A typedef, of what? The current mechanism forces the
scripting language to provide a type-based match, even where C++ makes
distinctions (e.g. pointer v.s. reference) that do not exist in the scripting
language. This, too, makes lookups very inefficient.

The returned information, once a match is found, is exact, but because of its
specificity, requires the caller to figure out C++ concepts that have no
meaning in the scripting language. E.g., there is no reason for Python to
consider an implicitly instantiated function template different from an
explicitly instantiated one.

## Task ideas and expected results

The project should start with a design C++ entities grouping that make sense
for scripting languages and design a query API on top of these. Special
consideration should be given to the various name aliasing mechanisms in C++
(e.g., `using` and `typedef`), especially as relates to C++ access rules.
This design can likely start from the existing Cling wrapper API from Cppyy
and modify it to improve consistency, remove redundancy, and enable usage
patterns that minimize lookups into Cling.

Next is a redesign of Cling's lookup facilities to support this new API
efficiently, with particular care to use cases that require multiple,
consecutive/related, lookups, such as finding a specific function template
instantiation, or step-wise resolution of a typedef.

This design is then to be implemented, using test-driven development. As a
stretch goal, the cppyy-backend should be modified to use the new API.

## Mentors
  * **[Wim Lavrijsen](mailto:wlavrijsen@lbl.gov)**
  * [Vassil Vassilev](mailto:vvasilev@cern.ch)

## Links
  * [cling](https://github.com/vgvassilev/cling)
  * [clang](http://clang.llvm.org/)
  * [llvm](http://llvm.org/)
  * [cppyy-backend](https://bitbucket.org/wlav/cppyy-backend/src/master/clingwrapper/src/)
