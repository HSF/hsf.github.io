---
title: Efficient storage of versioned ROOT files in a git repository
layout: gsoc_proposal
project: ROOT
year: 2018
organization: CERN
---

# Description

Physicists have often the need to store ROOT files inside a git repository,
mostly to be able to have them versioned and for the convenience of having
them shipped together with the source.

However given the fact that git treats files as an atomic units and due to the
common "compressed blob" look ROOT files, this can result in extremely
large git repositories because git is unable to further aggregate and compress
them, even if their uncompressed versions differ very little one from the other.

The aim of the project is to provide a tool to convert ROOT files in a form
which is suitable for being stored in a git repository using the object store
model of git as a way to store separate, uncompressed `TKey`s, ROOT smallest
storage unit inside a file. Under the assumption people tend to store in a git
repository ROOT files which have only a small fraction of the `TKey`s
significantly changing, this should allow git to efficiently group and compress
similar entries, possibly resulting in much more compact repositories than the
one resulting from the naive file by file approach.

# Tasks

The project is divided in four parts:

* Have an helper function which allows to stream ROOT files to a git blob
  store.
* Have an helper function which allows creating a ROOT file from a git blob
  store.
* Profile the speed required for doing the above and the scalability of the
  storage in terms of size.
* Provide a native API which allows to retrieve deserialised object,
  rather than ROOT files.

# Possible extensions

A natural extension of this work, if the student has a Windows machine
available, is to study the interplay with [Microsoft's GVFS](https://gvfs.io).

# Mentors

* Giulio Eulisse (CERN - ALICE)
* Danilo Piparo (CERN - ROOT)

# Links

* [Git object model](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)
* [ROOT TFile Format](https://root.cern.ch/doc/master/classTFile.html)
