---
title: Optimise calls in the Ceph RADOS Striper API to enable efficient concurrent access to read-only objects.
layout: gsoc_proposal
project: Ceph
year: 2020
organization:
  - RAL
  - uglasgow
---

## Description

Ceph is a scalable, self-healing, open source object storage solution used in many commercial organisations, and in academia and research. Examples of the latter include CERN, NASA, and the MeerKAT radio telescope, as well as the UK’s Rutherford Appleton Laboratory (RAL). RAL stores 25 petabytes of data originating from the CERN Large Hadron Collider in a Ceph cluster called Echo.  Data in Echo is being read at a rate of 20 - 50GB/s by analysis jobs at RAL and around the world. 

The software running on analysis clusters only needs to read object data from Echo. There are often many tens of read clients accessing a data object at the same time; to enable more efficient use of Echo in this manner, RAL are proposing a way to optimise read-only data access in Ceph. This would also increase the productivity of analysis workflows accessing this experimental data,

The underlying access layer used for ECHO is called libradosstriper. This C++ library allows efficient striping of objects over disks in a Ceph cluster to improve data distribution and throughput. Libradosstriper read operations currently require a write lock to be placed on the first stripe of an object (which contains metadata) to prevent modifications by other clients during the read. This is unnecessary for read-only access, and for ‘hot’ objects (those in use by many clients), this can become a bottleneck. A non-locking read would drastically reduce the number of metadata operations needed for striper reads, reduce the latency of these operations, and enable a higher throughput for reading data.

## Task ideas
* Devise a multiple-read microbenchmark representing the access pattern we wish to optimise - multiple, read-only access
* Deploy microbenchmark to record statistics (e.g. open() latency, etc) with the current libradosstriper API to obtain the baseline performance figures we wish to improve on
* Design an improved open() call which doesn’t create a write lock
* Test new version of libradosstriper with the multiple-read microbenchmark to show changes in performance, and show no negative effects have been introduced

## Expected results
A revised version of the libradosstriper API which optimises concurrent read-only accesses to an object.  A microbenchmark which can record statistics relating to read-only access to data objects.

## Requirements
* Essential: C++, Distributed system or client-server programming
* Useful: Object storage orientation

## Mentors
  * [Alastair Dewhurst](mailto:alastair.dewhurst@stfc.ac.uk)
  * [Ian Johnson](mailto:ian.johnson@stfc.ac.uk)
  * [Tom Byrne](mailto:tom.byrne@stfc.ac.uk)
  * [Sam Skipsey](mailto:samuel.skipsey@glasgow.ac.uk)
