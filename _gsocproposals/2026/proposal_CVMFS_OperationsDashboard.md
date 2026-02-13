---
title: Grafana Template for CernVM-FS Deployments
layout: gsoc_proposal
project: CernVM-FS
year: 2026
organization:
  - CERN
difficulty: medium
duration: 175
mentor_avail: June-October
project_mentors:
  - email: valentin.volkl@cern.ch
    first_name: Valentin
    last_name: Volkl
    organization: CERN
    is_preferred_contact: yes
  - email: jd@bnl.gov
    organization: BNL
    first_name: John S.
    last_name: De Stefano Jr.
  - email: caramarc@bnl.gov
    first_name: Costin
    last_name: Caramarcu
    organization: BNL
---

# Description

Particle physicists studying nature at the highest energy scales at the Large Hadron Collider rely on simulations and data processing for their experiments.
These workloads run on the "computing grid", a massive globally distributed computing infrastructure.
Deploying software efficiently and reliably to this grid is an important and challenging task.
CVMFS is an optimised shared file system developed specifically for this purpose: it is implemented as a POSIX read-only file system in user space (a FUSE module).
Files and directories are hosted on standard web servers and mounted in the universal namespace `/cvmfs`.
In many cases, it replaces package managers and shared software areas on cluster file systems as means to distribute the software used to process experiment data.

## Task idea

Monitoring is essential for any bigger CVMFS deployment - it can help with incidence response by showing problems at one glance as well  as with tuning configuration and performance.
Many different solutions to monitoring exist at different sites (see the lxplus dashboard below), but a centrally provided template could save time and effort for all operators.
Last year a centrally maintained prometheus exporter was created for metrics relevant to the CVMFS client, but there is still no centrally maintained dashboard template.
The main objective of this project will be to add a generic one that can be a good starting point for new CVMFS deployments. Besides the grafana dashboard, the prometheus exporter can also be an objective, reviewing metrics for relevance and improving performance, and possibly integrate also CVMFS server metrics and publication statistics.
Finally, easy-to-use deployment recipes (helm charts, ansible playbooks ...) for newcomers could be a stretch goal for this project.

## Expected results and milestones

 * Familiarisation with CVMFS and the metrics in the prometheus exporter
 * **Creation of a grafana dashboard template**
 * Surveying site operators and stakeholders for their requirements
 * Review of metrics in the prometheus exporter, speeding up collection
 * Addition of server/publication metrics
 * Creation of deployment recipes (ansible, k8s ...) 


## Requirements

 * Experience with Monitoring, in particular Prometheus/VictoriaMetris and Grafana


## How to apply

Once CERN/HSF is accepted as a GSoC org, please write an email with a short introduction to your interests and background to the mentors with the string "gsoc26" in the subject.
There will be a small evaluation task that we will mail to you then.


## Links

 * [CernVM-FS](https://cernvm.cern.ch/fs/)
 * <https://github.com/cvmfs-contrib/prometheus-cvmfs>
 * [Existing Dashboard for Lxplus (may require login)](https://monit-grafana.cern.ch/d/BPx0HuWMk/cvmfs?orgId=2)
