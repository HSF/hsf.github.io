---
title: Native desktop integration for Exascale LHC Data Management
layout: gsoc_proposal
project: Rucio
year: 2020
organization:
    - CERN
    - UWuppertal
	- INFN
---

## Description

Rucio is an open-source software framework that provides functionality to scientific collaborations to organize, manage, monitor, and access their distributed data and dataflows across heterogeneous infrastructures. Rucio was originally developed to meet the requirements of the high-energy physics experiment ATLAS, and is continuously enhanced to support diverse scientific communities. In 2019 Rucio orchestrated multiple Exabytes of data access and data transfers globally. With this project we seek to enhance the daily user experience for scientists, such that they can interact with the data managed by Rucio natively from their desktops, as many are familiar with tools like Dropbox.

## Task ideas

The tasks are as follows:
 * A native GUI desktop application for Linux, which can rest in the user's taskbar/systray
 * Support for scoped namespace browsing
 * View file metadata, such as system-internal ones, as well as user-defined ones
 * Download of files via drag and drop from the storage to the user's desktop
 * Upload of files via drag and drop from the user's desktop to the storage
 * Desktop notification of events, e.g., finished transfers
 * Optionally support a cross-platform application from the same codebase (Windows, macOS)

## Requirements

 * Mandatory
  * C99 or newer, or C++14 or newer
  * Python 3
  * Linux, Git, and Docker
 * Basic understanding
  * Cross-platform windowing libraries (e.g., GTK+, Qt, wxWidgets)
  * FUSE-compliant filesystems
  * HTTP REST APIs
  * Token-based authentication
 * Optional for MacOSX
  * Objective-C, Cocoa

## Expected results

By the end of GSoC'20 we are looking to have a fully working desktop application that runs under common Linux desktop environments. We are aware that low latency and high throughput might not be achieved during GSoC due to the scale of the namespace and data, as that requires long-term performance optimisations. As a stretch goal, cross-platform compatibility with Windows and macOS would be very useful.

## Mentors
 * [Mario Lassnig](mailto:mario.lassnig@cern.ch)
 * [Thomas Beermann](mailto:thomas.beermann@cern.ch)
 * [Gabriele Gaetano Fronzé](mailto:gabriele.gaetano.fronze@cern.ch)

## Links
 1. [Rucio GitHub](https://github.com/rucio/rucio)
 2. [Journal article](https://doi.org/10.1007/s41781-019-0026-3)
