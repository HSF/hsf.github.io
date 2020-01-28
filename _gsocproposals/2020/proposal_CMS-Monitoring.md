---
title: Intelligent Alert Management System For HEP experiments
layout: gsoc_proposal
project: CMS
year: 2020
organization:
  - CERN
  - Cornell
  - INFN
---

## Description

The growth of distributed services introduces a challenge to properly monitor their status and reduce operational costs. In CMS experiment at CERN we deal with distributed computing infrastructure which includes central services for authentication, workload management, data management, databases, etc. To properly operate and maintain this infrastructure we rely on various open-source monitoring tools, including ElasticSearch, Kafka, Grafana stack (used by central CERN MONIT infrastructure), Prometheus, AlertManager, VictoriaMetrics software components (used by the experiment), as well as custom solutions like GGUS WLCG or ServiceNow ticketing systems.

On daily basis these CMS computing infrastructure may produce significant amount of information about various anomalies, intermittent problems, outages as well as undergo scheduled maintenance. Therefore the amount of alert notifications and tickets our operational teams should handle is very large.  We're working towards, an Operational Intelligent System aiming to detect, analyse, and predict anomalies of the computing environment, to suggest possible actions, and ultimately automate operation procedures.  An important component of this system should be an intelligent Alert Management System.

The system should collect anomalies, notifications, etc., from ES, InfluxDB, Prometheus data-sources, GGUS system and be able to aggregate, and create meaningful alerts to address various computing infrastructure failures. For instance, if certain component of global distributed system experiences a problem in terms of its storage the Alert Management system should notify via appropriate channels a set of instructions on how to fix and handle this situation. Before sending the alert it should check if this is a real anomaly or part of on-going outage, or schedule maintenance.

We foresee that some sort of ML/AI tools may be required to identify and tag certain problems, as well as apply various statistical tools to identify the anomalies and their recoveries.

## Task ideas
 * Implement `vmalert` for VictoriaMetrics back-end
 * Implement parser for GGUS WLCG alert system and inject GGUS states into VictoriaMetrics
 * Write common alert manager logging system with ability to analyze incoming alerts
   * apply ML/AI models to alerts
   * write template based notifications
 * Write aggregated layer of various alerts
 * Deploy middleware components to Kubernetes infrastructure
 * Perform tests with real alerts coming from CERN experiments (ATLAS, CMS, etc.)

## Expected results
A student should implement an additional middleware (layers) on top of existing open-source solutions, e.g. `vmalert` for VictoriaMetrics, and be able to compose them into working implementation of intelligent Alert system for CMS experiment.  The system should be deployed to Kubernetes cluster as a set of loosely coupled components and/or micro-services.

## Requirements
We're seeking a candidate proficient in Go and Python languages, and be familiar with one or more open-source monitoring solutions like Prometheus, ElasticSearch, InfluxDB, Grafana, AlertManager and/or similar monitoring tools. Knowledge of Kubernetes is a plus.

## Mentors
  * [Valentin Kuznetsov](mailto:vkuznet@gmail.com)
  * [Federica Legger](mailto:federica.legger@to.infn.it)
  * [Christian Ariza](mailto:christian.ariza@gmail.com)

## Links
  * [Prometheus](https://prometheus.io/)
  * [AlertManager](https://prometheus.io/docs/alerting/alertmanager/)
  * [VictoriaMetrics](https://victoriametrics.com/)
  * [ElasticSearch](https://www.elastic.co/)
  * [Grafana](https://grafana.com/)
  * [GGUS](https://ggus.eu/)
