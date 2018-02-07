---
title: WLCG Lightweight Site Orchestration
layout: gsoc_proposal
project: WLCG
year: 2018
organization:
  - CERN
---

## Description

The Worldwide LHC Computing Grid (WLCG) unites resources from over 160 computing centres and research institutes spread across the world and the number is expected to grow in the coming years. However, provisioning resources (compute, network, storage) at new sites to support WLCG workloads is still no straightforward task and often requires significant assistance from WLCG experts. Recently, the WLCG community has initiated steps towards reducing such overheads through the use of prefab Docker containers or OpenStack VM images, along with the adoption of popular tools like Puppet for configuration. In 2017, the Lightweight Sites project was initiated to construct shared community repositories providing such building blocks. These repositories are governed by a single Lightweight Site Specification Document which describes a modular way to define site components such as Batch Systems, Compute Elements, Worker Nodes, Networks etc. In an agile process we further develop the specifications while implementing, analysing and improving upon the latest revision. Through this project, in broad terms, the GSoC participant can expect to work on: 
- Implementation of the specification using popular orchestration technologies (Docker Swarm, Kubernetes)
- Identifying parameters for benchmarking and evaluating the performance of different implementations. 
- Improving the specification based on outcomes of the implementations.


## Task ideas and expected results

* Set up a lightweight site using different orchestration technologies (Docker Swarm, Kubernetes, OpenStack Magnum). 
* Analyse the performance of the cluster of containers and design tests to benchmark various performance metrics of clusters related to Disk I/O, Network, Compute resource utilization on the bare metal/ hypervisor. 



**Requirements**

* Experience with creating containers with Docker. Familiarity with advanced concepts such as overlay networks, storage drivers, container memory management etc. is a plus.
* Experience with orchestration technologies like Docker Swarm/ Kubernetes/ OpenStack.
* Strong Linux fundamentals.
* Familiarity with fundamentals of Grid Computing, role of Compute Elements, batch systems, schedulers, Worker Nodes and related middleware.


**Mentors**
* [Mayank Sharma](mailto:mayank.sharma@cern.ch?subject=GSoC-LWSite) (Primary mentor)
* [Maarten Litmaath](mailto:maarten.litmaath@cern.ch?subject=GSoC-LWSite) (Co-mentor)



**Links**:
* [WLCG](http://wlcg.web.cern.ch)
* [Git Repositories](https://github.com/WLCG-Lightweight-Sites)
* [Introduction to WLCG](http://litmaath.web.cern.ch/litmaath/grids-intro/wlcg-intro-180130-long.pdf)
* [Introduction to WLCG Lightweight Sites](https://indico.jinr.ru/contributionDisplay.py?contribId=219&confId=151)
