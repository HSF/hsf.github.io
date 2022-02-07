---
title: Creation and usage of disposable Spark on Kubernetes clusters from notebook service (SWAN) for distributed physics analysis
layout: gsoc_proposal
project: SWAN
year: 2019
organization: CERN
---

## Description

The Hadoop expands its user base for analysts who want to perform analysis with big data technologies - namely Apache Spark – with main users from accelerator operations and infrastructure monitoring. Hadoop Service integration with Jupyter notebook (SWAN) Service offers scalable interactive data analysis and visualizations using Jupyter notebooks, with spark computations being offloaded to compute clusters - on-premise YARN clusters and more recently to cloud-native Kubernetes clusters.

With the recent developments in ROOT framework - Distributed RDataFrame, there is a growing number of physicists who are performing analysis using Apache Spark and ROOT RDataFrame and more so on the clusters created and managed by them. This project will develop the necessary integrations to use such Spark on Kubernetes clusters from Jupyter notebook service (SWAN)

## Task ideas
* Creation of Kubernetes cluster on CERN Openstack magnum interface from Jupyter notebooks
* Initializing Spark services (e.g shuffle service, history server) on Kubernetes cluster with helm
* Initializing CERN services (e.g CVMFS) on Kubernetes cluster with helm
* Admin of the cluster to create user service accounts
* Development of web interface Jupyter plugin to attach the Kubernetes cluster to the Jupyter notebook (SWAN) based on user service account token

## Expected results
A Jupyter plugin to create, initialize and attach Kubernetes cluster from the notebooks

## Requirements
1. Python
2. JavaScript
3. Spark

## Mentors
  * [Prasanth Kothuri](mailto:prasanth.kothuri@cern.ch)
  * [Piotr Mrowczynski](mailto:piotr.mrowczynski@cern.ch)
  * [Enric Tejedor Saavedra](mailto:etejedor@cern.ch)
  * [Diogo Castro](mailto:diogo.castro@cern.ch)

## Links
  * [Jupyter](http://jupyter.org)
  * [Spark](http://spark.apache.org)
  * [Spark Summit talk](https://databricks.com/session/experience-of-running-spark-on-kubernetes-on-openstack-for-high-energy-physics-workloads)
