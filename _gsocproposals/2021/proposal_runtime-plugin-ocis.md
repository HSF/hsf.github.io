---
project: CERNBox
title: Runtime plugin ecosystem support for OCIS
layout: gsoc_proposal
year: 2021
organization:
  - CERN
  - AARNet
  - ownCloud
---

## Description

[CERNBox](https://cernbox.web.cern.ch/cernbox/) is a sync and share collaborative cloud storage solution at CERN used by more than 37K users and storing over 12PB of data. [CloudStor](https://www.aarnet.edu.au/network-and-services/cloud-services/cloudstor), developed by AARNET, provides the research community in Australia with collaboration workspaces and tools for sharing and analysing data. CERNBox and CloudStor are based on the ownCloud open source software, who recently launched their new flagship product codenamed [oCIS](https://owncloud.github.io/ocis/) (ownCloud Infinite Scale).

oCIS relies on the [Reva](https://reva.link/) middleware framework, originally developed at CERN to provide interoperability between storage and application providers through the [CS3APIs](https://cs3org.github.io/cs3apis/). Reva allows OCIS to connect to arbitrary storages and enable collaborative data services and applications by extending it with plugins.

While the addition of extensions and plugins to the existing ecosystem is trivially supported, the current mechanism requires to re-compile the source code whenever changes are made to generate the static binary. The aim of this project is to add runtime pluggability to the Reva framework to accelerate the development experience at AARNet, ownCloud and CERN for the integration of well-known applications (RootJS, FileSender, Jupyter notebooks, etc.) in the new platform.

## Task ideas

* Study and research what mechanisms various plugin systems implement and which one would be best suited to our use case. Some examples which can be considered include:
    * [Yaegi](https://github.com/traefik/yaegi), a Go interpreter
    * [go-plugin](https://github.com/hashicorp/go-plugin), connects plugins over GRPC
    * [Pie](https://github.com/natefinch/pie), supports protocol-independent RPCs
    * [Goloader](https://github.com/dearplain/goloader), a lightweight linker
    * Just use native Go plugins
* Study how runtime plugins are created and packaged in the chosen framework and document it.
* Complement the build-time plugins with runtime support using the chosen technology.
* Migrate an existing build-time plugin to the new runtime model.


## Expected results
We expect that, at the end of GSOC '21, plugins could be added to Reva at runtime just by pointing to the source of a Go module hosted as a version-controlled repository. Documentation of the process and the functionality for other developers is also expected.

### Requirements
* Go, GRPC, Protocol Buffers, Build systems

### Mentors
* **[Ishank Arora](mailto:ishank.arora@cern.ch)** CERNBox
* [Alex Unger](mailto:aunger@owncloud.com) ownCloud
* [Michael Usher](mailto:Michael.Usher@aarnet.edu.au) AARNet
* [Hugo Gonzalez Labrador](mailto:hugo.gonzalez.labrador@cern.ch) CERNBox

## Links
  * [CERBox project](https://cernbox.web.cern.ch)
  * [OCIS project](https://owncloud.github.io/ocis/)
  * [Reva project](https://reva.link/)

