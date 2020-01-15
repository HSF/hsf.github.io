---
title: Python Components for the SIMPLE Grid Framework
layout: gsoc_proposal
project: WLCG
year: 2019
organization:
  - CERN
---

## Description

The Worldwide LHC Computing Grid (WLCG) unites resources from over 160 computing centres and research institutes spread across the world and the number is expected to grow in the coming years. However, provisioning resources (compute, network, storage) at new sites to support WLCG workloads is still no straightforward task and often requires significant assistance from WLCG experts. Recently, the WLCG community has initiated steps towards reducing such overheads, for example, through the use of prefab Docker containers or OpenStack VM images, along with the adoption of popular tools like Puppet for configuration. In 2017, the SIMPLE Grid project was initiated to construct shared community repositories providing such building blocks. These repositories are governed by a single SIMPLE Framework Specification Document which describes a modular way to define site components such as Batch Systems, Compute Elements, Worker Nodes, Networks etc

The SIMPLE Grid project is an extension of the SIMPLE Framework that combines popular configuration management technologies such as Puppet/Ansible and container orchestration technologies such as Docker Swarm/Kubernetes to allow deployment of complex computing clusters using a single site level configuration file. The various components of the framework and their functions are described in the SIMPLE specification document. Two of the core components written in Python are: SIMPLE Grid YAML Compiler and SIMPLE Grid Validation Engine.   



## Task ideas and expected results

* Through this project, in broad terms, the student participant can expect to improve the python based framework components through the following tasks :
Configuration Validation: The configuration validation engine builds on top of a Yamale schema validator. Its main objective is to validate the YAML based schemas of the following two components of the SIMPLE framework:
    * Site Level Configuration File
    * Component repositories

  The Site Level Configuration File is currently constructed without a well defined schema. Therefore,  a Yamale based schema needs to be defined for it. This would require definition of custom data types used by the framework. These data types will be discussed before the start of the project and most of them can be inferred from the framework’s specification document. The schemas for component repositories are present in the respective config-schema.yaml files, which need to be appropriately translated to be able to use the Yamale module. 

* Infrastructure Validation: Once the framework has configured the distributed computing infrastructure, the validation engine needs to ensure that all the services, containers and configuration files are in their expected state. Popular python frameworks such as TestInfra can be used for that.

* Testing the YAML compiler: The YAML compiler takes the site level configuration file as input and performs several operations to generate an augmented version of the site level configuration file. This augmented file is then used by other components of the SIMPLE framework to configure the distributed cluster of resources. The compiler builds on top of PyYaml and adds two new keywords, namely __include__ and __from__, which are described in the resources listed below. It downloads the component repositories to utilize their meta-info.yaml, config-schema.yaml and default-data.yaml files. While the functionality has been manually tested to work, we need to put proper unit tests and integration tests in place to ensure that the future enhancements do not break the existing features of the compiler. Popular python frameworks such as PyTest, Hypothesis and Tox are going to be used for that.

A more consolidated set of tasks is as follows:
* Define a schema for site-level configuration file.
* Validate the schema for existing site level configuration files by implementing the functionality in the validation engine.
* Define custom data types of the SIMPLE framework for the yamale python package.
* Extract expected configuration of the computing cluster from the site level configuration file and use TestInfra to validate the deployment achieved by the SIMPLE grid framework.
* Write unit tests and integration tests for the YAML compiler using PyTest, Hypothesis and Tox. Improve the existing functionality for the tests that fail. 


**Requirements**

* Familiarity and prior experience with Python.
* Fundamentals of software testing.
* Git/Agile development methodology.
* Familiarity with configuration management tools like Ansible/Puppet, and/or container orchestration technologies like Docker, Docker Swarm is a plus.


**Mentors**
* [Mayank Sharma](mailto:mayank.sharma@cern.ch?subject=GSoC-LWSite) (Primary mentor)
* [Maarten Litmaath](mailto:maarten.litmaath@cern.ch?subject=GSoC-LWSite) (Co-mentor)



**Links**:
* [Lightweight Sites Web Forum (request membership)](https://groups.google.com/forum/#!forum/wlcg-lightweight-sites)
* [Next Steps](https://groups.google.com/forum/#!category-topic/wlcg-lightweight-sites/gsoc/W45nOZtA98I)
* [Git Repositories](https://github.com/WLCG-Lightweight-Sites)
* [Introduction to SIMPLE Grid Framework](https://speakerdeck.com/maany/the-simple-framework-deploy-complex-clusters-with-ease)
* [SIMPLE Grid Project  : CHEP 2018 Conference Proceedings paper](https://cernbox.cern.ch/index.php/s/OCqVQ55Q3bjzs7x)
* [SIMPLE Grid Specification Document (Early draft)](https://docs.google.com/document/d/1yp_96UXcwNO49cktnHtT61iNmTO0RgrSQukuNYqACpM/edit#heading=h.3etse5r12l7p)
* [WLCG](http://wlcg.web.cern.ch/)
* [Introduction to WLCG](http://litmaath.web.cern.ch/litmaath/grids-intro/WLCG-intro-2019-v4.pdf)
* [Introduction to WLCG Lightweight Sites](https://indico.jinr.ru/contributionDisplay.py?contribId=219&confId=151)

