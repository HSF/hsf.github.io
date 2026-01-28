---
title: AI-Assisted PostgreSQL Optimization Using EXPLAIN Plans
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
    is_preferred_contact: yes
---

## Description

The [nopayloaddb](https://github.com/BNLNPPS/nopayloaddb) project works as an implementation of the Conditions Database reference for the HSF. It provides a RESTful API for managing metadata objects (global tags). Our current system is composed of Nginx, Django, and database ([link to helm chart](https://github.com/BNLNPPS/nopayloaddb-charts)).

The project aims to implement an AI-assisted optimization framework for PostgreSQL queries without modifying existing tables or schemas. By leveraging EXPLAIN plans, temporary tables, and database-level optimization techniques, the system will identify and suggest improvements for slow or resource-intensive queries.

As a first step, a PostgreSQL cluster will be deployed on Kubernetes/OpenShift using a Helm chart, including persistent volumes and one read replica. The AI tool will analyze query plans and cluster metrics to suggest dynamic parameter adjustments to improve performance, enabling efficient query execution and better resource utilization without altering the underlying schema.

## Steps

1. Prepare a Helm chart for a PostgreSQL cluster on Kubernetes/OpenShift with PVs and one read replica   
2. Set up monitoring and metric collection for query performance and cluster health  
3. Collect EXPLAIN plans from slow and resource-intensive queries
4. Develop an AI-assisted engine to analyze query plans, identify bottlenecks, and suggest optimizations 
5. Implement dynamic tuning of PostgreSQL cluster parameters based on AI insights
6. Test AI-driven recommendations in a staging environment and validate performance improvements

## Expected Results

* Helm-based PostgreSQL cluster with PV and read replica ready for production
* AI-assisted query optimization based on EXPLAIN plans
* Dynamic cluster parameter adjustment guided by AI to maximize performance
* Improved query execution efficiency without modifying existing schemas

## Requirements

* Kubernetes, basic understanding, k8s, Helm, OpenShift
* Django and Nginx, basic understanding of web frameworks and logging
* Database knowledge, PostgreSQL, database replication

## Links

* Django REST API: <https://github.com/BNLNPPS/nopayloaddb> 
* Automized deployment with helm-chart: <https://github.com/BNLNPPS/nopayloaddb-charts>