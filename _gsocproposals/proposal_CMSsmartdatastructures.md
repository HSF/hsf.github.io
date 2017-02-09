---
title: Smart data structures in CUDA
layout: gsoc_proposal
project: CMS
organization: CERN
---

## Description
The entire CMS event reconstruction is written in C++, configured in python enabling the use of dynamic data structures with high granularity. 
This feature is very useful because typical High-Energy Physics algorithms are fed with variable size inputs and produce outputs, whose size is many times impossible to estimate or generalize. 
The CMS software framework is going through a transition aimed at transforming it into a heterogeneous software framework, in order to profit of GPUs higher throughput and energy efficiency.
CUDA language is used to program NVIDIA GPUs and it is not dynamic-data-structures-friendly, since it was designed for working with data structures of predictable size.
Furthermore, allocating memory on a GPU has a fixed cost which is orders of magnitude higher than doing that on the host.

## Task ideas
 * Creation of a testbed for the creation and validation of STL-like data structures 
 * Design and implementation of arena allocators to allocate/resize/access a CUDA vector-of-vector
 * Implementation of GPU-friendly tree-like data structure
 * Smart allocators to preallocate memory and assign it to requesting functions, keeping track of the memory usage and reassigning it on demand.
 
## Expected results
Creation of a library containing the developed data structures

## Requirements
C++, CUDA

## Mentors 
  * [Felice Pantaleo](mailto:felice.pantaleo@cern.ch)
  * [Vincenzo Innocente](mailto:vincenzo.innocente@cern.ch)
  * [Marco Rovere](mailto:marco.rovere@cern.ch)
  * [Andrea Bocci](mailto:andrea.bocci@cern.ch)

