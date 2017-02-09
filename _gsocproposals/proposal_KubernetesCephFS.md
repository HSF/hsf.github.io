---
title: Kubernetes CephFS driver using FUSE
layout: gsoc_proposal
project: Kubernetes
organization: CERN
---

## Description

[Kubernetes](http://kubernetes.io) is an open-source system for automating deployment, scaling, and management of containerized applications. It groups containers making up logical units for easy management and discovery. Usage at CERN has been increasing, with tens of clusters deployed covering multiple use cases from data analysis to infrastructure services.

This project aims at improving the integration between Kubernetes and [CephFS](http://ceph.com). CEPH is a popular multi-purpose storage solution, used at CERN for many years as the backend for block storage in the OpenStack deployment. It provides in addition a distributed filesystem, which recently became production ready. Kubernetes has a CephFS driver based on the CEPH kernel client, which lacks some important features and often lags behind compared to the FUSE client implementation.

## Task ideas

 * Reimplement the CephFS Kubernetes volume driver using the FUSE client
 * Add support for SELinux
 * Add support for functionality currently not available:
  * Quotas
  * Capacity
 * Test the new driver against OpenStack Manila shares, backed by CephFS at CERN
 * Develop any missing OpenStack Manila functionality for proper integration with the new driver
 * Perform and report large scale performance tests, using the CERN OpenStack infrastructure

## Expected results

Ready to use Kubernetes CephFS volume driver based on the FUSE client, scalable to thousands of concurrent clients.

## Requirements

Golang, Python

## Mentors 
  * [Ricardo Rocha](mailto:ricardo.rocha@cern.ch)
  * [Spyridon Trigazis](mailto:spyridon.trigazis@cern.ch)

## Links
  * [Kubernetes](http://kubernetes.io)
  * [Ceph](https://ceph.com)
  * [OpenStack Manila](https://wiki.openstack.org/wiki/Manila)
