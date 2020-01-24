---
title: Intelligent Alert Management System For HEP experiments
layout: gsoc_proposal
project: Monitoring
year: 2020
organization: CERN
---

## Description

We would like to build an intelligent Alert Management System for HEP experiments.
It should embrace existing open-source solutions based on Prometheus and AlertManager
to select alerts from various sub-systems and reduce amount
of non-relevant alerts. The system should be able to correlate alerts from
CERN MONIT infrastructure based on ElasticSearch, Kafka, Grafana stack, GGUS WLCG, and
Prometheus, AlertManager, VictoriaMetrics software components used in HEP experiments.

The system should collect various alerts from ES, InfluxDB, Prometheus data-sources,
GGUS system and be able to aggregate, and create meaningful alerts to address
various sub-system failures. For instance, if GRID site has experience a problem
in terms of its storage the new system should notify via appropriate channels
a set of instructions how to fix and handle this situation.

We foresee that some sort of ML/AI tools may be required to identify (cluster)
certain problems as well as apply various statistical tools to identify
the anomalies and their recoveries.

We're seeking a candidate proficient in Go and Python languages.

## Task ideas
 * Implement `vmalert` for VictoriaMetrics backend
 * Implement parser for GGUS WLCG alert system and inject GGUS states into VictoriaMetrics
 * Implement a common kubernetes infrastructure among various participant software components
 * Write common alert manager logging system with ability to analyze incoming alerts
   * apply ML/AI models to alerts
   * write template based notifications
 * Write aggregated layer of various alerts
 * Perform tests with real alerts coming from CERN experiments (ATLAS, CMS, etc.)

## Expected results
Working implementation of intelligent Alert system for CMS experiment.

## Requirements
Go, Python languages, be familiar with ElasticSearch, Prometheus, InfluxDB, Grafana,
AlertManager and similar monitoring tools. Knowledge of kubernetes is a plus.

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
