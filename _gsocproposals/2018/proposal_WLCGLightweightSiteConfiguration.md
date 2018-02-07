---
title: WLCG Lightweight Site Configuration
layout: gsoc_proposal
project: WLCG
year: 2018
organization:
  - CERN
---

## Description

The Worldwide LHC Computing Grid (WLCG) unites resources from over 160 computing centres and research institutes spread across the world and the number is expected to grow in the coming years. However, provisioning resources (compute, network, storage) at new sites to support WLCG workloads is still no straightforward task and often requires significant assistance from WLCG experts. Recently, the WLCG community has initiated steps towards reducing such overheads through the use of prefab Docker containers or OpenStack VM images, along with the adoption of popular tools like Puppet for configuration. In 2017, the Lightweight Sites project was initiated to construct shared community repositories providing such building blocks. These repositories are governed by a single Lightweight Site Specification Document which describes a modular way to define site components such as Batch Systems, Compute Elements, Worker Nodes, Networks etc. In an agile process we further develop the specifications while implementing, analysing and improving upon the latest revision. Through this project, in broad terms, the GSoC participant can expect to work on: 
- Implementation of the specification using popular orchestration technologies (Docker Swarm, Kubernetes) and configuration management tools (Puppet, Ansible, Chef) .
- Identifying parameters for benchmarking and evaluating the performance of different implementations. 
- Improving the specification based on outcomes of the implementations.


## Task ideas and expected results

* Implement configuration of CREAM Computing Element, TORQUE Batch Service and Worker Node containers (Docker) using Ansible (from existing Puppet/YAIM Implementations). 
* Improve the existing Puppet implementation of these service components.

**Requirements**

* Experience with creating Puppet modules/Ansible playbooks.
* Experience with other configuration management tools like Chef/ SaltStack is a plus. 
* Strong Linux fundamentals and shell scripting expertise.
* ITSM experience is not required, but preferred.



**Mentors**
* [Mayank Sharma](mailto:mayank.sharma@cern.ch?subject=GSoC-LWSite) (Primary mentor)
* [Maarten Litmaath](mailto:maarten.litmaath@cern.ch?subject=GSoC-LWSite) (Co-mentor)



**Links**:
  * [WLCG](http://wlcg.web.cern.ch)
  * [Git Repositories](https://github.com/WLCG-Lightweight-Sites)
  * [Introduction to WLCG](http://litmaath.web.cern.ch/litmaath/grids-intro/wlcg-intro-180130-long.pdf)
  * [Introduction to WLCG Lightweight Sites](https://indico.jinr.ru/contributionDisplay.py?contribId=219&confId=151)
  * [Puppet VM Learning Guide](https://puppet.com/download-learning-vm?_ga=1.75488720.375650118.1442481193)

