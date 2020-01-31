---
title: Kubernetes operator for XRootD
layout: gsoc_proposal
project: XRootD
year: 2020
organization:
  - CC-IN2P3
  - LPC-Clermont
  - SLAC
---
## Description

[Kubernetes](https://kubernetes.io/) is an open-source system for automating deployment, scaling, and management of containerized applications.

A [Kubernetes Operator](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) is an abstraction for deploying non-trivial applications on Kubernetes. The Operator pattern aims to capture the key aim of a human operator who is managing a service or set of services. Indeed, human operators who look after specific applications and services have deep knowledge of how the system ought to behave, how to deploy it, and how to react if there are problems.

At CERN, the vast majority of physics and infrastructure data reside in a system named EOS. [EOS](https://eos.web.cern.ch/) is a disk-based, low-latency storage service with a highly scalable hierarchical namespace, which enables data access via the [XRootD protocol](http://xrootd.org/). The [XRootD protocol](http://xrootd.org/) is also used by the [Large Synoptic Survey Telescope data management team](https://www.lsst.org/about/dm) in order to build a system for user query access, called [QServ](https://github.com/lsst/qserv), which will store galaxies and stars catalogs and that will ultimately contain trillions of rows and petabytes of data.

This project aims to develop a Kubernetes Operator for XRootD in order to ease and fully automate deployment and management of XRootD clusters. This Operator targets the whole field of existing infrastructure where XRootD can run: development workstations, continous integration platforms, bare-metal clusters in academic datacenters, and also public cloud platforms.

## Task ideas

 * Provide an **XRootD operator**, which will demonstrate how to deploy and manage an XRootD service at scale, using Kubernetes.
 * Implement Kubernetes operator's advanced features like **seamless upgrades**, **full lifecycle**, **deep insights** and **auto-pilot**.
 * Explain to the **XRootD community** and in peculiar, to the XRootD system administrators, how to leverage this  Kubernetes Operator in order to ease and scale up worlwide XRootD clusters management.

## Expected results

A production-ready operator for XRootD, enabling at least **Basic Install** and **Seamless Upgrades** features, and its related documentation.

## Requirements
[Go](https://golang.org), Shell scripting, [Kubernetes](https://kubernetes.io/), C++

## Mentors
  * [Yvan Calas](mailto:yvan.calas@cc.in2p3.fr)
  * [Andrew Hanushevsky](mailto:abh@slac.stanford.edu)
  * [Fabrice Jammes](mailto:fabrice.jammes@in2p3.fr)
  
## Links
  * [Operator framework](https://github.com/operator-framework)
  * [OperatorHub.io](https://operatorhub.io)
  * [Qserv Operator](https://github.com/lsst/qserv-operator)
