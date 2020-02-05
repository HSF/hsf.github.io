---
title: Health Checks and Monitoring Dashboard for ScienceBox
project: SWAN
layout: gsoc_proposal
year: 2020
organization: CERN
---

## Description

[ScienceBox](https://sciencebox.web.cern.ch/) is a comprehensive set of services for cloud storage and computing applications suitable for both general-purpose use cases and advanced scientific scenarios.
It provides [EOS](https://eos.web.cern.ch/), the CERN software for massive distributed storage in the cloud, [CERNBox](http://cernbox.web.cern.ch), the cloud storage, synchronization and sharing service for science, and [SWAN](https://swan.web.cern.ch), a fully-fledged interactive data analysis platform accessible from a web browser.
ScienceBox is available in two flavors:
1) A one-click setup for demonstration purposes running on a single machine with docker-compose, and
2) A production-oriented deployment with the ability to scale out according to storage and computing needs based on Kubernetes.


## Task ideas

This project focuses on:
  * Implementing health checks for ScienceBox services running in containers. This ranges from basic probing (e.g., check network sockets/running processes, issue HTTP requests) to the development of custom scripts for functional tests verifying the expected behavior of services.
  * Managing application-level logs through sidecar containers running log parsing and ingestion agents (e.g., [Apache Flume](https://flume.apache.org/)). Ingested metrics should be collected on a centralized storage backend (e.g., [Elastic Search](https://www.elastic.co/products/elasticsearch) or [InfluxDB](https://www.influxdata.com/products/influxdb-overview/)).
  * Exploring collected metrics interactively (e.g., via [Timber](https://timber.io/) or [Kibana] (https://www.elastic.co/products/kibana)) and creating visualization dashboards (e.g., time-series, heatmaps in [Grafana] (https://grafana.com/) for ScienceBox administrators
  * Complementing the set of containers provided by ScienceBox with the ones requires for log ingestion, storage, and processing/visualization.

It is encouraged to re-use widely adopted technologies as much as possible.


## Expected results
  * A working implementation of health-checks and sidecar containers for log ingestions.
  * An updated version of ScienceBox with additional containers required to run dedicated services for log inspection and visualization.

## Requirements
  * Python, Shell scripting
  * Basic understanding of file systems, HTTP protocol, and process monitoring
  * Experience with Docker containers and Kubernetes
  * Experience with Helm charts is a plus

## Mentors
  * [Enrico Bocchi](mailto:enrico.bocchi@cern.ch)
  * [Diogo Castro](mailto:diogo.castro@cern.ch)

## Links
  * [SWAN](https://swan.web.cern.ch/)
  * [ScienceBox](https://sciencebox.web.cern.ch/)
