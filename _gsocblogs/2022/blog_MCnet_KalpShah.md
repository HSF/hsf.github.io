---
project: MCnet
title: Dataset-manipulation tools for simulated collider events
author: Kalp Shah
date: 9.08.2022
year: 2022
layout: blog_post
logo: UGlasgow-logo.png
intro:
  A software package that provides tools for manipulation of HEP specific
  datasets
---

## Introduction

This project aims to make the process of performing any form of modification to
the simulated collider events a much simpler one. Examples of such changes
include slicing, converting, merging, splitting, and any combination of such
processes.

The scope of the project changed during the middle, and implementation of a
pileup tool was added to it. It is a tool that generates signal events
superimposed with min-bias events, resulting in an event-generator-level
approximation to the presence of pileup in high-luminosity collisions.

## Work Done

It was decided to split the modification toolkit as a collection of small python
programs that perform a particular task which can then be used together for
performing a combination type process. Till the mid-evaluation, the functions
that are implemented are the following :

- Conversion of file formats
- Slicing out the top n events from a HepMC3 file, equivalent to the `head`
  command
- Slicing out the top n events from a HepMC3 file, equivalent to the `tail`
  command
- Cutting out any range of particles from a HepMC3 file
- Merging of different HepMC3 files to a single file

On the other hand, progress on the pile up tool was made. The tool is called
pilemc which was previously a C++ tool last updated in 2015.

The pilemc code is written in python, which allows for adding pileup to a signal
file. The following feaures were implemented :

- A memory efficient event finder is used which first seeks the event and then
  sends the event to the main pilemc code
- As the event has to be composed using the signal vertex and particles combined
  with the pile-up vertex and particles. Thus, a custom event composer is
  required which combines them into a single event which can then be added to
  the output file

## Links

The event manipulation tools are present in the bin folder of the
[MCutils repository](https://gitlab.com/hepcedar/mcutils/-/tree/manip-tools/)

The codes for pilemc are present [here](https://gitlab.com/hepcedar/pilemc)
