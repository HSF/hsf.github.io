---
title: Intelligent Log Analysis for the HSF Conditions Database
layout: gsoc_proposal
project: HSFCondDB
year: 2025
difficulty: medium
duration: 350
mentor_avail: June-October
organization:
  - BNL
project_mentors:
  - email: mashinistov@bnl.gov
    organization: BNL
    first_name: Ruslan
    last_name: Mashinistov
  - email: jd@bnl.gov
    organization: BNL
    first_name: John S.
    last_name: De Stefano Jr.
  - email: mhernande1@bnl.gov
    organization: BNL
    first_name: Michel
    last_name: Hernandez Villanueva
---

## Description

The [nopayloaddb](https://github.com/BNLNPPS/nopayloaddb) project works as an implementation of the Conditions Database 
reference for the HSF. It provides a RESTful API for managing payloads, global tags, payload types, and associated data. 

Our current system, composed of Nginx, Django, and database ([link to helm chart](https://github.com/BNLNPPS/nopayloaddb-charts)), 
lacks a centralized logging solution making it difficult to effectively monitor and troubleshoot issues. 
This task will address this deficiency by implementing a centralized logging system aggregating logs from multiple 
components, and develop a machine learning model to perform intelligent log analysis.  The model will identify unusual 
log entries indicative of software bugs, database bottlenecks, or other performance issues, allowing us to address 
problems before they escalate. Additionally, by analyzing system metrics, the model will provide insights for an optimal 
adjustment of parameters during periods of increased request rates.

## Steps

1. Set up a centralized logging system   
2. Collect and structure logs from Nginx, Django, and the database  
3. Develop an ML model for log grouping and anomaly detection 
4. Implement Kubernetes-based database with replication 
5. Train an ML model to optimize Kubernetes parameters dynamically


## Expected Results

* A centralized logging system for improved monitoring and troubleshooting 
* ML-powered anomaly detection
* ML-driven dynamic configuration for optimal performance

## Requirements

* Python and basic understanding of ML frameworks
* Kubernetes, basic understanding, k8s, Helm, Operators, OpenShift
* Django and Nginx, basic understanding of web frameworks and logging
* Database knowledge, PostgreSQL, database replication


## Links

* Django REST API: <https://github.com/BNLNPPS/nopayloaddb> 
* Automized deployment with helm-chart: <https://github.com/BNLNPPS/nopayloaddb-charts>
